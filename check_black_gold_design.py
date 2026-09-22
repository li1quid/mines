from pathlib import Path

root = Path('mines-seo-site')
css = (root / 'assets' / 'style.css').read_text(encoding='utf-8')
html_pages = list(root.glob('*.html'))
missing_css = []
for page in html_pages:
    html = page.read_text(encoding='utf-8')
    if 'assets/style.css' not in html:
        missing_css.append(page.name)

checks = {
    'black_gold_theme': 'Black & Gold Premium Theme' in css,
    'gold_texture': 'repeating-linear-gradient' in css,
    'radial_glow': 'radial-gradient' in css,
    'glass_panels': 'backdrop-filter' in css,
    'mobile_820': '@media (max-width:820px)' in css,
    'mobile_520': '@media (max-width:520px)' in css,
    'no_horizontal_scroll': 'overflow-x:hidden' in css,
    'buttons_gold': '#f6c85f' in css,
    'apk_gold_styles': 'apk-guide-card' in css and 'apk-symbol' in css,
}

print('html_pages=' + str(len(html_pages)))
print('missing_css=' + (','.join(missing_css) if missing_css else 'none'))
for key, value in checks.items():
    print(f'{key}={value}')
