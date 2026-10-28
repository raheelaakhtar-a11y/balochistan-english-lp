"""Student Worksheet v4, Level 1 Maths Day 1. English worksheet design (black and white friendly, one pale accent,
printed solved examples that are NOT questions), maths tasks: count and circle, draw the dots in Ten Boxes, join the dots 1 to 20.
Page 1 = You Do, page 2 = Exit Check."""
from common_m6 import *
from doc_ws import CSS_WS, foot_ws, G

EXTRA = """
.bx.sm{border-radius:1.6mm}
.dash{border:.4mm dashed #888;border-radius:2.4mm}
"""


def hdr(title, right=""):
    return (f'<div style="display:flex;align-items:center;gap:5mm"><div style="flex:1"><div class="small" style="font-weight:700;color:#000">Level 1 Maths · Day 1</div><h1>{title}</h1></div>{right}</div>')


def circle_row(i, n, obj, layout, opts, h=14.4, cell=6.4, bw=18, bh=10.4, fs=21, gw=88, max_h=None, aspect=1.5, label=None):
    boxes = "".join(f'<span class="bx" style="width:{bw}mm;height:{bh}mm;font-size:{fs}pt">{o}</span>' for o in opts)
    lab = f'<span style="font-weight:800;width:6mm;font-size:11pt">{label if label is not None else i}</span>'
    return (f'<div style="display:flex;align-items:center;gap:3mm;height:{h}mm">{lab}'
            f'<div class="grp" style="width:{gw}mm;height:{h - 1.2}mm">{G(n, obj, layout, cell, seed=i, max_h=max_h or (h - 2.4), aspect=aspect)}</div>{boxes}</div>')


def draw_row(label, numeral, frames, h=15.2, w=None, filled=0, gw=None):
    w = w or {1: 31, 2: 62}[frames]
    box = boxes_svg(frames, filled, w_mm=w, mode="l")
    return (f'<div style="display:flex;align-items:center;gap:4mm;height:{h}mm"><span style="font-weight:800;width:6mm;font-size:11pt">{label}</span>'
            f'<span class="bx" style="width:19mm;height:11.4mm;font-size:22pt">{numeral}</span>'
            f'<div class="grp" style="flex:1;height:{h - 1.4}mm;justify-content:flex-start;padding-left:3mm">{box}</div></div>')


def page1():
    rows1 = "".join(circle_row(i + 1, n, o, l, opts, aspect=3.4) for i, (n, o, l, opts) in enumerate(T1))
    ex2 = draw_row("Ex", T2_EX, 1, filled=T2_EX)
    rows2 = "".join(draw_row(i + 1, n, 1 if n <= 10 else 2) for i, n in enumerate(T2))
    return f"""<section class="page ws"><div class="content">
 {hdr("Count, Draw and Join", f'<div style="width:19mm" class="gray">{scene("kids_wave")}</div>')}
 <div class="idrow"><span>Name</span><span style="flex:.55">Class</span><span style="flex:.8">Date</span></div>

 <div class="task"><div class="hd"><span class="n">1</span>Count the objects. Circle how many.</div>
  <div style="border-bottom:.3mm dashed #888;margin-bottom:.6mm">{ex1_with_circle()}</div>{rows1}</div>
 <div class="task"><div class="hd"><span class="n">2</span>Draw one dot in a box for each count.</div>
  <div style="border-bottom:.3mm dashed #888;margin-bottom:.6mm">{ex2}</div>{rows2}</div>
 <div class="task" style="margin-bottom:0"><div class="hd"><span class="n">3</span>Join the dots in order, from 1 to 20.</div>
  <div style="display:flex;align-items:center;gap:6mm"><div style="flex:none">{dotdot_svg(60)}</div>
   <div style="font-size:10.6pt;line-height:1.5;flex:1"><b>Start at 1.</b><br>Draw a line to 2, then 3, then 4. Keep going to 20.<br>Then go back to 1.</div></div></div>
</div>{foot_ws(1)}</section>"""


def ex1_with_circle():
    n, o, l, opts = T1_EX
    boxes = "".join(f'<span class="bx" style="width:18mm;height:10.4mm;font-size:21pt;{"border-radius:50%;border-width:.9mm;" if x == n else ""}">{x}</span>' for x in opts)
    return (f'<div style="display:flex;align-items:center;gap:3mm;height:14.4mm"><span style="font-weight:800;width:6mm;font-size:9pt">Ex</span>'
            f'<div class="grp" style="width:88mm;height:13.2mm">{G(n, o, l, 6.4, seed=9, max_h=12)}</div>{boxes}</div>')


def page2():
    rows = ""
    for i, e in enumerate(EXIT):
        if e[0] == "c":
            _, n, o, l, opts = e
            cell = 7.2
            rows += (f'<div style="display:flex;align-items:center;gap:4mm;height:25.8mm;border-bottom:.3mm dashed #999"><span style="font-weight:900;font-size:15pt;width:7mm">{i+1}</span>'
                     f'<div class="grp" style="width:88mm;height:21.4mm">{G(n, o, l, cell, seed=i + 2, max_h=19.5, aspect=3.3 if l == "scatter" else 1.5)}</div>'
                     + "".join(f'<span class="bx" style="width:19mm;height:14mm;font-size:26pt">{x}</span>' for x in opts) + '</div>')
        else:
            n = e[1]
            frames = 1 if n <= 10 else 2
            rows += (f'<div style="display:flex;align-items:center;gap:4mm;height:25.8mm;border-bottom:.3mm dashed #999"><span style="font-weight:900;font-size:15pt;width:7mm">{i+1}</span>'
                     f'<div style="width:88mm;display:flex;align-items:center;gap:4mm"><span class="bx" style="width:22mm;height:15mm;font-size:28pt">{n}</span>'
                     f'<div class="grp" style="flex:1;height:19mm;justify-content:flex-start;padding-left:3mm">{boxes_svg(frames, 0, w_mm=36 if frames == 1 else 70, mode="l")}</div></div>'
                     f'<span class="small" style="color:#000;font-weight:600;line-height:1.25;width:58mm">Draw {n} dots.<br>One dot in each box.</span></div>')
    return f"""<section class="page ws"><div class="content">
 {hdr("Exit Check: Count and Show", '<div style="border:.6mm solid #000;border-radius:3mm;padding:1.6mm 4mm;font-weight:900;font-size:15pt">Score: ____ / 8</div>')}
 <div class="idrow"><span>Name</span><span style="flex:.6">Date</span></div>
 <div style="margin-top:1mm">{rows}</div>
 <div style="display:flex;align-items:center;gap:5mm;margin-top:3mm">
  <div class="gray" style="width:20mm">{scene("kids_wave")}</div>
  <div style="flex:1;border:.5mm solid #000;border-radius:3.5mm;padding:2.4mm 4mm;background:#FBE9B5"><b style="font-size:13pt">Well done!</b><br><span style="font-size:10.5pt">You can count and say how many.</span></div>
  <div style="border:.4mm solid #000;border-radius:3mm;padding:2mm 3mm;font-size:8.5pt;line-height:1.3;width:44mm"><b>Teacher</b><br>☐ Part B: counted out the stones</div></div>
</div>{foot_ws(2)}</section>"""


def build():
    html = head_html("Level 1 Maths Day 1 - Student Worksheet v6").replace("</style>", CSS_WS + EXTRA + "</style>") + page1() + page2() + OVERFLOW_JS
    out = os.path.join(WORK, "ws6.html")
    open(out, "w", encoding="utf-8").write(html)
    return out


if __name__ == "__main__":
    print(build())
