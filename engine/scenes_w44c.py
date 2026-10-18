"""Cenas 23 e 24/10/2026: Buber (encontro), Levinas, Confúcio (aprender), Boécio (roda)."""
from lib3 import *


# ------------------------------------------------------------------ 23/10 A (Buber)
def d23a1():
    """Capa: dois desconhecidos se cruzando numa rua de pedra com lanternas ao entardecer."""
    P = Paint(2301)
    backdrop(P, "dusk", 200, sunp=(840, 196, 26), seed=2301, clouds=2)
    P.layer(rect(-5, 200, 300, 520), (184, 166, 128), op=0.98, wob=2, rim=0.3, vary=0.12)
    P.layer(poly([(-25, 200), (140, 130), (320, 200)]), (150, 70, 52), op=0.98, wob=2, rim=0.3)
    P.layer(rect(800, 190, SW + 5, 520), (196, 176, 136), op=0.98, wob=2, rim=0.3, vary=0.12)
    P.layer(poly([(780, 190), (950, 110), (SW + 25, 190)]), (150, 70, 52), op=0.98, wob=2, rim=0.3)
    lit_window(P, 60, 280, 150, 380)
    lit_window(P, 870, 270, 960, 370)
    cobbles(P, 440, SH + 5, seed=23, glow_x=540)
    lantern(P, 330, 340, 1.0)
    lantern(P, 760, 340, 1.0)
    person(P, 450, 600, 230, coat=OCHRE, profile=0.5)
    person(P, 640, 590, 215, coat=(70, 112, 128), hair=(70, 48, 36), profile=-0.5)
    return fin(P, 2302)


def d23a2():
    """Mercado: bancas de flores e frutas, vários vultos com cores diferentes."""
    P = Paint(2311)
    room_bg(P, (170, 150, 112))
    P.vgrad(-5, 200, (120, 96, 70), (180, 160, 120), mask=rect(-5, -5, SW + 5, 200), wob=2, rim=0)
    P.layer(rect(-5, 470, SW + 5, SH + 5), (110, 94, 72), op=1.0, wob=2, rim=0.2)
    for x, col in [(150, (92, 132, 214)), (400, (214, 100, 90)), (650, (232, 184, 92)), (900, (120, 160, 90))]:
        P.layer(rect(x - 110, 330, x + 110, 480), (120, 84, 52), op=0.98, wob=1.5, rim=0.3)
        P.layer(rect(x - 120, 316, x + 120, 336), (176, 98, 62), op=0.98, wob=1.2, rim=0.3)
        for k in range(7):
            P.layer(ell(x - 80 + k * 27, 300, 18, 16), col, op=0.97, wob=1, rim=0.3)
        banana_leaf(P, x, 330, 0.0 + (x % 3 - 1) * 0.3, 120, 26)
    for x, y, h, c in [(260, 560, 200, (70, 112, 128)), (530, 580, 210, (60, 60, 70)), (780, 570, 205, (150, 80, 70)), (1000, 580, 215, (110, 130, 100))]:
        person(P, x, y, h, coat=c, hair=(60, 44, 36))
    P.glow(540, 90, 280, WARM, 0.3)
    return fin(P, 2312)


def d23a3():
    """Fila de vultos escuros iguais, só um de sobretudo ocre: reduzidos a papéis."""
    P = Paint(2321)
    room_bg(P, (36, 60, 70))
    P.layer(rect(-5, 500, SW + 5, SH + 5), (80, 70, 60), op=1.0, wob=2, rim=0.2)
    P.layer(rect(840, 160, SW + 5, 500), (90, 100, 100), op=0.98, wob=1.5, rim=0.3)
    P.layer(rect(870, 260, SW + 5, 300), (150, 140, 120), op=0.98, wob=1)
    clock_round(P, 700, 150, 56, hands=(0.4, 0.8))
    for i, x in enumerate([160, 330, 500, 670]):
        c = OCHRE if i == 2 else (44, 52, 60)
        person(P, x, 580, 220 - i * 4, coat=c, hair=(30, 28, 28), trousers=(30, 32, 40))
    return fin(P, 2322)


