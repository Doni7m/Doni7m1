"""Cenas da semana 12-18/10/2026 — parte A (segunda e terça)."""
from lib2 import *


def fin(P, seed):
    return P.finish(top=30, bottom=34, left=45, right=45, feather=70, seed=seed)


# ============================ SEGUNDA — Epicuro (amizade) =====================
def mon_a1():
    """Duas xícaras num muro de pedra ao entardecer."""
    P = Paint(101)
    backdrop(P, "dusk", 360, sunp=(700, 356, 36), seed=101, clouds=3)
    hill_houses(P, -10, 460, 400, n=6, seed=11)
    stone_wall(P, 480, seed=5)
    cup(P, 420, 470, steam=True)
    cup(P, 600, 470, steam=True, col=(226, 200, 150))
    pot_plant(P, 820, 470, 1.0, seed=3)
    gulls(P, [(300, 120, 1.0), (360, 150, 0.8), (880, 110, 0.9)])
    return fin(P, 102)


def mon_a2():
    """Mesa de trabalho: celular aceso, agenda cheia, calendário na parede."""
    P = Paint(111)
    room_bg(P)
    # calendário
    P.layer(rect(110, 70, 330, 280), (236, 226, 200), op=0.98, wob=1, rim=0.3)
    P.layer(rect(110, 70, 330, 100), (176, 98, 62), op=0.98, wob=1)
    for i in range(1, 7):
        P.line([(110 + i * 31, 100), (110 + i * 31, 280)], w=1, alpha=0.35)
    for j in range(1, 6):
        P.line([(110, 100 + j * 36), (330, 100 + j * 36)], w=1, alpha=0.35)
    r = np.random.default_rng(4)
    for _ in range(18):
        cx, cy = 110 + r.integers(0, 7) * 31 + 4, 100 + r.integers(0, 5) * 36 + 6
        P.layer(rect(cx, cy, cx + 24, cy + 10), (196, 138, 52), op=0.85, wob=0.6)
    window_frame(P, 700, 60, 980, 330, stars=18, seed=7)
    table(P, 60, 1020, 440)
    book(P, 330, 436, w=240)
    P.line([(280, 430), (360, 424)], w=3, alpha=0.7)
    phone(P, 620, 434, w=96, lit=True)
    P.layer(rect(660, 400, 668, 436), (246, 236, 214), op=0.5, wob=0.5)
    cup(P, 800, 438, steam=True)
    lamp(P, 910, 440, h=130)
    return fin(P, 112)


def mon_a3():
    """Marina à noite: muitos barcos, um deles partindo."""
    P = Paint(121)
    backdrop(P, "night", 300, moonp=(820, 100, 26), seed=121)
    hill_houses(P, 40, 640, 300, n=7, seed=21)
    for (x, y, s, lit) in [(180, 420, 0.9, True), (430, 450, 1.0, False), (700, 430, 0.85, True), (930, 470, 1.0, True)]:
        boat(P, x, y, s, lit=lit, hull=[(150, 60, 48), (60, 100, 120), (196, 138, 52)][int(x) % 3])
    boat(P, 560, 560, 1.15, lit=True, hull=(150, 60, 48), sail=False)
    stone_wall(P, 596, seed=9, cap=True)
    for x in (140, 460, 780):
        P.layer(rect(x - 3, 520, x + 3, 600), (50, 36, 28), op=0.98, wob=0.6)
        P.glow(x, 514, 40, WARM, 0.9)
        P.glow(x, 514, 120, (255, 200, 110), 0.25)
    return fin(P, 122)


