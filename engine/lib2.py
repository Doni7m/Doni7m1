"""Biblioteca de elementos reutilizáveis para novas cenas (aquarela/guache, Madeira)."""
import numpy as np
from PIL import Image, ImageChops
from paint import *

PAPER_WALL = (14, 46, 60)
WOOD_T = (150, 104, 62)
WOOD_D = (96, 64, 38)
WOOD_X = (74, 50, 32)
ROCK = (28, 52, 62)
STONEL = (134, 124, 108)


# ------------------------------------------------------------------ céu e mar
def backdrop(P, mode="night", horizon=330, moonp=None, sunp=None, seed=1, island=False, clouds=0, sea_bottom=SH + 5):
    """Céu + mar com horizonte. mode: night, dusk, dawn, day, storm."""
    if mode == "night":
        sky(P, -5, horizon, NAVY, (30, 82, 96))
        P.stars(90, max(60, horizon - 40), seed=seed + 1)
        if moonp:
            moon(P, *moonp)
        sea(P, horizon - 8, sea_bottom, DTEAL, NAVY, seed=seed + 2)
        if moonp:
            moon_reflection(P, moonp[0], horizon + 4, horizon + 190, n=22, seed=seed + 3)
    elif mode == "dusk":
        P.vgrad(-5, horizon, (24, 48, 92), (226, 152, 98), mask=rect(-5, -5, SW + 5, horizon), wob=2, rim=0, vary=0.10)
        if sunp:
            x, y, r = sunp
            P.glow(x, y, r * 4, GOLD, 0.55)
            P.layer(ell(x, y, r, r), (252, 226, 160), op=0.98, wob=1.5, rim=0.05)
        sea(P, horizon - 8, sea_bottom, (44, 84, 100), (14, 34, 64), seed=seed + 2)
        if sunp:
            moon_reflection(P, sunp[0], horizon + 4, horizon + 190, n=22, seed=seed + 3)
    elif mode == "dawn":
        P.vgrad(-5, horizon, (58, 108, 128), (246, 212, 156), mask=rect(-5, -5, SW + 5, horizon), wob=2, rim=0, vary=0.08)
        if sunp:
            x, y, r = sunp
            P.glow(x, y, r * 4.5, WARM, 0.6)
            P.layer(ell(x, y, r, r), (255, 236, 176), op=0.98, wob=1.5, rim=0.05)
        sea(P, horizon - 8, sea_bottom, (66, 120, 134), (30, 82, 98), seed=seed + 2)
        if sunp:
            moon_reflection(P, sunp[0], horizon + 4, horizon + 170, n=22, seed=seed + 3)
    elif mode == "day":
        P.vgrad(-5, horizon, (92, 148, 172), (232, 226, 200), mask=rect(-5, -5, SW + 5, horizon), wob=2, rim=0, vary=0.07)
        sea(P, horizon - 8, sea_bottom, (50, 116, 132), (22, 72, 94), seed=seed + 2)
    elif mode == "storm":
        P.vgrad(-5, horizon, (30, 54, 72), (110, 130, 130), mask=rect(-5, -5, SW + 5, horizon), wob=2, rim=0, vary=0.12)
        sea(P, horizon - 8, sea_bottom, (30, 76, 88), (10, 30, 52), seed=seed + 2)
    for i in range(clouds):
        r = np.random.default_rng(seed * 7 + i)
        cx, cy = r.uniform(80, SW - 80), r.uniform(30, max(60, horizon - 80))
        col = (236, 226, 204) if mode in ("dawn", "dusk", "day") else (70, 100, 112)
        for k in range(3):
            P.layer(ell(cx + r.uniform(-60, 60), cy + r.uniform(-10, 10), r.uniform(80, 150), r.uniform(12, 22)),
                    col, op=0.30, wob=2, rim=0, soft=9)
    if island:
        far_island(P, horizon, island if isinstance(island, tuple) else (600, 300))


