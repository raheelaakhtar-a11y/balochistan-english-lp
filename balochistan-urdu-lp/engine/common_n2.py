"""v2 additions on top of common_u (v1 stays reproducible): English section tags (Poppins), speech bubbles, stroke-order diagrams,
print-safe (pale) tiles, and a minutes check so every page total matches the 60-minute plan."""
from common_n import *  # noqa: F401,F403
import itertools

CSS2 = r"""
@font-face{font-family:"Poppins";src:url("fonts/Poppins-Regular.ttf");font-weight:400}
@font-face{font-family:"Poppins";src:url("fonts/Poppins-SemiBold.ttf");font-weight:600}
@font-face{font-family:"Poppins";src:url("fonts/Poppins-Bold.ttf");font-weight:700}
.en{font-family:Poppins,Arial,sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;font-size:7.4pt;font-weight:600;letter-spacing:.07em;
text-transform:uppercase;color:var(--teal);line-height:1.5;white-space:nowrap}
.bar .en{color:var(--gold);font-size:8pt;display:block;line-height:1.3;text-align:right}
.box h2 .en{font-size:7.2pt;color:var(--grey);border:.3mm solid #B8C2D0;border-radius:99px;padding:0 2mm;background:#fff;line-height:1.55}
.navy h2 .en,.teal h2 .en{color:#fff;background:transparent;border-color:#6E86A3}
.say{font-size:11.6pt;line-height:1.95}
.bub{position:relative;background:#fff;border:.5mm solid var(--navy);border-radius:4mm;padding:.8mm 3.4mm;color:#14304F;font-size:11.6pt;line-height:1.95}
.bub:after{content:"";position:absolute;inset-inline-start:-2.6mm;top:5mm;width:3.6mm;height:3.6mm;background:#fff;border-inline-start:.5mm solid var(--navy);border-bottom:.5mm solid var(--navy);transform:rotate(45deg)}
.bub b.t{color:var(--teal)}
.talk{display:flex;gap:3mm;align-items:flex-start}
.talk .who{width:22mm;flex:none;background:#fff;border-radius:3mm;overflow:hidden;border:.4mm solid #C7D4EC}
.talk .bub{flex:1}
.sg{position:relative;display:inline-block;flex:none}
.sg .gl{position:absolute;inset:0;display:flex;align-items:flex-start;justify-content:center;line-height:1.3;padding-top:.014em;font-family:NNU,serif}
.sg svg{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
"""

# geometry in fractions of a 1.687em square (measured from the Noto Nastaliq glyphs): body stroke path, start marker, other marks
_BODY = {"ب": "M .79 .58 C .72 .80 .45 .83 .22 .62", "پ": "M .79 .58 C .72 .80 .45 .83 .22 .62", "ت": "M .79 .58 C .72 .80 .45 .83 .22 .62",
         "ٹ": "M .79 .66 C .72 .88 .45 .91 .22 .70", "ا": "M .49 .36 L .49 .79", "ث": "M .79 .58 C .72 .80 .45 .83 .22 .62"}
_START = {"ب": (.90, .50), "پ": (.90, .50), "ت": (.90, .50), "ٹ": (.90, .58), "ا": (.64, .34), "ث": (.90, .50)}
_MARK = {"ب": (.64, .97), "پ": (.65, .97), "ت": (.64, .42), "ٹ": (.64, .44), "ا": None, "ث": (.64, .42)}   # where the number 2 goes (dots / small mark)
_END = {"ب": (.22, .62), "پ": (.22, .62), "ت": (.22, .62), "ٹ": (.22, .70), "ا": (.49, .79), "ث": (.22, .62)}
_ctr = itertools.count(1)


def stroke_box(letter, size_pt=40, glyph="#A9B4C2", ink="#001F3F", num_bg="#F5B301", num_fg="#001F3F", mono=False, nums=True):
    """A letter drawn light grey with a numbered start dot and an arrow along the stroke (1 = body, 2 = dots / mark)."""
    k = next(_ctr)
    if mono:
        ink, num_bg, num_fg = "#000", "#fff", "#000"
    sx, sy = _START[letter]
    ex, ey = _END[letter]
    path = " ".join(f"{float(t)*100:.1f}" if t.replace('.', '', 1).isdigit() else t for t in _BODY[letter].replace(",", "").split())
    svg = (f'<svg viewBox="0 0 100 100"><defs><marker id="ah{k}" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">'
           f'<path d="M0 0 L10 5 L0 10 z" fill="{ink}"/></marker></defs>'
           f'<path d="{path}" fill="none" stroke="{ink}" stroke-width="3.4" stroke-linecap="round" marker-end="url(#ah{k})" opacity=".9"/>')
    if nums:
        stroke = f'stroke="{ink}" stroke-width="1.2"' if mono else ""
        svg += (f'<circle cx="{sx*100:.1f}" cy="{sy*100:.1f}" r="7.6" fill="{num_bg}" {stroke}/>'
                f'<text x="{sx*100:.1f}" y="{sy*100+4.6:.1f}" text-anchor="middle" font-size="12" font-family="NNU" fill="{num_fg}">۱</text>')
        m = _MARK[letter]
        if m:
            svg += (f'<circle cx="{m[0]*100:.1f}" cy="{m[1]*100:.1f}" r="6.8" fill="{num_bg}" {stroke}/>'
                    f'<text x="{m[0]*100:.1f}" y="{m[1]*100+4.2:.1f}" text-anchor="middle" font-size="11" font-family="NNU" fill="{num_fg}">۲</text>')
    svg += "</svg>"
    side = f"{size_pt * 1.687 / 72 * 25.4:.1f}mm"
    return f'<span class="sg" style="font-size:{size_pt}pt;width:{side};height:{side}"><span class="gl" style="color:{glyph}">{letter}</span>{svg}</span>'


def ptile(letter, w=14, h=11, fs=22):
    """Print-safe tile: dark letter on a pale tint with a coloured border (still readable in plain black and white)."""
    return (f'<span class="lt" style="width:{w}mm;height:{h}mm;font-size:{fs}pt;background:{TILE[letter]}22;color:#001F3F;border:.6mm solid {TILE[letter]};'
            f'border-radius:2.2mm;display:inline-flex;align-items:flex-start;justify-content:center;line-height:1.3;padding-top:{max(.6, fs*.03):.1f}mm">{letter}</span>')


def bar2(title, en, sub, mins=None):
    pill = f'<div class="pill">{mins}</div>' if mins else ""
    return (f'<div class="bar"><div class="day">دن<b>۱</b></div><h1><span class="en">{en}</span>{title}<small>{sub}</small></h1>{pill}</div>')


def head_html2(title):
    return head_html(title).replace("</style>", CSS2 + "</style>")


# ---- minutes: every plan page and the 60-minute bar must agree ----
MINUTES = {"warmup": 5, "hook": 5, "i_do": 20, "we_do": 12, "you_do": 8, "exit": 10}
assert sum(MINUTES.values()) == 60
assert 2 + 6 * 3 == MINUTES["i_do"] and 4 * 3 == MINUTES["we_do"] and 3 + 3 + 2 == MINUTES["you_do"] and 6 + 4 == MINUTES["exit"] and 1 + 4 == MINUTES["warmup"] and 1 + 2 + 2 == MINUTES["hook"]
