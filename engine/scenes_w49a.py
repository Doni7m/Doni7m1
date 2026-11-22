"""Cenas 23-24/11/2026: Seneca (r23), Simone Weil (r24)."""
import re
from lib4 import *

NIGHT_ROOM = (22, 44, 56)
ELDER = (206, 204, 200)


def hourglass(P, x, ybase, h=120, sand=(236, 190, 100), level=0.5):
    w = h * 0.34
    wood = (92, 62, 38)
    P.layer(rect(x - w - 8, ybase - 10, x + w + 8, ybase), wood, op=0.98, wob=1, rim=0.3)
    P.layer(rect(x - w - 8, ybase - h, x + w + 8, ybase - h + 10), wood, op=0.98, wob=1, rim=0.3)
    ym = ybase - h / 2
    P.layer(poly([(x - w, ybase - h + 10), (x + w, ybase - h + 10), (x + 4, ym), (x - 4, ym)]), (206, 230, 232), op=0.55, wob=0.8, rim=0.3)
    P.layer(poly([(x - 4, ym), (x + 4, ym), (x + w, ybase - 10), (x - w, ybase - 10)]), (206, 230, 232), op=0.55, wob=0.8, rim=0.3)
    # areia embaixo e um pouco no alto
    yb = ybase - 10 - (h / 2 - 10) * level
    k = (ybase - 10 - yb) / (h / 2 - 10)
    P.layer(poly([(x - w * k, yb), (x + w * k, yb), (x + w, ybase - 10), (x - w, ybase - 10)]), sand, op=0.95, wob=0.8)
    P.layer(poly([(x - w * 0.5, ybase - h + 10), (x + w * 0.5, ybase - h + 10), (x + 2, ym - 18), (x - 2, ym - 18)]), sand, op=0.9, wob=0.8)
    P.line([(x, ym - 18), (x, ym + 24)], w=2, alpha=0.7, color=sand)
    for dx in (-w - 4, w + 4):
        P.layer(rect(x + dx - 3, ybase - h + 10, x + dx + 3, ybase - 10), wood, op=0.98, wob=0.8)
    P.glow(x, ym, h * 0.9, WARM, 0.25)


# ============================================================ 23/11 Seneca: tempo e atencao
def r23a1():
    P = Paint(9101)
    backdrop(P, "dusk", 290, sunp=(700, 280, 44), seed=9101, clouds=2)
    far_island(P, 290, span=(120, 260))
    stone_wall(P, 500, SH + 5, seed=7, base=(98, 88, 78))
    hourglass(P, 760, 500, 150, level=0.35)
    person(P, 340, 640, 330, coat=OCHRE, profile=0.3)
    gulls(P, [(220, 150, 1.0), (300, 190, 0.8), (880, 120, 0.9)])
    return fin(P, 9102)


def r23a2():
    P = Paint(9111)
    night_room(P)
    clock_round(P, 540, 150, r=70, hands=(0.62, 0.93))
    table(P, 90, 990, 440)
    phone(P, 520, 430, w=170, lit=True)
    P.glow(520, 400, 170, (150, 190, 230), 0.45)
    for i, x in enumerate((200, 300, 380, 700, 790, 880)):
        paper_tag(P, x, 436 + (i % 2) * 6, w=70, tilt=(-0.1, 0.12)[i % 2])
    stack_papers(P, 930, 438, n=6, w=110)
    letter(P, 215, 420, w=130, tilt=0.06)
    cup(P, 650, 430, steam=False)
    return fin(P, 9112)


def night_room(P, sky_top=NAVY, sky_bot=(30, 82, 96), win=(720, 70, 980, 330), stars=30):
    room_bg(P, NIGHT_ROOM)
    floor(P, 560, (62, 44, 34))
    window_frame(P, *win, sky_top=sky_top, sky_bot=sky_bot, stars=stars, seed=5)


def r23a3():
    P = Paint(9121)
    backdrop(P, "storm", 200, seed=9121)
    hill_houses(P, -10, SW + 10, 215, n=10, seed=91, lit=True)
    cobbles(P, 400, glow_x=540)
    facade(P, 700, 1010, 190, 420)
    clock_round(P, 855, 250, r=52, hands=(0.1, 0.55))
    rain(P, 0, SW, 0, 600, n=110, seed=3)
    person(P, 420, 600, 280, coat=OCHRE, profile=0.7)
    lantern(P, 250, 430, 1.1)
    for x, y, s in [(560, 520, 0.0)]:
        pass
    return fin(P, 9122)


