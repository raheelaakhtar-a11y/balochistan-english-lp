"""Generate the Day-1 picture set via kie.ai (nano-banana-pro). Key is read from the repo .env, never printed."""
import json, os, sys, time, urllib.request, urllib.error, concurrent.futures as cf

REPO = os.environ.get("AGENT_SKILLS_REPO", os.getcwd())  # folder with .env (KIE_API_KEY) and skills/kie-ai-imagegen
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

STYLE = ("Friendly flat-vector children's picture-book illustration, thick clean dark-navy outlines, "
         "bright simple colours, soft rounded shapes, one single subject centred and filling about seventy percent "
         "of the frame, plain pure white background, no shadow, no border. The picture contains no writing of any kind.")
NEG = ("--no text, letters, numbers, words, labels, watermark, logo, extra objects, duplicated objects, "
       "blurry details, photographic style, dark background, grid pattern")

OBJ = {
    "A": "one shiny red apple with a short brown stem and one green leaf",
    "B": "one round ball with red, yellow and blue panels",
    "C": "one friendly grey tabby cat sitting upright with its tail curled round its feet",
    "D": "one yellow duck with an orange beak and orange feet, standing, side view",
    "E": "one plain white egg standing upright",
    "F": "one orange-and-white fish swimming, side view",
    "G": "one cream-and-brown goat with two small horns, standing, side view",
    "H": "one brown hen with a red comb, standing, side view",
    "I": "one ice cream cone with two scoops, one pink and one cream",
    "J": "one blue ceramic jug with a single handle",
    "K": "one diamond-shaped red-and-yellow kite with a curly ribbon tail and a string",
    "L": "one friendly golden lion with a brown mane, sitting, facing the viewer",
    "M": "one ripe yellow-orange mango with one green leaf",
    "N": "one butterfly net with a long black handle and a round mesh net",
    "O": "one round orange fruit with one green leaf",
    "P": "one blue ballpoint pen lying diagonally with its cap beside it",
    "Q": "one folded patchwork quilt made of red, blue, yellow and green squares",
    "R": "one white rabbit with long upright ears and a pink nose, sitting",
    "S": "one smiling cartoon sun, yellow with short orange rays",
    "T": "one traditional silver teapot with a curved spout, a small lid and a little steam",
    "U": "one open bright-red umbrella with a curved wooden handle",
    "V": "one small yellow delivery van, side view",
    "W": "one round wristwatch with a brown strap and a white face showing clock hands",
    "X": "one xylophone with seven coloured bars and two wooden mallets",
    "Y": "one red yo-yo with a yellow centre hanging on a string",
    "Z": "one zebra with black and white stripes, standing, side view",
}

BOY = "a Pakistani boy about seven years old with short black hair, a blue shalwar kameez, smiling"
GIRL = "a Pakistani girl about seven years old with a long black plait, a purple kameez and a pink dupatta, smiling"
TEACHER = "a kind Pakistani woman teacher in a green shalwar kameez with a cream dupatta, smiling"

SCENE = {
    "kids_wave": f"{BOY} and {GIRL}, standing side by side, both waving happily, full body",
    "teacher_point": f"{TEACHER}, standing and pointing with one hand towards the viewer's right, upper body, calm and encouraging",
    "pair_book": f"{BOY} and {GIRL}, sitting side by side at a small wooden desk looking at one open picture book, the girl pointing at the book with one finger, upper bodies",
}

PROMPTS = {f"obj_{k}": f"{STYLE} Subject: {v}. {NEG}" for k, v in OBJ.items()}
PROMPTS.update({f"scene_{k}": f"{STYLE} Subject: {v}. {NEG}" for k, v in SCENE.items()})


def post(url, body):
    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers=H, method="POST")
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())


def get(url):
    req = urllib.request.Request(url, headers=H)
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())


def balance():
    return get("https://api.kie.ai/api/v1/chat/credit")


def render(name):
    dest = os.path.join(OUT, f"{name}.png")
    if os.path.exists(dest):
        return name, "cached"
    LIMITER.acquire()
    res = post("https://api.kie.ai/api/v1/jobs/createTask", {
        "model": "nano-banana-pro",
        "input": {"prompt": PROMPTS[name], "aspect_ratio": "1:1", "resolution": "1K", "output_format": "png"},
    })
    k = classify(res)
    if k is QuotaExhausted:
        raise QuotaExhausted(str(res))
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
        print(balance())
    elif cmd == "run":
        names = sys.argv[2:] or list(PROMPTS)
        names = list(PROMPTS) if names == ["all"] else names
        with cf.ThreadPoolExecutor(6) as ex:
            for n, status in ex.map(render, names):
                print(n, status, flush=True)