def mon_a4():
    """Pérgula com luzes e uma mesa posta para amigos."""
    P = Paint(131)
    backdrop(P, "night", 250, moonp=(900, 90, 24), seed=131)
    hill_houses(P, 560, 1090, 250, n=4, seed=31)
    # pergula
    for x in (100, 980):
        P.layer(rect(x - 14, 60, x + 14, SH + 5), WOOD_X, op=0.98, wob=1.5, rim=0.25)
    P.layer(rect(60, 56, 1020, 84), WOOD_D, op=0.98, wob=1.5, rim=0.25)
    for x in range(150, 960, 110):
        P.layer(rect(x, 80, x + 12, 120), (90, 60, 36), op=0.9, wob=1)
    leafy(P, 300, 70, 130, (30, 90, 70), n=30, seed=3)
    leafy(P, 760, 70, 150, (28, 84, 66), n=34, seed=4)
    string_lights(P, 100, 980, 96, sag=34, n=12)
    P.glow(540, 380, 300, WARM, 0.35)
    table(P, 160, 920, 450)
    for x in (300, 470, 620):
        cup(P, x, 446, steam=(x != 470), col=[CREAM, (226, 200, 150), (206, 220, 214)][x % 3])
    # pão e jarro
    P.layer(ell(760, 436, 56, 18), (210, 156, 84), op=0.98, wob=1.5, rim=0.3)
    P.layer(poly([(380, 400), (440, 400), (432, 446), (388, 446)]), (84, 124, 160), op=0.97, wob=1, rim=0.3)
    hydrangea(P, 120, 560, 50, seed=9)
    hydrangea(P, 960, 570, 46, col=(160, 120, 190), seed=10)
    return fin(P, 132)


def mon_a5():
    """Beco de pedra ao entardecer: alguém caminha e olha o celular."""
    P = Paint(141)
    P.vgrad(-5, 420, (22, 46, 84), (214, 150, 100), mask=rect(-5, -5, SW + 5, 420), wob=2, rim=0, vary=0.1)
    P.stars(30, 140, seed=14)
    # mar ao fundo
    P.layer(rect(380, 200, 700, 420), (44, 96, 112), op=1.0, wob=1.5, rim=0.2)
    P.glow(540, 260, 120, GOLD, 0.35)
    # paredes
    P.layer(poly([(-5, -5), (380, 150), (380, 470), (-5, 640)]), (84, 72, 62), op=1.0, wob=2, rim=0.3, vary=0.2)
    P.layer(poly([(SW + 5, -5), (700, 150), (700, 470), (SW + 5, 640)]), (96, 82, 70), op=1.0, wob=2, rim=0.3, vary=0.2)
    for (x, y, w, h) in [(120, 200, 70, 90), (130, 400, 70, 80)]:
        P.layer(rect(x, y, x + w, y + h), WARM, op=0.98, wob=1)
        P.glow(x + w / 2, y + h / 2, 70, WARM, 0.6)
    for (x, y, w, h) in [(900, 220, 70, 90), (890, 410, 70, 80)]:
        P.layer(rect(x, y, x + w, y + h), (252, 204, 120), op=0.98, wob=1)
        P.glow(x + w / 2, y + h / 2, 70, WARM, 0.55)
    cobbles(P, 470, seed=15, glow_x=540)
    P.layer(poly([(380, 470), (700, 470), (SW + 5, 645), (-5, 645)]), (150, 126, 96), op=0.55, wob=2, rim=0, soft=6)
    person(P, 540, 600, 250)
    P.glow(560, 478, 40, (140, 190, 240), 0.8)
    P.layer(rect(550, 470, 574, 486), (150, 196, 240), op=0.98, wob=0.5)
    return fin(P, 142)


def mon_a6():
    """Dois caminhantes seguem uma trilha rumo a uma casa acesa na encosta."""
    P = Paint(151)
    backdrop(P, "dusk", 300, sunp=(250, 300, 30), seed=151, clouds=2)
    P.layer(poly(ridge(330, 70, 16)), (30, 64, 70), op=0.98, wob=3)
    P.layer(poly(ridge(420, 60, 17)), (24, 52, 58), op=0.98, wob=3)
    house(P, 760, 330, 96, 64, body=(150, 138, 118), seed=3)
    P.layer(poly([(430, 645), (700, 645), (780, 400), (760, 400)]), (176, 146, 104), op=0.97, wob=3, rim=0.25)
    P.layer(poly([(470, 645), (560, 645), (770, 410), (762, 410)]), (206, 176, 128), op=0.5, wob=3, rim=0, soft=4)
    person(P, 560, 560, 200)
    person(P, 640, 540, 188, coat=(70, 112, 128), hair=(66, 46, 36))
    for x, y in [(110, 520), (230, 570), (900, 560)]:
        hydrangea(P, x, y, 44, seed=int(x))
    return fin(P, 152)


