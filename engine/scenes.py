import os
import numpy as np
from PIL import ImageChops
from paint import *


def scene1():
    """Homem de costas diante de uma janela, mar e casas iluminadas lá fora."""
    P = Paint(11)
    sky(P, -5, 400, NAVY, (30, 82, 96))
    P.stars(90, 300, seed=21)
    moon(P, 640, 140, 30)
    sea(P, 380, SH + 5, DTEAL, NAVY, seed=30)
    moon_reflection(P, 640, 392, 600, seed=31)
    # hillside right with houses
    P.layer(poly(ridge(430, 60, 7, x0=420)), (22, 52, 62), op=0.97, wob=3)
    for i, (x, y, w, h) in enumerate([(470, 470, 52, 38), (560, 500, 46, 34), (640, 478, 58, 40), (730, 520, 50, 36),
                                      (410, 540, 44, 32), (520, 580, 56, 40), (690, 585, 54, 38)]):
        house(P, x, y, w, h, body=(120, 138, 140), seed=i)
    # window opening (arch) -> wall painted outside of it
    win = shape(lambda d: (d.rectangle([330, 150, 790, 650], fill=255), d.ellipse([330, 20, 790, 280], fill=255)))
    wall = ImageChops.invert(win)
    P.layer(wall, (12, 40, 52), op=1.0, wob=2, rim=0.3, vary=0.18, soft=1.2)
    # window frame + mullions
    for x0, y0, x1, y1 in [(330, 150, 342, 640), (778, 150, 790, 640), (550, 20, 566, 640), (330, 330, 790, 342), (330, 480, 790, 492)]:
        P.layer(rect(x0, y0, x1, y1), (18, 36, 66), op=0.97, wob=1.2, rim=0.2)
    P.layer(shape(lambda d: d.arc([330, 20, 790, 280], 180, 360, fill=255, width=14)), (18, 36, 66), op=0.97, wob=1.2)
    # sill
    P.layer(rect(290, 600, 830, 640), (30, 56, 72), op=0.97, wob=1.5)
    P.line([(330, 150), (330, 640)], w=2, alpha=0.5)
    P.line([(790, 150), (790, 640)], w=2, alpha=0.5)
    P.glow(560, 330, 200, (120, 150, 190), 0.10)
    person(P, 470, 636, 430)
    return P.finish(top=30, bottom=34, left=45, right=45, feather=70, seed=12)


