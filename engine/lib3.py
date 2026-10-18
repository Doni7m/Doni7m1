"""Extras de cena para a semana 19-25/10/2026 (sobre lib2/paint)."""
import numpy as np
from lib2 import *


def fin(P, seed):
    return P.finish(top=30, bottom=34, left=45, right=45, feather=70, seed=seed)


def floor(P, y=560, col=(70, 48, 32)):
    P.layer(rect(-5, y, SW + 5, SH + 5), col, op=1.0, wob=2, rim=0.2)


def big_tree(P, x, ybase, h, lean=0.0, trunk=(70, 50, 36), leaf=(40, 98, 70), seed=1, crown=0.5):
    L, R = [], []
    for t in np.linspace(0, 1, 12):
        cx = x + lean * h * np.sin(t * 2.5) + 16 * np.sin(t * 7)
        w = 34 * (1 - 0.55 * t)
        y = ybase - h * t
        L.append((cx - w, y))
        R.append((cx + w, y))
    P.layer(poly(L + R[::-1]), trunk, op=0.98, wob=3, rim=0.25)
    topx = x + lean * h * np.sin(2.5)
    leafy(P, topx, ybase - h - 10, h * crown, leaf, n=44, seed=seed)
    return topx


def guitar(P, x, y, s=1.0, col=(176, 98, 62)):
    P.layer(ell(x, y + 30 * s, 54 * s, 50 * s), col, op=0.98, wob=1.2, rim=0.3)
    P.layer(ell(x, y - 24 * s, 40 * s, 38 * s), col, op=0.98, wob=1.2, rim=0.2)
    P.layer(ell(x, y + 4 * s, 16 * s, 16 * s), (30, 22, 20), op=0.95, wob=0.8)
    P.layer(rect(x - 7 * s, y - 200 * s, x + 7 * s, y - 50 * s), (70, 46, 30), op=0.98, wob=1)
    P.layer(rect(x - 12 * s, y - 226 * s, x + 12 * s, y - 198 * s), (60, 40, 26), op=0.98, wob=1)


def wheel(P, x, y, r, col=(120, 82, 48), spokes=8):
    P.layer(shape(lambda d: [d.ellipse([x - r, y - r, x + r, y + r], fill=255),
                             d.ellipse([x - r * 0.84, y - r * 0.84, x + r * 0.84, y + r * 0.84], fill=0)]), col, op=0.98, wob=1.5, rim=0.3)
    for k in range(spokes):
        a = k * np.pi / spokes * 2
        pts = [(x - np.cos(a) * r * 0.9, y - np.sin(a) * r * 0.9), (x + np.cos(a) * r * 0.9, y + np.sin(a) * r * 0.9)]
        P.layer(shape(lambda d, pts=pts: d.line(pts, fill=255, width=10)), col, op=0.98, wob=1.2, rim=0.2)
    P.layer(ell(x, y, r * 0.14, r * 0.14), (74, 50, 30), op=0.98, wob=1)


def ladder(P, x, ybase, h, w=70, col=(150, 108, 66), lean=0.0):
    for dx in (-w / 2, w / 2):
        P.layer(poly([(x + dx, ybase), (x + dx + 8, ybase), (x + dx + 8 + lean, ybase - h), (x + dx + lean, ybase - h)]), col, op=0.98, wob=1.2, rim=0.3)
    for k in range(1, 8):
        yy = ybase - h * k / 8
        P.layer(rect(x - w / 2, yy - 4, x + w / 2 + lean * k / 8, yy + 4), col, op=0.98, wob=1)


def sapling(P, x, ybase, h, leaf=(74, 140, 92)):
    P.layer(poly([(x - 4, ybase), (x + 4, ybase), (x + 2, ybase - h), (x - 2, ybase - h)]), (92, 66, 44), op=0.98, wob=0.8)
    for dx, dy, rx in [(-18, 0.8, 18), (16, 0.65, 18), (-12, 0.5, 14), (0, 1.0, 20), (14, 0.88, 14)]:
        P.layer(ell(x + dx, ybase - h * dy, rx, rx * 0.5), leaf, op=0.97, wob=1, rim=0.25)


