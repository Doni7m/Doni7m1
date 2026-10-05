"""Cenas da semana 12-18/10/2026 — parte B (quarta e quinta)."""
from lib2 import *


def fin(P, seed):
    return P.finish(top=30, bottom=34, left=45, right=45, feather=70, seed=seed)


# ============================ QUARTA — Simone Weil (atenção) ==================
def wed_a1():
    """Farol na falésia: o facho de luz escolhe um ponto no mar escuro."""
    P = Paint(301)
    backdrop(P, "night", 330, seed=301)
    P.glow(300, 300, 280, (250, 230, 170), 0.18)
    # facho
    P.layer(poly([(830, 190), (-10, 250), (-10, 360), (830, 200)]), (255, 240, 180), op=0.22, wob=2, rim=0, soft=8)
    P.layer(poly([(830, 192), (-10, 285), (-10, 320), (830, 198)]), (255, 244, 200), op=0.20, wob=2, rim=0, soft=5)
    cliff(P, "right", top=400, seed=31, col=(10, 28, 40), reach=520)
    # torre
    P.layer(poly([(790, 440), (870, 440), (856, 220), (804, 220)]), (226, 218, 198), op=0.98, wob=1.5, rim=0.3)
    P.layer(poly([(800, 400), (860, 400), (862, 370), (798, 370)]), (176, 98, 62), op=0.9, wob=1)
    P.layer(poly([(804, 300), (856, 300), (858, 270), (802, 270)]), (176, 98, 62), op=0.9, wob=1)
    P.layer(rect(796, 200, 864, 222), (60, 44, 36), op=0.98, wob=1)
    P.layer(rect(808, 170, 852, 202), (255, 238, 170), op=0.98, wob=0.8)
    P.glow(830, 186, 70, (255, 238, 170), 0.9)
    P.layer(poly([(800, 170), (830, 140), (860, 170)]), (60, 44, 36), op=0.98, wob=1)
    return fin(P, 302)


def wed_a2():
    """Duas pessoas num muro ao entardecer; uma delas olha o celular."""
    P = Paint(311)
    backdrop(P, "dusk", 340, sunp=(300, 336, 32), seed=311, clouds=2)
    hill_houses(P, 560, 1090, 380, n=5, seed=33)
    stone_wall(P, 500, seed=34)
    person(P, 560, 500, 290, sit=True)
    person(P, 720, 500, 270, coat=(70, 112, 128), hair=(66, 46, 36), sit=True)
    P.glow(600, 330, 60, (140, 190, 240), 0.7)
    P.layer(rect(586, 322, 616, 344), (150, 196, 240), op=0.98, wob=0.5)
    return fin(P, 312)


def wed_a3():
    """Bule a vapor e duas xícaras à espera, num dia claro."""
    P = Paint(321)
    room_bg(P, (50, 92, 100))
    window_frame(P, 330, 60, 760, 400, sky_top=(120, 170, 190), sky_bot=(236, 228, 202), seed=3, frame=(150, 110, 70))
    far_island(P, 340, (420, 300))
    P.layer(rect(340, 330, 750, 396), (50, 116, 132), op=0.95, wob=1)
    table(P, 120, 960, 460)
    # bule
    P.layer(ell(520, 420, 62, 44), (206, 220, 214), op=0.98, wob=1.2, rim=0.3)
    P.layer(rect(500, 366, 540, 380), (186, 200, 196), op=0.98, wob=0.8)
    P.layer(ell(520, 364, 10, 6), (176, 98, 62), op=0.98, wob=0.6)
    P.layer(poly([(572, 410), (622, 390), (628, 398), (578, 428)]), (206, 220, 214), op=0.98, wob=1)
    P.layer(rrect(444, 396, 464, 436, 8), (186, 200, 196), op=0.95, wob=1)
    for k in range(3):
        xs = np.linspace(0, 1, 30)
        pts = [(632 + 8 * np.sin(t * 9 + k), 388 - t * 60) for t in xs]
        P.layer(shape(lambda d, pts=pts: d.line(pts, fill=255, width=4)), (240, 232, 215), op=0.35, wob=1, rim=0, soft=2.2)
    cup(P, 300, 456, steam=False)
    cup(P, 740, 456, steam=False, col=(226, 200, 150))
    chair(P, 130, 645, 320)
    chair(P, 960, 645, 320)
    return fin(P, 322)


