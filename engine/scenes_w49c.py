"""Cenas 27-28/11/2026: Epicuro (r27), Espinosa (r28)."""
import re
from lib4 import *

NIGHT_ROOM = (22, 44, 56)
WARM_ROOM = (70, 46, 36)


def steam(P, x, y, n=3):
    for k in range(n):
        xs = np.linspace(0, 1, 30)
        pts = [(x - 6 + 12 * (k - 1) + 8 * np.sin(t * 9 + k), y - t * 64) for t in xs]
        P.layer(shape(lambda d, pts=pts: d.line(pts, fill=255, width=4)), (240, 232, 215), op=0.35, wob=1, rim=0, soft=2.2)


def bowl(P, x, y, w=120, soup=True, hot=True):
    P.layer(poly([(x - w / 2, y - 36), (x + w / 2, y - 36), (x + w / 2 - 20, y), (x - w / 2 + 20, y)]), CREAM, op=0.98, wob=1.2, rim=0.3)
    P.layer(ell(x, y - 36, w / 2, 9), (130, 90, 56) if not soup else (206, 120, 60), op=0.98, wob=1)
    P.layer(ell(x - w * 0.12, y - 37, w * 0.2, 4), (240, 190, 120), op=0.6, wob=1, soft=1.5)
    P.layer(ell(x, y + 3, w * 0.5, 5), (8, 22, 44), op=0.3, wob=0, rim=0, soft=3)
    if hot:
        steam(P, x, y - 44)


def loaf(P, x, y, w=160):
    P.layer(ell(x, y - w * 0.15, w / 2, w * 0.17), (190, 128, 70), op=0.98, wob=1.5, rim=0.3)
    P.layer(ell(x - w * 0.1, y - w * 0.2, w * 0.3, w * 0.07), (226, 170, 98), op=0.6, wob=1.5, rim=0, soft=2)
    for k in range(3):
        P.line([(x - w * 0.22 + k * w * 0.2, y - w * 0.27), (x - w * 0.12 + k * w * 0.2, y - w * 0.14)], w=3, alpha=0.45, color=(110, 64, 30))
    P.layer(ell(x, y + 2, w * 0.5, 5), (8, 22, 44), op=0.3, wob=0, rim=0, soft=3)


def bottle(P, x, y, h=120, col=(40, 90, 70)):
    P.layer(rrect(x - 17, y - h * 0.62, x + 17, y, 8), col, op=0.98, wob=1, rim=0.3)
    P.layer(rect(x - 6, y - h, x + 6, y - h * 0.6), col, op=0.98, wob=0.8)
    P.layer(rect(x - 17, y - h * 0.4, x + 17, y - h * 0.18), (236, 224, 190), op=0.95, wob=0.6)


def note(P, x, y, w=90, col=(240, 232, 208), tilt=0.0):
    h = w * 0.8
    pts = [(x - w / 2, y - h / 2), (x + w / 2, y - h / 2 + w * tilt), (x + w / 2, y + h / 2 + w * tilt), (x - w / 2, y + h / 2)]
    P.layer(poly(pts), col, op=0.98, wob=0.8, rim=0.3)
    for k in range(3):
        P.line([(x - w * 0.34, y - h * 0.18 + k * 12), (x + w * 0.3, y - h * 0.18 + k * 12 + w * tilt * 0.5)], w=1, alpha=0.4)


def wall_around(P, x0, y0, x1, y1, col):
    """Parede ao redor de uma janela (x0..x1, y0..y1) sobre o fundo ja pintado."""
    P.layer(rect(-5, -5, SW + 5, y0, ), col, op=1.0, wob=1.5, rim=0.2, vary=0.15)
    P.layer(rect(-5, y1, SW + 5, SH + 5), col, op=1.0, wob=1.5, rim=0.2, vary=0.15)
    P.layer(rect(-5, y0 - 4, x0, y1 + 4), col, op=1.0, wob=1.5, rim=0.2, vary=0.15)
    P.layer(rect(x1, y0 - 4, SW + 5, y1 + 4), col, op=1.0, wob=1.5, rim=0.2, vary=0.15)


