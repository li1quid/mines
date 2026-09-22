from pathlib import Path
import re
import shutil

ROOT = Path('mines-seo-site')
patterns = [
    re.compile(r'\n?\s*<a\s+class="[^"]*"\s+href="other(?:-[a-z]{2})?\.html"><span>[^<]*</span>[^<]*</a>', re.I),
    re.compile(r'\n?\s*<link\s+rel="alternate"[^>]+href="[^"]*other(?:-[a-z]{2})?\.html"[^>]*>', re.I),
]
text_terms = ['Other games', 'Другие игры', 'Больше игр', 'otros juegos', 'andere spiele']

for path in ROOT.glob('*.html'):
    html = path.read_text(encoding='utf-8')
    for pattern in patterns:
        html = pattern.sub('', html)
    # Remove accidental empty lines left in nav, do not alter article words like "other players".
    html = re.sub(r'\n{3,}', '\n\n', html)
    path.write_text(html, encoding='utf-8')

for path in ROOT.glob('other*.html'):
    path.unlink()

# Remove navigation entries from generators/scripts where present.
for script in ROOT.glob('*.py'):
    source = script.read_text(encoding='utf-8')
    source = re.sub(r"\n\s*\('other\.html',\s*'[^']+',\s*'[^']+'\),", '', source)
    source = re.sub(r"\n\s*\{'dir':\s*'[^']+',\s*'slug':\s*'other'[^\n]+\},", '', source)
    source = re.sub(r"\n\s*'other\.html':\s*\{.*?\n\s*\},", '', source, flags=re.S)
    script.write_text(source, encoding='utf-8')

html_pages = list(ROOT.glob('*.html'))
nav_other_hits = []
for path in html_pages:
    html = path.read_text(encoding='utf-8')
    if re.search(r'href="other(?:-[a-z]{2})?\.html"', html, re.I):
        nav_other_hits.append(path.name)

seo_targets = ['index.html','index-en.html','index-es.html','index-de.html','index-ph.html','promo.html','promo-en.html','promo-es.html','promo-de.html','promo-ph.html','strategies.html','strategies-main-en.html','strategies-main-es.html','strategies-main-de.html','strategies-main-ph.html','faq.html','faq-en.html','faq-es.html','faq-de.html','faq-ph.html']
short = []
for name in seo_targets:
    path = ROOT / name
    if not path.exists():
        short.append((name, 'missing'))
        continue
    html = path.read_text(encoding='utf-8')
    m = re.search(r'<section class="seo-block">(.*?)</section>', html, re.S)
    if not m:
        m = re.search(r'<article class="seo-block article-content">(.*?)</article>', html, re.S)
    chars = len(re.sub(r'<[^>]+>', ' ', m.group(1) if m else ''))
    if chars < 1000:
        short.append((name, chars))

print('html_pages=' + str(len(html_pages)))
print('other_pages_left=' + str(len(list(ROOT.glob('other*.html')))))
print('other_nav_hits=' + (','.join(nav_other_hits) if nav_other_hits else 'none'))
print('short_seo=' + (str(short) if short else 'none'))
print('offer_links=' + str(sum(p.read_text(encoding='utf-8').count('https://lkzq.cc/644450') for p in html_pages)))

dest = Path(r'C:\Users\kompy\OneDrive\Desktop\сайт\mines\multilang-site')
if dest.exists():
    shutil.rmtree(dest)
shutil.copytree(ROOT, dest)
print('copied_to=' + str(dest))
