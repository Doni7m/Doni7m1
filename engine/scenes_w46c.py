"""Cenas 07-08/11/2026: Gadamer (n07), Aquino (n08) e imagens únicas B (02-08/11)."""
from lib4 import *


def chessboard(P, x0, y0, x1, y1, n=8):
    w, h = (x1 - x0) / n, (y1 - y0) / n
    for i in range(n):
        for j in range(n):
            col = (232, 214, 170) if (i + j) % 2 == 0 else (96, 66, 40)
            P.layer(rect(x0 + i * w, y0 + j * h, x0 + (i + 1) * w, y0 + (j + 1) * h), col, op=0.98, wob=0.6, rim=0.1)


# ============================================================ 07/11 Gadamer: conversa
def n07a1():
    P = Paint(6501)
    backdrop(P, "dusk", 280, sunp=(860, 260, 26), seed=6501, clouds=2)
    P.layer(rect(-5, 400, SW + 5, SH + 5), (170, 150, 110), op=0.97, wob=3, rim=0.2)
    table(P, 340, 760, 450, legs=True)
    cup(P, 480, 444, steam=True)
    cup(P, 620, 444, steam=True)
    chair(P, 290, 610, 300)
    chair(P, 810, 610, 300)
    person(P, 290, 600, 280, sit=True, coat=OCHRE, profile=0.7)
    person(P, 810, 600, 280, sit=True, coat=BLUE_COAT, profile=-0.7)
    return fin(P, 6502)


def n07a2():
    P = Paint(6511)
    backdrop(P, "night", 200, moonp=(860, 90, 22), seed=6511)
    cobbles(P, 340, seed=9, glow_x=540)
    facade(P, 20, 280, 220, 400, col=(170, 150, 112))
    lit_window(P, 80, 260, 140, 330)
    lit_window(P, 170, 260, 230, 330)
    lantern(P, 760, 330, 1.2)
    person(P, 470, 560, 230, coat=OCHRE, profile=0.6)
    person(P, 590, 560, 220, coat=BLUE_COAT, profile=-0.6)
    return fin(P, 6512)


def n07a3():
    P = Paint(6521)
    room_bg(P, (20, 40, 54))
    floor(P, 560, (60, 44, 34))
    window_frame(P, 40, 80, 260, 330, sky_top=(24, 48, 92), sky_bot=(226, 152, 98))
    window_frame(P, 820, 80, 1040, 330, sky_top=(13, 29, 58), sky_bot=(30, 82, 96), stars=14, seed=4)
    table(P, 220, 860, 430)
    chair(P, 250, 600, 300)
    chair(P, 830, 600, 300)
    person(P, 250, 590, 280, sit=True, coat=OCHRE, profile=-0.8)
    person(P, 830, 590, 280, sit=True, coat=BLUE_COAT, profile=0.8)
    cup(P, 520, 424, steam=False)
    return fin(P, 6522)


def n07a4():
    P = Paint(6531)
    backdrop(P, "night", 260, moonp=(180, 100, 24), seed=6531)
    stone_wall(P, 430, SH + 5, seed=41, base=(84, 80, 72))
    person(P, 400, 432, 230, sit=True, coat=OCHRE, profile=0.7)
    person(P, 680, 432, 220, sit=True, coat=SAGE_COAT, profile=-0.7)
    lantern(P, 540, 400, 1.3)
    gulls(P, [(840, 120, 0.9)])
    return fin(P, 6532)


def n07a5():
    P = Paint(6541)
    room_bg(P, (24, 46, 58))
    floor(P, 540, (64, 46, 34))
    window_frame(P, 700, 70, 960, 330, sky_top=(110, 140, 160), sky_bot=(180, 200, 206))
    rain(P, 700, 960, 70, 330, n=50, seed=8)
    table(P, 160, 680, 430)
    cup(P, 300, 424, steam=True)
    cup(P, 520, 424, steam=True)
    book(P, 410, 424, w=110)
    chair(P, 300, 600, 300)
    chair(P, 560, 600, 300, facing=1)
    person(P, 300, 590, 285, sit=True, coat=OCHRE, profile=0.6)
    return fin(P, 6542)