def wed_a4():
    """Uma pessoa de costas observa de perto uma hortênsia, à beira da levada."""
    P = Paint(331)
    backdrop(P, "day", 280, seed=331, clouds=2)
    P.layer(poly(ridge(300, 60, 36)), (70, 116, 100), op=0.98, wob=3)
    P.layer(poly(ridge(380, 60, 37)), (44, 92, 80), op=0.98, wob=3)
    P.layer(rect(-5, 470, SW + 5, SH + 5), (44, 92, 72), op=1.0, wob=2, rim=0.15)
    P.layer(poly([(-5, 540), (SW + 5, 520), (SW + 5, 560), (-5, 580)]), (170, 146, 108), op=0.97, wob=2, rim=0.2)
    hydrangea(P, 760, 400, 130, col=(92, 132, 214), seed=5)
    hydrangea(P, 930, 440, 70, col=(150, 120, 196), seed=6)
    person(P, 420, 580, 280)
    fern(P, 120, 600)
    return fin(P, 332)


def wed_a5():
    """Esplanada de dia: guarda-sol, duas xícaras e o celular virado para baixo."""
    P = Paint(341)
    backdrop(P, "day", 300, seed=341, clouds=3)
    hill_houses(P, 40, 520, 300, n=5, seed=41, lit=False, body=(180, 176, 160))
    stone_wall(P, 440, 520, seed=42)
    P.layer(rect(-5, 520, SW + 5, SH + 5), (176, 150, 112), op=1.0, wob=2, rim=0.15, vary=0.15)
    # guarda-sol
    P.layer(rect(536, 110, 544, 520), (96, 66, 40), op=0.98, wob=1)
    P.layer(poly([(240, 190), (540, 70), (840, 190), (790, 200), (700, 186), (540, 200), (380, 186), (290, 200)]), (232, 214, 170), op=0.98, wob=1.5, rim=0.3)
    P.layer(poly([(380, 186), (540, 70), (460, 190)]), (190, 120, 70), op=0.9, wob=1.2)
    P.layer(poly([(620, 190), (540, 70), (700, 186)]), (190, 120, 70), op=0.9, wob=1.2)
    table(P, 340, 740, 470, legs=True, ybot=620)
    cup(P, 450, 466, steam=True)
    cup(P, 640, 466, steam=True, col=(226, 200, 150))
    phone(P, 545, 462, w=70, face_down=True)
    chair(P, 260, 600, 300)
    chair(P, 820, 600, 300)
    return fin(P, 342)


def wed_a6():
    """Amanhecer na beira da falésia: alguém sentado, só respirando."""
    P = Paint(351)
    backdrop(P, "dawn", 330, sunp=(560, 326, 40), seed=351, clouds=3, island=(60, 300))
    P.layer(poly([(-10, 440), (300, 456), (640, 470), (760, 520), (820, 645), (-10, 645)]), (22, 44, 52), op=1.0, wob=3, rim=0.3, vary=0.2)
    P.layer(poly([(-10, 440), (300, 456), (640, 470), (650, 484), (300, 474), (-10, 460)]), (92, 136, 100), op=0.95, wob=2, rim=0.2)
    P.layer(poly([(60, 520), (260, 500), (360, 580), (120, 640)]), (40, 70, 76), op=0.85, wob=3, rim=0.3)
    person(P, 520, 478, 230, sit=True)
    gulls(P, [(780, 150, 1.0), (840, 180, 0.8)])
    return fin(P, 352)


