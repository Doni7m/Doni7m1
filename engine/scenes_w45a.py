"""Cenas 26 e 27/10/2026: Mill (felicidade como consequência), Emerson, Ortega y Gasset (circunstância), Descartes."""
from lib3 import *


# ------------------------------------------------------------------ 26/10 A (Mill)
def e26a1():
    """Capa: homem corre atrás de um balão dourado que sobe, no caminho de pedra à beira do mar."""
    P = Paint(2601)
    backdrop(P, "dawn", 300, sunp=(760, 250, 34), seed=2601, clouds=2)
    P.layer(rect(-5, 400, SW + 5, SH + 5), (86, 110, 96), op=0.97, wob=3, rim=0.15)
    cobbles(P, 470, seed=7, glow_x=500, base=(110, 118, 108))
    person(P, 330, 590, 230, coat=OCHRE, profile=0.5)
    P.line([(380, 400), (560, 200)], w=2, alpha=0.5, color=(70, 60, 50))
    P.glow(580, 190, 80, GOLD, 0.7)
    P.layer(ell(580, 190, 32, 40), (240, 190, 90), op=0.98, wob=1.2, rim=0.25)
    P.layer(ell(572, 180, 10, 14), (255, 232, 170), op=0.7, wob=1, rim=0)
    return fin(P, 2602)


def e26a2():
    """Régua: homem de costas diante de uma régua gigante apoiada na parede, mesa com caderno."""
    P = Paint(2611)
    room_bg(P, (22, 48, 62))
    floor(P, 520, (66, 48, 34))
    window_frame(P, 90, 70, 330, 300, stars=18, seed=4, cross=False)
    P.layer(rect(660, 60, 700, 520), (210, 186, 130), op=0.98, wob=1.2, rim=0.3)
    for k in range(18):
        P.layer(rect(660 if k % 2 == 0 else 672, 80 + k * 24, 700, 83 + k * 24), (60, 40, 28), op=0.9, wob=0.5, rim=0)
    table(P, 120, 520, 420)
    book(P, 300, 410, w=160)
    candle(P, 440, 420, h=44)
    person(P, 820, 590, 270, sit=False, profile=-0.3)
    P.glow(300, 380, 260, WARM, 0.25)
    return fin(P, 2612)


def e26a3():
    """Placar: sala de jantar, mesa com café esfriando, conversa, ele de costas olhando um relógio."""
    P = Paint(2621)
    room_bg(P, (24, 50, 64))
    floor(P, 540, (60, 44, 32))
    table(P, 220, 860, 400)
    cup(P, 350, 392, steam=False)
    cup(P, 700, 392, steam=False, col=(226, 200, 150))
    clock_round(P, 540, 170, 80, hands=(0.4, 0.1))
    lamp(P, 880, 430, h=120, g=0.5)
    chair(P, 330, 590, 300)
    person(P, 330, 580, 300, sit=True, profile=0.2)
    chair(P, 760, 590, 300)
    P.glow(540, 380, 330, WARM, 0.2)
    return fin(P, 2622)


def e26a4():
    """Mill: biblioteca, estante, homem lê com a atenção em outro lugar: mapa de causas — vela e livros."""
    P = Paint(2631)
    room_bg(P, (18, 40, 54))
    floor(P, 560, (60, 42, 30))
    for k in range(3):
        P.layer(rect(60, 90 + k * 140, 360, 100 + k * 140), WOOD_D, op=0.98, wob=1.2)
        for j in range(8):
            P.layer(rect(70 + j * 36, 20 + k * 140 + (j % 3) * 6, 98 + j * 36, 90 + k * 140),
                    [(176, 98, 62), (60, 100, 112), (200, 160, 80), (88, 70, 120)][j % 4], op=0.97, wob=1)
    table(P, 480, 960, 410)
    book(P, 650, 402, w=210)
    candle(P, 820, 410, h=60)
    P.glow(700, 340, 260, WARM, 0.35)
    window_frame(P, 440, 70, 700, 260, stars=24, seed=6, cross=False)
    moon(P, 600, 150, 22)
    person(P, 590, 590, 280, sit=True, profile=0.35)
    return fin(P, 2632)


def e26a5():
    """Fazer por si: homem rega vasos numa varanda ao amanhecer, hortênsias."""
    P = Paint(2641)
    backdrop(P, "dawn", 260, sunp=(260, 220, 30), seed=2641, clouds=2)
    stone_wall(P, 420, SH + 5, seed=14, base=(100, 92, 80))
    for i, x in enumerate([700, 810, 920]):
        hydrangea(P, x, 372, r=56, col=[(84, 124, 206), (150, 110, 190), (100, 150, 210)][i], seed=i + 1)
    person(P, 480, 590, 300, coat=OCHRE, profile=0.5)
    pot_plant(P, 160, 600, 1.4, seed=3)
    return fin(P, 2642)


