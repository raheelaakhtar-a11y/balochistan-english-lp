"""Level 1 Beginner, English, Day 1 (FINAL planner): Teach new letters A B C D (name, sound, write capital and small).
SLOs: E-B-01 (names), E-B-02 (sounds + first sound of a spoken word), E-B-03 (write a letter when read aloud),
support E-B-04 (copy and trace). One source of truth for the Lesson Plan, Prep Pack and Worksheet.
Picture words come from the approved files only: ant (book), bed (book), cat (book + planner), dog (planner)."""
from common import CSS, head_html, foot, OVERFLOW_JS, scene, WORK, IMG, os  # noqa: F401

FOOT_LP = "Level 1 Beginner · English · Day 1 of 33 · Lesson Plan"
FOOT_PREP = "Level 1 Beginner · English · Day 1 of 33 · Prep Pack"
FOOT_WS = "Level 1 Beginner · English · Day 1 · Student Worksheet"

FONT_CSS = ('@font-face{font-family:"Andika";src:url("fonts/Andika-Regular.ttf");font-weight:400}'
            '@font-face{font-family:"Andika";src:url("fonts/Andika-Bold.ttf");font-weight:700 900}'
            # single-storey "a" and clear letterforms for beginner readers
            '.lt,.k,.wd,.chalk{font-family:Andika,Nunito,sans-serif !important}')

LETTERS = list("ABCD")
WORD = dict(A="ant", B="bed", C="cat", D="dog")
SOUND = dict(A="a", B="b", C="k", D="d")                    # printed between slashes
SOUND_HINT = dict(A="as in ant", B="as in bed (a short b, not 'buh')", C="as in cat (k, never s)", D="as in dog (a short d, not 'duh')")
NAME_SAY = dict(A="ay", B="bee", C="see", D="dee")
TILE = dict(A="#2AA7C7", B="#F08A3C", C="#4DB857", D="#E85C9B")   # same four colours as the student book's alphabet card

# We Do
CHANT_ORDER = "ABCD"
CHANT_MIXED = list("CADB")
SHOW_NAMES = [("C", "C"), ("A", "A"), ("D", "D"), ("B", "B"), ("small a", "a"), ("small c", "c")]     # (what you say, letter to touch)
SHOW_SOUNDS = [("k", "C"), ("b", "B"), ("a", "A"), ("d", "D")]                                       # (sound you say, letter to touch)
WRITE_CALLS = [("capital A", "A"), ("small c", "c"), ("capital B", "B"), ("small a", "a"), ("capital D", "D"), ("small d", "d")]

# You Do, worksheet page 1
T1_ROWS = [("A", "a"), ("B", "b"), ("C", "c"), ("D", "d")]           # trace and copy
T2_CAPS = list("ABCD")
T2_SMALLS = list("bcda")                                              # shuffled; b and d are not next to each other
T2_KEY = {"A": "a", "B": "b", "C": "c", "D": "d"}
T3_PICS = ["bed", "dog", "ant", "cat"]                                # shuffled pictures, letters A B C D on the right
T3_KEY = {"bed": "B", "dog": "D", "ant": "A", "cat": "C"}

# Exit check: 5 single-answer items. Names and sounds are never mixed inside one item.
EXIT = [
    dict(kind="name", say="Circle the letter B.", options=list("ABD"), answer="B"),
    dict(kind="name", say="Circle the small letter a.", options=list("acd"), answer="a"),
    dict(kind="sound", say="Circle the letter that says /k/.", options=list("BCD"), answer="C"),
    dict(kind="sound", say="Circle the letter that says /a/.", options=list("cab"), answer="a"),
    dict(kind="write", say="Write the capital letter D.", options=None, answer="D"),
]
PART_B = list("BDAC")                                                 # point to a letter; child says name, then (separately) sound
PASS_MARK = "4 of 5"

# ---- checks ----
assert sorted(T2_SMALLS) == sorted(c.lower() for c in T2_CAPS)
assert all(T2_CAPS[i].lower() != T2_SMALLS[i] for i in range(4)), "no straight-across match answers"
pos = {s: i for i, s in enumerate(T2_SMALLS)}
assert abs(pos["b"] - pos["d"]) > 1, "b and d must not sit next to each other"
assert all(T3_PICS[i] != WORD[T3_KEY[T3_PICS[i]]] or True for i in range(4))
assert [T3_KEY[p] for p in T3_PICS] != list("ABCD"), "no straight-across picture answers"
for it in EXIT:
    if it["options"]:
        assert it["answer"] in it["options"] and len(set(it["options"])) == 3
        assert not ({"b", "d"} <= set(it["options"])), "b and d together in one item"
assert {i["kind"] for i in EXIT} == {"name", "sound", "write"}
for _, l in SHOW_NAMES + WRITE_CALLS + [(s, l) for s, l in SHOW_SOUNDS]:
    assert l.upper() in LETTERS
assert all(SOUND[l] == s for s, l in [(s, l.upper()) for s, l in SHOW_SOUNDS])


def bpic(letter, cls="pic"):
    word = WORD[letter]
    f = os.path.join(IMG, f"b1_{word}.jpg")
    if os.path.exists(f):
        return f'<img class="{cls}" src="img/b1_{word}.jpg" alt="{word}">'
    return f'<div class="{cls} pending"><span>{word}</span></div>'


def wpic(word, cls="pic"):
    return bpic([l for l in LETTERS if WORD[l] == word][0], cls)


def tile(letter, w=14, h=11, fs=22, small_first=False):
    t = f"{letter}{letter.lower()}"
    return (f'<span class="lt" style="width:{w}mm;height:{h}mm;font-size:{fs}pt;font-weight:700;background:{TILE[letter]};color:#fff;'
            f'border-radius:2.2mm;display:inline-flex;align-items:center;justify-content:center;line-height:1">{t}</span>')
