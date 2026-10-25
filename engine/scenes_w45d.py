"""Cenas 01/11/2026: Demócrito (medida e bom ânimo), Maimônides (ajudar a ficar de pé)."""
from lib3 import *


def balance(P, x, ybase, h, tilt=0.0, pan_load=(1, 1)):
    P.layer(rect(x - 10, ybase - h, x + 10, ybase), (96, 66, 40), op=0.98, wob=1.5, rim=0.3)
    P.layer(ell(x, ybase, 70, 14), (96, 66, 40), op=0.98, wob=1.5, rim=0.3)
    y0 = ybase - h
    L = (x - 200, y0 + 200 * tilt)
    R = (x + 200, y0 - 200 * tilt)
    P.layer(poly([(L[0], L[1] - 6), (R[0], R[1] - 6), (R[0], R[1] + 6), (L[0], L[1] + 6)]), (60, 44, 30), op=0.98, wob=1.2, rim=0.2)
    for (px, py), load in ((L, pan_load[0]), (R, pan_load[1])):
        P.line([(px, py), (px - 60, py + 110)], w=2, alpha=0.7)
        P.line([(px, py), (px + 60, py + 110)], w=2, alpha=0.7)
        P.layer(ell(px, py + 112, 70, 12), (186, 150, 70), op=0.98, wob=1.2, rim=0.3)
        for j in range(load):
            P.layer(ell(px - 28 + j * 28, py + 98, 16, 16), (212, 110, 70), op=0.98, wob=1, rim=0.3)


# ------------------------------------------------------------------ 01/11 A (Demócrito)
def e01a1():
    """Capa: mesa lotada: pratos, xícaras, celular, livros, velas, tudo amontoado; ele de costas."""
    P = Paint(4101)
    room_bg(P, (24, 46, 60))
    floor(P, 540, (66, 48, 36))
    table(P, 90, 990, 410)
    for k in range(9):
        cup(P, 160 + k * 92, 402 - (k % 2) * 8, steam=(k % 3 == 0), col=[(240, 226, 190), (226, 200, 150)][k % 2])
    stack_papers(P, 300, 392, n=6, w=130)
    book(P, 720, 396, w=140)
    phone(P, 880, 396, w=70, lit=True)
    candle(P, 600, 410, h=44)
    person(P, 540, 600, 290, coat=OCHRE, profile=0.0)
    return fin(P, 4102)


def e01a2():
    """Muito de tudo: TV, notebook, celular, caixas de compras; ele afundado no sofá."""
    P = Paint(4111)
    room_bg(P, (22, 40, 54))
    floor(P, 540, (60, 44, 34))
    tv(P, 360, 120, 720, 330)
    P.layer(rrect(220, 370, 860, 600, 50), (60, 100, 112), op=0.98, wob=2, rim=0.3)
    for k, (x, y, w, h) in enumerate([(100, 470, 120, 100), (200, 520, 100, 90), (900, 480, 110, 100), (820, 540, 120, 80)]):
        P.layer(rect(x, y, x + w, y + h), (176 - 14 * k, 138 - 8 * k, 90), op=0.98, wob=1.5, rim=0.3)
    person(P, 540, 590, 300, sit=True)
    phone(P, 620, 505, w=76, lit=True, tilt=2)
    P.glow(540, 330, 420, (120, 170, 230), 0.18)
    return fin(P, 4112)


def e01a3():
    """Ciclo: escada de pedra em espiral? Homem cansado sentado no chão encostado a um muro, mala e sacolas."""
    P = Paint(4121)
    backdrop(P, "dusk", 260, sunp=(860, 240, 28), seed=4121, clouds=2)
    stone_wall(P, 330, SH + 5, seed=91, base=(96, 88, 78))
    person(P, 420, 600, 240, coat=OCHRE, sit=True, profile=0.2)
    suitcase(P, 640, 580, 1.2)
    suitcase(P, 760, 590, 0.9, col=(60, 100, 120))
    return fin(P, 4122)


def e01a4():
    """Demócrito: balança em equilíbrio junto ao mar, frutas nos dois pratos."""
    P = Paint(4131)
    backdrop(P, "dawn", 300, sunp=(240, 270, 30), seed=4131, clouds=2)
    P.layer(rect(-5, 440, SW + 5, SH + 5), (176, 156, 112), op=0.97, wob=3, rim=0.2)
    balance(P, 600, 600, 330, tilt=0.0, pan_load=(2, 2))
    person(P, 220, 600, 230, coat=OCHRE, profile=0.5)
    return fin(P, 4132)


def e01a5():
    """A metade: mesa com um pão cortado ao meio, uma xícara pela metade, ele de costas, luz da manhã."""
    P = Paint(4141)
    room_bg(P, (24, 50, 62))
    floor(P, 540, (66, 48, 36))
    window_frame(P, 680, 70, 940, 320, sky_top=(150, 190, 204), sky_bot=(244, 230, 196), cross=True)
    table(P, 150, 640, 420)
    P.layer(ell(300, 414, 60, 18), (206, 156, 80), op=0.98, wob=1.5, rim=0.3)
    P.layer(ell(430, 414, 60, 18), (206, 156, 80), op=0.98, wob=1.5, rim=0.3)
    cup(P, 540, 410, steam=True)
    chair(P, 400, 590, 310)
    person(P, 400, 580, 300, sit=True, profile=0.25)
    P.glow(810, 280, 260, WARM, 0.3)
    return fin(P, 4142)


def e01a6():
    """Caminho calmo: trilha à beira do mar, ele caminha devagar, sol baixo."""
    P = Paint(4151)
    backdrop(P, "dusk", 250, sunp=(780, 230, 34), seed=4151, clouds=3)
    P.layer(rect(-5, 330, SW + 5, SH + 5), (70, 110, 84), op=0.97, wob=3, rim=0.15)
    P.layer(poly([(-5, 640), (200, 470), (860, 400), (1085, 440), (1085, 640)]), (170, 150, 110), op=0.97, wob=3, rim=0.2)
    fern(P, 120, 560, n=9, size=110)
    person(P, 520, 520, 190, coat=OCHRE, profile=0.5)
    return fin(P, 4152)


def e01a7():
    """Noite: janela com lua, lâmpada, xícara; ele de costas em casa, tranquilo."""
    P = Paint(4161)
    room_bg(P, (18, 40, 54))
    floor(P, 540, (60, 44, 32))
    window_frame(P, 640, 70, 960, 340, stars=36, seed=11)
    moon(P, 820, 190, 26)
    table(P, 90, 520, 430)
    cup(P, 300, 422, steam=True)
    book(P, 420, 420, w=130)
    lamp(P, 160, 450, h=130)
    chair(P, 760, 590, 300)
    person(P, 760, 580, 300, sit=True, profile=0.3)
    return fin(P, 4162)


def e01b():
    """Maimônides: escada encostada num muro, homem na base segura-a para outra pessoa subir; lanterna."""
    P = Paint(4171)
    backdrop(P, "dusk", 220, sunp=(880, 210, 30), seed=4171, clouds=2)
    stone_wall(P, 280, SH + 5, seed=92, base=(98, 90, 78))
    ladder(P, 520, 600, 300, w=90, lean=30)
    person(P, 340, 600, 240, coat=OCHRE, profile=0.5)
    person(P, 535, 340, 110, coat=(60, 100, 120), profile=0.0)
    lantern(P, 880, 400, 1.1)
    return fin(P, 4172)


SCENES = {n: f for n, f in globals().items() if n.startswith("e0") and callable(f)}
