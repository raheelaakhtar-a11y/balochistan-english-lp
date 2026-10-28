"""Level 2 Intermediate, Urdu, Day 1: Student Worksheet v2 (interactive, black-and-white print).
Pages 1-2 = v1 tasks (page 2 gains a colour-a-star strip); page 3 is new: a paper-clip mark spinner, 12 cut-out cards for a
pair-matching game and a home challenge. Page 3 is meant to be printed on one side only (it gets cut up)."""
import re
import doc_ws_i as v1
from common_i import *

CSS2 = """
.sp{display:flex;gap:6mm;align-items:center;margin-bottom:3mm}
.sp .wheel{width:70mm;height:70mm;flex:none}
.sp .steps div{display:flex;gap:2.6mm;align-items:flex-start;font-size:11pt;line-height:1.85;margin-bottom:.8mm}
.sp .steps .n{width:7mm;height:7mm;border-radius:50%;background:#FBE9B5;border:.5mm solid #000;display:flex;align-items:center;justify-content:center;font-size:11pt;font-weight:700;flex:none;line-height:1;margin-top:1.2mm}
.tally{display:flex;gap:2.4mm;margin-top:1.4mm}
.tally div{flex:1;border:.5mm solid #000;border-radius:2.4mm;height:17mm;text-align:center;font-size:8.8pt;line-height:1.4;padding-top:.6mm;font-weight:700}
.tally div b{display:block;font-size:15pt;line-height:1.3}
.cards{display:grid;grid-template-columns:repeat(4,1fr);border-top:.45mm dashed #000;border-inline-start:.45mm dashed #000}
.cards>div{height:33mm;border-bottom:.45mm dashed #000;border-inline-end:.45mm dashed #000;display:flex;align-items:center;justify-content:center}
.cards .w{font-size:21pt;font-weight:700;line-height:1.5;background:#FBE9B5}
.cards img{width:25mm;height:25mm;object-fit:contain;display:block;filter:grayscale(1) contrast(1.05)}
.star{width:12mm;height:12mm}
"""

PAIRS = ["kitab", "gulab", "qalam", "mirch", "dukan", "batakh"]


def wheel():
    labels = [("zabar", 50, 31), ("pesh", 77, 58), ("zer", 50, 82), ("jazm", 23, 58)]
    txt = "".join(f'<text x="{x}" y="{y}" text-anchor="middle" font-family="NNU" font-size="17" font-weight="700" fill="#000">{BASE}{MSYM[m]}</text>' for m, x, y in labels)
    nm = "".join(f'<text x="{x}" y="{y}" text-anchor="middle" font-family="NNU" font-size="6.4" fill="#000">{MNAME[m]}</text>'
                 for m, x, y in [("zabar", 50, 12), ("pesh", 88, 50), ("zer", 50, 97), ("jazm", 12, 50)])
    return ('<svg class="wheel" viewBox="0 0 100 100"><circle cx="50" cy="50" r="48" fill="#fff" stroke="#000" stroke-width="1.2"/>'
            '<line x1="16" y1="16" x2="84" y2="84" stroke="#000" stroke-width="1"/><line x1="84" y1="16" x2="16" y2="84" stroke="#000" stroke-width="1"/>'
            f'<circle cx="50" cy="50" r="3.2" fill="#000"/>{txt}</svg>')


def star_row():
    s = ('<svg class="star" viewBox="0 0 24 24"><path d="M12 2.5l2.9 6.2 6.8.8-5 4.7 1.3 6.7L12 17.6 6 20.9l1.3-6.7-5-4.7 6.8-.8z" '
         'fill="#fff" stroke="#000" stroke-width="1.3" stroke-linejoin="round"/></svg>')
    return (f'<div style="display:flex;align-items:center;gap:3mm;margin-top:3mm;border:.5mm solid #000;border-radius:3.5mm;padding:1mm 4mm">'
            f'<b style="font-size:11.5pt;line-height:1.8;flex:1">ہر صحیح جواب پر ایک ستارہ پنسل سے بھریں۔</b><span style="display:flex;gap:1.6mm">{s * 5}</span></div>')


