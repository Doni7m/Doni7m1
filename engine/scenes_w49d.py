"""Cenas 29/11/2026: Marco Aurélio (r29) - mudança e aceitar o que passa."""
import re
from lib4 import *

NIGHT_ROOM = (22, 44, 56)
LEAF_COLS = [(206, 120, 52), (190, 84, 56), (222, 170, 70), (150, 100, 50)]


def leaves(P, n, x0, x1, y0, y1, seed=1, size=(7, 13), cols=LEAF_COLS, op=0.9):
    r = np.random.default_rng(seed)
    for _ in range(n):
        x, y = r.uniform(x0, x1), r.uniform(y0, y1)
        a = r.uniform(0, 3.14)
        L, W = r.uniform(*size), r.uniform(*size) * 0.45
        c = cols[r.integers(len(cols))]
        P.layer(poly([(x - L * np.cos(a), y - L * np.sin(a)), (x + W * np.sin(a), y - W * np.cos(a)),
                      (x + L * np.cos(a), y + L * np.sin(a)), (x - W * np.sin(a), y + W * np.cos(a))]),
                tuple(int(v * r.uniform(0.85, 1.1)) for v in c), op=op, wob=0.6, rim=0.2)


def lighthouse(P, x, ybase, h, w=44):
    top = ybase - h
    P.layer(poly([(x - w, ybase), (x - w * 0.6, top), (x + w * 0.6, top), (x + w, ybase)]), (236, 226, 204), op=0.98, wob=1, rim=0.3)
    for k in (0.25, 0.6):
        y0 = ybase - h * k
        P.layer(poly([(x - w * (1 - 0.4 * k), y0), (x + w * (1 - 0.4 * k), y0), (x + w * (1 - 0.4 * (k + 0.12)), y0 - h * 0.12),
                      (x - w * (1 - 0.4 * (k + 0.12)), y0 - h * 0.12)]), (170, 64, 52), op=0.95, wob=0.8)
    P.layer(rect(x - w * 0.75, top - 6, x + w * 0.75, top + 4), (50, 40, 36), op=0.98, wob=0.8)
    P.layer(rect(x - w * 0.45, top - 36, x + w * 0.45, top - 6), (255, 226, 140), op=0.98, wob=0.6, rim=0.15)
    P.layer(poly([(x - w * 0.6, top - 36), (x, top - 62), (x + w * 0.6, top - 36)]), (60, 44, 38), op=0.98, wob=0.8)
    P.glow(x, top - 22, 90, WARM, 0.9)
    P.glow(x, top - 22, 260, (255, 210, 120), 0.3)


def arm(P, x0, y0, x1, y1, col=OCHRE, t=16, hand=True):
    P.layer(poly([(x0, y0 - t / 2), (x1, y1 - t / 2), (x1, y1 + t / 2), (x0, y0 + t / 2)]), tuple(int(c * 0.85) for c in col), op=0.98, wob=1, rim=0.25)
    if hand:
        P.layer(ell(x1, y1, 11, 9), SKIN, op=0.98, wob=0.6, rim=0.2)


# ================================================================== 1: capa
def r29a1():
    P = Paint(9701)
    backdrop(P, "dusk", 230, sunp=(820, 215, 30), seed=9701, clouds=2)
    hill_houses(P, 380, SW + 10, 240, n=8, seed=91, lit=True)
    hill_houses(P, 200, SW + 10, 340, n=9, seed=92, lit=True, body=(138, 148, 144))
    P.layer(rect(-5, 470, SW + 5, SH + 5), (60, 78, 62), op=1.0, wob=3, rim=0.2)
    big_tree(P, 170, 480, 300, lean=0.05, leaf=(196, 112, 50), seed=5, crown=0.55)
    leaves(P, 40, 40, 520, 200, 560, seed=3)
    stone_wall(P, 520, 700, seed=12, base=(92, 84, 74))
    person(P, 640, 525, 250, coat=OCHRE, profile=0.5)
    leaves(P, 26, 300, 900, 380, 520, seed=4)
    return fin(P, 9702)