def n07a6():
    P = Paint(6551)
    room_bg(P, (22, 44, 56))
    floor(P, 480, (62, 44, 34))
    table(P, 120, 960, 400)
    chessboard(P, 360, 330, 660, 396, n=8)
    for k in range(6):
        P.layer(ell(380 + k * 44, 338 + (k % 3) * 18, 8, 12), (30, 24, 24) if k % 2 else (246, 238, 220), op=0.98, wob=0.6, rim=0.2)
    cup(P, 220, 392, steam=True)
    cup(P, 800, 392, steam=True)
    person(P, 540, 620, 250, coat=OCHRE, profile=0.0)
    lamp(P, 940, 470, h=130)
    return fin(P, 6552)


def n07a7():
    P = Paint(6561)
    backdrop(P, "dusk", 250, sunp=(540, 240, 30), seed=6561, clouds=2)
    P.layer(rect(-5, 330, SW + 5, SH + 5), (96, 76, 56), op=0.98, wob=3, rim=0.15)
    string_lights(P, 60, 1020, 130, sag=50, n=13)
    table(P, 300, 780, 470)
    cup(P, 480, 464, steam=True)
    cup(P, 600, 464, steam=True)
    P.layer(rrect(520, 420, 560, 464, 6), (60, 100, 90), op=0.98, wob=1, rim=0.3)
    chair(P, 250, 620, 300)
    chair(P, 830, 620, 300)
    person(P, 250, 610, 285, sit=True, coat=OCHRE, profile=0.8)
    person(P, 830, 610, 280, sit=True, coat=RUST_COAT, profile=-0.8)
    return fin(P, 6562)


# ============================================================ 08/11 Aquino: tristeza e companhia
def n08a1():
    P = Paint(6601)
    backdrop(P, "storm", 280, seed=6601, clouds=4)
    P.layer(rect(-5, 400, SW + 5, SH + 5), (70, 70, 66), op=0.98, wob=3, rim=0.2)
    P.layer(poly([(260, 190), (820, 190), (900, 250), (180, 250)]), (120, 64, 48), op=0.98, wob=2, rim=0.3)
    P.layer(rect(280, 250, 300, 500), (84, 56, 34), op=0.98, wob=1.5)
    P.layer(rect(800, 250, 820, 500), (84, 56, 34), op=0.98, wob=1.5)
    bench(P, 540, 540, w=300)
    person(P, 480, 536, 240, sit=True, coat=OCHRE, profile=0.5)
    person(P, 600, 536, 230, sit=True, coat=BLUE_COAT, profile=-0.5)
    lantern(P, 540, 300, 1.0)
    rain(P, 0, 1080, 0, 560, n=90, seed=2)
    return fin(P, 6602)


def n08a2():
    P = Paint(6611)
    room_bg(P, (14, 28, 38))
    floor(P, 560, (46, 36, 28))
    window_frame(P, 700, 80, 960, 340, sky_top=(16, 30, 52), sky_bot=(40, 60, 84), stars=6, seed=2)
    table(P, 120, 560, 450)
    cup(P, 300, 444, steam=False)
    chair(P, 400, 600, 310)
    person(P, 400, 590, 295, sit=True, profile=0.4)
    P.layer(rect(80, 140, 100, 400), (84, 60, 40), op=0.98, wob=1)
    ochre_coat_folded(P, 260, 436, w=90)
    return fin(P, 6612)


def n08a3():
    P = Paint(6621)
    backdrop(P, "storm", 200, seed=6621, clouds=3)
    P.layer(poly([(-5, 640), (-5, 520), (1085, 340), (1085, 640)]), (110, 100, 84), op=0.98, wob=3, rim=0.25)
    boulder(P, 620, 420, 130, 100)
    person(P, 470, 480, 210, coat=OCHRE, profile=0.7)
    return fin(P, 6622)


