"""Level 3 Advanced, Urdu, Day 1 (28 Oct planner): Student Worksheet (interactive, black-and-white print, no Rumi logo).
Page 1 = three class tasks, page 2 = exit check (with a colour-a-star row), page 3 = cut-and-play: a paper-clip form spinner,
16 cut-out word cards to build sentences, and a home task. Page 3 is meant to be printed on one side only (it gets cut up)."""
import math
from common_a import *

CSS_WS = """
.ws .content{top:9mm;bottom:15mm}
.ws h1{margin:0;font-size:20pt;font-weight:700;color:#000;line-height:1.6}
.idrow{display:flex;gap:7mm;font-size:11pt;margin:.4mm 0 2mm;font-weight:700}
.idrow span{flex:1;border-bottom:.4mm solid #000;white-space:nowrap;line-height:1.8}
.task{border:.5mm solid #000;border-radius:3.5mm;padding:1.4mm 4mm 2mm;margin-bottom:2.6mm;position:relative}
.task .hd{display:flex;align-items:center;gap:3mm;margin-bottom:.4mm;font-size:11.5pt;font-weight:700;line-height:1.7}
.task .hd .ck{margin-inline-start:auto;font-size:8.6pt;font-weight:400}
.task .n{width:8mm;height:8mm;border-radius:50%;background:#FBE9B5;border:.5mm solid #000;display:flex;align-items:center;justify-content:center;font-size:12pt;font-weight:700;flex:none;line-height:1}
.bx{display:inline-flex;align-items:center;justify-content:center;font-weight:700;color:#000;border:.5mm solid #000;border-radius:2mm;background:#fff;line-height:1.5}
.dot{width:3.4mm;height:3.4mm;border:.5mm solid #000;border-radius:50%;display:inline-block;background:#fff;flex:none}
.mrow{display:flex;align-items:center;justify-content:space-between;height:14.4mm}
.gray{filter:grayscale(1) contrast(1.05)}
.sp{display:flex;gap:6mm;align-items:center;margin-bottom:3mm}
.sp .wheel{width:66mm;height:66mm;flex:none}
.sp .steps div{display:flex;gap:2.6mm;align-items:flex-start;font-size:11pt;line-height:1.85;margin-bottom:.8mm}
.sp .steps .n{width:7mm;height:7mm;border-radius:50%;background:#FBE9B5;border:.5mm solid #000;display:flex;align-items:center;justify-content:center;font-size:11pt;font-weight:700;flex:none;line-height:1;margin-top:1.2mm}
.tally{display:flex;gap:2.4mm;margin-top:1.4mm}
.tally div{flex:1;border:.5mm solid #000;border-radius:2.4mm;height:16mm;text-align:center;font-size:9.4pt;line-height:1.5;padding-top:.6mm;font-weight:700}
.cards{display:grid;grid-template-columns:repeat(4,1fr);border-top:.45mm dashed #000;border-inline-start:.45mm dashed #000}
.cards>div{height:23mm;border-bottom:.45mm dashed #000;border-inline-end:.45mm dashed #000;display:flex;align-items:center;justify-content:center}
.cards .cw{font-size:19pt;margin:0;padding:.4mm 3mm;border-width:.6mm;line-height:1.6}
.cards .cw i{font-size:7.6pt}
.star{width:12mm;height:12mm}
"""


def foot_ws(n):
    return foot(FOOT_WS, n, 3)


def head_row(title, sub="لیول ۳ اردو · دن ۱", scn="pair_book"):
    return f"""<div style="display:flex;align-items:center;gap:5mm">
  <div style="flex:1"><div class="small" style="font-weight:700;color:#000;line-height:1.6">{sub}</div><h1>{title}</h1></div>
  <div style="width:19mm" class="gray">{scene(scn)}</div></div>"""