def mon_a7():
    """Janela acesa, duas xícaras e uma cadeira puxada para trás, esperando."""
    P = Paint(161)
    room_bg(P, (12, 40, 52))
    window_frame(P, 150, 90, 560, 420, sky_top=NAVY, sky_bot=(40, 96, 108), stars=24, seed=16)
    P.glow(360, 300, 300, WARM, 0.25)
    table(P, 120, 760, 470)
    cup(P, 360, 464, steam=True)
    cup(P, 520, 464, steam=True, col=(226, 200, 150))
    candle(P, 440, 466, 40)
    chair(P, 860, 645, 340)
    chair(P, 220, 645, 340)
    pot_plant(P, 700, 470, 0.9, seed=6)
    return fin(P, 162)


# ============================ TERÇA — Sêneca (tempo) ==========================
def tue_a1():
    """Ampulheta sobre um parapeito, com o mar ao pôr do sol."""
    P = Paint(201)
    backdrop(P, "dusk", 360, sunp=(540, 358, 40), seed=201, clouds=3, island=(120, 300))
    stone_wall(P, 520, seed=21)
    x = 540
    P.layer(rect(x - 90, 140, x + 90, 164), WOOD_D, op=0.98, wob=1.2, rim=0.3)
    P.layer(rect(x - 90, 496, x + 90, 520), WOOD_D, op=0.98, wob=1.2, rim=0.3)
    glass = [(x - 74, 164), (x + 74, 164), (x + 6, 330), (x + 74, 496), (x - 74, 496), (x - 6, 330)]
    P.layer(poly(glass), (214, 232, 232), op=0.35, wob=1.2, rim=0.4, soft=1.2)
    P.layer(poly([(x - 60, 176), (x + 60, 176), (x + 4, 300), (x - 4, 300)]), (222, 160, 70), op=0.55, wob=1, rim=0.1)
    P.layer(poly([(x - 66, 496), (x + 66, 496), (x + 26, 430), (x - 26, 430)]), (232, 176, 84), op=0.95, wob=1.2, rim=0.2)
    P.layer(rect(x - 2, 300, x + 2, 440), (232, 176, 84), op=0.9, wob=0.6)
    P.line(glass + [glass[0]], w=2, alpha=0.5)
    P.layer(rect(x - 100, 130, x - 90, 530), (96, 66, 40), op=0.98, wob=1.2)
    P.layer(rect(x + 90, 130, x + 100, 530), (96, 66, 40), op=0.98, wob=1.2)
    gulls(P, [(220, 120, 1.0), (300, 160, 0.8), (860, 130, 0.9)])
    return fin(P, 202)


def tue_a2():
    """Relógio grande, celular cheio de notificações, xícaras e papéis na mesa."""
    P = Paint(211)
    room_bg(P, (18, 46, 62))
    clock_round(P, 250, 220, 120, hands=(0.08, 0.5))
    window_frame(P, 700, 80, 980, 330, stars=14, seed=21)
    table(P, 40, 1040, 450)
    phone(P, 560, 440, w=110, lit=True)
    for k, (dx, dy) in enumerate([(-30, -40), (30, -50), (0, -66), (-48, -64), (48, -70)]):
        P.glow(560 + dx, 440 + dy, 12, (240, 120, 100), 0.9)
    cup(P, 330, 444, steam=False)
    cup(P, 800, 444, steam=True, col=(226, 200, 150))
    cup(P, 900, 444, steam=False, col=(206, 220, 214))
    r = np.random.default_rng(6)
    for i in range(5):
        x, y = 140 + i * 40, 436 - i * 6
        P.layer(poly([(x, y), (x + 120, y - 6 + r.uniform(-4, 4)), (x + 124, y + 6), (x + 2, y + 10)]), (236, 228, 204), op=0.95, wob=0.8, rim=0.3)
    P.glow(560, 400, 160, (130, 170, 230), 0.25)
    return fin(P, 212)


