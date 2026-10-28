"""Level 1 Beginner, Urdu, Day 1 (final planner): Lesson Plan v2.
v3 = (see changes in README) ; v2 = English section tags, stroke-order diagrams, larger speech lines in bubbles with characters, fewer boxes, one consistent minutes check."""
from common_u2 import *
tile = ptile   # v3: print-safe pale tiles everywhere

TOTAL = 5
CSS3 = r""".enh{font-family:Poppins,Arial,sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;font-size:12.5pt;font-weight:700;color:#001F3F;line-height:1.6}
:root{--grey:#1D2025;--teal:#064B38}
.small{color:#1D2025}
.en{color:#064B38;font-weight:700}
.box h2 .en{color:#1D2025;border-color:#1D2025}
.foot{color:#1D2025}
.bub0:after{display:none}.bub0{margin:.6mm 0}
.p1 .box{padding:4mm 6mm;font-size:12pt;line-height:2.05}.p1 .box h2{font-size:14.5pt;margin-bottom:2mm}
.p1 .small{font-size:10pt}.p1 .chip{font-size:10pt}
.p2 .box{padding:4mm 6mm;margin-bottom:6mm;font-size:12pt;line-height:2.1}.p2 .box h2{font-size:14.5pt;margin-bottom:2mm}
.p4 .box{margin-bottom:5mm}.p2 .bub{font-size:13pt}.p2 .small{font-size:10pt}.p2 .board{padding:4mm 6mm}"""
F = lambda n: foot(FOOT_LP, n, TOTAL)


def steps(items):
    return '<div class="stp">' + "".join(f'<div class="s"><span class="n2">{ur(i+1)}</span><div>{t}</div></div>' for i, t in enumerate(items)) + '</div>'


def sounds(seq, sep=" · "):
    return sep.join(f'<b class="sn">{SOUND[l]}</b>' for l in seq)


def talk(img, html, w=22):
    return f'<div class="talk"><div class="who" style="width:{w}mm">{scene(img)}</div><div class="bub">{html}</div></div>'


