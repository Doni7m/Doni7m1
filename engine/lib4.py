"""Extras de cena para a semana 02-08/11/2026 (sobre lib2/lib3)."""
import numpy as np
from lib3 import *

BLUE_COAT = (60, 100, 120)
RUST_COAT = (176, 98, 62)
SAGE_COAT = (110, 130, 90)


def bookshelf(P, x0, y0, x1, y1, rows=4, seed=1):
    r = np.random.default_rng(seed)
    P.layer(rect(x0, y0, x1, y1), (58, 40, 28), op=0.98, wob=1.5, rim=0.3)
    rh = (y1 - y0) / rows
    cols = [(150, 60, 48), (60, 100, 120), (196, 138, 52), (110, 130, 90), (232, 214, 170), (90, 70, 110)]
    for k in range(rows):
        yb = y0 + (k + 1) * rh - 6
        x = x0 + 8
        while x < x1 - 14:
            w = r.uniform(10, 22)
            h = r.uniform(rh * 0.55, rh * 0.85)
            P.layer(rect(x, yb - h, x + w, yb), cols[int(r.integers(0, len(cols)))], op=0.97, wob=0.6, rim=0.25)
            x += w + r.uniform(1, 4)
        P.layer(rect(x0, yb, x1, yb + 6), (84, 56, 34), op=0.98, wob=1)


def paper_tag(P, x, y, w=70, tilt=0.0):
    h = w * 0.5
    P.layer(poly([(x - w / 2, y - h / 2), (x + w / 2, y - h / 2 + w * tilt), (x + w / 2, y + h / 2 + w * tilt), (x - w / 2, y + h / 2)]),
            (244, 236, 210), op=0.98, wob=0.6, rim=0.3)
    for k in range(2):
        P.line([(x - w * 0.34, y - 4 + k * 10), (x + w * 0.3, y - 4 + k * 10 + w * tilt)], w=1, alpha=0.5)


def framed(P, x0, y0, x1, y1, top=(120, 170, 190), bot=(236, 214, 160)):
    P.layer(rect(x0 - 8, y0 - 8, x1 + 8, y1 + 8), (96, 66, 40), op=0.98, wob=1, rim=0.3)
    P.vgrad(y0, y1, top, bot, mask=rect(x0, y0, x1, y1), wob=0.8, rim=0.2)


def rain(P, x0, x1, y0, y1, n=70, seed=1, col=(190, 214, 224)):
    r = np.random.default_rng(seed)
    for _ in range(n):
        x, y = r.uniform(x0, x1), r.uniform(y0, y1)
        P.line([(x, y), (x - 8, y + 26)], w=2, alpha=0.4, color=col)


def terrace(P, ytop, h, col, seed=1, edge=(120, 110, 96)):
    P.layer(poly(ridge(ytop, 6, seed, x0=-20, x1=SW + 20, step=40) + [(SW + 20, ytop + h), (-20, ytop + h)]), col, op=0.98, wob=2, rim=0.25)
    P.layer(rect(-10, ytop + h - 12, SW + 10, ytop + h), edge, op=0.98, wob=1.5, rim=0.3)


def boulder(P, x, y, rx, ry, col=(104, 100, 94)):
    P.layer(ell(x, y, rx, ry), col, op=0.98, wob=3, rim=0.3, vary=0.2)
    P.layer(ell(x - rx * 0.25, y - ry * 0.3, rx * 0.5, ry * 0.4), tuple(min(255, int(c * 1.3)) for c in col), op=0.6, wob=2, rim=0, soft=2)


def bed(P, x0, x1, ytop, col=(176, 98, 62)):
    P.layer(rect(x0, ytop, x1, ytop + 80), (96, 66, 40), op=0.98, wob=1.5, rim=0.3)
    P.layer(rect(x0 + 8, ytop - 26, x1 - 8, ytop + 12), col, op=0.98, wob=2, rim=0.3)
    P.layer(rrect(x0 + 14, ytop - 48, x0 + 130, ytop - 12, 14), (236, 226, 202), op=0.98, wob=1.5, rim=0.3)


def pier(P, x0, x1, y):
    P.layer(rect(x0, y, x1, y + 34), (110, 100, 88), op=0.98, wob=2, rim=0.3, vary=0.18)
    P.layer(rect(x0, y, x1, y + 8), (158, 146, 124), op=0.95, wob=1.2)
    for x in np.arange(x0 + 30, x1, 70):
        P.layer(rect(x, y + 34, x + 16, y + 110), (60, 50, 42), op=0.95, wob=1.5)
