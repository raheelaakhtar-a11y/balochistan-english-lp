"""Level 1 Beginner, Urdu, Day 1 (final planner): Student Worksheet (B&W friendly, no Rumi logo)."""
from common_u import *

CSS_WS = """
.ws .content{top:9mm;bottom:15mm}
.ws h1{margin:0;font-size:20pt;font-weight:700;color:#000;line-height:1.6}
.idrow{display:flex;gap:7mm;font-size:11pt;margin:.4mm 0 2mm;font-weight:700}
.idrow span{flex:1;border-bottom:.4mm solid #000;white-space:nowrap;line-height:1.8}
.task{border:.5mm solid #000;border-radius:3.5mm;padding:1.4mm 4mm 2mm;margin-bottom:2.6mm;position:relative}
.task .hd{display:flex;align-items:center;gap:3mm;margin-bottom:.4mm;font-size:11.5pt;font-weight:700;line-height:1.7}
.task .hd .ck{margin-inline-start:auto;font-size:8.6pt;font-weight:400}
.task .n{width:8mm;height:8mm;border-radius:50%;background:#FBE9B5;border:.5mm solid #000;display:flex;align-items:center;justify-content:center;font-size:12pt;font-weight:700;flex:none;line-height:1}
.bx{display:inline-flex;align-items:flex-start;justify-content:center;font-weight:400;color:#000;border:.5mm solid #000;border-radius:2mm;background:#fff;line-height:1.3;padding-top:.8mm}
.dot{width:3.4mm;height:3.4mm;border:.5mm solid #000;border-radius:50%;display:inline-block;background:#fff;flex:none}
.mrow{display:flex;align-items:center;justify-content:space-between;height:12.2mm}
.tc{width:19mm;height:14.2mm;border-bottom:.45mm solid #000;display:inline-flex;align-items:flex-start;justify-content:center;font-size:26pt;line-height:1.3;color:#BDBDBD;margin-inline-start:1.4mm}
.tc.blank{color:transparent}
.gray{filter:grayscale(1) contrast(1.05)}
"""


def foot_ws(n):
    return foot(FOOT_WS, n, 2)


def page1():
    t1 = ""
    for l in T1_LETTERS:
        t1 += (f'<div style="display:flex;align-items:flex-end;height:15mm"><span style="font-size:16pt;margin-inline-end:2mm;line-height:1.3">&#8592;</span>'
               f'<span class="tc">{l}</span><span class="tc">{l}</span><span class="tc">{l}</span><span class="tc blank">.</span><span class="tc blank">.</span></div>')
    t2 = "".join(
        f'<div class="mrow"><span style="margin-inline-start:12mm;display:inline-block" class="gray"><img src="img/u1_{PIC[p]}.jpg" style="width:11mm;height:11mm;object-fit:contain;display:block"></span>'
        f'<span style="display:flex;align-items:center;flex:1;justify-content:space-between;padding:0 2mm"><i class="dot"></i><i class="dot"></i></span>'
        f'<span class="bx" style="width:17mm;height:11.4mm;font-size:16pt;margin-inline-end:12mm">{l}</span></div>' for p, l in zip(T2_PICS, T2_LETTERS))
    t3 = ""
    for tg, opts in T3_ROWS:
        t3 += (f'<div style="display:flex;align-items:center;gap:2.4mm;margin-bottom:.8mm"><span class="bx" style="width:15mm;height:12.4mm;font-size:17pt;background:#FBE9B5">{tg}</span>'
               f'<span style="width:.5mm;height:9mm;background:#000;display:inline-block;margin:0 1mm"></span>'
               + "".join(f'<span class="bx" style="flex:1;height:12.4mm;font-size:17pt;border-color:#888">{o}</span>' for o in opts) + '</div>')
    return f"""<section class="page ws"><div class="content">
 <div style="display:flex;align-items:center;gap:5mm">
  <div style="flex:1"><div class="small" style="font-weight:700;color:#000;line-height:1.6">لیول ۱ اردو · دن ۱</div><h1>نئے حروف: {" · ".join(LETTERS)}</h1></div>
  <div style="width:19mm" class="gray">{scene("kids_wave")}</div></div>
 <div class="idrow"><span>نام</span><span style="flex:.55">جماعت</span><span style="flex:.8">تاریخ</span></div>

 <div class="task"><div class="hd"><span class="n">۱</span>حروف کو ٹریس کریں، پھر نقل کریں۔<span class="ck">جانچ: آپ کی ڈیسک پٹی</span></div>{t1}</div>
 <div class="task"><div class="hd"><span class="n">۲</span>تصویر سے اس کے پہلے حرف تک لکیر کھینچیں۔<span class="ck">جانچ: آپ کی ڈیسک پٹی</span></div>{t2}</div>
 <div class="task" style="margin-bottom:0"><div class="hd"><span class="n">۳</span>پہلے خانے جیسے حرف کے گرد دائرہ لگائیں۔<span class="ck">جانچ: آپ کی ڈیسک پٹی</span></div>{t3}</div>
</div>{foot_ws(1)}</section>"""


def page2():
    rows = ""
    for i, it in enumerate(EXIT):
        if it["options"]:
            boxes = "".join(f'<span class="bx" style="width:33mm;height:27mm;font-size:38pt;padding-top:1.6mm">{o}</span>' for o in it["options"])
        else:
            boxes = '<span style="display:inline-block;width:70mm;height:20mm;border-bottom:.5mm solid #000"></span>'
        rows += f'<div style="display:flex;align-items:center;gap:7mm;height:34mm;border-bottom:.3mm dashed #999"><span style="font-weight:700;font-size:16pt;width:8mm;line-height:1">{ur(i+1)}</span>{boxes}</div>'
    return f"""<section class="page ws"><div class="content">
 <div style="display:flex;align-items:center;gap:5mm">
  <div style="flex:1"><div class="small" style="font-weight:700;color:#000;line-height:1.6">لیول ۱ اردو · دن ۱</div><h1>خروجی جانچ: سنیں اور گھیریں</h1></div>
  <div style="border:.6mm solid #000;border-radius:3mm;padding:.4mm 4mm;font-weight:700;font-size:14pt;line-height:1.9">اسکور: ____ / ۵</div></div>
 <div class="idrow"><span>نام</span><span style="flex:.6">تاریخ</span></div>
 <div style="margin-top:1mm">{rows}</div>
 <div style="display:flex;align-items:center;gap:5mm;margin-top:4mm">
  <div class="gray" style="width:24mm">{scene("kids_wave")}</div>
  <div style="flex:1;border:.5mm solid #000;border-radius:3.5mm;padding:1mm 4mm;background:#FBE9B5"><b style="font-size:13pt;line-height:1.8">شاباش!</b><br><span style="font-size:10.5pt;line-height:1.8">آپ ا، ب، پ، ت اور ٹ سیکھ رہے ہیں۔</span></div>
  <div style="border:.4mm solid #000;border-radius:3mm;padding:.6mm 3mm;font-size:8.8pt;line-height:1.8;width:44mm"><b>استاد</b><br>&#9744; حصہ ب: آواز سنی</div></div>
</div>{foot_ws(2)}</section>"""


def build():
    html = head_html("Level 1 Urdu Day 1 - Student Worksheet").replace("</style>", CSS_WS + "</style>") + page1() + page2() + OVERFLOW_JS
    out = os.path.join(WORK, "wsu.html")
    open(out, "w", encoding="utf-8").write(html)
    return out


if __name__ == "__main__":
    print(build())
