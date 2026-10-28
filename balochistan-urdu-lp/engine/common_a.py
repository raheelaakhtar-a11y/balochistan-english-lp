"""Level 3 Advanced, URDU, Day 1 (28 Oct 2026 planner): Teach and model.
SLO taught: U-A-08 Use correct singular/plural and gender agreement within sentences (common nouns and verbs; no rare patterns).
Support folded in: U-A-10 Identify nouns, verbs and adjectives in a sentence. Builds on U-I-11 (masculine/feminine forms).
One sentence frame: ADJECTIVE + NOUN + VERB + ہے/ہیں. Four forms: one boy-word, many boy-words, one girl-word, many girl-words.
Every sentence is GENERATED from the word tables below, so the Lesson Plan, Prep Pack and Worksheet cannot disagree."""
from common_u2 import *  # noqa: F401,F403
import os

FORMS = ["ms", "mp", "fs", "fp"]              # masculine singular / plural, feminine singular / plural
IDX = {"ms": 0, "mp": 1, "fs": 2, "fp": 2}     # index into the adjective / verb triples (feminine plural keeps the feminine singular form)
HELP = {"ms": "ہے", "mp": "ہیں", "fs": "ہے", "fp": "ہیں"}
FCOL = {"ms": "#2AA7C7", "mp": "#F08A3C", "fs": "#E85C9B", "fp": "#7B61C9"}
FLABEL = {"ms": "ایک لڑکا", "mp": "کئی لڑکے", "fs": "ایک لڑکی", "fp": "کئی لڑکیاں"}
FTERM = {"ms": "ایک · لڑکا", "mp": "کئی · لڑکا", "fs": "ایک · لڑکی", "fp": "کئی · لڑکی"}
FRULE = {"ms": "نام، کیسا اور کام والے لفظ سب «ا» پر ختم ہوتے ہیں۔ آخر میں «ہے»۔",
         "mp": "لڑکا ← لڑکے۔ نام، کیسا اور کام والے لفظ سب «ے» پر ختم ہوتے ہیں۔ آخر میں «ہیں»۔",
         "fs": "نام، کیسا اور کام والے لفظ سب «ی» پر ختم ہوتے ہیں۔ آخر میں «ہے»۔",
         "fp": "لڑکی ← لڑکیاں۔ کیسا اور کام والے لفظ «ی» پر ہی رہتے ہیں۔ آخر میں «ہیں»۔"}

ADJ = {"chota": ("چھوٹا", "چھوٹے", "چھوٹی"), "bara": ("بڑا", "بڑے", "بڑی"), "acha": ("اچھا", "اچھے", "اچھی")}
VERB = {"parhna": ("پڑھتا", "پڑھتے", "پڑھتی"), "daurna": ("دوڑتا", "دوڑتے", "دوڑتی"),
        "khelna": ("کھیلتا", "کھیلتے", "کھیلتی"), "baithna": ("بیٹھتا", "بیٹھتے", "بیٹھتی")}
NOUN = {"larka": ("لڑکا", "لڑکے", "m"), "kutta": ("کتا", "کتے", "m"), "bacha": ("بچہ", "بچے", "m"), "ghora": ("گھوڑا", "گھوڑے", "m"),
        "larki": ("لڑکی", "لڑکیاں", "f"), "billi": ("بلی", "بلیاں", "f"), "chidiya": ("چڑیا", "چڑیاں", "f"), "murghi": ("مرغی", "مرغیاں", "f")}
ROLE = {"a": "کیسا", "n": "نام", "v": "کام", "h": ""}          # short labels shown under the words (formal: صفت / اسم / فعل)
ROLE_FORMAL = {"a": "صفت", "n": "اسم", "v": "فعل"}


def words(adj, noun, verb, form):
    """[adjective, noun, verb, helper] for one form. Gender of the noun must match the form."""
    assert NOUN[noun][2] == form[0], (noun, form)
    return [ADJ[adj][IDX[form]], NOUN[noun][0 if form[1] == "s" else 1],
            VERB[verb][IDX[form]], HELP[form]]


