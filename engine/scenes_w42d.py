"""Cenas da semana 12-18/10/2026 — parte D (domingo e as sete imagens únicas B)."""
from lib2 import *


def fin(P, seed):
    return P.finish(top=30, bottom=34, left=45, right=45, feather=70, seed=seed)


# ============================ DOMINGO — Epicteto (o que depende de nós) =======
def sun_a1():
    """Bifurcação: um caminho desce para o mar, outro sobe para uma casa na colina."""
    P = Paint(701)
    backdrop(P, "dusk", 300, sunp=(560, 296, 32), seed=701, clouds=3)
    P.layer(poly(ridge(330, 60, 71)), (36, 76, 76), op=0.98, wob=3)
    house(P, 800, 330, 80, 56, body=(150, 138, 118), seed=4)
    P.layer(rect(-5, 420, SW + 5, SH + 5), (40, 80, 64), op=1.0, wob=2, rim=0.15, vary=0.2)
    P.layer(poly([(480, 645), (640, 645), (620, 520), (560, 470)]), (176, 146, 104), op=0.97, wob=3, rim=0.25)
    P.layer(poly([(560, 470), (620, 520), (800, 430), (790, 410), (700, 440)]), (176, 146, 104), op=0.97, wob=3, rim=0.25)
    P.layer(poly([(560, 470), (590, 480), (320, 440), (230, 420), (250, 410), (330, 424)]), (176, 146, 104), op=0.97, wob=3, rim=0.25)
    # poste de madeira
    P.layer(rect(556, 380, 566, 480), (96, 66, 40), op=0.98, wob=1)
    P.layer(poly([(566, 392), (640, 396), (656, 408), (566, 416)]), (126, 90, 54), op=0.98, wob=1)
    P.layer(poly([(556, 428), (490, 424), (474, 436), (556, 442)]), (126, 90, 54), op=0.98, wob=1)
    person(P, 560, 600, 200)
    return fin(P, 702)


def sun_a2():
    """Madrugada: papéis amassados, relógio marcando três horas e alguém que não consegue largar o pensamento."""
    P = Paint(711)
    room_bg(P, (14, 40, 54))
    clock_round(P, 780, 190, 90, hands=(0.1, 0.0))
    table(P, 60, 1020, 450)
    rr = np.random.default_rng(72)
    for (x, y) in [(150, 440), (240, 446), (330, 438), (700, 444), (800, 440), (900, 446)]:
        pts = [(x + rr.uniform(-26, 26), y - 24 + rr.uniform(-8, 8)) for _ in range(7)]
        P.layer(ell(x, y - 16, 28, 22), (232, 224, 200), op=0.97, wob=2, rim=0.35)
        P.line([(x - 14, y - 22), (x + 6, y - 10), (x - 4, y - 24)], w=1, alpha=0.4)
    lamp(P, 100, 450, h=130)
    cup(P, 1000, 444, steam=False, w=60)
    person(P, 480, 645, 330, sit=True)
    return fin(P, 712)


def sun_a3():
    """Lua enorme sobre o mar; alguém na falésia estende o olhar para o que não alcança."""
    P = Paint(721)
    backdrop(P, "night", 380, moonp=(700, 220, 90), seed=721)
    P.layer(poly([(-10, 520), (300, 500), (500, 540), (560, 645), (-10, 645)]), (10, 24, 36), op=1.0, wob=3, rim=0.3, vary=0.2)
    person(P, 300, 510, 180)
    return fin(P, 722)


def sun_a4():
    """Livro aberto sobre uma rocha à beira do mar, com uma lanterna."""
    P = Paint(731)
    backdrop(P, "dusk", 320, sunp=(300, 316, 34), seed=731, clouds=3, island=(620, 340))
    P.layer(poly([(-10, 470), (400, 440), (860, 470), (1090, 450), (1090, SH + 5), (-10, SH + 5)]), (40, 48, 56), op=1.0, wob=3, rim=0.3, vary=0.2)
    P.layer(poly([(240, 470), (700, 450), (740, 520), (200, 540)]), (96, 92, 90), op=0.98, wob=2, rim=0.3)
    book(P, 440, 466, w=260)
    for k in range(5):
        P.line([(330, 460 + k * 2), (430, 454 + k * 2)], w=1, alpha=0.3)
    lantern(P, 640, 440, 0.8)
    foam(P, 0, SW, 380, n=30, seed=3)
    return fin(P, 732)