def scene2():
    """Mesa à noite: lâmpada, chá, celular virado para baixo, cadeira vazia."""
    P = Paint(21)
    P.layer(rect(-5, -5, SW + 5, SH + 5), (14, 46, 60), op=1.0, wob=0, rim=0, vary=0.2)
    # window with night
    P.vgrad(60, 340, NAVY, (30, 82, 96), mask=rect(700, 60, 990, 340), wob=1.5, rim=0.3)
    P.stars(14, 200, seed=22)
    P.layer(ell(930, 130, 20, 20), (240, 226, 190), op=0.95, wob=1)
    P.glow(930, 130, 60, GOLD, 0.25)
    for x0, y0, x1, y1 in [(692, 52, 700, 348), (990, 52, 998, 348), (692, 52, 998, 60), (692, 340, 998, 348), (840, 52, 848, 348)]:
        P.layer(rect(x0, y0, x1, y1), (110, 78, 50), op=0.97, wob=1.2, rim=0.25)
    # warm light wash
    P.glow(330, 420, 300, WARM, 0.45)
    # table
    P.layer(rect(60, 480, 1020, 512), (150, 104, 62), op=0.98, wob=2, rim=0.3)
    P.layer(rect(60, 512, 1020, 540), (96, 64, 38), op=0.98, wob=2, rim=0.25)
    P.layer(rect(120, 540, 148, 645), (84, 56, 34), op=0.98, wob=2, rim=0.25)
    P.layer(rect(930, 540, 958, 645), (84, 56, 34), op=0.98, wob=2, rim=0.25)
    P.glow(330, 485, 140, WARM, 0.5)
    # lamp
    P.layer(ell(330, 478, 46, 8), (60, 42, 28), op=0.97, wob=1)
    P.layer(rect(326, 400, 334, 478), (60, 42, 28), op=0.97, wob=1)
    P.layer(ell(330, 372, 38, 44), (252, 214, 130), op=0.97, wob=1.5, rim=0.15)
    P.glow(330, 372, 70, (255, 235, 170), 0.7)
    P.line([(330, 328), (330, 416)], w=2, alpha=0.2, color=(120, 80, 30))
    # cup + steam
    P.layer(poly([(470, 434), (542, 434), (532, 480), (480, 480)]), CREAM, op=0.98, wob=1.2, rim=0.3)
    P.layer(ell(506, 434, 36, 6), (210, 180, 130), op=0.98, wob=1)
    P.layer(rrect(540, 444, 562, 466, 8), CREAM, op=0.95, wob=1)
    for k in range(3):
        xs = np.linspace(0, 1, 30)
        pts = [(500 + 12 * (k - 1) + 8 * np.sin(t * 9 + k), 428 - t * 70) for t in xs]
        P.layer(shape(lambda d, pts=pts: d.line(pts, fill=255, width=4)), (240, 232, 215), op=0.35, wob=1, rim=0, soft=2.2)
    # phone, face down
    P.layer(poly([(640, 468), (722, 464), (730, 480), (648, 484)]), (24, 26, 34), op=0.98, wob=0.8, rim=0.3)
    P.line([(640, 468), (722, 464), (730, 480), (648, 484), (640, 468)], w=2, alpha=0.5)
    # chairs (empty)
    def chair(x, base, h, tilt=0):
        c = (74, 50, 32)
        P.layer(rect(x - 52, base - h * 0.42, x + 52, base - h * 0.42 + 16), c, op=0.98, wob=1.5, rim=0.25)
        P.layer(rect(x - 48, base - h * 0.42, x - 36, base), c, op=0.98, wob=1.5)
        P.layer(rect(x + 36, base - h * 0.42, x + 48, base), c, op=0.98, wob=1.5)
        P.layer(rect(x - 48, base - h, x - 38, base - h * 0.42), c, op=0.98, wob=1.5)
        P.layer(rect(x + 38, base - h, x + 48, base - h * 0.42), c, op=0.98, wob=1.5)
        for k in range(3):
            yy = base - h + 14 + k * 30
            P.layer(rect(x - 48, yy, x + 48, yy + 10), c, op=0.98, wob=1.5)
    chair(220, 636, 330)
    chair(830, 640, 330)
    return P.finish(top=30, bottom=34, left=45, right=45, feather=70, seed=23)


def scene3():
    """Caminho de pedra na falésia, figura pequena, mar prateado lá embaixo."""
    P = Paint(31)
    sky(P, -5, 330, NAVY, (28, 78, 92))
    P.stars(130, 300, seed=32)
    moon(P, 840, 90, 20)
    sea(P, 320, SH + 5, (28, 84, 98), NAVY, seed=33)
    moon_reflection(P, 840, 332, 520, n=22, seed=34)
    # far headland and village lights
    P.layer(poly([(520, 336), (600, 318), (690, 306), (790, 304), (890, 312), (990, 308), (1090, 318), (1090, 338), (520, 338)]), (18, 44, 58), op=0.97, wob=2)
    r = np.random.default_rng(5)
    for _ in range(16):
        x, y = r.uniform(700, 1040), r.uniform(318, 334)
        P.glow(x, y, 5, WARM, 0.9)
    # cliff mass (foreground)
    cliff = [(-10, 240), (140, 262), (300, 320), (430, 410), (560, 515), (690, 645), (-10, 645)]
    P.layer(poly(cliff), (10, 28, 40), op=1.0, wob=3, rim=0.3, vary=0.2)
    # lighter rock facets
    for pts, col in [([(0, 300), (150, 330), (260, 420), (80, 470)], (24, 52, 62)),
                     ([(120, 520), (300, 470), (420, 560), (260, 640), (80, 640)], (18, 44, 54)),
                     ([(380, 500), (520, 540), (600, 640), (440, 640)], (30, 60, 70))]:
        P.layer(poly(pts), col, op=0.9, wob=3, rim=0.3)
    # path along the cliff edge
    path = [(20, 248), (140, 268), (300, 326), (430, 412), (555, 512), (590, 524), (452, 424), (322, 340), (150, 285), (30, 266)]
    P.layer(poly(path), (176, 150, 112), op=0.96, wob=2, rim=0.25)
    P.layer(poly([(40, 252), (140, 270), (150, 278), (50, 262)]), (200, 174, 128), op=0.7, wob=1)
    for i in range(14):
        t = i / 13
        x = 30 + t * 520 + r.normal(0, 4)
        y = 258 + (t ** 1.15) * 260
        P.layer(ell(x, y, r.uniform(7, 15), r.uniform(3, 6)), (140, 118, 88), op=0.35, wob=1)
    # lone walker
    person(P, 372, 392, 112)
    return P.finish(top=30, bottom=34, left=45, right=45, feather=70, seed=35)


