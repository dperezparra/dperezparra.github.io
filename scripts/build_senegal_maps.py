#!/usr/bin/env python3
"""
Regenerate the Senegal school maps shown on /datasets/.

One choropleth per school type, shaded by the number of schools in each
COMMUNE. Output goes to assets/media/datasets/.

    python3 scripts/build_senegal_maps.py

SOURCE DATA (not in this repo - it is not openly published):

    /Users/perezp/Dropbox/Education and Marriage in Senegal/Data/School Census/
        primary school census.xlsx
        secondary school census.xlsx

BOUNDARIES: OpenStreetMap admin_level=8, fetched through Overpass (ODbL).

WHY OSM AND NOT GADM / geoBoundaries / OCHA

The census locates schools to commune, and only OSM carries a commune layer
that actually corresponds to it:

    OSM admin_level=8        550 units   98.2% of schools matched
    GADM level 4             433 units   78%  (structurally capped: 433 < 549)
    geoBoundaries ADM3       121 units   arrondissements, not communes
    OCHA COD ADM3            125 units   arrondissements, not communes

Senegal has ~550 communes since the 2014 reorganisation; the other layers
predate it or stop a level short.

MATCHING (see match_communes)

Three passes, in order: a hand-written alias table, then exact match on a
normalised key, then difflib at >= 0.84. Normalisation strips the census's
"Com " prefix and OSM's "Communauté rurale de / d' / des" forms, folds accents,
and collapses the orthographic variation that is routine in Senegalese place
names - th/t, dj/j, ck/k, kh/h, ou/u, y/i, w/v, and doubled letters. That is
what takes the match from 81% to 98%: "Ngayokhene"/"Ngayokhème",
"Koumpentoun"/"Koumpentoum", "Thiakar"/"Thiakhar" are the same place.

The run prints the final coverage and lists whatever is left unmatched -
currently ~19 communes and under 2% of schools, some of which are simply
absent from OSM. Unmatched communes are drawn in the "no data" tone.

DESIGN NOTES

  * Sequential ramp: one hue, light to dark, lightness strictly decreasing
    (asserted at run time). Sequential encodes magnitude - never a rainbow.
  * One ABSOLUTE scale shared by all three panels, so they are comparable.
  * Transparent background, labels in HTML, so one asset serves both themes.
"""

import json
import os
import re
import subprocess
import sys
import unicodedata
import difflib
from collections import Counter

import pandas as pd
from PIL import Image, ImageDraw

SRC = "/Users/perezp/Dropbox/Education and Marriage in Senegal/Data/School Census"
OUT = "assets/media/datasets"
CACHE = "/tmp/osm_sen_communes.json"
OVERPASS = "https://overpass-api.de/api/interpreter"
QUERY = """[out:json][timeout:600];
area["ISO3166-1"="SN"][admin_level=2]->.sn;
relation["boundary"="administrative"]["admin_level"="8"](area.sn);
out geom;"""

WIDTH, SUPERSAMPLE = 840, 2
RAMP = ["#ede9fe", "#c4b5fd", "#a78bfa", "#7c3aed", "#5b21b6"]
BREAKS = [10, 20, 40, 80]              # upper edges; 5 bins, tail open
NODATA = "#f4f4f5"

TYPES = [
    ("Petite enfance", "senegal-petite-enfance"),
    ("Primaire", "senegal-primaire"),
    ("Moyen & secondaire", "senegal-moyen-secondaire"),
]

CENSUS_PREFIX = re.compile(r"^(com|art|dpt|ia|ief|ville|cv)[\s.]+", re.I)
OSM_PREFIX = re.compile(
    r"^(communaut[eé]s?\s+rurales?\s+(de\s+|des\s+|du\s+|d')?"
    r"|communes?\s+(de\s+|des\s+|du\s+|d')?"
    r"|arrondissement\s+(de\s+|d')?|ville\s+de\s+)", re.I)

ALIAS = {
    "Com Jaxaay": "Commune de Jaxaay - Parcelles",
    "Com Joal": "Joal-Fadiouth",
    "Com Dahra": "Dahra Djoloff",
    "Com Saly": "Saly Portudal",
    "Com Plateau": "Commune de Dakar-Plateau",
    "Com Koki": "Communauté rurale de Coki",
    "Com Fass Gueule Tapee Col": "Commune de Gueule Tapée-Fass-Colobane",
    "Com Diender Guedji": "Communauté rurale de Diender",
    "Com Agnam Civol": "Communauté rurale des Agnams",
    "Com Popenguine": "Popenguine-Ndayane",
    "Com Enampor": "Communauté rurale d'Enampore",
    "Com Nioro": "Nioro du Rip",
    "Com Dialokoto": "Communauté rurale de Dialacoto",
    "Com Boutoupa Cam": "Communauté rurale de Boutoupa-Camaracounda",
    "Com Thiakar": "Communauté rurale de Thiakhar",
    "Com Oudougar": "Communauté rurale de Oudoucar",
    "Com Santhiaba Mandjack": "Communauté rurale de Santhiaba Manjacque",
    "Com Mbacke Cadior": "Communauté rurale de Mbacké Kadjor",
    "Com Guede Chantier": "Communauté rurale de Guédé Village",
    "Com Ndioumane Thiekene": "Communauté rurale de Ndioumane",
}