def sun_a5():
    """Caderno com duas colunas, caneta e chá: o que posso e o que não posso fazer."""
    P = Paint(741)
    room_bg(P, (16, 44, 58))
    P.layer(rect(-5, 300, SW + 5, SH + 5), (130, 90, 54), op=1.0, wob=1.5, rim=0.2, vary=0.2)
    window_frame(P, 700, 40, 990, 250, stars=14, seed=3)
    P.glow(300, 360, 340, WARM, 0.3)
    P.layer(poly([(190, 330), (880, 330), (940, 560), (130, 560)]), (240, 232, 208), op=0.99, wob=1, rim=0.35)
    P.line([(535, 332), (535, 560)], w=3, alpha=0.6)
    for j in range(7):
        y = 370 + j * 30
        P.line([(205 - j * 4, y), (520, y)], w=1, alpha=0.3)
        P.line([(550, y), (905 + j * 4, y)], w=1, alpha=0.3)
    for j, wd in enumerate([160, 190, 130, 170]):
        P.layer(rect(230 - j * 4, 360 + j * 30, 230 - j * 4 + wd, 368 + j * 30), (196, 138, 52), op=0.8, wob=0.8)
    for j, wd in enumerate([110, 150]):
        P.layer(rect(580 + j * 6, 360 + j * 30, 580 + j * 6 + wd, 368 + j * 30), (60, 100, 130), op=0.8, wob=0.8)
    P.line([(900, 520), (990, 470)], w=5, alpha=0.9, color=(40, 30, 24))
    cup(P, 1000, 330, steam=True, w=60)
    lamp(P, 90, 340, h=120)
    return fin(P, 742)


def sun_a6():
    """Muro de proteção do mar: as ondas batem, a muralha segura e um poste ilumina."""
    P = Paint(751)
    backdrop(P, "storm", 280, seed=751, clouds=5)
    foam(P, 0, SW, 330, n=60, seed=4)
    foam(P, 0, SW, 420, n=50, seed=5)
    P.layer(ell(300, 380, 220, 40), (236, 240, 232), op=0.55, wob=2, rim=0, soft=8)
    P.layer(ell(800, 420, 240, 50), (236, 240, 232), op=0.5, wob=2, rim=0, soft=8)
    stone_wall(P, 470, 645, seed=75, base=(78, 74, 70))
    P.layer(rect(520, 270, 532, 470), (50, 36, 28), op=0.98, wob=0.8)
    lantern(P, 526, 250, 0.9)
    return fin(P, 752)


def sun_a7():
    """Lanternas de papel flutuando sobre o mar da praia escura."""
    P = Paint(761)
    backdrop(P, "night", 300, moonp=(820, 90, 24), seed=761)
    P.vgrad(420, 645, (36, 42, 52), (16, 20, 30), mask=poly([(-5, 500), (SW + 5, 440), (SW + 5, SH + 5), (-5, SH + 5)]), wob=3, rim=0.2, vary=0.16)
    foam(P, 0, SW, 450, n=40, seed=6)
    rr = np.random.default_rng(76)
    for (x, y, s) in [(300, 330, 0.9), (460, 280, 0.7), (580, 360, 1.0), (700, 250, 0.6), (200, 410, 1.1), (840, 340, 0.8), (380, 220, 0.5)]:
        lantern(P, x, y, s * 0.7, g=0.8)
        P.layer(ell(x, 318 + (y - 318) * 0.2 + 70, 24 * s, 3), (244, 214, 140), op=0.4, wob=0, rim=0, soft=1) if False else None
    person(P, 640, 540, 130)
    return fin(P, 762)


# ============================ IMAGENS ÚNICAS (slot B) =========================
def b_mon():
    """Nuvens pesadas sobre o mar e uma fresta de luz iluminando as Desertas."""
    P = Paint(801)
    backdrop(P, "storm", 360, seed=801, clouds=6, island=(480, 520))
    P.glow(740, 340, 240, GOLD, 0.45)
    P.glow(740, 360, 120, (255, 240, 190), 0.4)
    P.layer(poly([(700, 40), (780, 40), (900, 360), (600, 360)]), (255, 232, 170), op=0.14, wob=3, rim=0, soft=10)
    moon_reflection(P, 740, 366, 560, n=22, seed=7)
    return fin(P, 802)


