"""Cenas 25-26/11/2026: Arendt (r25, recomeço) e Kierkegaard (r26, vertigem da escolha)."""
import re
from lib4 import *

NIGHT_ROOM = (22, 44, 56)
GRASS = (84, 130, 86)
EARTH = (96, 66, 44)
PATH = (196, 168, 118)


def sample(pts, step):
    """Pontos igualmente espaçados ao longo de uma polilinha, com direção."""
    out = []
    acc = 0.0
    for (x0, y0), (x1, y1) in zip(pts[:-1], pts[1:]):
        L = float(np.hypot(x1 - x0, y1 - y0))
        d = acc
        while d < L:
            t = d / L
            out.append((x0 + (x1 - x0) * t, y0 + (y1 - y0) * t, x1 - x0, y1 - y0))
            d += step
        acc = d - L
    return out


def strip(P, pts, w0, w1, col, edge=None, op=0.98, n=60):
    """Faixa (caminho) ao longo de pts; largura w0 no início e w1 no fim."""
    xs = np.interp(np.linspace(0, len(pts) - 1, n), range(len(pts)), [p[0] for p in pts])
    ys = np.interp(np.linspace(0, len(pts) - 1, n), range(len(pts)), [p[1] for p in pts])
    L, R = [], []
    for i in range(n):
        j = min(i + 1, n - 1)
        k = max(i - 1, 0)
        dx, dy = xs[j] - xs[k], ys[j] - ys[k]
        ln = max(1e-6, float(np.hypot(dx, dy)))
        nx, ny = -dy / ln, dx / ln
        w = (w0 + (w1 - w0) * i / (n - 1)) / 2
        L.append((xs[i] + nx * w, ys[i] + ny * w))
        R.append((xs[i] - nx * w, ys[i] - ny * w))
    if edge:
        E = [(x + (x - xs[i]) * 0.14, y + (y - ys[i]) * 0.14) for i, (x, y) in enumerate(L)]
        F = [(x + (x - xs[i]) * 0.14, y + (y - ys[i]) * 0.14) for i, (x, y) in enumerate(R)]
        P.layer(poly(E + F[::-1]), edge, op=op, wob=2, rim=0.2)
    P.layer(poly(L + R[::-1]), col, op=op, wob=2, rim=0.25, vary=0.15)


def footprints(P, pts, step=34, s=1.0, col=(120, 84, 56), op=0.55, ssh=1.0):
    for i, (x, y, dx, dy) in enumerate(sample(pts, step)):
        ln = max(1e-6, float(np.hypot(dx, dy)))
        nx, ny = -dy / ln, dx / ln
        side = 1 if i % 2 else -1
        k = float(s) * (1 + ssh * (y - 300) / 800)
        px, py = x + nx * side * 9 * k, y + ny * side * 9 * k * 0.6
        P.layer(ell(px, py, 5 * k, 9 * k * 0.8), col, op=op, wob=1, rim=0.15, soft=0.8)
        P.layer(ell(px - dx / ln * 7 * k, py - dy / ln * 5 * k, 3.4 * k, 4 * k * 0.8), col, op=op * 0.9, wob=1, rim=0.1, soft=0.8)


def mist(P, x, y, w, h, col=(236, 232, 220), op=0.45, n=3, seed=1):
    r = np.random.default_rng(seed)
    for _ in range(n):
        P.layer(ell(x + r.uniform(-w * 0.3, w * 0.3), y + r.uniform(-h, h), w * r.uniform(0.5, 0.8), h * r.uniform(0.5, 1.0)),
                col, op=op, wob=3, rim=0, soft=14)


