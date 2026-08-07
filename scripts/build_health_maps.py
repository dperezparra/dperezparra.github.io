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

  * Palette: two steps of one green, emerald 500 #10b981 for primary care and
    emerald 600 #059669 for hospitals - 0.7 degrees apart in hue, so it really
    is green on green. Level of care is ORDERED, so this is an ordinal ramp
    rather than a categorical pair.

    The thing that decides these values is that ONE transparent PNG has to
    serve both themes. A translucent mesh tracks whatever surface it sits on -
    pale on white, dim on dark - while an opaque mark does not, so the pair
    separates in both directions as long as the hospital step sits near the
    middle. Worst-case separation across the two surfaces, in OKLab L:

        mesh @a90 + #059669   0.205   <- chosen
        mesh @a90 + #047857   0.117
        mesh @a130 + #047857  0.040   (invisible on dark)

    A deeper hospital step looks better in isolation on white and then
    disappears into #17181c, which is exactly the trap. #059669 is 3.8:1 on
    white and 4.7:1 on dark, so it clears both surfaces on its own too.

  * Size reinforces the same order: hospitals are drawn much larger, so the two
    never rely on colour alone - and the legend repeats that size difference.
    The gap has to be big because the map is shown at half the column width; at
    440 px the downscale averages a small mark towards the surface. Sizes were
    picked by rendering at the real display size and looking, not at 1:1.

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
PHC      = ((0x10, 0xB9, 0x81), 1.4, 90)
HOSPITAL = ((0x05, 0x96, 0x69), 5.6, 250)
GAP = 2.4      # surface gap punched around every hospital mark, in render px


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

    def marks(sub, r, fn):
        for lon, lat in zip(sub.lon.values, sub.lat.values):
            x, y = project(lon, lat)
            fn([x - r, y - r, x + r, y + r])

    # PHC mesh first; then every hospital clears a gap in it before any hospital
    # is drawn, so the gap reads as page surface in either theme and no hospital
    # erases its neighbour.
    rgb, r, alpha = PHC
    marks(phc, r, lambda box: draw.ellipse(box, fill=rgb + (alpha,)))

    rgb, r, alpha = HOSPITAL
    marks(hospital, r + GAP, lambda box: punch.ellipse(box, fill=(0, 0, 0, 0)))
    marks(hospital, r, lambda box: draw.ellipse(box, fill=rgb + (alpha,)))

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
