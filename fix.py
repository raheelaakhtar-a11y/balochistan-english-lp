s=open('build.py',encoding='utf-8').read()
i=s.index('# key -> document module')
s=s[:i]+'''# key -> (document module, html/pdf stem it writes). Day 1 (M-B-01). For another day copy a module and add a key.
MODS = {"lp": ("doc_lp_m8", "lp8"), "prep": ("doc_prep_m6", "prep6"), "ws": ("doc_ws_m6", "ws6")}

if __name__ == "__main__":
    print("images processed:", process_images())
    sys.path.insert(0, WORK)
    for w in (sys.argv[1:] or list(MODS)):
        mod, stem = MODS[w]
        __import__(mod).build()
        pdf, ok, ovf = render(stem)
        pages = pngs(stem)[0] if ok else 0
        print(f"{w}: pdf={ok} pages={pages} overflow={ovf}")
'''
open('build.py','w',encoding='utf-8').write(s)
k=open('kie_gen.py',encoding='utf-8').read()
old=r'REPO = r"C:\Users\WALEED SALES\Desktop\Agent Skills\agent-skills-taleemabad"'
assert old in k
k=k.replace(old,'REPO = os.environ.get("AGENT_SKILLS_REPO", ' + old[7:] + ')   # the pack checkout: holds kie_throttle.py and .env')
open('kie_gen.py','w',encoding='utf-8').write(k)
