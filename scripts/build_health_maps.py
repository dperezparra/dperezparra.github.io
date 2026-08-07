#!/usr/bin/env python3
"""
Regenerate the Nigerian health facility map shown on /datasets/.

One combined map: the national outline, the primary health care mesh underneath,
and the hospitals on top split by ownership. Output goes to
assets/media/datasets/, where Hugo picks it up.

    python3 scripts/build_health_maps.py

SOURCE DATA (not in this repo - it is not openly published):

    /Users/perezp/Dropbox/Hospitals and Fertility/Data/HC_v1.dta

    The register as downloaded is
    .../Data/HC facilities/Nigeria-hospitals-and-clinics_hxl.xlsx (42,064 rows,
    the first being the HXL tag row). HC_v1.dta is that file after cleaning,
    with the self-geocoded coordinates merged into longitude/latitude and
    geolocated_R marking which rows they came from.

DESIGN NOTES

  * ONE map rather than a facet set, unlike the school maps next door. Three
    series is exactly the cap a point map allows - it is an all-pairs form, so
    every pair of hues has to separate, not just neighbours - and the question
    here is where the three overlap, which small multiples would hide.

  * Palette: #2a78d6 / #d95926 / #199e70. Validated with the dataviz validator
    at --pairs all against BOTH surfaces, #ffffff and #17181c, and it passes
    every check on both with no warnings - which is what lets one transparent
    PNG serve light and dark mode. The blue/orange pair is the strongest of the
    three (CVD dE 25.4, normal 32.3), so it carries public vs private, the
    distinction a reader most needs to make. Aqua takes the PHC mesh, whose
    weaker pairings (dE 9.4 vs orange) are backed by a large size difference -
    identity there never rests on hue alone.

  * Size encodes TYPE, not ownership: both hospital classes are drawn at the
    same radius. Only the draw order differs - private (4,645) first, public
    (1,354) last - so the rarer class is not buried under the commoner one.
    That is a rendering concession, not an encoding; the marks are identical.

  * Backgrounds are transparent and all text lives in HTML, so labels stay
    crisp, themed and translatable.

  * Outline: Natural Earth 1:50m admin-0 (public domain), mainland ring only.
    Same frame and projection as the school maps, so the two are comparable.
"""

import json
import os
import subprocess
import sys

import pandas as pd
from PIL import Image, ImageDraw

SRC = "/Users/perezp/Dropbox/Hospitals and Fertility/Data/HC_v1.dta"
OUT = "assets/media/datasets"
NE_URL = ("https://raw.githubusercontent.com/nvkelso/natural-earth-vector/"
          "master/geojson/ne_50m_admin_0_countries.geojson")

# Same frame as build_school_maps.py - do not change one without the other.
LON0, LON1, LAT0, LAT1 = 2.6860, 14.6197, 4.2774, 13.8729
WIDTH, SUPERSAMPLE = 1120, 2

#            rgb                    radius  alpha
PHC     = ((0x19, 0x9E, 0x70), 1.5, 95)
PRIVATE = ((0xD9, 0x59, 0x26), 3.4, 235)
PUBLIC  = ((0x2A, 0x78, 0xD6), 3.4, 245)
GAP = 1.7      # surface gap punched around every hospital mark, in render px


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

    df = pd.read_stata(SRC)
    df["lon"] = pd.to_numeric(df["longitude"], errors="coerce")
    df["lat"] = pd.to_numeric(df["latitude"], errors="coerce")
    inside = df[df.lat.between(LAT0, LAT1) & df.lon.between(LON0, LON1)]
    print(f"{len(df):,} facilities, {df.lon.notna().sum():,} with coordinates, "
          f"{len(inside):,} inside the frame "
          f"({len(inside) / len(df) * 100:.1f}%)")
    print(f"  self-geocoded rows kept: {(inside.geolocated_R == 1).sum():,} "
          f"of {(df.geolocated_R == 1).sum():,}")

    layers = [
        ("PHC",              inside[inside.facility_type == "PHC"],                       PHC),
        ("Private hospital", inside[(inside.facility_type == "Hospital")
                                    & (inside.ownership == "Private")],                   PRIVATE),
        ("Public hospital",  inside[(inside.facility_type == "Hospital")
                                    & (inside.ownership == "Public")],                    PUBLIC),
    ]

    img = Image.new("RGBA", (WIDTH * SUPERSAMPLE, height * SUPERSAMPLE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img, "RGBA")           # composites onto what is there
    punch = ImageDraw.Draw(img)                  # writes raw pixels, so it erases
    draw.line(outline + [outline[0]], fill=(156, 163, 175, 200),
              width=2 * SUPERSAMPLE, joint="curve")

    def marks(sub, r, fn):
        for lon, lat in zip(sub.lon.values, sub.lat.values):
            x, y = project(lon, lat)
            fn([x - r, y - r, x + r, y + r])

    hosp = [(sub, spec) for name, sub, spec in layers if name != "PHC"]

    # PHC mesh first, then every hospital mark clears a gap in it before any
    # hospital is drawn - so the gap reads as page surface in either theme, and
    # no hospital erases another of the same pass.
    for name, sub, (rgb, r, alpha) in layers:
        if name != "PHC":
            continue
        marks(sub, r, lambda box, c=rgb + (alpha,): draw.ellipse(box, fill=c))

    for sub, (_, r, _) in hosp:
        marks(sub, r + GAP, lambda box: punch.ellipse(box, fill=(0, 0, 0, 0)))

    for i, (sub, (rgb, r, alpha)) in enumerate(hosp):
        if i:   # re-clear, so public and private also keep a gap between them
            marks(sub, r + GAP, lambda box: punch.ellipse(box, fill=(0, 0, 0, 0)))
        marks(sub, r, lambda box, c=rgb + (alpha,): draw.ellipse(box, fill=c))

    for label, sub, (rgb, _, _) in layers:
        print(f"  {label:18s} {len(sub):7,} points  "
              f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}")

    os.makedirs(OUT, exist_ok=True)
    path = f"{OUT}/nigeria-health-facilities.png"
    flat = img.resize((WIDTH, height), Image.LANCZOS)
    # 41k antialiased dots make a 24-bit PNG about 770 KB; three hues plus their
    # edge pixels need nowhere near that many colours. FASTOCTREE is the one PIL
    # quantizer that keeps the alpha channel, and at 128 colours the three mark
    # hues survive to within 3/255 - checked, not assumed. ~180 KB.
    flat.quantize(colors=128, method=Image.FASTOCTREE).save(path, optimize=True)
    print(f"-> {path}  ({os.path.getsize(path) / 1024:.0f} KB)")


if __name__ == "__main__":
    main()
