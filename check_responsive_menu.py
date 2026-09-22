from pathlib import Path

root = Path('mines-seo-site')
html_pages = list(root.glob('*.html'))
missing = []
for page in html_pages:
    html = page.read_text(encoding='utf-8')
    if 'class="menu-toggle"' not in html or 'id="site-nav"' not in html:
        missing.append(page.name)

css = (root / 'assets' / 'style.css').read_text(encoding='utf-8')
js = (root / 'assets' / 'app.js').read_text(encoding='utf-8')
index_html = (root / 'index.html').read_text(encoding='utf-8')

print(f'html_pages={len(html_pages)}')
print('missing_mobile_menu=' + (','.join(missing) if missing else 'none'))
print('css_collapsible=' + str('mobile collapsible section menu' in css))
print('css_820_media=' + str('@media (max-width:820px)' in css))
print('css_520_media=' + str('@media (max-width:520px)' in css))
print('css_no_horizontal=' + str('overflow-x:hidden' in css))
print('js_menu_toggle=' + str('menu-open' in js and 'aria-expanded' in js))
print('js_click_outside=' + str('!sidebar.contains(e.target)' in js))
print('js_escape_close=' + str("e.key === 'Escape'" in js))
print('index_guides=' + str('href="home-en.html"' in index_html))
