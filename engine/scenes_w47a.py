"""Cenas 09-11/11/2026: Heidegger (q09), Heschel (q09b), Stein (q10), Benjamin (q10b), Han (q11), Wang Yangming (q11b)."""
from lib4 import *

NIGHT_ROOM = (22, 44, 56)


def desk_room(P, sky=(120, 170, 190), bot=(246, 226, 180)):
    room_bg(P, NIGHT_ROOM)
    floor(P, 540, (62, 44, 34))
    window_frame(P, 720, 70, 980, 320, sky_top=sky, sky_bot=bot)


# ============================================================ 09/11 Heidegger: soltar
def q09a1():
    P = Paint(7101)
    backdrop(P, "dawn", 300, sunp=(760, 280, 34), seed=7101, clouds=3)
    cliff(P, "left", top=410, seed=21, col=(18, 44, 52), reach=640)
    person(P, 420, 430, 230, coat=OCHRE, profile=0.3)
    gulls(P, [(800, 140, 1.1), (900, 180, 0.8), (700, 120, 0.9)])
    return fin(P, 7102)


def q09a2():
    P = Paint(7111)
    desk_room(P, sky=(30, 50, 80), bot=(60, 90, 110))
    table(P, 90, 700, 410)
    stack_papers(P, 200, 400, n=5, w=130)
    stack_papers(P, 420, 400, n=3, w=130)
    clock_round(P, 560, 160, r=62, hands=(0.35, 0.05))
    lamp(P, 620, 410, 150)
    chair(P, 400, 590, 310)
    person(P, 400, 580, 290, sit=True, profile=0.2)
    return fin(P, 7112)


def q09a3():
    P = Paint(7121)
    backdrop(P, "storm", 280, seed=7121, clouds=3)
    boat(P, 760, 330, 1.0, lit=True)
    pier(P, -5, 700, 470)
    person(P, 560, 472, 230, coat=OCHRE, profile=0.5)
    foam(P, 0, 1080, 540, n=30, seed=5)
    return fin(P, 7122)


def q09a4():
    P = Paint(7131)
    backdrop(P, "day", 260, seed=7131, clouds=2)
    terrace(P, 300, 400, (84, 130, 86), seed=2)
    terrace(P, 430, 260, (70, 116, 80), seed=3)
    waterfall(P, 820, 250, 470, 40, 120)
    person(P, 330, 560, 230, coat=OCHRE, profile=0.4)
    hydrangea(P, 120, 520, 50, seed=3)
    return fin(P, 7132)


def q09a5():
    P = Paint(7141)
    desk_room(P)
    table(P, 120, 660, 420)
    stack_papers(P, 220, 410, n=4, w=120)
    cup(P, 520, 414, steam=True)
    candle(P, 600, 414)
    chair(P, 400, 590, 310)
    person(P, 400, 580, 292, sit=True, profile=-0.3)
    P.glow(840, 220, 260, WARM, 0.3)
    return fin(P, 7142)


def q09a6():
    P = Paint(7151)
    backdrop(P, "day", 300, seed=7151, clouds=2)
    P.layer(rect(-5, 470, SW + 5, SH + 5), (222, 202, 160), op=0.98, wob=3, rim=0.15)
    P.layer(poly([(780, 110), (830, 160), (780, 250), (730, 160)]), (206, 96, 78), op=0.98, wob=1.5, rim=0.3)
    P.line([(780, 250), (700, 330), (640, 420), (560, 500)], w=2, alpha=0.7)
    person(P, 540, 560, 230, coat=OCHRE, profile=0.5)
    gulls(P, [(300, 120, 1.0)])
    return fin(P, 7152)


def q09a7():
    P = Paint(7161)
    backdrop(P, "dusk", 300, sunp=(800, 290, 30), seed=7161, clouds=2)
    bench(P, 460, 520, 300)
    person(P, 530, 520, 220, sit=True, profile=0.3)
    cup(P, 650, 470, steam=True)
    lantern(P, 160, 450, 1.1)
    foam(P, 0, 1080, 560, n=28, seed=8)
    return fin(P, 7162)


def q09b():
    P = Paint(7171)
    backdrop(P, "day", 300, seed=7171, clouds=2)
    P.layer(rect(-5, 450, SW + 5, SH + 5), (226, 196, 140), op=0.98, wob=3, rim=0.2)
    hydrangea(P, 180, 430, 56, seed=2)
    hydrangea(P, 920, 440, 60, col=(120, 150, 220), seed=4)
    table(P, 380, 700, 420)
    cup(P, 500, 414, steam=True)
    book(P, 590, 416, w=110)
    chair(P, 330, 590, 300)
    person(P, 330, 580, 285, sit=True, profile=0.3)
    return fin(P, 7172)


