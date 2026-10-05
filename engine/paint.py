"""Procedural gouache/watercolor engine (numpy + PIL + scipy)."""
import numpy as np
from PIL import Image, ImageDraw
from scipy.ndimage import gaussian_filter

SW, SH = 1080, 640
IVORY = np.array([246, 239, 224], np.float32)

# palette
NAVY = (13, 29, 58)
DEEP = (20, 46, 84)
TEAL = (31, 87, 98)
DTEAL = (16, 58, 70)
MOSS = (52, 92, 82)
OCHRE = (196, 138, 52)
OCHRE_D = (160, 104, 38)
CREAM = (240, 226, 190)
GOLD = (232, 184, 92)
WARM = (252, 212, 128)
STONE = (112, 104, 92)
WOOD = (122, 82, 48)
HAIR = (34, 28, 26)
SKIN = (196, 148, 118)


def lowfreq(h, w, scale, seed):
    r = np.random.default_rng(seed)
    small = r.random((max(2, h // scale) + 2, max(2, w // scale) + 2)).astype(np.float32)
    im = Image.fromarray((small * 255).astype(np.uint8)).resize((w, h), Image.BICUBIC)
    return np.asarray(im, np.float32) / 255.0


def new_mask():
    return Image.new("L", (SW, SH), 0)


def shape(fn):
    m = new_mask()
    fn(ImageDraw.Draw(m))
    return m


def poly(pts):
    return shape(lambda d: d.polygon(pts, fill=255))


def rect(x0, y0, x1, y1):
    return shape(lambda d: d.rectangle([x0, y0, x1, y1], fill=255))


def ell(cx, cy, rx, ry):
    return shape(lambda d: d.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=255))


def rrect(x0, y0, x1, y1, r):
    return shape(lambda d: d.rounded_rectangle([x0, y0, x1, y1], radius=r, fill=255))


def ridge(y0, amp, seed, x0=-30, x1=SW + 30, step=18):
    r = np.random.default_rng(seed)
    xs = np.arange(x0, x1 + step, step)
    ph = r.random(4) * 6.28
    ys = y0 + amp * (0.5 * np.sin(xs / (140 + r.random() * 60) + ph[0])
                     + 0.3 * np.sin(xs / 61 + ph[1])
                     + 0.2 * np.sin(xs / 24 + ph[2]))
    pts = [(float(x), float(y)) for x, y in zip(xs, ys)]
    pts += [(x1, SH + 20), (x0, SH + 20)]
    return pts


class Paint:
    def __init__(self, seed=1):
        self.c = np.tile(IVORY / 255.0, (SH, SW, 1)).astype(np.float32)
        self.n1 = lowfreq(SH, SW, 70, seed)
        self.n2 = lowfreq(SH, SW, 16, seed + 1)
        self.n3 = lowfreq(SH, SW, 4, seed + 2)
        self.ys, self.xs = np.mgrid[0:SH, 0:SW]
        self.lines = []
        self.rng = np.random.default_rng(seed + 10)

    # ---- core painting -------------------------------------------------
    def layer(self, mask, color, op=0.96, wob=4.0, rim=0.20, grain=0.10, vary=0.14, soft=1.0):
        m = np.asarray(mask, np.float32) / 255.0
        if wob:
            dx = (self.n2 - 0.5) * 2 * wob
            dy = (self.n1 - 0.5) * 2 * wob
            xi = np.clip((self.xs + dx).astype(np.int32), 0, SW - 1)
            yi = np.clip((self.ys + dy).astype(np.int32), 0, SH - 1)
            m = m[yi, xi]
        if soft:
            m = gaussian_filter(m, soft)
        col = np.asarray(color, np.float32)
        if col.ndim == 1:
            col = np.broadcast_to(col / 255.0, (SH, SW, 3))
        else:
            col = col / 255.0
        var = 1.0 + vary * (self.n1 - 0.5) * 2 + grain * (self.n3 - 0.5) * 2
        pig = col * var[..., None]
        if rim:
            inner = gaussian_filter(m, 5)
            edge = np.clip((m - inner) * 3.0, 0, 1)
            pig = pig * (1.0 - rim * edge[..., None])
        a = (m * op)[..., None]
        self.c = self.c * (1 - a) + pig * a
        return m

    def vgrad(self, y0, y1, c0, c1, mask=None, **kw):
        t = np.clip((self.ys - y0) / float(y1 - y0), 0, 1)[..., None]
        col = np.asarray(c0, np.float32) * (1 - t) + np.asarray(c1, np.float32) * t
        if mask is None:
            mask = rect(-5, y0, SW + 5, y1 if y1 > y0 else SH)
        return self.layer(mask, col, **kw)

    def glow(self, x, y, r, color=WARM, strength=0.8):
        d2 = (self.xs - x) ** 2 + (self.ys - y) ** 2
        g = np.exp(-d2 / (2.0 * r * r)).astype(np.float32)[..., None] * strength
        col = np.asarray(color, np.float32) / 255.0
        self.c = 1.0 - (1.0 - self.c) * (1.0 - g * col)

    def stars(self, n, ymax, seed=5):
        r = np.random.default_rng(seed)
        for _ in range(n):
            x = r.integers(20, SW - 20)
            y = r.integers(10, ymax)
            self.glow(x, y, r.uniform(1.4, 3.0), CREAM, r.uniform(0.5, 0.95))

    def line(self, pts, w=2, alpha=0.55, color=(28, 36, 48)):
        self.lines.append((pts, w, alpha, color))

    def strokes(self, x0, x1, y0, y1, n, color, op=0.25, wmin=30, wmax=140, hmax=3, seed=3):
        r = np.random.default_rng(seed)
        for _ in range(n):
            w = r.uniform(wmin, wmax)
            x = r.uniform(x0, x1 - w)
            y = r.uniform(y0, y1)
            h = r.uniform(1.2, hmax)
            self.layer(ell(x + w / 2, y, w / 2, h), color, op=op, wob=0, rim=0, grain=0.05, vary=0.1, soft=0.8)

    # ---- finishing -------------------------------------------------------
    def finish(self, top=40, bottom=40, left=40, right=40, feather=60, seed=9):
        # pencil linework
        img = Image.fromarray((np.clip(self.c, 0, 1) * 255).astype(np.uint8)).convert("RGBA")
        ov = Image.new("RGBA", img.size, (0, 0, 0, 0))
        d = ImageDraw.Draw(ov)
        r = np.random.default_rng(seed)
        for pts, w, alpha, color in self.lines:
            jp = [(x + r.normal(0, 0.7), y + r.normal(0, 0.7)) for x, y in pts]
            d.line(jp, fill=color + (int(255 * alpha),), width=w, joint="curve")
        img = Image.alpha_composite(img, ov).convert("RGB")
        c = np.asarray(img, np.float32) / 255.0
        # organic dissolve into paper
        dist = np.minimum.reduce([self.xs - left, SW - self.xs - right, self.ys - top, SH - self.ys - bottom]).astype(np.float32)
        t = dist / float(feather * 1.35) + (lowfreq(SH, SW, 90, seed) - 0.5) * 0.7 + (lowfreq(SH, SW, 22, seed + 3) - 0.5) * 0.16
        t = np.clip(t, 0, 1)
        t = t * t * (3 - 2 * t)
        ivory = IVORY / 255.0
        out = ivory * (1 - t[..., None]) + c * t[..., None]
        return (np.clip(out, 0, 1) * 255).astype(np.uint8)


# ---------- reusable scene elements -------------------------------------

def sky(P, y_top, y_bot, c_top=NAVY, c_bot=TEAL):
    P.vgrad(y_top, y_bot, c_top, c_bot, mask=rect(-5, y_top, SW + 5, y_bot), wob=2, rim=0, vary=0.10)


def moon(P, x, y, r=34):
    P.glow(x, y, r * 3.2, GOLD, 0.35)
    P.layer(ell(x, y, r, r), (246, 232, 190), op=0.98, wob=1.5, rim=0.1)
    P.glow(x, y, r * 1.2, CREAM, 0.5)


def moon_reflection(P, x, y0, y1, n=26, seed=4):
    r = np.random.default_rng(seed)
    for i in range(n):
        t = i / n
        y = y0 + (y1 - y0) * t
        w = 90 * (1 - 0.5 * t) * r.uniform(0.35, 1.0)
        xx = x + r.normal(0, 18 * (0.4 + t))
        P.layer(ell(xx, y, w, 1.6 + 1.6 * t), (244, 214, 140), op=r.uniform(0.35, 0.8), wob=0, rim=0, grain=0.04, soft=0.7)


def sea(P, y_top, y_bot, c_top=DTEAL, c_bot=NAVY, seed=2):
    P.vgrad(y_top, y_bot, c_top, c_bot, mask=rect(-5, y_top, SW + 5, y_bot), wob=2, rim=0, vary=0.08)
    P.strokes(0, SW, y_top + 6, y_bot, 55, (70, 128, 138), op=0.22, seed=seed)
    P.strokes(0, SW, y_top + 6, y_bot, 40, (8, 22, 44), op=0.22, seed=seed + 1)


def house(P, x, y, w, h, roof=OCHRE_D, body=(150, 160, 150), lit=True, seed=0, pencil=True):
    # body
    P.layer(rect(x, y, x + w, y + h), body, op=0.95, wob=2, rim=0.3)
    # roof
    P.layer(poly([(x - 6, y + 2), (x + w / 2, y - h * 0.55), (x + w + 6, y + 2)]), roof, op=0.97, wob=2, rim=0.3)
    # windows
    nwin = 2 if w > 40 else 1
    ww, wh = max(7, w * 0.16), max(9, h * 0.30)
    for i in range(nwin):
        cx = x + w * (0.3 + 0.4 * i) if nwin == 2 else x + w / 2
        wy = y + h * 0.28
        if lit:
            P.glow(cx, wy + wh / 2, 22, WARM, 0.55)
            P.layer(rect(cx - ww / 2, wy, cx + ww / 2, wy + wh), WARM, op=0.98, wob=0.5, rim=0, grain=0.04, soft=0.5)
        else:
            P.layer(rect(cx - ww / 2, wy, cx + ww / 2, wy + wh), (60, 80, 92), op=0.9, wob=0.5, rim=0)
    if pencil:
        P.line([(x, y + h), (x, y), (x + w / 2, y - h * 0.55), (x + w, y), (x + w, y + h)], w=2, alpha=0.5)


def person(P, x, ybase, h, coat=OCHRE, hair=HAIR, trousers=NAVY, sit=False, profile=0.0):
    """Adult figure seen from behind. x center, ybase = feet y, h = total height."""
    top = ybase - h
    hr = 0.062 * h
    cy_head = top + hr
    neck_y = top + 2 * hr
    sh_y = neck_y + 0.03 * h
    sw_ = 0.135 * h
    hem_y = ybase - 0.42 * h
    hem_w = 0.17 * h
    if sit:
        hem_y = ybase - 0.10 * h
    # legs
    if not sit:
        P.layer(rect(x - 0.075 * h, hem_y - 4, x - 0.012 * h, ybase - 0.02 * h), trousers, op=0.97, wob=1.5, rim=0.2)
        P.layer(rect(x + 0.012 * h, hem_y - 4, x + 0.075 * h, ybase - 0.02 * h), trousers, op=0.97, wob=1.5, rim=0.2)
        P.layer(ell(x - 0.05 * h, ybase - 0.012 * h, 0.05 * h, 0.018 * h), (20, 18, 20), op=0.97, wob=1)
        P.layer(ell(x + 0.05 * h, ybase - 0.012 * h, 0.05 * h, 0.018 * h), (20, 18, 20), op=0.97, wob=1)
    # coat body
    body = [(x - sw_, sh_y), (x - sw_ * 0.55, neck_y), (x + sw_ * 0.55, neck_y), (x + sw_, sh_y),
            (x + hem_w, hem_y), (x - hem_w, hem_y)]
    P.layer(poly(body), coat, op=0.98, wob=1.5, rim=0.28)
    # sleeves
    sl = (int(coat[0] * 0.82), int(coat[1] * 0.82), int(coat[2] * 0.82))
    P.layer(poly([(x - sw_, sh_y), (x - sw_ - 0.03 * h, sh_y + 0.10 * h), (x - sw_ - 0.02 * h, hem_y - 0.10 * h),
                  (x - sw_ + 0.03 * h, hem_y - 0.10 * h), (x - sw_ * 0.75, sh_y + 0.05 * h)]), sl, op=0.97, wob=1.2, rim=0.2)
    P.layer(poly([(x + sw_, sh_y), (x + sw_ + 0.03 * h, sh_y + 0.10 * h), (x + sw_ + 0.02 * h, hem_y - 0.10 * h),
                  (x + sw_ - 0.03 * h, hem_y - 0.10 * h), (x + sw_ * 0.75, sh_y + 0.05 * h)]), sl, op=0.97, wob=1.2, rim=0.2)
    # center seam + collar
    P.line([(x, neck_y + 0.02 * h), (x, hem_y)], w=2, alpha=0.35, color=(80, 50, 20))
    # neck, head, hair
    P.layer(rect(x - 0.022 * h, neck_y - 0.012 * h, x + 0.022 * h, neck_y + 0.02 * h), SKIN, op=0.95, wob=0.8)
    P.layer(ell(x + profile * hr, cy_head, hr * 0.95, hr * 1.08), hair, op=0.98, wob=0.8, rim=0.2)
    P.layer(ell(x + profile * hr, cy_head - hr * 0.1, hr * 0.98, hr * 0.92), hair, op=0.98, wob=0.8, rim=0.0)
    P.line(body + [body[0]], w=2, alpha=0.4, color=(70, 44, 18))
    return (x, cy_head)


def leafy(P, cx, cy, r, color=MOSS, n=18, seed=1, op=0.95):
    rr = np.random.default_rng(seed)
    for _ in range(n):
        a = rr.uniform(0, 6.28)
        d = rr.uniform(0, r)
        rx = rr.uniform(r * 0.25, r * 0.5)
        ry = rr.uniform(r * 0.18, r * 0.35)
        col = tuple(int(c * rr.uniform(0.8, 1.2)) for c in color)
        col = tuple(min(255, max(0, c)) for c in col)
        P.layer(ell(cx + np.cos(a) * d, cy + np.sin(a) * d * 0.8, rx, ry), col, op=op, wob=3, rim=0.25, soft=1.2)
