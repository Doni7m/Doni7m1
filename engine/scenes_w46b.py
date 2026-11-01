"""Cenas 05-06/11/2026: Pieper (n05), Tillich (n06)."""
from lib4 import *


# ============================================================ 05/11 Pieper: lazer
def n05a1():
    P = Paint(6301)
    P.vgrad(-5, SH + 5, (170, 206, 200), (96, 150, 110), mask=rect(-5, -5, SW + 5, SH + 5), wob=0, rim=0, vary=0.08)
    P.layer(rect(-5, 520, SW + 5, SH + 5), (70, 116, 84), op=0.97, wob=3, rim=0.2)
    big_tree(P, 170, 560, 360, lean=0.05, seed=3, crown=0.5)
    big_tree(P, 910, 560, 360, lean=-0.05, seed=4, crown=0.5)
    pts = [(190, 330 + 120 * np.sin(np.pi * t)) for t in [0]]
    top = [(190 + 700 * t, 330 + 120 * np.sin(np.pi * t)) for t in np.linspace(0, 1, 20)]
    bot = [(190 + 700 * t, 345 + 140 * np.sin(np.pi * t)) for t in np.linspace(0, 1, 20)]
    P.layer(poly(top + bot[::-1]), (226, 190, 120), op=0.98, wob=2, rim=0.3)
    person(P, 540, 492, 160, sit=True, profile=0.3)
    return fin(P, 6302)


def n05a2():
    P = Paint(6311)
    backdrop(P, "day", 330, seed=6311, clouds=2)
    P.layer(rect(-5, 430, SW + 5, SH + 5), (222, 202, 160), op=0.98, wob=3, rim=0.15)
    chair(P, 540, 600, 300)
    person(P, 540, 590, 280, sit=True, profile=0.0)
    stack_papers(P, 380, 190, n=4, w=120)
    clock_round(P, 700, 170, r=56, hands=(0.45, 0.1))
    for (x, y, rx) in [(380, 200, 150), (560, 180, 160), (720, 200, 150)]:
        P.layer(ell(x, y + 30, rx, 20), (255, 255, 255), op=0.25, wob=2, rim=0, soft=8)
    return fin(P, 6312)


def n05a3():
    P = Paint(6321)
    room_bg(P, (22, 44, 56))
    floor(P, 560, (60, 44, 34))
    for k, (x, y, r) in enumerate([(120, 150, 44), (250, 130, 56), (400, 150, 44), (560, 130, 60), (730, 150, 46), (880, 130, 54), (1010, 150, 40)]):
        clock_round(P, x, y, r=r, hands=(0.1 * k + 0.08, 0.5 + 0.07 * k))
    table(P, 60, 1020, 400)
    stack_papers(P, 240, 380, n=6, w=130)
    stack_papers(P, 520, 380, n=4, w=130)
    stack_papers(P, 800, 380, n=5, w=130)
    person(P, 540, 620, 200, coat=OCHRE, profile=0.0)
    return fin(P, 6322)


def n05a4():
    P = Paint(6331)
    backdrop(P, "dawn", 280, sunp=(540, 260, 34), seed=6331, clouds=3)
    cliff(P, "left", top=400, seed=11, col=(18, 44, 52), reach=620)
    cliff(P, "right", top=480, seed=12, col=(16, 40, 50), reach=300)
    person(P, 330, 440, 230, coat=OCHRE, profile=0.5)
    gulls(P, [(700, 150, 1.1), (800, 190, 0.8), (880, 130, 0.9)])
    return fin(P, 6332)


def n05a5():
    P = Paint(6341)
    room_bg(P, (26, 48, 58))
    floor(P, 530, (66, 48, 36))
    window_frame(P, 700, 70, 980, 330, sky_top=(110, 140, 160), sky_bot=(180, 200, 206))
    rain(P, 700, 980, 70, 330, n=60, seed=3)
    table(P, 120, 650, 420)
    P.layer(ell(300, 400, 70, 40), (60, 60, 66), op=0.98, wob=1.5, rim=0.3)
    P.layer(ell(300, 366, 78, 10), (90, 90, 96), op=0.98, wob=1)
    for k in range(3):
        P.layer(ell(290 + k * 20, 330 - k * 10, 6, 6), (240, 232, 215), op=0.3, wob=1, rim=0, soft=3)
    for k, c in enumerate([(206, 96, 78), (74, 140, 92), (232, 180, 80), (206, 96, 78)]):
        P.layer(ell(460 + k * 38, 412, 16, 12), c, op=0.98, wob=1, rim=0.3)
    cup(P, 580, 412, steam=True)
    person(P, 430, 590, 300, profile=0.3)
    return fin(P, 6342)


def n05a6():
    P = Paint(6351)
    P.vgrad(-5, SH + 5, (160, 200, 196), (70, 120, 90), mask=rect(-5, -5, SW + 5, SH + 5), wob=0, rim=0, vary=0.1)
    laurel_trunks(P, [(100, 60, 60, (64, 50, 40)), (980, 50, 90, (58, 46, 38))])
    P.layer(poly([(-5, 640), (-5, 430), (1085, 400), (1085, 640)]), (84, 140, 150), op=0.95, wob=3, rim=0.2, soft=1.4)
    P.layer(poly([(-5, 640), (-5, 560), (1085, 540), (1085, 640)]), (110, 120, 80), op=0.97, wob=3, rim=0.2)
    P.layer(poly([(480, 470), (560, 470), (590, 488), (450, 488)]), (248, 244, 232), op=0.98, wob=1, rim=0.3)
    P.layer(poly([(520, 410), (520, 468), (570, 468)]), (248, 244, 232), op=0.98, wob=1, rim=0.3)
    fern(P, 840, 600, n=9, size=110)
    person(P, 260, 590, 230, sit=True, coat=OCHRE, profile=0.5)
    return fin(P, 6352)