# ============================================================ 10/11 Stein: compreensão
def q10a1():
    P = Paint(7201)
    backdrop(P, "dusk", 300, sunp=(540, 300, 30), seed=7201, clouds=2)
    bench(P, 330, 520, 420)
    person(P, 450, 520, 215, sit=True, profile=0.5)
    person(P, 620, 520, 215, sit=True, coat=BLUE_COAT, profile=-0.5)
    foam(P, 0, 1080, 570, n=26, seed=9)
    return fin(P, 7202)


def q10a2():
    P = Paint(7211)
    desk_room(P, sky=(40, 70, 100), bot=(100, 130, 150))
    table(P, 180, 760, 420)
    cup(P, 400, 414)
    cup(P, 540, 414)
    phone(P, 640, 414, lit=True)
    chair(P, 250, 590, 300, facing=1)
    person(P, 250, 580, 285, sit=True, profile=0.5)
    chair(P, 700, 590, 300)
    person(P, 700, 580, 285, sit=True, coat=BLUE_COAT, profile=0.9)
    return fin(P, 7212)


def q10a3():
    P = Paint(7221)
    backdrop(P, "dusk", 220, sunp=(880, 200, 26), seed=7221, clouds=2)
    stone_wall(P, 260, SH + 5, seed=33, base=(100, 92, 80))
    stone_stairs(P, 160, 800, 330, 640, steps=8)
    person(P, 260, 600, 190, coat=OCHRE, profile=0.5)
    person(P, 610, 400, 150, coat=BLUE_COAT, profile=-0.5)
    return fin(P, 7222)


def q10a4():
    P = Paint(7231)
    backdrop(P, "night", 300, moonp=(780, 110, 32), seed=7231, clouds=1)
    pier(P, -5, 1085, 470)
    person(P, 380, 472, 220, coat=OCHRE, profile=0.5)
    person(P, 700, 472, 220, coat=BLUE_COAT, profile=-0.5)
    lantern(P, 480, 410, 1.0)
    lantern(P, 600, 410, 1.0)
    P.glow(540, 410, 160, WARM, 0.45)
    return fin(P, 7232)


def q10a5():
    P = Paint(7241)
    desk_room(P)
    table(P, 200, 800, 420)
    cup(P, 440, 414)
    cup(P, 580, 414)
    candle(P, 510, 414)
    chair(P, 250, 590, 300)
    person(P, 250, 580, 285, sit=True, profile=0.7)
    chair(P, 780, 590, 300)
    person(P, 780, 580, 285, sit=True, coat=BLUE_COAT, profile=-0.7)
    return fin(P, 7242)


def q10a6():
    P = Paint(7251)
    backdrop(P, "night", 310, moonp=(300, 120, 34), seed=7251, clouds=1)
    P.layer(rect(-5, 500, SW + 5, SH + 5), (60, 70, 66), op=0.98, wob=3, rim=0.2)
    bench(P, 460, 520, 380)
    person(P, 600, 520, 215, sit=True, profile=0.4)
    person(P, 720, 520, 215, sit=True, coat=BLUE_COAT, profile=0.0)
    lantern(P, 240, 440, 1.0)
    return fin(P, 7252)


def q10a7():
    P = Paint(7261)
    desk_room(P, sky=(24, 40, 70), bot=(60, 80, 110))
    table(P, 140, 640, 420)
    letter(P, 360, 408, w=170, tilt=-0.05)
    lamp(P, 560, 420, 160)
    chair(P, 300, 590, 300)
    person(P, 300, 580, 285, sit=True, profile=0.3)
    return fin(P, 7262)


def q10b():
    P = Paint(7271)
    room_bg(P, (30, 54, 66))
    floor(P, 560, (66, 48, 36))
    window_frame(P, 240, 70, 840, 380, sky_top=(120, 140, 154), sky_bot=(190, 200, 204))
    rain(P, 240, 840, 70, 380, n=90, seed=5)
    P.layer(rect(210, 380, 870, 410), (120, 84, 52), op=0.98, wob=1.5, rim=0.3)
    P.layer(ell(520, 380, 70, 16), (150, 110, 70), op=0.98, wob=2, rim=0.3)
    P.layer(ell(520, 362, 20, 26), (240, 232, 205), op=0.98, wob=1, rim=0.3)
    chair(P, 220, 590, 300)
    person(P, 220, 580, 290, sit=True, profile=0.6)
    return fin(P, 7272)


