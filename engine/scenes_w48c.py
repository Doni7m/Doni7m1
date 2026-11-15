"""Cenas das imagens únicas (B) de 16-22/11/2026."""
import re
from lib4 import *

NIGHT_ROOM = (22, 44, 56)


# 16/11 Patočka: cuidar da alma (chama protegida)
def r16b():
    P = Paint(8801)
    room_bg(P, NIGHT_ROOM)
    floor(P, 570, (62, 44, 34))
    window_frame(P, 120, 70, 420, 330, sky_top=NAVY, sky_bot=(30, 82, 96), stars=30, seed=6)
    table(P, 300, 900, 470)
    candle(P, 600, 466, h=90)
    P.glow(600, 390, 230, WARM, 0.6)
    book(P, 420, 460, w=170)
    cup(P, 780, 462, steam=True)
    return fin(P, 8802)


# 17/11 Musônio Rufo: prática (plantar, repetir)
def r17b():
    P = Paint(8811)
    backdrop(P, "day", 240, seed=8811, clouds=2)
    terrace(P, 290, 350, (84, 130, 86), seed=6)
    terrace(P, 400, 240, (70, 116, 80), seed=7)
    P.layer(rect(-5, 500, SW + 5, SH + 5), (130, 96, 64), op=0.98, wob=3, rim=0.2, vary=0.2)
    sapling(P, 760, 560, 100)
    sapling(P, 860, 570, 80)
    sapling(P, 960, 580, 60)
    person(P, 460, 600, 250, coat=OCHRE, profile=0.6)
    return fin(P, 8812)


# 18/11 Leibniz: som do mar, ondas
def r18b():
    P = Paint(8821)
    backdrop(P, "day", 230, seed=8821, clouds=2)
    foam(P, 0, SW, 300, n=30, seed=3)
    foam(P, 0, SW, 380, n=36, seed=4)
    foam(P, 0, SW, 460, n=40, seed=5)
    foam(P, 0, SW, 540, n=44, seed=6)
    P.layer(poly(ridge(560, 20, 9, x0=-20, x1=SW + 20, step=40) + [(SW + 20, SH + 20), (-20, SH + 20)]), (110, 98, 84), op=0.98, wob=3, rim=0.3)
    person(P, 300, 590, 200, coat=OCHRE, profile=0.6)
    gulls(P, [(700, 120, 1.0), (800, 160, 0.8), (880, 110, 0.7)])
    return fin(P, 8822)


# 19/11 Xunzi: passos acumulados
def r19b():
    P = Paint(8831)
    backdrop(P, "dawn", 260, sunp=(800, 250, 34), seed=8831, clouds=2)
    terrace(P, 300, 340, (84, 130, 86), seed=8)
    stone_stairs(P, 280, 800, 260, 630, steps=10)
    person(P, 540, 450, 170, coat=OCHRE, profile=0.3)
    gulls(P, [(200, 130, 1.0)])
    return fin(P, 8832)


# 20/11 Watsuji: o lugar nos molda (ilha, vento)
def r20b():
    P = Paint(8841)
    backdrop(P, "day", 250, seed=8841, clouds=3)
    hill_houses(P, -10, SW + 10, 270, n=9, seed=111, lit=False, body=(200, 186, 150))
    banana_leaf(P, 110, 620, -0.5, 300, 70)
    banana_leaf(P, 980, 620, 0.55, 280, 66)
    P.layer(rect(-5, 560, SW + 5, SH + 5), (150, 118, 84), op=0.98, wob=3, rim=0.2, vary=0.18)
    person(P, 540, 620, 230, coat=OCHRE, profile=0.5)
    gulls(P, [(300, 140, 1.0), (420, 100, 0.8)])
    return fin(P, 8842)


# 21/11 Jankélévitch: o que foi vivido permanece (casa acesa, lembrança)
def r21b():
    P = Paint(8851)
    backdrop(P, "dusk", 280, sunp=(780, 270, 34), seed=8851, clouds=2)
    P.layer(rect(-5, 500, SW + 5, SH + 5), (92, 84, 74), op=0.98, wob=3, rim=0.2)
    facade(P, 90, 400, 330, 560)
    lit_window(P, 160, 390, 250, 480, silhouette=True)
    lit_window(P, 270, 390, 340, 480)
    bench(P, 640, 600, 300)
    ochre_coat_folded(P, 640, 560, 110)
    string_lights(P, 420, 1000, 330, sag=40, n=9)
    return fin(P, 8852)


# 22/11 Mbiti: ser esperado
def r22b():
    P = Paint(8861)
    room_bg(P, (14, 36, 46))
    stone_wall(P, 130, 560, seed=6, base=(60, 62, 62))
    cobbles(P, 540, glow_x=620)
    door(P, 560, 180, 700, 552, lit=True, ajar=0.3)
    person(P, 640, 530, 160, coat=RUST_COAT, profile=0.0)
    person(P, 300, 610, 270, coat=OCHRE, profile=0.6)
    lantern(P, 820, 360, 1.1)
    return fin(P, 8862)


SCENES = {n: f for n, f in globals().items() if re.match(r"^r\d\d", n) and callable(f)}
