"""Cenas 02-04/11/2026: Montaigne (n02), Sartre (n03), Plutarco (n04)."""
from lib4 import *


def fin4(P, s):
    return fin(P, s)


# ============================================================ 02/11 Montaigne: um canto só seu
def n02a1():
    P = Paint(6001)
    room_bg(P, (20, 44, 58))
    floor(P, 540, (62, 44, 34))
    P.layer(rect(700, -5, 722, SH + 5), (70, 48, 32), op=0.98, wob=1.5, rim=0.3)
    lit_window(P, 120, 90, 300, 300)
    lit_window(P, 380, 90, 560, 300)
    table(P, 90, 640, 440)
    for k in range(5):
        cup(P, 150 + k * 110, 432, steam=(k % 2 == 0))
    person(P, 200, 560, 190, coat=BLUE_COAT, profile=0.4)
    person(P, 380, 560, 195, coat=RUST_COAT, profile=-0.3)
    person(P, 560, 560, 185, coat=SAGE_COAT, profile=0.2)
    window_frame(P, 800, 90, 980, 280, stars=20, seed=6)
    moon(P, 900, 170, 20)
    lamp(P, 800, 520, h=120)
    chair(P, 880, 585, 300)
    person(P, 880, 575, 290, sit=True, profile=0.4)
    return fin4(P, 6002)


def n02a2():
    P = Paint(6011)
    room_bg(P, (22, 40, 54))
    floor(P, 548, (60, 44, 34))
    table(P, 60, 1020, 400)
    for k, (x, t) in enumerate([(150, -3), (300, 4), (470, -2), (640, 5), (800, -4), (950, 2)]):
        phone(P, x, 392, w=78, lit=True, tilt=t)
    stack_papers(P, 230, 380, n=5, w=120)
    stack_papers(P, 720, 380, n=6, w=120)
    clock_round(P, 540, 170, r=70, hands=(0.1, 0.55))
    P.glow(540, 300, 480, (120, 170, 230), 0.16)
    person(P, 540, 600, 270, coat=OCHRE, profile=0.0)
    return fin4(P, 6012)


def n02a3():
    P = Paint(6021)
    backdrop(P, "dusk", 300, sunp=(700, 280, 28), seed=6021, clouds=2, island=(120, 260))
    P.layer(poly([(-5, 640), (-5, 470), (400, 440), (1085, 500), (1085, 640)]), (60, 98, 76), op=0.97, wob=3, rim=0.2)
    cliff(P, "right", top=380, seed=7, col=(14, 34, 44), reach=300)
    bench(P, 420, 560, w=250)
    person(P, 420, 556, 250, coat=OCHRE, sit=True, profile=0.5)
    gulls(P, [(220, 120, 1.0), (300, 150, 0.7), (860, 100, 0.9)])
    return fin4(P, 6022)


def n02a4():
    P = Paint(6031)
    room_bg(P, (22, 40, 52))
    floor(P, 560, (60, 42, 30))
    bookshelf(P, -5, 40, 240, 540, rows=6, seed=2)
    bookshelf(P, 840, 40, 1085, 540, rows=6, seed=3)
    window_frame(P, 330, 90, 750, 350, stars=40, seed=9)
    moon(P, 560, 190, 26)
    table(P, 300, 780, 440)
    book(P, 460, 432, w=150)
    candle(P, 640, 432, h=40)
    chair(P, 540, 600, 320)
    person(P, 540, 590, 300, sit=True, profile=0.0)
    return fin4(P, 6032)