def far_island(P, horizon, span=(600, 300)):
    x0, w = span
    pts = [(x0, horizon - 4), (x0 + w * 0.15, horizon - 22), (x0 + w * 0.4, horizon - 34), (x0 + w * 0.6, horizon - 26),
           (x0 + w * 0.85, horizon - 14), (x0 + w, horizon - 4)]
    P.layer(poly(pts + [(x0 + w, horizon + 2), (x0, horizon + 2)]), (44, 78, 92), op=0.9, wob=2, rim=0.1)


def cliff(P, side="left", top=240, seed=1, col=(10, 28, 40), reach=520):
    r = np.random.default_rng(seed)
    if side == "left":
        pts = [(-10, top), (reach * 0.3, top + 20), (reach * 0.6, top + 90), (reach * 0.85, top + 190), (reach, SH + 5), (-10, SH + 5)]
    else:
        pts = [(SW + 10, top), (SW - reach * 0.3, top + 20), (SW - reach * 0.6, top + 90), (SW - reach * 0.85, top + 190), (SW - reach, SH + 5), (SW + 10, SH + 5)]
    P.layer(poly(pts), col, op=1.0, wob=3, rim=0.3, vary=0.2)
    for _ in range(4):
        cx = (r.uniform(20, reach * 0.7)) if side == "left" else SW - r.uniform(20, reach * 0.7)
        cy = r.uniform(top + 60, SH - 40)
        P.layer(poly([(cx - 70, cy + 20), (cx - 10, cy - 40), (cx + 60, cy - 10), (cx + 40, cy + 50), (cx - 50, cy + 60)]),
                tuple(int(c * 1.9) for c in col), op=0.55, wob=3, rim=0.3)


def hill_houses(P, x0, x1, ytop, n=6, seed=1, lit=True, body=(116, 134, 138)):
    r = np.random.default_rng(seed)
    P.layer(poly(ridge(ytop, 45, seed, x0=x0, x1=x1)), (20, 50, 60), op=0.97, wob=3)
    for i in range(n):
        x = r.uniform(x0 + 10, x1 - 70)
        y = ytop + 20 + (i % 3) * 38 + r.uniform(0, 14)
        house(P, x, y, r.uniform(44, 62), r.uniform(32, 42), body=body, lit=lit, seed=i + seed)


def stone_wall(P, ytop, ybot=SH + 5, seed=3, base=(86, 80, 72), cap=True, x0=-5, x1=SW + 5):
    r = np.random.default_rng(seed)
    P.layer(rect(x0, ytop, x1, ybot), base, op=1.0, wob=1.5, rim=0.3, vary=0.18)
    if cap:
        P.layer(rect(x0, ytop - 10, x1, ytop + 12), STONEL, op=1.0, wob=1.5, rim=0.3)
    row = 0
    y = ytop + 22
    while y < ybot - 6:
        x = x0 - 20 + (row % 2) * 30
        while x < x1:
            w = r.uniform(70, 130)
            P.layer(rect(x, y, x + w - 4, y + 22), tuple(int(v * r.uniform(0.82, 1.1)) for v in (96, 88, 78)), op=0.9, wob=1.2, rim=0.3, soft=0.8)
            x += w
        y += 26
        row += 1


def cobbles(P, ytop, ybot=SH + 5, seed=2, glow_x=None, base=(62, 80, 84)):
    r = np.random.default_rng(seed)
    P.layer(rect(-5, ytop, SW + 5, ybot), (30, 54, 58), op=1.0, wob=2, rim=0.1)
    for _ in range(190):
        x, y = r.uniform(-10, SW), r.uniform(ytop + 6, ybot - 4)
        near = 0.0 if glow_x is None else 1 - min(1, abs(x - glow_x) / 380)
        col = np.array(base) * (1 - near) + np.array([188, 150, 92]) * near
        col = tuple(int(v * r.uniform(0.8, 1.15)) for v in col)
        P.layer(ell(x, y, r.uniform(12, 30), r.uniform(5, 11)), col, op=0.75, wob=1, rim=0.25, soft=0.8)


def gulls(P, pts, col=(40, 52, 64)):
    for (x, y, s) in pts:
        P.line([(x - 18 * s, y - 6 * s), (x - 8 * s, y - 12 * s), (x, y), (x + 8 * s, y - 12 * s), (x + 18 * s, y - 6 * s)], w=3, alpha=0.7, color=col)


