from pathlib import Path
import shutil

ROOT = Path('mines-seo-site')
CSS = ROOT / 'assets' / 'style.css'
JS = ROOT / 'assets' / 'app.js'
DEST = Path(r'C:\Users\kompy\OneDrive\Desktop\сайт\mines\multilang-site')

THEME_BUTTON = '<button class="theme-toggle" type="button" aria-pressed="false" data-theme-toggle><span class="theme-toggle__icon">☀</span><span class="theme-toggle__text">Светлая тема</span></button>'

light_theme_css = r'''

/* White & Blue Theme Switcher — design-only override */
.theme-toggle{
  position:relative;
  min-height:44px;
  display:inline-flex;
  align-items:center;
  justify-content:center;
  gap:9px;
  padding:10px 14px;
  border:1px solid rgba(255,214,128,.24);
  border-radius:999px;
  color:#fff0bd;
  background:linear-gradient(135deg,rgba(255,214,128,.12),rgba(255,255,255,.035));
  box-shadow:inset 0 1px 0 rgba(255,255,255,.08),0 12px 28px rgba(0,0,0,.22);
  font-size:13px;
  font-weight:900;
  line-height:1;
  cursor:pointer;
  white-space:nowrap;
  transition:transform .18s ease,background .18s ease,border-color .18s ease,box-shadow .18s ease,color .18s ease;
}
.theme-toggle:hover{transform:translateY(-1px);border-color:rgba(255,214,128,.42);background:linear-gradient(135deg,rgba(255,214,128,.20),rgba(255,255,255,.055))}
.theme-toggle__icon{display:grid;place-items:center;width:24px;height:24px;border-radius:999px;color:#120b03;background:linear-gradient(135deg,#fff3bd,#f6c85f)}
html[data-theme="light"]{
  color-scheme:light;
  background:#eef8ff;
}
html[data-theme="light"] body{
  color:#102033;
  background:
    radial-gradient(circle at 10% -12%,rgba(36,148,255,.26),transparent 32rem),
    radial-gradient(circle at 92% 0%,rgba(112,211,255,.30),transparent 35rem),
    radial-gradient(circle at 58% 42%,rgba(255,255,255,.78),transparent 30rem),
    linear-gradient(180deg,#f8fdff 0%,#eaf7ff 42%,#f7fbff 100%);
}
html[data-theme="light"] body::before{
  background:
    radial-gradient(circle at 20% 20%,rgba(42,156,255,.10) 0 1px,transparent 1.5px),
    linear-gradient(rgba(26,126,220,.060) 1px,transparent 1px),
    linear-gradient(90deg,rgba(26,126,220,.050) 1px,transparent 1px);
  background-size:18px 18px,46px 46px,46px 46px;
  opacity:.90;
  mask-image:linear-gradient(180deg,rgba(0,0,0,.76),rgba(0,0,0,.50) 54%,transparent 94%);
}
html[data-theme="light"] body::after{
  background:
    radial-gradient(circle at 50% 0%,rgba(255,255,255,.88),transparent 34rem),
    linear-gradient(115deg,transparent 0 34%,rgba(33,149,255,.095) 46%,transparent 58% 100%);
  mix-blend-mode:multiply;
  opacity:.70;
}
html[data-theme="light"] a{color:#086bc2}
html[data-theme="light"] .seo-block a,html[data-theme="light"] .article-content a{color:#075da8}
html[data-theme="light"] .sidebar{
  border-right-color:rgba(21,112,197,.16);
  background:
    linear-gradient(180deg,rgba(247,252,255,.94),rgba(226,243,255,.82)),
    repeating-linear-gradient(135deg,rgba(24,132,232,.050) 0 1px,transparent 1px 10px);
  box-shadow:18px 0 60px rgba(42,122,190,.10);
}
html[data-theme="light"] .sidebar::before{
  background:radial-gradient(circle at 28% 12%,rgba(70,178,255,.25),transparent 62%),linear-gradient(135deg,rgba(255,255,255,.72),rgba(186,229,255,.32));
  border-color:rgba(46,145,230,.14);
}
html[data-theme="light"] .brand,html[data-theme="light"] .brand strong{color:#102033}
html[data-theme="light"] .brand span span{color:#58728d}
html[data-theme="light"] .brand-logo{
  color:#fff;
  background:linear-gradient(135deg,#49b9ff 0%,#1488f2 48%,#0d4fa6 100%);
  box-shadow:0 18px 42px rgba(35,139,235,.20),inset 0 1px 0 rgba(255,255,255,.62),inset 0 -12px 22px rgba(3,59,132,.18);
}
html[data-theme="light"] .brand-logo::after{border-color:rgba(21,128,224,.24);box-shadow:0 0 24px rgba(42,156,255,.14)}
html[data-theme="light"] .nav a,html[data-theme="light"] .nav-subtoggle{
  color:#213a56;
  background:linear-gradient(135deg,rgba(255,255,255,.76),rgba(219,241,255,.52));
  border-color:rgba(32,134,224,.12);
}
html[data-theme="light"] .nav a span,html[data-theme="light"] .nav-subtoggle span{background:rgba(39,146,238,.10);color:#0d67bd}
html[data-theme="light"] .nav a.active,html[data-theme="light"] .nav a:hover,html[data-theme="light"] .nav-subtoggle:hover,html[data-theme="light"] .nav-group.open .nav-subtoggle{
  color:#083c78;
  border-color:rgba(33,142,238,.32);
  background:linear-gradient(135deg,rgba(220,243,255,.94),rgba(255,255,255,.78));
  box-shadow:inset 0 1px 0 rgba(255,255,255,.84),0 14px 30px rgba(40,132,218,.13),0 0 28px rgba(41,151,245,.10);
}
html[data-theme="light"] .nav a.active::before{background:linear-gradient(180deg,#76d8ff,#168df2,#0a5ab8)}
html[data-theme="light"] .nav-submenu{background:linear-gradient(180deg,rgba(247,252,255,.88),rgba(224,243,255,.78));border-color:rgba(33,142,238,.14)}
html[data-theme="light"] .side-cta{
  border-color:rgba(22,132,230,.26);
  background:linear-gradient(145deg,rgba(223,245,255,.92),rgba(255,255,255,.72)),repeating-linear-gradient(135deg,rgba(24,132,232,.045) 0 1px,transparent 1px 10px);
  color:#15314e;
}
html[data-theme="light"] .side-cta::before{background:rgba(49,161,255,.18)}
html[data-theme="light"] .topbar{
  border-bottom-color:rgba(21,112,197,.13);
  background:rgba(246,252,255,.76);
  box-shadow:0 14px 36px rgba(42,122,190,.10);
}
html[data-theme="light"] .topbar small{color:#315571}
html[data-theme="light"] .topbar small::before{background:linear-gradient(135deg,rgba(210,242,255,.90),rgba(255,255,255,.72));border-color:rgba(33,142,238,.26);color:#0d68bd}
html[data-theme="light"] .hero::after{background:linear-gradient(90deg,#7bdcff,#168df2,#0b63c7,transparent)}
html[data-theme="light"] .section-kicker,html[data-theme="light"] .badge{
  color:#075fae;
  border-color:rgba(33,142,238,.22);
  background:linear-gradient(135deg,rgba(220,243,255,.90),rgba(255,255,255,.70));
  box-shadow:inset 0 1px 0 rgba(255,255,255,.78),0 10px 24px rgba(40,132,218,.10);
}
html[data-theme="light"] h1,html[data-theme="light"] h2,html[data-theme="light"] .card h2,html[data-theme="light"] .panel h2{color:#102033;text-shadow:0 2px 28px rgba(37,145,238,.10)}
html[data-theme="light"] p,html[data-theme="light"] .lead,html[data-theme="light"] .seo-block p,html[data-theme="light"] .article-content p{color:#304b65}
html[data-theme="light"] .lead{color:#45647f}
html[data-theme="light"] .btn-pulse,html[data-theme="light"] .btn-main,html[data-theme="light"] .lang-switcher a.active,html[data-theme="light"] .lang-switcher a:hover,html[data-theme="light"] .lang-switcher-toggle:hover,html[data-theme="light"] .lang-switcher.open .lang-switcher-toggle{
  color:#fff;
  background:linear-gradient(135deg,#64cfff 0%,#168df2 46%,#0a58b8 100%);
  box-shadow:0 16px 34px rgba(33,142,238,.22),0 0 0 0 rgba(33,142,238,.20),inset 0 1px 0 rgba(255,255,255,.58),inset 0 -14px 24px rgba(3,59,132,.16);
}
html[data-theme="light"] .btn-ghost{color:#0b63b6;background:rgba(227,246,255,.72);border-color:rgba(33,142,238,.22)}
html[data-theme="light"] .panel,html[data-theme="light"] .card,html[data-theme="light"] .seo-block,html[data-theme="light"] .cta-strip,html[data-theme="light"] .faq-list details,html[data-theme="light"] .apk-guide-card{
  border-color:rgba(21,112,197,.13);
  background:
    linear-gradient(180deg,rgba(255,255,255,.84),rgba(232,247,255,.58)),
    repeating-linear-gradient(135deg,rgba(33,142,238,.035) 0 1px,transparent 1px 12px),
    linear-gradient(145deg,rgba(255,255,255,.94),rgba(221,242,255,.84));
  box-shadow:0 24px 62px rgba(49,122,184,.12),inset 0 1px 0 rgba(255,255,255,.80);
}
html[data-theme="light"] .panel::before,html[data-theme="light"] .card::before,html[data-theme="light"] .seo-block::before,html[data-theme="light"] .cta-strip::before{background:linear-gradient(135deg,rgba(90,190,255,.28),rgba(255,255,255,.70),rgba(255,255,255,0))}
html[data-theme="light"] .game-panel::after,html[data-theme="light"] .signal-panel::after,html[data-theme="light"] .promo-hero::after,html[data-theme="light"] .apk-guide-card::after{background:radial-gradient(circle,rgba(33,142,238,.15),transparent 68%)}
html[data-theme="light"] .game-toolbar input,html[data-theme="light"] .game-toolbar select{
  color:#17344f;
  background:rgba(255,255,255,.82);
  border-color:rgba(21,112,197,.16);
}
html[data-theme="light"] .game-toolbar input:focus,html[data-theme="light"] .game-toolbar select:focus{border-color:rgba(33,142,238,.55);box-shadow:0 0 0 4px rgba(33,142,238,.12),inset 0 1px 0 rgba(255,255,255,.86)}
html[data-theme="light"] .mult{color:#075fae;background:linear-gradient(135deg,rgba(218,243,255,.90),rgba(255,255,255,.68));border-color:rgba(33,142,238,.20)}
html[data-theme="light"] .cell{
  border-color:rgba(21,112,197,.13);
  background:radial-gradient(circle at 28% 20%,rgba(255,255,255,.72),transparent 34%),linear-gradient(145deg,#e5f7ff,#ffffff 72%);
  box-shadow:inset 0 -10px 18px rgba(44,125,190,.08),inset 0 1px 0 rgba(255,255,255,.85),0 11px 22px rgba(42,122,190,.10);
}
html[data-theme="light"] .cell:hover{border-color:rgba(33,142,238,.34);box-shadow:inset 0 -10px 18px rgba(44,125,190,.08),0 14px 30px rgba(33,142,238,.13)}
html[data-theme="light"] .cell.safe,html[data-theme="light"] .cell.gem{color:#063664;background:linear-gradient(145deg,#e3fbff,#73d8ff 52%,#168df2);box-shadow:0 16px 30px rgba(33,142,238,.20),inset 0 1px 0 rgba(255,255,255,.82)}
html[data-theme="light"] .cell.mine{color:#fff;background:linear-gradient(145deg,#ff7c7c,#be2740);box-shadow:0 16px 30px rgba(190,39,64,.16)}
html[data-theme="light"] .cta-strip{background:linear-gradient(135deg,rgba(222,245,255,.94),rgba(255,255,255,.78)),repeating-linear-gradient(135deg,rgba(33,142,238,.035) 0 1px,transparent 1px 10px)}
html[data-theme="light"] .promo-code{color:#075fae;border-color:rgba(33,142,238,.46);background:linear-gradient(135deg,rgba(224,246,255,.92),rgba(255,255,255,.76));box-shadow:inset 0 1px 0 rgba(255,255,255,.86),0 18px 38px rgba(33,142,238,.12)}
html[data-theme="light"] .lang-switcher-toggle,html[data-theme="light"] .lang-options{
  background:linear-gradient(180deg,rgba(255,255,255,.96),rgba(231,247,255,.94));
  border-color:rgba(21,112,197,.16);
  box-shadow:0 18px 45px rgba(42,122,190,.13),inset 0 1px 0 rgba(255,255,255,.86);
}
html[data-theme="light"] .lang-options a{color:#213a56;border-color:rgba(33,142,238,.10)}
html[data-theme="light"] .lang-options a:hover{background:rgba(220,243,255,.86)}
html[data-theme="light"] .lang-code{color:#0b65ba}
html[data-theme="light"] .lang-name,html[data-theme="light"] .lang-current small{color:#607a92}
html[data-theme="light"] .lang-current strong{color:#17344f}
html[data-theme="light"] .apk-symbol{color:#fff;background:linear-gradient(135deg,#67d5ff,#168df2 52%,#0a58b8);box-shadow:0 15px 30px rgba(33,142,238,.20)}
html[data-theme="light"] .apk-note{border-color:rgba(33,142,238,.24);background:linear-gradient(145deg,rgba(223,245,255,.92),rgba(255,255,255,.82))}
html[data-theme="light"] .apk-seo li{border-color:rgba(21,112,197,.12);background:rgba(230,247,255,.72)}
html[data-theme="light"] .footer{border-top-color:rgba(21,112,197,.12);background:rgba(244,251,255,.58);color:#607a92}
html[data-theme="light"] .toast{background:linear-gradient(135deg,#67d5ff,#168df2);color:#fff}
html[data-theme="light"] .theme-toggle{
  color:#075fae;
  border-color:rgba(33,142,238,.22);
  background:linear-gradient(135deg,rgba(222,245,255,.92),rgba(255,255,255,.74));
  box-shadow:inset 0 1px 0 rgba(255,255,255,.84),0 12px 26px rgba(33,142,238,.12);
}
html[data-theme="light"] .theme-toggle__icon{color:#fff;background:linear-gradient(135deg,#67d5ff,#168df2)}
@media (max-width:820px){
  .topbar{display:grid;grid-template-columns:1fr;gap:10px;align-items:stretch;padding:12px clamp(12px,4vw,18px)}
  .topbar small,.topbar .btn,.topbar .theme-toggle{width:100%;justify-content:center}
  .theme-toggle{min-height:46px;font-size:12px;padding:10px 12px}
  .theme-toggle__icon{width:22px;height:22px}
  html[data-theme="light"] .sidebar{background:rgba(247,252,255,.94);border-bottom-color:rgba(21,112,197,.14)}
  html[data-theme="light"] .menu-toggle{color:#0b63b6;background:linear-gradient(135deg,rgba(222,245,255,.94),rgba(255,255,255,.76));border-color:rgba(33,142,238,.25)}
  html[data-theme="light"] .menu-toggle span{background:#0b63b6}
  html[data-theme="light"] .sidebar .nav{background:linear-gradient(180deg,rgba(255,255,255,.98),rgba(230,247,255,.96));border-color:rgba(21,112,197,.14)}
  html[data-theme="light"] .sidebar .nav::after{background:linear-gradient(90deg,transparent,rgba(33,142,238,.26),rgba(110,205,255,.18),transparent)}
  html[data-theme="light"] .sidebar .nav a.active::after{background:linear-gradient(135deg,#67d5ff,#168df2);color:#fff}
}
@media (max-width:520px){
  .topbar{gap:8px}
  .theme-toggle{border-radius:16px}
  .theme-toggle__text{font-size:12px}
  html[data-theme="light"] body{background:linear-gradient(180deg,#f8fdff 0%,#eaf7ff 48%,#f7fbff 100%)}
}
'''

