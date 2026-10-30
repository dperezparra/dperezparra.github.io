#!/usr/bin/env python3
"""
Regenerate the illustrations on the Working Papers cards on /research/.

One flat-vector scene per paper, drawn from scratch - no data, no figures from
the papers themselves. Output overwrites each paper's featured.png, which the
card view crops to 16:9 and the paper page uses as its share image.

    python3 scripts/build_paper_illustrations.py

DESIGN NOTES

  * 1600x900 so the card's `Fill 800x450` only downsamples and crops nothing.
    Each scene is drawn at 2x and reduced with Lanczos, which is the cheapest
    way to get anti-aliased edges out of PIL.

  * Palette is Tailwind's purple ramp - the site's `appearance.color` - plus a
    single warm amber accent. The background is opaque and light, so the image
    reads the same in light and dark mode (the card frames it either way).

  * No text in either image: the card already carries the title, and baked-in
    words would be unreadable at phone width.
"""

import math
import os
import random

from PIL import Image, ImageDraw

OUT = "content/publication"
W, H, SS = 1600, 900, 2

P50, P100, P200, P300 = "#faf5ff", "#f3e8ff", "#e9d5ff", "#d8b4fe"
P400, P500, P600, P700 = "#c084fc", "#a855f7", "#9333ea", "#7e22ce"
P800, P900, P950 = "#6b21a8", "#581c87", "#3b0764"
AMBER, AMBER_LIGHT = "#f59e0b", "#fcd34d"
WHITE = "#ffffff"


def rgba(hex_colour, alpha=255):
    h = hex_colour.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)) + (alpha,)


class Canvas:
    """A supersampled RGBA canvas whose methods take final-size coordinates."""

    def __init__(self, top, bottom):
        self.im = Image.new("RGBA", (W * SS, H * SS))
        # vertical gradient background
        d = ImageDraw.Draw(self.im)
        t, b = rgba(top), rgba(bottom)
        for y in range(H * SS):
            f = y / (H * SS - 1)
            d.line([(0, y), (W * SS, y)], fill=tuple(round(t[i] + (b[i] - t[i]) * f) for i in range(4)))

    def layer(self):
        """A transparent layer, so translucent shapes blend instead of overwrite."""
        lay = Image.new("RGBA", self.im.size)
        return lay, ImageDraw.Draw(lay)

    def merge(self, lay):
        self.im.alpha_composite(lay)

    @staticmethod
    def s(v):
        return round(v * SS)

    def pts(self, points):
        return [(x * SS, y * SS) for x, y in points]

    def box(self, x0, y0, x1, y1):
        return [x0 * SS, y0 * SS, x1 * SS, y1 * SS]

    def save(self, path):
        self.im.convert("RGB").resize((W, H), Image.LANCZOS).save(path, optimize=True)
        print("wrote", path)


def dashed(draw, cv, points, colour, width, dash=18, gap=12, closed=False):
    """Dashed polyline; the dash pattern runs continuously round corners."""
    pts = list(points) + ([points[0]] if closed else [])
    on, left = True, dash
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        seg = math.hypot(x1 - x0, y1 - y0)
        pos = 0.0
        while pos < seg:
            step = min(left, seg - pos)
            if on:
                a, b = pos / seg, (pos + step) / seg
                draw.line(cv.pts([(x0 + (x1 - x0) * a, y0 + (y1 - y0) * a),
                                  (x0 + (x1 - x0) * b, y0 + (y1 - y0) * b)]),
                          fill=colour, width=cv.s(width))
            pos += step
            left -= step
            if left <= 0:
                on = not on
                left = dash if on else gap


def star(cx, cy, r_out, r_in, n=5, rot=-90):
    pts = []
    for i in range(2 * n):
        r = r_out if i % 2 == 0 else r_in
        a = math.radians(rot + i * 180 / n)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


# ---------------------------------------------------------------------------
# Boots in the Beat - a city carved into patrol quadrants
# ---------------------------------------------------------------------------

