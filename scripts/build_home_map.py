#!/usr/bin/env python3
"""
Regenerate data/world_map.json, the country outlines behind the home page map.

    curl -sL -o /tmp/countries-110m.json \\
        https://cdn.jsdelivr.net/npm/world-atlas@2.0.2/countries-110m.json
    python3 scripts/build_home_map.py /tmp/countries-110m.json

SOURCE: world-atlas 2.0.2 (ISC), a TopoJSON build of Natural Earth 1:110m
Admin 0 countries (public domain).

WHAT IT WRITES

Every country whose centre falls in the Americas-to-Africa frame, already
projected to SVG coordinates with a plain linear lon/lat mapping:

    x = (lon - lon_min) * scale
    y = (lat_max - lat) * scale

The home block (layouts/_partials/hbx/blocks/home-map/block.html) places the
pins with the SAME mapping, reading lon_min / lat_max / scale from this file,
so outlines and pins always agree. Points closer than ~1px are dropped to keep
the inline SVG small (~40 KB).
"""

import json
import sys

OUT = "data/world_map.json"
LON_MIN, LON_MAX, LAT_MIN, LAT_MAX = -95, 62, -57, 40
SCALE = 4


def main(src):
    topo = json.load(open(src))
    sx, sy = topo["transform"]["scale"]
    tx, ty = topo["transform"]["translate"]

    # TopoJSON arcs are delta-encoded and quantised.
    arcs = []
    for arc in topo["arcs"]:
        x = y = 0
        pts = []
        for dx, dy in arc:
            x += dx
            y += dy
            pts.append((x * sx + tx, y * sy + ty))
        arcs.append(pts)

    def ring(indexes):
        pts = []
        for i in indexes:
            a = arcs[i] if i >= 0 else arcs[~i][::-1]
            pts.extend(a if not pts else a[1:])
        return pts

    def proj(lon, lat):
        return ((lon - LON_MIN) * SCALE, (LAT_MAX - lat) * SCALE)

    countries = []
    for g in topo["objects"]["countries"]["geometries"]:
        polys = g["arcs"] if g["type"] == "MultiPolygon" else [g["arcs"]]
        rings = [ring(r) for poly in polys for r in poly]
        pts = [p for r in rings for p in r]
        clon = sum(p[0] for p in pts) / len(pts)
        clat = sum(p[1] for p in pts) / len(pts)
        if not (LON_MIN - 20 < clon < LON_MAX + 10 and LAT_MIN - 5 < clat < LAT_MAX + 12):
            continue
        d = ""
        for r in rings:
            if not any(LON_MIN - 30 < lo < LON_MAX + 30 and LAT_MIN - 10 < la < LAT_MAX + 20 for lo, la in r):
                continue
            xy = [proj(*p) for p in r]
            keep = [xy[0]]
            for p in xy[1:]:
                if abs(p[0] - keep[-1][0]) + abs(p[1] - keep[-1][1]) > 1.2:
                    keep.append(p)
            if len(keep) >= 3:
                d += "M" + "L".join(f"{x:.0f},{y:.0f}" for x, y in keep) + "Z"
        if d:
            countries.append({"name": g["properties"]["name"], "d": d})

    data = {
        "width": (LON_MAX - LON_MIN) * SCALE,
        "height": (LAT_MAX - LAT_MIN) * SCALE,
        "lon_min": LON_MIN,
        "lat_max": LAT_MAX,
        "scale": SCALE,
        "countries": countries,
    }
    with open(OUT, "w") as f:
        json.dump(data, f, ensure_ascii=False, separators=(",", ":"))
    print(f"wrote {OUT}: {len(countries)} countries")


if __name__ == "__main__":
    main(sys.argv[1])
