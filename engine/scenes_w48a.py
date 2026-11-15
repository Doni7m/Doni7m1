"""Cenas 16-18/11/2026: Lucrécio (r16), Simmel (r17), MacIntyre (r18)."""
import re
from lib4 import *

NIGHT_ROOM = (22, 44, 56)
CROWD = [BLUE_COAT, RUST_COAT, SAGE_COAT, (120, 110, 130), (150, 150, 160)]


def night_room(P, sky_top=NAVY, sky_bot=(30, 82, 96), win=(720, 70, 980, 330), stars=30):
    room_bg(P, NIGHT_ROOM)
    floor(P, 560, (62, 44, 34))
    window_frame(P, *win, sky_top=sky_top, sky_bot=sky_bot, stars=stars, seed=5)


# ============================================================ 16/11 Lucrécio: medo do escuro
def r16a1():
    P = Paint(8101)
    backdrop(P, "night", 300, seed=8101)
    cliff(P, "left", top=400, seed=31, col=(14, 36, 46), reach=700)
    person(P, 430, 430, 200, coat=OCHRE, profile=0.4)
    lantern(P, 520, 390, 1.1)
    P.glow(520, 400, 150, WARM, 0.35)
    return fin(P, 8102)


def r16a2():
    P = Paint(8111)
    night_room(P)
    table(P, 120, 440, 470)
    phone(P, 280, 462, w=76, lit=True)
    P.glow(280, 440, 120, (150, 190, 230), 0.35)
    chair(P, 620, 600, 300)
    person(P, 620, 590, 280, sit=True, profile=0.4)
    return fin(P, 8112)


def r16a3():
    P = Paint(8121)
    room_bg(P, (16, 36, 46))
    floor(P, 560, (50, 36, 28))
    door(P, 440, 100, 660, 560, lit=False, ajar=0.45)
    P.glow(560, 556, 230, WARM, 0.28)
    person(P, 270, 580, 270, coat=OCHRE, profile=0.5)
    return fin(P, 8122)


def r16a4():
    P = Paint(8131)
    backdrop(P, "dawn", 320, sunp=(600, 320, 38), seed=8131, clouds=2)
    cliff(P, "right", top=420, seed=34, col=(24, 52, 58), reach=560)
    foam(P, 80, 700, 560, n=28, seed=4)
    gulls(P, [(300, 160, 1.0), (380, 130, 0.8)])
    return fin(P, 8132)


def r16a5():
    P = Paint(8141)
    night_room(P, win=(120, 70, 380, 300), stars=20)
    table(P, 200, 960, 440)
    candle(P, 560, 436, h=70)
    P.glow(560, 380, 200, WARM, 0.55)
    letter(P, 400, 438, w=170)
    cup(P, 720, 432, steam=True)
    return fin(P, 8142)


def r16a6():
    P = Paint(8151)
    backdrop(P, "night", 300, moonp=(220, 110, 28), seed=8151)
    floor(P, 470, (62, 56, 50))
    bench(P, 560, 560, 340)
    person(P, 500, 560, 250, coat=OCHRE, sit=True, profile=0.4)
    person(P, 620, 560, 240, coat=BLUE_COAT, sit=True, profile=-0.4)
    lantern(P, 820, 500, 1.1)
    return fin(P, 8152)


def r16a7():
    P = Paint(8161)
    backdrop(P, "dawn", 310, sunp=(760, 300, 40), seed=8161, clouds=3)
    cliff(P, "left", top=410, seed=47, col=(18, 44, 52), reach=720)
    person(P, 470, 430, 230, coat=OCHRE, profile=0.5)
    lantern(P, 560, 400, 0.9)
    gulls(P, [(820, 150, 1.1), (920, 190, 0.8)])
    return fin(P, 8162)


# ============================================================ 17/11 Simmel: solidão na multidão
def r17a1():
    P = Paint(8201)
    backdrop(P, "night", 190, moonp=(900, 90, 24), seed=8201)
    hill_houses(P, -10, SW + 10, 210, n=11, seed=61, lit=True)
    cobbles(P, 440, glow_x=540)
    lantern(P, 330, 430, 1.2)
    person(P, 560, 610, 250, coat=OCHRE, profile=0.3)
    return fin(P, 8202)


def r17a2():
    P = Paint(8211)
    night_room(P, win=(100, 60, 420, 300), stars=24)
    table(P, 220, 980, 450)
    cup(P, 420, 444, steam=True)
    cup(P, 740, 444, steam=True)
    lamp(P, 880, 450, h=120)
    chair(P, 330, 620, 290)
    chair(P, 800, 620, 290)
    return fin(P, 8212)


def r17a3():
    P = Paint(8221)
    backdrop(P, "dusk", 230, sunp=(300, 220, 30), seed=8221)
    stone_wall(P, 250, 420, seed=5)
    cobbles(P, 410, glow_x=560)
    r = np.random.default_rng(8)
    for i, x in enumerate([90, 200, 300, 420, 700, 800, 910, 1010]):
        h = r.uniform(190, 250)
        person(P, x, 560 + r.uniform(-20, 70), h, coat=CROWD[i % len(CROWD)], profile=r.uniform(-0.5, 0.5))
    person(P, 560, 620, 280, coat=OCHRE, profile=0.2)
    return fin(P, 8222)


def r17a4():
    P = Paint(8231)
    backdrop(P, "dusk", 200, sunp=(860, 190, 28), seed=8231)
    hill_houses(P, -10, SW + 10, 230, n=12, seed=71, lit=True)
    hill_houses(P, -10, SW + 10, 350, n=12, seed=72, lit=True, body=(132, 146, 144))
    hill_houses(P, -10, SW + 10, 470, n=10, seed=73, lit=True, body=(150, 156, 148))
    string_lights(P, 80, 1000, 585, sag=24, n=13)
    return fin(P, 8232)


