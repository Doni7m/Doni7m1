"""Cenas 25/10/2026: Merleau-Ponty (corpo) e Iris Murdoch."""
from lib3 import *


def d25a1():
    """Capa: homem caminha por uma levada (canal de água) entre samambaias, névoa da manhã."""
    P = Paint(2501)
    P.vgrad(-5, 240, (110, 160, 172), (236, 232, 210), mask=rect(-5, -5, SW + 5, 240), wob=2, rim=0, vary=0.07)
    P.layer(poly(ridge(180, 80, 111, x0=-30, x1=SW + 30)), (74, 114, 104), op=0.95, wob=3)
    P.layer(poly(ridge(280, 60, 112, x0=-30, x1=SW + 30)), (46, 90, 80), op=1.0, wob=3)
    P.layer(rect(-5, 330, SW + 5, SH + 5), (36, 82, 66), op=1.0, wob=2, rim=0.1)
    P.layer(poly([(-5, 640), (-5, 540), (1085, 430), (1085, 640)]), (150, 130, 96), op=0.97, wob=3, rim=0.2)
    P.layer(poly([(-5, 540), (1085, 430), (1085, 452), (-5, 568)]), (60, 140, 156), op=0.95, wob=2, rim=0.2, soft=1.4)
    fern(P, 120, 520, n=9, size=130)
    fern(P, 920, 410, n=9, size=110)
    person(P, 520, 570, 210, coat=OCHRE, profile=0.1)
    P.strokes(0, SW, 250, 330, 14, (240, 240, 232), op=0.3, wmin=120, wmax=300, seed=2)
    return fin(P, 2502)


def d25a2():
    """Mais um café: mesa com três xícaras vazias, notebook aceso, relógio tarde."""
    P = Paint(2511)
    room_bg(P, (20, 42, 56))
    floor(P, 560, (64, 46, 34))
    window_frame(P, 90, 70, 380, 330, stars=18, seed=3, cross=False)
    clock_round(P, 700, 180, 84, hands=(0.95, 0.08))
    table(P, 220, 980, 420)
    P.layer(poly([(380, 420), (650, 420), (630, 300), (400, 300)]), (30, 32, 38), op=0.98, wob=1, rim=0.25)
    P.layer(poly([(406, 404), (624, 404), (610, 316), (416, 316)]), (140, 186, 230), op=0.95, wob=0.8, rim=0)
    P.glow(515, 350, 260, (120, 170, 230), 0.35)
    cup(P, 730, 424, steam=False)
    cup(P, 820, 424, steam=False, col=(226, 200, 150))
    cup(P, 910, 424, steam=True)
    lamp(P, 270, 420, h=110, g=0.4)
    return fin(P, 2512)


def d25a3():
    """Carregando o peso: homem sobe escada de pedra com mala grande ao entardecer."""
    P = Paint(2521)
    backdrop(P, "dusk", 220, sunp=(200, 216, 30), seed=2521, clouds=2)
    P.layer(rect(-5, 300, SW + 5, SH + 5), (60, 86, 76), op=1.0, wob=2, rim=0.1)
    stone_wall(P, 380, SH + 5, seed=53, base=(112, 100, 84), x0=-5, x1=300)
    stone_stairs(P, 380, 900, 300, 640, steps=7)
    person(P, 560, 520, 200, coat=OCHRE, profile=-0.2)
    suitcase(P, 440, 560, 1.4)
    lantern(P, 960, 380, 1.0)
    return fin(P, 2522)


def d25a4():
    """O corpo habita o mundo: homem de costas, pés na água rasa, braços relaxados, mar ao pôr do sol."""
    P = Paint(2531)
    backdrop(P, "dusk", 260, sunp=(540, 256, 40), seed=2531, clouds=3)
    P.layer(rect(-5, 430, SW + 5, SH + 5), (96, 138, 148), op=0.95, wob=3, rim=0.1)
    foam(P, 0, SW, 450, n=60, seed=5)
    foam(P, 0, SW, 540, n=50, seed=6)
    P.layer(poly([(-5, 640), (-5, 560), (300, 540), (800, 560), (1085, 540), (1085, 640)]), (190, 170, 130), op=0.97, wob=3, rim=0.2)
    person(P, 540, 590, 250, coat=OCHRE, profile=0.0)
    P.layer(ell(540, 586, 80, 10), (130, 180, 190), op=0.55, wob=2, rim=0, soft=2)
    gulls(P, [(200, 110, 1.0), (280, 90, 0.8), (800, 120, 0.9)], col=(120, 100, 100))
    return fin(P, 2532)


