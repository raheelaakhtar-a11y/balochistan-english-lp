"""Urdu Beginner Day 1 (28 Oct planner): new picture word ث ثمر (fruit basket, book p.1 chart #7)."""
import sys
import kie_gen as K
SUBJ = {"samar": "one wicker basket full of mixed fresh fruit: a pineapple, bananas, a red apple, an orange and a bunch of grapes"}
for k, v in SUBJ.items():
    K.PROMPTS[f"u2_{k}"] = f"{K.STYLE} Subject: {v}. {K.NEG}"
if __name__ == "__main__":
    for n in (sys.argv[1:] or [f"u2_{k}" for k in SUBJ]):
        print(*K.render(n), flush=True)