def sent(adj, noun, verb, form):
    return " ".join(words(adj, noun, verb, form)) + "۔"


def chips(ws, size=13, labels=True):
    roles = ["a", "n", "v", "h"]
    out = ""
    for w, r in zip(ws, roles):
        lab = f"<i>{ROLE[r]}</i>" if (labels and ROLE[r]) else ""
        out += f'<span class="cw r{r}" style="font-size:{size}pt">{w}{lab}</span>'
    return out


# two picture sets: A = children reading, B = animals running. noun keys per gender; picture file per form
SETS = {"A": dict(adj="chota", noun=dict(m="larka", f="larki"), verb="parhna",
                  pic=dict(ms="boy_reads", mp="boys_read", fs="girl_reads", fp="girls_read")),
        "B": dict(adj="chota", noun=dict(m="kutta", f="billi"), verb="daurna",
                  pic=dict(ms="dog_runs", mp="dogs_run", fs="cat_runs", fp="cats_run"))}


def set_words(s, form):
    d = SETS[s]
    return words(d["adj"], d["noun"][form[0]], d["verb"], form)


def set_sent(s, form):
    return " ".join(set_words(s, form)) + "۔"


def apic(s, form, cls="pic"):
    stem = "a1_" + SETS[s]["pic"][form]
    if os.path.exists(os.path.join(IMG, stem + ".jpg")):
        return f'<img class="{cls}" src="img/{stem}.jpg" alt="{set_sent(s, form)}">'
    return f'<div class="{cls} pending"><span>{set_sent(s, form)}</span></div>'


assert set_sent("A", "ms") == "چھوٹا لڑکا پڑھتا ہے۔" and set_sent("A", "mp") == "چھوٹے لڑکے پڑھتے ہیں۔"
assert set_sent("A", "fs") == "چھوٹی لڑکی پڑھتی ہے۔" and set_sent("A", "fp") == "چھوٹی لڑکیاں پڑھتی ہیں۔"
assert set_sent("B", "ms") == "چھوٹا کتا دوڑتا ہے۔" and set_sent("B", "mp") == "چھوٹے کتے دوڑتے ہیں۔"
assert set_sent("B", "fs") == "چھوٹی بلی دوڑتی ہے۔" and set_sent("B", "fp") == "چھوٹی بلیاں دوڑتی ہیں۔"
assert len({set_sent(s, f) for s in SETS for f in FORMS}) == 8

# ---- Warm-up (U-A-10): naming / how / doing words, with an action each. No two of the same kind in a row. ----
GESTURE = {"n": "میز تھپتھپائیں", "a": "ہاتھ کھولیں", "v": "کھڑے ہوں"}
WARM = [("لڑکی", "n"), ("دوڑتا", "v"), ("چھوٹا", "a"), ("کتا", "n"), ("کھیلتی", "v"), ("بڑی", "a"), ("بلی", "n"), ("پڑھتے", "v")]
assert all(a[1] != b[1] for a, b in zip(WARM, WARM[1:]))
_ALLW = {w: "a" for t in ADJ.values() for w in t} | {w: "v" for t in VERB.values() for w in t} | {w: "n" for t in NOUN.values() for w in t[:2]}
assert all(_ALLW[w] == r for w, r in WARM), "warm-up word has the wrong kind"

# ---- Hook: say it again, one -> many (and back) ----
HOOK = [("chota", "billi", "daurna", "fs", "fp"), ("bara", "ghora", "baithna", "mp", "ms"), ("acha", "chidiya", "baithna", "fp", "fs")]
for a, n, v, f0, f1 in HOOK:
    assert f0[0] == f1[0] and f0 != f1


def hook_pair(i):
    a, n, v, f0, f1 = HOOK[i]
    return sent(a, n, v, f0), sent(a, n, v, f1), f1


