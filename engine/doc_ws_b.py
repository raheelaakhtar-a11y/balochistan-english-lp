"""Level 1 Beginner, English, Day 1 (final planner): Student Worksheet (B&W friendly, no Rumi logo)."""
from common_b import *

CSS_WS = FONT_CSS + """
.ws .content{top:9mm;bottom:15mm}
.ws h1{margin:0;font-size:21pt;font-weight:700;color:#000;line-height:1.1}
.idrow{display:flex;gap:7mm;font-size:11pt;margin:3mm 0 3mm;font-weight:600}
.idrow span{flex:1;border-bottom:.4mm solid #000;padding-bottom:.5mm;white-space:nowrap}
.task{border:.5mm solid #000;border-radius:3.5mm;padding:2.4mm 4mm 2.6mm;margin-bottom:3mm;position:relative}
.task .hd{display:flex;align-items:center;gap:3mm;margin-bottom:1.6mm;font-size:12pt;font-weight:800}
.task .hd .chk{margin-left:auto;font-size:8.5pt;font-weight:600}
.task .n{width:8mm;height:8mm;border-radius:50%;background:#FBE9B5;border:.5mm solid #000;display:flex;align-items:center;justify-content:center;font-size:12pt;font-weight:900;flex:none}
.bx{display:inline-flex;align-items:center;justify-content:center;font-family:Andika,sans-serif;font-weight:700;color:#000;border:.5mm solid #000;border-radius:2mm;background:#fff}
.dot{width:3.4mm;height:3.4mm;border:.5mm solid #000;border-radius:50%;display:inline-block;background:#fff;flex:none}
.mrow{display:flex;align-items:center;justify-content:space-between;height:11mm}
.tc{width:25mm;height:15mm;border-bottom:.45mm solid #000;display:inline-flex;align-items:flex-end;justify-content:center;font-family:Andika,sans-serif;font-weight:400;font-size:38pt;line-height:.82;color:#BDBDBD;margin-right:1.4mm}
.tc.blank{color:transparent}
.gray{filter:grayscale(1) contrast(1.05)}
.pc{width:14mm}
"""


def foot_ws(n):
    return foot(FOOT_WS, n, 2, mark=None)


def page1():
    t1 = ""
    for cap, small in T1_ROWS:
        t1 += (f'<div style="display:flex;align-items:flex-end;height:15.6mm"><span class="tc">{cap}</span><span class="tc">{small}</span>'
               f'<span class="tc">{cap}</span><span class="tc">{small}</span><span class="tc blank">.</span><span class="tc blank">.</span></div>')
    t2 = "".join(
        f'<div class="mrow"><span class="bx" style="width:16mm;height:9mm;font-size:18pt;margin-left:17mm">{c}</span>'
        f'<span style="display:flex;align-items:center;flex:1;justify-content:space-between;padding:0 2mm"><i class="dot"></i><i class="dot"></i></span>'
        f'<span class="bx" style="width:16mm;height:9mm;font-size:18pt;margin-right:17mm">{s}</span></div>' for c, s in zip(T2_CAPS, T2_SMALLS))
    t3 = "".join(
        f'<div class="mrow" style="height:14.4mm"><span style="width:15mm;margin-left:14mm;display:inline-block" class="gray">{wpic(p, "pc")}</span>'
        f'<span style="display:flex;align-items:center;flex:1;justify-content:space-between;padding:0 2mm"><i class="dot"></i><i class="dot"></i></span>'
        f'<span class="bx" style="width:16mm;height:9mm;font-size:18pt;margin-right:17mm">{L}</span></div>' for p, L in zip(T3_PICS, "ABCD"))
    return f"""<section class="page ws"><div class="content">
 <div style="display:flex;align-items:center;gap:5mm">
  <div style="flex:1"><div class="small" style="font-weight:700;color:#000">Level 1 English · Day 1</div><h1>Meet A, B, C and D</h1></div>
  <div style="width:19mm" class="gray">{scene("kids_wave")}</div></div>
 <div class="idrow"><span>Name</span><span style="flex:.55">Class</span><span style="flex:.8">Date</span></div>

 <div class="task"><div class="hd"><span class="n">1</span>Trace the letters. Then copy them.<span class="chk">Check: your Letter Strip</span></div>{t1}</div>
 <div class="task"><div class="hd"><span class="n">2</span>Draw a line from the big letter to its small partner.<span class="chk">Check: your Letter Strip</span></div>{t2}</div>
 <div class="task" style="margin-bottom:0"><div class="hd"><span class="n">3</span>Draw a line from the picture to its first letter.<span class="chk">Check: your Letter Strip</span></div>{t3}</div>
</div>{foot_ws(1)}</section>"""


def page2():
    rows = ""
    for i, it in enumerate(EXIT):
        if it["options"]:
            boxes = "".join(f'<span class="bx" style="width:32mm;height:19mm;font-size:36pt">{o}</span>' for o in it["options"])
        else:
            boxes = '<span style="display:inline-block;width:70mm;height:19mm;border-bottom:.5mm solid #000"></span>'
        rows += f'<div style="display:flex;align-items:center;gap:7mm;height:27mm;border-bottom:.3mm dashed #999"><span style="font-weight:900;font-size:16pt;width:8mm">{i+1}</span>{boxes}</div>'
    return f"""<section class="page ws"><div class="content">
 <div style="display:flex;align-items:center;gap:5mm">
  <div style="flex:1"><div class="small" style="font-weight:700;color:#000">Level 1 English · Day 1</div><h1>Exit Check: Listen and Show</h1></div>
  <div style="border:.6mm solid #000;border-radius:3mm;padding:1.6mm 4mm;font-weight:900;font-size:15pt">Score: ____ / 5</div></div>
 <div class="idrow"><span>Name</span><span style="flex:.6">Date</span></div>
 <div style="margin-top:2mm">{rows}</div>
 <div style="display:flex;align-items:center;gap:5mm;margin-top:5mm">
  <div class="gray" style="width:24mm">{scene("kids_wave")}</div>
  <div style="flex:1;border:.5mm solid #000;border-radius:3.5mm;padding:3mm 4mm;background:#FBE9B5"><b style="font-size:13pt">Well done!</b><br><span style="font-size:10.5pt">You are learning the letters A, B, C and D.</span></div>
  <div style="border:.4mm solid #000;border-radius:3mm;padding:2mm 3mm;font-size:8.5pt;line-height:1.3;width:44mm"><b>Teacher</b><br>&#9744; Part B: said a name and a sound</div></div>
</div>{foot_ws(2)}</section>"""


def build():
    html = head_html("Level 1 English Day 1 - Student Worksheet").replace("</style>", CSS_WS + "</style>") + page1() + page2() + OVERFLOW_JS
    out = os.path.join(WORK, "wsb.html")
    open(out, "w", encoding="utf-8").write(html)
    return out


if __name__ == "__main__":
    print(build())
