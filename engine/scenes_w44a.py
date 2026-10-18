"""Cenas 19 e 20/10/2026: Pascal (silêncio), Agostinho, Laozi (água), William James."""
from lib3 import *


# ------------------------------------------------------------------ 19/10 A (Pascal)
def d19a1():
    """Capa: homem sentado de costas no quarto, celular virado para baixo na mesa, janela com lua."""
    P = Paint(1901)
    room_bg(P, (18, 44, 58))
    window_frame(P, 660, 80, 990, 400, stars=36, seed=3)
    moon(P, 830, 190, 26)
    floor(P, 548)
    table(P, 70, 520, 430)
    phone(P, 250, 414, w=120, lit=False, face_down=True)
    cup(P, 400, 432, steam=True)
    lamp(P, 150, 432, h=120)
    chair(P, 760, 590, 300)
    person(P, 760, 580, 300, sit=True, profile=0.3)
    return fin(P, 1902)


def d19a2():
    """Televisão acesa e celular iluminado: sofá, homem de costas."""
    P = Paint(1911)
    room_bg(P, (22, 40, 54))
    floor(P, 540, (60, 44, 34))
    P.layer(rect(330, 360, 750, 470), WOOD_D, op=0.98, wob=1.5, rim=0.3)
    tv(P, 360, 130, 720, 360)
    P.layer(rrect(220, 370, 860, 600, 50), (60, 100, 112), op=0.98, wob=2, rim=0.3)
    P.layer(rrect(190, 440, 300, 610, 30), (48, 84, 96), op=0.98, wob=2)
    P.layer(rrect(780, 440, 890, 610, 30), (48, 84, 96), op=0.98, wob=2)
    person(P, 540, 590, 300, sit=True)
    phone(P, 620, 505, w=76, lit=True, tilt=2)
    P.glow(540, 330, 420, (120, 170, 230), 0.16)
    lamp(P, 130, 500, h=140, g=0.4)
    return fin(P, 1912)


def d19a3():
    """O que ficou para depois: carta fechada, relógio tarde, xícara fria, cadeira vazia."""
    P = Paint(1921)
    room_bg(P, (20, 46, 60))
    floor(P, 556)
    clock_round(P, 300, 190, 78, hands=(0.12, 0.45))
    table(P, 420, 920, 400)
    letter(P, 560, 380, w=170, tilt=-0.04)
    cup(P, 760, 402, steam=False, col=(214, 200, 168))
    candle(P, 860, 402, h=40)
    chair(P, 250, 580, 310)
    window_frame(P, 700, 60, 960, 250, stars=18, seed=9, cross=False)
    P.glow(560, 340, 280, WARM, 0.18)
    return fin(P, 1922)


def d19a4():
    """Quarto pequeno: homem sentado na beira da cama, candeeiro, janela com mar e lua."""
    P = Paint(1931)
    room_bg(P, (16, 40, 54))
    window_frame(P, 560, 70, 930, 360, stars=30, seed=11, cross=False)
    moon(P, 760, 160, 22)
    P.layer(rect(560, 300, 930, 360), (22, 62, 76), op=0.98, wob=1)
    moon_reflection(P, 760, 300, 360, n=8, seed=3)
    floor(P, 520, (70, 48, 32))
    P.layer(rrect(60, 380, 560, 540, 20), (110, 76, 48), op=0.98, wob=2, rim=0.3)
    P.layer(rrect(60, 340, 540, 430, 26), OCHRE, op=0.96, wob=2, rim=0.3)
    P.layer(rrect(70, 350, 220, 410, 20), (240, 226, 190), op=0.95, wob=1.5)
    table(P, 940, 1060, 410, legs=True)
    candle(P, 1000, 412, h=50)
    person(P, 400, 520, 300, sit=True, profile=0.35)
    return fin(P, 1932)