# ---------------- PAGE 1 ----------------
def page1():
    ribbon = ""
    for d in range(1, 34):
        if d == 1:
            st = "background:#F5B301;color:#001F3F;font-weight:700;outline:.5mm solid #001F3F"
        elif d <= 7:
            st = "background:#FBE08A;color:#001F3F"
        elif d <= 9:
            st = "background:#E9EEF6;color:#3A4A63"
        elif d >= 31:
            st = "background:#BDE5D2;color:#064B38"
        else:
            st = "background:#E6E9EE;color:#3A4A63"
        ribbon += f'<span style="flex:1;height:8.5mm;border-radius:1.2mm;display:flex;align-items:center;justify-content:center;font-size:7.4pt;line-height:1;{st}">{ur(d)}</span>'
    bits = [("آغاز", 5, "#6C7A8D"), ("دلچسپی", 5, "#0B8F6A"), ("میں کر کے دکھاؤں", 20, "#F5B301"), ("ہم سب مل کر", 12, "#F08A3C"),
            ("اکیلے", 8, "#2AA7C7"), ("خروجی جانچ", 10, "#001F3F")]
    assert [m for _, m, _ in bits] == [MINUTES[k] for k in ("warmup", "hook", "i_do", "we_do", "you_do", "exit")]
    tbar = "".join(f'<div style="flex:{m};background:{c};color:{"#001F3F" if c in ("#F5B301","#F08A3C","#2AA7C7") else "#fff"};'
                   f'padding:2mm 1mm;font-size:9.5pt;font-weight:700;text-align:center;line-height:1.8">{n}<br><span style="font-weight:400">{ur(m)} منٹ</span></div>'
                   for n, m, c in bits)
    return f"""<section class="page p1">
<div style="background:var(--navy);height:44mm;color:#fff;display:flex;align-items:center;padding:0 10mm;gap:6mm;position:relative">
 <div style="color:var(--gold);font-weight:700;line-height:1.3;text-align:center"><div style="font-size:15pt;color:#fff">دن</div><div style="font-size:50pt;line-height:1.25">۱</div><div style="font-size:15pt;color:#fff">از ۳۳</div></div>
 <div style="flex:1;padding-inline-start:5mm;border-inline-start:.5mm solid #2B4A6B">
  <span class="en" style="color:var(--gold)">Day 1 of 33 · Teach new letters</span>
  <div style="font-size:16pt;font-weight:700;line-height:1.7">لیول ۱ بنیادی · اردو</div>
  <div style="font-size:9.5pt;color:#fff;line-height:1.7">بلوچستان ونٹر پروگرام · درست سطح پر تدریس</div>
  <div style="margin-top:1.4mm;display:flex;gap:2mm"><span class="pill" style="font-size:9.5pt">۶۰ منٹ</span><span class="pill" style="font-size:9.5pt;background:var(--gold);color:var(--navy)">نئے حروف سکھائیں</span></div>
 </div>
 <div style="width:36mm;background:#fff;border-radius:5mm;overflow:hidden;border:.8mm solid var(--gold)">{scene("kids_wave")}</div>
</div>
<div class="content" style="top:47mm">
 <div style="display:flex;gap:.8mm;margin-bottom:.4mm">{ribbon}</div>
 <div class="small" style="margin-bottom:2mm">۳۳ دن۔ دن ۱ تا ۷ (سنہری) میں نئے حروف، دن ۸ اور ۹ میں دہرائی، دن ۳۱ تا ۳۳ (سبز) میں آخری دہرائی۔</div>

 <div class="box gold" style="display:flex;gap:4mm;align-items:center;padding:4mm 6mm;margin-bottom:5mm">
  <div style="display:flex;gap:2mm">{"".join(tile(l, 17, 20, 26).replace(TILE[l]+"22", "#ffffff") for l in LETTERS)}</div>
  <div><span class="en" style="color:var(--navy)">Today's letters</span>
  <div style="font-size:14pt;font-weight:700;line-height:1.8">آواز، تصویر والا لفظ اور لکھنا</div></div>
 </div>

 <div class="row" style="display:block">
  <div class="box sky" style="margin-bottom:5mm"><h2><span class="en">Learning outcomes</span>آج کے سیکھنے کے مقاصد</h2>
   <p style="margin-bottom:.4mm"><span class="chip">U-B-01</span> <b>اردو حروف تہجی کے حروف کو پہچاننا اور ان کا نام لینا</b></p>
   <p style="margin-bottom:.4mm"><span class="chip">U-B-02</span> <b>حرف کی آواز اور بولے گئے لفظ کی پہلی آواز بتانا</b></p>
   <p style="margin-bottom:.4mm"><span class="chip">U-B-03</span> <b>حرف بولا جائے تو اسے لکھنا</b></p>
   <p class="small" style="margin:0">دن ۱ تا ۹۔ ساتھ میں: <span class="chip">U-B-04</span> دائیں سے بائیں ٹریس اور نقل کرنا۔</p>
  </div>
 </div>


 <div class="box" style="margin-bottom:5mm;background:#E3F4EC;border:.7mm solid #0B8F6A;color:#001F3F"><h2 style="color:#001F3F"><span class="en">Today's goal</span>آج کا ہدف</h2><div style="font-size:15pt;font-weight:700;line-height:2;color:#001F3F">ہر حرف کی آواز بولیں، اس کے تصویر والے لفظ بتائیں اور ہر حرف لکھیں۔</div></div>

 <div style="margin-bottom:5mm"><span class="en" style="margin-inline-end:3mm">The 60 minutes</span><span style="font-size:9.5pt;font-weight:700;color:var(--navy)">وقت کی تقسیم (۶۰ منٹ)</span>
  <div style="display:flex;border-radius:2.5mm;overflow:hidden;margin-top:.6mm">{tbar}</div></div>

 <div class="box mint" style="margin-bottom:0"><h2><span class="en">To prepare</span>تیاری (تقریباً ۲۰ منٹ)</h2>
  <div style="columns:2;column-gap:6mm;font-size:11.5pt;line-height:2.1">
   <div>☐ حروف کا چارٹ دیوار پر لگائیں</div><div>☐ پانچ تصویر والے حرفی کارڈ کاٹیں</div>
   <div>☐ ہر بچے کے لیے ایک ڈیسک پٹی کاٹیں</div><div>☐ استاد کی رہنما شیٹ اپنے پاس رکھیں</div>
   <div>☐ ورک شیٹ: ہر بچے کے لیے ایک، دونوں طرف</div><div>☐ چاک، ڈسٹر، ہر بچے کے لیے کاپی اور پنسل</div>
  </div></div>
</div>
{F(1)}</section>"""