def page3():
    cards = [f'<div class="w">{wd(k)}</div>' for k in PAIRS] + [f'<div>{wpic(k, "pc")}</div>' for k in PAIRS]
    # shuffle once, deterministic, so words and pictures of one pair do not sit side by side
    order = [0, 7, 2, 9, 10, 3, 4, 11, 6, 1, 8, 5]
    grid = "".join(cards[i] for i in order)
    home = "".join(f'<span style="display:inline-block;width:8mm;height:8mm;border:.5mm solid #000;border-radius:50%;margin-inline-start:2mm"></span>' for _ in range(3))
    return f"""<section class="page ws"><div class="content">
 <div style="display:flex;align-items:center;gap:5mm">
  <div style="flex:1"><div class="small" style="font-weight:700;color:#000;line-height:1.6">لیول ۲ اردو · دن ۱ · ساتھی کے ساتھ</div><h1>کاٹیں اور کھیلیں</h1></div>
  <div style="width:19mm" class="gray">{scene("kids_wave")}</div></div>
 <div class="idrow"><span>نام</span><span style="flex:.6">ساتھی کا نام</span></div>

 <div class="task"><div class="hd"><span class="n">۱</span>نشانی گھماؤ کھیل<span class="ck">دو بچے · ۳ منٹ</span></div>
  <div class="sp">{wheel()}
   <div class="steps" style="flex:1">
    <div><span class="n">۱</span><span>پنسل کی نوک گول کے بیچ میں رکھیں۔ پیپر کلپ پنسل کے گرد گھمائیں۔</span></div>
    <div><span class="n">۲</span><span>کلپ جس حصے پر رکے، اس کی آواز بولیں۔ ساتھی وہی آواز دہرائے۔</span></div>
    <div><span class="n">۳</span><span>پھر ساتھی گھمائے۔ ہر بار اپنی ٹیلی میں ایک لکیر لگائیں۔</span></div>
    <div class="tally">{"".join(f'<div><b>{BASE}{MSYM[m]}</b>{MNAME[m]}</div>' for m in MARKS)}</div>
   </div></div></div>

 <div class="task" style="margin-bottom:0"><div class="hd"><span class="n">۲</span>کارڈ کاٹیں، جوڑے بنائیں<span class="ck">دو بچے · ۵ منٹ</span></div>
  <div style="font-size:10.4pt;line-height:1.85;margin-bottom:1.6mm">نقطوں والی لکیروں پر کاٹیں۔ سب کارڈ الٹے رکھیں۔ باری باری دو کارڈ اٹھائیں۔ لفظ پڑھیں۔ لفظ اور اس کی تصویر ملیں تو جوڑا رکھ لیں۔ زیادہ جوڑے جیتتے ہیں۔</div>
  <div class="cards">{grid}</div></div>

 <div style="border:.5mm solid #000;border-radius:3.5mm;padding:1.2mm 4mm;margin-top:3mm;display:flex;align-items:center;gap:4mm;background:#FBE9B5">
  <b style="font-size:12pt;line-height:1.8">گھر کا چیلنج:</b><span style="font-size:11pt;line-height:1.8;flex:1">اپنے جوڑوں میں سے ۳ لفظ گھر والوں کو پڑھ کر سنائیں۔ ہر بار ایک گول بھریں۔</span><span style="display:flex">{home}</span></div>
</div>{foot(FOOT_WS, 3, 3)}</section>"""


def build():
    p1 = v1.page1().replace("از ۲", "از ۳")
    p2 = v1.page2().replace("از ۲", "از ۳")
    marker = '<div style="display:flex;align-items:center;gap:5mm;margin-top:4mm">'
    p2 = p2.replace(marker, star_row() + marker, 1)
    html = (head_i("Level 2 Urdu Day 1 - Student Worksheet v2 (interactive)").replace("</style>", v1.CSS_WS + CSS2 + "</style>")
            + p1 + p2 + page3() + OVERFLOW_JS)
    out = os.path.join(WORK, "wsi2.html")
    open(out, "w", encoding="utf-8").write(html)
    return out


if __name__ == "__main__":
    print(build())
