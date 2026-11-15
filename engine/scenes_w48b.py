"""Cenas 19-22/11/2026: Thich Nhat Hanh (r19), Sor Juana (r20), Flusser (r21), Jaspers (r22)."""
import re
from lib4 import *

NIGHT_ROOM = (22, 44, 56)
KITCHEN_WALL = (58, 84, 88)


def kitchen(P, win=(380, 60, 700, 300), sky=((92, 148, 172), (232, 226, 200))):
    room_bg(P, KITCHEN_WALL)
    floor(P, 570, (96, 66, 44))
    window_frame(P, *win, sky_top=sky[0], sky_bot=sky[1], stars=0)


def pot(P, x, y, s=1.0, steam=True):
    P.layer(rect(x - 60 * s, y - 60 * s, x + 60 * s, y), (70, 74, 80), op=0.98, wob=1.2, rim=0.3)
    P.layer(rect(x - 70 * s, y - 62 * s, x + 70 * s, y - 52 * s), (96, 100, 106), op=0.98, wob=1)
    P.layer(rect(x - 90 * s, y - 40 * s, x - 60 * s, y - 32 * s), (50, 52, 56), op=0.98, wob=1)
    if steam:
        for k in range(4):
            xs = np.linspace(0, 1, 30)
            pts = [(x - 36 * s + 24 * k * s + 9 * np.sin(t * 8 + k), y - 70 * s - t * 120 * s) for t in xs]
            P.layer(shape(lambda d, pts=pts: d.line(pts, fill=255, width=5)), (240, 232, 215), op=0.35, wob=1, rim=0, soft=2.4)


# ============================================================ 19/11 Thich Nhat Hanh: caminhar sem pressa
def r19a1():
    P = Paint(8401)
    backdrop(P, "day", 250, seed=8401, clouds=2)
    terrace(P, 290, 360, (84, 130, 86), seed=2)
    terrace(P, 400, 250, (70, 116, 80), seed=3)
    P.layer(rect(-5, 520, SW + 5, SH + 5), (176, 150, 112), op=0.98, wob=3, rim=0.2, vary=0.18)
    banana_leaf(P, 120, 560, -0.6, 230, 60)
    hydrangea(P, 900, 520, 60, seed=5)
    person(P, 520, 600, 230, coat=OCHRE, profile=0.3)
    return fin(P, 8402)


def r19a2():
    P = Paint(8411)
    backdrop(P, "day", 200, seed=8411, clouds=1)
    stone_wall(P, 230, 420, seed=4)
    clock_round(P, 200, 130, r=66, hands=(0.1, 0.8))
    cobbles(P, 410, base=(110, 104, 94))
    person(P, 640, 620, 270, coat=OCHRE, profile=0.7)
    phone(P, 520, 470, w=80, lit=True, tilt=0.2)
    return fin(P, 8412)


def r19a3():
    P = Paint(8421)
    backdrop(P, "dusk", 220, sunp=(240, 210, 30), seed=8421)
    stone_wall(P, 250, 640, seed=3, base=(92, 84, 74))
    stone_stairs(P, 380, 840, 250, 630, steps=8)
    person(P, 640, 470, 200, coat=OCHRE, profile=0.8)
    clock_round(P, 860, 120, r=60, hands=(0.2, 0.95))
    return fin(P, 8422)


def r19a4():
    P = Paint(8431)
    backdrop(P, "dawn", 220, sunp=(880, 210, 34), seed=8431, clouds=2)
    laurel_trunks(P, [(120, 50, 70, (64, 50, 40)), (980, 44, 90, (58, 46, 38))])
    P.layer(rect(-5, 470, SW + 5, SH + 5), (176, 150, 112), op=0.98, wob=3, rim=0.2, vary=0.18)
    fern(P, 260, 500, n=9, size=120)
    hydrangea(P, 720, 500, 76, seed=7)
    person(P, 520, 600, 260, coat=OCHRE, profile=0.5)
    return fin(P, 8432)