def d23a4():
    """Eu e Tu: duas pessoas frente a frente de perfil sob uma lanterna, noite."""
    P = Paint(2331)
    backdrop(P, "night", 260, moonp=(180, 110, 22), seed=2331)
    P.layer(poly(ridge(320, 40, 97, x0=-30, x1=SW + 30)), (18, 48, 58), op=1.0, wob=3)
    cobbles(P, 470, SH + 5, seed=24, glow_x=540)
    lantern(P, 540, 250, 1.4, g=1.0)
    P.line([(540, -5), (540, 214)], w=3, alpha=0.7, color=(40, 30, 24))
    person(P, 450, 600, 250, coat=OCHRE, profile=0.9)
    person(P, 640, 600, 240, coat=(70, 112, 128), hair=(70, 48, 36), profile=-0.9)
    return fin(P, 2332)


def d23a5():
    """Banco de praça: duas pessoas lado a lado, de costas, diante do mar."""
    P = Paint(2341)
    backdrop(P, "dusk", 300, sunp=(540, 296, 34), seed=2341, clouds=2, island=(700, 300))
    P.layer(rect(-5, 470, SW + 5, SH + 5), (110, 100, 80), op=1.0, wob=2, rim=0.2)
    P.layer(rect(-5, 452, SW + 5, 480), STONEL, op=1.0, wob=1.5, rim=0.3)
    bench(P, 540, 600, w=330)
    person(P, 470, 590, 250, sit=True, profile=0.1)
    person(P, 610, 590, 235, sit=True, coat=(70, 112, 128), hair=(70, 48, 36), profile=-0.1)
    tree_pine(P, 130, 560, 300)
    tree_pine(P, 960, 560, 280)
    return fin(P, 2342)


def d23a6():
    """Varanda no alto, vizinha com vaso acena para o homem na rua."""
    P = Paint(2351)
    room_bg(P, (150, 170, 170))
    P.vgrad(-5, 200, (92, 148, 172), (232, 226, 200), mask=rect(-5, -5, SW + 5, 200), wob=2, rim=0)
    facade(P, 120, 760, 220, 520, col=(214, 196, 150))
    lit_window(P, 190, 300, 280, 400, silhouette=False)
    door(P, 560, 380, 650, 520, lit=False)
    P.layer(rect(330, 270, 520, 290), (96, 66, 40), op=0.98, wob=1)
    P.layer(rect(330, 290, 520, 300), (70, 46, 30), op=0.98, wob=1)
    pot_plant(P, 380, 270, 0.9, seed=3)
    hydrangea(P, 470, 240, 40, col=(150, 120, 196), seed=4)
    person(P, 440, 270, 110, coat=(176, 98, 62), hair=(70, 48, 36), profile=0.2)
    cobbles(P, 520, SH + 5, seed=26, glow_x=700, base=(130, 120, 100))
    person(P, 860, 600, 240, coat=OCHRE, profile=-0.3)
    banana_leaf(P, 1000, 560, -0.3, 160, 34)
    return fin(P, 2352)


def d23a7():
    """Encontro na escada: duas pessoas se encontram a meio de uma escadaria com lanternas."""
    P = Paint(2361)
    backdrop(P, "night", 220, moonp=(880, 100, 22), seed=2361)
    P.layer(poly(ridge(280, 40, 98, x0=-30, x1=SW + 30)), (18, 48, 58), op=1.0, wob=3)
    P.layer(rect(-5, 310, SW + 5, SH + 5), (28, 62, 62), op=1.0, wob=2, rim=0.1)
    stone_stairs(P, 300, 780, 310, 640, steps=7)
    lantern(P, 250, 380, 1.1)
    lantern(P, 830, 380, 1.1)
    person(P, 460, 470, 190, coat=OCHRE, profile=0.7)
    person(P, 610, 400, 160, coat=(70, 112, 128), hair=(70, 48, 36), profile=-0.7)
    return fin(P, 2362)