def n08a4():
    P = Paint(6631)
    room_bg(P, (20, 42, 54))
    floor(P, 540, (60, 44, 34))
    window_frame(P, 100, 70, 380, 330, stars=30, seed=5)
    moon(P, 240, 190, 24)
    bed(P, 540, 1060, 480)
    P.layer(rect(430, 420, 520, 540), (120, 82, 48), op=0.98, wob=1.5, rim=0.3)
    cup(P, 475, 414, steam=True)
    lamp(P, 880, 440, h=130)
    P.layer(rect(660, 360, 760, 400), (240, 232, 215), op=0.98, wob=1.5, rim=0.3)
    P.layer(rect(660, 400, 760, 408), (210, 196, 160), op=0.9, wob=1)
    phone(P, 600, 440, w=70, lit=True)
    return fin(P, 6632)


def n08a5():
    P = Paint(6641)
    room_bg(P, (20, 40, 52))
    floor(P, 560, (58, 42, 32))
    window_frame(P, 60, 80, 330, 330, stars=26, seed=7)
    bed(P, 400, 1040, 470)
    person(P, 560, 470, 250, sit=True, profile=0.5)
    phone(P, 640, 400, w=100, lit=True, tilt=3)
    lamp(P, 980, 440, h=120)
    return fin(P, 6642)


def n08a6():
    P = Paint(6651)
    backdrop(P, "night", 220, moonp=(150, 100, 22), seed=6651)
    stone_wall(P, 280, SH + 5, seed=51, base=(84, 80, 72))
    stone_stairs(P, 380, 700, 470, 640, steps=4)
    door(P, 460, 290, 620, 470, lit=True, ajar=0.3)
    lantern(P, 760, 360, 1.1)
    lit_window(P, 820, 330, 930, 440, silhouette=True)
    person(P, 540, 640, 200, coat=OCHRE, profile=0.0)
    return fin(P, 6652)


def n08a7():
    P = Paint(6661)
    backdrop(P, "dusk", 280, sunp=(540, 270, 34), seed=6661, clouds=2)
    stone_wall(P, 470, SH + 5, seed=53, base=(96, 90, 80))
    bench(P, 540, 580, w=300)
    person(P, 480, 576, 240, sit=True, coat=OCHRE, profile=0.0)
    person(P, 610, 576, 230, sit=True, coat=SAGE_COAT, profile=0.0)
    cup(P, 400, 500, steam=True)
    cup(P, 690, 500, steam=True)
    gulls(P, [(220, 120, 1.0), (860, 150, 0.8)])
    return fin(P, 6662)


# ============================================================ imagens únicas B (cenas distintas)
def n02b():
    """Foucault: cuidar de si: ele rega vasos na varanda, manhã."""
    P = Paint(6701)
    backdrop(P, "dawn", 260, sunp=(240, 240, 30), seed=6701, clouds=2)
    P.layer(rect(-5, 430, SW + 5, SH + 5), (140, 104, 70), op=0.98, wob=3, rim=0.2)
    P.layer(rect(-5, 420, SW + 5, 440), (176, 146, 106), op=0.98, wob=2, rim=0.3)
    for k, x in enumerate([560, 700, 840, 980]):
        pot_plant(P, x, 420, 1.2, seed=k + 2)
    hydrangea(P, 130, 380, r=70)
    person(P, 400, 600, 270, coat=OCHRE, profile=0.7)
    return fin(P, 6702)