def r19a5():
    P = Paint(8441)
    cobbles(P, -5, ybot=SH + 5, seed=12, base=(112, 104, 92))
    # pernas e sapatos vistos de cima do joelho
    P.layer(rect(430, -5, 500, 380), NAVY, op=0.97, wob=1.5, rim=0.2)
    P.layer(rect(600, -5, 670, 250), NAVY, op=0.97, wob=1.5, rim=0.2)
    P.layer(ell(468, 400, 62, 24), (22, 18, 20), op=0.97, wob=1)
    P.layer(ell(640, 272, 62, 24), (22, 18, 20), op=0.97, wob=1)
    P.layer(ell(540, 520, 36, 8), (30, 40, 44), op=0.3, wob=0, soft=3)
    return fin(P, 8442)


def r19a6():
    P = Paint(8451)
    backdrop(P, "day", 300, seed=8451, clouds=1)
    floor(P, 470, (160, 136, 100))
    stone_wall(P, 440, 500, seed=2)
    bench(P, 520, 600, 380)
    person(P, 500, 600, 250, coat=OCHRE, sit=True, profile=0.5)
    cup(P, 700, 566, steam=True)
    pot_plant(P, 860, 560, 1.2, seed=4)
    return fin(P, 8452)


def r19a7():
    P = Paint(8461)
    backdrop(P, "dusk", 290, sunp=(700, 280, 36), seed=8461, clouds=2)
    cliff(P, "right", top=400, seed=51, col=(24, 52, 58), reach=520)
    P.layer(rect(-5, 520, 700, SH + 5), (150, 118, 84), op=0.98, wob=3, rim=0.2, vary=0.18)
    person(P, 380, 560, 220, coat=OCHRE, profile=0.5)
    gulls(P, [(760, 150, 1.0), (860, 190, 0.8)])
    return fin(P, 8462)


# ============================================================ 20/11 Sor Juana: pensar na cozinha
def r20a1():
    P = Paint(8501)
    kitchen(P)
    table(P, 150, 930, 450)
    pot(P, 540, 440, 1.3)
    pot_plant(P, 260, 450, 1.1, seed=2)
    return fin(P, 8502)


def r20a2():
    P = Paint(8511)
    kitchen(P, win=(100, 60, 360, 290))
    table(P, 200, 980, 450)
    stack_papers(P, 320, 440, n=5, w=130)
    cup(P, 520, 444, steam=True)
    clock_round(P, 760, 160, r=70, hands=(0.6, 0.1))
    lamp(P, 860, 450, h=120)
    return fin(P, 8512)


def r20a3():
    P = Paint(8521)
    kitchen(P, win=(700, 60, 980, 300), sky=((30, 50, 80), (60, 90, 110)))
    table(P, 120, 700, 470)
    stack_papers(P, 260, 460, n=6, w=130)
    chair(P, 460, 640, 300)
    person(P, 460, 630, 280, sit=True, coat=OCHRE, profile=0.2)
    clock_round(P, 360, 160, r=70, hands=(0.35, 0.05))
    return fin(P, 8522)


def r20a4():
    P = Paint(8531)
    kitchen(P)
    table(P, 130, 950, 450)
    book(P, 340, 440, w=220)
    pot(P, 700, 440, 1.0)
    candle(P, 520, 442, h=50)
    return fin(P, 8532)


def r20a5():
    P = Paint(8541)
    kitchen(P, win=(740, 60, 1000, 290))
    table(P, 120, 780, 450)
    P.layer(ell(400, 432, 150, 26), (60, 62, 66), op=0.98, wob=1.2, rim=0.3)
    P.layer(ell(400, 428, 130, 18), (186, 120, 62), op=0.95, wob=1)
    r = np.random.default_rng(3)
    for k in range(7):
        P.layer(ell(340 + k * 18 + r.uniform(-4, 4), 424 + r.uniform(-4, 4), 11, 8), (240, 226, 190), op=0.97, wob=0.8, rim=0.3)
    for k in range(3):
        xs = np.linspace(0, 1, 30)
        pts = [(350 + 50 * k + 9 * np.sin(t * 8 + k), 400 - t * 120) for t in xs]
        P.layer(shape(lambda d, pts=pts: d.line(pts, fill=255, width=5)), (240, 232, 215), op=0.35, wob=1, rim=0, soft=2.4)
    P.layer(ell(660, 436, 28, 22), (232, 196, 70), op=0.98, wob=1, rim=0.3)
    P.layer(ell(700, 440, 26, 20), (232, 196, 70), op=0.98, wob=1, rim=0.3)
    pot_plant(P, 200, 450, 1.1, seed=3)
    return fin(P, 8542)


