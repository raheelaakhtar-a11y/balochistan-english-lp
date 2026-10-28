"""Level 2 Intermediate, URDU, Day 1 (FINAL planner, 27 Oct 2026): Teach and model.
SLO taught: U-I-01 Read 3-5 letter words and short phrases fluently (common joins, vowel marks zabar zer pesh jazm).
Support folded in: U-I-06 Read words that carry vowel marks (zabar, zer, pesh). Builds on U-B-07 (read 2-3 letter words).
Avoid (planner): shadda, tanween, rare marks, rare letters, words over five letters.
One data block feeds the Lesson Plan, Prep Pack and Worksheet so call lists and answers cannot disagree."""
from common_u2 import *  # noqa: F401,F403
import os

MARKS = ["zabar", "zer", "pesh", "jazm"]
MNAME = {"zabar": "زبر", "zer": "زیر", "pesh": "پیش", "jazm": "جزم"}
MSYM = {"zabar": "َ", "zer": "ِ", "pesh": "ُ", "jazm": "ْ"}
MSOUND = {"zabar": "اَ", "zer": "اِ", "pesh": "اُ", "jazm": "ْ"}
MCOL = {"zabar": "#2AA7C7", "zer": "#F08A3C", "pesh": "#4DB857", "jazm": "#7B61C9"}
MWHERE = {"zabar": "حرف کے اوپر ایک چھوٹی ترچھی لکیر",
          "zer": "حرف کے نیچے ایک چھوٹی ترچھی لکیر",
          "pesh": "حرف کے اوپر ایک چھوٹا سا گول نشان، جیسے چھوٹا و",
          "jazm": "حرف کے اوپر ایک چھوٹا سا دائرہ یا گول نشان"}
MSHORT = {"zabar": "اوپر لکیر", "zer": "نیچے لکیر", "pesh": "اوپر گول نشان", "jazm": "اوپر چھوٹا دائرہ"}
MHOW = {"zabar": "منہ کھول کر چھوٹی سی آواز: اَ",
        "zer": "ہونٹ پھیلا کر چھوٹی سی آواز: اِ",
        "pesh": "ہونٹ گول کر کے چھوٹی سی آواز: اُ",
        "jazm": "اس حرف پر کوئی آواز نہیں لگتی۔ اس سے پہلے والی آواز کے ساتھ ملا کر بولیں"}
BASE = "ب"
MEX = {"zabar": ["بَ", "دَ", "کَ"], "zer": ["بِ", "دِ", "کِ"], "pesh": ["بُ", "دُ", "کُ"], "jazm": ["بَرْ", "دِرْ", "کُرْ"]}

# word key -> (word with marks, syllables shown sound by sound, picture file stem, mark block it teaches)
W = {
    "qalam": ("قَلَم", ["قَ", "لَ", "م"], "i1_qalam", "zabar"),
    "batakh": ("بَطَخ", ["بَ", "طَ", "خ"], "i1_batakh", "zabar"),
    "anar": ("اَنار", ["اَ", "نا", "ر"], "u1_anar", "zabar"),
    "kitab": ("کِتاب", ["کِ", "تا", "ب"], "i1_kitab", "zer"),
    "glass": ("گِلاس", ["گِ", "لا", "س"], "i1_glass", "zer"),
    "sitara": ("سِتارہ", ["سِ", "تا", "رہ"], "i1_sitara", "zer"),
    "gulab": ("گُلاب", ["گُ", "لا", "ب"], "i1_gulab", "pesh"),
    "dukan": ("دُکان", ["دُ", "کا", "ن"], "i1_dukan", "pesh"),
    "bulbul": ("بُلْبُل", ["بُلْ", "بُل"], "i1_bulbul", "pesh"),
    "kursi": ("کُرْسی", ["کُرْ", "سی"], "i1_kursi", "jazm"),
    "mirch": ("مِرْچ", ["مِرْ", "چ"], "i1_mirch", "jazm"),
    "khargosh": ("خَرْگوش", ["خَرْ", "گوش"], "i1_khargosh", "jazm"),
}
BLOCK_WORDS = {m: [k for k, v in W.items() if v[3] == m] for m in MARKS}
assert all(len(v) == 3 for v in BLOCK_WORDS.values()) and len(W) == 12
# planner difficulty: 3-5 letters. Count base letters (strip marks).
_MARKCH = set(MSYM.values())
for k, (w, parts, pf, m) in W.items():
    n = len([c for c in w if c not in _MARKCH])
    assert 3 <= n <= 5, (k, n)
    assert "".join(parts) == w, (k, "".join(parts), w)
    assert "ّ" not in w and "ً" not in w and "ٌ" not in w and "ٍ" not in w, "no shadda / tanween"

# We do: chorus order = no two neighbouring words teach the same mark
CHORUS = ["glass", "qalam", "bulbul", "mirch", "anar", "dukan", "kitab", "khargosh", "gulab", "sitara", "batakh", "kursi"]
_MAIN = {"glass": "zer", "qalam": "zabar", "bulbul": "pesh", "mirch": "zer", "anar": "zabar", "dukan": "pesh", "kitab": "zer",
         "khargosh": "zabar", "gulab": "pesh", "sitara": "zer", "batakh": "zabar", "kursi": "pesh"}
