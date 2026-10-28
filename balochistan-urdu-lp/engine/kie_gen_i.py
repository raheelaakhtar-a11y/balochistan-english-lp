"""Urdu Intermediate Day 1 picture words (text-free objects, same style as the Beginner set)."""
import sys
import kie_gen as K

SUBJ = {
    "qalam": "one blue-and-silver pen lying diagonally with its cap beside it",
    "batakh": "one yellow duck with an orange beak and orange feet, standing, side view",
    "kitab": "one closed red hardcover book with a plain blank cover, standing slightly angled",
    "glass": "one clear drinking glass of water with a little water in it",
    "sitara": "one bright yellow five-pointed star with a few tiny sparkles around it",
    "gulab": "one red rose flower with a green stem and two green leaves",
    "dukan": "one small colourful village shop with an open front, a striped awning and a few jars on a shelf, no sign text",
    "bulbul": "one small brown bird with a black crest on its head, sitting on a branch, side view",
    "kursi": "one simple wooden chair with four legs and a straight back, side view",
    "mirch": "one shiny red chilli pepper with a green stem",
    "khargosh": "one white rabbit with long upright ears and a pink nose, sitting",
}
for k, v in SUBJ.items():
    K.PROMPTS[f"i1_{k}"] = f"{K.STYLE} Subject: {v}. {K.NEG}"

if __name__ == "__main__":
    import concurrent.futures as cf
    names = [f"i1_{n}" for n in (sys.argv[1:] or SUBJ)]
    with cf.ThreadPoolExecutor(3) as ex:
        for n, status in ex.map(K.render, names):
            print(n, status, flush=True)