# ============================================================ 11/11 Han: autoexigência
def q11a1():
    P = Paint(7301)
    desk_room(P, sky=(14, 24, 50), bot=(30, 56, 80))
    table(P, 100, 740, 410)
    stack_papers(P, 220, 400, n=6, w=140)
    stack_papers(P, 450, 400, n=4, w=130)
    lamp(P, 620, 410, 160)
    clock_round(P, 400, 170, r=64, hands=(0.9, 0.3))
    chair(P, 330, 590, 320)
    person(P, 330, 580, 300, sit=True, profile=0.2)
    return fin(P, 7302)


def q11a2():
    P = Paint(7311)
    room_bg(P, (60, 96, 104))
    floor(P, 540, (150, 118, 84))
    window_frame(P, 700, 60, 980, 330, sky_top=(130, 190, 210), sky_bot=(250, 236, 190))
    P.glow(840, 200, 320, WARM, 0.4)
    table(P, 120, 620, 420, col=(170, 124, 80))
    stack_papers(P, 250, 410, n=3, w=120)
    cup(P, 450, 414, steam=False)
    chair(P, 300, 590, 300)
    person(P, 300, 580, 290, sit=True, profile=0.5)
    return fin(P, 7312)


def q11a3():
    P = Paint(7321)
    room_bg(P, (22, 44, 56))
    floor(P, 560, (60, 44, 34))
    wheel(P, 540, 330, 250, spokes=10)
    person(P, 540, 590, 230, coat=OCHRE, profile=0.0)
    return fin(P, 7322)


def q11a4():
    P = Paint(7331)
    room_bg(P, (16, 36, 48))
    floor(P, 560, (50, 38, 30))
    import numpy as _np
    r = _np.random.default_rng(3)
    for k in range(14):
        x = 70 + (k % 7) * 150 + r.uniform(-20, 20)
        y = 120 + (k // 7) * 150 + r.uniform(-15, 15)
        phone(P, x, y, w=64, lit=True, tilt=r.uniform(-0.15, 0.15))
    person(P, 540, 600, 190, coat=OCHRE, profile=0.0)
    return fin(P, 7332)


def q11a5():
    P = Paint(7341)
    desk_room(P, sky=(24, 40, 70), bot=(70, 90, 110))
    table(P, 160, 700, 420)
    book(P, 360, 416, w=170, open_=True)
    candle(P, 560, 414, h=44)
    cup(P, 280, 414, steam=True)
    chair(P, 400, 590, 310)
    person(P, 400, 580, 292, sit=True, profile=0.4)
    return fin(P, 7342)


def q11a6():
    P = Paint(7351)
    backdrop(P, "dusk", 300, sunp=(300, 290, 30), seed=7351, clouds=2)
    pier(P, -5, 900, 470)
    chair(P, 560, 468, 220, facing=1)
    person(P, 700, 472, 225, coat=OCHRE, profile=0.5)
    foam(P, 0, 1080, 540, n=30, seed=7)
    return fin(P, 7352)


def q11a7():
    P = Paint(7361)
    backdrop(P, "dawn", 310, sunp=(700, 300, 36), seed=7361, clouds=2)
    P.layer(rect(-5, 470, SW + 5, SH + 5), (176, 140, 98), op=0.98, wob=3, rim=0.2)
    table(P, 260, 560, 480)
    cup(P, 360, 474, steam=True)
    pot_plant(P, 470, 480, 0.9)
    chair(P, 330, 610, 280)
    person(P, 330, 600, 270, sit=True, profile=0.5)
    return fin(P, 7362)


def q11b():
    P = Paint(7371)
    backdrop(P, "dawn", 250, sunp=(540, 160, 40), seed=7371, clouds=2)
    stone_wall(P, 280, SH + 5, seed=35, base=(100, 92, 80))
    stone_stairs(P, 340, 740, 300, 640, steps=9)
    P.glow(540, 190, 300, WARM, 0.4)
    person(P, 540, 620, 200, coat=OCHRE, profile=0.0)
    return fin(P, 7372)


SCENES = {n: f for n, f in globals().items() if n.startswith("q") and callable(f)}
