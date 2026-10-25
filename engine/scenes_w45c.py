"""Cenas 30 e 31/10/2026: Mêncio (compaixão), Russell, Adam Smith (sentir junto), Dōgen."""
from lib3 import *


def well(P, x, y, s=1.0):
    P.layer(rect(x - 60 * s, y - 70 * s, x + 60 * s, y), (110, 100, 86), op=0.98, wob=2, rim=0.3, vary=0.18)
    P.layer(ell(x, y - 70 * s, 60 * s, 18 * s), (36, 60, 70), op=0.98, wob=1.5, rim=0.3)
    P.layer(rect(x - 70 * s, y - 80 * s, x + 70 * s, y - 68 * s), (140, 128, 108), op=0.98, wob=1.5, rim=0.25)
    P.layer(rect(x - 64 * s, y - 150 * s, x - 56 * s, y - 80 * s), (92, 66, 40), op=0.98, wob=1)
    P.layer(rect(x + 56 * s, y - 150 * s, x + 64 * s, y - 80 * s), (92, 66, 40), op=0.98, wob=1)
    P.layer(poly([(x - 80 * s, y - 150 * s), (x, y - 190 * s), (x + 80 * s, y - 150 * s)]), (150, 70, 52), op=0.98, wob=1.5, rim=0.3)


# ------------------------------------------------------------------ 30/10 A (Mêncio)
def e30a1():
    """Capa: poço de pedra na praça ao entardecer, homem corre em direção a uma criança pequena."""
    P = Paint(3001)
    backdrop(P, "dusk", 240, sunp=(820, 230, 30), seed=3001, clouds=2)
    hill_houses(P, -10, SW + 10, 230, n=8, seed=401, lit=True)
    cobbles(P, 400, seed=12, glow_x=540, base=(120, 108, 92))
    well(P, 700, 540, 1.3)
    person(P, 260, 600, 230, coat=OCHRE, profile=0.6)
    person(P, 520, 590, 110, coat=(60, 100, 120), profile=0.3)
    return fin(P, 3002)


def e30a2():
    """Laranjas caídas: rua de paralelepípedos, sacola rasgada, laranjas rolando; homem se abaixa para ajudar."""
    P = Paint(3011)
    backdrop(P, "day", 250, seed=3011, clouds=2)
    stone_wall(P, 250, 430, seed=81, base=(104, 94, 80), x0=-5, x1=SW + 5)
    cobbles(P, 430, seed=13, base=(130, 116, 96))
    for k in range(8):
        P.layer(ell(520 + k * 54, 540 + (k % 3) * 24, 18, 18), (232, 138, 40), op=0.98, wob=1, rim=0.3)
    person(P, 300, 600, 240, coat=OCHRE, profile=0.5, sit=True)
    person(P, 820, 590, 200, coat=(150, 70, 52), profile=-0.3)
    return fin(P, 3012)


def e30a3():
    """Cansado: homem encolhido sentado nos degraus à noite sob a lanterna."""
    P = Paint(3021)
    backdrop(P, "night", 230, moonp=(900, 100, 22), seed=3021)
    hill_houses(P, -10, SW + 10, 240, n=8, seed=402, lit=True)
    stone_wall(P, 400, SH + 5, seed=82, base=(88, 82, 72))
    stone_stairs(P, 280, 800, 450, 640, steps=4)
    person(P, 540, 580, 220, coat=OCHRE, sit=True, profile=0.2)
    lantern(P, 840, 400, 1.2)
    return fin(P, 3022)


def e30a4():
    """Mêncio: poço noturno com lanterna e criança debruçada ao longe; homem se aproxima."""
    P = Paint(3031)
    backdrop(P, "night", 230, moonp=(180, 100, 24), seed=3031)
    P.layer(rect(-5, 330, SW + 5, SH + 5), (36, 70, 68), op=0.98, wob=3, rim=0.15)
    well(P, 700, 520, 1.5)
    person(P, 560, 560, 90, coat=(60, 100, 120), profile=0.4)
    person(P, 300, 620, 250, coat=OCHRE, profile=0.5)
    lantern(P, 900, 330, 1.2)
    return fin(P, 3032)


def e30a5():
    """Semente: mesa de pedra com vasos de brotos, regador, mãos dele (de costas) regando."""
    P = Paint(3041)
    backdrop(P, "dawn", 260, sunp=(780, 240, 30), seed=3041, clouds=2)
    stone_wall(P, 410, SH + 5, seed=83, base=(98, 90, 78))
    for i, x in enumerate([180, 300, 420, 540]):
        pot_plant(P, x, 405, 1.1, kind="sprout", seed=i + 1)
    P.layer(rect(660, 330, 740, 400), (140, 140, 140), op=0.98, wob=1.5, rim=0.3)
    P.layer(poly([(740, 350), (840, 320), (840, 330), (744, 366)]), (140, 140, 140), op=0.98, wob=1.2)
    person(P, 860, 640, 330, coat=OCHRE, profile=-0.5)
    return fin(P, 3042)