def frame_only(P, x0, y0, x1, y1, frame=(110, 78, 50), cross=True):
    t = 10
    for a, b, c, d in [(x0 - t, y0 - t, x0, y1 + t), (x1, y0 - t, x1 + t, y1 + t), (x0 - t, y0 - t, x1 + t, y0), (x0 - t, y1, x1 + t, y1 + t + 4)]:
        P.layer(rect(a, b, c, d), frame, op=0.97, wob=1.2, rim=0.25)
    if cross:
        P.layer(rect((x0 + x1) / 2 - 4, y0, (x0 + x1) / 2 + 4, y1), frame, op=0.97, wob=1.2, rim=0.25)


def orange_tree(P, x, yb, h=330, seed=3):
    P.layer(poly([(x - 14, yb), (x - 8, yb - h * 0.55), (x + 8, yb - h * 0.55), (x + 14, yb)]), (70, 50, 36), op=0.98, wob=1.5, rim=0.3)
    leafy(P, x, yb - h * 0.72, h * 0.42, (44, 108, 70), n=34, seed=seed)
    r = np.random.default_rng(seed)
    for _ in range(11):
        a = r.uniform(0, 6.28)
        d = r.uniform(0.1, 0.8) * h * 0.4
        P.layer(ell(x + np.cos(a) * d, yb - h * 0.72 + np.sin(a) * d * 0.8, 11, 11), (236, 150, 48), op=0.97, wob=0.8, rim=0.3)


# ============================================================ 27/11 Epicuro: jantar simples
def r27a1():
    P = Paint(9501)
    room_bg(P, NIGHT_ROOM)
    floor(P, 600, (62, 44, 34))
    window_frame(P, 90, 60, 350, 330, sky_top=NAVY, sky_bot=(30, 82, 96), stars=26, seed=7)
    table(P, 70, 1010, 420)
    P.layer(rect(250, 424, 850, 436), (232, 222, 196), op=0.95, wob=1, rim=0.2)  # toalha/caminho
    candle(P, 540, 424, h=80)
    P.glow(540, 380, 260, WARM, 0.55)
    bowl(P, 400, 428, 140)
    bowl(P, 690, 428, 140)
    loaf(P, 545, 434, 170)
    cup(P, 850, 426, steam=False)
    bottle(P, 160, 426, 100)
    return fin(P, 9502)


def r27a2():
    P = Paint(9511)
    room_bg(P, WARM_ROOM)
    floor(P, 520, (50, 34, 26))
    window_frame(P, 440, 60, 640, 300, sky_top=NAVY, sky_bot=(60, 80, 90), stars=14, seed=4)
    table(P, 250, 830, 420)
    candle(P, 540, 424, h=70)
    P.glow(540, 380, 300, WARM, 0.6)
    bowl(P, 400, 432, 130)
    bowl(P, 690, 432, 130)
    loaf(P, 540, 436, 110)
    chair(P, 190, 640, 330)
    chair(P, 890, 640, 330)
    person(P, 170, 640, 300, sit=True, coat=OCHRE, profile=0.5)
    person(P, 910, 640, 290, sit=True, coat=BLUE_COAT, profile=-0.5)
    return fin(P, 9512)


def r27a3():
    P = Paint(9521)
    room_bg(P, (20, 40, 50))
    floor(P, 560, (56, 42, 32))
    # esquerda: excesso (prateleira abarrotada, caixas, relogios)
    bookshelf(P, 30, 60, 470, 560, rows=6, seed=5)
    bookshelf(P, 470, 120, 600, 560, rows=5, seed=8)
    suitcase(P, 150, 600, 1.0)
    suitcase(P, 300, 610, 0.8, col=(90, 80, 60))
    stack_papers(P, 410, 600, n=6, w=120)
    tv(P, 240, 330, 380, 420)
    clock_round(P, 120, 120, r=40, hands=(0.1, 0.5))
    P.layer(rect(-5, -5, 640, SH + 5), (14, 30, 40), op=0.22, wob=3, rim=0, soft=18)
    # direita: mesa simples, luz quente
    P.glow(840, 380, 330, WARM, 0.5)
    table(P, 700, 1010, 440)
    bowl(P, 800, 448, 120)
    loaf(P, 910, 452, 130)
    candle(P, 860, 444, h=60)
    chair(P, 790, 640, 300)
    person(P, 770, 640, 300, sit=True, coat=OCHRE, profile=-0.5)
    return fin(P, 9522)