def b_tue():
    """Estrada na encosta ao amanhecer, serpenteando em direção ao mar; alguém de costas segue em frente."""
    P = Paint(811)
    backdrop(P, "dawn", 330, sunp=(560, 326, 40), seed=811, clouds=3, island=(60, 300))
    P.layer(poly(ridge(380, 50, 81)), (60, 108, 90), op=0.98, wob=3)
    P.layer(rect(-5, 470, SW + 5, SH + 5), (52, 98, 72), op=1.0, wob=2, rim=0.15, vary=0.2)
    for k in range(40):
        t = k / 39
        x = 540 + 150 * np.sin(t * 5.0) * (0.25 + t * 0.75)
        y = 640 - t * 250
        P.layer(ell(x, y, 80 * (1 - t) + 10, 20 * (1 - t) + 3), (176, 146, 104), op=0.97, wob=2, rim=0.1, soft=1.2)
    for (x, y) in [(150, 520), (250, 560), (850, 520), (960, 570)]:
        hydrangea(P, x, y, 44, seed=int(x))
    person(P, 600, 600, 220)
    return fin(P, 812)


def b_wed():
    """Bastidor de bordado da Madeira, com o desenho ainda pela metade."""
    P = Paint(821)
    room_bg(P, (50, 92, 100))
    P.layer(rect(-5, 470, SW + 5, SH + 5), (130, 90, 54), op=1.0, wob=1.5, rim=0.2, vary=0.2)
    P.glow(540, 300, 380, WARM, 0.25)
    P.layer(ell(540, 300, 190, 190), (150, 104, 62), op=0.99, wob=1.2, rim=0.35)
    P.layer(ell(540, 300, 174, 174), (244, 236, 214), op=0.99, wob=1, rim=0.3)
    rr = np.random.default_rng(82)
    for k in range(9):
        a = k * 2 * np.pi / 9
        cx, cy = 540 + np.cos(a) * 80 - 30, 300 + np.sin(a) * 80
        if cx > 540:
            continue
        P.layer(ell(cx, cy, 34, 14), (60, 100, 130) if k % 2 else (196, 138, 52), op=0.95, wob=1, rim=0.1)
    for (cx, cy) in [(500, 300), (440, 360), (470, 240)]:
        P.layer(ell(cx, cy, 10, 10), (176, 98, 62), op=0.98, wob=0.6)
    P.line([(540, 300), (640, 260), (680, 440)], w=2, alpha=0.6, color=(176, 98, 62))
    P.layer(rect(630, 244, 636, 300), (210, 200, 180), op=0.98, wob=0.5)
    # tesoura e carretel
    P.layer(ell(820, 520, 20, 14), (176, 98, 62), op=0.98, wob=1)
    P.layer(rect(810, 490, 830, 520), (230, 220, 190), op=0.98, wob=0.8)
    P.layer(poly([(250, 520), (380, 500), (384, 508), (256, 530)]), (150, 150, 156), op=0.98, wob=0.8, rim=0.3)
    return fin(P, 822)


def b_thu():
    """Quarto ao amanhecer: janela clara, cama, chinelos e o casaco ocre numa cadeira."""
    P = Paint(831)
    room_bg(P, (36, 76, 90))
    window_frame(P, 110, 60, 480, 380, sky_top=(76, 124, 146), sky_bot=(244, 216, 160), seed=3, frame=(150, 110, 70))
    far_island(P, 330, (130, 300))
    P.layer(rect(116, 300, 474, 376), (70, 128, 140), op=0.95, wob=1)
    P.glow(300, 300, 280, WARM, 0.25)
    P.layer(rect(-5, 520, SW + 5, SH + 5), (70, 48, 34), op=1.0, wob=1.5, rim=0.2)
    P.layer(rect(640, 330, 1070, 540), (120, 80, 50), op=0.98, wob=1.2, rim=0.3)
    P.layer(rect(640, 380, 1070, 530), (214, 214, 202), op=0.98, wob=1.2, rim=0.3)
    P.layer(poly([(640, 440), (1070, 440), (1070, 530), (640, 530)]), OCHRE, op=0.98, wob=2, rim=0.3)
    P.layer(rrect(660, 380, 780, 430, 20), (236, 232, 218), op=0.98, wob=1.2, rim=0.3)
    P.layer(ell(260, 570, 36, 12), (150, 90, 60), op=0.98, wob=1)
    P.layer(ell(340, 575, 36, 12), (150, 90, 60), op=0.98, wob=1)
    chair(P, 520, 540, 290)
    ochre_coat_folded(P, 520, 420, w=110)
    return fin(P, 832)


