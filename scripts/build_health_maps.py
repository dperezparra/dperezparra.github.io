#!/usr/bin/env python3
"""
Regenerate the Nigerian health facility map shown on /datasets/.

One combined map: the national outline, the primary health care mesh underneath,
and the hospitals on top. Output goes to assets/media/datasets/, where Hugo
picks it up.

    python3 scripts/build_health_maps.py

SOURCE DATA (not in this repo - it is not openly published):

    /Users/perezp/Dropbox/Hospitals and Fertility/Data/HC_v1.dta

    The register as downloaded is
    .../Data/HC facilities/Nigeria-hospitals-and-clinics_hxl.xlsx (42,064 rows,
    the first being the HXL tag row). HC_v1.dta is that file after cleaning,
    with the self-geocoded coordinates merged into longitude/latitude and
    geolocated_R marking which rows they came from.

DESIGN NOTES

  * ONE map rather than a facet set, unlike the school maps next door: the
    question here is where the two layers of the system overlap, which small
    multiples would hide.

  * SHAPE carries the distinction: circles for primary care, triangles for
    hospitals. That is what lets the colour go pastel - emerald 300 #6ee7b7 for
    the mesh and emerald 500 #10b981 for the hospitals, 2.5 degrees apart in
    hue, so it reads as one soft green rather than two colours.

    Colour alone would not carry it at these values. ONE transparent PNG has to
    serve both themes, and a translucent mesh tracks whatever surface it sits
    on - pale on white, dim on dark - while an opaque mark does not. Worst-case
    separation across the two surfaces, in OKLab L:

        #6ee7b7 @a120 + #10b981   0.164   <- chosen
        #a7f3d0 @a120 + #10b981   0.131   (mesh near-invisible on white)
        #6ee7b7 @a150 + #059669   0.009   (the two collapse on dark)

    0.164 is below what colour alone should carry, which is precisely why the
    shapes are there. #10b981 is 2.5:1 on white and 7.0:1 on dark, so the
    hospital mark clears both surfaces on its own.

  * Hospital marks are also drawn larger, and larger than a like-for-like
    triangle would be: an equilateral triangle covers only ~41% of its
    circumcircle, so matching a circle's visual weight already takes a bigger
    radius before any deliberate size step. The map is shown at half the column
    width and at 440 px the downscale rounds a small triangle back into a blob,
    so sizes were picked by rendering at the real display size and looking, not
    at 1:1.

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
# The map is shown at half the text column, ~440 CSS px, so 880 is a 2x asset.
WIDTH, SUPERSAMPLE = 880, 2

#             rgb                    radius  alpha
PHC      = ((0x6E, 0xE7, 0xB7), 1.6, 120)   # circles
HOSPITAL = ((0x10, 0xB9, 0x81), 7.4, 250)   # triangles; radius is the circumradius
GAP = 2.6      # surface gap punched around every hospital mark, in render px


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

    phc = inside[inside.facility_type == "PHC"]
    hospital = inside[inside.facility_type == "Hospital"]

    img = Image.new("RGBA", (WIDTH * SUPERSAMPLE, height * SUPERSAMPLE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img, "RGBA")           # composites onto what is there
    punch = ImageDraw.Draw(img)                  # writes raw pixels, so it erases
    draw.line(outline + [outline[0]], fill=(156, 163, 175, 200),
              width=2 * SUPERSAMPLE, joint="curve")

    def circles(sub, r, fn):
        for lon, lat in zip(sub.lon.values, sub.lat.values):
            x, y = project(lon, lat)
            fn([x - r, y - r, x + r, y + r])

    # Upward-pointing equilateral triangle, r = circumradius. Sitting the
    # centroid on the point rather than the apex keeps the mark visually
    # centred on the facility.
    SIN30, COS30 = 0.5, 0.8660254
    def triangles(sub, r, fn):
        for lon, lat in zip(sub.lon.values, sub.lat.values):
            x, y = project(lon, lat)
            fn([(x, y - r), (x + COS30 * r, y + SIN30 * r), (x - COS30 * r, y + SIN30 * r)])

    # PHC mesh first; then every hospital clears a gap in it before any hospital
    # is drawn, so the gap reads as page surface in either theme and no hospital
    # erases its neighbour.
    rgb, r, alpha = PHC
    circles(phc, r, lambda box: draw.ellipse(box, fill=rgb + (alpha,)))

    rgb, r, alpha = HOSPITAL
    triangles(hospital, r + GAP, lambda pts: punch.polygon(pts, fill=(0, 0, 0, 0)))
    triangles(hospital, r, lambda pts: draw.polygon(pts, fill=rgb + (alpha,)))

    for label, sub, (rgb, _, _) in [("Primary health care", phc, PHC),
                                    ("Hospital", hospital, HOSPITAL)]:
        print(f"  {label:20s} {len(sub):7,} points  "
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
