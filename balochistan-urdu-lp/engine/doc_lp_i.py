"""Level 2 Intermediate, Urdu, Day 1 (final planner): Lesson Plan. Same approved format as the Beginner Day 1 LP (v4)."""
from common_i import *

TOTAL = 5
F = lambda n: foot(FOOT_LP, n, TOTAL)
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
.p2 .bub{font-size:13pt}.p2 .small{font-size:10pt}.p2 .board{padding:4mm 6mm}
.p4 .box{margin-bottom:5mm}
.wc{flex:1;background:#fff;border:.4mm solid #9AA6B5;border-radius:2.6mm;padding:.8mm 1.4mm;text-align:center;min-width:0}
.wc .pw{width:15mm;margin:0 auto}
.wc .w{font-size:14pt;font-weight:700;line-height:1.55;color:#001F3F}
.wc .pt{font-size:9.4pt;line-height:1.6;color:#1D2025}
.wd{display:inline-block;background:#fff;border:.4mm solid #9AA6B5;border-radius:2mm;padding:0 2.4mm;margin:.4mm .6mm;font-weight:700;font-size:13pt;line-height:1.7;color:#001F3F}
"""


def steps(items):
    return '<div class="stp">' + "".join(f'<div class="s"><span class="n2">{ur(i+1)}</span><div>{t}</div></div>' for i, t in enumerate(items)) + '</div>'


def talk(img, html, w=22):
    return f'<div class="talk"><div class="who" style="width:{w}mm">{scene(img)}</div><div class="bub">{html}</div></div>'


def say(html, size=None):
    st = f' style="font-size:{size}pt;line-height:1.8"' if size else ""
    return f'<div class="bub bub0"{st}><b class="t">کہیں:</b> {html}</div>'


def wchips(keys):
    return "".join(f'<span class="wd">{wd(k)}</span>' for k in keys)


# ---------------- PAGE 1 ----------------
def page1():
    ribbon = ""
    for d in range(1, 34):
        if d == 1:
            st = "background:#F5B301;color:#001F3F;font-weight:700;outline:.5mm solid #001F3F"
        elif d <= 4:
            st = "background:#FBE08A;color:#001F3F"
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
    tiles = "".join(f'<div style="text-align:center"><div>{mtile(m, 17, 20, 26)}</div><div style="font-size:10.5pt;font-weight:700;line-height:1.5">{MNAME[m]}</div></div>' for m in MARKS)
    return f"""<section class="page p1">
<div style="background:var(--navy);height:44mm;color:#fff;display:flex;align-items:center;padding:0 10mm;gap:6mm;position:relative">
 <div style="color:var(--gold);font-weight:700;line-height:1.3;text-align:center"><div style="font-size:15pt;color:#fff">دن</div><div style="font-size:50pt;line-height:1.25">۱</div><div style="font-size:15pt;color:#fff">از ۳۳</div></div>
 <div style="flex:1;padding-inline-start:5mm;border-inline-start:.5mm solid #2B4A6B">
  <span class="en" style="color:var(--gold)">Day 1 of 33 · Teach and model</span>
  <div style="font-size:16pt;font-weight:700;line-height:1.7">لیول ۲ درمیانہ · اردو</div>
  <div style="font-size:9.5pt;color:#C9D6E6;line-height:1.7">بلوچستان ونٹر پروگرام · درست سطح پر تدریس</div>
  <div style="margin-top:1.4mm;display:flex;gap:2mm"><span class="pill" style="font-size:9.5pt">۶۰ منٹ</span><span class="pill" style="font-size:9.5pt;background:var(--gold);color:var(--navy)">لفظ پڑھیں</span></div>
 </div>
 <div style="width:36mm;background:#fff;border-radius:5mm;overflow:hidden;border:.8mm solid var(--gold)">{scene("pair_book")}</div>
</div>
<div class="content" style="top:47mm">
 <div style="display:flex;gap:.8mm;margin-bottom:.4mm">{ribbon}</div>
 <div class="small" style="margin-bottom:2mm">۳۳ دن۔ دن ۱ تا ۴ (سنہری): لفظ اور چھوٹے جملے پڑھنا۔ دن ۵ سے لفظ لکھنا۔ دن ۳۱ تا ۳۳ (سبز): آخری دہرائی۔</div>

 <div class="box gold" style="display:flex;gap:4mm;align-items:center;padding:4mm 6mm;margin-bottom:5mm">
  <div style="display:flex;gap:2.4mm">{tiles}</div>
  <div><span class="en" style="color:var(--navy)">Today's marks</span>
  <div style="font-size:14pt;font-weight:700;line-height:1.8">ایک حرف، چار نشانیاں، چار آوازیں</div></div>
 </div>

 <div class="box sky" style="margin-bottom:5mm"><h2><span class="en">Learning outcomes</span>آج کے سیکھنے کے مقاصد</h2>
  <p style="margin-bottom:.4mm"><span class="chip">U-I-01</span> <b>۳ سے ۵ حروف کے الفاظ اور چھوٹے جملے روانی سے پڑھنا</b></p>
  <p style="margin-bottom:.4mm"><span class="chip">U-I-06</span> <b>زبر، زیر اور پیش والے الفاظ پڑھنا</b></p>
  <p class="small" style="margin:0">دن ۱ تا ۴۔ اس سے پہلے: <span class="chip">U-B-07</span> دو یا تین حروف کے الفاظ پڑھنا۔</p>
 </div>

 <div class="box" style="margin-bottom:5mm;background:#E3F4EC;border:.7mm solid #0B8F6A;color:#001F3F"><h2 style="color:#001F3F"><span class="en">Today's goal</span>آج کا ہدف</h2><div style="font-size:15pt;font-weight:700;line-height:2;color:#001F3F">زبر، زیر، پیش اور جزم والے الفاظ صحیح آواز سے پڑھیں اور ایک چھوٹا جملہ روانی سے پڑھیں۔</div></div>

 <div style="margin-bottom:5mm"><span class="en" style="margin-inline-end:3mm">The 60 minutes</span><span style="font-size:9.5pt;font-weight:700;color:var(--navy)">وقت کی تقسیم (۶۰ منٹ)</span>
  <div style="display:flex;border-radius:2.5mm;overflow:hidden;margin-top:.6mm">{tbar}</div></div>

 <div class="box mint" style="margin-bottom:0"><h2><span class="en">To prepare</span>تیاری (تقریباً ۲۰ منٹ)</h2>
  <div style="columns:2;column-gap:6mm;font-size:11.5pt;line-height:2.1">
   <div>☐ نشانیوں کا چارٹ دیوار پر لگائیں</div><div>☐ بارہ تصویر والے لفظی کارڈ کاٹیں</div>
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
   {talk("teacher_point", "السلام علیکم بچو! آج ہم لفظوں کو صحیح آواز کے ساتھ پڑھنا سیکھیں گے۔", 20)}</div>
  <div><span class="do">۲۔ چھ تصویریں بولیں (۴ منٹ)۔</span> لفظی کارڈ میں سے چھ تصویریں دکھائیں: <b>{"، ".join(wd(k) for k in PAIR_READ)}</b>۔ لفظ بولیں۔ بچے دو بار دہرائیں۔ پھر کوئی لفظ بولیں اور بچے اس کی تصویر دکھائیں۔</div></div>

 <div class="box sky"><h2><span class="en">Hook</span>دلچسپی: ایک حرف، کئی آوازیں <span class="t">۵ منٹ</span></h2>
  <ol>
   <li><span class="do">منظر بنائیں (۱ منٹ)۔</span> بورڈ پر بڑا <b>{BASE}</b> لکھیں۔
    {say("یہ حرف ب ہے۔ آج یہ اپنی آواز بدلے گا۔ کیسے؟ ایک چھوٹی سی نشانی سے!")}</li>
   <li><span class="do">تین آوازیں سنیں (۲ منٹ)۔</span> ب کے ساتھ ایک ایک نشانی لکھیں: <b>{MEX["zabar"][0]}، {MEX["zer"][0]}، {MEX["pesh"][0]}</b>۔ ہر ایک کی آواز بولیں۔ بچے آپ کے بعد وہی آواز بولیں۔</li>
   <li><span class="do">کون سی آواز؟ (۲ منٹ)۔</span> بورڈ پر ایک حرف نشانی کے ساتھ لکھیں۔
    {say("کون سی آواز؟")}بچے آواز بتائیں۔ تین بار کھیلیں: <b>{MEX["zer"][1]}</b>، پھر <b>{MEX["pesh"][2]}</b>، پھر <b>{MEX["zabar"][2]}</b>۔</li>
  </ol></div>

 <div class="board"><h3>Write on the board &nbsp;·&nbsp; بورڈ پر لکھیں</h3>
  <div style="display:flex;gap:4mm;align-items:flex-start">
   <div style="flex:1.2"><div style="font-size:8.8pt;color:#fff;line-height:1.8">ایک حرف، چار نشانیاں</div>
    <div style="font-size:34pt;line-height:1.5;letter-spacing:0;word-spacing:.35em">{BASE}{MSYM["zabar"]} {BASE}{MSYM["zer"]} {BASE}{MSYM["pesh"]} {BASE}{MSYM["jazm"]}</div></div>
   <div style="flex:1;border-inline:.4mm dashed #7E9A8F;padding:0 4mm">
    <div style="font-size:8.8pt;color:#fff;line-height:1.8">نشانی کا نام اور جگہ</div>
    <div style="font-size:12pt;line-height:1.95">{"<br>".join(f"<b style='color:#FFD966'>{MNAME[m]}</b> &nbsp;{MSHORT[m]}" for m in MARKS)}</div></div>
   <div style="flex:.9;font-size:10.2pt;line-height:1.85"><div style="font-size:8.8pt;color:#fff">ہمارے چار کام</div>
    <b style="color:#FFD966">۱</b> نشانی دیکھیں<br><b style="color:#FFD966">۲</b> آواز بولیں<br><b style="color:#FFD966">۳</b> جوڑ کر پڑھیں<br><b style="color:#FFD966">۴</b> پورا لفظ پڑھیں</div>
  </div></div>
</div>
{F(2)}</section>"""


# ---------------- PAGE 3 ----------------
def block_row(i, m):
    cards = "".join(f'<div class="wc"><div class="pw">{wpic(k)}</div><div class="w">{wd(k)}</div><div class="pt">{parts_html(k)}</div></div>' for k in BLOCK_WORDS[m])
    return (f'<div style="display:flex;gap:2.6mm;align-items:center;border:.4mm solid var(--line);border-radius:3mm;padding:.8mm 2.4mm;margin-bottom:1.4mm;background:#fff">'
            f'<div style="width:12mm;flex:none;text-align:center"><span class="num" style="width:6.4mm;height:6.4mm;font-size:10pt">{ur(i)}</span>'
            f'<div class="small" style="line-height:1.5">۵ منٹ</div></div>'
            f'<div style="flex:none">{mtile(m, 21, 20, 28)}</div>'
            f'<div style="flex:1.05;min-width:0;font-size:9.2pt;line-height:1.7"><div style="font-size:14pt;font-weight:700;line-height:1.5">{MNAME[m]}</div>'
            f'<div>{MWHERE[m]}</div><div><b>آواز:</b> <b class="sn" style="font-size:13pt">{MSOUND[m] if m != "jazm" else "اس حرف پر آواز نہیں"}</b></div></div>'
            f'<div style="flex:3.1;display:flex;gap:2mm;min-width:0">{cards}</div></div>')


def page3():
    rows = "".join(block_row(i + 1, m) for i, m in enumerate(MARKS))
    blocks = [("نشانی، آواز", "۱ منٹ", "حرف پر نشانی دکھائیں اور اس کی آواز بولیں۔ بچے دہرائیں۔"),
              ("جوڑ کر پڑھیں", "۱ منٹ", "بَ، دَ، کَ جیسے حروف پر وہی نشانی لگا کر پڑھیں۔"),
              ("ٹکڑے پڑھیں", "۲ منٹ", "لفظ کو ٹکڑوں میں پڑھیں، پھر پورا لفظ بولیں۔"),
              ("تصویر", "۱ منٹ", "تصویر دکھائیں۔ بچے لفظ پڑھ کر تصویر سے ملائیں۔")]
    assert sum(int(t.split()[0].translate(str.maketrans("۰۱۲۳۴۵۶۷۸۹", "0123456789"))) for _, t, _ in blocks) == 5
    bx = "".join(f'<div style="flex:1;background:#fff;border-radius:3mm;padding:.8mm 2.4mm;border:.3mm solid #C7D4EC"><div style="display:flex;align-items:center;gap:2mm"><span class="n2" style="width:6mm;height:6mm;font-size:9.5pt">{ur(i+1)}</span><b style="font-size:10pt">{t}</b><span class="small" style="margin-inline-start:auto">{mn}</span></div><div style="font-size:8.8pt;line-height:1.75">{d}</div></div>' for i, (t, mn, d) in enumerate(blocks))
    return f"""<section class="page">
{bar2("میں کر کے دکھاؤں", "I do · teach the marks", "چار نشانیاں، ہر نشانی کے لیے چار کام", "۲۰ منٹ")}
<div class="content">
 <div class="box sky" style="padding:1.6mm 4mm"><h2 style="margin-bottom:.4mm"><span class="en">Four actions</span>ہر نشانی کے لیے یہی ۴ کام <span class="t">ہر نشانی ۵ منٹ</span></h2>
  <div style="display:flex;gap:2.2mm">{bx}</div>
  <div class="small">زبر سے شروع کریں۔ پھر یہی زیر، پیش اور جزم کے لیے۔ ہر لفظ کے نیچے لکھے ٹکڑے <b>آواز آواز کر کے</b> پڑھنے کے لیے ہیں۔</div></div>
 {rows}
 <div class="box mint" style="margin:1.6mm 0 0"><h2 style="margin-bottom:.4mm"><span class="en">Worked example · Watch for</span>مثال: لفظ {wd("qalam")} اور خیال رکھیں</h2>
  <div style="display:flex;gap:4mm;align-items:flex-start">
   <div style="flex:1.25">{talk("teacher_point", '<b class="t">کہیں:</b> یہ ق ہے۔ اس پر زبر ہے۔ آواز قَ۔ اگلا حرف لَ۔ آخری حرف م۔ ساتھ بولیں: قَ ... لَ ... م ... قَلَم!', 20)}
    <div style="font-size:9pt;line-height:1.75;margin-top:.8mm">پھر بچے تصویر دیکھیں، لفظ دوبارہ پڑھیں اور تصویر سے ملائیں۔</div></div>
   <div style="flex:1"><ul style="font-size:8.9pt;line-height:1.75;margin:0">
    <li>نشانی کی جگہ دکھائیں: زبر اور پیش اوپر، زیر نیچے۔</li>
    <li>آوازیں چھوٹی اور صاف بولیں، پہلے ٹکڑے، پھر پورا لفظ۔</li>
    <li>جزم والے حرف پر آواز نہ لگائیں: کُرْ، “کُرَ” نہیں۔</li></ul></div>
  </div></div>
</div>
{F(3)}</section>"""


# ---------------- PAGE 4 ----------------
def page4():
    return f"""<section class="page p4">
{bar2("ہم سب مل کر", "We do · practise together", "پوری کلاس لفظ پڑھتی ہے", "۱۲ منٹ")}
<div class="content">
 <div class="box mint"><h2><span class="enh">1 · Read together</span> <span class="t">۴ منٹ</span></h2>
  <div style="display:flex;gap:4mm"><div style="flex:1.5">{steps(["لفظی کارڈ ایک ایک کر کے دکھائیں۔ پوری کلاس لفظ پڑھے۔",
          "ہر کارڈ پر پہلے نشانی کی طرف اشارہ کریں، پھر لفظ پڑھوائیں۔",
          "اس ترتیب میں پڑھوائیں، ایک ہی نشانی لگاتار نہیں آتی۔"])}</div>
   <div style="flex:1.4;background:#fff;border-radius:3mm;padding:1.4mm 3mm;align-self:flex-start"><div style="font-size:8.8pt;font-weight:700;color:var(--navy);line-height:1.8">الفاظ، اسی ترتیب میں</div>
    <div style="line-height:1.8">{wchips(CHORUS)}</div></div></div></div>

 <div class="box sky"><h2><span class="enh">2 · Read with a partner</span> <span class="t">۴ منٹ</span></h2>
  <div style="display:flex;gap:4mm"><div style="flex:1.5">{steps(["بچے جوڑی میں بیٹھیں۔ ڈیسک پٹی دونوں کے بیچ رکھیں۔",
          "ایک بچہ چھ الفاظ پڑھے، دوسرا سنے۔ پھر باری بدلیں۔",
          "غلط پڑھا گیا لفظ ساتھی پٹی کی تصویر سے جانچے اور سب مل کر ٹھیک کریں۔"])}
    <div style="margin-top:1.4mm">{talk("teacher_point", '<b class="t">کہیں:</b> ساتھی کو پڑھ کر سنائیں۔ نشانی دیکھ کر پڑھیں!', 18)}</div></div>
   <div style="flex:1.4;background:#fff;border-radius:3mm;padding:1.4mm 3mm;align-self:flex-start"><div style="font-size:8.8pt;font-weight:700;color:var(--navy);line-height:1.8">چھ الفاظ جو ہر بچہ پڑھے</div>
    <div style="line-height:1.8">{wchips(PAIR_READ)}</div></div>
  </div></div>

 <div class="box cream"><h2><span class="enh">3 · Read the phrases</span> <span class="t">۴ منٹ</span></h2>
  <div style="display:flex;gap:4mm"><div style="flex:1.5">{steps(["بورڈ پر ایک جملہ لکھیں۔ الفاظ پر انگلی رکھ کر پہلے خود پڑھیں۔",
          "پوری کلاس ساتھ پڑھے۔ پھر چند بچے اکیلے پڑھیں۔",
          "رکے بغیر، ایک سانس میں پڑھنے کی کوشش کریں۔"])}
    <div style="margin-top:1.4mm">{say("جملہ ایسے پڑھیں جیسے آپ بات کر رہے ہیں!")}</div></div>
   <div style="flex:1.4;background:#fff;border-radius:3mm;padding:1.4mm 3mm;align-self:flex-start"><div style="font-size:8.8pt;font-weight:700;color:var(--navy);line-height:1.8">تین جملے</div>
    <div style="font-size:13pt;line-height:2;font-weight:700">{"<br>".join(PHRASES)}</div></div></div></div>

 <div class="box" style="position:absolute;left:0;right:0;bottom:0;margin:0;background:#fff;border:.7mm solid #001F3F"><div style="display:flex;gap:5mm">
  <div style="flex:1.1"><h2><span class="en">Check before moving on</span>آگے بڑھنے سے پہلے جانچ</h2><div style="line-height:1.85">۴ یا ۵ بچوں سے سنیں: آپ جس لفظ کی طرف اشارہ کریں، بچہ اسے پڑھے۔<br><b style="color:#001F3F;text-decoration:underline">زیادہ تر درست؟</b> آگے بڑھیں۔ <b style="color:#001F3F;text-decoration:underline">زیادہ تر غلط؟</b> ۲ منٹ نشانی اور آواز دوبارہ کریں۔</div></div>
  <div style="flex:1;border-inline-start:.4mm solid #001F3F;padding-inline-start:5mm"><h2><span class="en">While you walk around</span>کلاس میں گھومتے ہوئے</h2><ul style="line-height:1.85;margin:0"><li>نشانی صحیح پڑھی جا رہی ہے؟</li><li>جزم والے حرف پر آواز تو نہیں لگ رہی؟</li><li>بچے ٹکڑوں سے پورا لفظ جوڑ رہے ہیں؟</li><li>ہر بار مختلف بچے سنیں: ۴ یا ۵، سب نہیں۔</li></ul></div>
 </div></div>
</div>
{F(4)}</section>"""


# ---------------- PAGE 5 ----------------
def page5():
    _t1 = [f'<b>{wd(k)} ← {ur(T1_PICS.index(k) + 1)}</b>' for k in T1]
    t1 = " &nbsp; ".join(_t1[:3]) + "<br>" + " &nbsp; ".join(_t1[3:])
    t3 = "&nbsp; ".join(f'<b>{wd(k)[0]}</b> {ur(i+1)}: <b style="font-size:13pt">{l}{MSYM[m]}</b>' for i, (k, l, m) in enumerate(T3))
    key = ""
    for i, it in enumerate(EXIT):
        pos = it["options"].index(it["answer"]) + 1
        key += (f'<tr><td><b>{ur(i+1)}</b></td><td><b style="font-size:12pt;line-height:1.4">{it["text"]}</b></td>'
                f'<td><span class="small">تصویر {ur(pos)}:</span> <b>{wd(it["answer"]) if it["answer"] in W else it["answer"]}</b></td></tr>')
    return f"""<section class="page">
{bar2("اکیلے اور خروجی جانچ", "You do · exit check", "اکیلے (۸ منٹ)، پھر خروجی جانچ (۱۰ منٹ)", "۱۸ منٹ")}
<div class="content">
 <div class="box mint" style="padding-bottom:1.4mm"><h2 style="margin-bottom:0"><span class="en">Your turn</span>اکیلے <span class="t">۸ منٹ</span></h2>
  <p class="small" style="margin:0 0 .8mm">ورک شیٹ صفحہ ۱۔ ہر کام کی پہلی لائن سب مل کر کریں۔ بچے ڈیسک پٹی سے خود جانچیں اور ورک شیٹ جمع کروائیں۔</p>
  <table class="ans"><tr><th style="width:42mm">کام</th><th style="width:16mm">ورک شیٹ</th><th style="width:14mm">وقت</th><th>جوابات</th></tr>
   <tr><td><b>۱</b> لفظ پڑھیں اور تصویر سے ملائیں</td><td>صفحہ ۱</td><td style="white-space:nowrap">۳ منٹ</td><td><span class="small" style="color:var(--ink)">تصویر نمبر اوپر سے:</span><br>{t1}</td></tr>
   <tr><td><b>۲</b> جملے ساتھی کو پڑھ کر سنائیں</td><td>صفحہ ۱</td><td style="white-space:nowrap">۳ منٹ</td><td>ساتھی ہر جملے پر ٹک لگائے: {"، ".join(PHRASES)}</td></tr>
   <tr><td><b>۳</b> پہلے حرف کی آواز گھیریں</td><td>صفحہ ۱</td><td style="white-space:nowrap">۲ منٹ</td><td>{t3}</td></tr>
  </table></div>

 <div class="box sky" style="padding-bottom:3mm"><h2><span class="en">Exit check</span>خروجی جانچ <span class="t">۱۰ منٹ</span></h2>
  <div style="display:flex;gap:4mm;align-items:flex-start">
   <div style="flex:1;background:#fff;border:.4mm solid #9AA6B5;border-radius:3mm;padding:1.4mm 4mm">
    <div style="font-weight:700;font-size:11pt;line-height:1.8"><span class="n2" style="margin-inline-end:2mm">الف</span>بچوں کا کام <span class="small">· ۶ منٹ</span></div>
    <div style="line-height:1.9"><b>ورک شیٹ صفحہ ۲:</b> “پڑھیں اور تصویر پر دائرہ لگائیں”۔ ہر لفظ یا جملہ خاموشی سے پڑھیں اور اس کی تصویر کے گرد دائرہ لگائیں۔</div></div>
   <div style="flex:1;background:#fff;border:.4mm solid #9AA6B5;border-radius:3mm;padding:1.4mm 4mm">
    <div style="font-weight:700;font-size:11pt;line-height:1.8"><span class="n2" style="margin-inline-end:2mm">ب</span>استاد کا کام <span class="small">· ۴ منٹ</span></div>
    <div style="line-height:1.9">۴ یا ۵ بچوں سے ایک ایک کارڈ پڑھوائیں (تین لفظ فی کارڈ، رہنما شیٹ دیکھیں)۔ ہر دن مختلف بچے۔</div></div>
  </div>
  <div style="margin-top:2.4mm"><table class="ans" style="font-size:9.4pt;line-height:1.5"><tr><th style="width:9mm;padding:0 1mm">آئٹم</th><th style="padding:0 1mm">بچہ کیا پڑھے</th><th style="padding:0 1mm">صحیح جواب</th></tr>{key}</table></div>
 </div>

 <div class="box grey" style="margin-bottom:1.4mm"><b><span class="en" style="margin-inline-end:3mm">At home · optional</span>گھر پر (اختیاری):</b> گھر میں کسی کو آج کے جملے پڑھ کر سنائیں۔</div>

 <div class="box" style="position:absolute;left:0;right:0;bottom:0;margin:0;background:#fff;border:.7mm solid #001F3F;padding:2mm 5mm"><h2 style="margin-bottom:.6mm"><span class="en">Score and decide</span>نتیجہ دیکھ کر فیصلہ کریں</h2>
  <div style="display:flex;gap:4mm;font-size:10pt;line-height:1.8">
   <div style="flex:1"><b>ٹھیک چل رہا ہے:</b> ۴ یا ۵ درست۔</div>
   <div style="flex:1.3"><b>مشق چاہیے:</b> ۳ درست۔ دن ۲ پر ان بچوں کے ساتھ لفظ دوبارہ پڑھیں۔</div>
   <div style="flex:1.3"><b>دوبارہ پڑھائیں:</b> ۲ یا کم درست۔ جس نشانی میں غلطی ہوئی، اس کے ۴ کام چھوٹے گروپ میں دہرائیں۔</div></div>
  <div class="small">ہر بچے کی حالت کلاس ٹریکر پر لکھیں۔ نمبر بلند آواز میں نہ بتائیں۔</div></div>
</div>
{F(5)}</section>"""


def build():
    html = head_i("Level 2 Urdu Day 1 - Lesson Plan v1").replace("</style>", CSS3 + "</style>") + page1() + page2() + page3() + page4() + page5() + OVERFLOW_JS
    out = os.path.join(WORK, "lpi.html")
    open(out, "w", encoding="utf-8").write(html)
    return out


if __name__ == "__main__":
    print(build())
