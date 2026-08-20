#!/usr/bin/env python3
"""
Crop a portrait to the square the homepage avatar wants and install it.

    python3 scripts/set_avatar.py ~/Downloads/photo.jpg
    python3 scripts/set_avatar.py ~/Downloads/photo.jpg --preview-only

The avatar is displayed as a CIRCLE at 270 px, so two things matter and
neither is "centre the image":

  * The circle inscribes the square, so anything in the corners is thrown
    away. Framing has to be judged on the circle, not the crop box - which
    is why --preview-only writes a masked preview to look at.

  * Eyes belong near 40% of the height, not at the middle. A face centred
    vertically in a portrait reads as slightly sunken, because the head
    extends further below the eyes than above them.

The crop is expressed as fractions of the source, so it survives being
handed the same photo at a different resolution. It assumes 3:4 portrait
and refuses anything else rather than silently mis-framing.
"""

import sys
from PIL import Image, ImageDraw

OUT = "content/authors/admin/avatar.jpg"
SIZE = 800          # ~3x the 270px display size, for retina
QUALITY = 88

# Measured off the photo: hair-top 0.408 of height, chin 0.617, eyes 0.522,
# face centre 0.533 of width. Square side 0.70 of width leaves the head at
# about 40% of the circle - the jacket and the street stay in, and the face
# is still the thing you see first. Tried 0.56 (head at 50%, too tight a
# crop) and 0.86 (head at 32%, face starts getting lost).
FACE_CX, EYES_CY, SIDE_W = 0.533, 0.522, 0.700
EYES_AT = 0.40      # where the eye line sits in the finished square


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    src = sys.argv[1]
    preview_only = "--preview-only" in sys.argv

    im = Image.open(src)
    im = im.convert("RGB")
    w, h = im.size
    ratio = w / h
    if abs(ratio - 3 / 4) > 0.02:
        sys.exit(f"expected a 3:4 portrait, got {w}x{h} (ratio {ratio:.3f}).\n"
                 "The crop fractions were measured on a 3:4 frame and would "
                 "mis-frame this. Re-measure before forcing it.")

    side = SIDE_W * w
    left = FACE_CX * w - side / 2
    top = EYES_CY * h - EYES_AT * side

    # Keep the box inside the frame without changing its size.
    left = max(0, min(left, w - side))
    top = max(0, min(top, h - side))
    box = tuple(round(v) for v in (left, top, left + side, top + side))
    print(f"source {w}x{h} -> crop {box}  (side {round(side)}px)")

    square = im.crop(box).resize((SIZE, SIZE), Image.LANCZOS)

    # What the page actually shows: the inscribed circle.
    preview = Image.new("RGB", (SIZE, SIZE), (255, 255, 255))
    mask = Image.new("L", (SIZE, SIZE), 0)
    ImageDraw.Draw(mask).ellipse([0, 0, SIZE - 1, SIZE - 1], fill=255)
    preview.paste(square, (0, 0), mask)
    preview.save("/tmp/avatar-preview.png")
    print("circle preview -> /tmp/avatar-preview.png")

    if preview_only:
        print("(preview only, nothing installed)")
        return
    square.save(OUT, quality=QUALITY, optimize=True, progressive=True)
    print(f"-> {OUT}")


if __name__ == "__main__":
    main()