def r23a4():
    P = Paint(9131)
    room_bg(P, (30, 48, 56))
    floor(P, 560, (70, 48, 34))
    window_frame(P, 90, 60, 400, 340, sky_top=(236, 170, 100), sky_bot=(252, 220, 150), stars=0, seed=3)
    P.glow(260, 220, 300, WARM, 0.5)
    bookshelf(P, 760, 80, 1020, 440, rows=4, seed=4)
    table(P, 150, 760, 450)
    hourglass(P, 560, 450, 190, level=0.45)
    book(P, 330, 440, w=190)
    candle(P, 700, 448, h=60)
    return fin(P, 9132)


def r23a5():
    P = Paint(9141)
    room_bg(P, (26, 46, 56))
    floor(P, 560, (66, 46, 32))
    window_frame(P, 700, 60, 1000, 330, sky_top=(120, 170, 190), sky_bot=(246, 226, 180), stars=0, seed=2)
    P.glow(850, 200, 280, WARM, 0.4)
    table(P, 120, 800, 450)
    book(P, 500, 442, w=190)
    cup(P, 680, 446, steam=True)
    lamp(P, 190, 452, h=130)
    chair(P, 400, 620, 310)
    person(P, 400, 610, 290, sit=True, coat=OCHRE, profile=0.3)
    return fin(P, 9142)


def r23a6():
    P = Paint(9151)
    night_room(P, win=(110, 70, 370, 310), stars=22)
    bed(P, 560, 1010, 460)
    person(P, 800, 480, 240, coat=(120, 96, 120), hair=(222, 220, 214), sit=True, profile=-0.4)
    lamp(P, 500, 500, h=110)
    person(P, 400, 620, 290, coat=OCHRE, profile=0.5)
    cup(P, 500, 500, w=60, steam=True)
    return fin(P, 9152)


def r23a7():
    P = Paint(9161)
    backdrop(P, "dusk", 270, sunp=(560, 270, 62), seed=9161, clouds=1)
    P.glow(560, 270, 420, WARM, 0.45)
    stone_wall(P, 430, 520, seed=11, cap=True)
    floor(P, 520, (150, 110, 74))
    table(P, 640, 1010, 480)
    cup(P, 760, 476, steam=True)
    book(P, 900, 474, w=120)
    chair(P, 350, 630, 330)
    person(P, 350, 620, 300, sit=True, coat=OCHRE, profile=0.5)
    pot_plant(P, 120, 520, 1.4, seed=5)
    string_lights(P, 60, 1020, 70, sag=40, n=13)
    return fin(P, 9162)


def r23b():
    P = Paint(9171)
    backdrop(P, "day", 250, seed=9171, clouds=2)
    foam(P, 380, 700, 330, n=22, seed=9)
    stone_wall(P, 120, SH + 5, seed=12, x0=-5, x1=380, base=(96, 88, 78))
    stone_wall(P, 120, SH + 5, seed=13, x0=700, x1=SW + 5, base=(90, 82, 74))
    P.layer(rect(340, 90, 740, 160), (104, 94, 82), op=0.98, wob=2, rim=0.3, vary=0.18)
    stone_stairs(P, 380, 700, 450, 625, steps=4)
    hydrangea(P, 180, 600, 60, seed=7)
    person(P, 540, 560, 230, coat=OCHRE, profile=0.1)
    return fin(P, 9172)


# ============================================================ 24/11 Simone Weil: atencao como escuta
def r24a1():
    P = Paint(9201)
    backdrop(P, "dusk", 280, sunp=(540, 270, 36), seed=9201, clouds=2)
    floor(P, 450, (110, 94, 78))
    stone_wall(P, 400, 460, seed=21, cap=True)
    chair(P, 330, 610, 320)
    chair(P, 750, 610, 320)
    table(P, 440, 640, 500, legs=True)
    cup(P, 500, 496, steam=True)
    cup(P, 590, 496, steam=True)
    lantern(P, 880, 440, 1.0)
    return fin(P, 9202)


def r24a2():
    P = Paint(9211)
    night_room(P, sky_top=(24, 48, 92), sky_bot=(226, 152, 98), win=(380, 60, 700, 280), stars=0)
    table(P, 360, 720, 450)
    cup(P, 450, 446, steam=True)
    cup(P, 630, 446, steam=True)
    candle(P, 540, 448, h=44)
    chair(P, 240, 620, 300)
    chair(P, 840, 620, 300)
    person(P, 270, 610, 285, sit=True, coat=OCHRE, profile=0.6)
    person(P, 810, 610, 275, sit=True, coat=BLUE_COAT, profile=-0.6)
    return fin(P, 9212)