def watering_can(P, x, y, s=1.0):
    P.layer(poly([(x - 40 * s, y - 56 * s), (x + 30 * s, y - 56 * s), (x + 34 * s, y), (x - 44 * s, y)]), (74, 120, 132), op=0.98, wob=1.2, rim=0.3)
    P.layer(poly([(x + 30 * s, y - 40 * s), (x + 110 * s, y - 100 * s), (x + 116 * s, y - 92 * s), (x + 34 * s, y - 20 * s)]), (74, 120, 132), op=0.98, wob=1, rim=0.25)
    P.layer(ell(x + 118 * s, y - 100 * s, 12 * s, 7 * s), (56, 96, 108), op=0.98, wob=0.8)
    P.layer(shape(lambda d: d.arc([x - 62 * s, y - 100 * s, x - 6 * s, y - 20 * s], 180, 360, fill=255, width=int(8 * s))), (74, 120, 132), op=0.98, wob=1)
    P.layer(rect(x - 44 * s, y - 62 * s, x + 30 * s, y - 52 * s), (96, 150, 160), op=0.95, wob=0.8)


def pen(P, x, y, ang=0.3, ln=120):
    dx, dy = np.cos(ang) * ln / 2, np.sin(ang) * ln / 2
    P.layer(poly([(x - dx, y - dy - 3), (x + dx, y + dy - 3), (x + dx, y + dy + 3), (x - dx, y - dy + 3)]), (40, 44, 60), op=0.98, wob=0.5, rim=0.2)
    P.layer(poly([(x + dx, y + dy - 3), (x + dx + 14, y + dy + 5), (x + dx, y + dy + 3)]), (200, 170, 90), op=0.98, wob=0.4)


def night_room(P, sky_top=NAVY, sky_bot=(30, 82, 96), win=(720, 70, 980, 330), stars=30, wall=NIGHT_ROOM, fl=(62, 44, 34)):
    room_bg(P, wall)
    floor(P, 560, fl)
    window_frame(P, *win, sky_top=sky_top, sky_bot=sky_bot, stars=stars, seed=5)


# ============================================================ 25/11 Arendt: natalidade, recomeço
def r25a1():
    P = Paint(9301)
    backdrop(P, "dawn", 290, sunp=(700, 270, 44), seed=9301, clouds=2)
    far_island(P, 290, (120, 260))
    terrace(P, 340, 150, (74, 120, 80), seed=3)
    P.layer(poly(ridge(450, 26, 9, x0=-30, x1=SW + 30, step=60) + [(SW + 30, SH + 5), (-30, SH + 5)]), EARTH, op=1.0, wob=3, rim=0.3, vary=0.2)
    for x, y, rx in [(250, 540, 50), (800, 560, 60), (420, 600, 40), (680, 610, 36)]:
        P.layer(ell(x, y, rx, rx * 0.22), (70, 46, 30), op=0.5, wob=2, rim=0, soft=2)
    P.glow(540, 420, 170, WARM, 0.3)
    sapling(P, 540, 490, 200, leaf=(92, 164, 98))
    P.layer(ell(540, 494, 54, 12), (120, 86, 58), op=0.98, wob=2, rim=0.25)
    for dx in (-110, 130):
        sapling(P, 540 + dx, 520 - abs(dx) * 0.0, 0, leaf=(80, 140, 90))
    gulls(P, [(300, 140, 1.0), (380, 110, 0.8)])
    return fin(P, 9302)


def r25a2():
    P = Paint(9311)
    backdrop(P, "dusk", 210, sunp=(850, 200, 28), seed=9311, clouds=1)
    hill_houses(P, -10, SW + 10, 220, n=8, seed=91, lit=True)
    P.layer(poly(ridge(330, 16, 12, x0=-30, x1=SW + 30, step=60) + [(SW + 30, SH + 5), (-30, SH + 5)]), (52, 96, 76), op=0.98, wob=3, rim=0.25)
    # caminho de pedra que recomeça: um trecho termina numa pedra e outro começa mais adiante
    strip(P, [(430, 645), (470, 590), (490, 545)], 170, 110, (170, 142, 100), edge=(110, 90, 62), n=30)
    strip(P, [(520, 500), (530, 430), (536, 350)], 80, 34, PATH, edge=(120, 100, 70), n=30)
    for (x, y, w) in [(525, 380, 30), (522, 430, 44), (510, 490, 60), (480, 560, 90), (445, 620, 120)]:
        P.layer(ell(x, y, w * 0.5, w * 0.14), (224, 200, 154), op=0.7, wob=1, rim=0.2, soft=0.8)
    for x, y, w in [(500, 522, 18), (520, 518, 14)]:
        P.layer(ell(x, y, w, w * 0.5), (150, 130, 96), op=0.9, wob=1, rim=0.2)
    # marco de pedra no inicio do novo caminho
    boulder(P, 640, 450, 30, 22, col=(128, 120, 104))
    boulder(P, 700, 500, 46, 30, col=(110, 104, 94))
    person(P, 270, 600, 270, coat=OCHRE, profile=0.3)
    return fin(P, 9312)