def wed_a7():
    """Dois caminhantes na floresta de louro, com raios de luz entre os troncos."""
    P = Paint(361)
    P.vgrad(-5, 340, (30, 74, 84), (214, 190, 140), mask=rect(-5, -5, SW + 5, 340), wob=2, rim=0, vary=0.1)
    r = np.random.default_rng(37)
    for depth, (col, y0, amp) in enumerate([((70, 110, 100), 240, 40), ((46, 88, 84), 290, 50), ((28, 64, 66), 330, 55)]):
        P.layer(poly(ridge(y0, amp, 90 + depth, step=14)), col, op=0.98, wob=4, rim=0.1)
        P.layer(ell(r.uniform(200, 800), y0 + 50, 300, 24), (230, 232, 214), op=0.22, wob=0, rim=0, soft=14)
    P.layer(rect(-5, 420, SW + 5, SH + 5), (26, 58, 58), op=1.0, wob=2, rim=0.1)
    P.layer(poly([(500, 330), (560, 330), (860, 645), (240, 645)]), (150, 126, 90), op=0.97, wob=3, rim=0.2)
    for x0 in (330, 520, 700):
        P.layer(poly([(x0, 0), (x0 + 60, 0), (x0 + 260, 560), (x0 + 120, 560)]), (255, 230, 160), op=0.12, wob=3, rim=0, soft=8)
    laurel_trunks(P, [(80, 46, 70, (22, 40, 44)), (210, 34, 120, (28, 48, 50)), (960, 52, 60, (22, 40, 44)), (1040, 38, 100, (28, 48, 50)), (700, 22, 220, (40, 62, 60))])
    fern(P, 130, 600)
    person(P, 500, 560, 230)
    person(P, 590, 545, 215, coat=(70, 112, 128), hair=(66, 46, 36))
    return fin(P, 362)


# ============================ QUINTA — Hannah Arendt (recomeços) ==============
def thu_a1():
    """Um broto atravessa a pedra vulcânica ao amanhecer."""
    P = Paint(401)
    backdrop(P, "dawn", 300, sunp=(760, 296, 34), seed=401, clouds=3, island=(80, 300))
    P.layer(poly([(-10, 430), (180, 390), (420, 410), (640, 392), (860, 420), (1090, 386), (1090, SH + 5), (-10, SH + 5)]), (40, 44, 52), op=1.0, wob=3, rim=0.3, vary=0.22)
    for pts, col in [([(40, 480), (200, 440), (300, 520), (120, 580)], (60, 64, 72)),
                     ([(700, 470), (900, 440), (980, 540), (760, 580)], (56, 60, 68)),
                     ([(300, 560), (520, 520), (700, 580), (460, 640)], (70, 72, 78))]:
        P.layer(poly(pts), col, op=0.9, wob=3, rim=0.3)
    # fissura
    P.layer(poly([(520, 480), (560, 430), (580, 440), (548, 500), (560, 580), (520, 580)]), (20, 22, 28), op=1.0, wob=1.5, rim=0.2)
    P.layer(rect(550, 340, 558, 450), (70, 130, 84), op=0.98, wob=0.8)
    P.layer(ell(520, 350, 46, 16), (84, 156, 98), op=0.98, wob=1, rim=0.3)
    P.layer(ell(594, 330, 52, 18), (98, 170, 108), op=0.98, wob=1, rim=0.3)
    P.layer(ell(548, 304, 30, 12), (112, 184, 118), op=0.98, wob=1, rim=0.3)
    P.glow(560, 330, 120, WARM, 0.3)
    return fin(P, 402)