def scene4():
    """Cômodo iluminado nos fundos de uma casa de pedra; luz sobre as pedras do chão."""
    P = Paint(41)
    sky(P, -5, 480, NAVY, (40, 96, 108))
    P.stars(60, 200, seed=42)
    # ground
    P.layer(rect(-5, 470, SW + 5, SH + 5), (28, 52, 56), op=1.0, wob=2, rim=0.1)
    # house wall
    P.layer(rect(500, 120, SW + 5, SH + 5), (98, 88, 78), op=1.0, wob=2, rim=0.3, vary=0.2)
    P.layer(poly([(470, 130), (790, 40), (SW + 5, 40), (SW + 5, 130)]), (60, 40, 36), op=0.98, wob=2, rim=0.3)
    r = np.random.default_rng(8)
    for _ in range(80):
        x, y = r.uniform(510, 1070), r.uniform(150, 470)
        P.layer(rect(x, y, x + r.uniform(24, 60), y + r.uniform(10, 18)), tuple(int(v * r.uniform(0.82, 1.12)) for v in (104, 94, 82)),
                op=0.5, wob=1, rim=0.2, soft=0.8)
    # doorway with warm interior
    P.vgrad(250, 640, (255, 214, 130), (232, 160, 70), mask=rect(650, 250, 840, 640), wob=1.5, rim=0.35)
    P.glow(745, 430, 150, WARM, 0.8)
    # desk + book + candle inside
    P.layer(rect(662, 500, 832, 515), (122, 82, 48), op=0.98, wob=1)
    P.layer(rect(666, 515, 676, 600), (90, 60, 36), op=0.98, wob=1)
    P.layer(rect(818, 515, 828, 600), (90, 60, 36), op=0.98, wob=1)
    P.layer(poly([(690, 498), (748, 492), (752, 500), (694, 506)]), CREAM, op=0.98, wob=0.8)
    P.layer(poly([(750, 492), (790, 498), (788, 505), (752, 500)]), (228, 212, 172), op=0.98, wob=0.8)
    P.layer(rect(800, 470, 806, 500), (246, 236, 214), op=0.98, wob=0.6)
    P.glow(803, 462, 18, (255, 240, 180), 1.0)
    P.layer(ell(803, 462, 3, 7), (255, 232, 140), op=1.0, wob=0.3)
    # door frame
    P.layer(rect(642, 242, 654, 645), (70, 46, 30), op=0.98, wob=1.2)
    P.layer(rect(836, 242, 848, 645), (70, 46, 30), op=0.98, wob=1.2)
    P.layer(rect(642, 242, 848, 256), (70, 46, 30), op=0.98, wob=1.2)
    # light spill on cobbles
    spill = poly([(650, 520), (840, 520), (980, 645), (440, 645)])
    P.layer(spill, (252, 206, 120), op=0.42, wob=3, rim=0, soft=6)
    for _ in range(170):
        x, y = r.uniform(-10, SW), r.uniform(500, 640)
        near = 1 - min(1, abs(x - 745) / 380)
        base = np.array([62, 80, 84]) * (1 - near) + np.array([188, 150, 92]) * near
        col = tuple(int(v * r.uniform(0.8, 1.15)) for v in base)
        P.layer(ell(x, y, r.uniform(12, 30), r.uniform(5, 11)), col, op=0.75, wob=1, rim=0.25, soft=0.8)
    # garden: banana leaves, hydrangeas
    def banana(cx, cy, ang, length, width, col):
        ts = np.linspace(0, 1, 14)
        left, right = [], []
        for t in ts:
            px = cx + np.sin(ang) * length * t + np.sin(t * 3.0) * 8
            py = cy - np.cos(ang) * length * t + (t ** 2) * 40
            w = width * np.sin(np.pi * (0.12 + 0.88 * t)) ** 0.8
            nx, ny = np.cos(ang), np.sin(ang)
            left.append((px - nx * w, py - ny * w)); right.append((px + nx * w, py + ny * w))
        P.layer(poly(left + right[::-1]), col, op=0.96, wob=4, rim=0.3)
        P.line([(cx + np.sin(ang) * length * t, cy - np.cos(ang) * length * t + (t ** 2) * 40) for t in ts], w=2, alpha=0.35, color=(10, 34, 34))
    for (cx, cy, ang, ln, wd, col) in [(120, 520, -0.55, 330, 70, (24, 80, 74)), (210, 540, 0.15, 380, 78, (30, 94, 82)),
                                       (300, 540, 0.75, 300, 66, (22, 72, 70)), (60, 540, -1.0, 250, 58, (28, 86, 78))]:
        banana(cx, cy, ang, ln, wd, col)
    for (cx, cy, rr) in [(430, 470, 46), (350, 500, 40), (480, 520, 38)]:
        leafy(P, cx, cy + 20, rr * 1.2, (24, 70, 68), n=10, seed=cx)
        for k in range(10):
            a = r.uniform(0, 6.28)
            d = r.uniform(0, rr * 0.8)
            P.layer(ell(cx + np.cos(a) * d, cy + np.sin(a) * d * 0.7, 11, 10), (84, 124, 206), op=0.95, wob=1.5, rim=0.3)
            P.layer(ell(cx + np.cos(a) * d - 3, cy + np.sin(a) * d * 0.7 - 3, 5, 4), (150, 180, 236), op=0.7, wob=1, rim=0)
    P.line([(500, 120), (500, 470)], w=2, alpha=0.45)
    return P.finish(top=30, bottom=34, left=45, right=45, feather=70, seed=43)