# ---------------- PAGE 2 ----------------
def page2():
    return f"""<section class="page p2">
{bar2("کلاس کا آغاز", "Start the lesson", "آغاز اور دلچسپی", "۱۰ منٹ")}
<div class="content">
 <div class="box grey"><h2><span class="en">Warm-up</span>آغاز: تصویر والے الفاظ بولیں <span class="t">۵ منٹ</span></h2>
  <div style="margin-bottom:1.2mm"><span class="do">۱۔ بچوں کو سلام کریں (۱ منٹ)۔</span>
   {talk("teacher_point", "السلام علیکم بچو! آج ہم پانچ نئے حروف سے ملیں گے۔", 20)}</div>
  <div><span class="do">۲۔ پانچ الفاظ بولیں (۴ منٹ)۔</span> حروف کے چارٹ پر ہر تصویر کی طرف اشارہ کریں: <b>انار، بٹن، پری، توا، ٹرک</b>۔ لفظ بولیں۔ بچے دو بار دہرائیں۔ پھر کوئی لفظ بولیں اور بچے چارٹ پر اس کی تصویر دکھائیں۔</div></div>

 <div class="box sky"><h2><span class="en">Hook</span>دلچسپی: پانچ حرفی دوست <span class="t">۵ منٹ</span></h2>
  <div style="margin:.4mm 0 1.6mm;padding:1.4mm 3.4mm;background:#fff;border-radius:3mm;border:.3mm solid #C7D4EC;display:flex;align-items:center;gap:3mm"><div class="small" style="flex:1">کلاس سے پہلے ا، ب، پ، ت، ٹ بورڈ پر بڑے لکھیں اور ہر حرف کو کاغذ سے ڈھانپ دیں۔</div></div>
  <ol>
   <li><span class="do">منظر بنائیں (۱ منٹ)۔</span>
    <div class="bub bub0"><b class="t">کہیں:</b> پانچ نئے دوست آج ہمارے سکول آئے ہیں۔ یہ حروف ہیں۔ آئیں، ان سے ملیں۔</div></li>
   <li><span class="do">دوستوں سے ملیں (۲ منٹ)۔</span> ایک حرف سے کاغذ ہٹائیں۔ اس کی آواز بولیں۔ بچے آپ کے بعد وہی آواز بولیں اور حرف کو ہاتھ ہلائیں۔ پہلے ا، پھر ب، پ، ت، ٹ۔</li>
   <li><span class="do">کون سا حرف چھپا ہے؟ (۲ منٹ)۔</span> ایک حرف کو دوبارہ ڈھانپیں۔
    <div class="bub bub0"><b class="t">کہیں:</b> کون سا حرف چھپا ہے؟</div>بچے اس کی آواز بتائیں۔ کاغذ ہٹا کر دیکھیں۔ تین بار کھیلیں: ا، پھر ٹ، پھر ب۔</li>
  </ol></div>

 <div class="board"><h3>Write on the board &nbsp;·&nbsp; بورڈ پر لکھیں</h3>
  <div style="display:flex;gap:4mm;align-items:flex-start">
   <div style="flex:1.2"><div style="font-size:8.8pt;color:#fff;line-height:1.8">آج کے حروف</div>
    <div style="font-size:30pt;line-height:1.5;letter-spacing:0;word-spacing:.35em">{" ".join(LETTERS)}</div></div>
   <div style="flex:1;border-inline:.4mm dashed #7E9A8F;padding:0 4mm">
    <div style="font-size:8.8pt;color:#fff;line-height:1.8">تصویر والے الفاظ</div>
    <div style="font-size:13pt;line-height:1.85">{"<br>".join(f"{l} &nbsp;{WORD[l]}" for l in LETTERS)}</div></div>
   <div style="flex:1;font-size:10.2pt;line-height:1.85"><div style="font-size:8.8pt;color:#fff">ہمارے چار کام</div>
    <b style="color:#FFD966">۱</b> آواز بولیں<br><b style="color:#FFD966">۲</b> تصویر کا لفظ بولیں<br><b style="color:#FFD966">۳</b> ٹریس کریں<br><b style="color:#FFD966">۴</b> لکھیں</div>
  </div></div>
</div>
{F(2)}</section>"""