def thu_a2():
    """Cômodo fechado: porta trancada, chave sobre a mesa e uma luz fraca."""
    P = Paint(411)
    room_bg(P, (14, 40, 54))
    door(P, 380, 90, 700, 500, lit=False)
    P.layer(rect(380, 90, 700, 500), (50, 36, 30), op=0.95, wob=1.2, rim=0.3)
    for k in range(2):
        P.layer(rect(410 + k * 140, 120, 520 + k * 140 - 20, 300), (64, 46, 38), op=0.9, wob=1, rim=0.2)
        P.layer(rect(410 + k * 140, 330, 520 + k * 140 - 20, 470), (64, 46, 38), op=0.9, wob=1, rim=0.2)
    P.layer(ell(660, 310, 10, 10), GOLD, op=0.98, wob=0.6)
    P.glow(540, 560, 220, WARM, 0.18)
    P.layer(rect(0, 520, SW, SH + 5), (60, 40, 30), op=1.0, wob=1.5, rim=0.2)
    table(P, 760, 1040, 480, legs=True)
    # chave
    kx, ky = 900, 474
    P.layer(ell(kx - 30, ky - 6, 14, 14), GOLD, op=0.98, wob=0.8, rim=0.3)
    P.layer(ell(kx - 30, ky - 6, 6, 6), (150, 104, 62), op=0.98, wob=0.5)
    P.layer(rect(kx - 18, ky - 9, kx + 46, ky - 3), GOLD, op=0.98, wob=0.8)
    P.layer(rect(kx + 32, ky - 3, kx + 38, ky + 10), GOLD, op=0.98, wob=0.6)
    P.layer(rect(kx + 42, ky - 3, kx + 46, ky + 8), GOLD, op=0.98, wob=0.6)
    candle(P, 800, 478, 30)
    ochre_coat_folded(P, 190, 520, w=150)
    return fin(P, 412)


def thu_a3():
    """Pegadas na praia de seixos escuros ao entardecer."""
    P = Paint(421)
    backdrop(P, "dusk", 300, sunp=(700, 296, 34), seed=421, clouds=3, island=(60, 340))
    P.vgrad(380, 640, (60, 70, 76), (28, 34, 44), mask=poly([(-5, 460), (SW + 5, 380), (SW + 5, SH + 5), (-5, SH + 5)]), wob=3, rim=0.2, vary=0.16)
    foam(P, 0, SW, 410, n=50, seed=3)
    r = np.random.default_rng(42)
    for i in range(12):
        t = i / 11
        x = 600 - t * 220 + (14 if i % 2 else -14)
        y = 440 + t * 150
        P.layer(ell(x, y, 12 + 8 * t, 6 + 4 * t), (14, 18, 26), op=0.55, wob=1, rim=0)
    for _ in range(40):
        P.layer(ell(r.uniform(0, SW), r.uniform(470, 600), r.uniform(6, 16), r.uniform(3, 7)), (96, 102, 106), op=0.5, wob=1)
    person(P, 820, 470, 120)
    return fin(P, 422)


def thu_a4():
    """Barco de pesca saindo do porto com o sol nascendo."""
    P = Paint(431)
    backdrop(P, "dawn", 340, sunp=(620, 336, 44), seed=431, clouds=3, island=(760, 280))
    P.layer(poly([(-10, 500), (-10, 330), (260, 360), (360, 420), (400, 500)]), (44, 70, 70), op=1.0, wob=3, rim=0.3, vary=0.2)
    P.layer(rect(-5, 480, 460, 520), (134, 124, 108), op=1.0, wob=1.5, rim=0.3)
    P.layer(rect(70, 270, 100, 480), (232, 226, 206), op=0.98, wob=1.2, rim=0.3)
    P.layer(rect(62, 250, 108, 274), (60, 44, 36), op=0.98, wob=1)
    P.layer(poly([(66, 250), (86, 224), (106, 250)]), (176, 98, 62), op=0.98, wob=1)
    boat(P, 640, 450, 1.2, hull=(150, 60, 48), sail=True)
    boat(P, 900, 400, 0.5, hull=(60, 100, 120))
    gulls(P, [(500, 130, 1.0), (560, 160, 0.8), (440, 170, 0.7)])
    return fin(P, 432)


