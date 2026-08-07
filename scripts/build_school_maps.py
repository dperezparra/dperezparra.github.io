#!/usr/bin/env python3
"""
Regenerate the Nigerian school maps shown on /datasets/.

Renders one small-multiple PNG per level of education: the national outline plus
one dot per geocoded school. Output goes to assets/media/datasets/, where Hugo
picks it up.

    python3 scripts/build_school_maps.py

SOURCE DATA (not in this repo - it is not openly published):

    /Users/perezp/Dropbox/Mobile phones and FGC/Dataset/Schools Nigeria/nigerian_schools_db.csv

    A byte-identical copy also sits in the Senegal project folder; this is the
    canonical location.

DESIGN NOTES

  * One hue for every panel, #7c3aed - the site accent. Identity comes from the
    panel label, not from colour, so there is no categorical palette to get
    wrong. That hue was checked with the dataviz validator and passes every
    check against BOTH the light and the dark surface, which is why a single
    transparent PNG serves both themes.

  * Faceting rather than one combined map is deliberate twice over: a point map
    is an all-pairs form, where a validated categorical palette tops out at
    three series (we have four levels), and 100k primary schools on one map
    would bury everything else anyway.

  * Backgrounds are transparent and labels live in HTML, so text stays crisp,
    themed and translatable.

  * Dot radius and alpha scale with the number of points, so a 1,100-point panel
    and a 100,000-point panel are both readable.

  * Outline: Natural Earth 1:50m admin-0 (public domain), mainland ring only.
"""

import json
import os
import subprocess
import sys

import pandas as pd
from PIL import Image, ImageDraw

SRC = "/Users/perezp/Dropbox/Mobile phones and FGC/Dataset/Schools Nigeria/nigerian_schools_db.csv"
OUT = "assets/media/datasets"
NE_URL = ("https://raw.githubusercontent.com/nvkelso/natural-earth-vector/"
          "master/geojson/ne_50m_admin_0_countries.geojson")

# Bounds of the mainland outline; the projection below must match the one used
# for any pin placed on these maps.
LON0, LON1, LAT0, LAT1 = 2.6860, 14.6197, 4.2774, 13.8729
WIDTH, SUPERSAMPLE = 840, 2
DOT = (0x7C, 0x3A, 0xED)

LEVELS = [
    ("Pre-Primary", "pre-primary"),
    ("Primary", "primary"),
    ("Junior Secondary", "junior-secondary"),
    ("Senior Secondary", "senior-secondary"),
]


def dot_style(n):
    """Bigger, more opaque dots when there are fewer of them."""
    if n > 50_000:
        return 1.5, 72
    if n > 10_000:
        return 1.9, 92
    if n > 2_000:
        return 2.8, 150
    return 3.4, 195


def nigeria_ring(cache="/tmp/ne50_countries.geojson"):
    # curl rather than urllib: the system Python here has no CA bundle wired up
    # and urlopen fails with CERTIFICATE_VERIFY_FAILED.
    if not os.path.exists(cache):
        subprocess.run(["curl", "-fsSL", "-o", cache, NE_URL], check=True)
    data = json.load(open(cache))
    feat = next(f for f in data["features"]
                if (f["properties"].get("NAME") or f["properties"].get("ADMIN")) == "Nigeria")
    geom = feat["geometry"]
    rings = (geom["coordinates"] if geom["type"] == "Polygon"
             else [r for poly in geom["coordinates"] for r in poly])
    return max(rings, key=len)


def main():
    if not os.path.exists(SRC):
        sys.exit(f"source data not found:\n  {SRC}")

    height = int(round(WIDTH * (LAT1 - LAT0) / (LON1 - LON0)))

    def project(lon, lat):
        return ((lon - LON0) / (LON1 - LON0) * WIDTH * SUPERSAMPLE,
                (LAT1 - lat) / (LAT1 - LAT0) * height * SUPERSAMPLE)

    outline = [project(x, y) for x, y in nigeria_ring()]

    df = pd.read_csv(SRC, low_memory=False)
    df["lat"] = pd.to_numeric(df["Latitude"], errors="coerce")
    df["lon"] = pd.to_numeric(df["Longitude"], errors="coerce")
    inside = df[df.lat.between(LAT0, LAT1) & df.lon.between(LON0, LON1)]
    print(f"{len(df):,} rows, {len(inside):,} with coordinates inside Nigeria")

    os.makedirs(OUT, exist_ok=True)
    for label, slug in LEVELS:
        sub = inside[inside["Level of Education"] == label]
        radius, alpha = dot_style(len(sub))
        img = Image.new("RGBA", (WIDTH * SUPERSAMPLE, height * SUPERSAMPLE), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img, "RGBA")
        draw.line(outline + [outline[0]], fill=(156, 163, 175, 200),
                  width=2 * SUPERSAMPLE, joint="curve")
        for lon, lat in zip(sub.lon.values, sub.lat.values):
            x, y = project(lon, lat)
            draw.ellipse([x - radius, y - radius, x + radius, y + radius], fill=DOT + (alpha,))
        path = f"{OUT}/nigeria-{slug}.png"
        img.resize((WIDTH, height), Image.LANCZOS).save(path, optimize=True)
        print(f"  {label:18s} {len(sub):7,} points -> {path}")


if __name__ == "__main__":
    main()
