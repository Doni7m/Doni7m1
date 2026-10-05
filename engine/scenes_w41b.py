"""Cenas semana 06-11/10/2026 — parte B (quinta e sexta)."""
from lib2 import *
from scenes_w41a import fin, inv


# ================= QUINTA A — Sócrates (examinar com gentileza) =================
def thu_a1():
    P = Paint(1501)
    room_bg(P, (16, 42, 56))
    window_frame(P, 600, 70, 940, 400, sky_top=NAVY, sky_bot=(30, 82, 96), stars=40, seed=3)
    table(P, 120, 700, 470)
    lamp(P, 200, 470, h=120)
    book(P, 460, 468, 150)
    person(P, 400, 645, 330, sit=True)
    return fin(P, 1502)


def thu_a2():
    P = Paint(1511)
    backdrop(P, "day", 280, seed=1511, clouds=2)
    P.layer(poly(ridge(300, 40, 31)), (60, 108, 92), op=0.98, wob=3)
    P.layer(rect(-5, 380, SW + 5, SH + 5), (140, 126, 106), op=1.0, wob=2, rim=0.2, vary=0.2)
    stone_stairs(P, 300, 780, 400, 640, steps=7)
    person(P, 540, 440, 150)
    return fin(P, 1512)


def thu_a3():
    P = Paint(1521)
    room_bg(P, (26, 56, 66))
    table(P, 100, 980, 440)
    lamp(P, 820, 440, h=150)
    book(P, 460, 438, 200)
    cup(P, 280, 440, 76)
    P.layer(rect(380, 400, 470, 410), (240, 230, 206), op=0.97, wob=1)
    pot_plant(P, 160, 440, 1.0, seed=3)
    return fin(P, 1522)


def thu_a4():
    P = Paint(1531)
    backdrop(P, "day", 300, seed=1531, clouds=2, island=(700, 300))
    P.layer(rect(-5, 400, SW + 5, SH + 5), (52, 98, 72), op=1.0, wob=2, rim=0.15, vary=0.2)
    bench(P, 480, 560, 300)
    person(P, 480, 548, 170, sit=True)
    hydrangea(P, 160, 540, 54, seed=6)
    hydrangea(P, 900, 560, 50, seed=9)
    return fin(P, 1532)


def thu_a5():
    P = Paint(1541)
    backdrop(P, "storm", 340, seed=1541, clouds=6)
    P.layer(poly([(-10, 520), (400, 500), (560, 560), (640, 645), (-10, 645)]), (24, 40, 46), op=1.0, wob=3, rim=0.3, vary=0.2)
    person(P, 240, 520, 190, coat=(130, 108, 80))
    P.glow(800, 300, 220, (255, 232, 170), 0.35)
    return fin(P, 1542)


def thu_a6():
    P = Paint(1551)
    P.vgrad(-5, 300, (92, 148, 172), (232, 226, 200), mask=rect(-5, -5, SW + 5, 300), wob=2, rim=0, vary=0.07)
    P.layer(poly(ridge(300, 50, 41)), (50, 100, 86), op=0.98, wob=3)
    P.layer(rect(-5, 340, SW + 5, SH + 5), (46, 92, 68), op=1.0, wob=2, rim=0.15, vary=0.2)
    P.layer(poly([(0, 560), (1080, 460), (1080, 500), (0, 610)]), (90, 130, 140), op=0.9, wob=2, rim=0.1)
    fern(P, 150, 600, n=9, size=100)
    fern(P, 930, 560, n=9, size=90)
    person(P, 560, 560, 200)
    return fin(P, 1552)


def thu_a7():
    P = Paint(1561)
    backdrop(P, "dawn", 340, sunp=(540, 330, 54), seed=1561, clouds=3, island=(780, 320))
    P.layer(poly([(-10, 520), (440, 500), (580, 560), (660, 645), (-10, 645)]), (24, 46, 52), op=1.0, wob=3, rim=0.3, vary=0.2)
    person(P, 300, 520, 200)
    return fin(P, 1562)


# ================= QUINTA B — Thoreau (simplificar) =================
def thu_b():
    P = Paint(1601)
    backdrop(P, "dusk", 330, sunp=(300, 322, 40), seed=1601, clouds=2)
    P.layer(rect(-5, 430, SW + 5, SH + 5), (52, 98, 72), op=1.0, wob=2, rim=0.15, vary=0.2)
    house(P, 640, 400, 200, 130, body=(176, 150, 112), seed=5)
    for x in (480, 960):
        tree_pine(P, x, 520, 220)
    return fin(P, 1602)


