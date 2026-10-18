"""Cenas 21 e 22/10/2026: Zhuangzi (árvore inútil), Paulo Freire, Bergson (mudança), Cícero."""
from lib3 import *


# ------------------------------------------------------------------ 21/10 A (Zhuangzi)
def d21a1():
    """Capa: árvore enorme e torta num prado, homem pequeno sentado à sombra, colinas ao fundo."""
    P = Paint(2101)
    P.vgrad(-5, 330, (92, 148, 172), (232, 226, 200), mask=rect(-5, -5, SW + 5, 330), wob=2, rim=0, vary=0.07)
    P.layer(poly(ridge(300, 70, 61, x0=-30, x1=SW + 30)), (92, 128, 112), op=0.95, wob=3)
    P.layer(poly(ridge(380, 40, 62, x0=-30, x1=SW + 30)), (60, 106, 88), op=1.0, wob=3)
    P.layer(rect(-5, 430, SW + 5, SH + 5), (74, 120, 84), op=1.0, wob=2, rim=0.1)
    big_tree(P, 600, 560, 360, lean=0.35, seed=2, crown=0.55)
    person(P, 470, 590, 150, coat=OCHRE, sit=True, profile=0.3)
    gulls(P, [(170, 120, 1.0), (240, 90, 0.8)], col=(110, 130, 140))
    return fin(P, 2102)


def d21a2():
    """Agenda cheia: parede de bilhetes coloridos, relógio, mesa e xícara vazia."""
    P = Paint(2111)
    room_bg(P, (28, 56, 68))
    floor(P, 560, (74, 56, 42))
    r = np.random.default_rng(5)
    cols = [(240, 226, 190), (232, 184, 92), (150, 190, 200), (214, 130, 100), (196, 220, 176)]
    for i in range(5):
        for j in range(5):
            x, y = 90 + i * 110 + r.uniform(-6, 6), 80 + j * 82 + r.uniform(-4, 4)
            P.layer(rect(x, y, x + 88, y + 66), cols[(i * 2 + j) % 5], op=0.96, wob=1.2, rim=0.3)
            for k in range(3):
                P.line([(x + 10, y + 16 + k * 14), (x + 70, y + 16 + k * 14 + r.uniform(-2, 2))], w=2, alpha=0.4)
    clock_round(P, 830, 200, 90, hands=(0.7, 0.05))
    table(P, 640, 1040, 440)
    cup(P, 760, 442, steam=False)
    phone(P, 930, 432, w=84, lit=True, tilt=2)
    return fin(P, 2112)


def d21a3():
    """Culpa silenciosa: homem curvado sobre a mesa à luz do candeeiro, pilha de livros, noite na janela."""
    P = Paint(2121)
    room_bg(P, (16, 40, 54))
    window_frame(P, 700, 70, 1000, 330, stars=24, seed=13)
    floor(P, 566, (62, 44, 32))
    table(P, 160, 800, 400)
    for i, (w, col) in enumerate([(210, (120, 60, 44)), (190, (60, 100, 120)), (170, (196, 138, 52))]):
        P.layer(rect(520 - w / 2, 400 - (i + 1) * 22, 520 + w / 2, 400 - i * 22), col, op=0.97, wob=1, rim=0.3)
    lamp(P, 250, 400, h=140)
    chair(P, 430, 590, 300)
    person(P, 430, 580, 300, sit=True, profile=0.2)
    book(P, 330, 396, w=150)
    return fin(P, 2122)


def d21a4():
    """A árvore torta: carpinteiro se afasta com o machado, tronco nodoso."""
    P = Paint(2131)
    P.vgrad(-5, 320, (130, 176, 190), (240, 226, 190), mask=rect(-5, -5, SW + 5, 320), wob=2, rim=0, vary=0.07)
    P.layer(poly(ridge(330, 50, 71, x0=-30, x1=SW + 30)), (110, 144, 120), op=0.95, wob=3)
    P.layer(rect(-5, 420, SW + 5, SH + 5), (90, 130, 84), op=1.0, wob=2, rim=0.1)
    P.layer(poly([(150, 640), (700, 500), (760, 640)]), (170, 150, 110), op=0.9, wob=3, rim=0.2)
    big_tree(P, 330, 520, 300, lean=-0.55, seed=4, crown=0.5)
    P.layer(rect(520, 500, 580, 540), (110, 76, 46), op=0.98, wob=1.5, rim=0.3)
    P.layer(rect(530, 440, 536, 520), (92, 66, 44), op=0.98, wob=0.8)
    P.layer(poly([(512, 440), (546, 430), (550, 458), (518, 462)]), (150, 150, 150), op=0.97, wob=0.8)
    person(P, 840, 600, 230, coat=(150, 100, 60), hair=(60, 48, 40))
    return fin(P, 2132)


