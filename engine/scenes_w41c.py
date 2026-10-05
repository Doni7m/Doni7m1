"""Cenas semana 06-11/10/2026 — parte C (sábado e domingo)."""
from lib2 import *
from scenes_w41a import fin, inv


# ================= SÁBADO A — Hume (sentir move a gente) =================
def sat_a1():
    P = Paint(1901)
    backdrop(P, "day", 330, seed=1901, clouds=4, island=(80, 300))
    boat(P, 640, 450, 1.4, sail=True)
    gulls(P, [(300, 120, 1.0), (380, 90, 0.9), (460, 130, 1.0)])
    return fin(P, 1902)


def sat_a2():
    P = Paint(1911)
    backdrop(P, "dusk", 330, sunp=(700, 322, 40), seed=1911, clouds=3)
    boat(P, 420, 440, 1.2, lit=True)
    boat(P, 760, 470, 0.9, hull=(60, 90, 120))
    return fin(P, 1912)


def sat_a3():
    P = Paint(1921)
    backdrop(P, "dusk", 300, sunp=(560, 296, 40), seed=1921, clouds=3)
    hill_houses(P, 40, 1040, 330, n=9, seed=4, lit=True)
    P.layer(rect(-5, 470, SW + 5, SH + 5), (60, 56, 52), op=1.0, wob=2, rim=0.2, vary=0.2)
    lantern(P, 320, 500, 1.2)
    person(P, 520, 620, 230)
    return fin(P, 1922)


def sat_a4():
    P = Paint(1931)
    P.vgrad(-5, 330, (92, 148, 172), (232, 226, 200), mask=rect(-5, -5, SW + 5, 330), wob=2, rim=0, vary=0.07)
    P.layer(poly(ridge(330, 50, 51)), (50, 100, 86), op=0.98, wob=3)
    P.layer(rect(-5, 400, SW + 5, SH + 5), (46, 92, 68), op=1.0, wob=2, rim=0.15, vary=0.2)
    for (x, y, r, s) in [(200, 500, 66, 1), (400, 540, 60, 2), (640, 500, 70, 3), (850, 540, 62, 4), (520, 600, 56, 5)]:
        hydrangea(P, x, y, r, seed=s * 7)
    person(P, 780, 450, 130)
    return fin(P, 1932)


def sat_a5():
    P = Paint(1941)
    backdrop(P, "day", 320, seed=1941, clouds=3, island=(760, 300))
    P.layer(rect(-5, 420, SW + 5, SH + 5), (52, 98, 72), op=1.0, wob=2, rim=0.15, vary=0.2)
    P.layer(poly([(480, 645), (600, 645), (600, 470), (560, 440)]), (176, 146, 104), op=0.97, wob=3, rim=0.25)
    P.layer(poly([(560, 460), (1090, 470), (1090, 500), (590, 500)]), (176, 146, 104), op=0.97, wob=3, rim=0.25)
    P.layer(poly([(560, 460), (-10, 430), (-10, 462), (560, 500)]), (176, 146, 104), op=0.97, wob=3, rim=0.25)
    P.layer(rect(552, 360, 564, 470), (96, 66, 40), op=0.98, wob=1)
    person(P, 540, 600, 210)
    return fin(P, 1942)


def sat_a6():
    P = Paint(1951)
    room_bg(P, (24, 54, 66))
    window_frame(P, 700, 80, 980, 380, sky_top=(58, 108, 128), sky_bot=(246, 212, 156))
    table(P, 100, 1000, 450)
    book(P, 460, 448, 190)
    cup(P, 700, 450, 76)
    candle(P, 260, 450)
    return fin(P, 1952)


def sat_a7():
    P = Paint(1961)
    backdrop(P, "dusk", 340, sunp=(540, 336, 56), seed=1961, clouds=3)
    P.layer(rect(-5, 480, SW + 5, SH + 5), (86, 80, 72), op=1.0, wob=2, rim=0.25, vary=0.2)
    boat(P, 260, 460, 1.0, lit=True)
    boat(P, 840, 470, 1.1, hull=(60, 90, 120))
    person(P, 540, 645, 250)
    return fin(P, 1962)


# ================= SÁBADO B — Wittgenstein (silêncio) =================
def sat_b():
    P = Paint(2001)
    backdrop(P, "night", 340, moonp=(540, 150, 60), seed=2001)
    P.layer(poly([(-10, 520), (500, 500), (660, 560), (720, 645), (-10, 645)]), (10, 24, 36), op=1.0, wob=3, rim=0.3, vary=0.2)
    person(P, 320, 520, 190, sit=True)
    return fin(P, 2002)


