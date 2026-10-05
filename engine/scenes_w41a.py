"""Cenas semana 06-11/10/2026 — parte A (terça e quarta)."""
from lib2 import *


def fin(P, seed):
    return P.finish(top=30, bottom=34, left=45, right=45, feather=70, seed=seed)


def inv(m):
    return ImageChops.invert(m)


def cave(P, cx, cy, rx, ry, rock=(30, 34, 40)):
    P.layer(inv(ell(cx, cy, rx, ry)), rock, op=1.0, wob=4, rim=0.3, vary=0.2)


# ================= TERÇA A — Platão (caverna) =================
def tue_a1():
    P = Paint(1101)
    backdrop(P, "dawn", 330, sunp=(540, 300, 46), seed=1101, clouds=2)
    cave(P, 540, 330, 380, 250)
    P.layer(rect(-5, 540, SW + 5, SH + 5), (38, 38, 42), op=1.0, wob=2, rim=0.2)
    person(P, 540, 560, 190)
    return fin(P, 1102)


def tue_a2():
    P = Paint(1111)
    P.layer(rect(-5, -5, SW + 5, SH + 5), (60, 52, 46), op=1.0, wob=2, rim=0, vary=0.2)
    P.layer(rect(120, 60, 960, 400), (232, 200, 140), op=0.97, wob=3, rim=0.25, vary=0.18)
    P.glow(540, 220, 340, WARM, 0.5)
    for (x, y, h) in [(300, 330, 150), (480, 340, 190), (700, 320, 140), (860, 335, 170)]:
        P.layer(ell(x, y - h * 0.8, h * 0.13, h * 0.17), (44, 30, 22), op=0.82, wob=2, rim=0)
        P.layer(poly([(x - h * .2, y), (x - h * .12, y - h * .62), (x + h * .12, y - h * .62), (x + h * .2, y)]), (44, 30, 22), op=0.82, wob=2, rim=0)
    for x in (260, 540, 820):
        person(P, x, 660, 230, sit=True, coat=(70, 62, 66), hair=(26, 22, 24))
    return fin(P, 1112)


def tue_a3():
    P = Paint(1121)
    backdrop(P, "day", 340, seed=1121, clouds=1)
    P.glow(540, 300, 380, (255, 244, 205), 0.8)
    cave(P, 540, 310, 340, 230)
    P.layer(rect(-5, 520, SW + 5, SH + 5), (40, 40, 44), op=1.0, wob=2, rim=0.2)
    x, h = person(P, 560, 560, 210, profile=-0.3)
    P.layer(rect(x - 36, h + 10, x - 10, h + 28), (246, 214, 170), op=0.95, wob=1)
    return fin(P, 1122)


def tue_a4():
    P = Paint(1131)
    backdrop(P, "dawn", 340, sunp=(700, 330, 52), seed=1131, clouds=3, island=(130, 320))
    cliff(P, "left", top=300, seed=3, col=(40, 56, 60), reach=420)
    person(P, 250, 520, 200)
    return fin(P, 1132)


def tue_a5():
    P = Paint(1141)
    backdrop(P, "dawn", 320, sunp=(840, 316, 40), seed=1141, clouds=2)
    P.layer(poly(ridge(380, 40, 11)), (62, 108, 92), op=0.98, wob=3)
    P.layer(rect(-5, 450, SW + 5, SH + 5), (52, 98, 72), op=1.0, wob=2, rim=0.15, vary=0.2)
    P.layer(ell(480, 530, 120, 36), (120, 112, 100), op=0.98, wob=2, rim=0.3, vary=0.2)
    person(P, 480, 540, 170, sit=True)
    hydrangea(P, 200, 560, 50, seed=3)
    hydrangea(P, 860, 570, 46, seed=8)
    return fin(P, 1142)


def tue_a6():
    P = Paint(1151)
    backdrop(P, "day", 320, seed=1151, clouds=3, island=(700, 300))
    P.layer(poly(ridge(380, 40, 13)), (60, 110, 96), op=0.98, wob=3)
    P.layer(rect(-5, 450, SW + 5, SH + 5), (60, 104, 76), op=1.0, wob=2, rim=0.15, vary=0.2)
    P.layer(poly([(360, 645), (620, 645), (600, 470), (560, 460)]), (176, 146, 104), op=0.97, wob=3, rim=0.25)
    person(P, 450, 620, 210, coat=OCHRE)
    person(P, 560, 600, 190, coat=(150, 70, 60), hair=(60, 40, 30))
    return fin(P, 1152)


def tue_a7():
    P = Paint(1161)
    backdrop(P, "dawn", 350, sunp=(540, 340, 60), seed=1161, clouds=3, island=(800, 300))
    P.layer(poly([(-10, 520), (420, 500), (560, 560), (640, 645), (-10, 645)]), (24, 46, 52), op=1.0, wob=3, rim=0.3, vary=0.2)
    person(P, 260, 520, 190)
    gulls(P, [(700, 120, 1.0), (780, 90, 0.9), (850, 130, 1.0)])
    return fin(P, 1162)


