#!/usr/bin/env python3
"""
Regenerate the Chilean policing rollout chart shown on /datasets/.

Cumulative number of municipalities covered by each of the two programmes,
1994-2022. Output goes to assets/media/datasets/, where Hugo picks it up.

    python3 scripts/build_chile_charts.py

SOURCE DATA (not in this repo - it is not openly published):

    .../Policia e inversiones en seguridad/Data/
        Plan Cuadrante/PCSPdata_2000-2013.dta      150 communes + entry year
        Seguridad Ciudadana/SC_data.dta            345 communes x 20 years

WHY A CHART AND NOT A MAP

The other two records on that page are maps because the question they answer is
"where". Here it is "when": both programmes arrive commune by commune, and that
staggered timing is the whole identifying variation. A choropleth of Chile would
also fight its own geometry - 4,300 km long and a few hundred wide, with almost
every treated commune inside Greater Santiago.

A WARNING ABOUT THE DUMMIES

PCSP_dummy and SC_dummy are labelled in Spanish and read 1 = No, 2 = Si, which
is the reverse of what an English-speaking reader assumes. Taking 1 as "yes"
silently returns 139 and 171 instead of 189 and 120. The counts below come from
the value labels, not the codes. Both series are read from the start-year
columns, which are populated only for municipalities that answered "Si", so
they are immune to the mix-up either way.

DESIGN NOTES

  * Two series, #7c3aed (the site accent) and #d95926. Checked with the dataviz
    validator against BOTH surfaces, #ffffff and #17181c: passes every check on
    both, CVD dE 31.8 and normal-vision dE 34.9, so one transparent PNG serves
    light and dark mode.

  * Series identity lives in the HTML legend, not in the image, so it stays
    crisp and translatable. Only the axis numbers are baked in, in #71717a -
    4.6:1 on white and 3.9:1 on the dark surface.

  * Step lines, not smoothed: a municipality joins on a date and stays. Drawing
    it as a slope would invent adoptions between the steps.
"""

import os
import sys

import pandas as pd
from PIL import Image, ImageDraw, ImageFont

SRC = "/Users/perezp/Dropbox/Policia e inversiones en seguridad/Data"
OUT = "assets/media/datasets"
FONT = "/System/Library/Fonts/Helvetica.ttc"

# Canvas is 2x the 880px asset, which is itself shown at ~440 CSS px, so canvas
# pixels divide by 4 to reach CSS pixels. Every size below is canvas px.
WIDTH, HEIGHT, SS = 880, 520, 2
CW, CH = WIDTH * SS, HEIGHT * SS
PAD_L, PAD_R, PAD_T, PAD_B = 96, 40, 36, 84

X0, X1 = 1994, 2022
Y1 = 200
YTICKS = [0, 50, 100, 150, 200]
XTICKS = [1995, 2000, 2005, 2010, 2015, 2020]

PC = (0x7C, 0x3A, 0xED)
SC = (0xD9, 0x59, 0x26)
INK = (0x71, 0x71, 0x7A)
GRID = (0xA1, 0xA1, 0xAA, 90)

# 48 canvas px = 12 CSS px at the size this is shown. Raster text reads a shade
# smaller than the crisp HTML around it, so it sits just above the 11px the site
# uses for its own small type.
LINE_W, GRID_W, FONT_PX = 8, 4, 48


def cumulative(years, lo, hi):
    """Running count of municipalities joined by each year in [lo, hi]."""
    counts = pd.Series(years).value_counts()
    total, out = 0, []
    for y in range(lo, hi + 1):
        total += int(counts.get(y, 0))
        out.append((y, total))
    return out


def main():
    pc_path = f"{SRC}/Plan Cuadrante/PCSPdata_2000-2013.dta"
    sc_path = f"{SRC}/Seguridad Ciudadana/SC_data.dta"
    for p in (pc_path, sc_path):
        if not os.path.exists(p):
            sys.exit(f"source data not found:\n  {p}")

    pc = pd.read_stata(pc_path, convert_categoricals=False)
    # convert_categoricals=True so `Si`/`No` come through as labels - see the
    # warning in the docstring.
    sc = pd.read_stata(sc_path).drop_duplicates("code_comuna")

    pc_years = pc.PCSP.dropna().astype(int).tolist()
    sc_years = sc.loc[sc.SC_dummy == "Si", "SC_PT"].dropna().astype(int).tolist()
    print(f"Plan Cuadrante      {len(pc_years):3d} municipalities, "
          f"{min(pc_years)}-{max(pc_years)}")
    print(f"Seguridad Ciudadana {len(sc_years):3d} municipalities, "
          f"{min(sc_years)}-{max(sc_years)}")

    series = [(cumulative(pc_years, X0, X1), PC),
              (cumulative(sc_years, X0, X1), SC)]

    def px(year):
        return PAD_L + (year - X0) / (X1 - X0) * (CW - PAD_L - PAD_R)

    def py(value):
        return CH - PAD_B - value / Y1 * (CH - PAD_T - PAD_B)

    img = Image.new("RGBA", (CW, CH), (0, 0, 0, 0))
    d = ImageDraw.Draw(img, "RGBA")
    font = ImageFont.truetype(FONT, FONT_PX)

    for v in YTICKS:
        y = py(v)
        d.line([(PAD_L, y), (CW - PAD_R, y)], fill=GRID, width=GRID_W)
        d.text((PAD_L - 20, y), f"{v}", font=font, fill=INK + (255,), anchor="rm")

    for year in XTICKS:
        d.text((px(year), CH - PAD_B + 26), f"{year}", font=font,
               fill=INK + (255,), anchor="mt")

    # Step lines: hold the level until the year it actually changes.
    for points, colour in series:
        path = []
        for i, (year, value) in enumerate(points):
            if i:
                path.append((px(year), py(points[i - 1][1])))
            path.append((px(year), py(value)))
        d.line(path, fill=colour + (255,), width=LINE_W, joint="curve")

    os.makedirs(OUT, exist_ok=True)
    path = f"{OUT}/chile-policing-rollout.png"
    flat = img.resize((WIDTH, HEIGHT), Image.LANCZOS)
    flat.quantize(colors=128, method=Image.FASTOCTREE).save(path, optimize=True)
    print(f"-> {path}  ({os.path.getsize(path) / 1024:.0f} KB)")


if __name__ == "__main__":
    main()