# ---------------- PAGE 3 ----------------
def letter_row(i, l):
    return (f'<div style="display:flex;gap:3mm;align-items:center;border:.4mm solid var(--line);border-radius:3mm;padding:.6mm 3mm;margin-bottom:1.2mm;background:#fff">'
            f'<div style="width:14mm;flex:none;text-align:center"><span class="num" style="width:6.4mm;height:6.4mm;font-size:10pt">{ur(i)}</span>'
            f'<div class="small" style="line-height:1.5">۴ منٹ</div></div>'
            f'<div style="flex:none">{tile(l, 22, 21, 30)}</div>'
            f'<div style="flex:none" title="stroke order">{stroke_box(l, 40)}</div>'
            f'<div style="width:19mm;flex:none">{pic(l)}</div>'
            f'<div style="flex:1;font-size:9.6pt;line-height:1.7"><div style="font-size:14pt;font-weight:700;line-height:1.5">{WORD[l]}</div>'
            f'<div><b>آواز:</b> <b class="sn" style="font-size:12pt">{SOUND[l]}</b> <span class="small">{HOW[l]}</span></div>'
            f'<div><b>دھیان دیں:</b> {LOOK[l]}</div></div></div>')


def page3():
    rows = "".join(letter_row(i + 1, l) for i, l in enumerate(LETTERS))
    blocks = [("آواز بولیں", "۱ منٹ", "حرفی کارڈ دکھائیں اور آواز بولیں۔ بچے دو بار دہرائیں۔"),
              ("تصویر کا لفظ", "۱ منٹ", "تصویر دکھائیں اور لفظ بولیں۔ پہلی آواز پر زور دیں۔ بچے دہرائیں۔"),
              ("ٹریس کریں", "۱ منٹ", "ہوا میں، پھر میز پر انگلی سے حرف ٹریس کریں۔ ساتھ آواز بولیں۔"),
              ("لکھیں", "۱ منٹ", "بورڈ پر حرف لکھیں۔ بچے کاپی پر لکھیں اور چارٹ سے ملائیں۔")]
    bx = "".join(f'<div style="flex:1;background:#fff;border-radius:3mm;padding:.8mm 2.4mm;border:.3mm solid #C7D4EC"><div style="display:flex;align-items:center;gap:2mm"><span class="n2" style="width:6mm;height:6mm;font-size:9.5pt">{ur(i+1)}</span><b style="font-size:10pt">{t}</b><span class="small" style="margin-inline-start:auto">{m}</span></div><div style="font-size:8.8pt;line-height:1.75">{d}</div></div>' for i, (t, m, d) in enumerate(blocks))
    return f"""<section class="page">
{bar2("میں کر کے دکھاؤں", "I do · teach new letters", "پانچ حروف، ہر حرف کے لیے چار کام", "۲۰ منٹ")}
<div class="content">
 <div class="box sky" style="padding:1.6mm 4mm"><h2 style="margin-bottom:.4mm"><span class="en">Four actions</span>ہر حرف کے لیے یہی ۴ کام <span class="t">ہر حرف ۴ منٹ</span></h2>
  <div style="display:flex;gap:2.2mm">{bx}</div>
  <div class="small">ا کے لیے چاروں کام کریں۔ پھر یہی ب، پ، ت اور ٹ کے لیے دہرائیں۔ ٹریس کرتے وقت تیر کی سمت دیکھیں: <b>۱</b> حرف کا جسم، <b>۲</b> نقطے یا نشانی۔</div></div>
 {rows}
 <div class="box mint" style="margin:1.6mm 0 0"><h2 style="margin-bottom:.4mm"><span class="en">Worked example · Watch for</span>مثال: حرف ب اور خیال رکھیں</h2>
  <div style="display:flex;gap:4mm;align-items:flex-start">
   <div style="flex:1.25">{talk("teacher_point", '<b class="t">کہیں:</b> یہ ب ہے۔ اس کی آواز بْ ہے۔ میرے ساتھ بولیں: بْ۔<br><b class="t">کہیں:</b> تصویر بٹن ہے۔ بٹن کی پہلی آواز بْ ہے۔ بولیں: بْ۔', 20)}
    <div style="font-size:9pt;line-height:1.75;margin-top:.8mm">پھر ب کو ہوا میں ٹریس کریں، میز پر ٹریس کریں، کاپی پر لکھیں اور چارٹ سے ملائیں۔</div></div>
   <div style="flex:1"><ul style="font-size:8.9pt;line-height:1.75;margin:0">
    <li>آوازیں چھوٹی اور صاف بولیں: بْ، “با” نہیں۔</li>
    <li>ب، پ، ت، ٹ کی شکل ملتی ہے۔ فرق نقطوں کا ہے۔ نقطے انگلی سے گنوائیں۔</li>
    <li>ت میں زبان دانتوں کے پیچھے، ٹ میں زبان کی نوک مڑی ہوئی۔ دونوں الگ الگ سنائیں۔</li></ul></div>
  </div></div>
</div>
{F(3)}</section>"""


