"""Urdu Beginner Day 1 picture words (book Lesson 1, printed p.1): انار بٹن پری توا ٹرک. Text-free objects, same style as the English set."""
import sys
import kie_gen as K

SUBJ = {
    "anar": "one whole red pomegranate with a small crown on top, and one pomegranate cut in half beside it showing red seeds",
    "button": "one round red shirt button with exactly four holes, slightly tilted",
    "pari": "one friendly fairy girl with two small transparent butterfly wings, a pink dress and a small star wand, standing, facing the viewer",
    "tawa": "one flat round black iron griddle pan with one long straight handle, seen from slightly above",
    "truck": "one colourful decorated Pakistani cargo truck, side view, painted with red, green, yellow and blue patterns, with six wheels",
}
for k, v in SUBJ.items():
    K.PROMPTS[f"u1_{k}"] = f"{K.STYLE} Subject: {v}. {K.NEG}"

if __name__ == "__main__":
    import concurrent.futures as cf
    names = [f"u1_{n}" for n in (sys.argv[1:] or SUBJ)]
    with cf.ThreadPoolExecutor(3) as ex:
        for n, status in ex.map(K.render, names):
            print(n, status, flush=True)
