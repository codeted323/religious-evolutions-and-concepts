import html, re, collections
from themes import TRADS, MATCHED, UNMATCHED

rows = [l.split('|') for l in open('q.tsv', encoding='utf8').read().split('\n') if l and not l.startswith('#')]
TN = dict(TRADS)
ORDER = [t for t, _ in TRADS]
E = html.escape

def slug(s): return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')

def quote_html(i):
    tr, ref, q, src, url = rows[i]
    q = q.strip()
    para = q.startswith('[paraphrase]') or (q.startswith('[') and q.endswith(']') and q.count('[') == 1)
    if para:
        body = E(q.replace('[paraphrase]', '').strip().strip('[]').strip())
        qh = f'<p class="q para">{body} <span class="ptag">paraphrase</span></p>'
    else:
        body = E(q)
        body = re.sub(r'\[([^\]]+)\]', r'<span class="ed">[\1]</span>', body)
        qh = f'<p class="q">“{body}”</p>'
    return f'{qh}<p class="cite">{E(ref)} · <a href="{E(url)}" target="_blank" rel="noopener">{E(src)}</a></p>'

def theme_html(tid, title, summ, qs, note, kind):
    by = collections.OrderedDict((t, []) for t in ORDER)
    for i in qs: by[rows[i][0]].append(i)
    present = [t for t in ORDER if by[t]]
    if kind == 'm':
        meta = f'<p class="meta">Found in {len(present)} of {len(ORDER)} traditions: {", ".join(TN[t] for t in present)}</p>'
    else:
        meta = f'<p class="meta">{E(note)}</p>' if note else ''
    out = [f'<section class="theme" id="{kind}-{tid}"><h3>{E(title)}</h3>{meta}<p class="summ">{E(summ)}</p>']
    if kind == 'm' and note:
        out.append(f'<p class="note">{E(note)}</p>')
    for t in present:
        out.append(f'<div class="trad"><div class="tname">{E(TN[t])}</div>' + ''.join(f'<div class="entry">{quote_html(i)}</div>' for i in by[t]) + '</div>')
    out.append('</section>')
    return ''.join(out)

toc, body = [], []

def toc_item(href, label, lvl):
    toc.append(f'<li class="l{lvl}"><a href="#{href}" data-t="{href}">{E(label)}</a></li>')

# Intro
toc_item('about', 'About this collection', 1)
nm = sum(len(t) for _, t in MATCHED); nu = sum(len(t) for _, t in UNMATCHED)
body.append(f'''<section id="about" class="top"><h1>Shared Wisdom</h1>
<p class="lede">Moral and practical guidance from the wisdom texts of eleven religious traditions, lined up to show where they say the same thing and where they stand apart.</p>
<p>The passages come from the texts each tradition treats as practical guidance for living. That means sayings, proverbs, parables and counsel more than formal law: Pirkei Avot and Proverbs, the Sermon on the Mount and the parables of Jesus, the Quran and hadith, the Bhagavad Gita, Tirukkural and Mahabharata, the Dhammapada and the Buddha's advice to Sigala, the Jain sutras, the Guru Granth Sahib, the Dao De Jing, the Analects, the Zoroastrian <i>Menog-i Khrad</i>, and Bahá'u'lláh's <i>Hidden Words</i>.</p>
<p>The collection has {len(rows)} passages, grouped into {nm} shared themes and {nu} distinctive ones.</p></section>''')