def banana_leaf(P, cx, cy, ang, length, width, col=(24, 80, 74)):
    ts = np.linspace(0, 1, 14)
    left, right = [], []
    for t in ts:
        px = cx + np.sin(ang) * length * t + np.sin(t * 3.0) * 8
        py = cy - np.cos(ang) * length * t + (t ** 2) * 40
        w = width * np.sin(np.pi * (0.12 + 0.88 * t)) ** 0.8
        nx, ny = np.cos(ang), np.sin(ang)
        left.append((px - nx * w, py - ny * w))
        right.append((px + nx * w, py + ny * w))
    P.layer(poly(left + right[::-1]), col, op=0.96, wob=4, rim=0.3)
    P.line([(cx + np.sin(ang) * length * t, cy - np.cos(ang) * length * t + (t ** 2) * 40) for t in ts], w=2, alpha=0.35, color=(10, 34, 34))


def hydrangea(P, cx, cy, r=46, col=(84, 124, 206), seed=1):
    leafy(P, cx, cy + 16, r * 1.2, (24, 70, 68), n=10, seed=seed)
    rr = np.random.default_rng(seed)
    for _ in range(10):
        a = rr.uniform(0, 6.28)
        d = rr.uniform(0, r * 0.8)
        P.layer(ell(cx + np.cos(a) * d, cy + np.sin(a) * d * 0.7, 11, 10), col, op=0.95, wob=1.5, rim=0.3)
        P.layer(ell(cx + np.cos(a) * d - 3, cy + np.sin(a) * d * 0.7 - 3, 5, 4), tuple(min(255, c + 60) for c in col), op=0.7, wob=1, rim=0)


def fern(P, fx, fy, n=9, size=90, col=(30, 94, 74)):
    for k in range(n):
        a = -2.6 + k * (5.2 / max(1, n - 1)) * 0.4 * (n / 9 + 0.0)
        pts = [(fx, fy), (fx + np.cos(a) * size, fy + np.sin(a) * size * 0.66 - 20)]
        P.layer(shape(lambda d, pts=pts: d.line(pts, fill=255, width=7)), col, op=0.9, wob=2, rim=0.2, soft=0.8)


def laurel_trunks(P, trunks, leaf_col=(22, 70, 64)):
    for (x, w, top, col) in trunks:
        P.layer(poly([(x - w / 2, SH + 5), (x - w * 0.35, top), (x + w * 0.35, top), (x + w / 2, SH + 5)]), col, op=0.98, wob=3, rim=0.25)
        leafy(P, x, top + 10, 150 if w > 30 else 110, leaf_col, n=34, seed=int(x))


# ----------------------------------------------------------------- mobiliário
def room_bg(P, col=PAPER_WALL):
    P.layer(rect(-5, -5, SW + 5, SH + 5), col, op=1.0, wob=0, rim=0, vary=0.2)


def window_frame(P, x0, y0, x1, y1, sky_top=NAVY, sky_bot=(30, 82, 96), stars=0, seed=2, frame=(110, 78, 50), cross=True):
    P.vgrad(y0, y1, sky_top, sky_bot, mask=rect(x0, y0, x1, y1), wob=1.5, rim=0.3)
    if stars:
        P.stars(stars, int(y1 - 60), seed=seed)
    t = 8
    for a, b, c, d in [(x0 - t, y0 - t, x0, y1 + t), (x1, y0 - t, x1 + t, y1 + t), (x0 - t, y0 - t, x1 + t, y0), (x0 - t, y1, x1 + t, y1 + t + 4)]:
        P.layer(rect(a, b, c, d), frame, op=0.97, wob=1.2, rim=0.25)
    if cross:
        P.layer(rect((x0 + x1) / 2 - 4, y0, (x0 + x1) / 2 + 4, y1), frame, op=0.97, wob=1.2, rim=0.25)
        P.layer(rect(x0, (y0 + y1) / 2 - 4, x1, (y0 + y1) / 2 + 4), frame, op=0.97, wob=1.2, rim=0.25)