def r24a3():
    P = Paint(9221)
    backdrop(P, "day", 230, seed=9221, clouds=2)
    hill_houses(P, -10, SW + 10, 250, n=9, seed=95, lit=False)
    floor(P, 430, (104, 92, 78))
    table(P, 340, 760, 470)
    phone(P, 430, 464, w=120, lit=True)
    cup(P, 660, 466, steam=True)
    chair(P, 240, 630, 320)
    chair(P, 860, 630, 320)
    person(P, 270, 620, 285, sit=True, coat=OCHRE, profile=0.5)
    person(P, 830, 620, 280, sit=True, coat=RUST_COAT, profile=-0.6)
    return fin(P, 9222)


def r24a4():
    P = Paint(9231)
    backdrop(P, "night", 200, moonp=(180, 90, 26), seed=9231)
    hill_houses(P, -10, SW + 10, 230, n=10, seed=97, lit=True)
    stone_wall(P, 340, 450, seed=23, base=(70, 70, 70))
    cobbles(P, 450, glow_x=540)
    P.glow(540, 480, 260, WARM, 0.35)
    person(P, 400, 620, 300, coat=OCHRE, profile=0.8)
    person(P, 690, 620, 285, coat=BLUE_COAT, profile=-0.8)
    lantern(P, 545, 470, 1.2)
    return fin(P, 9232)


def r24a5():
    P = Paint(9241)
    backdrop(P, "day", 300, seed=9241, clouds=2, island=True)
    cliff(P, "right", top=330, seed=51, col=(40, 78, 74), reach=420)
    boat(P, 300, 380, 0.6)
    floor(P, 480, (118, 104, 86))
    stone_wall(P, 440, 500, seed=24, cap=True)
    bench(P, 520, 610, 380)
    person(P, 450, 610, 255, coat=OCHRE, sit=True, profile=0.5)
    person(P, 590, 610, 245, coat=SAGE_COAT, sit=True, profile=-0.4)
    hydrangea(P, 940, 540, 58, seed=8)
    return fin(P, 9242)


def r24a6():
    P = Paint(9251)
    room_bg(P, (14, 36, 46))
    stone_wall(P, 100, 440, seed=25, base=(70, 66, 62))
    door(P, 440, 150, 640, 420, lit=True)
    person(P, 540, 420, 200, coat=BLUE_COAT, hair=(140, 130, 120), profile=-0.1)
    stone_stairs(P, 340, 740, 420, 625, steps=5)
    person(P, 540, 590, 230, coat=OCHRE, profile=0.1)
    lantern(P, 780, 330, 1.1)
    pot_plant(P, 250, 430, 1.2, seed=6)
    return fin(P, 9252)


def r24a7():
    P = Paint(9261)
    night_room(P, sky_top=(120, 170, 190), sky_bot=(246, 226, 180), win=(90, 60, 400, 330), stars=0)
    P.glow(250, 200, 280, WARM, 0.35)
    table(P, 120, 980, 450)
    cup(P, 450, 446, w=110, steam=True)
    cup(P, 640, 446, w=110, steam=True)
    letter(P, 810, 440, w=170, tilt=0.04)
    pot_plant(P, 920, 446, 1.0, seed=3)
    candle(P, 540, 448, h=40)
    return fin(P, 9262)


def r24b():
    P = Paint(9271)
    backdrop(P, "dusk", 170, sunp=(840, 170, 26), seed=9271)
    hill_houses(P, -10, SW + 10, 195, n=10, seed=99, lit=True)
    stone_wall(P, 300, 440, seed=26, base=(92, 84, 76))
    cobbles(P, 430, glow_x=540)
    string_lights(P, 40, 1040, 90, sag=50, n=15)
    P.layer(ell(540, 500, 190, 40), (150, 104, 62), op=0.98, wob=2, rim=0.3)
    P.layer(rect(520, 520, 560, 600), (96, 64, 38), op=0.98, wob=1.5)
    lantern(P, 540, 480, 1.0)
    cup(P, 450, 505, steam=False)
    cup(P, 640, 505, steam=False)
    for x, yb, h, c, pf in [(170, 560, 240, SAGE_COAT, 0.6), (900, 560, 235, RUST_COAT, -0.6),
                            (300, 620, 290, BLUE_COAT, 0.5), (800, 620, 285, (120, 110, 130), -0.5),
                            (545, 640, 310, OCHRE, 0.1)]:
        person(P, x, yb, h, coat=c, profile=pf)
    return fin(P, 9272)


SCENES = {n: f for n, f in globals().items() if re.match(r"^r\d\d", n) and callable(f)}