def beat_policing(path):
    rnd = random.Random(7)
    cv = Canvas(P100, P50)
    d = ImageDraw.Draw(cv.im)

    BW, BH, ST = 150, 118, 36           # block width/height, street width
    X0, Y0 = -70, -52                   # grid origin, off-canvas so the map bleeds

    # Quadrants follow the streets, not a ruler - the real ones were drawn round
    # neighbourhoods - so each is an irregular staircase of whole blocks. One
    # letter per block, columns left to right; H is the highlighted quadrant.
    QMAP = [
        "AAABBBCCCDD",
        "AABBBCCCDDD",
        "AEEEHHCDDDD",
        "EEEHHHHDDGG",
        "EEFHHHGGGGG",
        "FFFFHGGGGGG",
        "FFFFFFGGGGG",
        "FFFFFFFGGGG",
    ]
    rows, cols = len(QMAP), len(QMAP[0])
    HI = "H"

    def q(c, r):
        return QMAP[r][c] if 0 <= r < rows and 0 <= c < cols else None

    def block_xy(c, r):
        x = X0 + c * (BW + ST)
        y = Y0 + r * (BH + ST)
        return x, y

    def street_x(c):                    # centreline of the street left of column c
        return X0 + c * (BW + ST) - ST / 2

    def street_y(r):
        return Y0 + r * (BH + ST) - ST / 2

    # streets: the gradient shows through; blocks sit on top
    # highlighted quadrant: a translucent wash over its blocks and half-streets.
    # Each block's cell is exactly one grid step, so the cells tile edge to edge
    # and the wash never doubles up.
    lay, ld = cv.layer()
    for r in range(rows):
        for c in range(cols):
            if q(c, r) == HI:
                ld.rectangle(cv.box(street_x(c), street_y(r), street_x(c + 1), street_y(r + 1)),
                             fill=rgba(P400, 70))
    cv.merge(lay)

    parks = {(2, 4), (6, 1), (8, 5), (4, 3)}
    for c in range(cols):
        for r in range(rows):
            x, y = block_xy(c, r)
            if (c, r) in parks:
                d.rounded_rectangle(cv.box(x, y, x + BW, y + BH), radius=cv.s(14), fill="#dcf3e4")
                for _ in range(6):
                    tx, ty = x + rnd.uniform(24, BW - 24), y + rnd.uniform(24, BH - 24)
                    tr = rnd.uniform(11, 17)
                    d.ellipse(cv.box(tx - tr, ty - tr, tx + tr, ty + tr), fill="#9fd8b4")
                continue
            d.rounded_rectangle(cv.box(x, y, x + BW, y + BH), radius=cv.s(14), fill=WHITE)
            # buildings: a 2x2 or 3x2 grid of roofs, with jitter
            n = rnd.choice([2, 3])
            pad, gap = 12, 10
            cw = (BW - 2 * pad - (n - 1) * gap) / n
            rh = (BH - 2 * pad - gap) / 2
            for i in range(n):
                for j in range(2):
                    bx = x + pad + i * (cw + gap)
                    by = y + pad + j * (rh + gap)
                    shade = rnd.choice([P100, P200, P200, P300])
                    d.rounded_rectangle(cv.box(bx, by, bx + cw, by + rh), radius=cv.s(6), fill=shade)
                    # a lit window now and then
                    if rnd.random() < 0.35:
                        wx, wy = bx + cw * rnd.uniform(0.25, 0.6), by + rh * rnd.uniform(0.25, 0.5)
                        d.rounded_rectangle(cv.box(wx, wy, wx + 12, wy + 12), radius=cv.s(3), fill=AMBER_LIGHT)

    # quadrant boundaries: a street segment wherever the blocks either side of
    # it belong to different quadrants
    segs, hi_segs = [], []
    for r in range(rows):
        for c in range(cols):
            for nc, nr, seg in ((c + 1, r, [(street_x(c + 1), street_y(r)), (street_x(c + 1), street_y(r + 1))]),
                                (c, r + 1, [(street_x(c), street_y(r + 1)), (street_x(c + 1), street_y(r + 1))])):
                other = q(nc, nr)
                if other is None or other == q(c, r):
                    continue
                (hi_segs if HI in (q(c, r), other) else segs).append(seg)
    lay, ld = cv.layer()
    for seg in segs:
        dashed(ld, cv, seg, rgba(P700, 200), 5, dash=22, gap=14)
    # the highlighted quadrant gets a solid outline, with round corners joined
    for seg in hi_segs:
        ld.line(cv.pts(seg), fill=rgba(P700), width=cv.s(7))
        for x, y in seg:
            ld.ellipse(cv.box(x - 3.5, y - 3.5, x + 3.5, y + 3.5), fill=rgba(P700))
    cv.merge(lay)

    # patrol loop: the beat, run in the lane just outside a 3x2 run of the
    # quadrant's blocks, so it stays inside the quadrant's own streets
    IN = 8
    (lx0, ly0), (bx, by) = block_xy(3, 3), block_xy(5, 4)
    lx0, ly0, lx1, ly1 = lx0 - IN, ly0 - IN, bx + BW + IN, by + BH + IN
    loop = [(lx0, ly0), (lx1, ly0), (lx1, ly1), (lx0, ly1)]
    lay, ld = cv.layer()
    dashed(ld, cv, loop, rgba(AMBER), 7, dash=20, gap=13, closed=True)
    cv.merge(lay)

    # direction chevrons on the loop
    def chevron(cx, cy, ang):
        a = math.radians(ang)
        pts = [(cx + 16 * math.cos(a), cy + 16 * math.sin(a)),
               (cx + 13 * math.cos(a + 2.5), cy + 13 * math.sin(a + 2.5)),
               (cx + 13 * math.cos(a - 2.5), cy + 13 * math.sin(a - 2.5))]
        d.polygon(cv.pts(pts), fill=AMBER)

    chevron(lx0 + (lx1 - lx0) * 0.3, ly0, 0)
    chevron(lx1, (ly0 + ly1) / 2, 90)
    chevron(lx0, (ly0 + ly1) / 2, -90)

    # police car, top-down, driving along the bottom edge of the loop
    def car(cx, cy):
        L, Wd = 92, 50
        lay, ld = cv.layer()
        ld.rounded_rectangle(cv.box(cx - L / 2 + 4, cy - Wd / 2 + 8, cx + L / 2 + 4, cy + Wd / 2 + 8),
                             radius=cv.s(16), fill=rgba(P950, 60))
        cv.merge(lay)
        d.rounded_rectangle(cv.box(cx - L / 2, cy - Wd / 2, cx + L / 2, cy + Wd / 2), radius=cv.s(16), fill=P800)
        d.rounded_rectangle(cv.box(cx - 24, cy - Wd / 2 + 7, cx + 24, cy + Wd / 2 - 7), radius=cv.s(9), fill=WHITE)
        d.rounded_rectangle(cv.box(cx + 18, cy - Wd / 2 + 9, cx + 30, cy + Wd / 2 - 9), radius=cv.s(4), fill=P300)
        d.rounded_rectangle(cv.box(cx - 30, cy - Wd / 2 + 9, cx - 20, cy + Wd / 2 - 9), radius=cv.s(4), fill=P300)
        # light bar
        d.rounded_rectangle(cv.box(cx - 5, cy - 16, cx + 5, cy - 1), radius=cv.s(3), fill=AMBER)
        d.rounded_rectangle(cv.box(cx - 5, cy + 1, cx + 5, cy + 16), radius=cv.s(3), fill=P500)
        # headlights
        for sy in (-14, 14):
            d.ellipse(cv.box(cx + L / 2 - 9, cy + sy - 4, cx + L / 2 - 1, cy + sy + 4), fill=AMBER_LIGHT)

    car(lx0 + (lx1 - lx0) * 0.62, ly1)

    # one officer per quadrant - a map pin with a badge star
    def pin(cx, cy, size=1.0, pulse=False):
        r = 26 * size
        if pulse:
            lay, ld = cv.layer()
            for k, a in ((3.1, 40), (2.2, 70)):
                ld.ellipse(cv.box(cx - r * k, cy - r * k * 0.55 + 6, cx + r * k, cy + r * k * 0.55 + 6),
                           fill=rgba(P500, a))
            cv.merge(lay)
        lay, ld = cv.layer()
        ld.ellipse(cv.box(cx - r * 0.7, cy - 5, cx + r * 0.7, cy + 7), fill=rgba(P950, 70))
        cv.merge(lay)
        top = cy - r * 2.4
        d.polygon(cv.pts([(cx - r * 0.78, top + r * 1.45), (cx + r * 0.78, top + r * 1.45), (cx, cy)]), fill=P700)
        d.ellipse(cv.box(cx - r, top, cx + r, top + 2 * r), fill=P700)
        d.ellipse(cv.box(cx - r * 0.72, top + r * 0.28, cx + r * 0.72, top + r * 1.72), fill=WHITE)
        d.polygon(cv.pts(star(cx, top + r, r * 0.55, r * 0.24)), fill=AMBER)

    # every other quadrant: its officer on the visible inner intersection (all
    # four corner blocks in the quadrant) nearest the quadrant's middle
    for name in sorted(set("".join(QMAP)) - {HI}):
        cells = [(c, r) for r in range(rows) for c in range(cols) if q(c, r) == name]
        mx = sum(street_x(c) + (BW + ST) / 2 for c, _ in cells) / len(cells)
        my = sum(street_y(r) + (BH + ST) / 2 for _, r in cells) / len(cells)
        spots = [(street_x(c), street_y(r)) for r in range(1, rows) for c in range(1, cols)
                 if q(c - 1, r - 1) == q(c, r - 1) == q(c - 1, r) == q(c, r) == name]
        # a quadrant with no such corner on screen falls back to mid-street
        # between two of its blocks
        spots += [(street_x(c), street_y(r) + (BH + ST) / 2 + 20) for r in range(rows) for c in range(1, cols)
                  if q(c - 1, r) == q(c, r) == name] if not any(
                      60 < x < W - 60 and 90 < y < H - 20 for x, y in spots) else []
        spots = [(x, y) for x, y in spots if 60 < x < W - 60 and 90 < y < H - 20]
        if spots:
            pin(*min(spots, key=lambda p: math.hypot(p[0] - mx, p[1] - my)), 0.8)
    # the highlighted quadrant's own officers stand on its inner intersections
    pin(street_x(4), street_y(4), 1.35, pulse=True)
    pin(street_x(5), street_y(4), 1.05)

    cv.save(path)