def thu_a5():
    """Janela aberta de manhã: caderno, caneta e um raio de sol sobre a mesa."""
    P = Paint(441)
    room_bg(P, (56, 100, 108))
    window_frame(P, 140, 60, 560, 400, sky_top=(120, 170, 190), sky_bot=(240, 228, 196), seed=4, frame=(150, 110, 70), cross=False)
    far_island(P, 340, (140, 300))
    P.layer(rect(150, 330, 550, 396), (60, 128, 140), op=0.95, wob=1)
    P.layer(poly([(150, 60), (80, 80), (80, 420), (150, 400)]), (156, 108, 62), op=0.98, wob=1.2, rim=0.3)
    P.layer(poly([(560, 60), (630, 80), (630, 420), (560, 400)]), (156, 108, 62), op=0.98, wob=1.2, rim=0.3)
    P.layer(poly([(150, 400), (560, 400), (840, 640), (-10, 640)]), (255, 236, 170), op=0.22, wob=2, rim=0, soft=6)
    table(P, 120, 1000, 470)
    book(P, 420, 466, w=240)
    P.line([(380, 458), (470, 452)], w=2, alpha=0.5)
    P.layer(rect(500, 456, 576, 462), (60, 80, 120), op=0.98, wob=0.6)
    cup(P, 700, 466, steam=True)
    pot_plant(P, 880, 470, 1.0, seed=9)
    return fin(P, 442)


def thu_a6():
    """Escada ao anoitecer: quem está embaixo ilumina o caminho de quem sobe."""
    P = Paint(451)
    P.vgrad(-5, 280, (22, 44, 84), (200, 140, 98), mask=rect(-5, -5, SW + 5, 280), wob=2, rim=0, vary=0.1)
    P.stars(26, 120, seed=45)
    P.layer(poly(ridge(220, 40, 46)), (22, 54, 62), op=0.98, wob=3)
    for i, (x, y, w, h) in enumerate([(100, 240, 80, 58), (250, 270, 70, 52), (800, 240, 84, 60), (930, 280, 76, 54)]):
        house(P, x, y, w, h, body=(124, 132, 130), seed=i + 3)
    stone_stairs(P, 280, 800, 300, 645, steps=9)
    P.layer(rect(240, 300, 280, 645), (96, 82, 70), op=1.0, wob=2, rim=0.3)
    P.layer(rect(800, 300, 840, 645), (96, 82, 70), op=1.0, wob=2, rim=0.3)
    person(P, 540, 400, 120, coat=(70, 112, 128), hair=(66, 46, 36))
    person(P, 560, 600, 250)
    lantern(P, 500, 470, 0.9)
    return fin(P, 452)


def thu_a7():
    """Vaso com broto na varanda ao amanhecer, com um regador ao lado."""
    P = Paint(461)
    backdrop(P, "dawn", 300, sunp=(240, 296, 34), seed=461, clouds=2, island=(600, 360))
    P.layer(rect(-5, 430, SW + 5, 468), (118, 80, 48), op=0.98, wob=1.5, rim=0.3)
    P.layer(rect(-5, 468, SW + 5, SH + 5), (30, 56, 72), op=1.0, wob=1, rim=0.2)
    for x in range(30, SW, 92):
        P.layer(rect(x, 468, x + 14, SH + 5), (86, 58, 36), op=0.98, wob=1.5, rim=0.25)
    pot_plant(P, 540, 432, 1.7, kind="sprout")
    # regador
    P.layer(poly([(760, 432), (860, 432), (850, 360), (770, 360)]), (110, 150, 156), op=0.98, wob=1.2, rim=0.3)
    P.layer(poly([(770, 392), (700, 340), (692, 350), (762, 410)]), (110, 150, 156), op=0.98, wob=1)
    P.line([(770, 360), (800, 320), (850, 360)], w=4, alpha=0.7)
    pot_plant(P, 250, 432, 1.0, seed=3)
    return fin(P, 462)


SCENES = {n: f for n, f in globals().items() if (n.startswith("wed_") or n.startswith("thu_")) and callable(f)}