def d21a5():
    """Caminhar sem destino: trilha na falésia ao entardecer, homem de costas a passear."""
    P = Paint(2141)
    backdrop(P, "dusk", 300, sunp=(300, 296, 34), seed=2141, clouds=2, island=(620, 380))
    cliff(P, side="right", top=330, seed=5, col=(34, 70, 66), reach=560)
    P.layer(poly([(-5, 640), (-5, 560), (300, 520), (640, 470), (760, 640)]), (84, 120, 76), op=1.0, wob=3, rim=0.2)
    P.layer(poly([(240, 640), (420, 520), (640, 470), (700, 480), (480, 640)]), (190, 160, 110), op=0.95, wob=3, rim=0.2)
    person(P, 520, 560, 200, coat=OCHRE, profile=0.2)
    return fin(P, 2142)


def d21a6():
    """Porto de pesca: barcos de trabalho, cestos, homem sentado no muro olhando."""
    P = Paint(2151)
    backdrop(P, "dusk", 270, sunp=(160, 266, 30), seed=2151, clouds=1)
    boat(P, 540, 380, 1.1, lit=True, hull=(46, 98, 112))
    boat(P, 850, 350, 0.8, lit=False, hull=(176, 98, 62), sail=True)
    stone_wall(P, 470, SH + 5, seed=44, base=(100, 92, 80))
    P.layer(rrect(110, 440, 240, 480, 8), (176, 130, 80), op=0.98, wob=1.2, rim=0.3)
    P.layer(rrect(260, 450, 360, 482, 8), (150, 108, 64), op=0.98, wob=1.2, rim=0.3)
    person(P, 700, 480, 230, sit=True, profile=0.3)
    lantern(P, 960, 430, 0.9)
    return fin(P, 2152)


def d21a7():
    """Hora inútil: homem sentado debaixo de uma árvore à beira-mar, xícara ao lado, pôr do sol."""
    P = Paint(2161)
    backdrop(P, "dusk", 290, sunp=(820, 286, 40), seed=2161, clouds=3)
    P.layer(rect(-5, 420, SW + 5, SH + 5), (86, 124, 76), op=1.0, wob=2, rim=0.1)
    big_tree(P, 330, 560, 300, lean=0.3, seed=7, crown=0.6)
    bench(P, 420, 580, w=230)
    person(P, 420, 570, 230, sit=True, profile=0.3)
    cup(P, 600, 560, steam=True)
    return fin(P, 2162)


def d21b():
    """Paulo Freire: terraços de plantação (poios), duas pessoas aprendendo juntas."""
    P = Paint(2171)
    P.vgrad(-5, 220, (92, 148, 172), (232, 226, 200), mask=rect(-5, -5, SW + 5, 220), wob=2, rim=0, vary=0.07)
    P.layer(poly(ridge(210, 60, 81, x0=-30, x1=SW + 30)), (60, 106, 88), op=1.0, wob=3)
    for k, (y, col) in enumerate([(280, (74, 124, 84)), (370, (92, 138, 80)), (460, (110, 150, 80)), (550, (126, 160, 84))]):
        P.layer(rect(-5, y, SW + 5, SH + 5), col, op=1.0, wob=2, rim=0.2)
        P.layer(rect(-5, y - 6, SW + 5, y + 16), STONEL, op=1.0, wob=1.5, rim=0.3)
        for x in range(40, SW, 70):
            P.layer(ell(x + (k * 21) % 40, y + 40, 22, 10), (52, 104, 66), op=0.9, wob=1, rim=0.2)
    banana_leaf(P, 130, 480, -0.3, 160, 34)
    banana_leaf(P, 980, 470, 0.3, 160, 34)
    person(P, 420, 520, 190, coat=OCHRE, profile=0.5)
    person(P, 600, 440, 150, coat=(70, 112, 128), hair=(70, 48, 36), profile=-0.5)
    return fin(P, 2172)


