import sys, os, time, importlib
from multiprocessing import Pool
from PIL import Image
BASE = os.path.dirname(os.path.abspath(__file__))
ART = f"{BASE}/art_w42"

def job(args):
    mod, name = args
    m = importlib.import_module(mod)
    t = time.time()
    arr = m.SCENES[name]()
    Image.fromarray(arr).save(f"{ART}/{name}.png")
    return name, round(time.time() - t, 1)

if __name__ == "__main__":
    os.makedirs(ART, exist_ok=True)
    mods = [a for a in sys.argv[1:] if a.startswith("scenes_")]
    only = [a for a in sys.argv[1:] if not a.startswith("scenes_")]
    jobs = []
    for mod in mods:
        m = importlib.import_module(mod)
        for n in m.SCENES:
            if not only or any(n.startswith(o) for o in only):
                jobs.append((mod, n))
    with Pool(min(8, os.cpu_count() or 2)) as p:
        for n, t in p.imap_unordered(job, jobs):
            print(n, t, flush=True)