def table(P, x0, x1, ytop, legs=True, col=WOOD_T, ybot=SH + 5):
    P.layer(rect(x0, ytop, x1, ytop + 30), col, op=0.98, wob=2, rim=0.3)
    P.layer(rect(x0, ytop + 30, x1, ytop + 56), WOOD_D, op=0.98, wob=2, rim=0.25)
    if legs:
        P.layer(rect(x0 + 50, ytop + 56, x0 + 78, ybot), (84, 56, 34), op=0.98, wob=2, rim=0.25)
        P.layer(rect(x1 - 78, ytop + 56, x1 - 50, ybot), (84, 56, 34), op=0.98, wob=2, rim=0.25)


def chair(P, x, base, h=330, facing=0, c=WOOD_X):
    P.layer(rect(x - 52, base - h * 0.42, x + 52, base - h * 0.42 + 16), c, op=0.98, wob=1.5, rim=0.25)
    P.layer(rect(x - 48, base - h * 0.42, x - 36, base), c, op=0.98, wob=1.5)
    P.layer(rect(x + 36, base - h * 0.42, x + 48, base), c, op=0.98, wob=1.5)
    P.layer(rect(x - 48, base - h, x - 38, base - h * 0.42), c, op=0.98, wob=1.5)
    P.layer(rect(x + 38, base - h, x + 48, base - h * 0.42), c, op=0.98, wob=1.5)
    for k in range(3):
        yy = base - h + 14 + k * 30
        P.layer(rect(x - 48, yy, x + 48, yy + 10), c, op=0.98, wob=1.5)


def lamp(P, x, ybase, h=110, g=0.7, shade=(252, 214, 130)):
    P.layer(ell(x, ybase, 46, 8), (60, 42, 28), op=0.97, wob=1)
    P.layer(rect(x - 4, ybase - h, x + 4, ybase), (60, 42, 28), op=0.97, wob=1)
    P.layer(ell(x, ybase - h - 24, 38, 44), shade, op=0.97, wob=1.5, rim=0.15)
    P.glow(x, ybase - h - 24, 90, (255, 235, 170), g)
    P.glow(x, ybase - h, 260, WARM, 0.35)


def candle(P, x, y, h=34):
    P.layer(rect(x - 3, y - h, x + 3, y), (246, 236, 214), op=0.98, wob=0.6)
    P.glow(x, y - h - 8, 22, (255, 240, 180), 1.0)
    P.glow(x, y - h - 8, 90, WARM, 0.35)
    P.layer(ell(x, y - h - 8, 3, 7), (255, 232, 140), op=1.0, wob=0.3)


def cup(P, x, y, w=70, steam=True, col=CREAM):
    P.layer(poly([(x - w / 2, y - 46), (x + w / 2, y - 46), (x + w / 2 - 10, y), (x - w / 2 + 10, y)]), col, op=0.98, wob=1.2, rim=0.3)
    P.layer(ell(x, y - 46, w / 2, 6), (210, 180, 130), op=0.98, wob=1)
    P.layer(rrect(x + w / 2 - 2, y - 36, x + w / 2 + 20, y - 14, 8), col, op=0.95, wob=1)
    if steam:
        for k in range(3):
            xs = np.linspace(0, 1, 30)
            pts = [(x - 6 + 12 * (k - 1) + 8 * np.sin(t * 9 + k), y - 52 - t * 70) for t in xs]
            P.layer(shape(lambda d, pts=pts: d.line(pts, fill=255, width=4)), (240, 232, 215), op=0.35, wob=1, rim=0, soft=2.2)


def book(P, x, y, w=140, open_=True, col=CREAM):
    if open_:
        P.layer(poly([(x - w / 2, y), (x, y - 10), (x, y + 6), (x - w / 2 + 4, y + 14)]), col, op=0.98, wob=0.8)
        P.layer(poly([(x, y - 10), (x + w / 2, y), (x + w / 2 - 4, y + 14), (x, y + 6)]), (228, 212, 172), op=0.98, wob=0.8)
        for k in range(3):
            P.line([(x - w / 2 + 14, y + 1 + k * 3), (x - 8, y - 4 + k * 3)], w=1, alpha=0.3)
            P.line([(x + 8, y - 4 + k * 3), (x + w / 2 - 14, y + 1 + k * 3)], w=1, alpha=0.3)
    else:
        P.layer(rect(x - w / 2, y - 18, x + w / 2, y), (120, 60, 44), op=0.98, wob=0.8, rim=0.3)
        P.layer(rect(x - w / 2 + 6, y - 14, x + w / 2 - 2, y - 4), col, op=0.95, wob=0.6)


