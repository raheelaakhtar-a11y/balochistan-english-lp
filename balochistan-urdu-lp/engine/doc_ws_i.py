"""Level 2 Intermediate, Urdu, Day 1 (final planner): Student Worksheet (B&W friendly, no Rumi logo)."""
from common_i import *

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
.mrow{display:flex;align-items:center;justify-content:space-between;height:14.6mm}
.gray{filter:grayscale(1) contrast(1.05)}
.ck2{width:6mm;height:6mm;border:.5mm solid #000;border-radius:1.2mm;display:inline-block;flex:none}
"""


def foot_ws(n):
    return foot(FOOT_WS, n, 2)


def page1():
    t1 = "".join(
        f'<div class="mrow"><span style="margin-inline-start:6mm;display:inline-block;font-size:16pt;font-weight:700;color:#000;line-height:1.5;min-width:36mm;text-align:right">{wd(w)}</span>'
        f'<span style="display:flex;align-items:center;flex:1;justify-content:space-between;padding:0 2mm"><i class="dot"></i><i class="dot"></i></span>'
        f'<span class="gray" style="margin-inline-end:8mm;display:inline-block"><img src="img/{W[p][2]}.jpg" style="width:12.4mm;height:12.4mm;object-fit:contain;display:block"></span></div>'
        for w, p in zip(T1, T1_PICS))
    t2 = "".join(f'<div style="display:flex;align-items:center;gap:4mm;height:11mm"><span class="ck2"></span><span style="font-size:17pt;font-weight:700;line-height:1.6">{p}</span></div>' for p in T2)
    t3 = ""
    for (k, l, m), opts in zip(T3, T3_OPTS):
        t3 += (f'<div style="display:flex;align-items:center;gap:2.4mm;margin-bottom:.8mm"><span class="bx" style="width:34mm;height:12.4mm;font-size:14pt;background:#FBE9B5;font-weight:700;padding-top:1.2mm">{wd(k)}</span>'
               f'<span style="width:.5mm;height:9mm;background:#000;display:inline-block;margin:0 1mm"></span>'
               + "".join(f'<span class="bx" style="flex:1;height:12.4mm;font-size:19pt;border-color:#888">{l}{MSYM[o]}</span>' for o in opts) + '</div>')
    return f"""<section class="page ws"><div class="content">
 <div style="display:flex;align-items:center;gap:5mm">
  <div style="flex:1"><div class="small" style="font-weight:700;color:#000;line-height:1.6">لیول ۲ اردو · دن ۱</div><h1>نشانیوں والے الفاظ پڑھیں</h1></div>
  <div style="width:19mm" class="gray">{scene("pair_book")}</div></div>
 <div class="idrow"><span>نام</span><span style="flex:.55">جماعت</span><span style="flex:.8">تاریخ</span></div>

 <div class="task"><div class="hd"><span class="n">۱</span>لفظ پڑھیں، پھر لکیر سے اس کی تصویر تک پہنچیں۔<span class="ck">جانچ: آپ کی ڈیسک پٹی</span></div>{t1}</div>
 <div class="task"><div class="hd"><span class="n">۲</span>جملہ ساتھی کو پڑھ کر سنائیں۔ ساتھی ٹک لگائے۔<span class="ck">جانچ: آپ کا ساتھی</span></div>{t2}</div>
 <div class="task" style="margin-bottom:0"><div class="hd"><span class="n">۳</span>لفظ کے پہلے حرف کی آواز کے گرد دائرہ لگائیں۔<span class="ck">جانچ: آپ کی ڈیسک پٹی</span></div>{t3}</div>
</div>{foot_ws(1)}</section>"""


def page2():
    rows = ""
    for i, it in enumerate(EXIT):
        opts = "".join(f'<span class="bx gray" style="width:30mm;height:25mm;padding:1.4mm;align-items:center"><img src="img/{W[o][2]}.jpg" style="width:22mm;height:22mm;object-fit:contain;display:block"></span>' for o in it["options"])
        fs = 24 if it["kind"] == "word" else 17
        rows += (f'<div style="display:flex;align-items:center;gap:6mm;height:34mm;border-bottom:.3mm dashed #999"><span style="font-weight:700;font-size:16pt;width:8mm;line-height:1">{ur(i+1)}</span>'
                 f'<span class="bx" style="width:58mm;height:22mm;font-size:{fs}pt;font-weight:700;background:#FBE9B5;align-items:center;padding-top:0">{it["text"]}</span>'
                 f'<span style="display:flex;gap:5mm">{opts}</span></div>')
    return f"""<section class="page ws"><div class="content">
 <div style="display:flex;align-items:center;gap:5mm">
  <div style="flex:1"><div class="small" style="font-weight:700;color:#000;line-height:1.6">لیول ۲ اردو · دن ۱</div><h1>خروجی جانچ: پڑھیں اور تصویر پر دائرہ لگائیں</h1></div>
  <div style="border:.6mm solid #000;border-radius:3mm;padding:.4mm 4mm;font-weight:700;font-size:14pt;line-height:1.9">اسکور: ____ / ۵</div></div>
 <div class="idrow"><span>نام</span><span style="flex:.6">تاریخ</span></div>
 <div style="margin-top:1mm">{rows}</div>
 <div style="display:flex;align-items:center;gap:5mm;margin-top:4mm">
  <div class="gray" style="width:24mm">{scene("kids_wave")}</div>
  <div style="flex:1;border:.5mm solid #000;border-radius:3.5mm;padding:1mm 4mm;background:#FBE9B5"><b style="font-size:13pt;line-height:1.8">شاباش!</b><br><span style="font-size:10.5pt;line-height:1.8">آپ نشانیوں کے ساتھ لفظ پڑھنا سیکھ رہے ہیں۔</span></div>
  <div style="border:.4mm solid #000;border-radius:3mm;padding:.6mm 3mm;font-size:8.8pt;line-height:1.8;width:44mm"><b>استاد</b><br>&#9744; حصہ ب: کارڈ پڑھا</div></div>
</div>{foot_ws(2)}</section>"""


def build():
    html = head_i("Level 2 Urdu Day 1 - Student Worksheet v1").replace("</style>", CSS_WS + "</style>") + page1() + page2() + OVERFLOW_JS
    out = os.path.join(WORK, "wsi.html")
    open(out, "w", encoding="utf-8").write(html)
    return out


if __name__ == "__main__":
    print(build())
