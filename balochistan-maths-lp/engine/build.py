"""Build step: process scene pictures -> render each document to PDF with headless Edge -> overflow check -> page PNGs.
usage: python -W ignore build.py [lp|prep|ws ...]   (default: all three)
Run from PowerShell, not bash (a bash-launched Edge silently fails to write the PDF)."""
import os, re, subprocess, sys, glob, warnings
warnings.filterwarnings("ignore")
from PIL import Image

WORK = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(WORK, "img", "raw")
IMG = os.path.join(WORK, "img")
EDGE = os.environ.get("EDGE_PATH", r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
os.makedirs(IMG, exist_ok=True)


def process_images():
    """img/raw/*.png (from kie_gen.py) -> img/*.jpg (what the documents read)."""
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
    edge(["--no-pdf-header-footer", f"--print-to-pdf={pdf}", "--virtual-time-budget=8000", url])
    d = edge(["--dump-dom", "--virtual-time-budget=8000", url])
    m = re.search(r'name="ovf" content="([^"]*)"', d.stdout)
    return pdf, os.path.exists(pdf), (m.group(1) if m else "no-report")


def pngs(name, dpi=70):
    import pymupdf
    d = pymupdf.open(os.path.join(WORK, f"{name}.pdf"))
    outs = []
    for i, p in enumerate(d):
        o = os.path.join(WORK, "png", f"{name}_p{i+1}.png")
        os.makedirs(os.path.dirname(o), exist_ok=True)
        p.get_pixmap(dpi=dpi).save(o)
        outs.append(o)
    return len(d), outs


# key -> (document module, html/pdf stem it writes). Day 1 (M-B-01). For another day copy a module and add a key.
MODS = {"lp": ("doc_lp_m8", "lp8"), "prep": ("doc_prep_m6", "prep6"), "ws": ("doc_ws_m6", "ws6")}

if __name__ == "__main__":
    print("images processed:", process_images())
    sys.path.insert(0, WORK)
    for w in (sys.argv[1:] or list(MODS)):
        mod, stem = MODS[w]
        __import__(mod).build()
        pdf, ok, ovf = render(stem)
        pages = pngs(stem)[0] if ok else 0
        print(f"{w}: pdf={ok} pages={pages} overflow={ovf}")