# ------------------------------------------------------------------ 22/10 A (Bergson)
def d22a1():
    """Capa: escadaria de pedra subindo ao entardecer, homem de costas no meio do caminho."""
    P = Paint(2201)
    backdrop(P, "dusk", 250, sunp=(780, 246, 34), seed=2201, clouds=2)
    P.layer(poly(ridge(300, 40, 91, x0=-30, x1=SW + 30)), (60, 94, 84), op=0.95, wob=3)
    P.layer(rect(-5, 330, SW + 5, SH + 5), (52, 92, 72), op=1.0, wob=2, rim=0.2)
    stone_stairs(P, 330, 760, 330, 640, steps=8)
    person(P, 545, 520, 190, coat=OCHRE)
    lantern(P, 260, 440, 0.9)
    lantern(P, 840, 400, 0.9)
    return fin(P, 2202)


def d22a2():
    """Parede de fotografias antigas, sobretudo no cabide, luminária."""
    P = Paint(2211)
    room_bg(P, (26, 52, 64))
    floor(P, 556)
    for i, (x, y, w, h) in enumerate([(150, 100, 150, 190), (330, 130, 190, 130), (560, 90, 130, 170), (730, 140, 180, 120), (230, 330, 120, 100)]):
        P.layer(rect(x - 8, y - 8, x + w + 8, y + h + 8), (96, 66, 40), op=0.98, wob=1)
        P.layer(rect(x, y, x + w, y + h), [(170, 190, 180), (222, 200, 150), (150, 170, 190)][i % 3], op=0.97, wob=1, rim=0.3)
        P.layer(ell(x + w / 2, y + h * 0.4, w * 0.16, h * 0.18), (70, 56, 46), op=0.9, wob=1)
        P.layer(poly([(x + w * 0.25, y + h), (x + w / 2, y + h * 0.6), (x + w * 0.75, y + h)]), (70, 56, 46), op=0.9, wob=1)
    P.layer(rect(860, 280, 1020, 294), WOOD_X, op=0.98, wob=1)
    P.layer(poly([(890, 296), (960, 296), (975, 500), (880, 500)]), OCHRE, op=0.98, wob=2, rim=0.3)
    table(P, 380, 760, 430)
    lamp(P, 480, 430, h=120)
    letter(P, 640, 414, w=130)
    return fin(P, 2212)


def d22a3():
    """Barco partindo do cais ao anoitecer, homem sentado no cais olhando as luzes."""
    P = Paint(2221)
    backdrop(P, "dusk", 300, sunp=(180, 296, 30), seed=2221, clouds=2)
    boat(P, 780, 400, 0.6, lit=True)
    P.layer(rect(-5, 470, SW + 5, 520), (96, 88, 76), op=1.0, wob=1.5, rim=0.3)
    P.layer(rect(-5, 520, SW + 5, SH + 5), (40, 38, 38), op=1.0, wob=1.5, rim=0.2)
    person(P, 300, 470, 230, sit=True, profile=0.5)
    lantern(P, 120, 430, 0.9)
    return fin(P, 2222)


def d22a4():
    """Duração: vela pela metade ao lado do relógio, mar na janela."""
    P = Paint(2231)
    room_bg(P, (18, 42, 56))
    window_frame(P, 560, 70, 960, 370, stars=30, seed=14, cross=False)
    P.layer(rect(560, 290, 960, 370), (22, 62, 76), op=0.98, wob=1)
    moon(P, 800, 170, 24)
    moon_reflection(P, 800, 290, 370, n=8, seed=4)
    floor(P, 556)
    table(P, 120, 560, 420)
    candle(P, 240, 420, h=56)
    candle(P, 330, 420, h=24)
    clock_round(P, 180, 220, 74, hands=(0.42, 0.9))
    cup(P, 440, 422, steam=True)
    return fin(P, 2232)


