"""Scene pictures for Level 1 Maths Day 1 via kie.ai (nano-banana-pro). Key is read from the repo .env, never printed.
Only text-free scene pictures are made here. Every counted group in the lesson is drawn as SVG by work\\common.py,
so a count can never be wrong. Scenes show no more than 4 countable objects."""
import json, os, sys, time, urllib.request, concurrent.futures as cf

REPO = os.environ.get("AGENT_SKILLS_REPO", r"C:\Users\WALEED SALES\Desktop\Agent Skills\agent-skills-taleemabad")   # the pack checkout: holds kie_throttle.py and .env
sys.path.insert(0, os.path.join(REPO, "skills", "kie-ai-imagegen", "scripts"))
from kie_throttle import LIMITER, QuotaExhausted, classify  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img", "raw")
os.makedirs(OUT, exist_ok=True)


def load_key():
    for line in open(os.path.join(REPO, ".env"), encoding="utf-8"):
        if line.startswith("KIE_API_KEY="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    raise SystemExit("KIE_API_KEY missing from .env (see KEYS.md)")


KEY = load_key()
H = {"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"}

# Same style sentence as the English pilot, so the pictures match across subjects
STYLE = ("Friendly flat-vector children's picture-book illustration, thick clean dark-navy outlines, "
         "bright simple colours, soft rounded shapes, one single subject centred and filling about seventy percent "
         "of the frame, plain pure white background, no shadow, no border. The picture contains no writing of any kind.")
NEG = ("--no text, letters, numbers, words, labels, watermark, logo, extra objects, duplicated objects, "
       "blurry details, photographic style, dark background, grid pattern")

BOY = "a Pakistani boy about seven years old with short black hair, a blue shalwar kameez, smiling"
GIRL = "a Pakistani girl about seven years old with a long black plait, a purple kameez and a pink dupatta, smiling"
TEACHER = "a kind Pakistani woman teacher in a green shalwar kameez with a cream dupatta, smiling"

SCENE = {
    "teacher_point": f"{TEACHER}, standing and pointing with one hand towards the viewer's right, upper body, calm and encouraging",
    "teacher_oops": f"{TEACHER}, upper body, one hand raised to her cheek with a playful surprised 'oops' expression and a funny wide smile, as if she has just made a silly mistake",
    "pair_book": f"{BOY} and {GIRL}, sitting side by side at a small wooden desk looking at one open picture book together, the girl pointing at the book with one finger, upper bodies",
}
PROMPTS = {f"scene_{k}": f"{STYLE} Subject: {v}. {NEG}" for k, v in SCENE.items()}


def post(url, body):
    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers=H, method="POST")
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())


def get(url):
    req = urllib.request.Request(url, headers=H)
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())


def render(name):
    dest = os.path.join(OUT, f"{name}.png")
    if os.path.exists(dest):
        return name, "cached"
    LIMITER.acquire()
    res = post("https://api.kie.ai/api/v1/jobs/createTask", {
        "model": "nano-banana-pro",
        "input": {"prompt": PROMPTS[name], "aspect_ratio": "1:1", "resolution": "1K", "output_format": "png"},
    })
    if classify(res) is QuotaExhausted:
        raise QuotaExhausted(str(res))      # a 433 means stop, never loop
    if res.get("code") != 200:
        return name, f"create-failed {res}"
    tid = res["data"]["taskId"]
    for _ in range(60):
        time.sleep(8)
        LIMITER.acquire()
        info = get(f"https://api.kie.ai/api/v1/jobs/recordInfo?taskId={tid}")
        st = info.get("data", {}).get("state")
        if st == "success":
            url = json.loads(info["data"]["resultJson"])["resultUrls"][0]
            with urllib.request.urlopen(url, timeout=120) as r, open(dest, "wb") as f:
                f.write(r.read())
            return name, "ok"
        if st == "fail":
            return name, f"failed {info['data'].get('failMsg')}"
    return name, "timeout"


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "balance":
        print(get("https://api.kie.ai/api/v1/chat/credit"))
    elif cmd == "run":
        names = sys.argv[2:] or list(PROMPTS)
        names = list(PROMPTS) if names == ["all"] else names
        with cf.ThreadPoolExecutor(2) as ex:
            for n, status in ex.map(render, names):
                print(n, status, flush=True)