def r25a3():
    P = Paint(9321)
    backdrop(P, "day", 150, seed=9321, clouds=2)
    P.layer(poly(ridge(210, 20, 5, x0=-30, x1=SW + 30, step=60) + [(SW + 30, SH + 5), (-30, SH + 5)]), (92, 140, 90), op=0.98, wob=3, rim=0.25)
    for k, (yy, col) in enumerate([(320, (82, 130, 84)), (440, (72, 118, 78)), (540, (64, 106, 72))]):
        terrace(P, yy, 100 + k * 6, col, seed=k + 3)
    way = [(260, 600), (760, 548), (330, 470), (700, 400), (420, 340), (560, 262)]
    strip(P, way, 100, 34, PATH, edge=(124, 100, 66), n=90)
    footprints(P, way, step=30, s=1.0)
    P.layer(ell(560, 252, 30, 8), (60, 40, 28), op=0.3, wob=1, rim=0, soft=3)
    person(P, 566, 258, 92, coat=OCHRE, profile=0.2)
    return fin(P, 9322)


def r25a4():
    P = Paint(9331)
    backdrop(P, "dawn", 300, sunp=(560, 290, 62), seed=9331, clouds=3, island=(740, 280))
    P.glow(560, 300, 300, WARM, 0.25)
    boat(P, 590, 470, 1.5, sail=True, hull=(150, 60, 48))
    foam(P, 330, 880, 495, n=26, seed=3)
    cliff(P, "left", top=500, seed=51, col=(18, 44, 52), reach=330)
    gulls(P, [(860, 150, 1.1), (940, 190, 0.8), (210, 200, 0.9)])
    return fin(P, 9332)


def r25a5():
    P = Paint(9341)
    night_room(P, sky_top=(120, 170, 190), sky_bot=(250, 214, 156), win=(110, 70, 450, 330), stars=0, wall=(58, 84, 88))
    P.glow(280, 260, 300, WARM, 0.35)
    table(P, 120, 960, 430)
    letter(P, 540, 452, w=300, tilt=0.0, stamp=False)
    P.layer(rect(400, 440, 560, 442), (200, 190, 160), op=0.0)
    pen(P, 640, 446, ang=0.35, ln=140)
    cup(P, 800, 436, steam=True)
    P.glow(540, 430, 140, (255, 230, 170), 0.2)
    return fin(P, 9342)


def r25a6():
    P = Paint(9351)
    backdrop(P, "day", 170, seed=9351, clouds=2)
    hill_houses(P, -10, SW + 10, 170, n=9, seed=93, lit=False, body=(176, 164, 136))
    stone_wall(P, 280, 640, seed=11, base=(96, 88, 78), x0=-5, x1=270)
    stone_wall(P, 280, 640, seed=12, base=(96, 88, 78), x0=810, x1=SW + 5)
    stone_stairs(P, 260, 820, 260, 628, steps=8)
    hydrangea(P, 150, 400, 56, seed=7)
    hydrangea(P, 930, 420, 60, seed=8, col=(120, 150, 214))
    person(P, 470, 470, 200, coat=OCHRE, profile=0.2)
    person(P, 580, 470, 196, coat=BLUE_COAT, profile=-0.2)
    P.layer(ell(530, 474, 130, 8), (30, 24, 20), op=0.0)
    return fin(P, 9352)


