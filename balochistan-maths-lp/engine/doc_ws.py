"""Student Worksheet, Level 1 Maths Day 1. Same format as the approved English Worksheet v2:
page 1 = the You Do tasks, page 2 = the Exit Check. Black and white friendly, one pale accent,
a printed solved example that is NOT one of the questions."""
from common import *

FOOT = f"{LEVEL} · Day 1 · Student Worksheet"
CSS_WS = """
.ws .content{top:9mm;bottom:15mm}
.ws h1{margin:0;font-size:21pt;font-weight:900;color:#000;line-height:1.1}
.idrow{display:flex;gap:7mm;font-size:11pt;margin:2.4mm 0 2.6mm;font-weight:600}
.idrow span{flex:1;border-bottom:.4mm solid #000;padding-bottom:.5mm;white-space:nowrap}
.task{border:.5mm solid #000;border-radius:3.5mm;padding:2.2mm 4mm 2.2mm;margin-bottom:2.4mm;position:relative}
.task .hd{display:flex;align-items:center;gap:3mm;margin-bottom:1.6mm;font-size:12pt;font-weight:800}
.task .n{width:8mm;height:8mm;border-radius:50%;background:#FBE9B5;border:.5mm solid #000;display:flex;align-items:center;justify-content:center;font-size:12pt;font-weight:900;flex:none}
.bx{display:inline-flex;align-items:center;justify-content:center;font-family:Nunito,sans-serif;font-weight:800;color:#000;border:.5mm solid #000;border-radius:2mm;background:#fff}
.dot{width:3.4mm;height:3.4mm;border:.5mm solid #000;border-radius:50%;display:inline-block;background:#fff;flex:none}
.grp{border:.35mm dashed #777;border-radius:2.4mm;padding:.4mm 1.6mm;display:flex;align-items:center;justify-content:center;background:#fff}
.gray{filter:grayscale(1) contrast(1.05)}
"""


def foot_ws(n):
    return foot(FOOT, n, 2)


def G(n, obj, layout="row", cell=7, seed=1, max_h=None, aspect=1.5):
    return group_svg(n, obj, layout, mode="l", cell_mm=cell, seed=seed, max_h_mm=max_h, aspect=aspect)


def mrow(n, obj, right, ex=False):
    """Task 1 row: group (left), connector dot, connector dot, number (right)."""
    lab = ('<span class="small" style="position:absolute;left:50%;top:2.2mm;font-weight:800;color:#000;transform:translateX(-50%);background:#fff;padding:0 1.5mm">Example: 5 cups, number 5</span>' if ex else "")
    line = ('<span style="flex:1;position:relative;height:4mm"><svg width="100%" height="100%" viewBox="0 0 100 4" preserveAspectRatio="none" style="position:absolute;left:0;top:0"><line x1="0" y1="2" x2="100" y2="2" stroke="#000" stroke-width=".8" vector-effect="non-scaling-stroke"/></svg></span>'
            if ex else '<span style="flex:1"></span>')
    return (f'<div style="display:flex;align-items:center;gap:2mm;height:16.2mm;position:relative;{"border-bottom:.3mm dashed #888;margin-bottom:1mm;" if ex else ""}">{lab}'
            f'<div class="grp" style="width:80mm;height:14.6mm">{G(n, obj, "row", 6.6)}</div>'
            f'<i class="dot"></i>{line}<i class="dot"></i>'
            f'<span class="bx" style="width:17mm;height:10mm;font-size:18pt;margin-right:3mm">{right}</span></div>')


def crow(i, n, obj, layout, opts, cell, h, bw=18, bh=10.4, fs=21, gw=88):
    boxes = "".join(f'<span class="bx" style="width:{bw}mm;height:{bh}mm;font-size:{fs}pt">{o}</span>' for o in opts)
    return (f'<div style="display:flex;align-items:center;gap:3mm;height:{h}mm"><span style="font-weight:800;width:5mm;font-size:11pt">{i}</span>'
            f'<div class="grp" style="width:{gw}mm;height:{h - 1.2}mm">{G(n, obj, layout, cell, seed=i)}</div>{boxes}</div>')


