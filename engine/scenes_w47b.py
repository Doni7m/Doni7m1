"""Cenas 12-13/11/2026: Dewey (q12), Mozi (q12b), Ricoeur (q13), Nagarjuna (q13b)."""
from lib4 import *


def signpost(P, x, ybase, h=300, flip=1):
    P.layer(rect(x - 8, ybase - h, x + 8, ybase), (96, 66, 40), op=0.98, wob=1.5, rim=0.3)
    for k, (dy, d) in enumerate([(0, 1), (70, -1)]):
        y = ybase - h + 20 + dy
        d = d * flip
        P.layer(poly([(x - 10, y), (x + 150 * d, y), (x + 175 * d, y + 22), (x + 150 * d, y + 44), (x - 10, y + 44)]),
                (190, 150, 96), op=0.98, wob=1.5, rim=0.3)


def grass_field(P, ytop, col=(86, 132, 86)):
    P.layer(rect(-5, ytop, SW + 5, SH + 5), col, op=0.98, wob=3, rim=0.2)


def dirt_path(P, pts_l, pts_r, col=(196, 168, 120)):
    P.layer(poly(pts_l + pts_r[::-1]), col, op=0.97, wob=3, rim=0.25)


# ============================================================ 12/11 Dewey: hábitos
def q12a1():
    P = Paint(7401)
    room_bg(P, (20, 40, 54))
    floor(P, 540, (60, 44, 34))
    bed(P, 60, 620, 470)
    phone(P, 420, 440, w=70, lit=True)
    P.glow(420, 440, 140, (140, 190, 240), 0.35)
    window_frame(P, 720, 70, 980, 320, sky_top=(14, 28, 56), sky_bot=(30, 60, 90), stars=30)
    person(P, 760, 600, 280, sit=True, profile=0.7)
    return fin(P, 7402)


def q12a2():
    P = Paint(7411)
    room_bg(P, (24, 46, 58))
    floor(P, 550, (62, 46, 36))
    table(P, 140, 700, 420)
    phone(P, 360, 414, lit=False, face_down=True)
    letter(P, 520, 408, w=130)
    pot_plant(P, 640, 420, 0.8)
    chair(P, 260, 590, 300)
    person(P, 260, 580, 285, sit=True, profile=0.5)
    window_frame(P, 760, 70, 990, 300, sky_top=(24, 44, 76), sky_bot=(70, 100, 120), stars=20)
    return fin(P, 7412)


def q12a3():
    P = Paint(7421)
    backdrop(P, "day", 250, seed=7421, clouds=2)
    grass_field(P, 330)
    dirt_path(P, [(460, 640), (500, 330), (540, 330)], [(720, 640), (560, 330), (540, 330)])
    P.layer(poly([(520, 640), (540, 330), (545, 330), (590, 640)]), (170, 140, 96), op=0.6, wob=3, rim=0, soft=3)
    person(P, 580, 560, 200, coat=OCHRE, profile=0.1)
    tree_pine(P, 140, 400, 220)
    tree_pine(P, 960, 380, 200)
    return fin(P, 7422)


def q12a4():
    P = Paint(7431)
    P.vgrad(-5, SH + 5, (170, 206, 200), (96, 150, 110), mask=rect(-5, -5, SW + 5, SH + 5), wob=0, rim=0, vary=0.08)
    cobbles(P, 330, SH + 5, seed=4, glow_x=540)
    P.layer(poly([(480, 640), (510, 330), (570, 330), (650, 640)]), (110, 96, 80), op=0.55, wob=3, rim=0, soft=5)
    hill_houses(P, 0, 1080, 260, n=7, seed=3, lit=False)
    person(P, 560, 600, 240, coat=OCHRE, profile=0.0)
    return fin(P, 7432)


def q12a5():
    P = Paint(7441)
    room_bg(P, (22, 44, 56))
    floor(P, 540, (62, 44, 34))
    bed(P, 40, 520, 480)
    book(P, 200, 440, w=120)
    table(P, 760, 1020, 420)
    phone(P, 890, 414, lit=True)
    lamp(P, 960, 420, 150)
    person(P, 640, 600, 260, coat=OCHRE, profile=0.9)
    return fin(P, 7442)


def q12a6():
    P = Paint(7451)
    backdrop(P, "day", 260, seed=7451, clouds=2)
    grass_field(P, 320, (92, 140, 92))
    dirt_path(P, [(300, 640), (440, 330), (480, 330)], [(520, 640), (500, 330), (480, 330)], col=(180, 154, 110))
    dirt_path(P, [(640, 640), (560, 330), (600, 330)], [(900, 640), (640, 330), (600, 330)], col=(206, 180, 130))
    sapling(P, 600, 400, 90)
    person(P, 780, 590, 220, coat=OCHRE, profile=0.4)
    return fin(P, 7452)


def q12a7():
    P = Paint(7461)
    room_bg(P, (30, 56, 66))
    floor(P, 560, (66, 48, 36))
    window_frame(P, 200, 60, 880, 380, sky_top=(120, 170, 190), sky_bot=(246, 214, 160))
    P.glow(560, 260, 320, WARM, 0.35)
    P.layer(rect(170, 380, 910, 410), (120, 84, 52), op=0.98, wob=1.5, rim=0.3)
    pot_plant(P, 700, 390, 0.9, kind="sprout")
    cup(P, 360, 380, steam=True)
    book(P, 480, 382, w=120)
    return fin(P, 7462)