def r27a4():
    P = Paint(9531)
    backdrop(P, "day", 230, seed=9531, clouds=2)
    terrace(P, 250, 400, (84, 130, 86), seed=14)
    terrace(P, 340, 300, (70, 116, 80), seed=15)
    stone_wall(P, 520, SH + 5, seed=12, base=(98, 90, 80))
    orange_tree(P, 300, 470, 380, seed=6)
    hydrangea(P, 120, 500, 54, seed=2)
    hydrangea(P, 190, 520, 46, col=(176, 120, 190), seed=3)
    hydrangea(P, 930, 505, 56, seed=5)
    bench(P, 640, 600, 380)
    person(P, 580, 600, 250, coat=OCHRE, sit=True, profile=0.5)
    person(P, 670, 600, 240, coat=RUST_COAT, sit=True, profile=-0.3)
    person(P, 760, 600, 245, coat=SAGE_COAT, sit=True, profile=-0.5)
    gulls(P, [(820, 120, 1.0)])
    return fin(P, 9532)


def r27a5():
    P = Paint(9541)
    backdrop(P, "dusk", 200, sunp=(220, 200, 26), seed=9541)
    hill_houses(P, -10, 520, 210, n=5, seed=91, lit=True)
    stone_wall(P, 300, SH + 5, seed=22, base=(78, 74, 68), cap=False)
    P.layer(rect(560, 220, 940, 520), (170, 150, 112), op=0.98, wob=2, rim=0.3, vary=0.12)  # fachada
    P.layer(poly([(540, 220), (750, 150), (960, 220)]), (150, 70, 52), op=0.98, wob=2, rim=0.3)
    door(P, 690, 290, 810, 520, lit=True, ajar=0.28)
    P.glow(750, 520, 260, WARM, 0.55)
    person(P, 750, 520, 175, coat=RUST_COAT, profile=0.0)  # anfitriao na soleira
    cobbles(P, 520, glow_x=700)
    stone_stairs(P, 600, 900, 520, 585, steps=2)
    lantern(P, 590, 330, 1.0)
    pot_plant(P, 920, 530, 1.1, seed=2)
    person(P, 390, 630, 300, coat=OCHRE, profile=0.4)
    loaf(P, 452, 506, 84)   # pao sob o braço
    bottle(P, 335, 470, 90)
    return fin(P, 9542)


def r27a6():
    P = Paint(9551)
    backdrop(P, "night", 330, moonp=(880, 110, 22), seed=9551)
    hill_houses(P, -10, SW + 10, 250, n=11, seed=95, lit=True)
    hill_houses(P, -10, SW + 10, 330, n=9, seed=96, lit=True, body=(132, 146, 144))
    wall_around(P, 180, 60, 900, 460, NIGHT_ROOM)
    frame_only(P, 180, 60, 900, 460, cross=True)
    P.layer(rect(120, 462, 960, 490), (110, 78, 50), op=0.98, wob=1.5, rim=0.3)
    floor(P, 520, (50, 36, 28))
    cup(P, 280, 462, steam=True)
    pot_plant(P, 800, 462, 0.9, seed=4)
    lamp(P, 1000, 600, h=150, g=0.5)
    px = 560
    person(P, px, 660, 330, coat=OCHRE, profile=0.7)
    # telefone junto a orelha
    phone(P, px + 34, 356, w=34, lit=True, tilt=3)
    return fin(P, 9552)