def d25a5():
    """Piscinas naturais de lava: poças azuis entre rochas negras, homem sentado à beira."""
    P = Paint(2541)
    backdrop(P, "day", 240, seed=2541, clouds=2)
    P.layer(rect(-5, 330, SW + 5, SH + 5), (28, 30, 34), op=1.0, wob=2, rim=0.2, vary=0.2)
    rock_pool(P, 280, 430, 190, 36)
    rock_pool(P, 760, 470, 220, 40)
    rock_pool(P, 540, 580, 260, 36)
    foam(P, 0, SW, 300, n=40, seed=4)
    person(P, 540, 536, 190, profile=0.2)
    return fin(P, 2542)


def d25a6():
    """Pausa pequena: banco no jardim com xícara, muro baixo, hortênsias e folhas de bananeira."""
    P = Paint(2551)
    P.vgrad(-5, 260, (92, 148, 172), (232, 226, 200), mask=rect(-5, -5, SW + 5, 260), wob=2, rim=0, vary=0.07)
    P.layer(poly(ridge(260, 50, 113, x0=-30, x1=SW + 30)), (74, 116, 98), op=1.0, wob=3)
    P.layer(rect(-5, 340, SW + 5, SH + 5), (74, 124, 80), op=1.0, wob=2, rim=0.1)
    stone_wall(P, 440, 520, seed=55, base=(120, 108, 90))
    hydrangea(P, 160, 430, 58, col=(92, 132, 214), seed=8)
    hydrangea(P, 940, 430, 58, col=(214, 130, 150), seed=9)
    banana_leaf(P, 70, 560, 0.4, 200, 40)
    bench(P, 560, 600, w=300)
    person(P, 560, 590, 250, sit=True, profile=0.2)
    cup(P, 750, 560, steam=True)
    return fin(P, 2552)


def d25a7():
    """Cozinha à noite: sopa fumegando, pão e vela, janela escura."""
    P = Paint(2561)
    room_bg(P, (36, 58, 66))
    window_frame(P, 700, 70, 980, 330, stars=20, seed=7, cross=True)
    floor(P, 560, (100, 70, 44))
    table(P, 120, 760, 420)
    P.layer(ell(360, 420, 100, 20), (240, 226, 190), op=0.98, wob=1, rim=0.3)
    P.layer(poly([(268, 408), (452, 408), (420, 396), (300, 396)]), (200, 120, 70), op=0.95, wob=1)
    for k in range(3):
        xs = np.linspace(0, 1, 30)
        pts = [(340 + 20 * (k - 1) + 8 * np.sin(t * 9 + k), 380 - t * 90) for t in xs]
        P.layer(shape(lambda d, pts=pts: d.line(pts, fill=255, width=4)), (240, 232, 215), op=0.35, wob=1, rim=0, soft=2.2)
    P.layer(ell(560, 412, 62, 22), (196, 138, 52), op=0.98, wob=1.2, rim=0.3)
    P.layer(ell(560, 400, 56, 14), (222, 164, 70), op=0.9, wob=1.2)
    candle(P, 660, 420, h=50)
    pot_plant(P, 160, 420, 1.0, seed=2)
    P.glow(400, 360, 320, WARM, 0.3)
    return fin(P, 2562)


def d25b():
    """Murdoch: encosta noturna com muitas janelas acesas, cada uma uma vida."""
    P = Paint(2571)
    backdrop(P, "night", 220, moonp=(880, 100, 24), seed=2571)
    hill_houses(P, -10, SW + 10, 240, n=12, seed=101, lit=True)
    hill_houses(P, -10, SW + 10, 360, n=12, seed=102, lit=True, body=(132, 146, 144))
    hill_houses(P, -10, SW + 10, 470, n=10, seed=103, lit=True, body=(150, 156, 148))
    string_lights(P, 60, 1020, 580, sag=26, n=14)
    return fin(P, 2572)


SCENES = {n: f for n, f in globals().items() if n.startswith("d25") and callable(f)}