def page1():
    t1 = ""
    for sent_it, pic_it in zip(T1_ITEMS, T1_PICS):
        t1 += (f'<div class="mrow"><span style="margin-inline-start:4mm;display:inline-block;font-size:14pt;font-weight:700;color:#000;line-height:1.5;min-width:62mm;text-align:right">{set_sent(*sent_it)[:-1]}</span>'
               f'<span style="display:flex;align-items:center;flex:1;justify-content:space-between;padding:0 2mm"><i class="dot"></i><i class="dot"></i></span>'
               f'<span class="gray" style="margin-inline-end:8mm;display:inline-block"><div style="width:13mm">{apic(*pic_it)}</div></span></div>')
    t2 = ""
    for i, t in enumerate(T2):
        blank = '<span style="display:inline-block;width:20mm;height:8mm;border-bottom:.5mm solid #000;vertical-align:bottom;margin:0 1mm"></span>'
        line = f'{t["before"]} {blank} {t["after"]}'.strip()
        opts = "".join(f'<span class="bx" style="flex:1;height:11mm;font-size:13pt">{o}</span>' for o in t["options"])
        t2 += (f'<div style="display:flex;align-items:center;gap:4mm;margin-bottom:1.2mm"><span style="font-weight:700;font-size:14pt;line-height:1.7;min-width:78mm">{ur(i+1)}۔ {line}</span>'
               f'<span style="display:flex;gap:2mm;flex:1">{opts}</span></div>')
    t3 = ""
    for a in T3:
        t3 += '<div style="display:flex;gap:7mm;align-items:center;justify-content:flex-start;height:23mm">' + "".join(
            f'<span style="font-size:19pt;font-weight:700;line-height:1.6;padding:0 1mm">{w}</span>' for w in words(*a)) + '</div>'
    key = ('<div style="display:flex;gap:8mm;font-size:10pt;line-height:1.8;margin-bottom:.8mm;align-items:center">'
           '<span style="display:flex;align-items:center;gap:2mm"><span style="width:10mm;height:7mm;border:.5mm solid #000;border-radius:50%;display:inline-block"></span>نام کے گرد دائرہ</span>'
           '<span style="display:flex;align-items:center;gap:2mm"><span style="display:inline-block;width:10mm;border-bottom:.6mm solid #000"></span>کیسا کے نیچے لکیر</span>'
           '<span style="display:flex;align-items:center;gap:2mm"><span style="width:10mm;height:7mm;border:.5mm solid #000;border-radius:1.4mm;display:inline-block"></span>کام پر ڈبہ</span></div>')
    return f"""<section class="page ws"><div class="content">
 {head_row("جملے ملائیں اور بدلیں")}
 <div class="idrow"><span>نام</span><span style="flex:.55">جماعت</span><span style="flex:.8">تاریخ</span></div>

 <div class="task"><div class="hd"><span class="n">۱</span>جملہ پڑھیں، پھر لکیر سے اس کی تصویر تک پہنچیں۔<span class="ck">جانچ: آپ کی ڈیسک پٹی</span></div>{t1}</div>
 <div class="task"><div class="hd"><span class="n">۲</span>جملے میں درست لفظ پر دائرہ لگائیں۔<span class="ck">جانچ: آپ کی ڈیسک پٹی</span></div>{t2}</div>
 <div class="task" style="margin-bottom:0"><div class="hd"><span class="n">۳</span>ہر لفظ کی قسم کا نشان لگائیں۔<span class="ck">جانچ: آپ کا ساتھی</span></div>{key}{t3}</div>
</div>{foot_ws(1)}</section>"""


