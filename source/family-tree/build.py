import json, re, sys
import numpy as np
from traits import TAXONOMY

FAMILIES = [
 ("pre","Prehistoric and reconstructed roots",""),
 ("ane","Ancient Near East and Egypt",""),
 ("eur","European and Mediterranean",""),
 ("ir","Iranian",""),
 ("jud","Jewish","About 14.8 million Jews (Pew, 2020)"),
 ("chr","Christian","About 2.3 billion Christians (Pew, 2020)"),
 ("isl","Islamic and Islam-derived","About 2.0 billion Muslims (Pew, 2020)"),
 ("gno","Gnostic and esoteric",""),
 ("hin","Hindu","About 1.2 billion Hindus, 14.9% of the world (Pew, 2020)"),
 ("ind","Jain, Sikh and other Indic",""),
 ("bud","Buddhist","About 324 million Buddhists (Pew, 2020)"),
 ("eas","East Asian",""),
 ("nea","Northern and Central Asian",""),
 ("afr","African",""),
 ("afd","Afro-Atlantic diaspora",""),
 ("amr","Indigenous Americas",""),
 ("oce","Oceania and Austronesian",""),
 ("sas","South and Southeast Asian Indigenous",""),
 ("mod","Modern and secular","About 24% of the world is religiously unaffiliated (Pew, 2020)"),
]
fam_ids = [f[0] for f in FAMILIES]

traits = {}; cats=[]
for cid, cname, subs in TAXONOMY:
    c = {"id":cid,"name":cname,"subs":[]}
    for sname, tl in subs:
        s = {"name":sname,"traits":[]}
        for code,name,desc,note in tl:
            assert code not in traits, code
            traits[code] = {"id":code,"name":name,"desc":desc,"note":note,"cat":cid,"sub":sname}
            s["traits"].append(code)
        c["subs"].append(s)
    cats.append(c)

rows=[]
for fn in ["data1.txt","data2.txt","data3.txt","data4.txt","data5.txt","data6.txt"]:
    for ln,line in enumerate(open(fn,encoding="utf8"),1):
        line=line.rstrip("\n")
        if not line.strip() or line.startswith("#"): continue
        p=line.split("|")
        tag=p[12] if len(p)==13 else ""
        if len(p)==13: p=p[:12]
        if len(p)!=12: sys.exit(f"{fn}:{ln} has {len(p)} fields: {line[:60]}")
        rows.append(dict(id=p[0],n=p[1],f=p[2],p=p[3] or None,x=[i for i in p[4].split(",") if i],
            s=int(p[5]),e=None if p[6]=="-" else int(p[6]),r=p[7],c=int(p[8]),st=p[9],raw=p[10],d=p[11],tag=tag,src=f"{fn}:{ln}"))
by={r["id"]:r for r in rows}
errs=[]; warns=[]
if len(by)!=len(rows): 
    from collections import Counter; errs.append(f"dup ids {[k for k,v in Counter(r['id'] for r in rows).items() if v>1]}")
for r in rows:
    if r["f"] not in fam_ids: errs.append(f"{r['id']} bad family {r['f']}")
    if r["p"] and r["p"] not in by: errs.append(f"{r['id']} bad parent {r['p']}")
    for x in r["x"]:
        if x not in by: errs.append(f"{r['id']} bad influence {x}")
    if r["e"] is not None and r["e"]<r["s"]: errs.append(f"{r['id']} ends before start")
    if (r["e"] is None)!=(r["st"] in "LR"): errs.append(f"{r['id']} status/end mismatch {r['st']} {r['e']}")
    if r["p"] and r["p"] in by:
        P=by[r["p"]]
        if r["s"]<P["s"]: warns.append(f"{r['id']} starts {r['s']} before parent {P['id']} {P['s']}")
        if P["e"] is not None and r["s"]>P["e"]+50: warns.append(f"{r['id']} starts {r['s']} after parent {P['id']} ended {P['e']}")
    for x in r["x"]:
        if x in by and by[x]["s"]>r["s"]+20: warns.append(f"{r['id']} ({r['s']}) influenced by later {x} ({by[x]['s']})")
    for tok in r["raw"].split():
        code=tok.lstrip("=+-")
        if code not in traits: errs.append(f"{r['id']} bad trait {tok}")
if errs: print("\n".join(errs)); sys.exit(1)

# resolve traits through inheritance
res={}
def resolve(i, stack=()):
    if i in res: return res[i]
    if i in stack: sys.exit(f"cycle {stack}")
    r=by[i]; toks=r["raw"].split()
    if toks and toks[0].startswith("="):
        cur=set(t.lstrip("=+") for t in toks if not t.startswith("-")); base=set()
        toks=[t for t in toks if t.startswith("-")]
    else:
        base=set(resolve(r["p"],stack+(i,))) if r["p"] else set(); cur=set(base)
    for t in toks:
        if t.startswith("-"):
            if t[1:] not in cur: warns.append(f"{i}: removes {t[1:]} not inherited")
            cur.discard(t[1:])
        else:
            c=t.lstrip("+")
            if c in cur: warns.append(f"{i}: adds {c} already inherited")
            cur.add(c)
    res[i]=cur; return cur