# ---- We do 1: board frame چھوٹا لڑکا پڑھتا ہے; teacher swaps the NAME card, class fixes the rest ----
WE1_FRAME = ("chota", "larka", "parhna")
WE1_CALLS = ["fp", "mp", "fs", "ms", "fp", "mp"]          # form of the new noun card each call; no two neighbours alike, first differs from the frame (ms)
assert all(a != b for a, b in zip(["ms"] + WE1_CALLS, WE1_CALLS))


def we1_sentence(form):
    a, n, v = WE1_FRAME
    return sent(a, "larka" if form[0] == "m" else "larki", v, form)


def we1_noun(form):
    return NOUN["larka" if form[0] == "m" else "larki"][0 if form[1] == "s" else 1]


# ---- We do 3: fix the sentence. each wrong sentence breaks exactly ONE word ----
WE3 = [("چھوٹے لڑکے پڑھتی ہیں۔", sent("chota", "larka", "parhna", "mp")),
       ("بڑی بلیاں دوڑتی ہے۔", sent("bara", "billi", "daurna", "fs")),
       ("اچھی بچے کھیلتے ہیں۔", sent("acha", "bacha", "khelna", "mp")),
       ("چھوٹی لڑکیاں پڑھتی ہے۔", sent("chota", "larki", "parhna", "fp"))]


def _onediff(a, b):
    x, y = a.rstrip("۔").split(), b.rstrip("۔").split()
    return len(x) == len(y) and sum(p != q for p, q in zip(x, y)) == 1


assert all(_onediff(w, r) for w, r in WE3)

# ---- You do, worksheet page 1 ----
T1_ITEMS = [("A", "fp"), ("B", "ms"), ("A", "fs"), ("B", "mp"), ("A", "mp"), ("B", "fs")]      # sentences (right column), in this order
T1_PICS = [("B", "mp"), ("A", "fs"), ("B", "fs"), ("A", "fp"), ("B", "ms"), ("A", "mp")]     # pictures (left column), in this order
assert sorted(T1_ITEMS) == sorted(T1_PICS) and all(a != b for a, b in zip(T1_ITEMS, T1_PICS)), "no straight-across answers"
# T2: circle the word that fits. (sentence with a blank, three options, answer index)
T2 = [dict(before="بڑے", blank="noun", after="بیٹھتے ہیں۔", options=["گھوڑا", "گھوڑے", "گھوڑیاں"], answer="گھوڑے"),
      dict(before="اچھی لڑکیاں", blank="verb", after="ہیں۔", options=["پڑھتی", "پڑھتا", "پڑھتے"], answer="پڑھتی"),
      dict(before="", blank="adj", after="بلی دوڑتی ہے۔", options=["چھوٹا", "چھوٹے", "چھوٹی"], answer="چھوٹی"),
      dict(before="اچھے بچے", blank="verb", after="ہیں۔", options=["کھیلتے", "کھیلتا", "کھیلتی"], answer="کھیلتے")]
assert all(t["answer"] in t["options"] and len(set(t["options"])) == 3 for t in T2)
assert len({t["options"].index(t["answer"]) for t in T2}) > 1
# T3: mark the kinds of word (U-A-10): circle the NAME, underline the HOW word, box the DOING word
T3 = [("acha", "billi", "daurna", "fs"), ("bara", "kutta", "khelna", "mp")]
T3_MARK = ("دائرہ", "لکیر", "ڈبہ")