def d22a5():
    """Escrever três linhas: mesinha na varanda com caderno, luzes e noite suave."""
    P = Paint(2241)
    backdrop(P, "night", 300, moonp=(160, 120, 24), seed=2241)
    P.layer(rect(-5, 480, SW + 5, SH + 5), (96, 70, 46), op=1.0, wob=2, rim=0.2)
    P.layer(rect(-5, 470, SW + 5, 490), STONEL, op=1.0, wob=1.5)
    string_lights(P, 60, 1020, 120, sag=40, n=12)
    table(P, 400, 760, 440, legs=True)
    book(P, 520, 438, w=150)
    cup(P, 660, 438, steam=True)
    candle(P, 600, 440, h=40)
    chair(P, 590, 600, 300)
    person(P, 590, 600, 300, sit=True, profile=0.2)
    hydrangea(P, 160, 500, 60, col=(120, 140, 220), seed=2)
    return fin(P, 2242)


def d22a6():
    """Caminho de lanternas: homem avança numa vereda, lanternas acesas ficaram para trás."""
    P = Paint(2251)
    backdrop(P, "night", 260, moonp=(880, 110, 22), seed=2251)
    P.layer(poly(ridge(330, 50, 92, x0=-30, x1=SW + 30)), (18, 48, 58), op=1.0, wob=3)
    P.layer(rect(-5, 400, SW + 5, SH + 5), (28, 62, 62), op=1.0, wob=2, rim=0.1)
    P.layer(poly([(-5, 640), (-5, 600), (420, 520), (800, 440), (1085, 420), (1085, 470), (620, 560), (400, 640)]), (150, 126, 92), op=0.97, wob=3, rim=0.2)
    for (x, y, s) in [(140, 560, 1.1), (360, 520, 1.0), (580, 490, 0.9), (780, 460, 0.8), (940, 440, 0.7)]:
        lantern(P, x, y, s)
    person(P, 880, 470, 120, coat=OCHRE)
    return fin(P, 2252)


def d22a7():
    """Casa em obra: escada encostada, balde de tinta, janela acesa e estrelas."""
    P = Paint(2261)
    backdrop(P, "night", 300, moonp=(180, 110, 22), seed=2261)
    P.layer(rect(-5, 500, SW + 5, SH + 5), (40, 78, 74), op=1.0, wob=2, rim=0.1)
    facade(P, 400, 900, 260, 520, col=(214, 200, 168))
    lit_window(P, 470, 330, 560, 430)
    P.layer(rect(640, 330, 720, 430), (184, 170, 140), op=0.98, wob=1, rim=0.3)
    door(P, 780, 380, 850, 520, lit=True, ajar=0.2)
    ladder(P, 320, 520, 300, w=70, lean=60)
    P.layer(rect(560, 520, 640, 560), (176, 98, 62), op=0.98, wob=1.2, rim=0.3)
    P.layer(ell(600, 520, 40, 8), (232, 184, 92), op=0.98, wob=1)
    person(P, 210, 590, 220)
    return fin(P, 2262)


def d22b():
    """Cícero: muda de árvore recém-plantada numa encosta ao pôr do sol; árvore velha ao lado."""
    P = Paint(2271)
    backdrop(P, "dusk", 280, sunp=(560, 276, 44), seed=2271, clouds=3)
    P.layer(poly(ridge(340, 50, 95, x0=-30, x1=SW + 30)), (60, 100, 78), op=1.0, wob=3)
    P.layer(rect(-5, 430, SW + 5, SH + 5), (86, 124, 76), op=1.0, wob=2, rim=0.1)
    big_tree(P, 220, 560, 330, lean=0.2, seed=3, crown=0.5)
    sapling(P, 640, 560, 120)
    P.layer(ell(640, 566, 50, 10), (92, 64, 40), op=0.95, wob=2)
    person(P, 770, 570, 210, coat=OCHRE, profile=-0.4)
    P.layer(rect(840, 560, 872, 574), (150, 150, 150), op=0.95, wob=0.8)
    return fin(P, 2272)


SCENES = {n: f for n, f in globals().items() if (n.startswith("d21") or n.startswith("d22")) and callable(f)}