def scene5():
    """Floresta de louro ao entardecer, levada e caminhante com lanterna."""
    P = Paint(51)
    sky(P, -5, 360, (22, 62, 74), (86, 128, 120))
    r = np.random.default_rng(6)
    # far tree layers + fog
    for depth, (col, y0, amp) in enumerate([((60, 100, 98), 250, 40), ((40, 82, 82), 290, 50), ((26, 62, 66), 330, 55)]):
        P.layer(poly(ridge(y0, amp, 60 + depth, step=14)), col, op=0.98, wob=4, rim=0.1)
        for _ in range(9):
            x = r.uniform(0, SW)
            P.layer(ell(x, y0 + 40 + depth * 20, r.uniform(120, 240), r.uniform(18, 30)), (226, 232, 214), op=0.20, wob=0, rim=0, soft=14)
    # ground
    P.layer(rect(-5, 420, SW + 5, SH + 5), (22, 52, 56), op=1.0, wob=2, rim=0.1)
    # path (vanishing)
    P.layer(poly([(520, 330), (570, 330), (820, 645), (260, 645)]), (150, 126, 90), op=0.97, wob=3, rim=0.2)
    P.layer(poly([(520, 330), (545, 330), (540, 645), (500, 645)]), (180, 150, 104), op=0.45, wob=3, rim=0, soft=8)
    # levada channel on the right of the path
    P.layer(poly([(578, 330), (600, 330), (980, 645), (830, 645)]), (84, 82, 72), op=0.98, wob=2, rim=0.3)
    P.layer(poly([(582, 334), (596, 334), (940, 645), (860, 645)]), (60, 112, 126), op=0.97, wob=1.5, rim=0.2)
    for i in range(18):
        t = i / 17
        x = 590 + t * 300 + r.normal(0, 4)
        y = 340 + t * 290
        P.layer(ell(x, y, 8 + 22 * t, 1.6 + 1.5 * t), (252, 214, 140), op=0.65, wob=0, rim=0, soft=0.8)
    # tree trunks and foliage
    for (x, w, top, col) in [(80, 46, 70, (22, 40, 44)), (210, 34, 120, (28, 48, 50)), (420, 28, 190, (34, 56, 56)),
                             (940, 52, 60, (22, 40, 44)), (1030, 38, 100, (28, 48, 50)), (700, 22, 220, (40, 62, 60))]:
        P.layer(poly([(x - w / 2, 645), (x - w * 0.35, top), (x + w * 0.35, top), (x + w / 2, 645)]), col, op=0.98, wob=3, rim=0.25)
        leafy(P, x, top + 10, 150 if w > 30 else 110, (22, 70, 64), n=34, seed=int(x))
    # ferns foreground
    for (fx, fy) in [(120, 600), (300, 630), (960, 610)]:
        for k in range(9):
            a = -2.6 + k * 0.4
            pts = [(fx, fy), (fx + np.cos(a) * 90, fy + np.sin(a) * 60 - 20)]
            P.layer(shape(lambda d, pts=pts: d.line(pts, fill=255, width=7)), (30, 94, 74), op=0.9, wob=2, rim=0.2, soft=0.8)
    # walker with lantern (from behind, on path)
    person(P, 520, 570, 250)
    P.glow(470, 470, 60, WARM, 0.9)
    P.glow(470, 470, 160, (255, 200, 110), 0.30)
    P.layer(rrect(460, 458, 480, 486, 4), (255, 226, 140), op=0.98, wob=0.5, rim=0.1)
    return P.finish(top=30, bottom=34, left=45, right=45, feather=70, seed=52)