def d19a5():
    """Manhã: homem sentado perto da janela, xícara no peitoril; ao fundo, o celular esquecido na outra sala."""
    P = Paint(1941)
    room_bg(P, (60, 96, 110))
    backdrop(P, "dawn", 300, sunp=(540, 296, 30), seed=1941, island=(660, 340), sea_bottom=SH + 5)
    P.layer(rect(-5, 0, 240, SH + 5), (96, 70, 46), op=1.0, wob=2, rim=0.2)
    P.layer(rect(840, 0, SW + 5, SH + 5), (96, 70, 46), op=1.0, wob=2, rim=0.2)
    P.layer(rect(-5, 520, SW + 5, SH + 5), (130, 92, 58), op=1.0, wob=2, rim=0.2)
    P.layer(rect(150, 380, 930, 410), (150, 108, 66), op=0.98, wob=1.5, rim=0.3)
    cup(P, 380, 380, steam=True)
    pot_plant(P, 760, 380, 1.0, seed=2)
    chair(P, 560, 600, 320)
    person(P, 560, 590, 320, sit=True, profile=-0.3)
    table(P, 30, 200, 520, legs=False)
    phone(P, 110, 506, w=70, lit=False, face_down=True)
    return fin(P, 1942)


def d19a6():
    """Varanda ao entardecer: dois amigos de costas conversando diante do mar."""
    P = Paint(1951)
    backdrop(P, "dusk", 300, sunp=(700, 296, 34), seed=1951, clouds=2, island=(120, 380))
    stone_wall(P, 470, SH + 5, seed=14, base=(120, 108, 90))
    person(P, 400, 470, 250, coat=OCHRE, profile=0.2)
    person(P, 560, 470, 238, coat=(70, 112, 128), hair=(70, 48, 36), profile=-0.2)
    cup(P, 700, 462, steam=True)
    cup(P, 790, 462, steam=True, col=(226, 200, 150))
    pot_plant(P, 940, 470, 1.1, seed=4)
    return fin(P, 1952)


def d19a7():
    """Cais à noite: homem sentado na ponta do cais, barcos amarrados, lua."""
    P = Paint(1961)
    backdrop(P, "night", 280, moonp=(860, 120, 26), seed=1961)
    boat(P, 230, 400, 1.0, lit=True)
    boat(P, 560, 360, 0.7, lit=False)
    P.layer(rect(-5, 470, SW + 5, 520), (86, 80, 72), op=1.0, wob=1.5, rim=0.3)
    P.layer(rect(-5, 520, SW + 5, SH + 5), (38, 36, 36), op=1.0, wob=1.5, rim=0.2)
    for x in (140, 420, 700, 980):
        P.layer(rect(x - 8, 440, x + 8, 480), (60, 48, 40), op=0.98, wob=1)
    bench(P, 700, 560, w=240)
    person(P, 700, 552, 250, sit=True, profile=0.3)
    lantern(P, 940, 440, 1.0)
    gulls(P, [(300, 100, 1.0), (380, 130, 0.8)], col=(120, 140, 150))
    return fin(P, 1962)


def d19b():
    """Agostinho: mesa com xícara fumegante, relógio e janela do amanhecer."""
    P = Paint(1971)
    room_bg(P, (30, 62, 74))
    window_frame(P, 640, 70, 1000, 380, sky_top=(58, 108, 128), sky_bot=(246, 212, 156), cross=True)
    P.glow(820, 330, 200, WARM, 0.5)
    floor(P, 540, (96, 70, 46))
    clock_round(P, 300, 200, 84, hands=(0.1, 0.36))
    table(P, 120, 620, 430)
    cup(P, 360, 432, steam=True)
    book(P, 200, 428, w=140)
    pot_plant(P, 540, 432, 0.9, kind="sprout")
    return fin(P, 1972)


