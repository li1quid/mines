from pathlib import Path

root = Path('mines-seo-site')
css = (root / 'assets' / 'style.css').read_text(encoding='utf-8')
js = (root / 'assets' / 'app.js').read_text(encoding='utf-8')
html_pages = sorted(root.glob('*.html'))
missing_toggle = []
missing_topbar = []
missing_css = []
for page in html_pages:
    html = page.read_text(encoding='utf-8')
    if 'assets/style.css' not in html:
        missing_css.append(page.name)
    if '<header class="topbar"' not in html:
        missing_topbar.append(page.name)
    if 'data-theme-toggle' not in html:
        missing_toggle.append(page.name)

checks = {
    'white_blue_theme_css': 'White & Blue Theme Switcher' in css,
    'light_theme_selector': 'html[data-theme="light"]' in css,
    'theme_toggle_css': '.theme-toggle' in css,
    'theme_mobile_820': '@media (max-width:820px)' in css and '.theme-toggle' in css,
    'theme_mobile_520': '@media (max-width:520px)' in css,
    'theme_js_storage': 'minesneonTheme' in js,
    'theme_js_toggle': '[data-theme-toggle]' in js,
    'keeps_black_gold_dark': 'Black & Gold Premium Theme' in css,
}

print('html_pages=' + str(len(html_pages)))
print('missing_css=' + (','.join(missing_css) if missing_css else 'none'))
print('missing_topbar=' + (','.join(missing_topbar) if missing_topbar else 'none'))
print('missing_toggle_count=' + str(len(missing_toggle)))
print('missing_toggle=' + (','.join(missing_toggle) if missing_toggle else 'none'))
for key, value in checks.items():
    print(f'{key}={value}')
