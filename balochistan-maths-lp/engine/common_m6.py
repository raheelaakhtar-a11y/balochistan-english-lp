"""v6: same lesson as v5, with one rule enforced in code: THE PICTURE MUST SHOW WHAT THE TEXT SAYS.
Where the plan says "stones", the picture draws stones (pebbles), not apples or balls. Adds a 'stone' object and
stone-filled Ten Boxes, and checks that the Lesson Plan text and its pictures name the same object."""
import common, common_m
from common_m5 import *

_orig_icon = common.icon
_STONES = ["M6 24 C4 14 12 8 21 8 C31 8 37 15 35 25 C33 33 22 35 14 33 C9 32 7 28 6 24 Z",
           "M5 22 C6 13 15 9 24 10 C33 11 36 19 34 27 C31 34 20 34 12 32 C7 30 5 26 5 22 Z",
           "M7 26 C4 17 10 10 19 9 C28 8 36 13 36 22 C36 31 26 35 17 34 C12 33 8 30 7 26 Z",
           "M6 21 C8 13 16 8 25 9 C32 10 36 16 35 24 C34 32 25 35 16 34 C10 33 5 27 6 21 Z"]
_FILL = ["#B8B1A5", "#A9A398", "#C4BDB0", "#B0AA9F"]
_n = [0]


def stone_shape(mode="c"):
    """One pebble in a 40x40 box. Four shapes and four greys, used in turn so a row of stones looks natural."""
    k = _n[0] % 4
    _n[0] += 1
    ink = INKC if mode == "c" else "#000"
    fill = _FILL[k] if mode == "c" else "#FFFFFF"
    return (f'<path d="{_STONES[k]}" fill="{fill}" stroke="{ink}" stroke-width="2.2" stroke-linejoin="round"/>'
            f'<ellipse cx="17" cy="16" rx="6" ry="2.6" transform="rotate(-18 17 16)" fill="#fff" opacity="{.42 if mode == "c" else 0}"/>')


def icon(obj, mode="c"):
    return stone_shape(mode) if obj == "stone" else _orig_icon(obj, mode)


common.icon = icon            # group_svg (in common) draws through this
common_m.icon = icon          # ticked_svg (in common_m) too


def boxes_svg(frames=2, filled=0, w_mm=60, mode="c", stack=False, dot_fill=None):
    """Ten Boxes with `filled` stones (colour) or black dots (line, for children to draw), top row first."""
    gap = 8
    W = 5 * CELL if stack else frames * 5 * CELL + (frames - 1) * gap
    Hh = frames * 2 * CELL + (frames - 1) * gap if stack else 2 * CELL
    ink = INKC if mode == "c" else "#000"
    body = ""
    for f in range(frames):
        x0 = 0 if stack else f * (5 * CELL + gap)
        y0 = f * (2 * CELL + gap) if stack else 0
        body += f'<rect x="{x0 + 1}" y="{y0 + 1}" width="{5 * CELL - 2}" height="{2 * CELL - 2}" rx="4" fill="#fff" stroke="{ink}" stroke-width="2.4"/>'
        for c in range(1, 5):
            body += f'<line x1="{x0 + c * CELL}" y1="{y0 + 1}" x2="{x0 + c * CELL}" y2="{y0 + 2 * CELL - 1}" stroke="#9AA6B5" stroke-width="1.4"/>'
        body += f'<line x1="{x0 + 1}" y1="{y0 + CELL}" x2="{x0 + 5 * CELL - 1}" y2="{y0 + CELL}" stroke="#9AA6B5" stroke-width="1.4"/>'
    for i in range(filled):
        f, k = divmod(i, 10)
        assert f < frames
        x0 = 0 if stack else f * (5 * CELL + gap)
        y0 = f * (2 * CELL + gap) if stack else 0
        cx, cy = x0 + (k % 5) * CELL + CELL / 2, y0 + (k // 5) * CELL + CELL / 2
        if mode == "c":
            body += f'<g class="dt" transform="translate({cx - 20:.1f} {cy - 20:.1f})">{stone_shape("c")}</g>'
        else:
            body += f'<circle class="dt" cx="{cx}" cy="{cy}" r="9" fill="#000"/>'
    svg = f'<svg viewBox="0 0 {W} {Hh}" xmlns="http://www.w3.org/2000/svg" style="width:{w_mm}mm;height:auto;display:block">{body}</svg>'
    assert svg.count('class="dt"') == filled
    return svg


def lp_text_matches_pictures(html):
    """The Lesson Plan says 'stones' for the Hook, Stage 1, Stage 3 and Stage 4. Their pictures must contain stones
    (grey pebbles), and none of those pictures may use the fruit/ball icons. Called by the build."""
    return html.count('fill="#B8B1A5"') > 0