def tue_a3():
    """Levada em dia claro: a água corre e leva uma folha."""
    P = Paint(221)
    P.vgrad(-5, 300, (96, 150, 168), (226, 224, 196), mask=rect(-5, -5, SW + 5, 300), wob=2, rim=0, vary=0.08)
    r = np.random.default_rng(22)
    for depth, (col, y0, amp) in enumerate([((90, 128, 120), 230, 40), ((58, 104, 96), 270, 46), ((36, 80, 76), 310, 50)]):
        P.layer(poly(ridge(y0, amp, 80 + depth, step=14)), col, op=0.98, wob=4, rim=0.1)
    P.layer(rect(-5, 380, SW + 5, SH + 5), (40, 84, 70), op=1.0, wob=2, rim=0.1)
    P.layer(poly([(470, 340), (610, 340), (SW + 5, 645), (240, 645)]), (176, 150, 108), op=0.97, wob=3, rim=0.2)
    # canal da levada: da esquerda para a frente
    P.layer(poly([(470, 340), (500, 340), (700, 645), (440, 645)]), (96, 92, 80), op=0.98, wob=2, rim=0.3)
    P.layer(poly([(478, 344), (494, 344), (640, 645), (500, 645)]), (70, 130, 146), op=0.97, wob=1.5, rim=0.2)
    for i in range(16):
        t = i / 15
        P.layer(ell(487 + t * 120 + r.normal(0, 3), 350 + t * 290, 6 + 24 * t, 1.6 + 1.6 * t), (236, 240, 226), op=0.55, wob=0, rim=0, soft=0.8)
    for (x, y, s) in [(520, 400, 0.4), (560, 500, 0.7), (600, 590, 1.0)]:
        P.layer(ell(x, y, 16 * s + 3, 6 * s + 2), (196, 138, 52), op=0.97, wob=0.8, rim=0.2)
    laurel_trunks(P, [(80, 46, 70, (22, 40, 44)), (220, 32, 130, (28, 48, 50)), (950, 50, 60, (22, 40, 44)), (1040, 36, 110, (28, 48, 50))], leaf_col=(34, 96, 72))
    fern(P, 150, 610)
    fern(P, 920, 620)
    person(P, 400, 450, 120)
    return fin(P, 222)


def tue_a4():
    """Escrivaninha à noite: livro aberto, tinteiro e figura de costas diante do mar."""
    P = Paint(231)
    room_bg(P, (14, 44, 58))
    window_frame(P, 560, 50, 1000, 400, stars=26, seed=23)
    P.layer(ell(840, 150, 26, 26), (244, 230, 190), op=0.97, wob=1)
    P.glow(840, 150, 90, GOLD, 0.3)
    P.layer(rect(566, 330, 994, 396), (16, 58, 70), op=0.95, wob=1)
    table(P, 60, 700, 440)
    book(P, 300, 436, w=220)
    P.layer(poly([(430, 436), (460, 436), (456, 420), (434, 420)]), (30, 24, 24), op=0.98, wob=0.6)
    P.line([(445, 420), (470, 380)], w=3, alpha=0.8, color=(210, 200, 170))
    lamp(P, 150, 440, h=130)
    person(P, 400, 645, 330, sit=True)
    return fin(P, 232)