def e26a6():
    """Dia pesado: janela com chuva e homem sentado ao lado de uma xícara e uma segunda cadeira vazia com casaco."""
    P = Paint(2651)
    room_bg(P, (20, 40, 52))
    floor(P, 540, (60, 44, 32))
    window_frame(P, 600, 80, 940, 360, sky_top=(40, 56, 72), sky_bot=(100, 120, 126), cross=True)
    for k in range(34):
        x = 610 + (k * 31) % 320
        y = 90 + (k * 53) % 250
        P.line([(x, y), (x - 6, y + 20)], w=2, alpha=0.5, color=(220, 232, 238))
    table(P, 90, 520, 420)
    cup(P, 280, 412, steam=True)
    lamp(P, 160, 432, h=120, g=0.5)
    chair(P, 330, 590, 300)
    person(P, 330, 580, 300, sit=True, profile=0.2)
    chair(P, 450, 590, 300, c=WOOD_X)
    ochre_coat_folded(P, 450, 468, w=100)
    return fin(P, 2652)


def e26a7():
    """Alegria de lado: homem trabalhando num banco de jardim, borboleta/luz dourada chegando de lado."""
    P = Paint(2661)
    backdrop(P, "dusk", 280, sunp=(930, 270, 30), seed=2661, clouds=2)
    P.layer(rect(-5, 400, SW + 5, SH + 5), (70, 110, 84), op=0.97, wob=3, rim=0.15)
    for x in (120, 260):
        banana_leaf(P, x, 420, -1.2, 190, 70)
    bench(P, 520, 570, w=300)
    person(P, 520, 570, 250, sit=True, profile=0.4)
    P.glow(930, 300, 280, GOLD, 0.5)
    for k in range(8):
        P.glow(760 + k * 16, 350 + (k % 3) * 20, 7, GOLD, 0.9)
    return fin(P, 2662)


def e26b():
    """Emerson: cadeira de madeira vazia à mesa posta, uma luz quente, e a cadeira dele puxada."""
    P = Paint(2671)
    room_bg(P, (20, 44, 58))
    floor(P, 520, (66, 48, 34))
    window_frame(P, 780, 70, 1000, 300, stars=20, seed=5, cross=False)
    table(P, 160, 780, 380)
    cup(P, 300, 372, steam=True)
    cup(P, 450, 372, steam=True, col=(226, 200, 150))
    cup(P, 600, 372, steam=True)
    chair(P, 220, 590, 300)
    chair(P, 700, 590, 300)
    chair(P, 460, 590, 300)
    P.glow(460, 380, 280, WARM, 0.3)
    lamp(P, 930, 560, h=160, g=0.6)
    return fin(P, 2672)


# ------------------------------------------------------------------ 27/10 A (Ortega)
def e27a1():
    """Capa: homem de costas no patamar de uma escadaria de pedra, vila com casas à sua volta."""
    P = Paint(2701)
    backdrop(P, "dusk", 250, sunp=(760, 240, 30), seed=2701, clouds=2)
    hill_houses(P, -10, SW + 10, 240, n=10, seed=201, lit=True)
    hill_houses(P, -10, SW + 10, 340, n=10, seed=202, lit=True, body=(132, 146, 144))
    stone_stairs(P, 260, 820, 440, 640, steps=5)
    person(P, 540, 470, 210, coat=OCHRE, profile=0.1)
    return fin(P, 2702)


def e27a2():
    """Contas: mesa com envelopes, calculadora, passaporte; ele sentado de costas."""
    P = Paint(2711)
    room_bg(P, (20, 44, 58))
    floor(P, 540, (62, 46, 34))
    table(P, 180, 900, 410)
    stack_papers(P, 360, 400, n=5, w=130)
    letter(P, 560, 394, w=140, tilt=0.04)
    book(P, 700, 402, w=130, open_=False, col=(40, 70, 110))
    lamp(P, 130, 450, h=130, g=0.5)
    chair(P, 540, 590, 310)
    person(P, 540, 580, 300, sit=True, profile=-0.2)
    clock_round(P, 860, 170, 70, hands=(0.85, 0.2))
    return fin(P, 2712)


def e27a3():
    """Largada desigual: duas pessoas numa linha de partida em estrada, a dele bem atrás, ladeira."""
    P = Paint(2721)
    backdrop(P, "day", 260, seed=2721, clouds=2)
    P.layer(poly([(-5, 640), (-5, 360), (1085, 280), (1085, 640)]), (122, 140, 96), op=0.97, wob=3, rim=0.15)
    P.layer(poly([(-5, 540), (1085, 470), (1085, 520), (-5, 600)]), (186, 168, 128), op=0.97, wob=3, rim=0.2)
    person(P, 760, 520, 120, coat=(60, 100, 120), profile=0.1)
    person(P, 640, 560, 150, coat=(150, 70, 52), profile=0.1)
    person(P, 300, 600, 220, coat=OCHRE, profile=0.1)
    P.line([(180, 612), (180, 540)], w=3, alpha=0.7, color=(60, 50, 40))
    P.line([(180, 540), (210, 548), (180, 556)], w=3, alpha=0.7, color=(60, 50, 40))
    return fin(P, 2722)