def scene6():
    """Duas pessoas lado a lado num muro de pedra, em silêncio, diante do mar."""
    P = Paint(61)
    sky(P, -5, 340, NAVY, (30, 82, 96))
    P.stars(100, 280, seed=62)
    moon(P, 800, 120, 30)
    sea(P, 330, SH + 5, DTEAL, NAVY, seed=63)
    moon_reflection(P, 800, 340, 520, n=24, seed=64)
    # hillside with lit houses on the left
    P.layer(poly(ridge(420, 55, 9, x1=520)), (20, 50, 60), op=0.97, wob=3)
    for i, (x, y, w, h) in enumerate([(60, 440, 52, 38), (150, 470, 58, 40), (250, 450, 48, 36), (330, 490, 54, 38), (420, 470, 50, 36), (120, 530, 56, 40)]):
        house(P, x, y, w, h, body=(116, 134, 138), seed=i)
    # stone wall foreground
    P.layer(rect(-5, 500, SW + 5, SH + 5), (86, 80, 72), op=1.0, wob=1.5, rim=0.3, vary=0.18)
    P.layer(rect(-5, 490, SW + 5, 512), (134, 124, 108), op=1.0, wob=1.5, rim=0.3)
    r = np.random.default_rng(12)
    for row in range(5):
        y = 520 + row * 26
        x = -20 + (row % 2) * 30
        while x < SW:
            w = r.uniform(70, 130)
            P.layer(rect(x, y, x + w - 4, y + 22), tuple(int(v * r.uniform(0.82, 1.1)) for v in (96, 88, 78)), op=0.9, wob=1.2, rim=0.3, soft=0.8)
            x += w
    # two figures sitting (back), small gap between them
    person(P, 640, 500, 300, coat=OCHRE, sit=True)
    person(P, 790, 500, 270, coat=(70, 112, 128), hair=(66, 46, 36), sit=True)
    P.layer(rect(-5, 498, SW + 5, 512), (134, 124, 108), op=0.0)
    return P.finish(top=30, bottom=34, left=45, right=45, feather=70, seed=65)