def q12b():
    P = Paint(7471)
    backdrop(P, "day", 240, seed=7471, clouds=2)
    hill_houses(P, 0, 1080, 250, n=6, seed=5, lit=False)
    grass_field(P, 400, (96, 140, 92))
    stone_wall(P, 440, SH + 5, seed=37, base=(120, 108, 92), x0=300, x1=780)
    person(P, 200, 590, 260, coat=OCHRE, profile=0.8)
    person(P, 880, 590, 260, coat=BLUE_COAT, profile=-0.8)
    lantern(P, 540, 380, 1.0)
    pot_plant(P, 400, 440, 0.8)
    return fin(P, 7472)


# ============================================================ 13/11 Ricoeur: narrativa
def q13a1():
    P = Paint(7501)
    room_bg(P, (22, 40, 54))
    floor(P, 540, (60, 44, 34))
    bookshelf(P, 60, 70, 360, 520, rows=5, seed=3)
    table(P, 340, 880, 420)
    book(P, 540, 416, w=190, open_=True)
    lamp(P, 800, 420, 160)
    chair(P, 560, 590, 300)
    person(P, 560, 580, 285, sit=True, profile=0.0)
    return fin(P, 7502)


def q13a2():
    P = Paint(7511)
    room_bg(P, (24, 44, 56))
    floor(P, 550, (62, 46, 36))
    table(P, 140, 760, 430)
    stack_papers(P, 320, 420, n=5, w=140)
    P.line([(280, 380), (360, 370), (340, 350), (420, 364)], w=3, alpha=0.8, color=(160, 60, 50))
    candle(P, 600, 424)
    chair(P, 460, 590, 300)
    person(P, 460, 580, 285, sit=True, profile=0.3)
    window_frame(P, 800, 70, 1000, 300, sky_top=(14, 28, 56), sky_bot=(30, 60, 90), stars=25)
    return fin(P, 7512)


def q13a3():
    P = Paint(7521)
    room_bg(P, (20, 38, 50))
    floor(P, 570, (56, 40, 32))
    bookshelf(P, 120, 60, 960, 560, rows=5, seed=8)
    P.layer(rect(500, 250, 560, 320), (20, 34, 44), op=0.98, wob=1)
    person(P, 540, 600, 280, coat=OCHRE, profile=0.0)
    return fin(P, 7522)


def q13a4():
    P = Paint(7531)
    room_bg(P, (30, 54, 66))
    floor(P, 560, (66, 48, 36))
    window_frame(P, 560, 60, 1000, 380, sky_top=(120, 170, 190), sky_bot=(246, 214, 160))
    P.glow(780, 230, 340, WARM, 0.35)
    bookshelf(P, 40, 80, 300, 540, rows=4, seed=5)
    chair(P, 420, 590, 310, facing=1)
    person(P, 420, 580, 295, sit=True, profile=0.7)
    book(P, 420, 450, w=90)
    return fin(P, 7532)


def q13a5():
    P = Paint(7541)
    room_bg(P, (26, 48, 58))
    floor(P, 540, (62, 44, 34))
    window_frame(P, 700, 70, 980, 320, sky_top=(110, 150, 170), sky_bot=(226, 206, 170))
    table(P, 100, 660, 420)
    letter(P, 300, 408, w=190, tilt=-0.03, stamp=False)
    P.line([(240, 392), (360, 386), (330, 372), (400, 380)], w=3, alpha=0.8, color=(40, 60, 100))
    cup(P, 520, 414)
    chair(P, 330, 590, 300)
    person(P, 330, 580, 285, sit=True, profile=0.2)
    return fin(P, 7542)


def q13a6():
    P = Paint(7551)
    room_bg(P, (22, 42, 54))
    floor(P, 520, (66, 48, 36))
    bookshelf(P, 640, 70, 1000, 500, rows=4, seed=11)
    stack_papers(P, 240, 560, n=6, w=150)
    stack_papers(P, 440, 570, n=4, w=150)
    stack_papers(P, 120, 575, n=3, w=130)
    person(P, 400, 540, 220, sit=True, profile=0.4)
    return fin(P, 7552)


def q13a7():
    P = Paint(7561)
    room_bg(P, (22, 42, 54))
    floor(P, 540, (62, 44, 34))
    table(P, 220, 860, 440)
    book(P, 540, 436, w=260, open_=True)
    P.glow(540, 400, 280, GOLD, 0.5)
    lamp(P, 820, 440, 170)
    person(P, 300, 600, 270, coat=OCHRE, profile=0.7)
    return fin(P, 7562)


def q13b():
    P = Paint(7571)
    backdrop(P, "dusk", 320, sunp=(540, 330, 30), seed=7571, clouds=2)
    hill_houses(P, 0, 1080, 300, n=9, seed=7, lit=True)
    string_lights(P, 0, 1080, 120, sag=60, n=14)
    string_lights(P, 0, 1080, 200, sag=40, n=12)
    P.layer(rect(-5, 520, SW + 5, SH + 5), (80, 66, 52), op=0.98, wob=2, rim=0.3)
    person(P, 540, 600, 240, coat=OCHRE, profile=0.0)
    return fin(P, 7572)


SCENES = {n: f for n, f in globals().items() if n.startswith("q") and callable(f)}