def tv(P, x0, y0, x1, y1):
    P.layer(rect(x0, y0, x1, y1), (26, 28, 34), op=0.98, wob=1.2, rim=0.25)
    P.vgrad(y0 + 12, y1 - 12, (110, 164, 224), (170, 200, 236), mask=rect(x0 + 12, y0 + 12, x1 - 12, y1 - 12), wob=0.8, rim=0)
    P.glow((x0 + x1) / 2, (y0 + y1) / 2, (x1 - x0) * 0.8, (120, 170, 230), 0.4)


def lit_window(P, x0, y0, x1, y1, silhouette=False):
    P.glow((x0 + x1) / 2, (y0 + y1) / 2, (x1 - x0) * 1.4, WARM, 0.5)
    P.layer(rect(x0, y0, x1, y1), (255, 214, 130), op=0.98, wob=1, rim=0.3)
    if silhouette:
        cx = (x0 + x1) / 2
        P.layer(ell(cx, y0 + (y1 - y0) * 0.38, (x1 - x0) * 0.16, (y1 - y0) * 0.17), (60, 40, 34), op=0.97, wob=0.8)
        P.layer(poly([(x0 + (x1 - x0) * 0.2, y1), (cx - (x1 - x0) * 0.1, y0 + (y1 - y0) * 0.58), (cx + (x1 - x0) * 0.1, y0 + (y1 - y0) * 0.58),
                      (x1 - (x1 - x0) * 0.2, y1)]), (60, 40, 34), op=0.97, wob=0.8)
    t = 6
    for a, b, c, d in [(x0 - t, y0 - t, x0, y1 + t), (x1, y0 - t, x1 + t, y1 + t), (x0 - t, y0 - t, x1 + t, y0), (x0 - t, y1, x1 + t, y1 + t + 2)]:
        P.layer(rect(a, b, c, d), (96, 66, 40), op=0.98, wob=0.8)


def facade(P, x0, x1, ytop, ybot, col=(190, 172, 132), roof=(150, 70, 52)):
    P.layer(rect(x0, ytop, x1, ybot), col, op=0.98, wob=2, rim=0.3, vary=0.12)
    P.layer(poly([(x0 - 20, ytop), ((x0 + x1) / 2, ytop - 80), (x1 + 20, ytop)]), roof, op=0.98, wob=2, rim=0.3)


def rock_pool(P, x, y, rx, ry):
    P.layer(ell(x, y, rx + 14, ry + 8), (18, 30, 38), op=0.98, wob=3, rim=0.3)
    P.layer(ell(x, y, rx, ry), (40, 124, 138), op=0.97, wob=2, rim=0.2, soft=1.6)
    P.layer(ell(x - rx * 0.2, y - ry * 0.2, rx * 0.5, ry * 0.3), (128, 190, 196), op=0.5, wob=1.5, rim=0, soft=3)


def stack_papers(P, x, y, n=5, w=120):
    r = np.random.default_rng(int(x))
    for i in range(n):
        letter(P, x + r.uniform(-8, 8), y - i * 14, w=w, tilt=r.uniform(-0.04, 0.04), stamp=(i % 2 == 0))


def waterfall(P, x, ytop, ybot, w0=50, w1=150, col=(214, 232, 236)):
    P.layer(poly([(x - w0 / 2, ytop), (x + w0 / 2, ytop), (x + w1 / 2 + 10, ybot), (x - w1 / 2 - 10, ybot)]), col, op=0.92, wob=3, rim=0.25, soft=1.4)
    for k in range(6):
        P.line([(x - w0 / 2 + k * w0 / 5, ytop), (x - w1 / 2 + k * w1 / 5, ybot)], w=2, alpha=0.25, color=(120, 170, 180))