toc_item('method', 'How to read it', 1)
body.append('''<section id="method" class="top"><h2>How to read it</h2>
<p><b>Matched</b> themes are ideas that at least three traditions in this collection express in substantially the same way. Each one lists which traditions it was found in. Where traditions qualify or disagree with the shared idea, a note says so.</p>
<p><b>Unmatched</b> themes are teachings found in only one or two traditions here, or points where the traditions take different positions. "Unmatched" means not matched <i>within this collection</i>. These are large literatures, and a parallel may well exist in a text not sampled here.</p>
<p>Within each section, themes are grouped by area of life.</p>
<p><b>Quotations</b> come from public-domain or freely available translations, which are named and linked under each passage. Longer verses are shortened, with "…" marking cuts. Text in [brackets] is either the translator's own insertion or a connecting phrase or paraphrase of mine. A few passages are given only in paraphrase, and are labelled as such. The theme summaries are mine.</p>
<p><b>Limits.</b> This is a sample, not a census. The coverage reflects which texts could be checked against an online source, so a tradition missing from a theme means only that no matching passage was gathered, not that the tradition lacks the idea. Translations differ, and an English match can hide real differences in the original concepts.</p></section>''')

# Glance table
toc_item('glance', 'At a glance', 1)
head = ''.join(f'<th title="{E(n)}"><span>{E(n)}</span></th>' for _, n in TRADS)
trs = []
for area, ths in MATCHED:
    trs.append(f'<tr class="area"><td colspan="{len(TRADS)+1}">{E(area)}</td></tr>')
    for tid, title, summ, qs, note in ths:
        have = {rows[i][0] for i in qs}
        cells = ''.join(f'<td>{"●" if t in have else ""}</td>' for t in ORDER)
        trs.append(f'<tr><th scope="row"><a href="#m-{tid}" data-t="m-{tid}">{E(title)}</a></th>{cells}</tr>')
counts = collections.Counter(r[0] for r in rows)
body.append(f'''<section id="glance" class="top"><h2>At a glance</h2>
<p>Which traditions express each shared theme, among the passages gathered here.</p>
<div class="tablewrap"><table class="glance"><thead><tr><th></th>{head}</tr></thead><tbody>{''.join(trs)}</tbody></table></div>
<p class="small">Passages per tradition: {', '.join(f"{TN[t]} {counts[t]}" for t in ORDER)}.</p></section>''')

def section(kind, label, data, intro):
    sid = 'matched' if kind == 'm' else 'unmatched'
    toc_item(sid, label, 0)
    body.append(f'<section id="{sid}" class="part"><h2 class="parth">{E(label)}</h2><p>{intro}</p></section>')
    for area, ths in data:
        aid = f'{kind}a-{slug(area)}'
        toc_item(aid, area, 1)
        body.append(f'<section id="{aid}" class="area"><h2>{E(area)}</h2></section>')
        for tid, title, summ, qs, note in ths:
            toc_item(f'{kind}-{tid}', title, 2)
            body.append(theme_html(tid, title, summ, qs, note, kind))

section('m', 'Matched', MATCHED, 'Guidance that three or more traditions share.')
section('u', 'Unmatched', UNMATCHED, 'Teachings particular to one or two traditions in this collection, and points of disagreement.')

# Sources
toc_item('sources', 'Traditions and sources', 0)
srcs = collections.OrderedDict((t, collections.OrderedDict()) for t in ORDER)
for tr, ref, q, src, url in rows:
    srcs[tr].setdefault(src, url)
sl = ''.join(f'<h3>{E(TN[t])}</h3><ul>' + ''.join(f'<li><a href="{E(u)}" target="_blank" rel="noopener">{E(s)}</a></li>' for s, u in srcs[t].items()) + '</ul>' for t in ORDER)
body.append(f'''<section id="sources" class="part"><h2 class="parth">Traditions and sources</h2>
<p>Each passage was read from the online edition linked beside it. The translations are public domain (for example, the World English Bible, JPS 1917, Legge, Müller, Pope, Jacobi, West and Pickthall) or are published for free use: Mishnah Yomit (CC-BY), Access to Insight, the Bahá'í Reference Library, SriGranth.org and Sunnah.com.</p>{sl}</section>''')

TOC = '<ul>' + ''.join(toc) + '</ul>'
tpl = open('page.html', encoding='utf8').read()
open('index.html', 'w', encoding='utf8').write(tpl.replace('<!--TOC-->', TOC).replace('<!--BODY-->', ''.join(body)))
print('ok', len(rows), nm, nu)
