"""Cenas do carrossel 'Casa e pertencimento' (Bachelard), 16/10/2026."""
from lib2 import *


def fin(P, seed):
    return P.finish(top=30, bottom=34, left=45, right=45, feather=70, seed=seed)


def c1():
    """Capa: encosta com muitas janelas acesas sobre o mar noturno."""
    P = Paint(701)
    backdrop(P, "night", 300, moonp=(840, 110, 28), seed=701)
    P.layer(poly(ridge(330, 70, 71, x0=-30, x1=SW + 30)), (14, 40, 52), op=1.0, wob=3)
    hill_houses(P, -10, SW + 10, 330, n=9, seed=72, lit=True)
    hill_houses(P, -10, SW + 10, 430, n=8, seed=73, lit=True, body=(132, 146, 144))
    P.layer(rect(-5, 560, SW + 5, SH + 5), (16, 44, 54), op=1.0, wob=2, rim=0.1)
    string_lights(P, 120, 960, 540, sag=26, n=12)
    gulls(P, [(220, 110, 1.0), (300, 140, 0.8)], col=(120, 140, 150))
    return fin(P, 702)


def c2():
    """Entrada: porta acesa entreaberta, sobretudo ocre no cabide, sapatos no tapete."""
    P = Paint(711)
    room_bg(P, (20, 50, 62))
    P.layer(rect(-5, 560, SW + 5, SH + 5), (70, 48, 32), op=1.0, wob=2, rim=0.2)
    door(P, 420, 120, 700, 570, lit=True, ajar=0.3)
    # cabide e sobretudo
    P.layer(rect(120, 150, 300, 164), WOOD_X, op=0.98, wob=1.2)
    for x in (150, 210, 270):
        P.layer(ell(x, 168, 6, 6), (200, 160, 80), op=0.95, wob=0.5)
    P.layer(poly([(170, 170), (250, 170), (268, 400), (150, 400)]), OCHRE, op=0.98, wob=2, rim=0.3)
    P.layer(poly([(170, 170), (210, 190), (250, 170), (240, 200), (210, 230), (180, 200)]), (222, 164, 70), op=0.9, wob=1.5)
    # tapete e sapatos
    P.layer(rect(380, 560, 760, 620), (150, 60, 48), op=0.97, wob=1.5, rim=0.3)
    P.layer(ell(480, 590, 46, 16), (30, 24, 26), op=0.97, wob=1)
    P.layer(ell(570, 596, 46, 16), (30, 24, 26), op=0.97, wob=1)
    # mesinha com chaves e vaso
    table(P, 780, 1020, 440, legs=True, ybot=SH + 5)
    P.layer(ell(850, 436, 24, 6), GOLD, op=0.95, wob=0.6)
    P.line([(850, 436), (880, 424)], w=3, alpha=0.8, color=(120, 90, 40))
    pot_plant(P, 950, 438, 1.0, seed=4)
    P.glow(560, 430, 340, WARM, 0.35)
    return fin(P, 712)


def c3():
    """Casa nova ainda vazia: malas, caixas, lâmpada nua, janela escura."""
    P = Paint(721)
    room_bg(P, (22, 46, 58))
    P.layer(rect(-5, 520, SW + 5, SH + 5), (92, 74, 56), op=1.0, wob=2, rim=0.2)
    window_frame(P, 700, 90, 940, 390, stars=24, seed=7)
    suitcase(P, 250, 560, 1.4)
    suitcase(P, 440, 566, 1.0, col=(86, 96, 100))
    for (x, y, w, h) in [(560, 580, 150, 110), (640, 470, 130, 100), (800, 590, 160, 120)]:
        P.layer(rect(x - w / 2, y - h, x + w / 2, y), (178, 138, 88), op=0.98, wob=1.5, rim=0.3)
        P.layer(rect(x - w / 2, y - h, x + w / 2, y - h + 14), (150, 112, 68), op=0.98, wob=1)
        P.layer(rect(x - 6, y - h, x + 6, y), (214, 192, 150), op=0.8, wob=0.8)
    # lâmpada nua pendurada
    P.line([(300, -5), (300, 150)], w=3, alpha=0.8, color=(40, 30, 24))
    P.layer(ell(300, 170, 14, 20), (255, 236, 160), op=0.98, wob=0.6)
    P.glow(300, 170, 160, WARM, 0.55)
    ochre_coat_folded(P, 440, 458, w=130)
    return fin(P, 722)


def c4():
    """O devaneio: homem de costas à janela, luz de candeeiro, mar e lua."""
    P = Paint(731)
    room_bg(P, (18, 44, 58))
    window_frame(P, 330, 70, 820, 440, stars=40, seed=11, cross=False)
    P.layer(rect(330, 396, 820, 440), (22, 62, 76), op=0.98, wob=1)
    moon(P, 640, 170, 30)
    moon_reflection(P, 640, 330, 440, n=14, seed=5)
    P.layer(rect(-5, 560, SW + 5, SH + 5), (70, 48, 32), op=1.0, wob=2, rim=0.2)
    chair(P, 575, 600, 330)
    person(P, 575, 590, 330, sit=True, profile=0.3)
    lamp(P, 930, 570, h=170)
    book(P, 120, 560, w=170)
    cup(P, 240, 560, steam=True)
    P.glow(575, 360, 360, WARM, 0.18)
    return fin(P, 732)


