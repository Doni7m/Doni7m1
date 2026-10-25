"""Cenas 28 e 29/10/2026: Beauvoir (liberdade dentro dos limites), Plotino, Voltaire (jardim), Diógenes."""
from lib3 import *


# ------------------------------------------------------------------ 28/10 A (Beauvoir)
def e28a1():
    """Capa: muro alto de pedra com um portão pequeno aberto para o mar; homem diante dele."""
    P = Paint(2801)
    backdrop(P, "dawn", 300, sunp=(540, 250, 36), seed=2801, clouds=2)
    stone_wall(P, 190, SH + 5, seed=41, base=(92, 86, 76), cap=True)
    door(P, 450, 300, 630, 520, lit=True, ajar=0.0)
    P.layer(rect(-5, 520, SW + 5, SH + 5), (90, 80, 66), op=0.98, wob=2, rim=0.2)
    person(P, 540, 600, 230, coat=OCHRE, profile=0.0)
    return fin(P, 2802)


def e28a2():
    """Tudo o que pesa: mesa com agenda, chaves, boletos, relógio, vaso; ele sentado de costas."""
    P = Paint(2811)
    room_bg(P, (22, 46, 60))
    floor(P, 540, (64, 46, 34))
    window_frame(P, 90, 70, 320, 290, stars=16, seed=7, cross=False)
    table(P, 170, 910, 410)
    stack_papers(P, 330, 400, n=4, w=130)
    book(P, 520, 402, w=150)
    letter(P, 700, 394, w=130, tilt=0.05)
    clock_round(P, 800, 160, 70, hands=(0.6, 0.0))
    lamp(P, 880, 450, h=120, g=0.4)
    chair(P, 540, 590, 310)
    person(P, 540, 580, 300, sit=True, profile=0.2)
    return fin(P, 2812)


def e28a3():
    """Duas portas fechadas: uma clara e uma escura, homem entre elas, nenhuma descreve a vida real."""
    P = Paint(2821)
    room_bg(P, (26, 50, 62))
    floor(P, 540, (60, 44, 32))
    door(P, 150, 150, 340, 540, lit=False)
    door(P, 740, 150, 930, 540, lit=False)
    P.glow(245, 340, 140, (255, 230, 170), 0.15)
    lantern(P, 540, 240, 1.0, g=0.7)
    person(P, 540, 590, 280, coat=OCHRE, profile=0.0)
    return fin(P, 2822)


def e28a4():
    """Beauvoir: homem com os pés na água rasa e sobre uma rocha, entre o mar e a terra."""
    P = Paint(2831)
    backdrop(P, "dusk", 300, sunp=(300, 270, 34), seed=2831, clouds=3)
    P.layer(rect(-5, 420, SW + 5, SH + 5), (60, 110, 124), op=0.96, wob=3, rim=0.1)
    cliff(P, side="right", top=330, seed=9, col=(40, 54, 56), reach=420)
    foam(P, 0, 700, 470, n=50, seed=2)
    foam(P, 0, 700, 560, n=40, seed=3)
    P.layer(ell(520, 590, 130, 30), (70, 78, 74), op=0.98, wob=2, rim=0.3)
    person(P, 520, 580, 240, coat=OCHRE, profile=0.2)
    return fin(P, 2832)


def e28a5():
    """Menor escolha: mesa com telefone aceito/aceso e uma xícara; ele pega o primeiro passo."""
    P = Paint(2841)
    room_bg(P, (20, 44, 58))
    floor(P, 540, (62, 46, 34))
    window_frame(P, 700, 70, 960, 320, sky_top=NAVY, sky_bot=(120, 90, 90), stars=12, seed=8, cross=False)
    table(P, 150, 640, 420)
    phone(P, 320, 410, w=100, lit=True)
    cup(P, 480, 412, steam=True)
    candle(P, 580, 420, h=44)
    chair(P, 400, 590, 310)
    person(P, 400, 580, 300, sit=True, profile=0.25)
    P.glow(320, 380, 200, (180, 210, 250), 0.25)
    return fin(P, 2842)


def e28a6():
    """Dentro dos limites: pátio fechado por muros, mas com uma escada para um terraço e uma árvore."""
    P = Paint(2851)
    backdrop(P, "day", 240, seed=2851, clouds=2)
    stone_wall(P, 300, SH + 5, seed=51, base=(100, 92, 80), x0=-5, x1=420)
    stone_wall(P, 300, SH + 5, seed=52, base=(100, 92, 80), x0=660, x1=SW + 5)
    P.layer(rect(380, 400, 700, SH + 5), (130, 114, 92), op=0.98, wob=2, rim=0.2)
    big_tree(P, 540, 420, 220, lean=0.1, leaf=(60, 120, 84), seed=5, crown=0.45)
    person(P, 340, 600, 220, coat=OCHRE, profile=0.2)
    return fin(P, 2852)