assert sorted(CHORUS) == sorted(W)
assert all(_MAIN[a] != _MAIN[b] for a, b in zip(CHORUS, CHORUS[1:])), "same mark twice in a row"
assert all(_MAIN[k] == W[k][3] or W[k][3] == "jazm" for k in W)
PAIR_READ = ["kursi", "gulab", "qalam", "kitab", "bulbul", "sitara"]       # partner A reads, partner B listens; then swap
assert sorted(set(PAIR_READ)) == sorted(PAIR_READ)
PHRASES = ["یہ کِتاب ہے۔", "گُلاب سُرْخ ہے۔", "خَرْگوش کُرْسی پر ہے۔"]

# You do, worksheet page 1
T1 = ["gulab", "qalam", "mirch", "kitab", "dukan", "batakh"]            # words, left to right of the answer key; matched to pictures in T1_PICS order
T1_PICS = ["kitab", "batakh", "gulab", "dukan", "mirch", "qalam"]       # picture column (right) in this order
assert sorted(T1) == sorted(T1_PICS) and all(a != b for a, b in zip(T1, T1_PICS)), "no straight-across answers"
T2 = PHRASES
# T3: circle the sound of the first letter (letter + mark): options are the same letter with zabar / zer / pesh
T3 = [("qalam", "ق", "zabar"), ("glass", "گ", "zer"), ("gulab", "گ", "pesh"), ("anar", "ا", "zabar"), ("kitab", "ک", "zer"), ("dukan", "د", "pesh")]
T3_OPTS = [["zer", "pesh", "zabar"], ["zabar", "zer", "pesh"], ["pesh", "zabar", "zer"], ["zer", "zabar", "pesh"], ["pesh", "zer", "zabar"], ["zabar", "pesh", "zer"]]
for (k, l, m), opts in zip(T3, T3_OPTS):
    assert m in opts and sorted(opts) == sorted(MARKS[:3]) and W[k][1][0].startswith(l)

# Exit check, Part A: read the word (or phrase) and circle its picture
EXIT = [dict(text=W["mirch"][0], answer="mirch", options=["qalam", "glass", "mirch"], kind="word"),
        dict(text=W["bulbul"][0], answer="bulbul", options=["kursi", "dukan", "bulbul"], kind="word"),
        dict(text=W["qalam"][0], answer="qalam", options=["qalam", "batakh", "kitab"], kind="word"),
        dict(text=W["sitara"][0], answer="sitara", options=["glass", "sitara", "khargosh"], kind="word"),
        dict(text=PHRASES[1], answer="gulab", options=["mirch", "gulab", "sitara"], kind="phrase")]
for it in EXIT:
    assert it["answer"] in it["options"] and len(set(it["options"])) == 3
assert len({it["options"].index(it["answer"]) for it in EXIT}) > 1, "answer is always in the same place"
EXIT_WORDS = [it["text"] for it in EXIT]
# Part B: teacher listens to 4-5 children read a card of three words
PART_B = [["gulab", "kitab", "batakh"], ["dukan", "glass", "anar"], ["kursi", "khargosh", "mirch"]]
assert not set(sum(PART_B, [])) - set(W)

FOOT_LP = "لیول ۲ درمیانہ · اردو · دن ۱ از ۳۳ · لیسن پلان"
FOOT_PREP = "لیول ۲ درمیانہ · اردو · دن ۱ از ۳۳ · تیاری کا پیکٹ"
FOOT_WS = "لیول ۲ درمیانہ · اردو · دن ۱ · طالب علم کی ورک شیٹ"


def wpic(key, cls="pic"):
    stem = W[key][2]
    word = W[key][0]
    if os.path.exists(os.path.join(IMG, stem + ".jpg")):
        return f'<img class="{cls}" src="img/{stem}.jpg" alt="{word}">'
    return f'<div class="{cls} pending"><span>{word}</span></div>'


def wd(key):
    return W[key][0]


def mtile(mark, w=22, h=21, fs=30, letter=BASE):
    """Letter with a mark, pale tint + coloured border, dark letter (prints in black and white)."""
    return (f'<span class="lt" style="width:{w}mm;height:{h}mm;font-size:{fs}pt;background:{MCOL[mark]}22;color:#001F3F;border:.6mm solid {MCOL[mark]};'
            f'border-radius:2.2mm;display:inline-flex;align-items:flex-start;justify-content:center;line-height:1.3;padding-top:{max(.6, fs*.03):.1f}mm">'
            f'{letter}{MSYM[mark]}</span>')


def parts_html(key, sep=" · "):
    return sep.join(f'<b>{p}</b>' for p in W[key][1])


def head_i(title):
    return head_html2(title)


def wchips(keys):
    return "".join(f'<span class="wd">{wd(k)}</span>' for k in keys)