def norm(s, osm=False):
    s = (OSM_PREFIX if osm else CENSUS_PREFIX).sub("", str(s).strip())
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"[^a-z0-9]", "", s)
    s = (s.replace("th", "t").replace("dj", "j").replace("ck", "k").replace("kh", "h")
          .replace("ou", "u").replace("y", "i").replace("w", "v"))
    return re.sub(r"(.)\1+", r"\1", s)


def oklab_l(hex_color):
    r, g, b = (int(hex_color[i:i + 2], 16) / 255 for i in (1, 3, 5))
    f = lambda c: c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = f(r), f(g), f(b)
    l = (0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b) ** (1 / 3)
    m = (0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b) ** (1 / 3)
    s = (0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b) ** (1 / 3)
    return 0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s


def fetch_communes():
    if not os.path.exists(CACHE):
        subprocess.run(["curl", "-fsSL", "-m", "900", "-X", "POST",
                        "--data-binary", QUERY, OVERPASS, "-o", CACHE], check=True)
    return json.load(open(CACHE))["elements"]


def rings_of(rel):
    """Stitch a relation's `outer` ways into closed rings."""
    segs = [[(p["lon"], p["lat"]) for p in m["geometry"]]
            for m in rel.get("members", [])
            if m.get("role") == "outer" and m.get("geometry")]
    rings, current = [], None
    while segs:
        if current is None:
            current = segs.pop(0)
            continue
        tail = current[-1]
        for i, s in enumerate(segs):
            if s[0] == tail:
                current += segs.pop(i)[1:]
                break
            if s[-1] == tail:
                current += list(reversed(segs.pop(i)))[1:]
                break
        else:                       # nothing joins: close what we have, start over
            rings.append(current)
            current = None
            continue
        if current[0] == current[-1]:
            rings.append(current)
            current = None
    if current:
        rings.append(current)
    return [r for r in rings if len(r) >= 4]


def match_communes(census_names, osm_names):
    idx = {}
    for o in osm_names:
        idx.setdefault(norm(o, True), o)
    keys = list(idx)
    mapping, how = {}, Counter()
    for u in census_names:
        if u in ALIAS and ALIAS[u] in osm_names:
            mapping[u] = ALIAS[u]; how["alias"] += 1; continue
        n = norm(u)
        if n in idx:
            mapping[u] = idx[n]; how["exact"] += 1; continue
        hit = difflib.get_close_matches(n, keys, n=1, cutoff=0.84)
        if hit:
            mapping[u] = idx[hit[0]]; how["fuzzy"] += 1
    return mapping, how


def main():
    light = [oklab_l(c) for c in RAMP]
    assert all(a > b for a, b in zip(light, light[1:])), "ramp must darken monotonically"

    rels = [r for r in fetch_communes() if r.get("tags", {}).get("name")]
    geom = {r["tags"]["name"]: rings_of(r) for r in rels}
    geom = {k: v for k, v in geom.items() if v}
    print(f"OSM communes with usable geometry: {len(geom)}/{len(rels)}")

    pri = pd.read_excel(f"{SRC}/primary school census.xlsx")
    sec = pd.read_excel(f"{SRC}/secondary school census.xlsx")
    pri["_type"] = pri["LIBELLE_TYPE_SYSTEME_ENSEIGNEMENT"].map(
        {"PETITE ENFANCE": "Petite enfance", "PRIMAIRE": "Primaire"})
    sec["_type"] = "Moyen & secondaire"
    cen = pd.concat([pri, sec])
    cen["COMMUNE"] = cen["COMMUNE"].astype(str)

    mapping, how = match_communes(sorted(cen["COMMUNE"].unique()), list(geom))
    cen["_com"] = cen["COMMUNE"].map(mapping)
    hit = cen["_com"].notna().sum()
    print(f"matched {len(mapping)}/{cen['COMMUNE'].nunique()} communes "
          f"({len(mapping)/cen['COMMUNE'].nunique()*100:.1f}%), "
          f"{hit:,}/{len(cen):,} schools ({hit/len(cen)*100:.1f}%)  {dict(how)}")
    miss = cen[cen._com.isna()]["COMMUNE"].value_counts()
    if len(miss):
        print(f"  unmatched ({len(miss)} communes, {miss.sum():,} schools):",
              ", ".join(miss.index[:8]) + ("…" if len(miss) > 8 else ""))

    pts = [p for rs in geom.values() for r in rs for p in r]
    LON0, LON1 = min(p[0] for p in pts), max(p[0] for p in pts)
    LAT0, LAT1 = min(p[1] for p in pts), max(p[1] for p in pts)
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
        counts = cen[cen._type == label].groupby("_com").size()
        img = Image.new("RGBA", (WIDTH * SUPERSAMPLE, height * SUPERSAMPLE), (0, 0, 0, 0))
        d = ImageDraw.Draw(img, "RGBA")
        for name, rs in geom.items():
            n = int(counts.get(name, 0))
            b = bin_of(n)
            fill = RAMP[b] if b is not None else NODATA
            rgb = tuple(int(fill[i:i + 2], 16) for i in (1, 3, 5))
            for ring in rs:
                d.polygon([project(x, y) for x, y in ring],
                          fill=rgb + (255,), outline=(255, 255, 255, 150))
        img.resize((WIDTH, height), Image.LANCZOS).save(f"{OUT}/{slug}.png", optimize=True)
        nz = counts[counts > 0]
        print(f"  {label:20s} {counts.sum():6,} schools across {len(nz):3d} communes "
              f"({nz.min()}–{nz.max()} each) -> {slug}.png")


if __name__ == "__main__":
    main()