def r27a7():
    P = Paint(9561)
    backdrop(P, "night", 260, moonp=(140, 90, 22), seed=9561)
    P.layer(rect(-5, 420, SW + 5, SH + 5), (24, 54, 52), op=1.0, wob=2, rim=0.2, vary=0.2)
    P.layer(rect(250, 190, 840, 600), (176, 156, 116), op=0.98, wob=2, rim=0.3, vary=0.12)
    P.layer(poly([(220, 195), (545, 100), (870, 195)]), (150, 70, 52), op=0.98, wob=2, rim=0.3)
    # janela iluminada com mesa e duas silhuetas
    x0, y0, x1, y1 = 340, 270, 750, 500
    P.vgrad(y0, y1, (255, 220, 140), (236, 168, 80), mask=rect(x0, y0, x1, y1), wob=1, rim=0.3)
    P.glow(545, 400, 420, WARM, 0.6)
    for cx, col in [(450, (60, 40, 34)), (650, (50, 44, 54))]:
        P.layer(ell(cx, 372, 26, 30), col, op=0.97, wob=0.8)
        P.layer(poly([(cx - 62, y1 - 40), (cx - 28, 405), (cx + 28, 405), (cx + 62, y1 - 40)]), col, op=0.97, wob=0.8)
    P.layer(rect(x0, 462, x1, 478), (126, 84, 50), op=0.98, wob=0.8)
    candle(P, 545, 462, h=44)
    P.layer(ell(480, 456, 30, 8), CREAM, op=0.98, wob=0.6)
    P.layer(ell(610, 456, 30, 8), CREAM, op=0.98, wob=0.6)
    frame_only(P, x0, y0, x1, y1, frame=(96, 66, 40), cross=False)
    P.layer(rect(330, y1 + 4, 760, y1 + 20), (110, 100, 88), op=0.98, wob=1.2)
    hydrangea(P, 200, 560, 62, seed=7)
    hydrangea(P, 880, 560, 62, col=(176, 120, 190), seed=9)
    pot_plant(P, 330, 590, 1.2, seed=5)
    lantern(P, 840, 400, 0.8)
    return fin(P, 9562)


def r27b():
    P = Paint(9571)
    backdrop(P, "dawn", 300, sunp=(700, 280, 36), seed=9571, clouds=2)
    boat(P, 330, 372, 0.5)
    gulls(P, [(560, 120, 1.0), (640, 150, 0.8)])
    wall_around(P, 110, 40, 970, 470, (104, 124, 114))
    frame_only(P, 110, 40, 970, 470, frame=(236, 226, 200), cross=False)
    P.layer(rect(60, 466, 1030, 500), (216, 192, 150), op=0.99, wob=1.5, rim=0.3)
    P.layer(rect(60, 500, 1030, SH + 5), (150, 104, 62), op=1.0, wob=2, rim=0.2)
    cup(P, 450, 468, steam=True)
    loaf(P, 620, 470, 150)
    pot_plant(P, 850, 468, 1.2, seed=2)
    P.glow(540, 480, 400, WARM, 0.25)
    return fin(P, 9572)


# ============================================================ 28/11 Espinosa: o que da e tira forca
def r28a1():
    P = Paint(9601)
    backdrop(P, "dawn", 260, sunp=(240, 230, 40), seed=9601, clouds=2)
    P.layer(poly(ridge(300, 30, 3, x0=-20, x1=SW + 20) + [(SW + 20, SH + 5), (-20, SH + 5)]), (84, 130, 86), op=1.0, wob=3, rim=0.2)
    # direita: sombra e mata fechada
    P.layer(rect(560, -5, SW + 5, SH + 5), (14, 30, 44), op=0.55, wob=6, rim=0, soft=40)
    for x, h in [(720, 300), (820, 360), (930, 320), (1030, 380)]:
        tree_pine(P, x, 400, h, col=(16, 52, 50))
    # caminho em bifurcacao
    P.layer(poly([(430, SH + 5), (650, SH + 5), (600, 500), (548, 440), (470, 500)]), (206, 180, 130), op=0.98, wob=2, rim=0.3)
    P.layer(poly([(548, 440), (400, 380), (180, 330), (210, 322), (420, 360), (580, 420)]), (222, 196, 140), op=0.98, wob=1.5, rim=0.3)
    P.layer(poly([(548, 440), (700, 390), (860, 350), (880, 358), (720, 410), (580, 450)]), (96, 90, 84), op=0.98, wob=1.5, rim=0.3)
    P.glow(220, 330, 200, WARM, 0.45)
    lantern(P, 160, 300, 0.8)
    person(P, 548, 560, 230, coat=OCHRE, profile=0.0)
    gulls(P, [(380, 140, 1.0), (460, 110, 0.8)])
    return fin(P, 9602)


