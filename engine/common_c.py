"""Level 2 Intermediate, English, Day 1 (FINAL planner): E-I-01 Read 3-5 letter words and short phrases fluently
(Teach and model), with support E-I-06 Read words with common blends and digraphs folded in. Builds on E-B-07.
Planner difficulty: blends cl, bl, dr, br; digraphs ch, sh, ph, th; phrases of 2-3 words; 3-5 letter words.
Avoid: plain CVC only; st, tr, wh and long-vowel patterns; unusual spellings.
Word sources: Grade 1 book (Unit 3 blends p.22, Review p.28, Unit 4 digraphs pp.34-35), Grade 2 book Unit 1 (black, much, thin, with),
programme blueprint (chin, ship, shop). Quick Words are the Grade 1 book p.2 words (E-B-07, already read at Beginner)."""
from common import CSS, head_html, foot, OVERFLOW_JS, scene, WORK, IMG, os  # noqa: F401
from common_b import FONT_CSS  # noqa: F401  (Andika: single-storey a)

FOOT_LP = "Intermediate · English · Day 1 of 33 · Lesson Plan"

# one box per sound; ck and the digraphs ch, sh, th share a box (two letters, one sound)
SOUNDS = dict(clap="c l a p", clip="c l i p", black="b l a ck", drum="d r u m", drop="d r o p", brick="b r i ck",
              chin="ch i n", much="m u ch", ship="sh i p", shop="sh o p", thin="th i n", **{"with": "w i th"}, phone="ph o n e", photo="ph o t o",
              block="b l o ck", brush="b r u sh", check="ch e ck")
SAY = dict(clap="k l a p", clip="k l i p", black="b l a k", drum="d r u m", drop="d r o p", brick="b r i k",   # sounds said aloud
           chin="ch i n", much="m u ch", ship="sh i p", shop="sh o p", thin="th i n", **{"with": "w i th"}, phone="f oh n", photo="f oh t oh",
           block="b l o k", brush="b r u sh", check="ch e k")
SOUND_COLOURS = ["#2AA7C7", "#F08A3C", "#4DB857", "#E85C9B", "#8E6BC7"]
PATTERN_COL = dict(cl="#2AA7C7", bl="#F08A3C", dr="#4DB857", br="#E85C9B", ch="#8E6BC7", sh="#2AA7C7", th="#F08A3C", ph="#E85C9B")

# I Do: 4 sets, 20 minutes
SETS = [("Set 1", "Blends cl and bl", 5, [("clap", "cl"), ("clip", "cl"), ("black", "bl")],
         "A blend is two letters that each keep their own sound: c then l. Say both sounds fast. ck at the end says one sound, /k/."),
        ("Set 2", "Blends dr and br", 5, [("drum", "dr"), ("drop", "dr"), ("brick", "br")],
         "Say /d/ then /r/ close together, not 'duh-r'. Same for /b/ then /r/. ck says /k/ again."),
        ("Set 3", "Digraphs ch and sh", 5, [("chin", "ch"), ("much", "ch"), ("ship", "sh"), ("shop", "sh")],
         "A digraph is two letters that make ONE sound. ch says /ch/ and sh says /sh/. Look for the pair at the start or the end of the word."),
        ("Set 4", "Digraphs th and ph", 5, [("thin", "th"), ("with", "th"), ("phone", "ph"), ("photo", "ph")],
         "th is two letters, one sound: put the tip of your tongue between your teeth and blow. ph is two letters, one sound: /f/. In phone and photo the o says its name. In phone the e at the end is silent.")]
TAUGHT = [w for _, _, _, ws, _ in SETS for w, _ in ws]                     # 12
COLD = ["block", "brush", "check"]                                          # We Do: new words built from the same patterns
ALL_WORDS = TAUGHT + COLD                                                   # 15
GROUPS = [("cl", ["clap", "clip"]), ("bl", ["black", "block"]), ("dr", ["drum", "drop"]), ("br", ["brick", "brush"]),
          ("ch", ["chin", "much", "check"]), ("sh", ["ship", "shop"]), ("th", ["thin", "with"]), ("ph", ["phone", "photo"])]