def d23b():
    """Levinas: janela acesa com uma silhueta olhando para fora, rua de pedra vazia, lanterna."""
    P = Paint(2371)
    backdrop(P, "night", 150, moonp=(900, 70, 20), seed=2371)
    facade(P, 280, 800, 190, 500, col=(178, 164, 130))
    lit_window(P, 450, 260, 630, 440, silhouette=True)
    lit_window(P, 340, 300, 400, 400)
    door(P, 700, 360, 770, 500, lit=False)
    cobbles(P, 500, SH + 5, seed=27, glow_x=540)
    lantern(P, 900, 420, 1.0)
    pot_plant(P, 300, 500, 1.0, seed=6)
    return fin(P, 2372)


# ------------------------------------------------------------------ 24/10 A (Confúcio)
def d24a1():
    """Capa: livro aberto sobre a mesa, xícara, planta e mar na janela."""
    P = Paint(2401)
    room_bg(P, (36, 68, 80))
    window_frame(P, 90, 70, 520, 370, sky_top=(92, 148, 172), sky_bot=(232, 226, 200), cross=True)
    P.layer(rect(90, 270, 520, 370), (50, 116, 132), op=0.98, wob=1)
    floor(P, 560, (110, 80, 52))
    table(P, 340, 1000, 430)
    book(P, 650, 424, w=300)
    cup(P, 860, 432, steam=True)
    pot_plant(P, 440, 432, 0.9, kind="sprout")
    lamp(P, 950, 432, h=130, g=0.4)
    return fin(P, 2402)


def d24a2():
    """Formulários e carimbos: balcão, pilhas de papel, relógio de parede."""
    P = Paint(2411)
    room_bg(P, (92, 108, 108))
    floor(P, 520, (120, 110, 94))
    P.layer(rect(80, 420, 1000, 470), (130, 92, 56), op=0.98, wob=1.5, rim=0.3)
    P.layer(rect(60, 470, 1020, 640), (96, 66, 40), op=0.98, wob=1.5, rim=0.3)
    stack_papers(P, 260, 418, n=6, w=170)
    stack_papers(P, 540, 418, n=3, w=150)
    stack_papers(P, 800, 418, n=5, w=160)
    clock_round(P, 540, 170, 76, hands=(0.08, 0.5))
    P.layer(rect(160, 120, 260, 320), (150, 160, 150), op=0.9, wob=1.5, rim=0.3)
    P.layer(rect(860, 120, 960, 320), (150, 160, 150), op=0.9, wob=1.5, rim=0.3)
    return fin(P, 2412)


def d24a3():
    """Violão encostado no canto, empoeirado, ao lado de um livro de idiomas fechado."""
    P = Paint(2421)
    room_bg(P, (22, 48, 62))
    floor(P, 520, (70, 50, 34))
    P.layer(rect(700, 80, 1040, 330), (38, 72, 88), op=0.98, wob=1.5, rim=0.3)
    window_frame(P, 720, 100, 1020, 310, stars=14, seed=2, cross=False)
    guitar(P, 380, 400, 1.2)
    P.layer(rect(250, 520, 520, 540), (60, 44, 32), op=0.97, wob=1)
    book(P, 700, 530, w=160, open_=False)
    book(P, 700, 512, w=140, open_=False, col=(60, 100, 120))
    lamp(P, 880, 530, h=120, g=0.4)
    return fin(P, 2422)


def d24a4():
    """Estudioso: homem sentado de perfil a uma escrivaninha baixa com rolo de papel e pincel; luz quente."""
    P = Paint(2431)
    room_bg(P, (30, 60, 72))
    window_frame(P, 600, 80, 940, 350, stars=18, seed=3, cross=True)
    floor(P, 520, (96, 68, 44))
    table(P, 220, 760, 430)
    book(P, 470, 424, w=360)
    P.line([(640, 424), (700, 392)], w=5, alpha=0.9, color=(40, 30, 24))
    candle(P, 330, 430, h=44)
    chair(P, 140, 580, 320)
    person(P, 150, 570, 300, sit=True, profile=0.9)
    return fin(P, 2432)