def e30a6():
    """Descanso: banco sob uma árvore, xícara fumegando, lâmpada acesa."""
    P = Paint(3051)
    backdrop(P, "dusk", 270, sunp=(300, 260, 30), seed=3051, clouds=3)
    P.layer(rect(-5, 400, SW + 5, SH + 5), (70, 108, 80), op=0.97, wob=3, rim=0.15)
    big_tree(P, 760, 520, 260, lean=-0.1, leaf=(50, 110, 80), seed=7, crown=0.5)
    bench(P, 480, 580, w=300)
    person(P, 480, 575, 230, coat=OCHRE, sit=True, profile=0.2)
    cup(P, 600, 512, steam=True)
    return fin(P, 3052)


def e30a7():
    """Dois lado a lado no cais olhando o mar ao pôr do sol."""
    P = Paint(3061)
    backdrop(P, "dusk", 300, sunp=(540, 270, 36), seed=3061, clouds=3)
    P.layer(poly([(-5, 640), (-5, 470), (1085, 470), (1085, 640)]), (120, 104, 84), op=0.97, wob=3, rim=0.2)
    foam(P, 0, SW, 430, n=40, seed=8)
    person(P, 480, 580, 240, coat=OCHRE, profile=0.2)
    person(P, 600, 580, 215, coat=(60, 100, 120), profile=-0.2)
    boat(P, 880, 400, 0.8, lit=True)
    return fin(P, 3062)


def e30b():
    """Russell: janela grande aberta para um jardim iluminado, livro e vasos no peitoril."""
    P = Paint(3071)
    room_bg(P, (22, 44, 56))
    floor(P, 560, (66, 48, 34))
    P.vgrad(70, 400, (150, 196, 206), (246, 230, 196), mask=rect(200, 70, 880, 400), wob=1.5, rim=0.35)
    P.layer(poly(ridge(300, 40, 241, x0=200, x1=880)), (74, 130, 92), op=0.97, wob=2)
    P.layer(rect(200, 340, 880, 400), (90, 150, 100), op=0.97, wob=2)
    for t in (190, 880):
        P.layer(rect(t - 14, 56, t + 14, 420), (110, 78, 50), op=0.97, wob=1.2, rim=0.25)
    P.layer(rect(180, 400, 900, 424), (110, 78, 50), op=0.97, wob=1.2, rim=0.25)
    pot_plant(P, 340, 400, 1.1, kind="geranium", seed=2)
    book(P, 540, 398, w=150)
    pot_plant(P, 760, 400, 1.1, kind="sprout", seed=3)
    person(P, 540, 620, 250, coat=OCHRE, profile=0.0)
    P.glow(540, 260, 400, (255, 238, 190), 0.25)
    return fin(P, 3072)


# ------------------------------------------------------------------ 31/10 A (Adam Smith)
def e31a1():
    """Capa: dois lado a lado num banco olhando as luzes da cidade à noite."""
    P = Paint(3101)
    backdrop(P, "night", 270, moonp=(180, 100, 24), seed=3101)
    hill_houses(P, -10, SW + 10, 270, n=12, seed=501, lit=True)
    hill_houses(P, -10, SW + 10, 370, n=10, seed=502, lit=True, body=(132, 146, 144))
    bench(P, 540, 620, w=320)
    person(P, 480, 612, 210, coat=OCHRE, sit=True, profile=0.1)
    person(P, 600, 612, 195, coat=(60, 100, 120), sit=True, profile=-0.1)
    return fin(P, 3102)


def e31a2():
    """Conselho apressado: mesa de café, dois, um deles gesticulando (coat vermelha) e o outro de costas calado."""
    P = Paint(3111)
    room_bg(P, (24, 50, 64))
    floor(P, 540, (60, 44, 32))
    window_frame(P, 740, 70, 980, 300, stars=14, seed=9, cross=False)
    table(P, 160, 780, 410)
    cup(P, 330, 402, steam=True)
    cup(P, 580, 402, steam=False, col=(226, 200, 150))
    chair(P, 330, 590, 300)
    person(P, 330, 580, 300, sit=True, profile=0.3)
    chair(P, 620, 590, 300)
    person(P, 620, 580, 280, coat=(150, 70, 52), sit=True, profile=-0.4)
    lamp(P, 880, 470, h=120, g=0.4)
    return fin(P, 3112)


