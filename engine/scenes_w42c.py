"""Cenas da semana 12-18/10/2026 — parte C (sexta e sábado)."""
from lib2 import *


def fin(P, seed):
    return P.finish(top=30, bottom=34, left=45, right=45, feather=70, seed=seed)


# ============================ SEXTA — Aristóteles (coragem) ===================
def fri_a1():
    """Molhe de pedra avançando para o mar: alguém na ponta, ao anoitecer."""
    P = Paint(501)
    backdrop(P, "dusk", 330, sunp=(780, 326, 34), seed=501, clouds=3)
    P.layer(poly([(430, 380), (650, 380), (800, 645), (280, 645)]), (112, 100, 84), op=1.0, wob=2, rim=0.3, vary=0.18)
    P.layer(poly([(430, 380), (650, 380), (655, 392), (425, 392)]), (150, 138, 118), op=1.0, wob=1.5)
    r = np.random.default_rng(51)
    for i in range(10):
        t = i / 9
        y = 400 + t * 220
        P.layer(rect(430 - t * 150, y, 650 + t * 150, y + 3), (70, 62, 52), op=0.55, wob=0.6)
    P.glow(540, 372, 40, WARM, 0.8)
    P.layer(rect(536, 330, 544, 380), (50, 36, 28), op=0.98, wob=0.6)
    lantern(P, 540, 318, 0.5)
    foam(P, 260, 420, 470, n=14, seed=5)
    foam(P, 660, 840, 470, n=14, seed=6)
    person(P, 540, 380, 140)
    return fin(P, 502)


def fri_a2():
    """Beco à noite: a porta entreaberta deixa escapar luz; alguém hesita diante dela."""
    P = Paint(511)
    room_bg(P, (14, 38, 52))
    P.layer(rect(-5, -5, SW + 5, 480), (66, 58, 52), op=1.0, wob=2, rim=0.3, vary=0.2)
    rr = np.random.default_rng(52)
    for _ in range(70):
        x, y = rr.uniform(0, SW), rr.uniform(10, 470)
        P.layer(rect(x, y, x + rr.uniform(30, 70), y + rr.uniform(10, 18)), tuple(int(v * rr.uniform(0.82, 1.12)) for v in (78, 68, 60)), op=0.5, wob=1, rim=0.2, soft=0.8)
    door(P, 430, 150, 650, 480, lit=True, ajar=0.35)
    P.glow(540, 480, 280, WARM, 0.5)
    cobbles(P, 480, seed=53, glow_x=540)
    P.layer(poly([(430, 480), (650, 480), (880, 645), (200, 645)]), (252, 206, 120), op=0.35, wob=3, rim=0, soft=6)
    person(P, 540, 600, 260)
    lantern(P, 160, 220, 0.8)
    return fin(P, 512)


def fri_a3():
    """Mar bravo contra a falésia; ao alto, num mirante, uma figura pequena."""
    P = Paint(521)
    backdrop(P, "storm", 300, seed=521, clouds=5)
    cliff(P, "right", top=200, seed=52, col=(14, 30, 40), reach=520)
    cliff(P, "left", top=420, seed=53, col=(18, 36, 46), reach=360)
    foam(P, 0, 700, 430, n=70, seed=7)
    foam(P, 0, 560, 560, n=60, seed=8)
    P.layer(ell(250, 340, 140, 30), (236, 240, 232), op=0.45, wob=2, rim=0, soft=6)
    # mirante
    P.layer(rect(700, 196, 940, 214), (96, 66, 40), op=0.98, wob=1)
    for x in range(710, 940, 40):
        P.layer(rect(x, 160, x + 6, 200), (96, 66, 40), op=0.98, wob=0.8)
    P.layer(rect(700, 158, 940, 166), (96, 66, 40), op=0.98, wob=0.8)
    person(P, 820, 198, 76)
    return fin(P, 522)