def r20a6():
    P = Paint(8551)
    room_bg(P, KITCHEN_WALL)
    floor(P, 590, (96, 66, 44))
    backdrop(P, "day", 330, seed=8551, clouds=1)
    P.layer(rect(-5, -5, 140, SH + 5), KITCHEN_WALL, op=1.0, wob=0, rim=0)
    P.layer(rect(940, -5, SW + 5, SH + 5), KITCHEN_WALL, op=1.0, wob=0, rim=0)
    P.layer(rect(130, 520, 950, 560), WOOD_T, op=0.98, wob=1.5, rim=0.3)
    pot_plant(P, 330, 520, 1.2, seed=4)
    cup(P, 700, 514, steam=True)
    hydrangea(P, 860, 470, 50, seed=3)
    return fin(P, 8552)


def r20a7():
    P = Paint(8561)
    backdrop(P, "night", 200, moonp=(860, 90, 24), seed=8561)
    hill_houses(P, -10, SW + 10, 230, n=9, seed=91, lit=True)
    facade(P, 340, 760, 330, 640)
    lit_window(P, 450, 380, 560, 500, silhouette=True)
    lit_window(P, 600, 380, 700, 500)
    return fin(P, 8562)


# ============================================================ 21/11 Flusser: entre dois lugares
def r21a1():
    P = Paint(8601)
    backdrop(P, "dusk", 290, sunp=(760, 280, 34), seed=8601, clouds=2)
    pier(P, -5, 760, 470)
    suitcase(P, 380, 470, 1.4)
    person(P, 520, 472, 240, coat=OCHRE, profile=0.6)
    foam(P, 0, SW, 560, n=28, seed=7)
    return fin(P, 8602)


def r21a2():
    P = Paint(8611)
    night_room(P, win=(760, 70, 1000, 320)) if False else None
    room_bg(P, NIGHT_ROOM)
    floor(P, 560, (62, 44, 34))
    window_frame(P, 700, 70, 980, 320, sky_top=NAVY, sky_bot=(30, 82, 96), stars=30, seed=3)
    table(P, 120, 700, 460)
    cup(P, 300, 454, steam=True)
    cup(P, 520, 454, steam=True)
    letter(P, 410, 456, w=130)
    lamp(P, 640, 460, h=110)
    return fin(P, 8612)


def r21a3():
    P = Paint(8621)
    backdrop(P, "dusk", 330, sunp=(300, 320, 34), seed=8621, clouds=2)
    boat(P, 640, 420, 1.3, lit=True, sail=True)
    foam(P, 0, SW, 520, n=40, seed=8)
    return fin(P, 8622)


def r21a4():
    P = Paint(8631)
    backdrop(P, "dawn", 300, sunp=(540, 290, 36), seed=8631, island=(700, 260), clouds=2)
    cliff(P, "left", top=420, seed=57, col=(18, 44, 52), reach=640)
    person(P, 420, 440, 210, coat=OCHRE, profile=0.5)
    gulls(P, [(700, 140, 1.0), (800, 170, 0.8)])
    return fin(P, 8632)


def r21a5():
    P = Paint(8641)
    kitchen(P, win=(100, 60, 360, 290))
    table(P, 200, 980, 450)
    pot(P, 560, 440, 1.0)
    cup(P, 760, 444, steam=True)
    letter(P, 380, 448, w=150)
    pot_plant(P, 880, 450, 1.1, seed=5)
    return fin(P, 8642)


def r21a6():
    P = Paint(8651)
    backdrop(P, "night", 320, moonp=(780, 100, 28), seed=8651)
    cliff(P, "left", top=410, seed=63, col=(14, 36, 46), reach=720)
    person(P, 460, 440, 220, coat=OCHRE, profile=0.6)
    lantern(P, 560, 410, 1.0)
    P.glow(560, 420, 140, WARM, 0.3)
    return fin(P, 8652)