def n02a5():
    P = Paint(6041)
    P.vgrad(-5, SH + 5, (150, 196, 190), (60, 110, 86), mask=rect(-5, -5, SW + 5, SH + 5), wob=0, rim=0, vary=0.1)
    laurel_trunks(P, [(150, 56, 80, (64, 50, 40)), (860, 64, 60, (58, 46, 38)), (1010, 40, 120, (70, 54, 42))])
    P.layer(poly([(-5, 640), (300, 470), (780, 430), (1085, 470), (1085, 640)]), (150, 134, 100), op=0.97, wob=3, rim=0.2)
    P.layer(poly([(-5, 640), (-5, 600), (900, 470), (1085, 470), (1085, 500)]), (96, 160, 176), op=0.8, wob=3, rim=0.1, soft=2)
    fern(P, 200, 520, n=9, size=120)
    fern(P, 930, 540, n=9, size=110)
    person(P, 520, 540, 210, coat=OCHRE, profile=0.5)
    return fin4(P, 6042)


def n02a6():
    P = Paint(6051)
    backdrop(P, "night", 240, moonp=(220, 110, 24), seed=6051)
    stone_wall(P, 280, SH + 5, seed=14, base=(80, 76, 70))
    cobbles(P, 520, seed=6, glow_x=760)
    door(P, 680, 330, 840, 560, lit=True, ajar=0.22)
    lantern(P, 900, 380, 1.0)
    pot_plant(P, 620, 560, 1.2, seed=3)
    person(P, 470, 590, 250, coat=OCHRE, profile=0.5)
    lit_window(P, 120, 340, 220, 460, silhouette=True)
    lit_window(P, 250, 340, 340, 460, silhouette=True)
    return fin4(P, 6052)


def n02a7():
    P = Paint(6061)
    backdrop(P, "night", 260, moonp=(780, 100, 28), seed=6061)
    hill_houses(P, 0, 1080, 300, n=9, seed=6)
    P.layer(rect(-5, 520, SW + 5, SH + 5), (34, 52, 50), op=0.98, wob=3, rim=0.2)
    boat(P, 300, 440, 0.7, lit=True)
    lit_window(P, 640, 360, 760, 480, silhouette=True)
    stone_wall(P, 540, SH + 5, seed=17, base=(70, 70, 64))
    return fin4(P, 6062)


# ============================================================ 03/11 Sartre: ainda em construção
def n03a1():
    P = Paint(6101)
    room_bg(P, (20, 44, 56))
    floor(P, 560, (60, 44, 34))
    for (x, y, t) in [(160, 160, -0.1), (260, 240, 0.08), (860, 180, 0.1), (950, 290, -0.07), (120, 360, 0.05), (900, 400, -0.1)]:
        paper_tag(P, x, y, 100, t)
    person(P, 540, 600, 400, coat=OCHRE, profile=0.0)
    for (x, y, t) in [(520, 340, -0.1), (570, 400, 0.12), (540, 460, -0.06)]:
        paper_tag(P, x, y, 46, t)
    return fin4(P, 6102)


def n03a2():
    P = Paint(6111)
    room_bg(P, (26, 46, 56))
    floor(P, 570, (62, 46, 34))
    rr = np.random.default_rng(5)
    for row in range(3):
        for col in range(9):
            letter(P, 100 + col * 110 + rr.uniform(-6, 6), 90 + row * 120 + rr.uniform(-6, 6), w=84, tilt=rr.uniform(-0.05, 0.05), stamp=(col + row) % 3 == 0)
    person(P, 540, 610, 230, coat=OCHRE, profile=0.0)
    return fin4(P, 6112)


def n03a3():
    P = Paint(6121)
    backdrop(P, "dawn", 260, sunp=(540, 250, 30), seed=6121, clouds=2)
    P.layer(rect(-5, 330, SW + 5, SH + 5), (216, 194, 150), op=0.98, wob=3, rim=0.15)
    foam(P, 0, 1080, 332, n=30, seed=4)
    for k in range(14):
        t = k / 13
        x = 140 + 300 * t
        y = 610 - 240 * t
        P.layer(ell(x, y, 12 - 4 * t, 5 - 2 * t), (150, 124, 86), op=0.7, wob=1)
    person(P, 470, 380, 120, coat=OCHRE, profile=0.2)
    return fin4(P, 6122)


