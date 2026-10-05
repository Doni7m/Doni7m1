import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy.ndimage import gaussian_filter

BASE = os.path.dirname(os.path.abspath(__file__))
ART = f"{BASE}/art"
OUT = f"{BASE}/out"
DATE = "2026-10-05"
W, H = 1080, 1350
IVORY = (246, 239, 224)
INK = (43, 38, 33)
MUTED = (112, 100, 86)
ACCENT = (150, 96, 52)
LINE = (178, 164, 138)
FONT_DIR = "/usr/share/fonts/truetype/google-fonts/"
MX = 92            # ~8,5% de margem lateral
TEXT_TOP, TEXT_BOTTOM = 128, 566

SLIDES = [
    dict(main="Estar sozinho e se sentir sozinho não são a mesma coisa.", sub=None, big=True),
    dict(main="O celular está quieto, a casa em silêncio. E surge a pergunta: será que deveria haver mais gente aqui?", sub=None),
    dict(main="Existe a solidão que dói, quando falta alguém. E existe a que acalma, quando finalmente sobra espaço para você.", sub=None),
    dict(main="Montaigne sugeria guardar nos fundos da vida um cômodo só seu, um espaço interior onde você continua inteiro, mesmo cercado de gente.",
         sub="Uma reflexão inspirada em Montaigne"),
    dict(main="Reserve vinte minutos sem tela e sem tarefa: caminhar, fazer um chá, escrever três linhas. Não para fugir dos outros, mas para voltar a si.", sub=None),
    dict(main="Nem toda solidão é escolha. Quando pesa, ela merece atenção e companhia, e não pressa para passar. Procurar alguém também é cuidar de si.", sub=None),
    dict(main="Quem cuida do seu cômodo interior pode chegar aos outros mais presente.", sub="Salve para reler numa noite silenciosa.", closing=True),
]


def lora(size, italic=False, weight=500):
    f = ImageFont.truetype(FONT_DIR + ("Lora-Italic-Variable.ttf" if italic else "Lora-Variable.ttf"), size)
    try:
        f.set_variation_by_axes([weight])
    except Exception:
        pass
    return f


def wrap(d, text, font, max_w):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= max_w:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def balanced(d, text, font, max_w):
    lines = wrap(d, text, font, max_w)
    n = len(lines)
    best = lines
    w = max_w
    while w > max_w * 0.55:
        w -= 8
        cand = wrap(d, text, font, w)
        if len(cand) > n:
            break
        best = cand
    return best


def paper(seed=3):
    r = np.random.default_rng(seed)
    base = np.ones((H, W, 3), np.float32) * np.array(IVORY, np.float32)
    fine = gaussian_filter(r.normal(0, 1, (H, W)).astype(np.float32), 0.7)
    fibers = gaussian_filter(r.normal(0, 1, (H, W)).astype(np.float32), 6)
    blot = gaussian_filter(r.normal(0, 1, (H, W)).astype(np.float32), 60)
    tex = 1 + 0.006 * fine + 0.006 * fibers / (fibers.std() + 1e-6) + 0.006 * blot / (blot.std() + 1e-6)
    base *= tex[..., None]
    return np.clip(base, 0, 255).astype(np.uint8)


def render(i, spec):
    n = i + 1
    bg = Image.fromarray(paper(seed=10 + n)).convert("RGB")
    # ilustração (multiplica sobre o papel para herdar a textura)
    d0 = ImageDraw.Draw(bg)

    # texto principal com ajuste automático de tamanho
    max_w = W - 2 * MX
    d = d0
    sizes = range(104, 44, -2) if spec.get("big") else range(76, 44, -2)
    chosen = None
    for sz in sizes:
        f = lora(sz, weight=700)
        lines = balanced(d, spec["main"], f, max_w)
        lh = int(sz * 1.22)
        sub_h = 0
        if spec.get("sub"):
            sub_h = 34 + 30
        total = len(lines) * lh + sub_h
        if total <= (TEXT_BOTTOM - TEXT_TOP):
            chosen = (sz, f, lines, lh)
            break
    sz, f, lines, lh = chosen
    y = TEXT_TOP
    for ln in lines:
        d.text((MX, y), ln, font=f, fill=INK)
        y += lh
    text_end = y
    if spec.get("sub"):
        fs = lora(32, italic=True, weight=500)
        d.text((MX, y + 18), spec["sub"], font=fs, fill=ACCENT)
        text_end = y + 18 + 36
    # ilustração: multiplica sobre o papel (herda a textura) e centraliza o espaço livre
    ill = np.asarray(Image.open(f"{ART}/scene_{n}.png").convert("RGB"), np.float32) / 255.0
    ivory = np.array(IVORY, np.float32) / 255.0
    ratio = ill / ivory
    canvas = np.asarray(bg, np.float32) / 255.0
    y0 = int(min(584, 300 + text_end / 2))
    region = canvas[y0:y0 + ill.shape[0], :, :]
    canvas[y0:y0 + ill.shape[0], :, :] = np.clip(region * ratio, 0, 1)
    img = Image.fromarray((canvas * 255).astype(np.uint8)).convert("RGB")
    d = ImageDraw.Draw(img)

    # rodapé: linha fina, @doni7m à esquerda, numeração à direita
    d.line([(MX, 1236), (W - MX, 1236)], fill=LINE, width=2)
    ff = lora(30, weight=600)
    d.text((MX, 1256), "@doni7m", font=ff, fill=MUTED)
    tag = f"{n:02d} / 07"
    d.text((W - MX - d.textlength(tag, font=ff), 1256), tag, font=ff, fill=MUTED)
    return img, (sz, len(lines))


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for i, spec in enumerate(SLIDES):
        img, info = render(i, spec)
        path = f"{OUT}/{DATE}_{i + 1:02d}.png"
        img.save(path)
        print(path, img.size, "font", info[0], "lines", info[1])
    # contact sheet apenas para conferência (não faz parte da entrega)
    thumbs = [Image.open(f"{OUT}/{DATE}_{k:02d}.png").resize((360, 450)) for k in range(1, 8)]
    sheet = Image.new("RGB", (360 * 4, 450 * 2), (255, 255, 255))
    for k, t in enumerate(thumbs):
        sheet.paste(t, ((k % 4) * 360, (k // 4) * 450))
    sheet.save(f"{BASE}/check_sheet.png")
