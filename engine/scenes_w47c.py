"""Cenas 14-15/11/2026: Popper (q14), Zambrano (q14b), Bloch (q15), Alain (q15b)."""
from lib4 import *
from scenes_w47b import signpost, grass_field, dirt_path


# ============================================================ 14/11 Popper: errar e revisar
def q14a1():
    P = Paint(7601)
    room_bg(P, (22, 40, 52))
    floor(P, 560, (60, 44, 34))
    P.layer(rect(160, 70, 920, 440), (30, 50, 44), op=0.98, wob=1.5, rim=0.3)
    P.layer(rect(150, 440, 930, 456), (110, 76, 46), op=0.98, wob=1)
    P.line([(240, 150), (520, 160), (700, 150)], w=4, alpha=0.8, color=(236, 232, 220))
    P.line([(240, 230), (460, 240), (620, 226)], w=4, alpha=0.8, color=(236, 232, 220))
    P.line([(240, 310), (560, 300), (760, 316)], w=4, alpha=0.8, color=(236, 232, 220))
    P.line([(600, 220), (740, 250)], w=6, alpha=0.9, color=(200, 90, 70))
    person(P, 340, 600, 280, coat=OCHRE, profile=0.6)
    return fin(P, 7602)


def q14a2():
    P = Paint(7611)
    backdrop(P, "day", 250, seed=7611, clouds=2)
    grass_field(P, 330, (92, 138, 90))
    dirt_path(P, [(200, 640), (500, 330), (560, 330)], [(900, 640), (560, 330), (540, 330)])
    signpost(P, 700, 480, 260)
    person(P, 400, 600, 220, coat=OCHRE, profile=0.3)
    return fin(P, 7612)


def q14a3():
    P = Paint(7621)
    backdrop(P, "storm", 280, seed=7621, clouds=2)
    stone_wall(P, 360, SH + 5, seed=39, base=(96, 90, 80))
    boulder(P, 640, 470, 150, 90)
    person(P, 340, 600, 230, coat=OCHRE, profile=0.5)
    return fin(P, 7622)


def q14a4():
    P = Paint(7631)
    backdrop(P, "dawn", 280, sunp=(700, 250, 34), seed=7631, clouds=2)
    cliff(P, "right", top=300, seed=41, col=(24, 50, 58), reach=520)
    P.layer(rect(-5, 500, SW + 5, SH + 5), (86, 118, 84), op=0.98, wob=3, rim=0.2)
    signpost(P, 320, 540, 300, flip=-1)
    person(P, 560, 600, 220, coat=OCHRE, profile=0.5)
    return fin(P, 7632)


def q14a5():
    P = Paint(7641)
    room_bg(P, (24, 44, 56))
    floor(P, 550, (62, 46, 36))
    table(P, 220, 840, 430)
    cup(P, 440, 424)
    cup(P, 640, 424)
    lamp(P, 540, 430, 140)
    chair(P, 230, 600, 300)
    person(P, 230, 590, 285, sit=True, profile=0.7)
    chair(P, 850, 600, 300)
    person(P, 850, 590, 285, sit=True, coat=BLUE_COAT, profile=-0.7)
    return fin(P, 7642)


def q14a6():
    P = Paint(7651)
    backdrop(P, "day", 300, seed=7651, clouds=2)
    P.layer(rect(-5, 480, SW + 5, SH + 5), (210, 190, 150), op=0.98, wob=3, rim=0.15)
    bench(P, 400, 540, 300)
    person(P, 480, 540, 215, sit=True, profile=0.4)
    book(P, 590, 480, w=90, open_=True)
    gulls(P, [(780, 120, 1.0), (880, 160, 0.8)])
    return fin(P, 7652)


def q14a7():
    P = Paint(7661)
    backdrop(P, "dawn", 290, sunp=(540, 290, 36), seed=7661, clouds=2)
    grass_field(P, 420, (92, 138, 90))
    dirt_path(P, [(300, 640), (500, 420), (580, 420)], [(900, 640), (580, 420), (560, 420)], col=(206, 180, 130))
    person(P, 600, 540, 190, coat=OCHRE, profile=0.0)
    gulls(P, [(300, 150, 1.0)])
    return fin(P, 7662)