theme_js = r'''

(function(){
  const root = document.documentElement;
  const storageKey = 'minesneonTheme';
  const buttons = Array.from(document.querySelectorAll('[data-theme-toggle]'));
  if(!buttons.length) return;
  const meta = document.querySelector('meta[name="theme-color"]');
  function savedTheme(){ try{return localStorage.getItem(storageKey);}catch(e){return null;} }
  function storeTheme(theme){ try{localStorage.setItem(storageKey, theme);}catch(e){} }
  function applyTheme(theme){
    const light = theme === 'light';
    if(light) root.setAttribute('data-theme','light'); else root.removeAttribute('data-theme');
    if(meta) meta.setAttribute('content', light ? '#eef8ff' : '#050403');
    buttons.forEach(function(btn){
      btn.setAttribute('aria-pressed', light ? 'true' : 'false');
      const icon = btn.querySelector('.theme-toggle__icon');
      const text = btn.querySelector('.theme-toggle__text');
      if(icon) icon.textContent = light ? '☾' : '☀';
      if(text) text.textContent = light ? 'Темная тема' : 'Светлая тема';
    });
  }
  applyTheme(savedTheme() === 'light' ? 'light' : 'dark');
  buttons.forEach(function(btn){
    btn.addEventListener('click', function(){
      const next = root.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
      storeTheme(next);
      applyTheme(next);
    });
  });
})();
'''