def r28a2():
    P = Paint(9611)
    # direita: rua fria
    room_bg(P, (22, 38, 52))
    P.layer(rect(520, -5, SW + 5, SH + 5), (28, 48, 62), op=1.0, wob=2, rim=0, vary=0.2)
    hill_houses(P, 520, SW + 10, 260, n=5, seed=77, lit=False, body=(80, 96, 104))
    cobbles(P, 470, seed=8, base=(60, 76, 86))
    rain(P, 530, SW, 0, 600, n=90, seed=4)
    lantern(P, 960, 330, 0.9, g=0.25)
    person(P, 790, 620, 280, coat=OCHRE, profile=-0.5)
    P.layer(rect(520, -5, SW + 5, SH + 5), (40, 60, 80), op=0.25, wob=2, rim=0, soft=6)
    # esquerda: casa acolhedora
    P.layer(rect(-5, -5, 520, SH + 5), WARM_ROOM, op=1.0, wob=2, rim=0, vary=0.18)
    P.layer(rect(-5, 470, 520, SH + 5), (60, 40, 30), op=1.0, wob=2, rim=0.2)
    P.glow(260, 330, 420, WARM, 0.55)
    framed(P, 60, 70, 210, 200)
    lamp(P, 440, 470, h=170, g=0.8)
    table(P, 60, 420, 440, legs=True)
    cup(P, 200, 444, steam=True)
    book(P, 320, 438, 100)
    chair(P, 120, 620, 300)
    person(P, 250, 640, 300, sit=True, coat=OCHRE, profile=0.4)
    # emenda
    P.layer(rect(512, -5, 530, SH + 5), (60, 40, 30), op=1.0, wob=1.5, rim=0.3)
    return fin(P, 9612)


def r28a3():
    P = Paint(9621)
    room_bg(P, (40, 62, 70))
    floor(P, 580, (74, 52, 36))
    window_frame(P, 90, 60, 420, 360, sky_top=(120, 170, 190), sky_bot=(246, 226, 180), stars=0, seed=3)
    P.layer(poly([(90, 360), (420, 360), (760, 600), (360, 600)]), (255, 236, 180), op=0.22, wob=2, rim=0, soft=8)
    P.glow(260, 220, 320, WARM, 0.35)
    table(P, 300, 880, 440)
    book(P, 540, 440, 260)
    paper_tag(P, 660, 430, 70, tilt=0.1)
    paper_tag(P, 440, 428, 60, tilt=-0.15)
    P.line([(580, 436), (640, 430)], w=3, alpha=0.8, color=(40, 30, 24))
    cup(P, 780, 438, steam=True)
    chair(P, 960, 640, 330)
    person(P, 950, 640, 300, sit=True, coat=OCHRE, profile=-0.6)
    pot_plant(P, 330, 440, 1.0, kind="sprout")
    return fin(P, 9622)


def r28a4():
    P = Paint(9631)
    backdrop(P, "dawn", 300, sunp=(540, 290, 58), seed=9631, clouds=1)
    P.glow(540, 290, 520, WARM, 0.35)
    cols = [((64, 118, 134), 340, 8, 11), ((52, 106, 124), 400, 16, 12), ((40, 92, 112), 470, 28, 13), ((28, 74, 96), 560, 44, 14)]
    for col, y, amp, sd in cols:
        P.layer(poly(ridge(y, amp, sd, x0=-30, x1=SW + 30, step=30) + [(SW + 30, SH + 5), (-30, SH + 5)]), col, op=0.98, wob=3, rim=0.3)
        foam(P, 40, SW - 40, y - amp * 0.6, n=int(6 + amp * 0.5), seed=sd)
    boat(P, 330, 350, 0.45)
    gulls(P, [(780, 150, 1.0), (850, 120, 0.8), (700, 180, 0.7)])
    return fin(P, 9632)