# ================= TERÇA B — Heráclito (rio) =================
def tue_b():
    P = Paint(1201)
    P.vgrad(-5, 340, (92, 148, 172), (232, 226, 200), mask=rect(-5, -5, SW + 5, 340), wob=2, rim=0, vary=0.07)
    P.layer(poly(ridge(300, 60, 21)), (40, 92, 84), op=0.98, wob=3)
    P.layer(rect(-5, 330, SW + 5, SH + 5), (52, 98, 72), op=1.0, wob=2, rim=0.15, vary=0.2)
    # rio sinuoso
    for k in range(50):
        t = k / 49
        x = 430 + 140 * np.sin(t * 4.2) * (0.3 + t * 0.7)
        y = 330 + t * 320
        P.layer(ell(x, y, 40 + 130 * t, 12 + 30 * t), (70, 140, 160), op=0.95, wob=2, rim=0.1, soft=1.2)
    P.strokes(150, 950, 380, 640, 70, (236, 244, 240), op=0.35, wmin=20, wmax=80)
    for (x, y) in [(150, 560), (900, 540)]:
        fern(P, x, y, n=9, size=100)
    person(P, 180, 640, 210, profile=0.4)
    return fin(P, 1202)


# ================= QUARTA A — Nietzsche (vida que repetiria) =================
def wed_a1():
    P = Paint(1301)
    room_bg(P, (22, 54, 66))
    window_frame(P, 360, 70, 720, 420, sky_top=(58, 108, 128), sky_bot=(246, 212, 156))
    P.glow(540, 330, 260, WARM, 0.5)
    table(P, 220, 860, 460)
    cup(P, 540, 460, 70)
    person(P, 300, 645, 300, sit=True, profile=0.3)
    return fin(P, 1302)


def wed_a2():
    P = Paint(1311)
    backdrop(P, "dusk", 330, sunp=(150, 300, 30), seed=1311, clouds=2)
    for i, (x, y, r, c) in enumerate([(300, 280, 26, 0.9), (460, 250, 28, 0.8), (620, 225, 30, 0.7), (780, 205, 32, 0.6), (930, 190, 34, 0.5)]):
        P.layer(ell(x, y, r, r), (252, 226, 160), op=c, wob=1.5, rim=0.05)
        P.glow(x, y, r * 3, GOLD, c * 0.4)
    P.layer(poly([(-10, 520), (350, 510), (480, 560), (560, 645), (-10, 645)]), (24, 46, 52), op=1.0, wob=3, rim=0.3, vary=0.2)
    person(P, 200, 520, 190)
    return fin(P, 1312)


def wed_a3():
    P = Paint(1321)
    room_bg(P, (30, 62, 70))
    window_frame(P, 700, 90, 980, 380, sky_top=(58, 108, 128), sky_bot=(246, 212, 156))
    table(P, 120, 1000, 470)
    cup(P, 420, 470, 80)
    book(P, 620, 468, 160)
    lamp(P, 200, 470, h=120)
    pot_plant(P, 900, 470, 1.0, seed=2)
    return fin(P, 1322)


def wed_a4():
    P = Paint(1331)
    backdrop(P, "dusk", 340, sunp=(640, 330, 56), seed=1331, clouds=3, island=(90, 300))
    P.layer(poly([(-10, 500), (470, 480), (620, 560), (700, 645), (-10, 645)]), (24, 46, 52), op=1.0, wob=3, rim=0.3, vary=0.2)
    person(P, 380, 500, 210)
    return fin(P, 1332)


def wed_a5():
    P = Paint(1341)
    backdrop(P, "day", 300, seed=1341, clouds=2, island=(700, 300))
    P.layer(rect(-5, 400, SW + 5, SH + 5), (52, 98, 72), op=1.0, wob=2, rim=0.15, vary=0.2)
    for k in range(40):
        t = k / 39
        x = 250 + 560 * t + 40 * np.sin(t * 6)
        y = 640 - 200 * t
        P.layer(ell(x, y, 70 * (1 - t) + 14, 16 * (1 - t) + 4), (176, 146, 104), op=0.97, wob=2, rim=0.1, soft=1.2)
    person(P, 300, 620, 230)
    hydrangea(P, 140, 560, 50, seed=5)
    return fin(P, 1342)


def wed_a6():
    P = Paint(1351)
    room_bg(P, (28, 60, 70))
    window_frame(P, 100, 70, 420, 400, sky_top=(58, 108, 128), sky_bot=(246, 212, 156))
    table(P, 60, 1020, 470)
    cup(P, 640, 470, 76)
    book(P, 820, 468, 160)
    candle(P, 520, 470)
    pot_plant(P, 940, 470, 0.9, seed=4)
    return fin(P, 1352)


def wed_a7():
    P = Paint(1361)
    backdrop(P, "dusk", 340, sunp=(540, 336, 60), seed=1361, clouds=3)
    P.layer(rect(-5, 500, SW + 5, SH + 5), (86, 80, 72), op=1.0, wob=2, rim=0.25, vary=0.2)
    P.layer(rect(-5, 500, SW + 5, 524), (140, 128, 108), op=1.0, wob=1.5, rim=0.2)
    table(P, 700, 1000, 560)
    cup(P, 850, 560, 70)
    person(P, 400, 645, 300, sit=True)
    return fin(P, 1362)


# ================= QUARTA B — Aristóteles (para quê?) =================
def wed_b():
    P = Paint(1401)
    backdrop(P, "dawn", 330, sunp=(600, 322, 44), seed=1401, clouds=3, island=(60, 300))
    boat(P, 600, 440, 1.3, sail=True)
    gulls(P, [(300, 120, 1.0), (370, 90, 0.9), (440, 130, 1.0)])
    return fin(P, 1402)


SCENES = {k: v for k, v in dict(globals()).items() if (k.startswith("tue_") or k.startswith("wed_")) and callable(v)}