# ---------------- PAGE 4 ----------------
def page4():
    return f"""<section class="page p4">
{bar2("ہم سب مل کر", "We do · practise together", "پوری کلاس اپنی میز کے پاس کھڑی ہو کر", "۱۲ منٹ")}
<div class="content">
 <div class="box mint"><h2><span class="enh">1 · Say the sounds</span> <span class="t">۴ منٹ</span></h2>
  <div style="display:flex;gap:4mm"><div style="flex:1.7">{steps(["بچے اپنی میز کے پاس کھڑے ہوں۔ چارٹ پر ایک حرف کی طرف اشارہ کریں۔",
          "پہلا راؤنڈ: ا، ب، پ، ت، ٹ کی طرف ترتیب سے اشارہ کریں۔ پوری کلاس <b>آواز</b> بولے۔",
          "دوسرا راؤنڈ: اسی طرح ملی جلی ترتیب میں اشارہ کریں: ب، ا، ت، پ، ٹ۔"])}</div>
   <div style="flex:1;background:#fff;border-radius:3mm;padding:1.4mm 3mm;align-self:flex-start"><div style="font-size:8.8pt;font-weight:700;color:var(--navy);line-height:1.8">آوازیں</div>
    <div style="font-size:12pt;line-height:1.8">{sounds(CHANT_ORDER)}</div><div class="small">ہر آواز چھوٹی اور صاف، آخر میں کوئی آواز نہیں۔</div></div></div></div>

 <div class="box sky"><h2><span class="enh">2 · Show me</span> <span class="t">۴ منٹ</span></h2>
  <div style="display:flex;gap:4mm">
   <div style="flex:1.7">{steps(["بچے اپنی <b>ڈیسک پٹی</b> سامنے رکھیں۔",
          "ایک آواز دو بار بولیں۔ بچے پٹی پر وہ حرف چھوئیں۔",
          "بچوں کی انگلیاں دیکھیں۔ کسی نے غلط حرف چھوا؟ چارٹ پر صحیح حرف دکھائیں اور سب مل کر آواز بولیں۔"])}
    <div style="margin-top:1.4mm">{talk("teacher_point", '<b class="t">کہیں:</b> مجھے دکھاؤ ... بْ!', 18)}</div></div>
   <div style="flex:1;background:#fff;border-radius:3mm;padding:1.4mm 3mm;align-self:flex-start"><div style="font-size:8.8pt;font-weight:700;color:var(--navy);line-height:1.8">آوازیں، اسی ترتیب میں</div>
    <div style="font-size:12pt;line-height:1.8">{sounds(SHOW_ME)}</div></div>
  </div></div>

 <div class="box cream"><h2><span class="enh">3 · Write it</span> <span class="t">۴ منٹ</span></h2>
  <div style="display:flex;gap:4mm"><div style="flex:1.7">{steps(["بچے کاپی اور پنسل اٹھائیں۔",
          "آواز بولیں۔ بچے وہ حرف لکھیں۔ پھر بورڈ پر وہ حرف لکھیں۔",
          "بچے اپنا حرف بورڈ اور چارٹ سے ملائیں اور ضرورت ہو تو ٹھیک کریں۔"])}
    <div style="margin-top:1.4mm"><div class="bub bub0"><b class="t">کہیں:</b> لکھیں ... تْ!</div></div></div>
   <div style="flex:1;background:#fff;border-radius:3mm;padding:1.4mm 3mm;align-self:flex-start"><div style="font-size:8.8pt;font-weight:700;color:var(--navy);line-height:1.8">اس ترتیب میں بولیں</div><div style="font-size:12pt;line-height:1.8">{sounds(WRITE_CALLS)}</div></div></div></div>

 <div class="box" style="position:absolute;left:0;right:0;bottom:0;margin:0;background:#fff;border:.7mm solid #001F3F"><div style="display:flex;gap:5mm">
  <div style="flex:1.1"><h2><span class="en">Check before moving on</span>آگے بڑھنے سے پہلے جانچ</h2><div style="line-height:1.85">۴ یا ۵ بچوں سے سنیں: آپ جس حرف کی طرف اشارہ کریں، بچہ اس کی آواز بتائے۔<br><b style="color:#001F3F;text-decoration:underline">زیادہ تر درست؟</b> آگے بڑھیں۔ <b style="color:#001F3F;text-decoration:underline">زیادہ تر غلط؟</b> ۲ منٹ “مجھے دکھاؤ” دوبارہ کریں۔</div></div>
  <div style="flex:1;border-inline-start:.4mm solid #001F3F;padding-inline-start:5mm"><h2><span class="en">While you walk around</span>کلاس میں گھومتے ہوئے</h2><ul style="line-height:1.85;margin:0"><li>انگلی صحیح حرف پر ہے؟</li><li>آوازیں چھوٹی اور صاف ہیں؟</li><li>حرف صحیح سمت میں لکھے جا رہے ہیں؟</li><li>ہر بار مختلف بچے سنیں: ۴ یا ۵، سب نہیں۔</li></ul></div>
 </div></div>
</div>
{F(4)}</section>"""