def phone(P, x, y, w=88, lit=True, face_down=False, tilt=0):
    h = w * 0.56
    P.layer(poly([(x - w / 2, y - h / 2 + tilt), (x + w / 2, y - h / 2 - tilt), (x + w / 2 + 6, y + h / 2), (x - w / 2 + 6, y + h / 2 + tilt)]),
            (24, 26, 34), op=0.98, wob=0.8, rim=0.3)
    if lit and not face_down:
        P.glow(x, y, w * 1.1, (120, 170, 230), 0.35)
        P.layer(poly([(x - w / 2 + 8, y - h / 2 + 6), (x + w / 2 - 6, y - h / 2 + 4), (x + w / 2 - 2, y + h / 2 - 6), (x - w / 2 + 12, y + h / 2 - 4)]),
                (130, 176, 226), op=0.95, wob=0.6, rim=0)


def clock_round(P, x, y, r=60, hands=(0.3, 0.9), face=CREAM):
    P.layer(ell(x, y, r + 8, r + 8), (70, 48, 30), op=0.98, wob=1)
    P.layer(ell(x, y, r, r), face, op=0.98, wob=0.8, rim=0.2)
    for k in range(12):
        a = k * np.pi / 6
        P.line([(x + np.sin(a) * r * 0.82, y - np.cos(a) * r * 0.82), (x + np.sin(a) * r * 0.92, y - np.cos(a) * r * 0.92)], w=2, alpha=0.6)
    for frac, ln, wd in [(hands[0], 0.5, 4), (hands[1], 0.78, 3)]:
        a = frac * 2 * np.pi
        P.line([(x, y), (x + np.sin(a) * r * ln, y - np.cos(a) * r * ln)], w=wd, alpha=0.8)


def letter(P, x, y, w=150, tilt=-0.05, stamp=True):
    h = w * 0.62
    pts = [(x - w / 2, y - h / 2), (x + w / 2, y - h / 2 + w * tilt), (x + w / 2, y + h / 2 + w * tilt), (x - w / 2, y + h / 2)]
    P.layer(poly(pts), (240, 232, 208), op=0.98, wob=0.8, rim=0.3)
    P.line([(x - w / 2, y - h / 2), (x, y + w * tilt * 0.2), (x + w / 2, y - h / 2 + w * tilt)], w=2, alpha=0.4)
    for k in range(3):
        P.line([(x - w * 0.35, y + h * 0.08 + k * 10), (x + w * 0.1, y + h * 0.08 + k * 10 + w * tilt * 0.3)], w=1, alpha=0.4)
    if stamp:
        P.layer(rect(x + w / 2 - 34, y - h / 2 + 8, x + w / 2 - 8, y - h / 2 + 32), (176, 98, 62), op=0.95, wob=0.6)


def pot_plant(P, x, y, s=1.0, kind="geranium", seed=1):
    P.layer(poly([(x - 28 * s, y - 44 * s), (x + 28 * s, y - 44 * s), (x + 20 * s, y), (x - 20 * s, y)]), (176, 98, 62), op=0.98, wob=1.2, rim=0.3)
    if kind == "sprout":
        P.layer(rect(x - 2 * s, y - 44 * s - 38 * s, x + 2 * s, y - 44 * s), (60, 120, 80), op=0.97, wob=0.8)
        P.layer(ell(x - 14 * s, y - 44 * s - 36 * s, 16 * s, 8 * s), (74, 140, 92), op=0.97, wob=0.8, rim=0.2)
        P.layer(ell(x + 14 * s, y - 44 * s - 42 * s, 16 * s, 8 * s), (86, 150, 100), op=0.97, wob=0.8, rim=0.2)
    else:
        leafy(P, x, y - 70 * s, 40 * s, (40, 98, 70), n=10, seed=seed)
        r = np.random.default_rng(seed)
        for _ in range(6):
            P.layer(ell(x + r.uniform(-26, 26) * s, y - 86 * s + r.uniform(-18, 12) * s, 8 * s, 8 * s), (206, 96, 78), op=0.95, wob=1, rim=0.3)


