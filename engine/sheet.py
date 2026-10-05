import sys, glob
from PIL import Image, ImageDraw
prefix = sys.argv[1]; out = sys.argv[2]
files = sorted(glob.glob(f"art_w42/{prefix}*.png"))
cols = 4; tw, th = 480, 284
rows = (len(files)+cols-1)//cols
sh = Image.new("RGB", (cols*tw, rows*th), (246,239,224))
d = ImageDraw.Draw(sh)
for i,f in enumerate(files):
    im = Image.open(f).resize((tw, th))
    sh.paste(im, ((i%cols)*tw, (i//cols)*th))
    d.text(((i%cols)*tw+6, (i//cols)*th+4), f.split('/')[-1][:-4], fill=(0,0,0))
sh.save(out)