# ------------------------------------------------------------------ 20/10 A (Laozi)
def d20a1():
    """Capa: água descendo em cascata por encosta verde, rochas e samambaias."""
    P = Paint(2001)
    P.vgrad(-5, 300, (96, 150, 168), (226, 226, 200), mask=rect(-5, -5, SW + 5, 300), wob=2, rim=0, vary=0.08)
    P.layer(poly(ridge(180, 90, 21, x0=-30, x1=SW + 30)), (44, 84, 80), op=1.0, wob=3)
    P.layer(poly(ridge(300, 70, 22, x0=-30, x1=SW + 30)), (30, 70, 66), op=1.0, wob=3)
    P.layer(rect(-5, 330, SW + 5, SH + 5), (26, 62, 58), op=1.0, wob=2, rim=0.1)
    waterfall(P, 540, 200, 520, 40, 220)
    P.layer(ell(540, 540, 250, 50), (60, 140, 150), op=0.95, wob=3, rim=0.2, soft=2)
    foam(P, 360, 720, 520, n=40, seed=3)
    for x, y, rx in [(250, 560, 80), (360, 590, 60), (780, 570, 90), (900, 540, 60)]:
        P.layer(ell(x, y, rx, rx * 0.5), (64, 66, 66), op=0.98, wob=2, rim=0.3)
    fern(P, 150, 470, n=9, size=130)
    fern(P, 950, 470, n=9, size=130)
    gulls(P, [(840, 90, 0.9)], col=(90, 110, 120))
    return fin(P, 2002)


def d20a2():
    """Dia que aperta: mesa com pilha de papéis, relógio e telefone aceso, entardecer na janela."""
    P = Paint(2011)
    room_bg(P, (30, 54, 66))
    window_frame(P, 90, 70, 480, 380, sky_top=(24, 48, 92), sky_bot=(226, 152, 98), cross=True)
    floor(P, 560, (72, 56, 42))
    table(P, 480, 1040, 420)
    stack_papers(P, 640, 418, n=6, w=150)
    stack_papers(P, 870, 418, n=4, w=130)
    phone(P, 760, 410, w=96, lit=True, tilt=3)
    clock_round(P, 760, 190, 80, hands=(0.9, 0.05))
    cup(P, 980, 420, steam=True)
    lamp(P, 520, 420, h=120, g=0.5)
    return fin(P, 2012)


def d20a3():
    """Endurecer: grande muro de pedra fechado, homem pequeno diante dele, entardecer frio."""
    P = Paint(2021)
    P.vgrad(-5, 260, (36, 56, 80), (150, 140, 140), mask=rect(-5, -5, SW + 5, 260), wob=2, rim=0, vary=0.08)
    stone_wall(P, 200, SH + 5, seed=31, base=(76, 76, 78), cap=True)
    P.layer(rect(430, 260, 650, 560), (46, 40, 40), op=0.98, wob=1.5, rim=0.3)
    P.layer(poly([(430, 260), (540, 190), (650, 260)]), (46, 40, 40), op=0.98, wob=1.5, rim=0.3)
    P.layer(rect(520, 380, 530, 420), (120, 100, 70), op=0.95, wob=0.6)
    P.layer(rect(-5, 560, SW + 5, SH + 5), (56, 56, 54), op=1.0, wob=2, rim=0.2)
    person(P, 300, 600, 220, coat=OCHRE)
    P.glow(540, 420, 260, (140, 150, 170), 0.18)
    return fin(P, 2022)


def d20a4():
    """A água contorna a pedra: rio com grande rocha, espuma e margens verdes."""
    P = Paint(2031)
    P.vgrad(-5, 210, (92, 148, 172), (232, 226, 200), mask=rect(-5, -5, SW + 5, 210), wob=2, rim=0, vary=0.07)
    P.layer(poly(ridge(170, 60, 33, x0=-30, x1=SW + 30)), (40, 84, 80), op=1.0, wob=3)
    P.layer(rect(-5, 250, SW + 5, SH + 5), (52, 130, 142), op=1.0, wob=2, rim=0.1)
    P.strokes(0, SW, 260, SH, 90, (200, 232, 236), op=0.35, wmin=60, wmax=220, seed=5)
    P.strokes(0, SW, 260, SH, 50, (24, 84, 96), op=0.3, wmin=60, wmax=200, seed=6)
    P.layer(poly([(380, 520), (440, 330), (560, 280), (700, 330), (760, 520)]), (70, 72, 74), op=0.99, wob=3, rim=0.3, vary=0.2)
    P.layer(poly([(440, 330), (560, 280), (640, 310), (520, 360)]), (118, 118, 112), op=0.8, wob=2, rim=0.1)
    foam(P, 330, 480, 510, n=18, seed=7)
    foam(P, 660, 820, 510, n=18, seed=8)
    P.layer(rect(-5, 560, 220, SH + 5), (40, 84, 70), op=1.0, wob=3, rim=0.2)
    P.layer(rect(870, 560, SW + 5, SH + 5), (40, 84, 70), op=1.0, wob=3, rim=0.2)
    fern(P, 100, 560, n=8, size=110)
    return fin(P, 2032)