def n03b():
    """Marcel: disponibilidade: porta aberta, luz acesa, cadeira e xícara à espera."""
    P = Paint(6711)
    backdrop(P, "night", 220, moonp=(880, 100, 22), seed=6711)
    stone_wall(P, 260, SH + 5, seed=61, base=(86, 80, 72))
    door(P, 380, 300, 560, 560, lit=True, ajar=0.35)
    lantern(P, 680, 400, 1.2)
    chair(P, 780, 590, 300)
    cup(P, 780, 418, steam=True)
    P.layer(rect(730, 420, 830, 436), (120, 82, 48), op=0.98, wob=1.2, rim=0.3)
    P.layer(rect(752, 436, 764, 520), (120, 82, 48), op=0.98, wob=1)
    P.layer(rect(796, 436, 808, 520), (120, 82, 48), op=0.98, wob=1)
    return fin(P, 6712)


def n04b():
    """Nishida: o pôr do sol inteiro; ele pequeno numa rocha."""
    P = Paint(6721)
    backdrop(P, "dusk", 360, sunp=(540, 340, 56), seed=6721, clouds=3)
    P.layer(poly([(-5, 640), (-5, 560), (300, 520), (700, 540), (1085, 500), (1085, 640)]), (22, 36, 44), op=1.0, wob=3, rim=0.3)
    person(P, 520, 540, 100, sit=True, coat=OCHRE, profile=0.0)
    return fin(P, 6722)


def n05b():
    """Nussbaum: o frágil: broto nascendo na fresta da pedra, luz da manhã."""
    P = Paint(6731)
    backdrop(P, "dawn", 200, sunp=(820, 180, 30), seed=6731, clouds=2)
    P.layer(rect(-5, 430, SW + 5, SH + 5), (96, 90, 80), op=0.98, wob=3, rim=0.3, vary=0.2)
    boulder(P, 300, 470, 150, 60, col=(110, 104, 94))
    boulder(P, 800, 480, 170, 66, col=(104, 98, 90))
    P.glow(540, 330, 260, WARM, 0.5)
    sapling(P, 540, 470, 250, leaf=(90, 160, 100))
    P.layer(ell(540, 474, 60, 14), (60, 50, 40), op=0.9, wob=2, rim=0.2)
    return fin(P, 6732)


def n06b():
    """Hadot: praticar aos poucos: ele sobe uma escadaria de pedra, degrau a degrau, com lanterna."""
    P = Paint(6741)
    backdrop(P, "dawn", 200, sunp=(860, 190, 28), seed=6741, clouds=2)
    hill_houses(P, 0, 1080, 220, n=7, seed=14, body=(190, 172, 132))
    stone_stairs(P, 260, 820, 280, 640, steps=10)
    person(P, 520, 450, 150, coat=OCHRE, profile=0.0)
    lantern(P, 900, 420, 1.0)
    return fin(P, 6742)


def n07b():
    """Shantideva: deixar o peso no banco: mala no chão, ele sentado no mar ao fim do dia."""
    P = Paint(6751)
    backdrop(P, "dusk", 280, sunp=(760, 260, 30), seed=6751, clouds=3)
    P.layer(rect(-5, 400, SW + 5, SH + 5), (62, 98, 76), op=0.98, wob=3, rim=0.15)
    stone_wall(P, 480, SH + 5, seed=81, base=(92, 86, 76))
    bench(P, 440, 580, w=260)
    person(P, 440, 576, 250, sit=True, coat=OCHRE, profile=0.5)
    suitcase(P, 250, 590, 1.0)
    return fin(P, 6752)


def n08b():
    """Hegel: ser visto: ele com lanterna numa ponta, janela acesa com silhueta do outro lado da baía."""
    P = Paint(6761)
    backdrop(P, "night", 300, moonp=(540, 100, 24), seed=6761)
    cliff(P, "left", top=380, seed=91, col=(14, 36, 46), reach=420)
    cliff(P, "right", top=400, seed=92, col=(14, 36, 46), reach=420)
    person(P, 180, 410, 200, coat=OCHRE, profile=0.6)
    lantern(P, 250, 360, 1.0)
    house(P, 840, 330, 110, 80, lit=True, seed=4)
    lit_window(P, 870, 350, 920, 400, silhouette=True)
    return fin(P, 6762)


SCENES = {n: f for n, f in globals().items() if n.startswith("n0") and callable(f)}