def d24a5():
    """Jardim de hortênsias e etiquetas, homem de costas lendo um cartão."""
    P = Paint(2441)
    P.vgrad(-5, 260, (92, 148, 172), (232, 226, 200), mask=rect(-5, -5, SW + 5, 260), wob=2, rim=0, vary=0.07)
    P.layer(poly(ridge(250, 60, 101, x0=-30, x1=SW + 30)), (70, 116, 98), op=1.0, wob=3)
    P.layer(rect(-5, 340, SW + 5, SH + 5), (66, 116, 76), op=1.0, wob=2, rim=0.1)
    for x, y, col, s in [(160, 470, (92, 132, 214), 60), (340, 440, (150, 120, 196), 54), (860, 460, (92, 132, 214), 62), (1000, 430, (214, 130, 150), 50)]:
        hydrangea(P, x, y, s, col=col, seed=int(x))
    fern(P, 700, 540, n=9, size=110)
    P.layer(rect(250, 480, 256, 540), (110, 76, 46), op=0.95, wob=0.6)
    P.layer(rect(236, 470, 270, 494), (240, 226, 190), op=0.97, wob=0.6)
    person(P, 540, 590, 240, coat=OCHRE, profile=0.1)
    book(P, 540, 480, w=70)
    return fin(P, 2442)


def d24a6():
    """Praticar: homem sentado tocando violão, partitura no chão, janela com tarde."""
    P = Paint(2451)
    room_bg(P, (36, 66, 78))
    window_frame(P, 130, 70, 480, 340, sky_top=(24, 48, 92), sky_bot=(226, 152, 98), cross=False)
    floor(P, 520, (120, 86, 54))
    chair(P, 650, 590, 310)
    person(P, 650, 580, 300, sit=True, profile=0.3)
    guitar(P, 640, 500, 0.8)
    letter(P, 360, 560, w=110, tilt=0.03, stamp=False)
    letter(P, 480, 580, w=110, tilt=-0.03, stamp=False)
    lamp(P, 900, 560, h=190, g=0.5)
    return fin(P, 2452)


def d24a7():
    """Observando estrelas: homem sentado numa pedra com lanterna e livro, céu cheio de estrelas."""
    P = Paint(2461)
    P.vgrad(-5, 420, (10, 22, 48), (40, 90, 104), mask=rect(-5, -5, SW + 5, 420), wob=2, rim=0, vary=0.1)
    P.stars(220, 400, seed=5)
    moon(P, 880, 130, 22)
    P.layer(poly(ridge(380, 70, 103, x0=-30, x1=SW + 30)), (14, 40, 52), op=1.0, wob=3)
    P.layer(rect(-5, 470, SW + 5, SH + 5), (26, 56, 56), op=1.0, wob=2, rim=0.1)
    P.layer(poly([(250, 640), (300, 520), (560, 500), (640, 640)]), (60, 62, 64), op=0.99, wob=3, rim=0.3)
    person(P, 450, 530, 200, sit=True, profile=0.3)
    lantern(P, 640, 540, 0.8)
    book(P, 330, 522, w=90)
    return fin(P, 2462)


def d24b():
    """Boécio: roda de carroça encostada num muro de pedra ao luar."""
    P = Paint(2471)
    backdrop(P, "night", 220, moonp=(840, 90, 26), seed=2471)
    stone_wall(P, 330, SH + 5, seed=47, base=(76, 76, 78))
    wheel(P, 540, 440, 170)
    P.glow(540, 440, 320, (170, 200, 230), 0.15)
    P.layer(rect(-5, 560, SW + 5, SH + 5), (46, 46, 44), op=1.0, wob=2, rim=0.2)
    return fin(P, 2472)


SCENES = {n: f for n, f in globals().items() if (n.startswith("d23") or n.startswith("d24")) and callable(f)}