def r25a7():
    P = Paint(9361)
    night_room(P, sky_top=(236, 176, 110), sky_bot=(255, 232, 170), win=(100, 70, 420, 330), stars=0, wall=(70, 70, 64))
    P.glow(260, 240, 340, (255, 214, 130), 0.5)
    table(P, 100, 980, 450, col=(168, 120, 70))
    pot_plant(P, 540, 452, 2.6, kind="sprout")
    watering_can(P, 760, 450, 1.2)
    cup(P, 300, 446, steam=True)
    P.glow(540, 380, 200, (255, 220, 140), 0.35)
    return fin(P, 9362)


def r25b():
    P = Paint(9371)
    backdrop(P, "night", 250, moonp=(780, 110, 26), seed=9371, island=(560, 340))
    cobbles(P, 340, glow_x=560, seed=9)
    stone_wall(P, 300, 640, seed=21, base=(60, 62, 62), x0=-5, x1=330)
    stone_wall(P, 340, 640, seed=22, base=(60, 62, 62), x0=780, x1=SW + 5)
    leafy(P, 120, 280, 90, (22, 70, 64), n=24, seed=5)
    leafy(P, 960, 330, 80, (26, 76, 66), n=22, seed=6)
    P.glow(540, 520, 230, WARM, 0.3)
    person(P, 520, 610, 260, coat=OCHRE, profile=0.2)
    lantern(P, 608, 470, 1.1)
    return fin(P, 9372)


# ============================================================ 26/11 Kierkegaard: vertigem da liberdade
def r26a1():
    P = Paint(9401)
    backdrop(P, "day", 230, seed=9401, clouds=3, island=(660, 340))
    foam(P, 520, 1000, 590, n=30, seed=7)
    foam(P, 620, 1000, 520, n=18, seed=8)
    cliff(P, "left", top=420, seed=61, col=(110, 104, 88), reach=560)
    P.layer(poly(ridge(412, 8, 3, x0=-10, x1=260, step=30) + [(260, 462), (-10, 480)]), (84, 130, 86), op=0.98, wob=2, rim=0.25)
    person(P, 150, 450, 230, coat=OCHRE, profile=0.5)
    gulls(P, [(700, 380, 1.2), (820, 420, 1.0)])
    return fin(P, 9402)


def r26a2():
    P = Paint(9411)
    room_bg(P, (16, 40, 50))
    stone_wall(P, 140, 560, seed=14, base=(72, 66, 62))
    cobbles(P, 540, glow_x=540)
    door(P, 190, 170, 380, 540, lit=True, ajar=0.35)
    door(P, 700, 170, 890, 540, lit=True, ajar=0.35)
    P.glow(300, 360, 200, (252, 190, 100), 0.25)
    P.glow(800, 360, 200, (150, 210, 214), 0.28)
    pot_plant(P, 540, 546, 1.0, seed=4)
    person(P, 540, 620, 260, coat=OCHRE, profile=0.1)
    return fin(P, 9412)


def r26a3():
    P = Paint(9421)
    backdrop(P, "dusk", 170, sunp=(820, 160, 30), seed=9421, clouds=1)
    hill_houses(P, -10, SW + 10, 170, n=9, seed=95, lit=True)
    hill_houses(P, -10, SW + 10, 280, n=11, seed=96, lit=True, body=(132, 146, 144))
    P.layer(poly(ridge(380, 14, 17, x0=-30, x1=SW + 30, step=60) + [(SW + 30, SH + 5), (-30, SH + 5)]), (56, 98, 74), op=0.98, wob=3, rim=0.25)
    base = (540, 590)
    for tgt, w1 in [((170, 400), 30), ((520, 360), 20), ((930, 410), 30), ((330, 300), 14)]:
        mid = ((base[0] + tgt[0]) / 2 + (tgt[1] - base[1]) * 0.1, (base[1] + tgt[1]) / 2)
        strip(P, [base, mid, tgt], 110, w1, (190, 164, 116), edge=(116, 92, 62), n=50)
        for t in np.linspace(0.12, 0.92, 8):
            x = (1 - t) ** 2 * base[0] + 2 * (1 - t) * t * mid[0] + t * t * tgt[0]
            y = (1 - t) ** 2 * base[1] + 2 * (1 - t) * t * mid[1] + t * t * tgt[1]
            P.layer(rect(x - 30 * (1 - t) - 6, y - 2, x + 30 * (1 - t) + 6, y + 2), (110, 90, 64), op=0.5, wob=1)
    person(P, 540, 612, 150, coat=OCHRE, profile=0.1)
    return fin(P, 9422)