def b_fri():
    """Mesa de café da manhã ao sol: xícara, pão, flores e a luz da janela."""
    P = Paint(841)
    room_bg(P, (56, 100, 108))
    window_frame(P, 220, 40, 820, 360, sky_top=(120, 170, 190), sky_bot=(244, 230, 196), seed=3, frame=(150, 110, 70))
    far_island(P, 330, (300, 300))
    P.layer(rect(230, 300, 810, 356), (60, 128, 140), op=0.95, wob=1)
    P.layer(poly([(220, 360), (820, 360), (1000, 640), (60, 640)]), (255, 236, 170), op=0.22, wob=2, rim=0, soft=6)
    table(P, 100, 980, 450)
    cup(P, 420, 446, steam=True)
    P.layer(ell(600, 428, 66, 22), (214, 160, 90), op=0.98, wob=1.5, rim=0.3)
    P.layer(ell(600, 420, 54, 14), (232, 190, 120), op=0.7, wob=1.5)
    P.layer(poly([(750, 446), (810, 446), (800, 380), (760, 380)]), (84, 124, 160), op=0.98, wob=1, rim=0.3)
    hydrangea(P, 780, 340, 60, col=(150, 120, 196), seed=3)
    P.layer(rect(280, 440, 330, 448), (232, 224, 200), op=0.98, wob=0.6)
    return fin(P, 842)


def b_sat():
    """Duas encostas com casas acesas frente a frente e um barco com luz no meio do mar."""
    P = Paint(851)
    backdrop(P, "night", 380, seed=851)
    P.layer(poly([(-10, 420), (180, 330), (330, 300), (420, 380), (440, 470), (-10, 470)]), (14, 36, 48), op=0.98, wob=2)
    P.layer(poly([(1090, 420), (900, 330), (760, 300), (680, 380), (660, 470), (1090, 470)]), (14, 36, 48), op=0.98, wob=2)
    for i, (x, y) in enumerate([(40, 360), (130, 340), (220, 320), (300, 340), (90, 410), (210, 400)]):
        house(P, x, y, 50, 36, body=(100, 118, 122), seed=i + 7)
    for i, (x, y) in enumerate([(950, 360), (860, 340), (780, 330), (700, 360), (980, 410), (860, 400)]):
        house(P, x, y, 50, 36, body=(100, 118, 122), seed=i + 17)
    boat(P, 540, 500, 0.9, lit=True)
    P.glow(540, 520, 160, WARM, 0.35)
    moon_reflection(P, 540, 520, 600, n=10, seed=8)
    return fin(P, 852)


def b_sun():
    """Uma concha numa rocha à beira do mar, no fim do dia."""
    P = Paint(861)
    backdrop(P, "dusk", 330, sunp=(780, 326, 34), seed=861, clouds=3)
    P.layer(poly([(-10, 470), (300, 430), (700, 450), (1090, 440), (1090, SH + 5), (-10, SH + 5)]), (40, 46, 54), op=1.0, wob=3, rim=0.3, vary=0.2)
    P.layer(poly([(260, 470), (500, 440), (820, 470), (860, 560), (230, 570)]), (92, 90, 90), op=0.98, wob=2, rim=0.3)
    cx, cy = 540, 400
    P.layer(ell(cx, cy, 120, 80), (234, 210, 178), op=0.99, wob=1.5, rim=0.35)
    for k in range(7):
        P.layer(ell(cx - 6 + k * 3, cy + 4, 108 - k * 14, 70 - k * 9), (226 - k * 6, 196 - k * 6, 160 - k * 5), op=0.7, wob=1, rim=0.3)
    for k in range(9):
        a = -0.9 + k * 0.22
        P.line([(cx + 10, cy + 10), (cx + np.cos(a) * 118, cy + np.sin(a) * 76)], w=2, alpha=0.35, color=(120, 80, 56))
    P.layer(ell(cx + 60, cy + 54, 54, 30), (206, 168, 128), op=0.98, wob=1.2, rim=0.3)
    foam(P, 0, SW, 360, n=26, seed=3)
    return fin(P, 862)


SCENES = {n: f for n, f in globals().items() if (n.startswith("sun_") or n.startswith("b_")) and callable(f)}
