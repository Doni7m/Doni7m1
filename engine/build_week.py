# -*- coding: utf-8 -*-
import os, sys, json
import numpy as np
from PIL import Image, ImageDraw
import compose as C
from content_w42 import POSTS, norm

BASE = os.path.dirname(os.path.abspath(__file__))
ART = f"{BASE}/art_w42"
OUTROOT = os.path.abspath(f"{BASE}/../posts")
W, H = C.W, C.H


def render(spec, scene, n=None, total=None, big=False, footer_num=True, seed=10):
    bg = Image.fromarray(C.paper(seed=seed)).convert("RGB")
    d = ImageDraw.Draw(bg)
    max_w = W - 2 * C.MX
    sizes = range(104, 44, -2) if big else range(76, 44, -2)
    chosen = None
    for sz in sizes:
        f = C.lora(sz, weight=700)
        lines = C.balanced(d, spec[0], f, max_w)
        lh = int(sz * 1.22)
        sub_h = 64 if spec[1] else 0
        if len(lines) * lh + sub_h <= (C.TEXT_BOTTOM - C.TEXT_TOP):
            chosen = (sz, f, lines, lh)
            break
    assert chosen, spec[0]
    sz, f, lines, lh = chosen
    y = C.TEXT_TOP
    for ln in lines:
        assert d.textlength(ln, font=f) <= max_w + 1, ln
        d.text((C.MX, y), ln, font=f, fill=C.INK)
        y += lh
    text_end = y
    if spec[1]:
        fs = C.lora(32, italic=True, weight=500)
        d.text((C.MX, y + 18), spec[1], font=fs, fill=C.ACCENT)
        text_end = y + 18 + 36
    ill = np.asarray(Image.open(f"{ART}/{scene}.png").convert("RGB"), np.float32) / 255.0
    ivory = np.array(C.IVORY, np.float32) / 255.0
    ratio = ill / ivory
    canvas = np.asarray(bg, np.float32) / 255.0
    y0 = int(min(584, 300 + text_end / 2))
    region = canvas[y0:y0 + ill.shape[0], :, :]
    canvas[y0:y0 + ill.shape[0], :, :] = np.clip(region * ratio, 0, 1)
    img = Image.fromarray((canvas * 255).astype(np.uint8)).convert("RGB")
    d = ImageDraw.Draw(img)
    d.line([(C.MX, 1236), (W - C.MX, 1236)], fill=C.LINE, width=2)
    ff = C.lora(30, weight=600)
    d.text((C.MX, 1256), "@doni7m", font=ff, fill=C.MUTED)
    if footer_num:
        tag = f"{n:02d} / {total:02d}"
        d.text((W - C.MX - d.textlength(tag, font=ff), 1256), tag, font=ff, fill=C.MUTED)
    return img, sz, len(lines), y0 + ill.shape[0]


def main(only=None):
    report = []
    for p in POSTS:
        key = f"{p['date']}_{p['slot']}"
        if only and key not in only:
            continue
        out = f"{OUTROOT}/{key}"
        os.makedirs(out, exist_ok=True)
        tags = p["hashtags"]
        assert len(tags) == 30 and len({norm(t) for t in tags}) == 30, key
        if p["kind"] == "carousel":
            assert len(p["slides"]) == 7 and len(p["scenes"]) == 7
            for i, (spec, sc) in enumerate(zip(p["slides"], p["scenes"])):
                words = len(spec[0].split())
                assert words <= 26, (key, i, words)
                img, sz, nl, yend = render(spec, sc, n=i + 1, total=7, big=(i == 0), seed=10 + i)
                path = f"{out}/{key}_{i + 1:02d}.jpg"
                img.save(path, "JPEG", quality=92, optimize=True)
                report.append((key, i + 1, sz, nl, words, os.path.getsize(path)))
        else:
            img, sz, nl, yend = render(p["slides"][0], p["scenes"][0], big=True, footer_num=False, seed=40)
            path = f"{out}/{key}.jpg"
            img.save(path, "JPEG", quality=92, optimize=True)
            report.append((key, 1, sz, nl, len(p["slides"][0][0].split()), os.path.getsize(path)))
        legenda = "1. LEGENDA PRONTA PARA PUBLICAR\n\n" + p["caption"] + "\n\n2. HASHTAGS\n\n" + " ".join(tags) + \
                  "\n\n3. REFERÊNCIA FILOSÓFICA — NÃO COPIAR PARA A LEGENDA\n\n" + p["ref"] + "\n"
        open(f"{out}/legenda.txt", "w", encoding="utf-8").write(legenda)
        full = p["caption"] + "\n\n" + " ".join(tags)
        assert len(full) <= 2200, (key, len(full))
        print(key, "ok", "len texto Metricool:", len(full), flush=True)
    for r in report:
        print(r)


if __name__ == "__main__":
    main(sys.argv[1:] or None)