for r in rows: resolve(r["id"])
for r in rows:
    par=res[r["p"]] if r["p"] else set()
    r["t"]=sorted(res[r["id"]]); r["g"]=sorted(res[r["id"]]-par); r["l"]=sorted(par-res[r["id"]])
    if not r["p"]: r["g"]=r["t"]; r["l"]=[]

# similarity
ids=[r["id"] for r in rows]; T=list(traits)
M=np.array([[1 if t in res[i] else 0 for t in T] for i in ids],float)
inter=M@M.T; sz=M.sum(1); uni=sz[:,None]+sz[None,:]-inter
J=np.where(uni>0,inter/np.maximum(uni,1),0)
for k,r in enumerate(rows):
    order=np.argsort(-J[k]); sims=[]
    for j in order:
        if j==k: continue
        sims.append([ids[j],round(float(J[k,j]),3)])
        if len(sims)==8: break
    r["sim"]=sims
    so=[]
    for j in order:
        if j==k or rows[j]["f"]==r["f"]: continue
        so.append([ids[j],round(float(J[k,j]),3)])
        if len(so)==5: break
    r["so"]=so
# 2D layout from similarity (classical MDS on 1-J)
from sklearn.manifold import MDS
D=1-J
xy=MDS(n_components=2,dissimilarity="precomputed",random_state=7,n_init=4,max_iter=600,normalized_stress="auto",init="random").fit_transform(D)
xy=(xy-xy.min(0))/(xy.max(0)-xy.min(0))
for k,r in enumerate(rows): r["xy"]=[round(float(xy[k,0]),4),round(float(xy[k,1]),4)]
# family affinity matrix
fm=[]
for a in fam_ids:
    ia=[k for k,r in enumerate(rows) if r["f"]==a]; row=[]
    for b in fam_ids:
        ib=[k for k,r in enumerate(rows) if r["f"]==b]
        vals=[J[x,y] for x in ia for y in ib if x!=y]
        row.append(round(float(np.mean(vals)),3) if vals else None)
    fm.append(row)

TAGS={"FL":"https://en.wikipedia.org/wiki/List_of_founders_of_religious_traditions","JN":"https://en.wikipedia.org/wiki/Japanese_new_religions",
"TA":"https://en.wikipedia.org/wiki/Taoism","CS":"https://en.wikipedia.org/wiki/Chinese_salvationist_religions","SB":"https://en.wikipedia.org/wiki/Schools_of_Buddhism",
"CB":"https://en.wikipedia.org/wiki/Chinese_Buddhism","TB":"https://en.wikipedia.org/wiki/Timeline_of_Buddhism","HD":"https://en.wikipedia.org/wiki/Hindu_denominations",
"SO":"https://en.wikipedia.org/wiki/List_of_Sufi_orders","MH":"https://en.wikipedia.org/wiki/Madhhab","TC":"https://en.wikipedia.org/wiki/Timeline_of_Christianity",
"WE":"https://en.wikipedia.org/wiki/Western_esotericism","LC":"https://en.wikipedia.org/wiki/Afro-American_religion","CU":"https://www.wikiwand.com/en/articles/List_of_cults"}
AUD={}
for fn in ("audit.tsv","audit2.tsv"):
  for l in open(fn,encoding="utf8"):
    if l.startswith("#") or not l.strip(): continue
    i,stt,note,srcs=l.rstrip("\n").split("|",3)
    AUD[i]=(stt,note,[u for u in srcs.split(";") if u])
EXT={}
for l in open("extras.tsv",encoding="utf8"):
    if l.startswith("#") or not l.strip(): continue
    i,kt,kf=l.rstrip("\n").split("|")
    EXT[i]=([x.strip() for x in kt.split(";") if x.strip()],[x.strip() for x in kf.split(";") if x.strip()])
for r in rows:
    if r["id"] in AUD: st_,note,srcs=AUD[r["id"]]
    elif r["tag"] and r["tag"]!="-":
        k=r["tag"].rstrip("!"); conf=r["tag"].endswith("!")
        st_="ok" if conf else "part"
        note=("Name and founder or date confirmed in the cited list." if conf else "Name (and founder where given) confirmed in the cited list; the date follows standard references and is not confirmed there.")
        srcs=[TAGS[k]]
    else: st_,note,srcs="unv","Added in the expansion; not individually checked against a source. Dates follow standard references at the confidence shown.",[]
    r["au"]=st_; r["an"]=note; r["src"]=srcs
    r["kt"],r["kf"]=EXT.get(r["id"],([],[]))
missing=[i for i in list(AUD)+list(EXT) if i not in by]
if missing: print("audit ids not in data:",missing)
out={"families":[{"id":a,"name":b,"note":c} for a,b,c in FAMILIES],"cats":cats,"traits":traits,
     "trads":[{k:r[k] for k in ["id","n","f","p","x","s","e","r","c","st","d","t","g","l","sim","so","xy","au","an","src","kt","kf"]} for r in rows],
     "famsim":fm}
json.dump(out,open("data.json","w",encoding="utf8"),ensure_ascii=False,separators=(",",":"))
print(len(rows),"traditions",len(traits),"traits")
print("\n".join(warns))
