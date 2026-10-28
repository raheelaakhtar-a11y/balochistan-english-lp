"""Level 1 Beginner, Urdu, Day 1 (28 Oct planner): Student Worksheet, 3 pages.
Page 1 = class tasks, page 2 = exit check, page 3 = 'Home adventure' (games a child will want to do at home, with family).
Colour on screen, still readable in black and white (dark text on pale fills, strong borders)."""
from common_n2 import *
import random

CSS_WS = """
.ws .content{top:8mm;bottom:14mm}
.ws h1{margin:0;font-size:21pt;font-weight:700;color:#001F3F;line-height:1.5}
.banner{display:flex;align-items:center;gap:4mm;border-radius:5mm;padding:.8mm 6mm;border:.7mm solid #001F3F;margin-bottom:1.4mm}
.idrow{display:flex;gap:7mm;font-size:11pt;margin:.2mm 0 2mm;font-weight:700}
.idrow span{flex:1;border-bottom:.45mm solid #001F3F;white-space:nowrap;line-height:1.8}
.task{border-radius:4mm;padding:1.2mm 4mm 1.6mm;margin-bottom:2.2mm;position:relative;border:.7mm solid var(--tc);background:var(--tb)}
.task .hd{display:flex;align-items:center;gap:3mm;margin-bottom:.2mm;font-size:11.5pt;font-weight:700;line-height:1.6;color:#001F3F}
.task .hd .ck{margin-inline-start:auto;font-size:8.6pt;font-weight:400;color:#1D2025}
.task .n{width:8.4mm;height:8.4mm;border-radius:50%;background:var(--tc);color:#fff;border:.5mm solid #001F3F;display:flex;align-items:center;justify-content:center;font-size:12.5pt;font-weight:700;flex:none;line-height:1}
.bx{display:inline-flex;align-items:flex-start;justify-content:center;font-weight:400;color:#001F3F;border:.55mm solid #001F3F;border-radius:2mm;background:#fff;line-height:1.3;padding-top:.6mm}
.dot{width:3.4mm;height:3.4mm;border:.5mm solid #001F3F;border-radius:50%;display:inline-block;background:#fff;flex:none}
.tc{width:17mm;height:12.4mm;border-bottom:.5mm dashed #001F3F;display:inline-flex;align-items:flex-start;justify-content:center;font-size:23pt;line-height:1.3;color:#B9BFC9;margin-inline-start:1.2mm;background:#fff;border-radius:1.6mm 1.6mm 0 0}
.tc.blank{color:transparent}
.ck2{width:6.4mm;height:6.4mm;border:.55mm solid #001F3F;border-radius:1.4mm;display:inline-block;flex:none;background:#fff}
.sound{font-weight:700;color:#001F3F}
"""

PALE = {l: TILE[l] + "26" for l in LETTERS}


def foot_ws(n):
    return foot(FOOT_WS, n, 3)


def star(size=7, fill="#F5B301", stroke="#001F3F"):
    pts = " ".join(f"{50 + r * __import__('math').cos(__import__('math').radians(a)):.1f},{52 + r * __import__('math').sin(__import__('math').radians(a)):.1f}"
                   for a, r in [(-90 + 36 * i, 46 if i % 2 == 0 else 19) for i in range(10)])
    return f'<svg viewBox="0 0 100 100" style="width:{size}mm;height:{size}mm;display:inline-block;flex:none"><polygon points="{pts}" fill="{fill}" stroke="{stroke}" stroke-width="4" stroke-linejoin="round"/></svg>'


def face(size=10):
    return (f'<svg viewBox="0 0 100 100" style="width:{size}mm;height:{size}mm;display:inline-block;flex:none"><circle cx="50" cy="50" r="44" fill="#fff" stroke="#001F3F" stroke-width="5"/>'
            '<circle cx="35" cy="40" r="5" fill="#001F3F"/><circle cx="65" cy="40" r="5" fill="#001F3F"/><path d="M28 60 Q50 82 72 60" fill="none" stroke="#001F3F" stroke-width="5" stroke-linecap="round"/></svg>')


def task_style(c):
    return f'--tc:{c};--tb:{c}1A'