def q14b():
    P = Paint(7671)
    P.vgrad(-5, SH + 5, (150, 196, 186), (70, 118, 86), mask=rect(-5, -5, SW + 5, SH + 5), wob=0, rim=0, vary=0.1)
    big_tree(P, 120, 600, 520, lean=0.03, seed=3, crown=0.4)
    big_tree(P, 960, 600, 520, lean=-0.03, seed=4, crown=0.4)
    P.glow(540, 330, 360, WARM, 0.4)
    P.layer(ell(540, 560, 420, 60), (110, 150, 90), op=0.95, wob=3, rim=0.2)
    table(P, 400, 700, 470, ybot=620)
    book(P, 500, 466, w=100)
    candle(P, 620, 466)
    person(P, 360, 600, 250, sit=True, profile=0.5)
    return fin(P, 7672)


# ============================================================ 15/11 Bloch: esperança
def q15a1():
    P = Paint(7701)
    backdrop(P, "dawn", 300, sunp=(540, 290, 38), seed=7701, clouds=3)
    stone_wall(P, 520, SH + 5, seed=43, base=(104, 96, 84))
    person(P, 400, 530, 230, coat=OCHRE, profile=0.4)
    gulls(P, [(700, 150, 1.0), (800, 120, 0.8)])
    return fin(P, 7702)


def q15a2():
    P = Paint(7711)
    room_bg(P, (22, 40, 52))
    floor(P, 560, (56, 40, 32))
    door(P, 380, 90, 700, 560, lit=False)
    P.layer(rect(380, 552, 700, 566), (255, 214, 130), op=0.95, wob=0.8, rim=0.1)
    P.glow(540, 560, 200, WARM, 0.35)
    person(P, 540, 620, 250, coat=OCHRE, profile=0.0)
    return fin(P, 7712)


def q15a3():
    P = Paint(7721)
    backdrop(P, "dusk", 220, sunp=(880, 200, 26), seed=7721, clouds=2)
    P.layer(rect(-5, 420, SW + 5, SH + 5), (84, 66, 50), op=0.98, wob=3, rim=0.2)
    table(P, 380, 700, 470, ybot=620)
    chair(P, 320, 610, 300)
    chair(P, 780, 610, 300, facing=1)
    cup(P, 540, 464, steam=False)
    return fin(P, 7722)


def q15a4():
    P = Paint(7731)
    room_bg(P, (18, 36, 48))
    floor(P, 570, (56, 40, 32))
    door(P, 380, 90, 700, 560, lit=True, ajar=0.5)
    P.glow(540, 330, 360, WARM, 0.5)
    person(P, 540, 620, 240, coat=OCHRE, profile=0.2)
    return fin(P, 7732)


def q15a5():
    P = Paint(7741)
    room_bg(P, (24, 44, 56))
    floor(P, 540, (62, 44, 34))
    window_frame(P, 720, 70, 980, 320, sky_top=(24, 44, 76), sky_bot=(90, 120, 140), stars=15)
    table(P, 120, 640, 420)
    letter(P, 300, 410, w=150)
    phone(P, 460, 414, lit=True)
    pot_plant(P, 560, 420, 0.9, kind="sprout")
    chair(P, 320, 590, 300)
    person(P, 320, 580, 285, sit=True, profile=0.3)
    return fin(P, 7742)


def q15a6():
    P = Paint(7751)
    backdrop(P, "dawn", 280, sunp=(800, 270, 30), seed=7751, clouds=2)
    facade(P, 380, 700, 300, 600, col=(214, 196, 150))
    lit_window(P, 500, 340, 580, 430, silhouette=False)
    ladder(P, 440, 600, 300, w=60, lean=20)
    sapling(P, 200, 600, 110)
    person(P, 340, 610, 210, coat=OCHRE, profile=0.7)
    return fin(P, 7752)


def q15a7():
    P = Paint(7761)
    backdrop(P, "night", 300, moonp=(820, 100, 30), seed=7761, clouds=1)
    cliff(P, "left", top=380, seed=47, col=(14, 36, 46), reach=720)
    lantern(P, 560, 360, 1.2)
    person(P, 520, 440, 190, coat=OCHRE, profile=0.5)
    P.glow(560, 380, 220, WARM, 0.5)
    return fin(P, 7762)


def q15b():
    P = Paint(7771)
    backdrop(P, "dawn", 300, sunp=(760, 290, 34), seed=7771, clouds=2)
    P.layer(rect(-5, 470, SW + 5, SH + 5), (186, 150, 106), op=0.98, wob=3, rim=0.2)
    table(P, 260, 580, 490)
    cup(P, 360, 484, steam=True)
    pot_plant(P, 480, 490, 0.9)
    chair(P, 330, 620, 280)
    person(P, 330, 610, 270, sit=True, profile=0.5)
    hydrangea(P, 900, 500, 56, seed=5)
    return fin(P, 7772)


SCENES = {n: f for n, f in globals().items() if n.startswith("q") and callable(f)}
