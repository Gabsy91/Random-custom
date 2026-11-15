"""Process raw captures (assets/raw/clean) into ready-to-animate assets (assets/final).

- screens: bottom tab bar already hidden at capture; resized to 1080 px wide (LANCZOS)
- product strip: crop of the product page from brand line to protection block, 1080 px wide
- cards / chips / protection block: tight crops, kept at 3x source resolution for punch-ins
- logo mark: traced to SVG (potracer) for a stroke-draw reveal; PNGs copied
Usage: python3 scripts/process_assets.py
"""
import json, os, re, shutil
import numpy as np
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "assets/raw")
CLEAN = os.path.join(RAW, "clean")
FIN = os.path.join(ROOT, "assets/final")
os.makedirs(FIN, exist_ok=True)
DPR = 3
boxes = json.load(open(os.path.join(CLEAN, "boxes.json")))


def save(im, name):
    p = os.path.join(FIN, name)
    im.save(p, optimize=True)
    print(f"{name:28s} {im.size}")


def w1080(im):
    return im.resize((1080, round(im.size[1] * 1080 / im.size[0])), Image.LANCZOS)


# full screens
for n in ("home_screen", "results_default", "results_sorted", "product_strip"):
    save(w1080(Image.open(os.path.join(CLEAN, n + ".png")).convert("RGB")), n + ".png")

# result cards, named by price (default order on the site: 164, 157, 178, 171)
for i, price in enumerate((164, 157, 178, 171)):
    im = Image.open(os.path.join(CLEAN, f"card_default_{i}.png")).convert("RGB")
    save(im.crop((6, 6, im.size[0] - 6, im.size[1] - 6)), f"card_{price}.png")


def crop_box(src, b, pad=4):
    im = Image.open(os.path.join(CLEAN, src)).convert("RGB")
    x0, y0 = int((b["x"] - pad) * DPR), int((b["y"] - pad) * DPR)
    x1, y1 = int((b["x"] + b["w"] + pad) * DPR), int((b["y"] + b["h"] + pad) * DPR)
    return im.crop((x0, y0, x1, y1))


# "Prix croissant" chip in both states (screens are viewport shots, so CSS y == screen y)
save(crop_box("results_default.png", boxes["results_chip_asc"]), "chip_asc_off.png")
save(crop_box("results_sorted.png", boxes["results_chip_asc"]), "chip_asc_on.png")
# protection block
im = Image.open(os.path.join(CLEAN, "product_protection.png")).convert("RGB")
save(im, "protection.png")

# logo
for n in ("logo-mark.png", "logo-mark-dark.png", "icon.png"):
    shutil.copy(os.path.join(RAW, n), os.path.join(FIN, n))
import potrace  # potracer (pure python)

lg = np.array(Image.open(os.path.join(RAW, "logo-mark-dark.png")).convert("RGBA"))
mask = lg[:, :, 3] > 128
plist = potrace.Bitmap(mask).trace(turdsize=20, alphamax=0.0, opticurve=False)
paths = []
for curve in plist:
    d = [f"M{curve.start_point.x:.1f},{curve.start_point.y:.1f}"]
    for seg in curve.segments:
        if seg.is_corner:
            d.append(f"L{seg.c.x:.1f},{seg.c.y:.1f}L{seg.end_point.x:.1f},{seg.end_point.y:.1f}")
        else:
            d.append(f"C{seg.c1.x:.1f},{seg.c1.y:.1f} {seg.c2.x:.1f},{seg.c2.y:.1f} {seg.end_point.x:.1f},{seg.end_point.y:.1f}")
    path = "".join(d) + "Z"
    xs = [float(v) for v in re.findall(r"[-\d.]+", path)[0::2]]
    if min(xs) <= 0.5 and max(xs) >= mask.shape[1] - 0.5:   # full-frame rectangle artefact
        continue
    paths.append(path)
h, w = mask.shape
svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">' + "".join(
    f'<path fill-rule="evenodd" d="{d}"/>' for d in paths) + "</svg>"
open(os.path.join(FIN, "logo-mark.svg"), "w").write(svg)
print("logo-mark.svg", len(paths), "paths")

# fonts
os.makedirs(os.path.join(ROOT, "assets/fonts"), exist_ok=True)
for f in os.listdir(os.path.join(RAW, "fonts")):
    shutil.copy(os.path.join(RAW, "fonts", f), os.path.join(ROOT, "assets/fonts", f))