# ---------------- PAGE 5 ----------------
def page5():
    t1 = " ، ".join(f'<b style="font-size:13pt">{l}</b>' for l in T1_LETTERS)
    t2 = " &nbsp; ".join(f'<b>{WORD[l]} ← <span style="font-size:13pt">{l}</span></b>' for l in T2_PICS)
    t3 = "".join(f'<span style="display:inline-block;margin-inline-start:4mm"><b style="font-size:12pt">{tg}:</b> ' + "، ".join(ur(i + 1) for i, o in enumerate(opts) if o == tg) + '</span>' for tg, opts in T3_ROWS)
    key = ""
    for i, it in enumerate(EXIT):
        act = "بچہ لکھے" if not it["options"] else "گھیریں"
        key += (f'<tr><td><b>{ur(i+1)}</b></td><td><b class="sn" style="font-size:12pt;line-height:1.4">{SOUND[it["sound"]]}</b></td>'
                f'<td><span style="font-size:14pt;font-weight:700;line-height:1.4">{it["answer"]}</span> <span class="small">{act}</span></td></tr>')
    return f"""<section class="page">
{bar2("اکیلے اور خروجی جانچ", "You do · exit check", "اکیلے (۸ منٹ)، پھر خروجی جانچ (۱۰ منٹ)", "۱۸ منٹ")}
<div class="content">
 <div class="box mint" style="padding-bottom:1.4mm"><h2 style="margin-bottom:0"><span class="en">Your turn</span>اکیلے <span class="t">۸ منٹ</span></h2>
  <p class="small" style="margin:0 0 .8mm">ورک شیٹ صفحہ ۱۔ ہر کام کی پہلی لائن سب مل کر کریں۔ بچے ڈیسک پٹی سے خود جانچیں اور ورک شیٹ جمع کروائیں۔</p>
  <table class="ans"><tr><th style="width:42mm">کام</th><th style="width:16mm">ورک شیٹ</th><th style="width:14mm">وقت</th><th>جوابات</th></tr>
   <tr><td><b>۱</b> ٹریس اور نقل</td><td>صفحہ ۱</td><td style="white-space:nowrap">۳ منٹ</td><td>{t1}</td></tr>
   <tr><td><b>۲</b> تصویر اور پہلا حرف ملائیں</td><td>صفحہ ۱</td><td style="white-space:nowrap">۳ منٹ</td><td>{t2}</td></tr>
   <tr><td><b>۳</b> وہی حرف گھیریں</td><td>صفحہ ۱</td><td style="white-space:nowrap">۲ منٹ</td><td><span class="small" style="color:var(--ink)">دائیں سے گنیں:</span> {t3}</td></tr>
  </table></div>

 <div class="box sky" style="padding-bottom:3mm"><h2><span class="en">Exit check</span>خروجی جانچ <span class="t">۱۰ منٹ</span></h2>
  <div style="display:flex;gap:4mm;align-items:flex-start">
   <div style="flex:1;background:#fff;border:.4mm solid #9AA6B5;border-radius:3mm;padding:1.4mm 4mm">
    <div style="font-weight:700;font-size:11pt;line-height:1.8"><span class="n2" style="margin-inline-end:2mm">الف</span>بچوں کا کام <span class="small">· ۶ منٹ</span></div>
    <div style="line-height:1.9"><b>ورک شیٹ صفحہ ۲:</b> “سنیں اور گھیریں”۔ آئٹم ۱ تا ۴ آواز سن کر صحیح حرف کے گرد دائرہ لگائیں۔ آئٹم ۵ میں حرف لکھیں۔</div></div>
   <div style="flex:1;background:#fff;border:.4mm solid #9AA6B5;border-radius:3mm;padding:1.4mm 4mm">
    <div style="font-weight:700;font-size:11pt;line-height:1.8"><span class="n2" style="margin-inline-end:2mm">ب</span>استاد کا کام <span class="small">· ۴ منٹ</span></div>
    <div style="line-height:1.9">۴ یا ۵ بچوں کو چارٹ پر <b>{" ، ".join(PART_B)}</b> میں سے اشارہ کر کے آواز بلوائیں۔ ہر دن مختلف بچے۔</div></div>
  </div>
  <div style="display:flex;gap:4mm;margin-top:2.4mm;align-items:flex-start">
   <div style="flex:1"><div style="font-weight:700;font-size:10.5pt;line-height:1.8">حصہ الف میں استاد: ہر آئٹم دو بار بولیں، ۳۰ سیکنڈ انتظار کریں۔</div>
    <div class="bub bub0" style="font-size:10.4pt;line-height:1.8"><b class="t">کہیں:</b> نمبر ایک۔ جو حرف بْ کہتا ہے، اس کے گرد دائرہ لگائیں۔</div></div>
   <div style="flex:1"><table class="ans" style="font-size:9.4pt;line-height:1.5"><tr><th style="width:9mm;padding:0 1mm">آئٹم</th><th style="padding:0 1mm">آپ بولیں</th><th style="padding:0 1mm">صحیح جواب</th></tr>{key}</table></div>
  </div>
 </div>

 <div class="box grey" style="margin-bottom:1.4mm"><b><span class="en" style="margin-inline-end:3mm">At home · optional</span>گھر پر (اختیاری):</b> گھر میں کسی کو ا، ب، پ، ت، ٹ کی آوازیں اور انار، بٹن، پری، توا، ٹرک سنائیں۔</div>
 <div class="small" style="line-height:1.7">{PASS_NOTE}</div>
 <div class="box" style="position:absolute;left:0;right:0;bottom:0;margin:0;background:#fff;border:.7mm solid #001F3F;padding:2mm 5mm"><h2 style="margin-bottom:.6mm"><span class="en">Score and decide</span>نتیجہ دیکھ کر فیصلہ کریں</h2>
  <div style="display:flex;gap:4mm;font-size:10pt;line-height:1.8">
   <div style="flex:1"><b>ٹھیک چل رہا ہے:</b> ۴ یا ۵ درست۔</div>
   <div style="flex:1.3"><b>مشق چاہیے:</b> ۳ درست۔ دن ۲ پر “مجھے دکھاؤ” دوبارہ کریں۔</div>
   <div style="flex:1.3"><b>دوبارہ پڑھائیں:</b> ۲ یا کم درست۔ غلط حروف کے ۴ کام چھوٹے گروپ میں دہرائیں۔</div></div>
  <div class="small">ہر بچے کی حالت کلاس ٹریکر پر لکھیں۔ نمبر بلند آواز میں نہ بتائیں۔</div></div>
</div>
{F(5)}</section>"""


def build():
    html = head_html2("Level 1 Urdu Day 1 - Lesson Plan v3").replace("</style>",CSS3+"</style>") + page1() + page2() + page3() + page4() + page5() + OVERFLOW_JS
    out = os.path.join(WORK, "lpu3.html")
    open(out, "w", encoding="utf-8").write(html)
    return out


if __name__ == "__main__":
    print(build())