def fri_a4():
    """Muro de pedra solta em construção num socalco; pedras empilhadas ao lado."""
    P = Paint(531)
    backdrop(P, "dusk", 300, sunp=(240, 296, 30), seed=531, clouds=2)
    P.layer(poly(ridge(330, 50, 54)), (40, 82, 74), op=0.98, wob=3)
    P.layer(rect(-5, 400, SW + 5, SH + 5), (60, 100, 70), op=1.0, wob=2, rim=0.15, vary=0.2)
    # muro parcial
    r = np.random.default_rng(55)
    for row in range(5):
        y = 440 + row * 26
        x = 80 + (row % 2) * 30
        wmax = 720 - row * 30
        while x < wmax:
            w = r.uniform(70, 120)
            P.layer(rect(x, y, x + w - 4, y + 24), tuple(int(v * r.uniform(0.84, 1.12)) for v in (110, 100, 86)), op=0.98, wob=1.2, rim=0.3, soft=0.8)
            x += w
    # pedras soltas
    for (x, y, w, h) in [(780, 560, 90, 40), (860, 520, 70, 34), (840, 566, 80, 36), (930, 566, 70, 32), (700, 584, 60, 28)]:
        P.layer(ell(x, y, w / 2, h / 2), tuple(int(v * r.uniform(0.9, 1.15)) for v in (118, 108, 92)), op=0.98, wob=1.2, rim=0.3)
    person(P, 640, 540, 250)
    return fin(P, 532)


def fri_a5():
    """Pedras para atravessar o riacho: um pé já no primeiro passo."""
    P = Paint(541)
    backdrop(P, "day", 260, seed=541, clouds=2, sea_bottom=290)
    P.layer(poly(ridge(280, 50, 56)), (80, 124, 108), op=0.98, wob=3)
    P.layer(rect(-5, 330, SW + 5, SH + 5), (52, 100, 76), op=1.0, wob=2, rim=0.15, vary=0.2)
    P.layer(poly([(-10, 420), (SW + 10, 400), (SW + 10, 540), (-10, 560)]), (60, 130, 146), op=0.98, wob=3, rim=0.2)
    rr = np.random.default_rng(57)
    for i in range(18):
        P.layer(ell(rr.uniform(0, SW), rr.uniform(430, 540), rr.uniform(30, 80), 2.2), (236, 240, 226), op=0.5, wob=0, rim=0, soft=1)
    stones = [(160, 560), (330, 520), (500, 490), (690, 470), (870, 450)]
    for (x, y) in stones:
        P.layer(ell(x, y, 66, 26), (118, 108, 94), op=0.99, wob=1.5, rim=0.3)
        P.layer(ell(x, y - 6, 58, 18), (150, 140, 120), op=0.8, wob=1.5, rim=0.1)
    person(P, 330, 520, 230)
    for x, y in [(100, 620), (960, 600)]:
        fern(P, x, y)
    return fin(P, 542)


def fri_a6():
    """Pequena ponte sobre a ravina ao fim do dia, com uma lanterna esperando do outro lado."""
    P = Paint(551)
    backdrop(P, "dusk", 280, sunp=(540, 276, 34), seed=551, clouds=2)
    P.layer(poly([(-10, 340), (330, 360), (400, 470), (360, SH + 5), (-10, SH + 5)]), (22, 44, 52), op=1.0, wob=3, rim=0.3, vary=0.2)
    P.layer(poly([(SW + 10, 340), (750, 360), (680, 470), (720, SH + 5), (SW + 10, SH + 5)]), (22, 44, 52), op=1.0, wob=3, rim=0.3, vary=0.2)
    P.vgrad(400, 645, (30, 64, 72), (8, 22, 36), mask=rect(380, 400, 700, SH + 5), wob=2, rim=0, vary=0.1)
    P.layer(poly([(300, 360), (780, 360), (780, 380), (300, 380)]), (110, 80, 50), op=0.99, wob=1.5, rim=0.3)
    for x in range(310, 780, 40):
        P.layer(rect(x, 336, x + 6, 360), (96, 66, 40), op=0.98, wob=0.8)
    P.layer(rect(300, 334, 780, 342), (96, 66, 40), op=0.98, wob=0.8)
    P.line([(300, 380), (540, 392), (780, 380)], w=3, alpha=0.5)
    lantern(P, 800, 320, 0.8)
    person(P, 380, 358, 120)
    leafy(P, 120, 360, 80, (24, 70, 64), n=16, seed=3)
    leafy(P, 980, 360, 80, (24, 70, 64), n=16, seed=4)
    return fin(P, 552)