def n05a7():
    P = Paint(6361)
    room_bg(P, (22, 44, 56))
    floor(P, 540, (62, 44, 34))
    window_frame(P, 700, 70, 960, 320, sky_top=(120, 170, 190), sky_bot=(246, 226, 180))
    table(P, 150, 640, 420)
    P.layer(ell(360, 410, 74, 14), (236, 226, 202), op=0.98, wob=1.2, rim=0.3)
    P.layer(poly([(320, 408), (400, 408), (390, 374), (330, 374)]), (176, 120, 66), op=0.98, wob=1.5, rim=0.3)
    cup(P, 500, 412, steam=True)
    pot_plant(P, 580, 330, 0.9, kind="sprout")
    chair(P, 330, 590, 310)
    person(P, 330, 580, 295, sit=True, profile=0.3)
    P.glow(830, 240, 260, WARM, 0.3)
    return fin(P, 6362)


# ============================================================ 06/11 Tillich: coragem de ser
def n06a1():
    P = Paint(6401)
    backdrop(P, "dawn", 250, sunp=(840, 230, 28), seed=6401, clouds=2)
    pier(P, -5, 760, 460)
    person(P, 700, 462, 230, coat=OCHRE, profile=0.4)
    lantern(P, 120, 420, 1.0)
    foam(P, 0, 1080, 520, n=26, seed=3)
    return fin(P, 6402)


def n06a2():
    P = Paint(6411)
    room_bg(P, (16, 34, 46))
    floor(P, 570, (50, 38, 30))
    door(P, 400, 120, 700, 560, lit=False)
    P.layer(rect(400, 552, 700, 566), (255, 214, 130), op=0.95, wob=0.8, rim=0.1)
    P.glow(550, 560, 220, WARM, 0.55)
    person(P, 550, 620, 300, coat=OCHRE, profile=0.0)
    return fin(P, 6412)


def n06a3():
    P = Paint(6421)
    backdrop(P, "storm", 280, seed=6421, clouds=4)
    boat(P, 760, 400, 0.6, lit=True)
    foam(P, 400, 1000, 400, n=28, seed=5)
    P.layer(rect(-5, 520, SW + 5, SH + 5), (84, 76, 66), op=0.98, wob=3, rim=0.2)
    bench(P, 300, 600, w=240)
    person(P, 300, 596, 250, sit=True, profile=0.4)
    rain(P, 0, 1080, 0, 520, n=60, seed=4)
    return fin(P, 6422)


def n06a4():
    P = Paint(6431)
    backdrop(P, "storm", 300, seed=6431, clouds=3)
    P.glow(560, 140, 380, GOLD, 0.45)
    P.layer(poly([(380, 20), (700, 20), (820, 300), (260, 300)]), (255, 232, 170), op=0.12, wob=4, rim=0, soft=10)
    cliff(P, "left", top=420, seed=21, col=(18, 40, 48), reach=700)
    person(P, 500, 440, 260, coat=OCHRE, profile=0.0)
    return fin(P, 6432)


def n06a5():
    P = Paint(6441)
    room_bg(P, (24, 46, 58))
    floor(P, 560, (62, 46, 34))
    framed(P, 110, 120, 300, 300, (120, 170, 190), (236, 214, 160))
    framed(P, 360, 120, 550, 300, (176, 98, 62), (240, 196, 130))
    framed(P, 610, 120, 800, 300, (74, 140, 92), (206, 226, 190))
    P.layer(rect(860, 120, 1000, 300), (80, 66, 50), op=0.5, wob=1.5, rim=0.2)
    ladder(P, 910, 600, 300, w=80, lean=0)
    person(P, 620, 610, 300, coat=OCHRE, profile=0.5)
    return fin(P, 6442)


def n06a6():
    P = Paint(6451)
    backdrop(P, "dusk", 220, sunp=(880, 200, 26), seed=6451, clouds=2)
    stone_wall(P, 270, SH + 5, seed=31, base=(100, 92, 80))
    stone_stairs(P, 280, 760, 330, 640, steps=7)
    person(P, 400, 600, 200, coat=OCHRE, profile=0.5)
    person(P, 470, 380, 150, coat=BLUE_COAT, profile=-0.5)
    lantern(P, 900, 420, 1.1)
    return fin(P, 6452)


def n06a7():
    P = Paint(6461)
    backdrop(P, "dawn", 300, sunp=(540, 280, 34), seed=6461, clouds=3)
    P.layer(poly([(-5, 640), (-5, 470), (1085, 470), (1085, 640)]), (84, 120, 88), op=0.97, wob=3, rim=0.2)
    P.layer(poly([(380, 640), (500, 470), (640, 470), (840, 640)]), (190, 170, 124), op=0.97, wob=3, rim=0.2)
    P.layer(poly([(520, 600), (560, 600), (700, 640), (440, 640)]), (60, 60, 60), op=0.25, wob=3, rim=0, soft=4)
    person(P, 540, 560, 200, coat=OCHRE, profile=0.0)
    return fin(P, 6462)


SCENES = {n: f for n, f in globals().items() if n.startswith("n0") and callable(f)}
