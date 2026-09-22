from pathlib import Path
import shutil

ROOT = Path('mines-seo-site')
DEST = Path(r'C:\Users\kompy\OneDrive\Desktop\сайт\mines\multilang-site')
THEME_BUTTON = '<button class="theme-toggle" type="button" aria-pressed="false" data-theme-toggle><span class="theme-toggle__icon">☀</span><span class="theme-toggle__text">Светлая тема</span></button>'

updated = 0
for page in ROOT.glob('*.html'):
    html = page.read_text(encoding='utf-8')
    if 'data-theme-toggle' in html:
        continue
    header_start = html.find('<header class="topbar"')
    if header_start == -1:
        continue
    small_end = html.find('</small>', header_start)
    header_end = html.find('</header>', header_start)
    if small_end == -1 or header_end == -1 or small_end > header_end:
        continue
    insert_at = small_end + len('</small>')
    separator = '\n        ' if '\n' in html[header_start:header_end] else ''
    html = html[:insert_at] + separator + THEME_BUTTON + html[insert_at:]
    page.write_text(html, encoding='utf-8')
    updated += 1

if DEST.exists():
    shutil.rmtree(DEST)
shutil.copytree(ROOT, DEST)

print('theme_toggle_fixed_pages=' + str(updated))
print('copied_to=' + str(DEST))