def e28a7():
    """Fim: estrada ao longo da levada, ele caminha, luz adiante."""
    P = Paint(2861)
    P.vgrad(-5, 240, (110, 160, 172), (240, 226, 190), mask=rect(-5, -5, SW + 5, 240), wob=2, rim=0, vary=0.07)
    P.layer(poly(ridge(180, 80, 211, x0=-30, x1=SW + 30)), (74, 114, 104), op=0.95, wob=3)
    P.layer(rect(-5, 300, SW + 5, SH + 5), (40, 90, 68), op=1.0, wob=2, rim=0.1)
    P.layer(poly([(-5, 640), (300, 440), (780, 440), (1085, 640)]), (170, 150, 108), op=0.97, wob=3, rim=0.2)
    fern(P, 120, 560, n=9, size=120)
    fern(P, 960, 560, n=9, size=120)
    person(P, 540, 510, 160, coat=OCHRE, profile=0.0)
    P.glow(540, 330, 160, GOLD, 0.45)
    return fin(P, 2862)


def e28b():
    """Plotino: bloco de pedra com formas surgindo, cinzel e lascas, ele de costas."""
    P = Paint(2871)
    room_bg(P, (22, 44, 56))
    floor(P, 500, (70, 54, 40))
    window_frame(P, 100, 60, 380, 300, sky_top=(120, 170, 190), sky_bot=(236, 226, 196), cross=True)
    P.layer(poly([(560, 520), (760, 520), (800, 260), (600, 220), (540, 300)]), (150, 140, 124), op=0.98, wob=2.5, rim=0.35, vary=0.2)
    P.layer(poly([(640, 220), (760, 240), (780, 340), (640, 330)]), (186, 176, 158), op=0.9, wob=2, rim=0.2)
    for k in range(7):
        P.layer(ell(480 + k * 40, 560 + (k % 3) * 8, 14, 6), (170, 160, 140), op=0.95, wob=1, rim=0.2)
    person(P, 400, 590, 280, coat=OCHRE, profile=0.5)
    P.glow(640, 280, 200, WARM, 0.25)
    return fin(P, 2872)


# ------------------------------------------------------------------ 29/10 A (Voltaire)
def e29a1():
    """Capa: terraços (poios) de pedra com bananeiras e horta, homem de costas com enxada."""
    P = Paint(2901)
    backdrop(P, "day", 200, seed=2901, clouds=2)
    for i, y in enumerate([260, 340, 420, 500]):
        P.layer(rect(-5, y, SW + 5, y + 90), [(86, 128, 90), (104, 144, 96), (122, 156, 104), (140, 170, 112)][i], op=0.97, wob=3, rim=0.25)
        stone_wall(P, y + 70, y + 94, seed=60 + i, base=(104, 96, 82), x0=-5, x1=SW + 5)
    banana_leaf(P, 160, 470, -1.1, 190, 70)
    banana_leaf(P, 900, 390, -1.0, 190, 70)
    person(P, 540, 600, 220, coat=OCHRE, profile=0.3)
    P.line([(600, 560), (660, 600)], w=5, alpha=0.8, color=(90, 66, 40))
    return fin(P, 2902)


def e29a2():
    """Muitas notícias: TV acesa, celular, jornais empilhados; homem de costas."""
    P = Paint(2911)
    room_bg(P, (22, 40, 54))
    floor(P, 540, (60, 44, 34))
    tv(P, 360, 120, 720, 340)
    P.layer(rrect(220, 370, 860, 600, 50), (60, 100, 112), op=0.98, wob=2, rim=0.3)
    stack_papers(P, 140, 600, n=6, w=140)
    person(P, 540, 590, 300, sit=True)
    phone(P, 620, 505, w=76, lit=True, tilt=2)
    P.glow(540, 330, 420, (120, 170, 230), 0.18)
    return fin(P, 2912)


def e29a3():
    """Madrugada: banco na rua deserta, só o brilho do celular no rosto/mão; relógio da torre marca 2h."""
    P = Paint(2921)
    backdrop(P, "night", 260, moonp=(880, 110, 22), seed=2921)
    cobbles(P, 440, seed=11, glow_x=480)
    hill_houses(P, -10, SW + 10, 270, n=8, seed=301, lit=False)
    bench(P, 480, 580, w=300)
    person(P, 480, 580, 250, sit=True, profile=0.1)
    phone(P, 560, 520, w=60, lit=True)
    lantern(P, 140, 400, 1.1)
    clock_round(P, 920, 190, 64, hands=(0.2, 0.0))
    return fin(P, 2922)