def lantern(P, x, y, s=1.0, g=0.9):
    P.layer(rrect(x - 20 * s, y - 28 * s, x + 20 * s, y + 28 * s, 6), (255, 226, 140), op=0.98, wob=0.5, rim=0.15)
    P.layer(rect(x - 22 * s, y - 32 * s, x + 22 * s, y - 26 * s), (50, 36, 28), op=0.98, wob=0.6)
    P.layer(rect(x - 22 * s, y + 26 * s, x + 22 * s, y + 32 * s), (50, 36, 28), op=0.98, wob=0.6)
    P.glow(x, y, 60 * s, WARM, g)
    P.glow(x, y, 150 * s, (255, 200, 110), 0.3)


def door(P, x0, y0, x1, y1, lit=True, ajar=0.0, frame=(70, 46, 30)):
    if lit:
        P.vgrad(y0, y1, (255, 214, 130), (232, 160, 70), mask=rect(x0, y0, x1, y1), wob=1.5, rim=0.35)
        P.glow((x0 + x1) / 2, (y0 + y1) / 2 + 40, (x1 - x0) * 0.8, WARM, 0.8)
    else:
        P.layer(rect(x0, y0, x1, y1), (24, 56, 66), op=1.0, wob=1.5, rim=0.35)
    if ajar:
        w = (x1 - x0) * ajar
        P.layer(poly([(x0, y0), (x0 + w, y0 + 14), (x0 + w, y1 - 6), (x0, y1)]), (96, 64, 38), op=0.98, wob=1.2, rim=0.3)
    t = 12
    P.layer(rect(x0 - t, y0 - t, x0, y1), frame, op=0.98, wob=1.2)
    P.layer(rect(x1, y0 - t, x1 + t, y1), frame, op=0.98, wob=1.2)
    P.layer(rect(x0 - t, y0 - t, x1 + t, y0 + 2), frame, op=0.98, wob=1.2)


def boat(P, x, y, s=1.0, lit=False, hull=(150, 60, 48), sail=False):
    P.layer(poly([(x - 90 * s, y - 20 * s), (x + 100 * s, y - 24 * s), (x + 70 * s, y + 14 * s), (x - 70 * s, y + 14 * s)]), hull, op=0.98, wob=1.2, rim=0.3)
    P.layer(rect(x - 90 * s, y - 24 * s, x + 100 * s, y - 18 * s), (232, 216, 180), op=0.98, wob=0.8)
    P.layer(rect(x - 20 * s, y - 52 * s, x + 30 * s, y - 22 * s), (226, 214, 184), op=0.98, wob=0.8, rim=0.2)
    P.layer(rect(x - 14 * s, y - 46 * s, x + 6 * s, y - 32 * s), (60, 80, 92), op=0.95, wob=0.5)
    if lit:
        P.glow(x - 4 * s, y - 40 * s, 30 * s, WARM, 0.9)
        P.layer(rect(x - 14 * s, y - 46 * s, x + 6 * s, y - 32 * s), WARM, op=0.98, wob=0.5)
    P.layer(rect(x + 56 * s - 2, y - 120 * s, x + 56 * s + 2, y - 22 * s), (70, 52, 36), op=0.97, wob=0.6)
    if sail:
        P.layer(poly([(x + 60 * s, y - 118 * s), (x + 60 * s, y - 26 * s), (x + 130 * s, y - 28 * s)]), (240, 230, 206), op=0.97, wob=1, rim=0.2)
    P.layer(ell(x, y + 18 * s, 100 * s, 5 * s), (8, 22, 44), op=0.35, wob=0, rim=0, soft=3)