def r26a4():
    P = Paint(9431)
    backdrop(P, "storm", 300, seed=9431)
    for k, (yy, col) in enumerate([(210, (92, 122, 126)), (260, (64, 96, 104)), (320, (40, 74, 84))]):
        P.layer(poly(ridge(yy, 40, 30 + k, x0=-30, x1=SW + 30, step=50) + [(SW + 30, yy + 220), (-30, yy + 220)]), col, op=0.97, wob=3, rim=0.2)
        mist(P, 540, yy + 90, 560, 30, op=0.55, n=3, seed=k + 2)
    mist(P, 540, 440, 600, 40, op=0.6, n=4, seed=9)
    # miradouro de pedra
    P.layer(poly([(-10, 520), (SW + 10, 520), (SW + 10, SH + 5), (-10, SH + 5)]), (104, 96, 84), op=1.0, wob=2, rim=0.3, vary=0.18)
    P.layer(rect(-10, 512, SW + 10, 532), (150, 140, 120), op=1.0, wob=1.5, rim=0.3)
    for x in range(40, SW, 150):
        P.layer(rect(x, 440, x + 22, 516), (126, 116, 100), op=0.98, wob=1.2, rim=0.3)
    P.layer(rect(-10, 436, SW + 10, 452), (140, 130, 112), op=0.98, wob=1.5, rim=0.3)
    person(P, 500, 590, 250, coat=OCHRE, profile=0.2)
    return fin(P, 9432)


def r26a5():
    P = Paint(9441)
    night_room(P, sky_top=(120, 170, 190), sky_bot=(246, 226, 180), win=(740, 70, 980, 320), stars=0, wall=(34, 62, 72))
    table(P, 110, 970, 440)
    # calendário em folha, um dia circulado
    P.layer(rect(250, 320, 650, 436), (244, 236, 212), op=0.98, wob=0.8, rim=0.3)
    P.layer(rect(250, 320, 650, 348), (176, 98, 62), op=0.98, wob=0.8)
    for i in range(1, 7):
        P.line([(250 + i * 400 / 7, 348), (250 + i * 400 / 7, 436)], w=1, alpha=0.35)
    for j in range(1, 3):
        P.line([(250, 348 + j * 29), (650, 348 + j * 29)], w=1, alpha=0.35)
    P.layer(ell(250 + 400 / 7 * 3.5, 348 + 29 * 1.5, 22, 16), (226, 160, 64), op=0.85, wob=1, rim=0.3)
    P.layer(ell(250 + 400 / 7 * 3.5, 348 + 29 * 1.5, 14, 9), (244, 236, 212), op=0.9, wob=0.8)
    pen(P, 740, 436, ang=-0.1, ln=130)
    cup(P, 850, 432, steam=True)
    lamp(P, 160, 440, h=120)
    P.glow(450, 380, 180, WARM, 0.25)
    return fin(P, 9442)