def fri_a7():
    """Piscina natural de rocha vulcânica ao amanhecer: alguém à beira, prestes a entrar."""
    P = Paint(561)
    backdrop(P, "dawn", 280, sunp=(780, 276, 34), seed=561, clouds=3, island=(80, 300))
    P.layer(poly([(-10, 340), (SW + 10, 330), (SW + 10, SH + 5), (-10, SH + 5)]), (36, 40, 48), op=1.0, wob=3, rim=0.3, vary=0.2)
    P.layer(poly([(120, 400), (940, 396), (980, 500), (900, 600), (200, 604), (80, 500)]), (86, 172, 176), op=0.98, wob=3, rim=0.3)
    P.layer(poly([(160, 420), (900, 416), (930, 480), (880, 570), (230, 572), (140, 490)]), (120, 196, 192), op=0.5, wob=3, rim=0, soft=8)
    foam(P, 0, SW, 316, n=34, seed=9)
    for pts, col in [([(40, 470), (160, 420), (200, 520), (60, 600)], (56, 60, 68)),
                     ([(900, 420), (1060, 440), (1070, 560), (940, 580)], (56, 60, 68))]:
        P.layer(poly(pts), col, op=0.95, wob=3, rim=0.3)
    person(P, 520, 420, 190, coat=OCHRE)
    return fin(P, 562)


# ============================ SÁBADO — Espinosa (tristeza e saudade) ==========
def sat_a1():
    """Uma única luz distante numa encosta, do outro lado do mar escuro."""
    P = Paint(601)
    backdrop(P, "night", 340, seed=601)
    P.layer(poly([(520, 340), (700, 296), (880, 270), (1090, 300), (1090, 346), (520, 346)]), (16, 40, 52), op=0.98, wob=2)
    house(P, 760, 296, 40, 30, body=(70, 90, 96), seed=2)
    P.glow(780, 320, 40, WARM, 0.9)
    P.glow(780, 320, 140, (255, 200, 110), 0.25)
    moon_reflection(P, 780, 350, 520, n=18, seed=3)
    cliff(P, "left", top=470, seed=61, col=(8, 22, 34), reach=600)
    person(P, 190, 500, 110, sit=True)
    return fin(P, 602)


def sat_a2():
    """Mala no canto, casaco ocre e um cartão-postal na parede."""
    P = Paint(611)
    room_bg(P, (16, 42, 56))
    # moldura
    P.layer(rect(380, 90, 700, 330), (110, 78, 50), op=0.98, wob=1.2, rim=0.3)
    P.vgrad(104, 316, (60, 110, 130), (240, 214, 160), mask=rect(394, 104, 686, 316), wob=1, rim=0.2)
    P.layer(rect(394, 230, 686, 316), (44, 100, 118), op=0.98, wob=1)
    P.layer(poly([(394, 316), (460, 250), (540, 316)]), (176, 98, 62), op=0.95, wob=1)
    P.layer(ell(560, 170, 18, 18), (252, 226, 160), op=0.98, wob=0.8)
    P.glow(540, 330, 260, WARM, 0.2)
    P.layer(rect(-5, 520, SW + 5, SH + 5), (60, 40, 30), op=1.0, wob=1.5, rim=0.2)
    suitcase(P, 380, 560, 1.7)
    ochre_coat_folded(P, 380, 410, w=200)
    P.layer(rect(700, 470, 940, 530), (110, 80, 52), op=0.98, wob=1, rim=0.3)
    pot_plant(P, 820, 470, 0.9, seed=5)
    return fin(P, 612)


def sat_a3():
    """Noite de chuva na janela: gotas, luzes borradas e uma lâmpada refletida."""
    P = Paint(621)
    room_bg(P, (12, 34, 48))
    window_frame(P, 150, 50, 930, 470, sky_top=(20, 40, 64), sky_bot=(40, 70, 90), seed=3)
    rr = np.random.default_rng(62)
    for _ in range(30):
        x, y = rr.uniform(170, 910), rr.uniform(300, 450)
        P.glow(x, y, rr.uniform(10, 22), rr.choice([0, 1]) * np.array([1, 1, 1]) * 0 + np.array([255, 210, 130]), 0.5)
    for _ in range(90):
        x, y = rr.uniform(160, 920), rr.uniform(60, 460)
        P.layer(ell(x, y, 2.2, rr.uniform(8, 22)), (200, 220, 236), op=rr.uniform(0.35, 0.7), wob=0, rim=0, soft=0.7)
    P.glow(780, 160, 120, (240, 220, 160), 0.18)
    P.layer(rect(120, 470, 960, 500), (96, 66, 40), op=0.98, wob=1.5, rim=0.3)
    pot_plant(P, 260, 470, 1.2, seed=8)
    cup(P, 640, 466, steam=True)
    candle(P, 780, 468, 36)
    return fin(P, 622)