# ================= DOMINGO A — Rousseau (sem vitrine) =================
def sun_a1():
    P = Paint(2101)
    room_bg(P, (18, 46, 58))
    table(P, 60, 1020, 470)
    phone(P, 540, 440, 160, lit=True)
    cup(P, 280, 470, 70)
    lamp(P, 880, 470, h=130)
    person(P, 540, 645, 220, sit=True)
    return fin(P, 2102)


def sun_a2():
    P = Paint(2111)
    backdrop(P, "dusk", 330, sunp=(300, 322, 40), seed=2111, clouds=3)
    P.layer(rect(-5, 470, SW + 5, SH + 5), (60, 56, 52), op=1.0, wob=2, rim=0.2, vary=0.2)
    lantern(P, 800, 500, 1.4)
    person(P, 520, 620, 230)
    return fin(P, 2112)


def sun_a3():
    P = Paint(2121)
    backdrop(P, "night", 220, seed=2121)
    P.layer(poly(ridge(262, 24, 9)), (14, 40, 50), op=1.0, wob=2, rim=0.2)
    hill_houses(P, 30, 1050, 262, n=12, seed=9, lit=True)
    P.layer(rect(-5, 520, SW + 5, SH + 5), (30, 44, 50), op=1.0, wob=2, rim=0.2, vary=0.2)
    person(P, 540, 645, 200)
    return fin(P, 2122)


def sun_a4():
    P = Paint(2131)
    P.vgrad(-5, 320, (92, 148, 172), (232, 226, 200), mask=rect(-5, -5, SW + 5, 320), wob=2, rim=0, vary=0.07)
    P.layer(poly(ridge(320, 60, 61)), (50, 100, 86), op=0.98, wob=3)
    P.layer(rect(-5, 400, SW + 5, SH + 5), (46, 92, 68), op=1.0, wob=2, rim=0.15, vary=0.2)
    for k in range(40):
        t = k / 39
        x = 300 + 400 * np.sin(t * 3.2) * (0.3 + t * 0.7) + 200
        y = 645 - t * 230
        P.layer(ell(x, y, 70 * (1 - t) + 12, 16 * (1 - t) + 3), (176, 146, 104), op=0.97, wob=2, rim=0.1, soft=1.2)
    person(P, 520, 620, 220)
    return fin(P, 2132)


def sun_a5():
    P = Paint(2141)
    backdrop(P, "day", 300, seed=2141, clouds=3, island=(120, 320))
    P.layer(rect(-5, 420, SW + 5, SH + 5), (52, 98, 72), op=1.0, wob=2, rim=0.15, vary=0.2)
    P.layer(ell(540, 540, 130, 34), (120, 112, 100), op=0.98, wob=2, rim=0.3, vary=0.2)
    person(P, 540, 550, 170, sit=True)
    return fin(P, 2142)


def sun_a6():
    P = Paint(2151)
    P.vgrad(-5, 330, (92, 148, 172), (232, 226, 200), mask=rect(-5, -5, SW + 5, 330), wob=2, rim=0, vary=0.07)
    P.layer(poly(ridge(330, 50, 71)), (40, 92, 84), op=0.98, wob=3)
    P.layer(rect(-5, 380, SW + 5, SH + 5), (46, 92, 68), op=1.0, wob=2, rim=0.15, vary=0.2)
    P.layer(poly([(0, 560), (1080, 460), (1080, 500), (0, 610)]), (90, 130, 140), op=0.9, wob=2, rim=0.1)
    fern(P, 160, 600, n=9, size=100)
    fern(P, 920, 560, n=9, size=90)
    person(P, 540, 570, 210)
    return fin(P, 2152)


def sun_a7():
    P = Paint(2161)
    backdrop(P, "dusk", 340, sunp=(540, 334, 56), seed=2161, clouds=3, island=(800, 300))
    P.layer(rect(-5, 500, SW + 5, SH + 5), (86, 80, 72), op=1.0, wob=2, rim=0.25, vary=0.2)
    table(P, 640, 960, 560)
    cup(P, 800, 560, 70)
    person(P, 400, 645, 290, sit=True)
    return fin(P, 2162)


# ================= DOMINGO B — Kant (três perguntas) =================
def sun_b():
    P = Paint(2201)
    backdrop(P, "dawn", 300, sunp=(700, 292, 46), seed=2201, clouds=3)
    P.layer(poly(ridge(340, 24, 3)), (40, 80, 78), op=1.0, wob=2, rim=0.2)
    hill_houses(P, 40, 700, 340, n=8, seed=3, lit=False)
    P.layer(rect(-5, 470, SW + 5, SH + 5), (60, 56, 52), op=1.0, wob=2, rim=0.2, vary=0.2)
    stone_stairs(P, 300, 700, 480, 645, steps=5)
    person(P, 500, 480, 150)
    return fin(P, 2202)


SCENES = {k: v for k, v in dict(globals()).items() if (k.startswith("sat_") or k.startswith("sun_")) and callable(v)}
