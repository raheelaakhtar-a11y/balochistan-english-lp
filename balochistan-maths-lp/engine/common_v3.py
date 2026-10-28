"""v3 = the approved English look (common.py design system: navy bar, gold day badge, mint/sky/cream boxes, Nunito + Inter)
plus the personality the English plans have: a train in the Hook, coloured number tiles, drawn children and a teacher.
Data still comes from common.py."""
from common import *

INKC = "#14304F"
SKIN = {"girl": "#E2A06A", "friend": "#D99560", "boy": "#DA9A62", "teacher": "#E6AE7A"}
TOP = {"girl": "#4DB857", "friend": "#2AA7C7", "boy": "#F08A3C", "teacher": "#4DB857"}


def person(kind="girl", pose="stand", w_mm=26):
    """Flat cartoon child / teacher in the same flat-vector style as the lesson pictures (drawn, not AI)."""
    sk, tp, I = SKIN[kind], TOP[kind], INKC
    arm = lambda d, hx, hy: (f'<path d="{d}" fill="none" stroke="{I}" stroke-width="11.5" stroke-linecap="round"/>'
                             f'<path d="{d}" fill="none" stroke="{tp}" stroke-width="8" stroke-linecap="round"/>'
                             f'<circle cx="{hx}" cy="{hy}" r="5.6" fill="{sk}" stroke="{I}" stroke-width="2"/>')
    legs = (f'<rect x="33" y="108" width="15" height="46" rx="5" fill="#FBF6EA" stroke="{I}" stroke-width="2"/>'
            f'<rect x="52" y="108" width="15" height="46" rx="5" fill="#FBF6EA" stroke="{I}" stroke-width="2"/>'
            f'<ellipse cx="40" cy="158" rx="9" ry="4.6" fill="{I}"/><ellipse cx="60" cy="158" rx="9" ry="4.6" fill="{I}"/>')
    body = f'<path d="M31 55 Q50 48 69 55 L77 114 L23 114 Z" fill="{tp}" stroke="{I}" stroke-width="2.2" stroke-linejoin="round"/>'
    left = arm("M33 60 Q22 82 25 104", 25, 106)
    right = {"stand": arm("M67 60 Q78 82 75 104", 75, 106),
             "raise": arm("M67 60 Q87 62 84 38", 84, 33),
             "point": arm("M67 60 L93 67", 97, 68)}[pose]
    neck = f'<rect x="44.5" y="46" width="11" height="9" fill="{sk}" stroke="{I}" stroke-width="2"/>'
    dup = ""
    if kind in ("girl", "friend"):
        dup = f'<path d="M31 55 Q50 70 69 55 L72 66 Q50 82 28 66 Z" fill="#FFFFFF" stroke="{I}" stroke-width="2" stroke-linejoin="round"/>'
    head = f'<circle cx="50" cy="31" r="17" fill="{sk}" stroke="{I}" stroke-width="2.2"/>'
    face = (f'<circle cx="44" cy="32" r="1.9" fill="{I}"/><circle cx="56" cy="32" r="1.9" fill="{I}"/>'
            f'<path d="M44 39 Q50 44.5 56 39" fill="none" stroke="{I}" stroke-width="1.8" stroke-linecap="round"/>'
            f'<circle cx="40" cy="37" r="2.8" fill="#F28B82" opacity=".45"/><circle cx="60" cy="37" r="2.8" fill="#F28B82" opacity=".45"/>')
    cap = f'<path d="M33 30 C32 10 68 10 67 30 C62 20 40 20 33 30Z" fill="#1E1E24" stroke="{I}" stroke-width="2"/>'
    if kind == "girl":
        hair = f'<path d="M64 36 C74 50 66 70 72 92" fill="none" stroke="{I}" stroke-width="8" stroke-linecap="round"/>' + cap
    elif kind == "friend":
        hair = (f'<path d="M67 22 C80 20 84 34 80 46" fill="none" stroke="#1E1E24" stroke-width="8" stroke-linecap="round"/>'
                f'<circle cx="68" cy="22" r="4" fill="#2AA7C7" stroke="{I}" stroke-width="1.6"/>') + cap
    elif kind == "boy":
        hair = f'<path d="M33 28 C34 9 66 9 67 28 C60 21 42 21 33 28Z" fill="#1E1E24" stroke="{I}" stroke-width="2"/>'
    else:
        hair = (f'<path d="M30 36 C28 6 72 6 70 36 C70 52 62 58 50 58 C38 58 30 52 30 36Z" fill="#F3E3BE" stroke="{I}" stroke-width="2.2" stroke-linejoin="round"/>'
                f'<ellipse cx="50" cy="35" rx="13.5" ry="15" fill="{sk}" stroke="{I}" stroke-width="2"/>')
        dup = f'<path d="M27 58 Q50 76 73 58 L76 74 Q50 92 24 74 Z" fill="#F3E3BE" stroke="{I}" stroke-width="2" stroke-linejoin="round"/>'
    out = legs + body + left + right + neck + dup + (hair if kind == "teacher" else head + hair) + face
    return f'<svg viewBox="0 0 104 164" xmlns="http://www.w3.org/2000/svg" style="width:{w_mm}mm;height:auto;display:block">{out}</svg>'


def train_html(show=(1, 2, 3, 4), last=20):
    """The Counting Train: an engine, coaches 1 to 4 each carrying that many stars, '...', and coach 20."""
    wheels = '<div style="display:flex;gap:5mm;margin-top:.4mm"><i style="width:3.2mm;height:3.2mm;border-radius:50%;background:#001F3F;display:block"></i><i style="width:3.2mm;height:3.2mm;border-radius:50%;background:#001F3F;display:block"></i></div>'
    coach = lambda n, pas: (f'<div style="display:flex;flex-direction:column;align-items:center;gap:.6mm"><div style="min-height:7mm;display:flex;align-items:flex-end">{pas}</div>'
                            f'<div class="lt k" style="width:19mm;height:11mm;font-size:15pt;background:{tile_colour(n)};border-radius:1.8mm">{n}</div>{wheels}</div>')
    engine = ('<div style="display:flex;flex-direction:column;align-items:center"><div style="min-height:7mm"></div>'
              '<div style="background:#C0392B;color:#fff;border-radius:2mm 5mm 1.5mm 1.5mm;width:19mm;height:11mm;display:flex;align-items:center;justify-content:center;font-size:7pt;font-weight:800">GO!</div>' + wheels + '</div>')
    cars = "".join(coach(n, group_svg(n, "star", "row", cell_mm=4.4, per_row=n)) for n in show)
    dots = '<div style="align-self:center;font-weight:900;font-size:14pt;color:var(--navy);padding-bottom:3mm">...</div>'
    return (f'<div style="display:flex;gap:2mm;align-items:flex-end;padding:2mm 3mm;background:#fff;border-radius:3mm;border:.3mm solid #C7D4EC">{engine}{cars}{dots}'
            f'{coach(last, "")}</div>')