def suitcase(P, x, y, s=1.0, col=(120, 70, 44)):
    P.layer(rrect(x - 70 * s, y - 80 * s, x + 70 * s, y, 8), col, op=0.98, wob=1, rim=0.3)
    P.layer(rect(x - 70 * s, y - 56 * s, x + 70 * s, y - 50 * s), (70, 40, 26), op=0.9, wob=0.6)
    P.layer(rrect(x - 26 * s, y - 100 * s, x + 26 * s, y - 80 * s, 6), (70, 40, 26), op=0.98, wob=0.8)
    P.layer(rect(x - 6 * s, y - 62 * s, x + 6 * s, y - 44 * s), GOLD, op=0.95, wob=0.5)


def ochre_coat_folded(P, x, y, w=120):
    P.layer(poly([(x - w / 2, y), (x + w / 2, y), (x + w / 2 + 10, y - 30), (x + w / 2 - 6, y - 56), (x - w / 2 + 6, y - 58), (x - w / 2 - 10, y - 30)]),
            OCHRE, op=0.98, wob=2, rim=0.3)
    P.layer(poly([(x - w / 2 + 6, y - 40), (x + w / 2 - 6, y - 40), (x + w / 2 - 6, y - 56), (x - w / 2 + 6, y - 58)]), (222, 164, 70), op=0.9, wob=1.5, rim=0.1)


def stone_stairs(P, x0, x1, ytop, ybot, steps=7, col=(112, 100, 84)):
    h = (ybot - ytop) / steps
    for i in range(steps):
        yy = ytop + i * h
        inset = i * (x1 - x0) * 0.04
        P.layer(rect(x0 + inset, yy, x1 - inset, yy + h), tuple(int(c * (0.78 + 0.05 * i)) for c in col), op=0.98, wob=1.5, rim=0.3, vary=0.18)
        P.layer(rect(x0 + inset, yy, x1 - inset, yy + 7), tuple(min(255, int(c * 1.25)) for c in col), op=0.9, wob=1, rim=0.1)


def bench(P, x, y, w=240, col=(96, 66, 40)):
    P.layer(rect(x - w / 2, y - 30, x + w / 2, y - 14), col, op=0.98, wob=1.5, rim=0.3)
    P.layer(rect(x - w / 2 + 14, y - 14, x - w / 2 + 30, y), col, op=0.98, wob=1.5)
    P.layer(rect(x + w / 2 - 30, y - 14, x + w / 2 - 14, y), col, op=0.98, wob=1.5)
    P.layer(rect(x - w / 2, y - 90, x + w / 2, y - 76), col, op=0.98, wob=1.5, rim=0.3)
    P.layer(rect(x - w / 2 + 20, y - 76, x - w / 2 + 32, y - 30), col, op=0.98, wob=1.5)
    P.layer(rect(x + w / 2 - 32, y - 76, x + w / 2 - 20, y - 30), col, op=0.98, wob=1.5)


def string_lights(P, x0, x1, y, sag=30, n=11):
    pts = [(x0 + (x1 - x0) * t, y + sag * np.sin(np.pi * t)) for t in np.linspace(0, 1, 40)]
    P.line(pts, w=2, alpha=0.5)
    for i in range(n):
        t = (i + 0.5) / n
        x = x0 + (x1 - x0) * t
        yy = y + sag * np.sin(np.pi * t)
        P.glow(x, yy + 8, 20, WARM, 0.95)
        P.layer(ell(x, yy + 8, 5, 6), (255, 232, 150), op=0.98, wob=0.3)


def foam(P, x0, x1, y, n=40, seed=1, col=(236, 240, 232)):
    r = np.random.default_rng(seed)
    for _ in range(n):
        P.layer(ell(r.uniform(x0, x1), y + r.uniform(-8, 12), r.uniform(20, 70), r.uniform(2, 6)), col, op=r.uniform(0.35, 0.8), wob=1, rim=0, soft=1.2)


def tree_pine(P, x, ybase, h, col=(24, 70, 66)):
    P.layer(rect(x - 6, ybase - h * 0.4, x + 6, ybase), (70, 50, 36), op=0.98, wob=1.5)
    leafy(P, x, ybase - h * 0.7, h * 0.35, col, n=24, seed=int(x))