def e31a3():
    """Silêncio que fica: homem sozinho com uma cadeira vazia à frente, vela e xícara."""
    P = Paint(3121)
    room_bg(P, (18, 40, 54))
    floor(P, 540, (60, 44, 32))
    window_frame(P, 90, 70, 340, 300, stars=22, seed=10, cross=False)
    table(P, 260, 780, 410)
    candle(P, 520, 410, h=54)
    cup(P, 420, 402, steam=True)
    cup(P, 620, 402, steam=False)
    chair(P, 330, 590, 300)
    person(P, 330, 580, 300, sit=True, profile=0.2)
    chair(P, 720, 590, 300)
    P.glow(520, 380, 300, WARM, 0.35)
    return fin(P, 3122)


def e31a4():
    """Smith: encosta com muitas janelas acesas, gente ao longe; luz de cada casa ligada por um fio de luzes."""
    P = Paint(3131)
    backdrop(P, "night", 220, moonp=(860, 90, 22), seed=3131)
    hill_houses(P, -10, SW + 10, 240, n=12, seed=503, lit=True)
    hill_houses(P, -10, SW + 10, 350, n=12, seed=504, lit=True, body=(132, 146, 144))
    hill_houses(P, -10, SW + 10, 460, n=10, seed=505, lit=True, body=(150, 156, 148))
    string_lights(P, 40, 1040, 420, sag=60, n=18)
    return fin(P, 3132)


def e31a5():
    """Escutar: mesa com duas xícaras e vela; ele de costas, cabeça inclinada para o outro lado, silêncio."""
    P = Paint(3141)
    room_bg(P, (20, 44, 58))
    floor(P, 540, (64, 46, 34))
    table(P, 220, 860, 410)
    cup(P, 400, 402, steam=True)
    cup(P, 680, 402, steam=True, col=(226, 200, 150))
    candle(P, 540, 410, h=60)
    chair(P, 330, 590, 300)
    person(P, 330, 580, 300, sit=True, profile=0.5)
    chair(P, 750, 590, 300)
    person(P, 750, 580, 285, coat=(60, 100, 120), sit=True, profile=-0.5)
    P.glow(540, 370, 300, WARM, 0.3)
    lamp(P, 130, 450, h=130, g=0.4)
    return fin(P, 3142)


def e31a6():
    """Perto o bastante: banco com dois casacos lado a lado, uma xícara, vento no mar."""
    P = Paint(3151)
    backdrop(P, "dusk", 280, sunp=(540, 255, 32), seed=3151, clouds=3)
    P.layer(rect(-5, 430, SW + 5, SH + 5), (110, 100, 84), op=0.97, wob=3, rim=0.2)
    foam(P, 0, SW, 420, n=36, seed=9)
    bench(P, 540, 590, w=330)
    ochre_coat_folded(P, 460, 540, w=120)
    P.layer(rrect(600, 520, 700, 560, 8), (60, 100, 120), op=0.98, wob=1.2, rim=0.3)
    cup(P, 560, 532, steam=True)
    return fin(P, 3152)


def e31a7():
    """Caminhar junto: dois caminhando por rua de pedra com lanterna, noite."""
    P = Paint(3161)
    backdrop(P, "night", 230, moonp=(860, 90, 24), seed=3161)
    hill_houses(P, -10, SW + 10, 240, n=10, seed=506, lit=True)
    cobbles(P, 440, seed=14, glow_x=540)
    stone_wall(P, 340, 440, seed=84, base=(84, 78, 70))
    lantern(P, 200, 360, 1.2)
    lantern(P, 900, 360, 1.2)
    person(P, 480, 590, 230, coat=OCHRE, profile=0.3)
    person(P, 600, 580, 210, coat=(60, 100, 120), profile=0.3)
    return fin(P, 3162)


def e31b():
    """Dōgen: lareira de pedra: toras acesas à esquerda e um monte de cinzas à direita, noite."""
    P = Paint(3171)
    room_bg(P, (22, 38, 48))
    floor(P, 580, (60, 44, 32))
    P.layer(rect(260, 150, 820, 600), (96, 88, 76), op=0.98, wob=2, rim=0.3, vary=0.18)
    P.layer(rect(330, 250, 750, 590), (22, 20, 20), op=0.99, wob=2, rim=0.25)
    P.glow(450, 480, 200, (255, 150, 60), 0.75)
    P.layer(rect(380, 520, 520, 560), (90, 56, 34), op=0.98, wob=1.5, rim=0.3)
    P.layer(ell(450, 500, 60, 34), (248, 168, 70), op=0.95, wob=2, rim=0.1)
    P.layer(ell(450, 480, 28, 40), (255, 214, 120), op=0.9, wob=2, rim=0.0)
    P.layer(ell(650, 566, 80, 24), (170, 164, 156), op=0.97, wob=2, rim=0.2, soft=2)
    P.layer(ell(650, 556, 52, 14), (200, 194, 186), op=0.8, wob=2, rim=0.0, soft=2)
    person(P, 140, 620, 230, coat=OCHRE, profile=0.7)
    return fin(P, 3172)


SCENES = {n: f for n, f in globals().items() if n.startswith("e3") and callable(f)}
