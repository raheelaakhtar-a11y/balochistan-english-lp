"""Advanced Day 1 pictures: one / many boys and girls reading, one / many dogs and cats running (text-free, same style as the other sets)."""
import sys
import kie_gen as K

SUBJ = {
    "boy_reads": f"{K.BOY}, sitting and reading one plain open book, full body, only one child",
    "boys_read": f"exactly three different Pakistani boys about seven years old with short black hair and blue shalwar kameez, sitting side by side in a row, each reading his own plain open book, full bodies",
    "girl_reads": f"{K.GIRL}, sitting and reading one plain open book, full body, only one child",
    "girls_read": "exactly three different Pakistani girls about seven years old with long black plaits, purple kameez and pink dupattas, sitting side by side in a row, each reading her own plain open book, full bodies",
    "dog_runs": "one friendly brown dog running happily, side view, only one dog",
    "dogs_run": "exactly three friendly brown dogs running happily one behind the other, side view",
    "cat_runs": "one friendly grey tabby cat running, side view, only one cat",
    "cats_run": "exactly three friendly grey tabby cats running one behind the other, side view",
}
for k, v in SUBJ.items():
    K.PROMPTS[f"a1_{k}"] = f"{K.STYLE.replace('one single subject centred and filling about seventy percent of the frame', 'the subject centred and filling about seventy percent of the frame')} Subject: {v}. {K.NEG}"

if __name__ == "__main__":
    import concurrent.futures as cf
    names = [f"a1_{n}" for n in (sys.argv[1:] or SUBJ)]
    with cf.ThreadPoolExecutor(3) as ex:
        for n, status in ex.map(K.render, names):
            print(n, status, flush=True)