def d20a5():
    """Respirar: homem de costas na varanda ao amanhecer, mar calmo."""
    P = Paint(2041)
    backdrop(P, "dawn", 330, sunp=(560, 326, 36), seed=2041, clouds=2)
    P.layer(poly(ridge(380, 30, 41, x0=-30, x1=SW + 30)), (40, 84, 92), op=0.95, wob=3)
    P.layer(rect(-5, 520, SW + 5, SH + 5), (140, 120, 92), op=1.0, wob=2, rim=0.2)
    P.layer(rect(-5, 500, SW + 5, 530), STONEL, op=1.0, wob=1.5, rim=0.3)
    person(P, 540, 560, 280, coat=OCHRE)
    pot_plant(P, 130, 530, 1.2, seed=7)
    pot_plant(P, 940, 530, 1.0, seed=8)
    return fin(P, 2042)


def d20a6():
    """Conversa calma: dois à mesa, de perfil, luz quente e chá."""
    P = Paint(2051)
    room_bg(P, (22, 48, 62))
    window_frame(P, 380, 60, 700, 300, sky_top=(24, 48, 92), sky_bot=(226, 152, 98), cross=False)
    floor(P, 560, (80, 58, 40))
    table(P, 280, 800, 420)
    cup(P, 440, 424, steam=True)
    cup(P, 640, 424, steam=True, col=(226, 200, 150))
    candle(P, 540, 424, h=40)
    chair(P, 210, 590, 320)
    chair(P, 870, 590, 320)
    person(P, 215, 580, 300, sit=True, profile=0.9)
    person(P, 865, 580, 290, sit=True, profile=-0.9, coat=(70, 112, 128), hair=(70, 48, 36))
    return fin(P, 2052)


def d20a7():
    """Mar subindo e descendo sobre rocha lisa, tarde dourada."""
    P = Paint(2061)
    backdrop(P, "dusk", 250, sunp=(780, 246, 40), seed=2061, clouds=2)
    P.layer(rect(-5, 330, SW + 5, SH + 5), (42, 96, 108), op=1.0, wob=2, rim=0.1)
    foam(P, 0, SW, 400, n=60, seed=9)
    foam(P, 0, SW, 470, n=40, seed=10)
    P.layer(poly([(-5, 640), (-5, 420), (200, 400), (420, 470), (500, 560), (520, 640)]), (44, 42, 44), op=0.99, wob=3, rim=0.3, vary=0.2)
    P.layer(poly([(520, 640), (620, 540), (840, 500), (1085, 520), (1085, 640)]), (52, 48, 48), op=0.99, wob=3, rim=0.3, vary=0.2)
    rock_pool(P, 230, 470, 90, 22)
    rock_pool(P, 820, 560, 130, 26)
    foam(P, 480, 620, 560, n=16, seed=3)
    gulls(P, [(220, 120, 1.0), (300, 90, 0.8)], col=(90, 100, 110))
    return fin(P, 2062)


def d20b():
    """William James: peitoril com hortênsia, xícara e luz da manhã; mar na janela."""
    P = Paint(2071)
    room_bg(P, (36, 70, 82))
    window_frame(P, 230, 70, 850, 410, sky_top=(92, 148, 172), sky_bot=(232, 226, 200), cross=True)
    P.layer(rect(230, 300, 850, 410), (50, 116, 132), op=0.98, wob=1)
    P.glow(540, 200, 300, WARM, 0.35)
    P.layer(rect(160, 410, 920, 440), (150, 108, 66), op=0.98, wob=1.5, rim=0.3)
    hydrangea(P, 330, 380, 50, col=(92, 132, 214), seed=5)
    cup(P, 560, 410, steam=True)
    book(P, 740, 408, w=130)
    floor(P, 560, (110, 80, 52))
    return fin(P, 2072)


SCENES = {n: f for n, f in globals().items() if (n.startswith("d19") or n.startswith("d20")) and callable(f)}
