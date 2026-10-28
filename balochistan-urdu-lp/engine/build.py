"""Build step: process pictures -> render each document to PDF with headless Edge -> overflow check -> page PNGs.
usage: build.py [lp|prep|ws ...]   (default: all that exist)"""
import os, re, subprocess, sys, glob, warnings
warnings.filterwarnings("ignore")
from PIL import Image

WORK = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(WORK, "img", "raw")
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
    import time
    for _ in range(60):
        if os.path.exists(pdf) and os.path.getsize(pdf) > 1000:
            break
        time.sleep(0.5)
    ok = os.path.exists(pdf)
    ovf = "no-report"
    if ok:
        import pymupdf
        t = pymupdf.open(pdf).metadata.get("title") or ""
        ovf = t[4:] if t.startswith("OVF:") else "no-report"
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
    which = sys.argv[1:] or ["lpu", "prepu", "wsu"]
    mods = {"lpu": "doc_lp_u", "prepu": "doc_prep_u", "wsu": "doc_ws_u", "lpu2": "doc_lp_u2", "prepu2": "doc_prep_u2", "wsu2": "doc_ws_u2", "lpu3": "doc_lp_u3", "prepu3": "doc_prep_u3", "lpu4": "doc_lp_u4", "lpi": "doc_lp_i", "prepi": "doc_prep_i", "wsi": "doc_ws_i", "wsi2": "doc_ws_i2", "lpn": "doc_lp_n", "prepn": "doc_prep_n", "wsn": "doc_ws_n", "lpa": "doc_lp_a", "prepa": "doc_prep_a", "wsa": "doc_ws_a"}
    sys.path.insert(0, WORK)
    for w in which:
        if not os.path.exists(os.path.join(WORK, mods[w] + ".py")):
            continue
        __import__(mods[w]).build()
        pdf, ok, ovf = render(w)
        pages = pngs(w)[0] if ok else 0
        print(f"{w}: pdf={ok} pages={pages} overflow={ovf}")
