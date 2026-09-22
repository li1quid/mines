from pathlib import Path
import re
import shutil
import py_compile

root = Path('mines-seo-site')
pattern = re.compile(r'^(analog|bonus|home|demo|promocode|registration|strategies|download|hack|mines-game)-(ru|en|es|de|ph)\.html$')
pages = [p for p in root.glob('*.html') if pattern.match(p.name)]
print(f'multilang_pages={len(pages)}')

sample = (root / 'demo-en.html').read_text(encoding='utf-8')
print('sample_lang_switcher=' + str('class="lang-switcher"' in sample))
print('sample_hreflang=' + str(sample.count('rel="alternate"')))
print('sample_offer_links=' + str(sample.count('https://lkzq.cc/644450')))
print('sample_nav_sections=' + str(len(re.findall(r'href="(analog|bonus|home|demo|promocode|registration|strategies|download|hack|mines-game)-en\.html"', sample))))

css = (root / 'assets' / 'style.css').read_text(encoding='utf-8')
print('css_lang_switcher=' + str('lang-switcher' in css))
print('css_article_content=' + str('article-content' in css))
print('css_no_horizontal=' + str('overflow-x:hidden' in css))

py_compile.compile(str(root / 'generate_multilang_pages.py'), doraise=True)
py_compile.compile(str(root / 'sync_multilang_css.py'), doraise=True)
print('python_generators_compile=True')

dest = Path(r'C:\Users\kompy\OneDrive\Desktop\сайт\mines\multilang-site')
if dest.exists():
    shutil.rmtree(dest)
shutil.copytree(root, dest)
print('copied_to=' + str(dest))
