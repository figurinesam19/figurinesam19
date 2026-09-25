import sys
from PIL import Image, ImageOps
KEEP = float(sys.argv[1]) if len(sys.argv) > 1 else 1.0
im = Image.open("source-prepped.png").convert("L")
mask = ImageOps.invert(im).point(lambda p: 255 if p > 10 else 0)
im = im.crop(mask.getbbox())
w, h = im.size
im = im.crop((0, 0, w, int(h * KEEP)))
w, h = im.size
s = int(max(w, h) * 1.05)
canvas = Image.new("L", (s, s), 255)
canvas.paste(im, ((s - w) // 2, s - h))
canvas.save("source-square.png")
print("garde", int(KEEP * 100), "% du sujet ->", s, "x", s)
