from pathlib import Path
import shutil

root = Path('mines-seo-site')

# 1) Make the mobile menu control clearer and add a title for the dropdown list.
for path in root.glob('*.html'):
    html = path.read_text(encoding='utf-8')
    html = html.replace('<b>Меню</b>', '<b>Разделы</b>')
    html = html.replace('<b>Menu</b>', '<b>Разделы</b>')
    html = html.replace('class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav"', 'class="menu-toggle" type="button" aria-label="Открыть список разделов" aria-expanded="false" aria-controls="site-nav"')
    html = html.replace('<nav class="nav" id="site-nav">', '<nav class="nav" id="site-nav" data-menu-title="Разделы сайта">')
    path.write_text(html, encoding='utf-8')

# 2) Add final mobile UX override: dropdown title, active marker, better touch layout.
css_path = root / 'assets' / 'style.css'
css = css_path.read_text(encoding='utf-8')
css_block = r'''

/* Logical mobile sections dropdown */
@media (max-width:820px){
  .sidebar{
    grid-template-columns:minmax(0,1fr) auto;
    gap:10px 12px;
  }
  .menu-toggle{
    position:relative;
    min-width:118px;
    justify-content:space-between;
    padding:10px 13px 10px 12px;
    background:linear-gradient(135deg,rgba(84,240,193,.12),rgba(139,124,255,.10));
    border-color:rgba(84,240,193,.22);
  }
  .menu-toggle b{font-size:13px;letter-spacing:.01em}
  .menu-toggle::after{
    content:"";
    width:8px;
    height:8px;
    margin-left:2px;
    border-right:2px solid currentColor;
    border-bottom:2px solid currentColor;
    transform:rotate(45deg) translateY(-2px);
    transition:transform .2s ease;
    opacity:.85;
  }
  .sidebar.menu-open .menu-toggle::after{transform:rotate(225deg) translate(-2px,-1px)}
  .sidebar .nav{
    position:relative;
    gap:7px;
    margin-top:2px;
  }
  .sidebar .nav::before{
    content:attr(data-menu-title);
    display:flex;
    align-items:center;
    justify-content:space-between;
    min-height:34px;
    padding:4px 7px 8px;
    color:#9fb0c8;
    font-size:12px;
    font-weight:900;
    letter-spacing:.08em;
    text-transform:uppercase;
  }
  .sidebar .nav::after{
    content:"";
    position:absolute;
    left:12px;
    right:12px;
    top:43px;
    height:1px;
    background:linear-gradient(90deg,transparent,rgba(84,240,193,.24),rgba(139,124,255,.16),transparent);
  }
  .sidebar.menu-open .nav{padding:10px 10px 12px}
  .sidebar .nav a{
    display:grid;
    grid-template-columns:34px minmax(0,1fr) auto;
    align-items:center;
    gap:10px;
    min-height:50px;
    padding:10px 12px;
    border-radius:17px;
    font-size:15px;
    line-height:1.2;
  }
  .sidebar .nav a span{
    width:34px;
    height:34px;
    border-radius:13px;
    background:rgba(255,255,255,.065);
  }
  .sidebar .nav a.active{
    border-color:rgba(84,240,193,.30);
    background:linear-gradient(135deg,rgba(84,240,193,.16),rgba(139,124,255,.12));
  }
  .sidebar .nav a.active::after{
    content:"Открыто";
    padding:4px 8px;
    border-radius:999px;
    color:#07111f;
    background:linear-gradient(135deg,#5cf0c3,#6ee7f9);
    font-size:10px;
    font-weight:1000;
    text-transform:uppercase;
    letter-spacing:.04em;
  }
}
@media (max-width:520px){
  .menu-toggle{min-width:106px;padding-inline:11px}
  .sidebar .nav a{min-height:48px;font-size:14px}
  .sidebar .nav a.active::after{content:"";width:8px;height:8px;padding:0;border-radius:999px;background:#5cf0c3;box-shadow:0 0 0 4px rgba(84,240,193,.12)}
}
@media (max-width:360px){
  .menu-toggle{min-width:48px;border-radius:16px}
  .menu-toggle b{display:none}
}
'''
if '/* Logical mobile sections dropdown */' not in css:
    css = css.rstrip() + css_block + '\n'
    css_path.write_text(css, encoding='utf-8')

# 3) Improve JS aria-label state for accessibility.
js_path = root / 'assets' / 'app.js'
js = js_path.read_text(encoding='utf-8')
old = "toggle.setAttribute('aria-expanded', open ? 'true' : 'false');"
new = "toggle.setAttribute('aria-expanded', open ? 'true' : 'false');\n    toggle.setAttribute('aria-label', open ? 'Закрыть список разделов' : 'Открыть список разделов');"
if old in js and new not in js:
    js = js.replace(old, new, 1)
    js_path.write_text(js, encoding='utf-8')

# 4) Keep generators aligned for future page regeneration.
for generator_name in ['generate_pages.py', 'generate_multilang_pages.py']:
    path = root / generator_name
    if not path.exists():
        continue
    source = path.read_text(encoding='utf-8')
    source = source.replace('<b>Меню</b>', '<b>Разделы</b>')
    source = source.replace('class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav"', 'class="menu-toggle" type="button" aria-label="Открыть список разделов" aria-expanded="false" aria-controls="site-nav"')
    source = source.replace('<nav class="nav" id="site-nav">', '<nav class="nav" id="site-nav" data-menu-title="Разделы сайта">')
    path.write_text(source, encoding='utf-8')

# 5) Copy to final OneDrive output.
dest = Path(r'C:\Users\kompy\OneDrive\Desktop\сайт\mines\multilang-site')
if dest.exists():
    shutil.rmtree(dest)
shutil.copytree(root, dest)

print('mobile_sections_menu_refined=true')
print('pages_updated=' + str(len(list(root.glob('*.html')))))
print('copied_to=' + str(dest))