def c5():
    """Canto de leitura: poltrona, manta, xícara fumegante, pequena estante e vaso."""
    P = Paint(741)
    room_bg(P, (24, 52, 62))
    P.layer(rect(-5, 570, SW + 5, SH + 5), (86, 60, 40), op=1.0, wob=2, rim=0.2)
    # estante
    P.layer(rect(70, 90, 330, 480), WOOD_D, op=0.98, wob=1.5, rim=0.3)
    r = np.random.default_rng(8)
    for k in range(3):
        y = 150 + k * 110
        P.layer(rect(70, y, 330, y + 8), WOOD_X, op=0.98, wob=1)
        x = 84
        while x < 316:
            w = r.uniform(16, 32)
            h = r.uniform(50, 84)
            P.layer(rect(x, y - h, x + w, y), tuple(int(v * r.uniform(0.8, 1.1)) for v in [(150, 60, 48), (60, 100, 120), (196, 138, 52), (226, 210, 170)][int(r.integers(0, 4))]), op=0.95, wob=0.8)
            x += w + 3
    # poltrona
    P.layer(rrect(480, 330, 780, 580, 40), (60, 100, 112), op=0.98, wob=2, rim=0.3)
    P.layer(rrect(440, 420, 520, 580, 26), (48, 84, 96), op=0.98, wob=2)
    P.layer(rrect(740, 420, 820, 580, 26), (48, 84, 96), op=0.98, wob=2)
    P.layer(rrect(500, 470, 760, 580, 20), (74, 118, 130), op=0.98, wob=2)
    P.layer(poly([(520, 470), (760, 470), (790, 560), (500, 560)]), OCHRE, op=0.95, wob=2, rim=0.3)
    for i in range(4):
        P.line([(530 + i * 60, 480), (520 + i * 64, 556)], w=2, alpha=0.4, color=(120, 80, 30))
    # mesinha e xícara
    P.layer(rect(870, 480, 1010, 494), WOOD_T, op=0.98, wob=1.2)
    P.layer(rect(930, 494, 944, 580), WOOD_D, op=0.98, wob=1)
    cup(P, 940, 480, steam=True)
    candle(P, 985, 480, h=30)
    pot_plant(P, 410, 586, 0.9, seed=9)
    P.glow(640, 380, 300, WARM, 0.25)
    return fin(P, 742)


def c6():
    """Viela de pedra com lanternas, banco com duas xícaras e vizinha à porta."""
    P = Paint(751)
    backdrop(P, "dusk", 220, sunp=(260, 216, 30), seed=751, clouds=2)
    P.layer(rect(-5, 250, SW + 5, SH + 5), (52, 56, 60), op=1.0, wob=2, rim=0.2)
    cobbles(P, 440, SH + 5, seed=12, glow_x=600)
    # casas dos lados
    P.layer(rect(-5, 120, 260, 470), (178, 160, 124), op=0.98, wob=2, rim=0.3, vary=0.12)
    P.layer(poly([(-5, 120), (130, 60), (270, 120)]), (150, 70, 52), op=0.98, wob=2, rim=0.3)
    door(P, 90, 270, 190, 470, lit=True, ajar=0.0)
    P.layer(rect(820, 100, 1085, 470), (190, 170, 130), op=0.98, wob=2, rim=0.3, vary=0.12)
    P.layer(poly([(800, 100), (950, 40), (1090, 100)]), (150, 70, 52), op=0.98, wob=2, rim=0.3)
    P.layer(rect(880, 220, 960, 330), (255, 214, 130), op=0.98, wob=1.2, rim=0.3)
    P.glow(920, 275, 130, WARM, 0.7)
    for x in (906, 934):
        P.layer(rect(x, 220, x + 4, 330), (110, 78, 50), op=0.95, wob=0.6)
    # escada ao fundo
    stone_stairs(P, 380, 700, 250, 440, steps=6)
    lantern(P, 330, 300, 1.1)
    lantern(P, 760, 300, 1.1)
    string_lights(P, 190, 820, 140, sag=34, n=9)
    # banco e xícaras
    bench(P, 560, 560, w=260)
    cup(P, 500, 530, steam=True)
    cup(P, 600, 530, steam=True, col=(226, 200, 150))
    person(P, 140, 470, 190, coat=(70, 112, 128), hair=(66, 46, 36), profile=-0.3)
    return fin(P, 752)


def c7():
    """Fecho: homem de costas chegando à porta acesa de uma casa baixa, mar ao fundo."""
    P = Paint(761)
    backdrop(P, "night", 260, moonp=(180, 120, 24), seed=761)
    P.layer(poly(ridge(300, 40, 77, x0=-30, x1=SW + 30)), (16, 44, 56), op=1.0, wob=3)
    P.layer(rect(-5, 470, SW + 5, SH + 5), (36, 70, 70), op=1.0, wob=2, rim=0.1)
    # caminho de pedra
    P.layer(poly([(430, 640), (760, 640), (680, 470), (620, 470)]), (150, 126, 92), op=0.98, wob=3, rim=0.25)
    # casa
    P.layer(rect(560, 250, 980, 480), (200, 188, 156), op=0.98, wob=2, rim=0.3, vary=0.1)
    P.layer(poly([(530, 252), (770, 160), (1010, 252)]), (150, 70, 52), op=0.98, wob=2, rim=0.3)
    door(P, 700, 330, 790, 480, lit=True, ajar=0.0)
    P.layer(rect(600, 320, 660, 400), (255, 214, 130), op=0.98, wob=1.2, rim=0.3)
    P.layer(rect(840, 320, 920, 400), (255, 214, 130), op=0.98, wob=1.2, rim=0.3)
    P.glow(745, 420, 300, WARM, 0.5)
    hydrangea(P, 520, 470, 52, col=(92, 132, 214), seed=3)
    hydrangea(P, 1000, 480, 48, col=(150, 120, 196), seed=4)
    lantern(P, 662, 420, 0.8)
    person(P, 560, 640, 250)
    return fin(P, 762)


SCENES = {n: f for n, f in globals().items() if n.startswith("c") and n[1:].isdigit() and callable(f)}