def page1():
    t1 = ""
    for l in LETTERS:
        t1 += (f'<div style="display:flex;align-items:center;height:12mm;gap:1mm">'
               f'<span style="flex:none">{ptile(l, 10, 9, 13)}</span>'
               f'<span style="flex:none;margin-inline-start:1mm">{stroke_box(l, 18, glyph="#B9BFC9")}</span>'
               f'<span class="tc" style="height:9.6mm;font-size:18pt">{l}</span><span class="tc" style="height:9.6mm;font-size:18pt">{l}</span><span class="tc blank" style="height:9.6mm">.</span><span class="tc blank" style="height:9.6mm">.</span></div>')
    t2 = "".join(
        f'<div style="display:flex;align-items:center;justify-content:space-between;height:10mm">'
        f'<span style="margin-inline-start:8mm;display:inline-block;background:#fff;border:.4mm solid #001F3F;border-radius:2mm;padding:.2mm"><img src="img/{PIC[p]}.jpg" style="width:8.6mm;height:8.6mm;object-fit:contain;display:block"></span>'
        f'<span style="display:flex;align-items:center;flex:1;justify-content:space-between;padding:0 2mm"><i class="dot"></i><i class="dot"></i></span>'
        f'<span style="margin-inline-end:8mm">{ptile(l, 14, 10, 17)}</span></div>' for p, l in zip(T2_PICS, T2_LETTERS))
    t3 = ""
    for tg, opts in T3_ROWS:
        t3 += (f'<div style="display:flex;align-items:center;gap:2mm;margin-bottom:.4mm"><span class="bx" style="width:13mm;height:8.8mm;font-size:15pt;background:{PALE[tg]};border-color:{TILE[tg]};border-width:.8mm">{tg}</span>'
               f'<span style="width:.5mm;height:7mm;background:#001F3F;display:inline-block;margin:0 .6mm"></span>'
               + "".join(f'<span class="bx" style="flex:1;height:8.8mm;font-size:15pt">{o}</span>' for o in opts) + '</div>')
    return f"""<section class="page ws"><div class="content">
 <div class="banner" style="background:#FFF1BF">
  <div style="flex:1"><div class="small" style="font-weight:700;color:#001F3F;line-height:1.5">لیول ۱ اردو · دن ۱ · کلاس کا کام</div><h1>میرے چھ حرفی دوست</h1></div>
  <div style="width:17mm;background:#fff;border-radius:3mm;overflow:hidden;border:.4mm solid #001F3F">{scene("kids_wave")}</div></div>
 <div class="idrow" style="margin-bottom:1.4mm"><span>نام</span><span style="flex:.55">جماعت</span><span style="flex:.8">تاریخ</span></div>

 <div class="task" style="{task_style('#2AA7C7')}"><div class="hd"><span class="n">۱</span>حرف کو ٹریس کریں، پھر نقل کریں۔<span class="ck">جانچ: آپ کی ڈیسک پٹی</span></div>{t1}</div>
 <div class="task" style="{task_style('#E85C9B')}"><div class="hd"><span class="n">۲</span>تصویر سے اس کے پہلے حرف تک لکیر کھینچیں۔<span class="ck">جانچ: آپ کی ڈیسک پٹی</span></div>{t2}</div>
 <div class="task" style="{task_style('#4DB857')};margin-bottom:0"><div class="hd"><span class="n">۳</span>پہلے خانے جیسے حرف کے گرد دائرہ لگائیں۔<span class="ck">جانچ: آپ کی ڈیسک پٹی</span></div>{t3}</div>
</div>{foot_ws(1)}</section>"""