# ================= SEXTA A — Schopenhauer (compaixão) =================
def fri_a1():
    P = Paint(1701)
    backdrop(P, "dusk", 330, sunp=(780, 322, 40), seed=1701, clouds=2)
    P.layer(rect(-5, 470, SW + 5, SH + 5), (60, 56, 52), op=1.0, wob=2, rim=0.2, vary=0.2)
    bench(P, 420, 580, 320)
    person(P, 360, 566, 170, sit=True)
    person(P, 480, 566, 170, sit=True, coat=(150, 70, 60), hair=(60, 40, 30))
    return fin(P, 1702)


def fri_a2():
    P = Paint(1711)
    backdrop(P, "dusk", 330, sunp=(540, 322, 48), seed=1711, clouds=3, island=(90, 300))
    P.layer(poly([(-10, 520), (500, 500), (640, 560), (700, 645), (-10, 645)]), (24, 46, 52), op=1.0, wob=3, rim=0.3, vary=0.2)
    person(P, 300, 520, 200)
    person(P, 400, 524, 180, coat=(150, 70, 60), hair=(60, 40, 30))
    return fin(P, 1712)


def fri_a3():
    P = Paint(1721)
    backdrop(P, "night", 330, moonp=(840, 130, 44), seed=1721)
    P.layer(rect(-5, 470, SW + 5, SH + 5), (30, 44, 50), op=1.0, wob=2, rim=0.2, vary=0.2)
    person(P, 640, 560, 160, sit=True, coat=(100, 100, 110))
    person(P, 380, 610, 220)
    lantern(P, 470, 480, 1.1)
    return fin(P, 1722)


def fri_a4():
    P = Paint(1731)
    backdrop(P, "dawn", 330, sunp=(540, 320, 46), seed=1731, clouds=3, island=(780, 300))
    P.layer(rect(-5, 480, SW + 5, SH + 5), (76, 90, 70), op=1.0, wob=2, rim=0.2, vary=0.2)
    person(P, 470, 590, 170, sit=True)
    person(P, 580, 590, 170, sit=True, coat=(150, 70, 60), hair=(60, 40, 30))
    return fin(P, 1732)


def fri_a5():
    P = Paint(1741)
    room_bg(P, (22, 52, 64))
    window_frame(P, 380, 70, 700, 400, sky_top=NAVY, sky_bot=(30, 82, 96), stars=30, seed=5)
    table(P, 120, 960, 470)
    cup(P, 500, 470, 76)
    person(P, 300, 645, 320, sit=True)
    return fin(P, 1742)


def fri_a6():
    P = Paint(1751)
    room_bg(P, (30, 62, 70))
    window_frame(P, 700, 80, 980, 380, sky_top=(58, 108, 128), sky_bot=(246, 212, 156))
    table(P, 100, 1000, 450)
    cup(P, 420, 450, 80)
    cup(P, 600, 450, 80, col=(236, 190, 170))
    pot_plant(P, 200, 450, 1.0, seed=7)
    return fin(P, 1752)


def fri_a7():
    P = Paint(1761)
    room_bg(P, (18, 46, 58))
    window_frame(P, 100, 70, 440, 400, sky_top=NAVY, sky_bot=(30, 82, 96), stars=40, seed=6)
    table(P, 60, 1020, 470)
    phone(P, 620, 440, 130, lit=True)
    lamp(P, 880, 470, h=130)
    cup(P, 360, 470, 70)
    return fin(P, 1762)


# ================= SEXTA B — Camus (a luta já basta) =================
def fri_b():
    P = Paint(1801)
    backdrop(P, "dawn", 280, sunp=(860, 270, 40), seed=1801, clouds=2)
    P.layer(poly([(-10, 640), (-10, 520), (300, 470), (620, 380), (900, 300), (1090, 280), (1090, 645)]), (60, 104, 84), op=1.0, wob=3, rim=0.3, vary=0.2)
    P.layer(poly([(-10, 640), (200, 560), (520, 470), (800, 380), (880, 340), (900, 360), (600, 500), (300, 600), (140, 645)]), (176, 146, 104), op=0.95, wob=3, rim=0.2)
    P.layer(ell(560, 450, 44, 44), (110, 104, 96), op=0.98, wob=2, rim=0.35, vary=0.2)
    person(P, 470, 520, 150, profile=0.4)
    return fin(P, 1802)


SCENES = {k: v for k, v in dict(globals()).items() if (k.startswith("thu_") or k.startswith("fri_")) and callable(v)}