QUICK = ["cat", "hen", "pot", "sun", "top", "bed"]                          # warm-up: Grade 1 book p.2 CVC words (E-B-07)
PHRASES = ["black drum", "brick shop", "clap clap clap"]                    # 2-3 words, taught words only

# We Do: reading order is mixed so children cannot chant the list from memory
WE_DO_ORDER = ["ship", "clap", "drum", "thin", "phone", "black", "chin", "brick", "photo", "shop"]
HOOK = [("cat", "k a t"), ("clap", "k l a p"), ("drum", "d r u m"), ("ship", "sh i p")]

# Exit check Part A: 6 items. Teacher says the word; board shows a, b, c; the child writes the letter of the right word.
EXIT = [("clip", ["clap", "clip", "chin"], "b"), ("drum", ["drum", "drop", "brick"], "a"), ("black", ["brick", "drum", "black"], "c"),
        ("ship", ["shop", "ship", "chin"], "b"), ("thin", ["thin", "with", "chin"], "a"), ("brick", ["black", "drop", "brick"], "c")]
# Part B: 4 or 5 children each read three words; a different group each day
PART_B = [["clap", "drum", "chin"], ["black", "ship", "thin"], ["clip", "brick", "shop"], ["drop", "phone", "with"], ["clap", "photo", "brick"]]
# You Do: sort and copy
SORT_ORDER = ["cl", "bl", "dr", "br", "ch", "sh", "th", "ph"]
SORT_KEY = {"cl": ["clap", "clip"], "bl": ["black"], "dr": ["drum", "drop"], "br": ["brick"], "ch": ["chin", "much"], "sh": ["ship", "shop"], "th": ["thin", "with"], "ph": ["phone", "photo"]}

# ---- checks ----
assert len(TAUGHT) == len(set(TAUGHT)) == 14 and len(set(ALL_WORDS)) == 17
for w in ALL_WORDS:
    assert 3 <= len(w) <= 5, w
    assert "".join(SOUNDS[w].split()) == w, f"sound boxes must spell {w}"
    assert len(SAY[w].split()) == len(SOUNDS[w].split()) or w == "phone"   # silent e has no sound
for w in WE_DO_ORDER + [x for r in PART_B for x in r] + [x for p in PHRASES for x in p.split()]:
    assert w in TAUGHT, w                                    # nothing read that was not taught
for _, ws in GROUPS:
    assert all(w in ALL_WORDS for w in ws)
for w, opts, ans in EXIT:
    assert opts["abc".index(ans)] == w and len(set(opts)) == 3 and all(o in TAUGHT for o in opts)
assert len({a for _, _, a in EXIT}) == 3 and [a for _, _, a in EXIT] != sorted(a for _, _, a in EXIT)
assert sorted(w for ws in SORT_KEY.values() for w in ws) == sorted(TAUGHT) and set(SORT_KEY) == set(SORT_ORDER)
assert all(p.startswith(k) or p.endswith(k) for k, ws in SORT_KEY.items() for p in ws)   # each word has its pattern at an end
assert not any(s in w for w in ALL_WORDS for s in ("st", "tr", "wh"))                # planner: st, tr, wh come later; no ph word today
assert sum(m for _, _, m, _, _ in SETS) == 20


def boxes(word, size=7.2, fs=14, gap=.9):
    out = ""
    for i, s in enumerate(SOUNDS[word].split()):
        c = SOUND_COLOURS[i % len(SOUND_COLOURS)]
        w = size * (1 if len(s) == 1 else 1.55)
        out += (f'<span class="k" style="display:inline-flex;align-items:center;justify-content:center;width:{w}mm;height:{size}mm;border:.45mm solid {c};'
                f'border-radius:1.6mm;background:#fff;color:#001F3F;font-weight:700;font-size:{fs}pt;margin-right:{gap}mm">{s}</span>')
    return out


def slash(word):
    return " ".join(f"/{s}/" for s in SAY[word].split())


def wpic(word, cls="pic"):
    """Picture for a word, or None when the word has no picture (abstract words: black, chin, much, thin, with)."""
    if os.path.exists(os.path.join(IMG, f"c1_{word}.jpg")):
        return f'<img class="{cls}" src="img/c1_{word}.jpg" alt="{word}">'
    return None