def r17a5():
    P = Paint(8241)
    night_room(P, sky_top=(120, 170, 190), sky_bot=(246, 226, 180), win=(110, 70, 400, 320), stars=0)
    table(P, 140, 960, 440)
    phone(P, 520, 432, w=120, lit=True)
    P.glow(520, 400, 130, (150, 190, 230), 0.35)
    cup(P, 720, 434, steam=True)
    pot_plant(P, 250, 440, 1.1, seed=3)
    return fin(P, 8242)


def r17a6():
    P = Paint(8251)
    backdrop(P, "dusk", 280, sunp=(700, 270, 34), seed=8251, clouds=1)
    floor(P, 450, (92, 84, 74))
    stone_wall(P, 400, 470, seed=9, cap=True)
    bench(P, 520, 580, 360)
    person(P, 450, 580, 250, coat=OCHRE, sit=True, profile=0.5)
    person(P, 580, 580, 245, coat=RUST_COAT, sit=True, profile=-0.5)
    string_lights(P, 60, 1020, 120, sag=40, n=13)
    return fin(P, 8252)


def r17a7():
    P = Paint(8261)
    room_bg(P, (14, 36, 46))
    stone_wall(P, 130, 560, seed=6, base=(60, 62, 62))
    cobbles(P, 540, glow_x=540)
    door(P, 430, 180, 650, 552, lit=True, ajar=0.3)
    person(P, 300, 600, 270, coat=OCHRE, profile=0.6)
    pot_plant(P, 760, 552, 1.2, seed=3)
    lantern(P, 800, 360, 1.0)
    return fin(P, 8262)


# ============================================================ 18/11 MacIntyre: pedir ajuda
def r18a1():
    P = Paint(8301)
    backdrop(P, "day", 190, seed=8301, clouds=2)
    stone_wall(P, 190, 640, seed=3, base=(98, 90, 80))
    stone_stairs(P, 300, 780, 140, 625, steps=9)
    door(P, 470, 60, 610, 140, lit=True)
    person(P, 540, 636, 210, coat=OCHRE, profile=0.2)
    return fin(P, 8302)


def r18a2():
    P = Paint(8311)
    backdrop(P, "dusk", 240, sunp=(840, 230, 30), seed=8311)
    hill_houses(P, -10, SW + 10, 250, n=9, seed=81, lit=True)
    cobbles(P, 440, glow_x=500)
    suitcase(P, 700, 590, 1.5, col=(120, 70, 44))
    suitcase(P, 840, 600, 1.2, col=(90, 80, 60))
    person(P, 480, 600, 260, coat=OCHRE, profile=0.6)
    return fin(P, 8312)


def r18a3():
    P = Paint(8321)
    night_room(P, win=(740, 70, 1000, 320), stars=18)
    table(P, 120, 800, 450)
    for x in (300, 520):
        P.layer(ell(x, 442, 74, 20), (240, 226, 190), op=0.98, wob=1, rim=0.3)
        P.layer(ell(x, 438, 62, 12), (200, 120, 70), op=0.95, wob=1)
    P.layer(rect(380, 410, 450, 436), (214, 170, 100), op=0.98, wob=1.2, rim=0.3)
    candle(P, 420, 424, h=40)
    chair(P, 220, 620, 290)
    chair(P, 620, 620, 290)
    person(P, 220, 610, 270, sit=True, coat=OCHRE, profile=0.5)
    return fin(P, 8322)


def r18a4():
    P = Paint(8331)
    backdrop(P, "day", 230, seed=8331, clouds=2)
    terrace(P, 270, 380, (84, 130, 86), seed=4)
    terrace(P, 380, 280, (70, 116, 80), seed=5)
    stone_stairs(P, 380, 700, 300, 625, steps=6)
    person(P, 520, 420, 190, coat=OCHRE, profile=0.3)
    person(P, 470, 620, 230, coat=BLUE_COAT, profile=-0.3)
    hydrangea(P, 160, 560, 54, seed=5)
    return fin(P, 8332)


def r18a5():
    P = Paint(8341)
    night_room(P, sky_top=(24, 48, 92), sky_bot=(226, 152, 98), win=(110, 70, 400, 320), stars=0)
    table(P, 140, 960, 450)
    phone(P, 520, 442, w=110, lit=True)
    P.glow(520, 410, 130, (150, 190, 230), 0.3)
    lamp(P, 760, 450, h=120)
    letter(P, 330, 448, w=150)
    return fin(P, 8342)


def r18a6():
    P = Paint(8351)
    room_bg(P, (14, 36, 46))
    stone_wall(P, 140, 560, seed=8, base=(70, 66, 62))
    cobbles(P, 540, glow_x=540)
    door(P, 420, 200, 620, 540, lit=True, ajar=0.15)
    stone_stairs(P, 380, 660, 520, 600, steps=2)
    pot_plant(P, 330, 546, 1.3, seed=2)
    lantern(P, 720, 340, 1.2)
    P.glow(720, 360, 120, WARM, 0.4)
    return fin(P, 8352)


def r18a7():
    P = Paint(8361)
    backdrop(P, "dawn", 300, sunp=(540, 290, 40), seed=8361, clouds=2)
    pier(P, -5, SW + 5, 480)
    foam(P, 0, SW, 560, n=30, seed=6)
    person(P, 470, 482, 250, coat=OCHRE, profile=0.3)
    person(P, 590, 482, 240, coat=BLUE_COAT, profile=-0.3)
    return fin(P, 8362)


SCENES = {n: f for n, f in globals().items() if re.match(r"^r\d\d", n) and callable(f)}