def page2():
    rows = ""
    for i, it in enumerate(EXIT):
        if it["options"]:
            boxes = "".join(f'<span class="bx" style="width:34mm;height:27mm;font-size:38pt;padding-top:1.6mm;background:#fff">{o}</span>' for o in it["options"])
        else:
            boxes = '<span style="display:inline-block;width:72mm;height:21mm;border-bottom:.6mm dashed #001F3F;background:#fff;border-radius:2mm 2mm 0 0"></span>'
        rows += (f'<div style="display:flex;align-items:center;gap:6mm;height:33mm;border:.6mm solid #2AA7C7;background:#2AA7C71A;border-radius:4mm;padding:0 5mm;margin-bottom:2mm">'
                 f'<span class="n" style="width:10mm;height:10mm;border-radius:50%;background:#2AA7C7;color:#fff;border:.5mm solid #001F3F;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:15pt;line-height:1;flex:none">{ur(i+1)}</span>{boxes}</div>')
    return f"""<section class="page ws"><div class="content">
 <div class="banner" style="background:#D8F0F8">
  <div style="flex:1"><div class="small" style="font-weight:700;color:#001F3F;line-height:1.5">لیول ۱ اردو · دن ۱ · خروجی جانچ</div><h1>سنیں اور دائرہ لگائیں</h1></div>
  <div style="border:.7mm solid #001F3F;border-radius:3mm;padding:.2mm 4mm;font-weight:700;font-size:14pt;line-height:1.9;background:#fff">اسکور: ____ / ۵</div></div>
 <div class="idrow"><span>نام</span><span style="flex:.6">تاریخ</span></div>
 <div style="margin-top:1mm">{rows}</div>
 <div style="display:flex;align-items:center;gap:5mm;margin-top:1mm">
  <div style="width:24mm;background:#fff;border-radius:3mm;overflow:hidden;border:.4mm solid #001F3F">{scene("kids_wave")}</div>
  <div style="flex:1;border:.7mm solid #001F3F;border-radius:3.5mm;padding:1mm 4mm;background:#FFF1BF"><b style="font-size:13pt;line-height:1.8">شاباش!</b><br><span style="font-size:10.5pt;line-height:1.8">آپ ا، ب، پ، ت، ٹ اور ث سیکھ رہے ہیں۔ گھر کا ایڈونچر اگلے صفحے پر ہے!</span></div>
  <div style="border:.5mm solid #001F3F;border-radius:3mm;padding:.6mm 3mm;font-size:8.8pt;line-height:1.8;width:44mm;background:#fff"><b>استاد</b><br>&#9744; حصہ ب: آواز سنی</div></div>
</div>{foot_ws(2)}</section>"""