def sat_a4():
    """Sol da manhã entrando pela janela e iluminando hortênsias num vaso."""
    P = Paint(631)
    room_bg(P, (58, 100, 108))
    window_frame(P, 600, 50, 980, 380, sky_top=(120, 170, 190), sky_bot=(244, 230, 196), seed=3, frame=(150, 110, 70))
    far_island(P, 340, (640, 280))
    P.layer(rect(610, 320, 970, 376), (60, 128, 140), op=0.95, wob=1)
    P.layer(poly([(600, 380), (980, 380), (560, 640), (-10, 640)]), (255, 236, 170), op=0.28, wob=2, rim=0, soft=6)
    table(P, 140, 700, 470)
    P.layer(poly([(320, 466), (420, 466), (406, 380), (334, 380)]), (84, 124, 160), op=0.98, wob=1, rim=0.3)
    hydrangea(P, 370, 330, 70, seed=7)
    hydrangea(P, 300, 360, 40, col=(150, 120, 196), seed=8)
    cup(P, 560, 466, steam=True)
    return fin(P, 632)


def sat_a5():
    """Varanda ao entardecer: alguém de costas conversa por telefone com quem está longe."""
    P = Paint(641)
    backdrop(P, "dusk", 330, sunp=(260, 326, 30), seed=641, clouds=3)
    hill_houses(P, 600, 1090, 340, n=5, seed=65)
    P.layer(rect(-5, 450, SW + 5, 486), (118, 80, 48), op=0.98, wob=1.5, rim=0.3)
    P.layer(rect(-5, 486, SW + 5, SH + 5), (30, 56, 72), op=1.0, wob=1, rim=0.2)
    for x in range(30, SW, 92):
        P.layer(rect(x, 486, x + 14, SH + 5), (86, 58, 36), op=0.98, wob=1.5, rim=0.25)
    person(P, 520, 640, 380, sit=False)
    P.layer(poly([(0, 450), (SW, 450), (SW, 486), (0, 486)]), (118, 80, 48), op=0.0)
    P.glow(556, 262, 50, (140, 190, 240), 0.8)
    P.layer(rect(548, 246, 566, 284), (150, 196, 240), op=0.98, wob=0.5)
    pot_plant(P, 160, 450, 1.0, seed=4)
    pot_plant(P, 900, 450, 1.0, seed=5)
    return fin(P, 642)


def sat_a6():
    """Porta aberta e luz quente: alguém chega à casa de quem acolhe."""
    P = Paint(651)
    backdrop(P, "night", 300, moonp=(180, 90, 24), seed=651)
    P.layer(rect(-5, 330, SW + 5, SH + 5), (28, 52, 56), op=1.0, wob=2, rim=0.1)
    P.layer(rect(560, 140, SW + 5, SH + 5), (98, 88, 78), op=1.0, wob=2, rim=0.3, vary=0.2)
    P.layer(poly([(520, 150), (800, 60), (SW + 5, 60), (SW + 5, 150)]), (60, 40, 36), op=0.98, wob=2, rim=0.3)
    door(P, 700, 260, 880, 600, lit=True, ajar=0.0)
    P.glow(790, 560, 300, WARM, 0.5)
    P.layer(poly([(700, 600), (880, 600), (1000, 645), (560, 645)]), (252, 206, 120), op=0.42, wob=3, rim=0, soft=6)
    cobbles(P, 590, seed=66, glow_x=790)
    P.layer(rect(660, 590, 920, 600), (150, 126, 96), op=0.9, wob=1)
    hydrangea(P, 960, 540, 50, seed=6)
    person(P, 420, 600, 230)
    lantern(P, 360, 480, 0.6)
    return fin(P, 652)


def sat_a7():
    """Carta sendo escrita à noite: papel, caneta, selo e a luz do abajur."""
    P = Paint(661)
    room_bg(P, (14, 42, 56))
    window_frame(P, 640, 60, 980, 340, stars=18, seed=3)
    P.layer(ell(830, 150, 22, 22), (244, 230, 190), op=0.97, wob=1)
    P.glow(830, 150, 80, GOLD, 0.3)
    table(P, 60, 1020, 450)
    letter(P, 440, 440, w=300, tilt=-0.02, stamp=False)
    P.line([(300, 428), (560, 424)], w=2, alpha=0.5)
    P.line([(300, 440), (520, 436)], w=2, alpha=0.5)
    P.line([(300, 452), (440, 449)], w=2, alpha=0.5)
    P.line([(560, 400), (640, 360)], w=4, alpha=0.8, color=(210, 200, 170))
    letter(P, 780, 430, w=170, tilt=0.04, stamp=True)
    lamp(P, 190, 450, h=140)
    cup(P, 900, 444, steam=True)
    return fin(P, 662)


SCENES = {n: f for n, f in globals().items() if (n.startswith("fri_") or n.startswith("sat_")) and callable(f)}
