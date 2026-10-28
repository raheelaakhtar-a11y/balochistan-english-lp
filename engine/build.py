"""Build step: process pictures -> render each document to PDF with headless Edge -> overflow check -> page PNGs.
usage: build.py [lp|prep|ws ...]   (default: all that exist)"""
import os, re, subprocess, sys, glob, warnings
warnings.filterwarnings("ignore")
from PIL import Image

WORK = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(os.path.dirname(WORK), "img", "raw")
IMG = os.path.join(WORK, "img")
EDGE = os.environ.get("EDGE_PATH", r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
os.makedirs(IMG, exist_ok=True)


def process_images():
    n = 0
    for f in glob.glob(os.path.join(RAW, "*.png")):
        out = os.path.join(IMG, os.path.basename(f)[:-4] + ".jpg")
        if os.path.exists(out) and os.path.getmtime(out) >= os.path.getmtime(f):
            continue
        im = Image.open(f).convert("RGB")
        im.thumbnail((760, 760))
        im.save(out, quality=88, optimize=True)
        n += 1
    return n


def edge(args, timeout=180):
    return subprocess.run([EDGE, "--headless=new", "--disable-gpu", "--no-first-run", "--hide-scrollbars"] + args,
                          capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=timeout)


def render(name):
    html = os.path.join(WORK, f"{name}.html")
    pdf = os.path.join(WORK, f"{name}.pdf")
    url = "file:///" + html.replace("\\", "/")
    if os.path.exists(pdf):
        os.remove(pdf)
    r = edge(["--no-pdf-header-footer", f"--print-to-pdf={pdf}", "--virtual-time-budget=8000", url])
    d = edge(["--dump-dom", "--virtual-time-budget=8000", url])
    m = re.search(r'name="ovf" content="([^"]*)"', d.stdout)
    ovf = m.group(1) if m else "no-report"
    ok = os.path.exists(pdf)
    return pdf, ok, ovf


def pngs(name, dpi=70):
    import pymupdf
    pdf = os.path.join(WORK, f"{name}.pdf")
    d = pymupdf.open(pdf)
    outs = []
    for i, p in enumerate(d):
        o = os.path.join(WORK, "png", f"{name}_p{i+1}.png")
        os.makedirs(os.path.dirname(o), exist_ok=True)
        p.get_pixmap(dpi=dpi).save(o)
        outs.append(o)
    return len(d), outs


if __name__ == "__main__":
    print("images processed:", process_images())
    which = sys.argv[1:] or ["lpi", "prepi", "wsi"]
    mods = {"lp": "doc_lp", "prep": "doc_prep", "ws": "doc_ws", "lpi": "doc_lp_i", "prepi": "doc_prep_i", "wsi": "doc_ws_i",
            "lpb": "doc_lp_b", "lpc": "doc_lp_c", "prepb": "doc_prep_b", "wsb": "doc_ws_b"}
    sys.path.insert(0, WORK)
    for w in which:
        if not os.path.exists(os.path.join(WORK, mods[w] + ".py")):
            continue
        __import__(mods[w]).build()
        pdf, ok, ovf = render(w)
        pages = pngs(w)[0] if ok else 0
        print(f"{w}: pdf={ok} pages={pages} overflow={ovf}")