css = CSS.read_text(encoding='utf-8')
if '/* White & Blue Theme Switcher — design-only override */' not in css:
    CSS.write_text(css.rstrip() + light_theme_css + '\n', encoding='utf-8')

js = JS.read_text(encoding='utf-8')
if 'minesneonTheme' not in js:
    JS.write_text(js.rstrip() + theme_js + '\n', encoding='utf-8')

updated = 0
for page in ROOT.glob('*.html'):
    html = page.read_text(encoding='utf-8')
    if 'data-theme-toggle' in html:
        continue
    marker = '<header class="topbar"><small>'
    if marker not in html:
        continue
    first_close_small = html.find('</small>', html.find(marker))
    if first_close_small == -1:
        continue
    insert_at = first_close_small + len('</small>')
    html = html[:insert_at] + THEME_BUTTON + html[insert_at:]
    page.write_text(html, encoding='utf-8')
    updated += 1

if DEST.exists():
    shutil.rmtree(DEST)
shutil.copytree(ROOT, DEST)

print('white_blue_theme_css=' + str('White & Blue Theme Switcher' in CSS.read_text(encoding='utf-8')))
print('theme_js=' + str('minesneonTheme' in JS.read_text(encoding='utf-8')))
print('html_pages_with_toggle_added=' + str(updated))
print('copied_to=' + str(DEST))