def r28a5():
    P = Paint(9641)
    room_bg(P, (24, 46, 56))
    floor(P, 590, (62, 44, 34))
    window_frame(P, 780, 60, 1000, 300, sky_top=(24, 48, 92), sky_bot=(226, 152, 98), stars=0, seed=2)
    table(P, 90, 920, 440)
    book(P, 500, 436, 170)
    warm = [(238, 188, 96), (226, 150, 80), (240, 206, 130)]
    cool = [(150, 176, 196), (128, 146, 170), (176, 190, 200)]
    for i in range(3):
        note(P, 160 + i * 100, 470 - 12 + (i % 2) * 6, 82, warm[i], tilt=-0.04 + i * 0.03)
        note(P, 700 + i * 100, 470 - 12 + ((i + 1) % 2) * 6, 82, cool[i], tilt=0.04 - i * 0.03)
    lamp(P, 400, 440, h=130, g=0.7)
    cup(P, 620, 434, steam=False)
    chair(P, 300, 640, 330)
    person(P, 300, 640, 290, sit=True, coat=OCHRE, profile=0.4)
    return fin(P, 9642)


def r28a6():
    P = Paint(9651)
    backdrop(P, "dusk", 250, sunp=(780, 240, 34), seed=9651, clouds=1)
    hill_houses(P, -10, 460, 255, n=5, seed=97, lit=True)
    stone_wall(P, 430, SH + 5, seed=31, base=(92, 84, 76))
    floor(P, 470, (92, 84, 74))
    bench(P, 540, 600, 400)
    person(P, 480, 600, 255, coat=OCHRE, sit=True, profile=0.5)
    person(P, 590, 600, 245, coat=BLUE_COAT, sit=True, profile=-0.6)
    P.line([(530, 470), (555, 455)], w=4, alpha=0.5, color=(70, 44, 18))
    hydrangea(P, 130, 560, 56, seed=4)
    hydrangea(P, 960, 560, 50, col=(176, 120, 190), seed=6)
    lantern(P, 860, 380, 1.1)
    gulls(P, [(900, 120, 1.0)])
    return fin(P, 9652)


def r28a7():
    P = Paint(9661)
    backdrop(P, "dusk", 220, sunp=(300, 210, 30), seed=9661)
    terrace(P, 260, 360, (74, 120, 82), seed=21)
    terrace(P, 340, 300, (60, 104, 74), seed=22)
    terrace(P, 420, 260, (52, 92, 68), seed=23)
    house(P, 680, 170, 190, 130, roof=OCHRE_D, body=(176, 166, 138), lit=True, seed=3)
    P.glow(775, 280, 240, WARM, 0.55)
    P.layer(poly([(380, SH + 5), (640, SH + 5), (590, 520), (700, 420), (760, 350), (790, 300), (770, 300), (730, 340), (640, 410), (520, 500)]),
            (216, 190, 140), op=0.98, wob=2, rim=0.3)
    for x, y in [(560, 470), (690, 400), (330, 520)]:
        lantern(P, x, y, 0.6)
    tree_pine(P, 900, 420, 280)
    tree_pine(P, 140, 440, 240)
    person(P, 520, 600, 250, coat=OCHRE, profile=0.5)
    return fin(P, 9662)


def r28b():
    P = Paint(9671)
    backdrop(P, "dawn", 300, sunp=(840, 290, 38), seed=9671, clouds=2)
    boat(P, 260, 372, 0.5)
    cliff(P, "left", top=420, seed=52, col=(24, 56, 62), reach=300)
    gulls(P, [(700, 130, 1.0)])
    pa = person(P, 450, 680, 330, coat=OCHRE, profile=0.5)
    person(P, 610, 680, 310, coat=BLUE_COAT, profile=-0.5)
    P.layer(poly([(390, 480), (420, 438), (520, 396), (610, 408), (700, 436), (730, 490), (720, 560), (680, 572), (640, 560), (590, 574), (540, 560), (490, 574), (440, 560), (400, 572), (380, 560)]), (176, 98, 62), op=0.98, wob=2, rim=0.3, vary=0.14)
    for k in range(4):
        P.line([(392 + k * 3, 470 + k * 24), (722 - k * 3, 470 + k * 24)], w=5, alpha=0.4, color=(236, 214, 160))
    stone_wall(P, 590, SH + 5, seed=41, base=(98, 90, 80))
    cup(P, 330, 580, steam=True)
    cup(P, 780, 580, steam=True)
    return fin(P, 9672)


SCENES = {n: f for n, f in globals().items() if re.match(r"^r\d\d", n) and callable(f)}