# ================================================================== 2: saudade quieta
def r29a2():
    P = Paint(9711)
    room_bg(P, NIGHT_ROOM)
    floor(P, 520, (60, 42, 32))
    window_frame(P, 560, 60, 900, 360, sky_top=NAVY, sky_bot=(30, 82, 96), stars=26, seed=9)
    hill_houses(P, 565, 895, 270, n=4, seed=95, lit=True)
    table(P, 740, 1040, 430)
    lamp(P, 820, 434, h=120)
    letter(P, 930, 430, w=130)
    letter(P, 960, 424, w=110, tilt=0.08, stamp=False)
    suitcase(P, 150, 600, 1.5)
    suitcase(P, 330, 590, 1.1, col=(90, 80, 60))
    person(P, 470, 600, 275, coat=OCHRE, profile=0.7)
    P.glow(720, 330, 220, WARM, 0.25)
    return fin(P, 9712)


# ================================================================== 3: contra o vento
def r29a3():
    P = Paint(9721)
    backdrop(P, "storm", 250, seed=9721, clouds=3)
    P.strokes(0, SW, 80, 220, 40, (200, 214, 214), op=0.2, wmin=120, wmax=300, hmax=3, seed=4)
    cliff(P, "right", top=380, seed=37, col=(24, 52, 58), reach=700)
    foam(P, 0, 480, 520, n=34, seed=8)
    foam(P, 0, 600, 600, n=30, seed=9)
    P.strokes(0, 700, 300, 520, 26, (214, 226, 224), op=0.22, wmin=80, wmax=240, hmax=3, seed=7)
    person(P, 930, 398, 230, coat=OCHRE, profile=-0.6)
    lantern(P, 862, 345, 0.8)
    arm(P, 905, 375, 868, 350, hand=True)
    gulls(P, [(220, 150, 1.1), (380, 120, 0.9), (150, 90, 0.8)])
    leaves(P, 18, 350, 800, 250, 400, seed=6, size=(6, 10))
    return fin(P, 9722)


# ================================================================== 4: natureza das coisas
def r29a4():
    P = Paint(9731)
    backdrop(P, "dusk", 300, sunp=(330, 290, 36), seed=9731, clouds=5)
    cliff(P, "right", top=330, seed=40, col=(20, 46, 54), reach=480)
    lighthouse(P, 880, 335, 170)
    for i, y in enumerate((380, 430, 490, 560, 620)):
        foam(P, 0, 640 + i * 40, y, n=10 + i * 4, seed=20 + i)
        P.strokes(0, SW, y - 12, y + 14, 12, (150, 190, 196), op=0.2, wmin=60, wmax=180, hmax=2, seed=30 + i)
    gulls(P, [(560, 150, 1.0), (620, 120, 0.8), (500, 190, 0.7)])
    return fin(P, 9732)


# ================================================================== 5: dois caminhos
def r29a5():
    P = Paint(9741)
    backdrop(P, "day", 200, seed=9741, clouds=2)
    hill_houses(P, -10, SW + 10, 215, n=9, seed=96, lit=False)
    P.layer(rect(-5, 330, SW + 5, SH + 5), (72, 120, 82), op=1.0, wob=3, rim=0.2, vary=0.2)
    P.layer(poly(ridge(318, 20, 11)), (60, 108, 76), op=0.98, wob=2)
    # caminho esquerdo (coberto de folhas) e direito (livre)
    P.layer(poly([(470, SH + 5), (300, SH + 5), (170, 400), (260, 340), (400, 340), (500, 420)]), (150, 134, 108), op=0.98, wob=2, rim=0.3, vary=0.15)
    P.layer(poly([(590, SH + 5), (780, SH + 5), (960, 400), (860, 340), (720, 340), (570, 420)]), (190, 178, 150), op=0.98, wob=2, rim=0.3, vary=0.15)
    P.layer(poly([(470, SH + 5), (590, SH + 5), (570, 420), (500, 420)]), (170, 156, 128), op=0.98, wob=2, rim=0.3)
    leaves(P, 150, 200, 440, 350, 640, seed=7, size=(8, 15))
    leaves(P, 12, 700, 900, 400, 600, seed=8)
    P.glow(840, 380, 160, WARM, 0.35)
    person(P, 535, 470, 200, coat=OCHRE, profile=0.2)
    pot_plant(P, 980, 560, 1.2, seed=4)
    hydrangea(P, 100, 580, 52, seed=3)
    return fin(P, 9742)


