from PIL import Image, ImageOps
im = Image.open("source-prepped.png").convert("L")
mask = ImageOps.invert(im).point(lambda p: 255 if p > 10 else 0)
im = im.crop(mask.getbbox())
w, h = im.size
s = int(max(w, h) * 1.05)
canvas = Image.new("L", (s, s), 255)
canvas.paste(im, ((s - w) // 2, (s - h) // 2))
canvas.save("source-prepped.png")
print("recadré :", w, "x", h, "->", s, "x", s)