def page1():
    ex = mrow(WS_EXAMPLE[0], WS_EXAMPLE[1], WS_EXAMPLE[0], ex=True)
    rows = "".join(mrow(g[0], g[1], r) for g, r in zip(T1, T1_RIGHT))
    t2 = "".join(crow(i + 1, n, o, l, opts, 6.4, 14.8) for i, (n, o, l, opts) in enumerate(T2))
    t3 = ""
    for i, (n, o, c) in enumerate(T3):
        t3 += (f'<div style="display:flex;align-items:center;gap:3mm;height:16mm"><span style="font-weight:800;width:5mm;font-size:11pt">{"ab"[i]}</span>'
               f'<div class="grp" style="width:90mm;height:14.6mm">{G(n, o, "row", 7 if n <= 10 else 5.6)}</div>'
               f'<div style="font-size:11pt;font-weight:700">Colour <span class="k" style="font-size:15pt;margin:0 .6mm">{c}</span> {pl(o)}.</div></div>')
    return f"""<section class="page ws"><div class="content">
 <div style="display:flex;align-items:center;gap:5mm">
  <div style="flex:1"><div class="small" style="font-weight:700;color:#000">Level 1 Maths · Day 1</div><h1>Count and Say How Many</h1></div>
  <div style="width:19mm" class="gray">{scene("kids_wave")}</div></div>
 <div class="idrow"><span>Name</span><span style="flex:.55">Class</span><span style="flex:.8">Date</span></div>

 <div class="task"><div class="hd"><span class="n">1</span>Match each group to its number.</div>{ex}{rows}</div>
 <div class="task"><div class="hd"><span class="n">2</span>Count. Circle how many.</div>{t2}</div>
 <div class="task" style="margin-bottom:0"><div class="hd"><span class="n">3</span>Count and colour.</div>{t3}</div>
</div>{foot_ws(1)}</section>"""


def page2():
    rows = ""
    for i, (n, o, l, opts) in enumerate(EXIT):
        boxes = "".join(f'<span class="bx" style="width:19mm;height:14mm;font-size:26pt">{x}</span>' for x in opts)
        cell = 7.2
        rows += (f'<div style="display:flex;align-items:center;gap:4mm;height:27.5mm;border-bottom:.3mm dashed #999"><span style="font-weight:900;font-size:15pt;width:7mm">{i+1}</span>'
                 f'<div class="grp" style="width:88mm;height:23mm">{G(n, o, l, cell, seed=i + 2, max_h=21.5, aspect=3.3 if l == "scatter" else 1.5)}</div>{boxes}</div>')
    return f"""<section class="page ws"><div class="content">
 <div style="display:flex;align-items:center;gap:5mm">
  <div style="flex:1"><div class="small" style="font-weight:700;color:#000">Level 1 Maths · Day 1</div><h1>Exit Check: Count and Circle</h1></div>
  <div style="border:.6mm solid #000;border-radius:3mm;padding:1.6mm 4mm;font-weight:900;font-size:15pt">Score: ____ / 8</div></div>
 <div class="idrow"><span>Name</span><span style="flex:.6">Date</span></div>
 <div style="margin-top:1mm">{rows}</div>
 <div style="display:flex;align-items:center;gap:5mm;margin-top:3mm">
  <div class="gray" style="width:20mm">{scene("kids_wave")}</div>
  <div style="flex:1;border:.5mm solid #000;border-radius:3.5mm;padding:2.4mm 4mm;background:#FBE9B5"><b style="font-size:13pt">Well done!</b><br><span style="font-size:10.5pt">You can count and say how many.</span></div>
  <div style="border:.4mm solid #000;border-radius:3mm;padding:2mm 3mm;font-size:8.5pt;line-height:1.3;width:44mm"><b>Teacher</b><br>☐ Part B: counted three groups aloud</div></div>
</div>{foot_ws(2)}</section>"""


def build():
    html = head_html("Level 1 Maths Day 1 - Student Worksheet").replace("</style>", CSS_WS + "</style>") + page1() + page2() + OVERFLOW_JS
    out = os.path.join(WORK, "ws.html")
    open(out, "w", encoding="utf-8").write(html)
    return out


if __name__ == "__main__":
    print(build())