# ---------------------------------------------------------------------------
# Shifting the Value of Norms - fast internet reaching a rural community
# ---------------------------------------------------------------------------

def fast_internet(path):
    rnd = random.Random(3)
    cv = Canvas("#ede4ff", "#fdfbff")
    d = ImageDraw.Draw(cv.im)

    TX, TY = 1180, 150                  # top of the tower

    # low sun behind the hills
    lay, ld = cv.layer()
    for k, a in ((150, 50), (115, 90), (88, 255)):
        ld.ellipse(cv.box(380 - k, 470 - k, 380 + k, 470 + k), fill=rgba(AMBER_LIGHT, a))
    cv.merge(lay)

    # signal arcs, fading outwards
    lay, ld = cv.layer()
    for i, r in enumerate(range(90, 1300, 110)):
        a = max(25, 190 - i * 16)
        ld.arc(cv.box(TX - r, TY - r, TX + r, TY + r), start=110, end=250, fill=rgba(P500, a), width=cv.s(7))
        ld.arc(cv.box(TX - r, TY - r, TX + r, TY + r), start=-70, end=70, fill=rgba(P500, a), width=cv.s(7))
    cv.merge(lay)

    def hill(base, amp, freq, phase, colour):
        pts = [(x, base + amp * math.sin(x / freq + phase) + amp * 0.4 * math.sin(x / (freq * 0.43) + phase * 2))
               for x in range(-20, W + 41, 20)]
        pts += [(W + 40, H + 20), (-20, H + 20)]
        d.polygon(cv.pts(pts), fill=colour)

    hill(560, 34, 230, 0.7, P200)
    hill(640, 26, 170, 2.1, "#dcc8fb")

    # the tower: tapered lattice
    BX, BY = TX, 690
    half_top, half_base = 16, 78
    legs_l = [(TX - half_top, TY + 40), (BX - half_base, BY)]
    legs_r = [(TX + half_top, TY + 40), (BX + half_base, BY)]
    for a, b in (legs_l, legs_r):
        d.line(cv.pts([a, b]), fill=P800, width=cv.s(10))
    levels = 9
    for i in range(levels + 1):
        f = i / levels
        y = TY + 40 + (BY - TY - 40) * f
        hw = half_top + (half_base - half_top) * f
        d.line(cv.pts([(TX - hw, y), (TX + hw, y)]), fill=P800, width=cv.s(5))
        if i < levels:
            f2 = (i + 1) / levels
            y2 = TY + 40 + (BY - TY - 40) * f2
            hw2 = half_top + (half_base - half_top) * f2
            d.line(cv.pts([(TX - hw, y), (TX + hw2, y2)]), fill=P700, width=cv.s(4))
            d.line(cv.pts([(TX + hw, y), (TX - hw2, y2)]), fill=P700, width=cv.s(4))
    # antennas and mast
    d.line(cv.pts([(TX, TY - 50), (TX, TY + 40)]), fill=P800, width=cv.s(8))
    for side in (-1, 1):
        d.rounded_rectangle(cv.box(TX + side * 30 - 9, TY - 6, TX + side * 30 + 9, TY + 62), radius=cv.s(5), fill=P900)
        d.line(cv.pts([(TX, TY + 20), (TX + side * 30, TY + 20)]), fill=P800, width=cv.s(5))
    d.rounded_rectangle(cv.box(TX - 9, TY - 18, TX + 9, TY + 40), radius=cv.s(5), fill=P900)
    lay, ld = cv.layer()
    ld.ellipse(cv.box(TX - 22, TY - 72, TX + 22, TY - 28), fill=rgba(AMBER, 80))
    cv.merge(lay)
    d.ellipse(cv.box(TX - 10, TY - 60, TX + 10, TY - 40), fill=AMBER)

    # foreground ground
    hill(720, 18, 260, 4.0, "#efe6ff")

    # village: round huts with conical roofs and square houses with pitched roofs
    def hut(cx, base, s, lit):
        w, h = 110 * s, 70 * s
        d.rounded_rectangle(cv.box(cx - w / 2, base - h, cx + w / 2, base), radius=cv.s(10 * s), fill=WHITE)
        d.polygon(cv.pts([(cx - w / 2 - 18 * s, base - h + 6 * s), (cx + w / 2 + 18 * s, base - h + 6 * s),
                          (cx, base - h - 72 * s)]), fill=P600)
        d.polygon(cv.pts([(cx, base - h - 72 * s), (cx + w / 2 + 18 * s, base - h + 6 * s),
                          (cx + 8 * s, base - h + 6 * s)]), fill=P700)
        d.rounded_rectangle(cv.box(cx - 14 * s, base - 46 * s, cx + 14 * s, base), radius=cv.s(12 * s), fill=P800)
        if lit:
            d.rounded_rectangle(cv.box(cx + 24 * s, base - 50 * s, cx + 42 * s, base - 30 * s),
                                radius=cv.s(4 * s), fill=AMBER_LIGHT)

    def house(cx, base, s, lit):
        w, h = 150 * s, 86 * s
        d.rectangle(cv.box(cx - w / 2, base - h, cx + w / 2, base), fill=WHITE)
        d.polygon(cv.pts([(cx - w / 2 - 14 * s, base - h + 4 * s), (cx + w / 2 + 14 * s, base - h + 4 * s),
                          (cx + w / 2 - 20 * s, base - h - 46 * s), (cx - w / 2 + 20 * s, base - h - 46 * s)]),
                  fill=P500)
        d.polygon(cv.pts([(cx + 10 * s, base - h - 46 * s), (cx + w / 2 - 20 * s, base - h - 46 * s),
                          (cx + w / 2 + 14 * s, base - h + 4 * s), (cx + 10 * s, base - h + 4 * s)]), fill=P600)
        d.rounded_rectangle(cv.box(cx - 18 * s, base - 52 * s, cx + 10 * s, base), radius=cv.s(3 * s), fill=P800)
        for wx in (-56, 30):
            fill = AMBER_LIGHT if (lit and wx > 0) else P200
            d.rounded_rectangle(cv.box(cx + wx * s, base - 60 * s, cx + (wx + 24) * s, base - 36 * s),
                                radius=cv.s(4 * s), fill=fill)

    def acacia(cx, base, s, colour):
        d.line(cv.pts([(cx, base), (cx - 6 * s, base - 70 * s)]), fill=colour, width=cv.s(10 * s))
        d.line(cv.pts([(cx - 4 * s, base - 50 * s), (cx + 30 * s, base - 84 * s)]), fill=colour, width=cv.s(7 * s))
        d.line(cv.pts([(cx - 6 * s, base - 66 * s), (cx - 34 * s, base - 88 * s)]), fill=colour, width=cv.s(7 * s))
        d.ellipse(cv.box(cx - 100 * s, base - 120 * s, cx + 90 * s, base - 78 * s), fill=colour)

    # placed in the gaps between the phones, so none is hidden behind one
    acacia(420, 660, 0.8, P300)
    acacia(1010, 690, 0.9, P300)
    acacia(1545, 650, 0.7, P300)

    homes = [  # (kind, x, base, scale, lit, has phone)
        ("hut", 120, 800, 0.95, True, True),
        ("house", 330, 770, 0.95, False, False),
        ("hut", 560, 805, 1.1, False, True),
        ("house", 790, 780, 1.05, True, True),
        ("hut", 990, 800, 0.9, True, False),
        ("house", 1400, 790, 1.0, False, True),
    ]
    tops = []
    for kind, x, base, s, lit, phone in homes:
        (hut if kind == "hut" else house)(x, base, s, lit)
        if phone:
            tops.append((x, base - (175 if kind == "hut" else 170) * s - 50))

    # households linked to one another - dotted curves between phones
    lay, ld = cv.layer()
    for (x0, y0), (x1, y1) in zip(tops, tops[1:]):
        mx, my = (x0 + x1) / 2, min(y0, y1) - 70
        curve = [((1 - t) ** 2 * x0 + 2 * (1 - t) * t * mx + t * t * x1,
                  (1 - t) ** 2 * y0 + 2 * (1 - t) * t * my + t * t * y1) for t in [i / 40 for i in range(41)]]
        for i, (px, py) in enumerate(curve[3:-3]):
            if i % 3 == 0:
                ld.ellipse(cv.box(px - 4, py - 4, px + 4, py + 4), fill=rgba(P600, 200))
    cv.merge(lay)

    # phones floating above the connected homes
    def phone(cx, cy, tilt_seed):
        w, h = 46, 80
        lay, ld = cv.layer()
        ld.ellipse(cv.box(cx - 52, cy - 52, cx + 52, cy + 52), fill=rgba(WHITE, 170))
        cv.merge(lay)
        d.rounded_rectangle(cv.box(cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2), radius=cv.s(10), fill=P900)
        d.rounded_rectangle(cv.box(cx - w / 2 + 5, cy - h / 2 + 9, cx + w / 2 - 5, cy + h / 2 - 9),
                            radius=cv.s(5), fill=P100)
        # chat bubbles on the screen
        d.rounded_rectangle(cv.box(cx - 13, cy - 22, cx + 9, cy - 11), radius=cv.s(4), fill=P400)
        d.rounded_rectangle(cv.box(cx - 7, cy - 6, cx + 14, cy + 5), radius=cv.s(4), fill=AMBER)
        d.rounded_rectangle(cv.box(cx - 13, cy + 10, cx + 5, cy + 21), radius=cv.s(4), fill=P400)
        # signal bars above
        for i in range(4):
            bh = 7 + i * 6
            bx = cx + 30 + i * 9
            d.rounded_rectangle(cv.box(bx, cy - 34 - bh, bx + 6, cy - 34), radius=cv.s(2),
                                fill=P700 if i < 3 or tilt_seed else P300)

    for i, (x, y) in enumerate(tops):
        phone(x, y, i % 2)

    cv.save(path)


if __name__ == "__main__":
    beat_policing(os.path.join(OUT, "plan-cuadrante", "featured.png"))
    fast_internet(os.path.join(OUT, "fgm-3g", "featured.png"))