def page3():
    rnd = random.Random(28)
    cells = [l for l in LETTERS for _ in range(5)]
    while True:
        rnd.shuffle(cells)
        if all(cells[i] != cells[i + 1] for i in range(len(cells) - 1)):
            break
    assert all(cells.count(l) == 5 for l in LETTERS) and len(cells) == 30
    SYM = {"ا": "•", "ب": "/", "پ": "×", "ت": "○", "ٹ": "–", "ث": "+"}
    CNAME = {"ا": "نیلا", "ب": "نارنجی", "پ": "ہرا", "ت": "گلابی", "ٹ": "جامنی", "ث": "پیلا"}
    key = "".join(f'<div style="display:flex;align-items:center;gap:1.4mm;flex:1;justify-content:center">'
                  f'<span class="bx" style="width:9.4mm;height:8mm;font-size:13pt;background:{TILE[l]}55;border-color:{TILE[l]};border-width:.8mm;flex:none">{l}</span>'
                  f'<span style="font-size:8.2pt;line-height:1.3;white-space:nowrap">{CNAME[l]}<br>{SYM[l]}</span></div>' for l in LETTERS)
    grid = "".join(f'<div class="bx" style="height:10mm;font-size:16pt;border-width:.5mm">{c}</div>' for c in cells)
    claps = "".join(f'<div style="flex:1;text-align:center">{ptile(l, 14, 12, 19)}<div style="margin-top:.4mm"><span class="ck2" style="width:6mm;height:6mm"></span></div></div>' for l in LETTERS)
    hunt = "".join(f'<div style="display:flex;align-items:center;gap:3mm;height:9.4mm"><span style="flex:none">{ptile(l, 11, 8.4, 15)}</span>'
                   + "".join('<i class="dot" style="width:6.2mm;height:6.2mm"></i>' for _ in range(6)) + '</div>' for l in LETTERS)
    return f"""<section class="page ws"><div class="content">
 <div class="banner" style="background:#E3F4EC;border-color:#0B8F6A">
  <div style="flex:1"><div class="small" style="font-weight:700;color:#001F3F;line-height:1.5">لیول ۱ اردو · دن ۱ · گھر پر کھیلیں · تقریباً ۱۵ منٹ</div><h1>گھر کا ایڈونچر</h1>
   <div style="font-size:10pt;line-height:1.6">گھر والوں کے ساتھ کھیلیں۔ ہر کھیل کے بعد ایک ستارہ رنگیں اور کل استاد کو دکھائیں!</div></div>
  <div style="display:flex;gap:1mm">{star(11)}{star(11)}{star(11)}{star(11)}</div></div>
 <div class="idrow"><span>نام</span><span style="flex:.6">تاریخ</span></div>

 <div class="task" style="{task_style('#2AA7C7')}"><div class="hd"><span class="n">۱</span>حرفی دوستوں کو سلام<span class="ck">کھیل: گھر کے بڑے کو آوازیں سنائیں۔ ہر آواز پر وہ تالی بجائیں، پھر خانے میں ٹک</span></div>
  <div style="display:flex;gap:2mm;margin-top:.8mm">{claps}</div></div>

 <div class="task" style="{task_style('#F08A3C')}"><div class="hd"><span class="n">۲</span>حرف شکاری<span class="ck">اخبار، کتاب یا دوا کے ڈبے پر حرف ڈھونڈیں۔ ہر بار ملنے پر ایک دائرہ بھریں</span></div>
  <div style="margin-top:.4mm">{hunt}</div></div>

 <div class="task" style="{task_style('#4DB857')}"><div class="hd"><span class="n">۳</span>رنگ بھرو<span class="ck">ہر حرف کے خانے میں اس کا رنگ بھریں۔ رنگ نہ ہوں تو اس کا نشان بنائیں</span></div>
  <div style="display:flex;gap:1.4mm;background:#fff;border:.4mm solid #001F3F;border-radius:2mm;padding:.8mm 1mm;margin:.6mm 0 1mm">{key}</div>
  <div style="display:grid;grid-template-columns:repeat(6,1fr);gap:1mm">{grid}</div></div>

 <div class="task" style="{task_style('#7B61C9')};margin-bottom:0"><div class="hd"><span class="n">۴</span>آپ استاد بنیں<span class="ck">گھر کے کسی بڑے یا بہن بھائی کو چھ آوازیں سکھائیں</span></div>
  <div style="display:flex;align-items:center;gap:5mm">
   <div style="display:flex;gap:3mm">{face(12)}{face(12)}{face(12)}</div>
   <div style="flex:1;font-size:10pt;line-height:1.7">جب وہ صحیح آواز بولیں تو ایک چہرہ مسکراتا ہوا بنائیں۔</div>
   <div style="width:56mm"><div style="border-bottom:.5mm solid #001F3F;height:10mm"></div><div class="small" style="line-height:1.5">گھر والے کا نام یا انگوٹھا</div></div></div></div>

 <div style="margin-top:2.4mm;border:.7mm dashed #001F3F;border-radius:4mm;background:#FFF1BF;padding:1.4mm 5mm;display:flex;align-items:center;gap:5mm"><div style="flex:1"><b style="font-size:12.5pt;line-height:1.7">میرے ستارے</b><div style="font-size:10pt;line-height:1.6">ہر کھیل کے بعد ایک ستارہ رنگیں۔ چاروں رنگ دیں تو کل استاد کو دکھائیں اور شاباش لیں!</div></div><div style="display:flex;gap:2.4mm">{star(15, "#fff")}{star(15, "#fff")}{star(15, "#fff")}{star(15, "#fff")}</div></div>
</div>{foot_ws(3)}</section>"""


def build():
    html = head_html2("Level 1 Urdu Day 1 (28 Oct planner) - Student Worksheet").replace("</style>", CSS_WS + "</style>") + page1() + page2() + page3() + OVERFLOW_JS
    out = os.path.join(WORK, "wsn.html")
    open(out, "w", encoding="utf-8").write(html)
    return out


if __name__ == "__main__":
    print(build())
