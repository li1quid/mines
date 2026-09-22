from pathlib import Path
import shutil

ROOT = Path('mines-seo-site')
CSS = ROOT / 'assets' / 'style.css'
DEST = Path(r'C:\Users\kompy\OneDrive\Desktop\сайт\mines\multilang-site')

contrast_css = r'''

/* Readable Light Theme Contrast Fix — calmer white-blue palette */
html[data-theme="light"]{
  background:#dcebf6;
}
html[data-theme="light"] body{
  color:#0b1828;
  background:
    radial-gradient(circle at 10% -12%,rgba(42,128,204,.12),transparent 30rem),
    radial-gradient(circle at 92% 0%,rgba(75,156,220,.10),transparent 34rem),
    linear-gradient(180deg,#eaf4fb 0%,#d9eaf5 46%,#e8f2f8 100%);
}
html[data-theme="light"] body::before{
  background:
    linear-gradient(rgba(20,84,136,.040) 1px,transparent 1px),
    linear-gradient(90deg,rgba(20,84,136,.035) 1px,transparent 1px);
  background-size:52px 52px;
  opacity:.52;
  mask-image:linear-gradient(180deg,rgba(0,0,0,.42),transparent 86%);
}
html[data-theme="light"] body::after{
  background:radial-gradient(circle at 50% -8%,rgba(255,255,255,.38),transparent 30rem);
  opacity:.42;
}
html[data-theme="light"] a{color:#064f95}
html[data-theme="light"] .seo-block a,html[data-theme="light"] .article-content a{color:#043f78}
html[data-theme="light"] .sidebar{
  border-right-color:rgba(19,74,119,.18);
  background:
    linear-gradient(180deg,rgba(229,241,249,.96),rgba(207,225,237,.92)),
    repeating-linear-gradient(135deg,rgba(19,91,150,.035) 0 1px,transparent 1px 12px);
  box-shadow:16px 0 46px rgba(28,70,104,.12);
}
html[data-theme="light"] .sidebar::before{
  background:linear-gradient(135deg,rgba(184,215,236,.56),rgba(216,231,241,.42));
  border-color:rgba(24,92,148,.16);
}
html[data-theme="light"] .brand,html[data-theme="light"] .brand strong{color:#0b1828}
html[data-theme="light"] .brand span span{color:#405d76}
html[data-theme="light"] .brand-logo{
  background:linear-gradient(135deg,#2f98df 0%,#156eb8 54%,#0a3f79 100%);
  box-shadow:0 14px 30px rgba(20,94,160,.20),inset 0 1px 0 rgba(255,255,255,.42);
}
html[data-theme="light"] .nav a,html[data-theme="light"] .nav-subtoggle{
  color:#18324a;
  background:linear-gradient(135deg,rgba(239,246,250,.82),rgba(214,229,239,.76));
  border-color:rgba(20,84,136,.15);
}
html[data-theme="light"] .nav a span,html[data-theme="light"] .nav-subtoggle span{background:rgba(20,104,178,.10);color:#0a579e}
html[data-theme="light"] .nav a.active,html[data-theme="light"] .nav a:hover,html[data-theme="light"] .nav-subtoggle:hover,html[data-theme="light"] .nav-group.open .nav-subtoggle{
  color:#082a4f;
  border-color:rgba(16,92,158,.34);
  background:linear-gradient(135deg,rgba(207,229,242,.94),rgba(236,246,251,.86));
  box-shadow:inset 0 1px 0 rgba(255,255,255,.62),0 12px 24px rgba(30,89,136,.13);
}
html[data-theme="light"] .nav-submenu{
  background:linear-gradient(180deg,rgba(229,241,249,.95),rgba(210,229,241,.92));
  border-color:rgba(20,84,136,.16);
}
html[data-theme="light"] .side-cta{
  color:#112a42;
  border-color:rgba(16,92,158,.24);
  background:linear-gradient(145deg,rgba(222,236,246,.94),rgba(204,223,236,.86));
}
html[data-theme="light"] .topbar{
  border-bottom-color:rgba(19,74,119,.16);
  background:rgba(225,239,248,.90);
  box-shadow:0 12px 30px rgba(28,70,104,.11);
}
html[data-theme="light"] .topbar small{color:#24445f}
html[data-theme="light"] .topbar small::before{
  color:#074d8d;
  background:linear-gradient(135deg,rgba(207,229,242,.96),rgba(239,246,250,.88));
  border-color:rgba(16,92,158,.24);
}
html[data-theme="light"] .section-kicker,html[data-theme="light"] .badge{
  color:#074d8d;
  border-color:rgba(16,92,158,.24);
  background:linear-gradient(135deg,rgba(207,229,242,.92),rgba(235,244,249,.82));
}
html[data-theme="light"] h1,html[data-theme="light"] h2,html[data-theme="light"] h3,html[data-theme="light"] .card h2,html[data-theme="light"] .panel h2{
  color:#081522;
  text-shadow:none;
}
html[data-theme="light"] p,html[data-theme="light"] li,html[data-theme="light"] .lead,html[data-theme="light"] .seo-block p,html[data-theme="light"] .article-content p{
  color:#182f45;
}
html[data-theme="light"] .lead{color:#273f56}
html[data-theme="light"] .muted,html[data-theme="light"] small{color:#4b647a}
html[data-theme="light"] .btn-pulse,html[data-theme="light"] .btn-main,html[data-theme="light"] .lang-switcher a.active,html[data-theme="light"] .lang-switcher a:hover,html[data-theme="light"] .lang-switcher-toggle:hover,html[data-theme="light"] .lang-switcher.open .lang-switcher-toggle{
  color:#fff;
  background:linear-gradient(135deg,#2d9be0 0%,#126bb6 52%,#083f7b 100%);
  box-shadow:0 12px 26px rgba(18,96,164,.24),inset 0 1px 0 rgba(255,255,255,.36);
}
html[data-theme="light"] .btn-ghost{
  color:#064f95;
  background:rgba(219,235,246,.82);
  border-color:rgba(16,92,158,.25);
}
html[data-theme="light"] .panel,html[data-theme="light"] .card,html[data-theme="light"] .seo-block,html[data-theme="light"] .cta-strip,html[data-theme="light"] .faq-list details,html[data-theme="light"] .apk-guide-card{
  border-color:rgba(19,74,119,.17);
  background:
    linear-gradient(180deg,rgba(236,245,250,.95),rgba(217,232,242,.90)),
    repeating-linear-gradient(135deg,rgba(19,91,150,.030) 0 1px,transparent 1px 13px);
  box-shadow:0 18px 44px rgba(35,80,115,.13),inset 0 1px 0 rgba(255,255,255,.60);
}
html[data-theme="light"] .panel::before,html[data-theme="light"] .card::before,html[data-theme="light"] .seo-block::before,html[data-theme="light"] .cta-strip::before{
  background:linear-gradient(135deg,rgba(125,178,216,.18),rgba(255,255,255,.34),rgba(255,255,255,0));
}
html[data-theme="light"] .game-toolbar input,html[data-theme="light"] .game-toolbar select{
  color:#10283f;
  background:rgba(233,242,248,.96);
  border-color:rgba(19,74,119,.20);
}
html[data-theme="light"] .mult{
  color:#064f95;
  background:linear-gradient(135deg,rgba(213,232,244,.94),rgba(235,244,249,.86));
  border-color:rgba(16,92,158,.22);
}
html[data-theme="light"] .cell{
  border-color:rgba(19,74,119,.18);
  background:linear-gradient(145deg,#d6e8f3,#eef6fa 72%);
  box-shadow:inset 0 -8px 16px rgba(35,80,115,.08),inset 0 1px 0 rgba(255,255,255,.62),0 9px 18px rgba(35,80,115,.10);
}
html[data-theme="light"] .cell.safe,html[data-theme="light"] .cell.gem{
  color:#062744;
  background:linear-gradient(145deg,#bfe3f5,#5fb9ea 55%,#126bb6);
}
html[data-theme="light"] .promo-code{
  color:#064f95;
  border-color:rgba(16,92,158,.38);
  background:linear-gradient(135deg,rgba(213,232,244,.94),rgba(238,246,250,.88));
}
html[data-theme="light"] .lang-switcher-toggle,html[data-theme="light"] .lang-options{
  background:linear-gradient(180deg,rgba(236,245,250,.98),rgba(216,232,242,.96));
  border-color:rgba(19,74,119,.18);
  box-shadow:0 14px 34px rgba(35,80,115,.13),inset 0 1px 0 rgba(255,255,255,.62);
}
html[data-theme="light"] .lang-options a{color:#18324a;border-color:rgba(19,74,119,.12)}
html[data-theme="light"] .lang-code{color:#074d8d}
html[data-theme="light"] .lang-name,html[data-theme="light"] .lang-current small{color:#4b647a}
html[data-theme="light"] .lang-current strong{color:#10283f}
html[data-theme="light"] .apk-symbol{
  background:linear-gradient(135deg,#2d9be0,#126bb6 55%,#083f7b);
  box-shadow:0 12px 24px rgba(18,96,164,.22);
}
html[data-theme="light"] .apk-note{border-color:rgba(16,92,158,.24);background:linear-gradient(145deg,rgba(216,232,242,.94),rgba(235,244,249,.88))}
html[data-theme="light"] .apk-seo li{border-color:rgba(19,74,119,.14);background:rgba(221,235,244,.84)}
html[data-theme="light"] .footer{border-top-color:rgba(19,74,119,.16);background:rgba(219,235,246,.66);color:#4b647a}
html[data-theme="light"] .theme-toggle{
  color:#074d8d;
  border-color:rgba(16,92,158,.26);
  background:linear-gradient(135deg,rgba(213,232,244,.94),rgba(236,245,250,.86));
}
@media (max-width:820px){
  html[data-theme="light"] .sidebar{background:rgba(225,239,248,.96);border-bottom-color:rgba(19,74,119,.16)}
  html[data-theme="light"] .menu-toggle{color:#074d8d;background:linear-gradient(135deg,rgba(213,232,244,.96),rgba(236,245,250,.88));border-color:rgba(16,92,158,.28)}
  html[data-theme="light"] .sidebar .nav{background:linear-gradient(180deg,rgba(232,242,248,.98),rgba(210,229,241,.97));border-color:rgba(19,74,119,.16)}
}
@media (max-width:520px){
  html[data-theme="light"] body{background:linear-gradient(180deg,#eaf4fb 0%,#d9eaf5 48%,#e8f2f8 100%)}
}
'''

css = CSS.read_text(encoding='utf-8')
if '/* Readable Light Theme Contrast Fix' not in css:
    CSS.write_text(css.rstrip() + contrast_css + '\n', encoding='utf-8')

if DEST.exists():
    shutil.rmtree(DEST)
shutil.copytree(ROOT, DEST)

print('readable_light_theme_fix=' + str('Readable Light Theme Contrast Fix' in CSS.read_text(encoding='utf-8')))
print('copied_to=' + str(DEST))
