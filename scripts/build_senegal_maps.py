#!/usr/bin/env python3
"""
Regenerate the Senegal school maps shown on /datasets/.

One choropleth per school type, shaded by the number of schools in each
department. Output goes to assets/media/datasets/.

    python3 scripts/build_senegal_maps.py

SOURCE DATA (not in this repo - it is not openly published):

    /Users/perezp/Dropbox/Education and Marriage in Senegal/Data/School Census/
        primary school census.xlsx
        secondary school census.xlsx

WHY DEPARTMENT AND NOT COMMUNE

The census locates schools to commune, and commune would be the better unit,
but no boundary layer matches it well enough to map honestly:

    commune  vs GADM level 4 (433 shapes)   62.7% exact, 78% with fuzzy matching
    department vs geoBoundaries ADM2 (45)   100% of schools, with 5 aliases

GADM's level-4 layer has 433 communes against the census's 549 - Senegal's
communes were reorganised and the layers genuinely do not correspond, so a
commune map would silently drop a fifth of the schools. Department covers every
school. If a current commune layer turns up, switch UNIT below.

DESIGN NOTES

  * Sequential ramp: one hue, light to dark, lightness strictly decreasing
    (asserted at run time). Sequential encodes magnitude - never a rainbow.
  * One ABSOLUTE scale shared by all three panels, so they are comparable: the
    point is that secondary schools are far rarer than primary ones, and a
    per-panel rescale would hide exactly that.
  * Transparent background, labels in HTML, so one asset serves both themes.
  * Boundaries: geoBoundaries gbOpen SEN ADM2 (CC BY 3.0 IGO).
"""

import json
import os
import re
import subprocess
import sys
import unicodedata
import difflib

import pandas as pd
from PIL import Image, ImageDraw

SRC = "/Users/perezp/Dropbox/Education and Marriage in Senegal/Data/School Census"
OUT = "assets/media/datasets"
API = "https://www.geoboundaries.org/api/current/gbOpen/SEN/ADM2/"

WIDTH, SUPERSAMPLE = 840, 2
# Sequential ramp, light -> dark. Verified monotonic in OKLab L at run time.
RAMP = ["#ede9fe", "#c4b5fd", "#a78bfa", "#7c3aed", "#5b21b6"]
BREAKS = [50, 100, 200, 350]          # upper edges; 5 bins with the tail open
EMPTY = "#f4f4f5"

TYPES = [
    ("Petite enfance", "senegal-petite-enfance"),
    ("Primaire", "senegal-primaire"),
    ("Moyen & secondaire", "senegal-moyen-secondaire"),
]

PREFIX = re.compile(r"^(com|art|dpt|ia|ief|ville|cv)[\s.]+", re.I)
ALIAS = {
    "keurmassar": "pikine",              # split from Pikine in 2021, after the 2019 layer
    "malemhoddar": "malemhodar",
    "medinayorofoulah": "medinayoroufoula",
    "nioro": "niorodurip",
    "stlouis": "saintlouis",
}


def norm(s):
    s = PREFIX.sub("", str(s).strip())
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]", "", s.lower())


def oklab_l(hex_color):
    r, g, b = (int(hex_color[i:i + 2], 16) / 255 for i in (1, 3, 5))
    f = lambda c: c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = f(r), f(g), f(b)
    l = (0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b) ** (1 / 3)
    m = (0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b) ** (1 / 3)
    s = (0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b) ** (1 / 3)
    return 0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s


def boundaries(cache="/tmp/sen_adm2.geojson"):
    if not os.path.exists(cache):
        meta = json.loads(subprocess.run(["curl", "-fsSL", API], capture_output=True,
                                         text=True, check=True).stdout)
        meta = meta[0] if isinstance(meta, list) else meta
        url = meta.get("simplifiedGeometryGeoJSON") or meta["gjDownloadURL"]
        subprocess.run(["curl", "-fsSL", "-o", cache, url], check=True)
    return json.load(open(cache))


def main():
    lightness = [oklab_l(c) for c in RAMP]
    assert all(a > b for a, b in zip(lightness, lightness[1:])), \
        f"ramp lightness must decrease monotonically, got {[round(x,3) for x in lightness]}"

    geo = boundaries()
    shapes = {norm(f["properties"]["shapeName"]): f for f in geo["features"]}

    pri = pd.read_excel(f"{SRC}/primary school census.xlsx")
    sec = pd.read_excel(f"{SRC}/secondary school census.xlsx")
    pri["_type"] = pri["LIBELLE_TYPE_SYSTEME_ENSEIGNEMENT"].map(
        {"PETITE ENFANCE": "Petite enfance", "PRIMAIRE": "Primaire"})
    sec["_type"] = "Moyen & secondaire"
    cen = pd.concat([pri, sec])

    def to_shape(v):
        n = ALIAS.get(norm(v), norm(v))
        if n in shapes:
            return n
        hit = difflib.get_close_matches(n, list(shapes), n=1, cutoff=0.85)
        return hit[0] if hit else None

    cen["_dept"] = cen["DEPARTEMENT"].map(to_shape)
    unmatched = cen["_dept"].isna().sum()
    print(f"{len(cen):,} schools, {unmatched} unmatched to a department "
          f"({(len(cen)-unmatched)/len(cen)*100:.1f}% covered)")
    if unmatched:
        print("  unmatched:", sorted(cen.loc[cen._dept.isna(), "DEPARTEMENT"].unique())[:10])

    # one projection for every panel
    xs = [pt[0] for f in geo["features"] for poly in _polys(f) for pt in poly]
    ys = [pt[1] for f in geo["features"] for poly in _polys(f) for pt in poly]
    LON0, LON1, LAT0, LAT1 = min(xs), max(xs), min(ys), max(ys)
    height = int(round(WIDTH * (LAT1 - LAT0) / (LON1 - LON0)))

    def project(lon, lat):
        return ((lon - LON0) / (LON1 - LON0) * WIDTH * SUPERSAMPLE,
                (LAT1 - lat) / (LAT1 - LAT0) * height * SUPERSAMPLE)

    def bin_of(n):
        if n <= 0:
            return None
        for i, edge in enumerate(BREAKS):
            if n < edge:
                return i
        return len(BREAKS)

    os.makedirs(OUT, exist_ok=True)
    for label, slug in TYPES:
        counts = cen[cen._type == label].groupby("_dept").size()
        img = Image.new("RGBA", (WIDTH * SUPERSAMPLE, height * SUPERSAMPLE), (0, 0, 0, 0))
        d = ImageDraw.Draw(img, "RGBA")
        for key, feat in shapes.items():
            n = int(counts.get(key, 0))
            b = bin_of(n)
            fill = RAMP[b] if b is not None else EMPTY
            rgb = tuple(int(fill[i:i + 2], 16) for i in (1, 3, 5))
            for poly in _polys(feat):
                d.polygon([project(x, y) for x, y in poly],
                          fill=rgb + (255,), outline=(255, 255, 255, 210))
        img.resize((WIDTH, height), Image.LANCZOS).save(f"{OUT}/{slug}.png", optimize=True)
        print(f"  {label:20s} {counts.sum():6,} schools, "
              f"{counts.min()}–{counts.max()} per department -> {slug}.png")


def _polys(feat):
    g = feat["geometry"]
    if g["type"] == "Polygon":
        return g["coordinates"]
    return [ring for poly in g["coordinates"] for ring in poly]


if __name__ == "__main__":
    main()