def scene7():
    """Varanda à noite: lâmpada, casaco ocre dobrado, vasos e o Atlântico com a lua."""
    P = Paint(71)
    sky(P, -5, 330, NAVY, (30, 82, 96))
    P.stars(110, 280, seed=72)
    moon(P, 800, 130, 34)
    sea(P, 320, SH + 5, DTEAL, NAVY, seed=73)
    moon_reflection(P, 800, 332, 520, n=26, seed=74)
    P.glow(260, 400, 260, WARM, 0.35)
    # balusters + rails
    wood = (118, 80, 48)
    for x in range(30, SW, 92):
        P.layer(rect(x, 430, x + 14, SH + 5), (86, 58, 36), op=0.98, wob=1.5, rim=0.25)
    P.layer(rect(-5, 400, SW + 5, 428), wood, op=0.98, wob=1.5, rim=0.3)
    P.layer(rect(-5, 596, SW + 5, 618), (96, 66, 40), op=0.98, wob=1.5, rim=0.3)
    # lantern on the rail
    P.layer(rect(236, 384, 284, 400), (50, 36, 28), op=0.98, wob=1)
    P.layer(rrect(240, 316, 280, 386, 14), (252, 212, 128), op=0.97, wob=1.2, rim=0.15)
    P.layer(shape(lambda d: d.arc([244, 296, 276, 336], 180, 360, fill=255, width=4)), (50, 36, 28), op=0.98, wob=0.8)
    P.glow(260, 352, 90, (255, 236, 170), 0.85)
    # cup
    P.layer(poly([(380, 360), (430, 360), (424, 398), (386, 398)]), CREAM, op=0.98, wob=1, rim=0.3)
    P.layer(rrect(428, 368, 444, 384, 6), CREAM, op=0.95, wob=1)
    # geranium pots on the left
    for x in (80, 150):
        P.layer(poly([(x - 28, 356), (x + 28, 356), (x + 20, 400), (x - 20, 400)]), (176, 98, 62), op=0.98, wob=1.2, rim=0.3)
        leafy(P, x, 332, 36, (40, 98, 70), n=10, seed=x)
        r = np.random.default_rng(x)
        for _ in range(6):
            P.layer(ell(x + r.uniform(-24, 24), 316 + r.uniform(-18, 12), 8, 8), (206, 96, 78), op=0.95, wob=1, rim=0.3)
    # chair with folded ochre coat
    c = (74, 50, 32)
    P.layer(rect(660, 420, 760, 436), c, op=0.98, wob=1.5)
    P.layer(rect(662, 436, 674, 600), c, op=0.98, wob=1.5)
    P.layer(rect(746, 436, 758, 600), c, op=0.98, wob=1.5)
    P.layer(rect(662, 230, 674, 420), c, op=0.98, wob=1.5)
    P.layer(rect(746, 230, 758, 420), c, op=0.98, wob=1.5)
    for k in range(3):
        P.layer(rect(662, 246 + k * 36, 758, 258 + k * 36), c, op=0.98, wob=1.5)
    P.layer(poly([(650, 410), (772, 410), (782, 440), (770, 470), (664, 472), (648, 440)]), OCHRE, op=0.98, wob=2, rim=0.3)
    P.layer(poly([(660, 420), (768, 420), (770, 436), (662, 440)]), (222, 164, 70), op=0.9, wob=1.5, rim=0.1)
    P.line([(650, 410), (772, 410), (782, 440), (770, 470), (664, 472), (648, 440), (650, 410)], w=2, alpha=0.4, color=(70, 44, 18))
    return P.finish(top=30, bottom=34, left=45, right=45, feather=70, seed=75)


SCENES = [scene1, scene2, scene3, scene4, scene5, scene6, scene7]

if __name__ == "__main__":
    import sys, os
    from PIL import Image
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "art")
    os.makedirs(out, exist_ok=True)
    which = [int(a) for a in sys.argv[1:]] or list(range(1, 8))
    for i in which:
        arr = SCENES[i - 1]()
        Image.fromarray(arr).save(f"{out}/scene_{i}.png")
        print("scene", i, arr.shape)
