from pathlib import Path
import re

root = Path('mines-seo-site')
pages = ['apk.html', 'apk-en.html', 'apk-es.html', 'apk-de.html', 'apk-ph.html']
css = (root / 'assets' / 'style.css').read_text(encoding='utf-8')
print('css_apk_guide=' + str('apk-guide' in css))
print('css_apk_symbol=' + str('apk-symbol' in css))
print('css_apk_seo=' + str('apk-seo' in css))
for page in pages:
    html = (root / page).read_text(encoding='utf-8')
    text = re.sub(r'<[^>]+>', ' ', html)
    print(f'{page}: guide={"apk-guide" in html}; cards={html.count("apk-guide-card")}; chars={len(text)}; offer={html.count("https://lkzq.cc/644450")}')