def e27a4():
    """Ortega: homem parado dentro de um círculo de luz; ao redor, objetos do mundo dele — casa, barco, vaso, mala."""
    P = Paint(2731)
    backdrop(P, "night", 300, moonp=(880, 100, 24), seed=2731)
    P.layer(rect(-5, 400, SW + 5, SH + 5), (36, 70, 68), op=0.98, wob=3, rim=0.15)
    P.glow(540, 480, 220, WARM, 0.45)
    person(P, 540, 590, 250, coat=OCHRE, profile=0.0)
    boat(P, 190, 450, 0.9, lit=True)
    suitcase(P, 840, 570, 1.1)
    pot_plant(P, 960, 560, 1.2, seed=5)
    house(P, 320, 420, 100, 70, lit=True, seed=3)
    return fin(P, 2732)


def e27a5():
    """Inventário: três pilhas de pedras em cores diferentes na mesa de pedra, mãos dele de costas."""
    P = Paint(2741)
    backdrop(P, "dawn", 240, sunp=(220, 220, 30), seed=2741, clouds=1)
    stone_wall(P, 340, SH + 5, seed=22, base=(96, 90, 80))
    for i, (x, col) in enumerate([(300, (176, 98, 62)), (540, (60, 110, 132)), (780, (210, 170, 80))]):
        for j in range(4):
            P.layer(ell(x + (j % 2) * 18 - 10, 330 - j * 26, 72 - j * 8, 22), col, op=0.97, wob=1.2, rim=0.3)
    person(P, 540, 640, 330, coat=OCHRE, profile=0.0)
    return fin(P, 2742)


def e27a6():
    """Mexer num canto: homem de costas arrumando uma estante; luz entrando por janela."""
    P = Paint(2751)
    room_bg(P, (24, 52, 64))
    floor(P, 560, (68, 50, 36))
    window_frame(P, 700, 70, 960, 320, sky_top=(120, 170, 190), sky_bot=(240, 226, 190), cross=True)
    for k in range(3):
        P.layer(rect(90, 110 + k * 150, 460, 122 + k * 150), WOOD_D, op=0.98, wob=1.2)
        for j in range(7):
            P.layer(rect(104 + j * 48, 40 + k * 150 + (j % 2) * 6, 140 + j * 48, 110 + k * 150),
                    [(176, 98, 62), (60, 100, 112), (200, 160, 80), (88, 70, 120)][(j + k) % 4], op=0.97, wob=1)
    person(P, 560, 590, 290, coat=OCHRE, profile=-0.4)
    P.glow(830, 300, 250, WARM, 0.4)
    return fin(P, 2752)


def e27a7():
    """Fim: homem de costas, encosta com terraços (poios) ao sol baixo, caminho adiante."""
    P = Paint(2761)
    backdrop(P, "dusk", 220, sunp=(540, 210, 36), seed=2761, clouds=3)
    for i, y in enumerate([300, 380, 460, 540]):
        P.layer(rect(-5, y, SW + 5, y + 70), [(70, 110, 84), (84, 124, 90), (98, 138, 96), (112, 150, 104)][i], op=0.97, wob=3, rim=0.25)
        stone_wall(P, y + 56, y + 76, seed=30 + i, base=(100, 92, 80), x0=-5, x1=SW + 5)
    person(P, 540, 640, 250, coat=OCHRE, profile=0.0)
    return fin(P, 2762)


def e27b():
    """Descartes: balança de pedra — de um lado um peso grande de pedra, de outro um cesto pequeno, mar ao fundo."""
    P = Paint(2771)
    backdrop(P, "dusk", 300, sunp=(540, 270, 30), seed=2771, clouds=2)
    P.layer(rect(-5, 420, SW + 5, SH + 5), (110, 98, 82), op=0.98, wob=3, rim=0.2)
    person(P, 300, 600, 240, coat=OCHRE, profile=0.3)
    P.layer(poly([(660, 600), (820, 600), (800, 450), (680, 450)]), (88, 80, 72), op=0.98, wob=2, rim=0.3)
    P.layer(ell(740, 440, 90, 34), (116, 106, 92), op=0.98, wob=2, rim=0.3)
    P.layer(ell(930, 580, 50, 22), (196, 138, 52), op=0.98, wob=1.5, rim=0.3)
    sapling(P, 930, 560, 80)
    return fin(P, 2772)


SCENES = {n: f for n, f in globals().items() if n.startswith("e2") and callable(f)}