# ---- Exit check, Part A: circle the correct sentence. Every wrong sentence breaks exactly one word. ----
EXIT = [dict(args=("acha", "larki", "khelna", "fs"), options=["اچھا لڑکی کھیلتی ہے۔", None, "اچھی لڑکی کھیلتا ہے۔"], pos=1),
        dict(args=("bara", "kutta", "daurna", "mp"), options=[None, "بڑے کتے دوڑتی ہیں۔", "بڑا کتے دوڑتے ہیں۔"], pos=0),
        dict(args=("chota", "billi", "baithna", "fp"), options=["چھوٹی بلیاں بیٹھتی ہے۔", "چھوٹے بلیاں بیٹھتی ہیں۔", None], pos=2),
        dict(args=("acha", "bacha", "parhna", "ms"), options=["اچھے بچہ پڑھتا ہے۔", None, "اچھا بچہ پڑھتے ہے۔"], pos=1),
        dict(args=("bara", "murghi", "daurna", "fp"), options=[None, "بڑی مرغیاں دوڑتی ہے۔", "بڑے مرغیاں دوڑتی ہیں۔"], pos=0)]
for it in EXIT:
    right = sent(*it["args"])
    it["options"][it["pos"]] = right
    it["answer"] = right
    assert all(_onediff(o, right) for i, o in enumerate(it["options"]) if i != it["pos"]), it
    assert len(set(it["options"])) == 3
assert len({it["pos"] for it in EXIT}) > 1, "answer is always in the same place"
EXIT_WRONG_KIND = ["کیسا", "کیسا", "کام", "کیسا", "نام"]     # which slot each worksheet-style distractor breaks (documentation only)

# Part B: teacher listens to 4-5 children say the sentence the other way (one -> many, many -> one)
PART_B = [[("acha", "bacha", "khelna", "ms", "mp"), ("bara", "billi", "baithna", "fs", "fp"), ("chota", "ghora", "daurna", "mp", "ms")],
          [("acha", "larki", "parhna", "fs", "fp"), ("chota", "kutta", "khelna", "mp", "ms"), ("bara", "chidiya", "daurna", "fp", "fs")],
          [("bara", "larka", "baithna", "ms", "mp"), ("acha", "murghi", "daurna", "fp", "fs"), ("chota", "bacha", "parhna", "mp", "ms")]]
for card in PART_B:
    for a, n, v, f0, f1 in card:
        assert f0[0] == f1[0] and f0 != f1

FOOT_LP = "لیول ۳ ایڈوانس · اردو · دن ۱ از ۳۳ · لیسن پلان"
FOOT_PREP = "لیول ۳ ایڈوانس · اردو · دن ۱ از ۳۳ · تیاری کا پیکٹ"
FOOT_WS = "لیول ۳ ایڈوانس · اردو · دن ۱ · طالب علم کی ورک شیٹ"

CSS_A = r"""
.cw{display:inline-block;text-align:center;border:.5mm solid var(--rc,#9AA6B5);background:var(--rb,#fff);border-radius:2mm;padding:0 1.8mm;margin:.4mm .4mm;font-weight:700;color:#001F3F;line-height:1.55}
.cw i{display:block;font-style:normal;font-size:7.6pt;font-weight:600;line-height:1.25;color:#1D2025}
.cw.rn{--rc:#2AA7C7;--rb:#2AA7C722;border-style:solid}
.cw.ra{--rc:#F08A3C;--rb:#F08A3C22;border-style:dashed}
.cw.rv{--rc:#4DB857;--rb:#4DB85722;border-style:dotted;border-width:.7mm}
.cw.rh{--rc:#9AA6B5;--rb:#fff}
"""


def head_a(title):
    return head_html2(title).replace("</style>", CSS_A + "</style>")


def ftile(form, w=22, h=18, fs=15):
    """Form tile: the noun for that form, pale tint, coloured border, dark text (prints in black and white)."""
    noun = NOUN["larka" if form[0] == "m" else "larki"][0 if form[1] == "s" else 1]
    return (f'<span class="lt" style="width:{w}mm;height:{h}mm;font-size:{fs}pt;background:{FCOL[form]}22;color:#001F3F;border:.6mm solid {FCOL[form]};'
            f'border-radius:2.2mm;display:inline-flex;align-items:center;justify-content:center;line-height:1.5;font-weight:700">{noun}</span>')