# ================================================================== 6: luto e companhia
def r29a6():
    P = Paint(9751)
    backdrop(P, "night", 290, moonp=(760, 120, 30), seed=9751, clouds=1)
    P.layer(poly([(-10, 470), (300, 470), (420, SH + 5), (-10, SH + 5)]), (28, 52, 58), op=1.0, wob=3, rim=0.3, vary=0.15)
    boulder(P, 90, 520, 90, 50)
    pier(P, 330, SW + 5, 470)
    foam(P, 0, 500, 580, n=24, seed=12)
    a_x, b_x, yb = 560, 650, 472
    person(P, b_x, yb, 235, coat=BLUE_COAT, profile=-0.5)
    person(P, a_x, yb, 250, coat=OCHRE, profile=0.5)
    sh_a = yb - 250 + 2 * 0.062 * 250 + 0.03 * 250
    sh_b = yb - 235 + 2 * 0.062 * 235 + 0.03 * 235
    arm(P, a_x + 34, sh_a + 6, b_x - 26, sh_b + 4, hand=True)
    P.layer(rect(840 - 3, 380, 840 + 3, 470), (60, 50, 42), op=0.97, wob=0.8)
    lantern(P, 840, 360, 1.2)
    return fin(P, 9752)


# ================================================================== 7: passa o que pesa
def r29a7():
    P = Paint(9761)
    backdrop(P, "dusk", 290, sunp=(520, 285, 56), seed=9761, clouds=2)
    P.glow(520, 290, 420, GOLD, 0.35)
    hill_houses(P, 560, SW + 10, 320, n=7, seed=97, lit=True)
    hill_houses(P, 640, SW + 10, 410, n=6, seed=98, lit=True, body=(150, 156, 148))
    stone_wall(P, 520, 700, seed=14, base=(96, 86, 74), x0=-5, x1=560)
    P.layer(poly([(-10, 520), (560, 520), (700, SH + 5), (-10, SH + 5)]), (88, 80, 70), op=1.0, wob=2, rim=0.2)
    person(P, 300, 522, 270, coat=OCHRE, profile=0.1)
    lantern(P, 430, 480, 0.8)
    pot_plant(P, 80, 520, 1.2, seed=6)
    gulls(P, [(700, 150, 1.1), (800, 190, 0.9), (620, 110, 0.8)])
    leaves(P, 12, 380, 900, 80, 300, seed=11, size=(6, 9))
    return fin(P, 9762)


# ================================================================== imagem única: soltar
def r29b():
    P = Paint(9771)
    backdrop(P, "dawn", 270, sunp=(300, 255, 40), seed=9771, clouds=3)
    boat(P, 300, 345, 0.8, sail=True)
    pier(P, 560, SW + 5, 480)
    P.layer(rect(1000, 440, 1012, 480), (60, 50, 42), op=0.95, wob=1)
    P.line([(566, 486), (520, 520), (470, 548), (420, 540), (380, 520)], w=3, alpha=0.7, color=(70, 52, 36))
    foam(P, 0, 600, 540, n=26, seed=13)
    foam(P, 0, SW, 600, n=26, seed=14)
    person(P, 790, 484, 250, coat=OCHRE, profile=-0.5)
    arm(P, 756, 272 + 0, 680, 255, hand=True)
    gulls(P, [(560, 160, 1.2), (640, 120, 1.0), (730, 170, 0.9), (460, 120, 0.8)])
    leaves(P, 7, 560, 700, 190, 300, seed=15, size=(8, 12))
    return fin(P, 9772)


SCENES = {n: f for n, f in globals().items() if re.match(r"^r\d\d", n) and callable(f)}