def n03a4():
    P = Paint(6131)
    backdrop(P, "dawn", 260, sunp=(860, 230, 30), seed=6131, clouds=2)
    P.layer(rect(-5, 400, SW + 5, SH + 5), (176, 156, 112), op=0.97, wob=3, rim=0.2)
    keel = poly([(160, 520), (760, 520), (840, 450), (120, 450)])
    P.layer(keel, (150, 104, 62), op=0.98, wob=2, rim=0.3)
    for k in range(8):
        x = 190 + k * 80
        P.layer(poly([(x, 520), (x + 14, 520), (x + 40, 320), (x + 26, 320)]), (130, 88, 52), op=0.98, wob=1.5, rim=0.25)
    P.layer(rect(130, 300, 850, 316), (130, 88, 52), op=0.98, wob=1.5)
    person(P, 940, 600, 250, coat=OCHRE, profile=-0.5)
    P.layer(rect(880, 470, 990, 482), (190, 140, 84), op=0.98, wob=1.2, rim=0.3)
    return fin4(P, 6132)


def n03a5():
    P = Paint(6141)
    room_bg(P, (24, 50, 62))
    floor(P, 540, (66, 48, 36))
    window_frame(P, 700, 80, 960, 330, sky_top=(120, 170, 190), sky_bot=(246, 226, 180))
    guitar(P, 220, 480, 1.2)
    table(P, 380, 700, 430)
    phone(P, 520, 424, w=90, lit=True)
    chair(P, 560, 590, 310)
    person(P, 560, 580, 295, sit=True, profile=-0.3)
    P.glow(830, 240, 260, WARM, 0.3)
    return fin4(P, 6142)


def n03a6():
    P = Paint(6151)
    backdrop(P, "day", 200, seed=6151, clouds=3)
    P.layer(rect(-5, 200, SW + 5, SH + 5), (200, 190, 160), op=0.5, wob=3, rim=0.1)
    hill_houses(P, 0, 1080, 220, n=6, seed=12, body=(190, 172, 132))
    stone_stairs(P, 300, 800, 300, 640, steps=9)
    person(P, 470, 560, 230, coat=OCHRE, profile=0.3)
    suitcase(P, 380, 585, 0.8)
    return fin4(P, 6152)


def n03a7():
    P = Paint(6161)
    backdrop(P, "dawn", 230, sunp=(540, 220, 28), seed=6161, clouds=2)
    stone_wall(P, 250, SH + 5, seed=19, base=(110, 100, 86))
    door(P, 420, 300, 660, 580, lit=True, ajar=0.3)
    pot_plant(P, 330, 580, 1.2, seed=5)
    pot_plant(P, 740, 580, 1.2, seed=6)
    person(P, 540, 620, 260, coat=OCHRE, profile=0.0)
    return fin4(P, 6162)


# ============================================================ 04/11 Plutarco: comparação
def n04a1():
    P = Paint(6201)
    room_bg(P, (18, 36, 48))
    floor(P, 570, (54, 40, 30))
    window_frame(P, 160, 70, 920, 400, stars=30, seed=3)
    P.layer(poly(ridge(300, 40, 4, x0=170, x1=910)), (14, 40, 52), op=0.98, wob=2)
    hill_houses(P, 170, 910, 230, n=12, seed=9)
    person(P, 540, 620, 300, coat=OCHRE, profile=0.0)
    return fin4(P, 6202)


def n04a2():
    P = Paint(6211)
    room_bg(P, (20, 36, 50))
    floor(P, 560, (56, 40, 30))
    bed(P, 120, 900, 470)
    person(P, 440, 520, 250, sit=True, profile=0.4)
    phone(P, 560, 400, w=110, lit=True)
    cols = [((120, 170, 190), (236, 214, 160)), ((176, 98, 62), (240, 190, 120)), ((74, 140, 92), (200, 226, 190)), ((90, 100, 160), (230, 200, 200))]
    for k, (x, y) in enumerate([(700, 120), (840, 230), (760, 330), (250, 140)]):
        framed(P, x, y, x + 110, y + 90, *cols[k])
    return fin4(P, 6212)