def e29a4():
    """Voltaire: canteiro pequeno cavado, enxada e plantinhas; horizonte distante com montanhas."""
    P = Paint(2931)
    backdrop(P, "dusk", 250, sunp=(780, 230, 30), seed=2931, clouds=2)
    P.layer(poly(ridge(200, 70, 221, x0=-30, x1=SW + 30)), (60, 90, 100), op=0.95, wob=3)
    P.layer(rect(-5, 330, SW + 5, SH + 5), (92, 74, 54), op=1.0, wob=3, rim=0.15)
    for k in range(5):
        P.layer(rect(100 + k * 160, 470, 190 + k * 160, 480), (62, 48, 34), op=0.95, wob=1.5)
    for x in (150, 310, 470):
        sapling(P, x, 480, 70)
    person(P, 690, 590, 250, coat=OCHRE, profile=0.2)
    P.line([(740, 440), (780, 560)], w=5, alpha=0.85, color=(90, 66, 40))
    return fin(P, 2932)


def e29a5():
    """Um canto: mesa com planta pequena, regador e carta pendente; luz quente."""
    P = Paint(2941)
    room_bg(P, (22, 46, 60))
    floor(P, 540, (64, 46, 34))
    window_frame(P, 100, 70, 360, 320, sky_top=(150, 190, 204), sky_bot=(244, 230, 196), cross=True)
    table(P, 300, 900, 410)
    pot_plant(P, 460, 410, 1.2, kind="sprout", seed=3)
    pot_plant(P, 580, 410, 1.0, kind="geranium", seed=4)
    letter(P, 740, 394, w=130, tilt=-0.04)
    cup(P, 850, 400, steam=True)
    chair(P, 620, 590, 310)
    person(P, 620, 580, 300, sit=True, profile=-0.25)
    return fin(P, 2942)


def e29a6():
    """Pés firmes num canto pequeno: homem num pedaço de terra diante de montanhas enormes."""
    P = Paint(2951)
    backdrop(P, "day", 260, seed=2951, clouds=3)
    P.layer(poly(ridge(170, 110, 231, x0=-30, x1=SW + 30)), (92, 112, 118), op=0.95, wob=3)
    P.layer(poly(ridge(260, 70, 232, x0=-30, x1=SW + 30)), (58, 98, 90), op=0.98, wob=3)
    P.layer(rect(-5, 420, SW + 5, SH + 5), (80, 120, 84), op=1.0, wob=3, rim=0.15)
    P.layer(rect(400, 520, 700, 640), (96, 74, 54), op=0.98, wob=2, rim=0.25)
    person(P, 540, 560, 210, coat=OCHRE, profile=0.0)
    return fin(P, 2952)


def e29a7():
    """Poios ao pôr do sol: terraços e cabana, homem leva um regador."""
    P = Paint(2961)
    backdrop(P, "dusk", 220, sunp=(540, 210, 34), seed=2961, clouds=3)
    for i, y in enumerate([310, 390, 470]):
        P.layer(rect(-5, y, SW + 5, y + 90), [(70, 112, 84), (86, 126, 90), (102, 140, 96)][i], op=0.97, wob=3, rim=0.25)
        stone_wall(P, y + 70, y + 94, seed=70 + i, base=(100, 92, 80), x0=-5, x1=SW + 5)
    house(P, 200, 400, 120, 80, lit=True, seed=6)
    person(P, 640, 600, 230, coat=OCHRE, profile=0.3)
    P.layer(rect(700, 540, 740, 580), (120, 100, 76), op=0.97, wob=1)
    return fin(P, 2962)


def e29b():
    """Diógenes: tonel de madeira ao lado de um muro, sol grande, sombra de alguém à direita."""
    P = Paint(2971)
    backdrop(P, "day", 260, seed=2971, clouds=1)
    P.glow(300, 180, 320, GOLD, 0.65)
    P.layer(ell(300, 170, 60, 60), (255, 236, 176), op=0.98, wob=1.5, rim=0.05)
    P.layer(rect(-5, 420, SW + 5, SH + 5), (176, 150, 100), op=0.98, wob=3, rim=0.2)
    P.layer(ell(540, 580, 130, 36), (128, 84, 52), op=0.98, wob=2, rim=0.3)
    P.layer(rect(410, 420, 670, 580), (150, 104, 62), op=0.98, wob=2, rim=0.3)
    for y in (450, 520):
        P.layer(rect(410, y, 670, y + 8), (80, 56, 34), op=0.95, wob=1)
    P.layer(ell(540, 420, 130, 36), (170, 124, 78), op=0.98, wob=2, rim=0.3)
    person(P, 800, 600, 230, coat=(150, 70, 52), profile=-0.3)
    return fin(P, 2972)


SCENES = {n: f for n, f in globals().items() if n.startswith("e2") and callable(f)}