def star_row():
    s = ('<svg class="star" viewBox="0 0 24 24"><path d="M12 2.5l2.9 6.2 6.8.8-5 4.7 1.3 6.7L12 17.6 6 20.9l1.3-6.7-5-4.7 6.8-.8z" '
         'fill="#fff" stroke="#000" stroke-width="1.3" stroke-linejoin="round"/></svg>')
    return (f'<div style="display:flex;align-items:center;gap:3mm;margin-top:3mm;border:.5mm solid #000;border-radius:3.5mm;padding:1mm 4mm">'
            f'<b style="font-size:11.5pt;line-height:1.8;flex:1">ہر درست جواب پر ایک ستارہ پنسل سے بھریں۔</b><span style="display:flex;gap:1.6mm">{s * 5}</span></div>')


def page2():
    rows = ""
    for i, it in enumerate(EXIT):
        opts = "".join(f'<span class="bx" style="flex:1;height:21mm;font-size:13.5pt;padding:0 2mm;text-align:center">{o}</span>' for o in it["options"])
        rows += (f'<div style="display:flex;align-items:center;gap:4mm;height:30mm;border-bottom:.3mm dashed #999"><span style="font-weight:700;font-size:16pt;width:8mm;line-height:1">{ur(i+1)}</span>'
                 f'<span style="display:flex;gap:4mm;flex:1">{opts}</span></div>')
    return f"""<section class="page ws"><div class="content">
 <div style="display:flex;align-items:center;gap:5mm">
  <div style="flex:1"><div class="small" style="font-weight:700;color:#000;line-height:1.6">لیول ۳ اردو · دن ۱</div><h1>خروجی جانچ: درست جملے پر دائرہ لگائیں</h1></div>
  <div style="border:.6mm solid #000;border-radius:3mm;padding:.4mm 4mm;font-weight:700;font-size:14pt;line-height:1.9">اسکور: ____ / ۵</div></div>
 <div class="idrow"><span>نام</span><span style="flex:.6">تاریخ</span></div>
 <div class="small" style="margin-bottom:.6mm;font-size:10.5pt">ہر آئٹم میں تین جملے ہیں۔ صرف ایک جملہ درست ہے۔</div>
 <div style="margin-top:1mm">{rows}</div>
 {star_row()}
 <div style="display:flex;align-items:center;gap:5mm;margin-top:4mm">
  <div class="gray" style="width:24mm">{scene("kids_wave")}</div>
  <div style="flex:1;border:.5mm solid #000;border-radius:3.5mm;padding:1mm 4mm;background:#FBE9B5"><b style="font-size:13pt;line-height:1.8">شاباش!</b><br><span style="font-size:10.5pt;line-height:1.8">آپ جملے کے سب لفظ ملا کر بولنا سیکھ رہے ہیں۔</span></div>
  <div style="border:.4mm solid #000;border-radius:3mm;padding:.6mm 3mm;font-size:8.8pt;line-height:1.8;width:44mm"><b>استاد</b><br>&#9744; حصہ ب: جملہ بدلا</div></div>
</div>{foot_ws(2)}</section>"""


def wheel():
    labels = {"ms": (50, 19), "mp": (78, 47), "fs": (50, 69), "fp": (22, 47)}
    txt = ""
    for f, (x, y) in labels.items():
        noun = we1_noun(f)
        txt += f'<text x="{x}" y="{y}" text-anchor="middle" font-family="NNU" font-size="8.4" font-weight="700" fill="#000">{FLABEL[f].split()[0]}</text>'
        txt += f'<text x="{x}" y="{y+12}" text-anchor="middle" font-family="NNU" font-size="11.5" font-weight="700" fill="#000">{noun}</text>'
    return ('<svg class="wheel" viewBox="0 0 100 100"><circle cx="50" cy="50" r="48" fill="#fff" stroke="#000" stroke-width="1.2"/>'
            '<line x1="16" y1="16" x2="84" y2="84" stroke="#000" stroke-width="1"/><line x1="84" y1="16" x2="16" y2="84" stroke="#000" stroke-width="1"/>'
            f'<circle cx="50" cy="50" r="3.2" fill="#000"/>{txt}</svg>')