def n04a3():
    P = Paint(6221)
    backdrop(P, "dusk", 240, sunp=(160, 220, 26), seed=6221, clouds=2)
    P.layer(poly([(-5, 640), (-5, 300), (400, 280), (1085, 260), (1085, 640)]), (30, 60, 66), op=0.98, wob=3, rim=0.2)
    facade(P, 600, 960, 250, 400, col=(210, 190, 150))
    lit_window(P, 640, 290, 700, 350)
    lit_window(P, 740, 290, 800, 350)
    lit_window(P, 840, 290, 900, 350)
    stone_stairs(P, 340, 760, 400, 640, steps=8)
    person(P, 520, 640, 150, coat=OCHRE, profile=0.0)
    return fin4(P, 6222)


def n04a4():
    P = Paint(6231)
    backdrop(P, "day", 190, seed=6231, clouds=2)
    for k, (y, col) in enumerate([(240, (88, 140, 84)), (330, (76, 128, 78)), (420, (64, 116, 72)), (510, (52, 104, 66))]):
        terrace(P, y, 130, col, seed=k + 3)
    for x in (140, 330, 520, 760, 930):
        banana_leaf(P, x, 520, -0.5, 100, 20)
        banana_leaf(P, x, 520, 0.5, 100, 20)
    person(P, 300, 330, 90, coat=BLUE_COAT, profile=0.3)
    person(P, 640, 420, 110, coat=RUST_COAT, profile=-0.3)
    person(P, 820, 255, 100, coat=OCHRE, profile=-0.4)
    return fin4(P, 6232)


def n04a5():
    P = Paint(6241)
    room_bg(P, (24, 50, 62))
    floor(P, 520, (66, 48, 36))
    window_frame(P, 200, 70, 520, 330, sky_top=(120, 170, 190), sky_bot=(246, 226, 180))
    P.layer(rect(120, 400, 900, 440), (150, 104, 62), op=0.98, wob=2, rim=0.3)
    P.layer(rect(120, 440, 900, 464), (96, 64, 38), op=0.98, wob=2, rim=0.25)
    P.layer(rect(160, 340, 210, 362), GOLD, op=0.98, wob=1, rim=0.3)
    P.layer(ell(185, 346, 22, 22), GOLD, op=0.98, wob=1, rim=0.3)
    letter(P, 420, 410, w=130)
    pot_plant(P, 700, 400, 1.3, kind="sprout")
    cup(P, 820, 400, steam=True)
    P.glow(360, 250, 280, WARM, 0.3)
    return fin4(P, 6242)


def n04a6():
    P = Paint(6251)
    backdrop(P, "dusk", 300, sunp=(840, 280, 26), seed=6251, clouds=3)
    stone_wall(P, 380, SH + 5, seed=21, base=(96, 90, 80))
    ladder(P, 400, 620, 600, w=110, lean=12)
    person(P, 640, 620, 240, coat=OCHRE, profile=-0.5)
    gulls(P, [(780, 90, 1.0), (880, 130, 0.8)])
    return fin4(P, 6252)


def n04a7():
    P = Paint(6261)
    backdrop(P, "dusk", 270, sunp=(700, 250, 28), seed=6261, clouds=2)
    P.layer(rect(-5, 400, SW + 5, SH + 5), (60, 90, 72), op=0.98, wob=3, rim=0.15)
    stone_wall(P, 480, SH + 5, seed=23, base=(94, 88, 78))
    bench(P, 420, 560, w=250)
    person(P, 420, 556, 250, coat=OCHRE, sit=True, profile=0.4)
    lantern(P, 620, 500, 1.2)
    lit_window(P, 860, 330, 940, 420)
    facade(P, 800, 1000, 330, 480)
    return fin4(P, 6262)


SCENES = {n: f for n, f in globals().items() if n.startswith("n0") and callable(f)}
