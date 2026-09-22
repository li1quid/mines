from pathlib import Path
import shutil

ROOT = Path('mines-seo-site')
CSS = ROOT / 'assets' / 'style.css'

black_gold_css = r'''

/* Black & Gold Premium Theme — design-only override */
:root{
  --bg:#050403;
  --bg-2:#0c0905;
  --surface:#120e08;
  --surface-2:#191208;
  --surface-3:#231809;
  --glass:rgba(18,14,8,.76);
  --glass-strong:rgba(22,16,9,.90);
  --line:rgba(255,214,128,.16);
  --line-strong:rgba(255,214,128,.30);
  --text:#fff8e7;
  --text-soft:#f6e7c4;
  --muted:#c8b88f;
  --muted-2:#8f805f;
  --primary:#f6c85f;
  --primary-2:#ffe6a3;
  --violet:#9b6b2f;
  --pink:#d09a3d;
  --gold:#ffd36a;
  --danger:#d95f45;
  --success:#d7b56d;
  --shadow-xl:0 34px 100px rgba(0,0,0,.70);
  --shadow:0 24px 70px rgba(0,0,0,.54);
  --shadow-soft:0 14px 38px rgba(0,0,0,.38);
}
html{background:#050403}
body{
  color:var(--text);
  background:
    radial-gradient(circle at 12% -10%,rgba(255,211,106,.18),transparent 32rem),
    radial-gradient(circle at 88% 2%,rgba(168,111,35,.18),transparent 34rem),
    radial-gradient(circle at 54% 42%,rgba(255,214,128,.07),transparent 30rem),
    linear-gradient(180deg,#050403 0%,#0c0905 46%,#030302 100%);
}
body::before{
  background:
    radial-gradient(circle at 20% 20%,rgba(255,255,255,.035) 0 1px,transparent 1.4px),
    linear-gradient(rgba(255,214,128,.024) 1px,transparent 1px),
    linear-gradient(90deg,rgba(255,214,128,.020) 1px,transparent 1px);
  background-size:18px 18px,48px 48px,48px 48px;
  opacity:.88;
  mask-image:linear-gradient(180deg,rgba(0,0,0,.92),rgba(0,0,0,.58) 52%,transparent 92%);
}
body::after{
  background:
    radial-gradient(circle at 50% 0%,rgba(255,229,164,.13),transparent 36rem),
    linear-gradient(115deg,transparent 0 36%,rgba(255,211,106,.045) 45%,transparent 56% 100%);
  mix-blend-mode:screen;
}
a{color:#ffdc83}.seo-block a,.article-content a{color:#ffe2a0;font-weight:900}
.sidebar{
  border-right-color:rgba(255,214,128,.17);
  background:
    linear-gradient(180deg,rgba(12,9,5,.92),rgba(8,6,4,.80)),
    repeating-linear-gradient(135deg,rgba(255,214,128,.035) 0 1px,transparent 1px 9px);
  box-shadow:18px 0 70px rgba(0,0,0,.35);
}
.sidebar::before{
  background:radial-gradient(circle at 30% 15%,rgba(255,214,128,.20),transparent 62%),linear-gradient(135deg,rgba(255,214,128,.10),rgba(105,68,22,.08));
  border:1px solid rgba(255,214,128,.10);
}
.brand-logo{
  color:#120b03;
  background:linear-gradient(135deg,#fff1b8 0%,#f6c85f 42%,#9c661f 100%);
  box-shadow:0 18px 46px rgba(246,200,95,.22),inset 0 1px 0 rgba(255,255,255,.65),inset 0 -12px 22px rgba(83,48,8,.22);
}
.brand-logo::after{border-color:rgba(255,214,128,.28);box-shadow:0 0 24px rgba(255,214,128,.12)}
.brand strong{color:#fff6dd}.brand span span{color:#bfae82}
.nav a,.nav-subtoggle{
  color:#f4e9ce;
  background:linear-gradient(135deg,rgba(255,214,128,.055),rgba(255,255,255,.018));
  border-color:rgba(255,214,128,.08);
}
.nav a span,.nav-subtoggle span{background:rgba(255,214,128,.085);box-shadow:inset 0 1px 0 rgba(255,255,255,.08)}
.nav a.active,.nav a:hover,.nav-subtoggle:hover,.nav-group.open .nav-subtoggle{
  color:#fff9ea;
  border-color:rgba(255,214,128,.32);
  background:linear-gradient(135deg,rgba(255,214,128,.18),rgba(120,75,20,.16));
  box-shadow:inset 0 1px 0 rgba(255,255,255,.08),0 16px 34px rgba(0,0,0,.25),0 0 28px rgba(255,214,128,.07);
}
.nav a.active::before{background:linear-gradient(180deg,#fff0b2,#f6c85f,#9d651d)}
.nav-submenu{background:linear-gradient(180deg,rgba(10,7,4,.72),rgba(20,14,7,.62));border-color:rgba(255,214,128,.14)}
.side-cta{
  border-color:rgba(255,214,128,.32);
  background:linear-gradient(145deg,rgba(255,214,128,.17),rgba(54,34,9,.20)),repeating-linear-gradient(135deg,rgba(255,255,255,.035) 0 1px,transparent 1px 10px);
}
.side-cta::before{background:rgba(255,214,128,.24)}
.topbar{
  border-bottom-color:rgba(255,214,128,.16);
  background:rgba(7,5,3,.72);
  box-shadow:0 14px 40px rgba(0,0,0,.28);
}
.topbar small{color:#e9d7ad}.topbar small::before{background:linear-gradient(135deg,rgba(255,214,128,.22),rgba(154,98,27,.18));border-color:rgba(255,214,128,.34);color:#ffe6a3}
.hero::after{background:linear-gradient(90deg,#fff0b2,#f6c85f,#8e5c1d,transparent)}
.section-kicker,.badge{
  color:#ffe6a3;
  border-color:rgba(255,214,128,.28);
  background:linear-gradient(135deg,rgba(255,214,128,.14),rgba(90,58,18,.10));
  box-shadow:inset 0 1px 0 rgba(255,255,255,.08),0 10px 28px rgba(0,0,0,.18);
}
h1,h2,.card h2,.panel h2{color:#fff7df;text-shadow:0 2px 28px rgba(255,214,128,.08)}
p,.lead,.seo-block p,.article-content p{color:#eadbbc}.lead{color:#d6c49b}
.btn-pulse,.btn-main,.lang-switcher a.active,.lang-switcher a:hover,.lang-switcher-toggle:hover,.lang-switcher.open .lang-switcher-toggle{
  color:#130c03;
  background:linear-gradient(135deg,#fff3bd 0%,#f6c85f 44%,#b97922 100%);
  box-shadow:0 16px 40px rgba(246,200,95,.22),0 0 0 0 rgba(246,200,95,.28),inset 0 1px 0 rgba(255,255,255,.72),inset 0 -14px 24px rgba(96,56,9,.18);
}
.btn-ghost{color:#ffefc4;background:rgba(255,214,128,.065);border-color:rgba(255,214,128,.22)}
.panel,.card,.seo-block,.cta-strip,.faq-list details,.apk-guide-card{
  border-color:rgba(255,214,128,.16);
  background:
    linear-gradient(180deg,rgba(255,214,128,.070),rgba(255,255,255,.020)),
    repeating-linear-gradient(135deg,rgba(255,255,255,.018) 0 1px,transparent 1px 12px),
    linear-gradient(145deg,rgba(24,17,9,.94),rgba(8,6,4,.94));
  box-shadow:0 26px 76px rgba(0,0,0,.55),inset 0 1px 0 rgba(255,255,255,.07);
}
.panel::before,.card::before,.seo-block::before,.cta-strip::before{
  background:linear-gradient(135deg,rgba(255,235,179,.28),rgba(180,113,32,.12),rgba(255,255,255,0));
}
.game-panel::after,.signal-panel::after,.promo-hero::after,.apk-guide-card::after{background:radial-gradient(circle,rgba(255,214,128,.15),transparent 68%)}
.game-toolbar input,.game-toolbar select{
  color:#fff7e4;
  background:rgba(7,5,3,.68);
  border-color:rgba(255,214,128,.18);
}
.game-toolbar input:focus,.game-toolbar select:focus{border-color:rgba(255,214,128,.58);box-shadow:0 0 0 4px rgba(255,214,128,.10),inset 0 1px 0 rgba(255,255,255,.06)}
.mult{color:#ffe6a3;background:linear-gradient(135deg,rgba(255,214,128,.16),rgba(110,68,17,.10));border-color:rgba(255,214,128,.20)}
.cell{
  border-color:rgba(255,214,128,.13);
  background:radial-gradient(circle at 28% 20%,rgba(255,232,172,.10),transparent 32%),linear-gradient(145deg,#22170a,#0b0804 72%);
  box-shadow:inset 0 -10px 18px rgba(0,0,0,.36),inset 0 1px 0 rgba(255,255,255,.07),0 11px 22px rgba(0,0,0,.30);
}
.cell:hover{border-color:rgba(255,214,128,.36);box-shadow:inset 0 -10px 18px rgba(0,0,0,.36),0 14px 30px rgba(246,200,95,.11)}
.cell.safe,.cell.gem{color:#120b03;background:linear-gradient(145deg,#fff1b2,#f6c85f 52%,#b87721);box-shadow:0 16px 32px rgba(246,200,95,.22),inset 0 1px 0 rgba(255,255,255,.58)}
.cell.mine{background:linear-gradient(145deg,#c85a3c,#572111);box-shadow:0 16px 32px rgba(200,90,60,.17)}
.cta-strip{background:linear-gradient(135deg,rgba(255,214,128,.18),rgba(96,59,13,.18)),repeating-linear-gradient(135deg,rgba(255,255,255,.025) 0 1px,transparent 1px 10px)}
.promo-code{color:#ffdf87;border-color:rgba(255,214,128,.68);background:linear-gradient(135deg,rgba(255,214,128,.16),rgba(255,255,255,.03));box-shadow:inset 0 1px 0 rgba(255,255,255,.10),0 18px 40px rgba(246,200,95,.12)}
.lang-switcher-toggle,.lang-options{
  background:linear-gradient(180deg,rgba(20,14,7,.96),rgba(9,7,4,.94));
  border-color:rgba(255,214,128,.22);
  box-shadow:0 20px 54px rgba(0,0,0,.40),inset 0 1px 0 rgba(255,255,255,.06);
}
.lang-options a{color:#f1e2c0;border-color:rgba(255,214,128,.10)}
.lang-options a:hover{background:rgba(255,214,128,.10)}
.lang-code{color:#ffdc83}.lang-name,.lang-current small{color:#bfae82}.lang-current strong{color:#fff3d0}
.apk-symbol{color:#130c03;background:linear-gradient(135deg,#fff3bd,#f6c85f 52%,#a96b1d);box-shadow:0 15px 30px rgba(246,200,95,.22)}
.apk-note{border-color:rgba(255,214,128,.28);background:linear-gradient(145deg,rgba(255,214,128,.13),rgba(22,15,8,.94))}
.apk-seo li{border-color:rgba(255,214,128,.13);background:rgba(255,214,128,.045)}
.footer{border-top-color:rgba(255,214,128,.14);background:rgba(4,3,2,.42);color:#bfae82}
.toast{background:linear-gradient(135deg,#fff3bd,#f6c85f);color:#120b03}
@keyframes pulseLux{
  0%{box-shadow:0 16px 40px rgba(246,200,95,.22),0 0 0 0 rgba(246,200,95,.26),inset 0 1px 0 rgba(255,255,255,.60)}
  68%{box-shadow:0 16px 40px rgba(246,200,95,.22),0 0 0 12px rgba(246,200,95,0),inset 0 1px 0 rgba(255,255,255,.60)}
  100%{box-shadow:0 16px 40px rgba(246,200,95,.22),0 0 0 0 rgba(246,200,95,0),inset 0 1px 0 rgba(255,255,255,.60)}
}
@media (max-width:820px){
  .sidebar{background:rgba(7,5,3,.93);border-bottom-color:rgba(255,214,128,.16)}
  .menu-toggle{color:#fff1c6;background:linear-gradient(135deg,rgba(255,214,128,.13),rgba(116,72,19,.12));border-color:rgba(255,214,128,.28)}
  .sidebar .nav{background:linear-gradient(180deg,rgba(18,13,7,.97),rgba(8,6,4,.96));border-color:rgba(255,214,128,.16)}
  .sidebar .nav::after{background:linear-gradient(90deg,transparent,rgba(255,214,128,.30),rgba(128,78,20,.18),transparent)}
  .sidebar .nav a.active::after{background:linear-gradient(135deg,#fff3bd,#f6c85f);color:#130c03}
}
'''

css = CSS.read_text(encoding='utf-8')
if '/* Black & Gold Premium Theme — design-only override */' not in css:
    CSS.write_text(css.rstrip() + black_gold_css + '\n', encoding='utf-8')

# Copy updated design version without changing page information.
dest = Path(r'C:\Users\kompy\OneDrive\Desktop\сайт\mines\multilang-site')
if dest.exists():
    shutil.rmtree(dest)
shutil.copytree(ROOT, dest)

print('black_gold_design_applied=true')
print('html_files_unchanged_by_script=true')
print('css_has_black_gold=' + str('Black & Gold Premium Theme' in CSS.read_text(encoding='utf-8')))
print('copied_to=' + str(dest))
