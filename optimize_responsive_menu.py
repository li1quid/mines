from pathlib import Path
import shutil

root = Path('mines-seo-site')
menu_button = '<button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav"><span></span><span></span><span></span><b>Меню</b></button>'

# Add one mobile menu button to every generated/static HTML page.
for path in root.glob('*.html'):
    html = path.read_text(encoding='utf-8')
    if 'class="menu-toggle"' not in html:
        html = html.replace('</a>\n      <nav class="nav">', '</a>\n      ' + menu_button + '\n      <nav class="nav" id="site-nav">', 1)
        html = html.replace('</a>\r\n      <nav class="nav">', '</a>\r\n      ' + menu_button + '\r\n      <nav class="nav" id="site-nav">', 1)
        if 'id="site-nav"' not in html:
            html = html.replace('<nav class="nav">', '<nav class="nav" id="site-nav">', 1)
    else:
        html = html.replace('<nav class="nav">', '<nav class="nav" id="site-nav">', 1)
    path.write_text(html, encoding='utf-8')

# CSS: add responsive layout + collapsible mobile menu.
css_path = root / 'assets' / 'style.css'
css = css_path.read_text(encoding='utf-8')
css_block = r'''

/* Full responsive optimization + mobile collapsible section menu */
.menu-toggle{display:none}
img,svg,video,canvas{max-width:100%;height:auto}
@media (min-width:1440px){
  :root{--container:1240px}
  .site{grid-template-columns:292px minmax(0,1fr)}
  .container{padding-left:56px;padding-right:56px}
}
@media (max-width:1200px){
  .site{grid-template-columns:258px minmax(0,1fr)}
  .container{padding-left:28px;padding-right:28px}
}
@media (max-width:820px){
  .sidebar{
    position:sticky;
    top:0;
    z-index:50;
    display:grid;
    grid-template-columns:1fr auto;
    align-items:center;
    gap:10px;
  }
  .brand{margin:0;min-width:0}
  .menu-toggle{
    min-height:44px;
    display:inline-flex;
    align-items:center;
    justify-content:center;
    gap:8px;
    padding:9px 12px;
    border:1px solid rgba(226,232,240,.16);
    border-radius:999px;
    color:#eef6ff;
    background:rgba(255,255,255,.065);
    box-shadow:inset 0 1px 0 rgba(255,255,255,.07),0 10px 24px rgba(0,0,0,.18);
    font-weight:900;
    cursor:pointer;
    -webkit-tap-highlight-color:transparent;
  }
  .menu-toggle span{
    display:block;
    width:16px;
    height:2px;
    border-radius:99px;
    background:currentColor;
    transition:transform .2s ease,opacity .2s ease;
  }
  .menu-toggle b{font-size:13px;line-height:1}
  .sidebar.menu-open .menu-toggle span:nth-child(1){transform:translateY(5px) rotate(45deg)}
  .sidebar.menu-open .menu-toggle span:nth-child(2){opacity:0}
  .sidebar.menu-open .menu-toggle span:nth-child(3){transform:translateY(-5px) rotate(-45deg)}
  .sidebar .nav{
    grid-column:1/-1;
    display:grid;
    max-height:0;
    overflow:hidden;
    padding:0;
    opacity:0;
    transform:translateY(-6px);
    border:1px solid transparent;
    border-radius:22px;
    background:rgba(10,16,31,.94);
    box-shadow:0 24px 54px rgba(0,0,0,.34),inset 0 1px 0 rgba(255,255,255,.05);
    transition:max-height .28s ease,opacity .2s ease,transform .2s ease,padding .2s ease,border-color .2s ease;
  }
  .sidebar.menu-open .nav{
    max-height:75vh;
    overflow:auto;
    padding:10px;
    opacity:1;
    transform:translateY(0);
    border-color:rgba(226,232,240,.12);
  }
  .sidebar .nav a{
    width:100%;
    min-height:46px;
    justify-content:flex-start;
    border-radius:16px;
    white-space:normal;
  }
}
@media (max-width:520px){
  .brand strong{font-size:17px}
  .brand span span{max-width:152px}
  .menu-toggle{padding:9px 11px}
  .menu-toggle b{display:none}
  .hero-grid,.cards{gap:14px}
  .container{padding-left:10px;padding-right:10px}
  .topbar{padding-left:10px;padding-right:10px}
  .cta-strip strong{font-size:16px}
}
@media (max-width:360px){
  .brand span span{display:none}
  .brand-logo{width:38px;height:38px}
  h1{font-size:30px}
}
'''
if '/* Full responsive optimization + mobile collapsible section menu */' not in css:
    css = css.rstrip() + css_block + '\n'
    css_path.write_text(css, encoding='utf-8')

# JS: menu open/close behavior.
js_path = root / 'assets' / 'app.js'
js = js_path.read_text(encoding='utf-8')
js_block = r'''

(function(){
  const sidebar = document.querySelector('.sidebar');
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.sidebar .nav');
  if(!sidebar || !toggle || !nav) return;
  function setOpen(open){
    sidebar.classList.toggle('menu-open', open);
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  }
  toggle.addEventListener('click', function(){ setOpen(!sidebar.classList.contains('menu-open')); });
  nav.addEventListener('click', function(e){ if(e.target.closest('a')) setOpen(false); });
  document.addEventListener('click', function(e){ if(!sidebar.contains(e.target)) setOpen(false); });
  document.addEventListener('keydown', function(e){ if(e.key === 'Escape') setOpen(false); });
  window.addEventListener('resize', function(){ if(window.innerWidth > 820) setOpen(false); });
})();
'''
if 'const sidebar = document.querySelector' not in js:
    js = js.rstrip() + js_block + '\n'
    js_path.write_text(js, encoding='utf-8')

# Keep page generators synchronized enough for future rebuilds.
for gen_name in ['generate_pages.py', 'generate_multilang_pages.py']:
    gen = root / gen_name
    if not gen.exists():
        continue
    src = gen.read_text(encoding='utf-8')
    if 'class="menu-toggle"' not in src:
        src = src.replace('</a>\n      <nav class="nav">', '</a>\n      ' + menu_button + '\n      <nav class="nav" id="site-nav">')
        src = src.replace('</a>\n      <nav class="nav">{nav_html}', '</a>\n      ' + menu_button + '\n      <nav class="nav" id="site-nav">{nav_html}')
        src = src.replace('</a>\n      <nav class="nav">{nav_html(slug, lang)}</nav>', '</a>\n      ' + menu_button + '\n      <nav class="nav" id="site-nav">{nav_html(slug, lang)}</nav>')
    src = src.replace('<nav class="nav">', '<nav class="nav" id="site-nav">')
    gen.write_text(src, encoding='utf-8')

# Copy to OneDrive output folder.
dest = Path(r'C:\Users\kompy\OneDrive\Desktop\сайт\mines\multilang-site')
if dest.exists():
    shutil.rmtree(dest)
shutil.copytree(root, dest)

print('responsive_collapsible_menu_done=true')
print('html_pages_updated=' + str(len(list(root.glob('*.html')))))
print('copied_to=' + str(dest))