def r21a7():
    P = Paint(8661)
    backdrop(P, "night", 200, moonp=(900, 90, 24), seed=8661)
    hill_houses(P, -10, SW + 10, 220, n=11, seed=101, lit=True)
    hill_houses(P, -10, SW + 10, 350, n=11, seed=102, lit=True, body=(132, 146, 144))
    hill_houses(P, -10, SW + 10, 470, n=9, seed=103, lit=True, body=(150, 156, 148))
    string_lights(P, 80, 1000, 590, sag=22, n=12)
    return fin(P, 8662)


# ============================================================ 22/11 Jaspers: o que fica de pé
def r22a1():
    P = Paint(8701)
    backdrop(P, "storm", 300, seed=8701, clouds=3)
    cliff(P, "left", top=400, seed=71, col=(14, 36, 46), reach=700)
    person(P, 430, 430, 220, coat=OCHRE, profile=0.5)
    foam(P, 0, SW, 540, n=34, seed=9)
    rain(P, 0, SW, 0, 400, n=60, seed=3)
    gulls(P, [(780, 160, 1.0), (880, 200, 0.8)])
    return fin(P, 8702)


def r22a2():
    P = Paint(8711)
    room_bg(P, NIGHT_ROOM)
    floor(P, 570, (62, 44, 34))
    window_frame(P, 100, 70, 380, 330, sky_top=(30, 54, 72), sky_bot=(110, 130, 130), stars=0)
    rain(P, 100, 380, 70, 330, n=30, seed=4)
    table(P, 300, 980, 460)
    letter(P, 480, 456, w=160)
    phone(P, 700, 458, w=96, face_down=True)
    lamp(P, 880, 460, h=110, g=0.4)
    return fin(P, 8712)


def r22a3():
    P = Paint(8721)
    backdrop(P, "storm", 280, seed=8721, clouds=3)
    boat(P, 540, 420, 1.4, lit=True)
    foam(P, 0, SW, 470, n=44, seed=11)
    foam(P, 0, SW, 560, n=34, seed=12)
    rain(P, 0, SW, 0, 600, n=50, seed=5)
    return fin(P, 8722)


def r22a4():
    P = Paint(8731)
    backdrop(P, "dusk", 300, sunp=(560, 300, 40), seed=8731, clouds=3, island=(760, 240))
    cliff(P, "right", top=430, seed=73, col=(24, 52, 58), reach=520)
    P.glow(560, 280, 280, WARM, 0.35)
    person(P, 800, 440, 190, coat=OCHRE, profile=-0.5)
    gulls(P, [(300, 170, 1.0)])
    return fin(P, 8732)


def r22a5():
    P = Paint(8741)
    room_bg(P, NIGHT_ROOM)
    floor(P, 570, (62, 44, 34))
    window_frame(P, 700, 70, 980, 320, sky_top=(24, 48, 92), sky_bot=(226, 152, 98), stars=0)
    table(P, 120, 700, 460)
    letter(P, 280, 456, w=150)
    letter(P, 500, 456, w=150, tilt=0.04, stamp=False)
    paper_tag(P, 280, 400, w=70)
    paper_tag(P, 500, 400, w=70)
    lamp(P, 640, 460, h=110)
    cup(P, 150 + 20, 454, steam=True)
    return fin(P, 8742)


def r22a6():
    P = Paint(8751)
    backdrop(P, "dawn", 210, sunp=(860, 200, 34), seed=8751, clouds=2)
    stone_wall(P, 210, 640, seed=3, base=(98, 90, 80))
    stone_stairs(P, 300, 800, 150, 625, steps=9)
    person(P, 520, 420, 190, coat=OCHRE, profile=0.3)
    lantern(P, 780, 330, 1.0)
    return fin(P, 8752)


def r22a7():
    P = Paint(8761)
    backdrop(P, "dawn", 310, sunp=(540, 300, 44), seed=8761, clouds=3)
    P.layer(rect(-5, 500, SW + 5, SH + 5), (60, 74, 76), op=0.98, wob=3, rim=0.2)
    boulder(P, 760, 520, 120, 60)
    boulder(P, 240, 540, 100, 50)
    person(P, 520, 560, 240, coat=OCHRE, profile=0.4)
    lantern(P, 620, 540, 0.9)
    gulls(P, [(220, 140, 1.0), (330, 170, 0.8)])
    return fin(P, 8762)


SCENES = {n: f for n, f in globals().items() if re.match(r"^r\d\d", n) and callable(f)}