def tue_a5():
    """Banco ao amanhecer, na beira da falésia: livro e termo à espera."""
    P = Paint(241)
    backdrop(P, "dawn", 330, sunp=(300, 326, 38), seed=241, clouds=3, island=(620, 340))
    P.layer(rect(-5, 450, SW + 5, SH + 5), (52, 96, 76), op=1.0, wob=2, rim=0.2, vary=0.2)
    for x in range(30, SW, 60):
        P.layer(poly([(x, 462), (x + 6, 437), (x + 12, 462)]), (74, 124, 90), op=0.8, wob=1)
    bench(P, 540, 560, w=300)
    book(P, 500, 530, w=110, open_=False)
    cup(P, 600, 530, w=56, steam=True)
    gulls(P, [(700, 140, 1.0), (770, 170, 0.8)])
    return fin(P, 242)


def tue_a6():
    """Escadaria de pedra na encosta: alguém descansa no meio do caminho."""
    P = Paint(251)
    P.vgrad(-5, 300, (24, 48, 92), (222, 150, 98), mask=rect(-5, -5, SW + 5, 300), wob=2, rim=0, vary=0.1)
    P.stars(30, 140, seed=25)
    P.layer(poly(ridge(220, 40, 26)), (22, 54, 62), op=0.98, wob=3)
    for i, (x, y, w, h) in enumerate([(80, 250, 80, 58), (230, 280, 70, 52), (780, 250, 84, 60), (920, 290, 76, 54), (640, 210, 70, 50)]):
        house(P, x, y, w, h, body=(124, 132, 130), seed=i)
    stone_stairs(P, 290, 790, 330, 645, steps=9)
    P.layer(rect(250, 330, 290, 645), (96, 82, 70), op=1.0, wob=2, rim=0.3)
    P.layer(rect(790, 330, 830, 645), (96, 82, 70), op=1.0, wob=2, rim=0.3)
    for x in (270, 810):
        lantern(P, x, 300, 0.7)
    person(P, 540, 536, 200, sit=True)
    return fin(P, 252)


def tue_a7():
    """Relógio de bolso sobre o casaco ocre dobrado, no parapeito da varanda."""
    P = Paint(261)
    backdrop(P, "dawn", 300, sunp=(760, 296, 34), seed=261, clouds=2, island=(100, 280))
    P.layer(rect(-5, 430, SW + 5, 470), (118, 80, 48), op=0.98, wob=1.5, rim=0.3)
    P.layer(rect(-5, 470, SW + 5, SH + 5), (30, 56, 72), op=1.0, wob=1, rim=0.2)
    for x in range(30, SW, 92):
        P.layer(rect(x, 470, x + 14, SH + 5), (86, 58, 36), op=0.98, wob=1.5, rim=0.25)
    ochre_coat_folded(P, 440, 432, w=240)
    x, y = 470, 330
    P.line([(x - 6, y - 60), (x - 40, y - 100), (x - 110, y - 70), (x - 170, y + 20), (x - 130, y + 90)], w=3, alpha=0.7, color=(120, 90, 40))
    P.layer(ell(x, y, 66, 66), (220, 180, 90), op=0.98, wob=1, rim=0.3)
    P.layer(ell(x, y, 54, 54), CREAM, op=0.98, wob=0.8, rim=0.2)
    for k in range(12):
        a = k * np.pi / 6
        P.line([(x + np.sin(a) * 42, y - np.cos(a) * 42), (x + np.sin(a) * 50, y - np.cos(a) * 50)], w=2, alpha=0.6)
    P.line([(x, y), (x + 20, y - 30)], w=4, alpha=0.8)
    P.line([(x, y), (x - 34, y + 8)], w=3, alpha=0.8)
    P.layer(rrect(x - 8, y - 82, x + 8, y - 64, 4), (220, 180, 90), op=0.98, wob=0.5)
    pot_plant(P, 880, 432, 1.1, seed=8)
    return fin(P, 262)


SCENES = {n: f for n, f in globals().items() if (n.startswith("mon_") or n.startswith("tue_")) and callable(f)}