# 16 cut-out cards: the four sentences' words, shuffled once (fixed order) so no row is a ready-made sentence
_CARD_ORDER = [5, 12, 0, 9, 14, 3, 7, 10, 1, 15, 6, 11, 8, 2, 13, 4]


def card_grid():
    roles = ["a", "n", "v", "h"]
    cards = []
    for f in FORMS:
        cards += list(zip(words("chota", "larka" if f[0] == "m" else "larki", "parhna", f), roles))
    assert len(cards) == 16 and sorted(_CARD_ORDER) == list(range(16))
    cells = ""
    for i in _CARD_ORDER:
        w, r = cards[i]
        lab = f"<i>{ROLE[r]}</i>" if ROLE[r] else ""
        cells += f'<div><span class="cw r{r}">{w}{lab}</span></div>'
    return cells


def page3():
    home = "".join('<span style="display:inline-block;width:8mm;height:8mm;border:.5mm solid #000;border-radius:50%;margin-inline-start:2mm"></span>' for _ in range(3))
    tally = "".join(f'<div><b style="font-size:11pt">{we1_noun(f)}</b>{FLABEL[f]}</div>' for f in FORMS)
    return f"""<section class="page ws"><div class="content">
 {head_row("کاٹیں اور کھیلیں", "لیول ۳ اردو · دن ۱ · ساتھی کے ساتھ", "kids_wave")}
 <div class="idrow"><span>نام</span><span style="flex:.6">ساتھی کا نام</span></div>

 <div class="task"><div class="hd"><span class="n">۱</span>شکل گھماؤ کھیل<span class="ck">دو بچے · ۳ منٹ</span></div>
  <div class="sp">{wheel()}
   <div class="steps" style="flex:1">
    <div><span class="n">۱</span><span>پنسل کی نوک گول کے بیچ میں رکھیں۔ پیپر کلپ پنسل کے گرد گھمائیں۔</span></div>
    <div><span class="n">۲</span><span>کلپ جس حصے پر رکے، اس شکل میں جملہ بولیں: «چھوٹا ... پڑھتا ہے» کو بدلیں۔</span></div>
    <div><span class="n">۳</span><span>ساتھی جانچے، پھر وہ گھمائے۔ ہر بار اپنی گنتی میں ایک لکیر لگائیں۔</span></div>
    <div class="tally">{tally}</div>
   </div></div></div>

 <div class="task" style="margin-bottom:0"><div class="hd"><span class="n">۲</span>کارڈ کاٹیں اور چار جملے بنائیں<span class="ck">دو بچے · ۵ منٹ</span></div>
  <div style="font-size:10.4pt;line-height:1.85;margin-bottom:1.6mm">نقطوں والی لکیروں پر کاٹیں۔ سب کارڈ ملا دیں۔ ان سے چار درست جملے بنائیں: ایک لڑکا، کئی لڑکے، ایک لڑکی، کئی لڑکیاں۔ ڈیسک پٹی سے جانچیں۔</div>
  <div class="cards">{card_grid()}</div></div>

 <div style="border:.5mm solid #000;border-radius:3.5mm;padding:1.2mm 4mm;margin-top:3mm;display:flex;align-items:center;gap:4mm;background:#FBE9B5">
  <b style="font-size:12pt;line-height:1.8">گھر کا کام:</b><span style="font-size:11pt;line-height:1.8;flex:1">اپنے بنائے ہوئے کسی جملے میں نام بدل کر گھر والوں کو سنائیں۔ ہر بار ایک گول بھریں۔</span><span style="display:flex">{home}</span></div>
</div>{foot_ws(3)}</section>"""


def build():
    html = head_a("Level 3 Urdu Day 1 - Student Worksheet v1 (interactive)").replace("</style>", CSS_WS + "</style>") + page1() + page2() + page3() + OVERFLOW_JS
    out = os.path.join(WORK, "wsa.html")
    open(out, "w", encoding="utf-8").write(html)
    return out


if __name__ == "__main__":
    print(build())