def r26a6():
    P = Paint(9451)
    room_bg(P, (36, 40, 44))
    stone_wall(P, 80, 560, seed=15, base=(66, 60, 56))
    window_frame(P, 100, 120, 400, 380, sky_top=NAVY, sky_bot=(60, 100, 112), stars=14, seed=3)
    string_lights(P, 60, 1020, 70, sag=34, n=13)
    floor(P, 560, (62, 44, 34))
    table(P, 320, 820, 430, legs=True)
    candle(P, 570, 430, h=44)
    P.glow(570, 380, 220, WARM, 0.5)
    cup(P, 450, 428, steam=True)
    cup(P, 690, 428, steam=True)
    chair(P, 270, 610, 280)
    chair(P, 870, 610, 280)
    person(P, 280, 600, 260, sit=True, coat=OCHRE, profile=0.7)
    person(P, 860, 600, 255, sit=True, coat=BLUE_COAT, profile=-0.7)
    return fin(P, 9452)


def r26a7():
    P = Paint(9461)
    backdrop(P, "dawn", 260, sunp=(300, 250, 38), seed=9461, clouds=2, island=(520, 300))
    foam(P, 80, 600, 560, n=24, seed=5)
    P.layer(poly(ridge(330, 20, 41, x0=-30, x1=SW + 30, step=60) + [(SW + 30, SH + 5), (-30, SH + 5)]), (70, 112, 78), op=0.98, wob=3, rim=0.25)
    P.layer(poly([(-30, 520), (200, 470), (480, 520), (620, SH + 5), (-30, SH + 5)]), (36, 82, 90), op=0.0)
    way = [(240, 640), (440, 560), (640, 480), (800, 420), (930, 380)]
    strip(P, way, 150, 50, (184, 156, 110), edge=(112, 90, 60), n=70)
    for i in range(8):
        x, y = 100 + i * 50, 520 + 26 * np.sin(i)
        P.layer(poly([(x, y + 40), (x + 6, y), (x + 12, y + 40)]), (60, 110, 70), op=0.9, wob=1)
    fern(P, 120, 600, n=7, size=70)
    P.glow(300, 300, 240, WARM, 0.25)
    person(P, 560, 540, 230, coat=OCHRE, profile=0.5)
    gulls(P, [(780, 150, 1.0), (860, 190, 0.8)])
    return fin(P, 9462)


def r26b():
    P = Paint(9471)
    P.vgrad(-5, 330, (92, 148, 172), (200, 220, 206), mask=rect(-5, -5, SW + 5, 330), wob=2, rim=0, vary=0.07)
    # paredão verde da encosta
    P.layer(poly([(-10, -10), (SW + 10, -10), (SW + 10, 330), (760, 260), (620, 90), (470, 90), (340, 270), (-10, 330)]), (28, 70, 62), op=1.0, wob=3, rim=0.3, vary=0.2)
    P.layer(poly([(-10, 200), (340, 270), (470, 90), (460, 440), (-10, 440)]), (22, 60, 56), op=0.9, wob=3, rim=0.25)
    leafy(P, 160, 220, 130, (30, 90, 70), n=36, seed=3)
    leafy(P, 930, 200, 140, (34, 96, 72), n=36, seed=4)
    waterfall(P, 540, 100, 420, w0=46, w1=140)
    P.glow(540, 420, 120, (230, 244, 240), 0.35)
    # rio
    P.vgrad(410, 645, (74, 150, 156), (28, 80, 96), mask=rect(-5, 410, SW + 5, 645), wob=2, rim=0.1)
    P.strokes(0, SW, 440, 630, 60, (190, 226, 226), op=0.3, seed=11)
    P.strokes(0, SW, 440, 630, 40, (14, 50, 70), op=0.25, seed=12)
    rock_pool(P, 280, 560, 90, 24)
    foam(P, 440, 650, 420, n=20, seed=4)
    boulder(P, 120, 440, 120, 60, col=(92, 92, 86))
    boulder(P, 960, 470, 150, 70, col=(96, 94, 86))
    boulder(P, 770, 540, 100, 40, col=(110, 104, 92))
    fern(P, 150, 420, n=8, size=70)
    person(P, 770, 528, 190, coat=OCHRE, sit=False, profile=0.4)
    return fin(P, 9472)


SCENES = {n: f for n, f in globals().items() if re.match(r"^r\d\d", n) and callable(f)}
