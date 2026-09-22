from pathlib import Path

root = Path('mines-seo-site')
css_path = root / 'assets' / 'style.css'
generator_path = root / 'generate_pages.py'

append = r'''

/* Multilingual article pages */
.article-hero{padding-bottom:22px}
.lang-switcher{
  display:flex;
  flex-wrap:wrap;
  gap:10px;
  margin-top:22px;
}
.lang-switcher a{
  min-height:44px;
  display:inline-flex;
  align-items:center;
  gap:8px;
  padding:9px 13px;
  border:1px solid rgba(226,232,240,.14);
  border-radius:999px;
  color:#d8e4f4;
  background:rgba(255,255,255,.045);
  font-weight:950;
  box-shadow:inset 0 1px 0 rgba(255,255,255,.045);
}
.lang-switcher a span{color:#9daac0;font-size:12px;font-weight:750;text-transform:none}
.lang-switcher a.active,
.lang-switcher a:hover{
  color:#06101d;
  background:linear-gradient(135deg,#5cf0c3,#6ee7f9 48%,#9a8cff);
  border-color:transparent;
  text-decoration:none;
  box-shadow:0 12px 28px rgba(84,240,193,.18),inset 0 1px 0 rgba(255,255,255,.38);
}
.lang-switcher a.active span,
.lang-switcher a:hover span{color:#102033}
.article-content{font-size:17px;line-height:1.72}
.article-content h2:first-child{margin-top:0}
.article-content h2,.article-content h3,.article-content h4{margin-top:30px}
.article-content h3{font-size:clamp(20px,2.3vw,28px);line-height:1.18;letter-spacing:-.03em;color:#fff}
.article-content h4{font-size:20px;color:#edf5ff}
.article-content hr{height:1px;border:0;margin:28px 0;background:linear-gradient(90deg,transparent,rgba(84,240,193,.28),rgba(139,124,255,.18),transparent)}
.article-content ol,.article-content ul{padding-left:24px}
.article-content li::marker{color:#7cf4d2}
.article-content code{padding:2px 6px;border-radius:8px;background:rgba(255,255,255,.08);color:#9af6df}
@media (max-width:640px){
  .lang-switcher{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px;margin-top:18px}
  .lang-switcher a{justify-content:center;width:100%;padding:9px 10px}
  .lang-switcher a span{display:none}
  .article-content{font-size:16px;line-height:1.68}
  .article-content h2,.article-content h3,.article-content h4{margin-top:24px}
}
'''

css = css_path.read_text(encoding='utf-8')
if '/* Multilingual article pages */' not in css:
    css = css.rstrip() + append + '\n'
    css_path.write_text(css, encoding='utf-8')

# Keep the old generator synchronized without breaking the Python raw triple-quoted string.
if generator_path.exists():
    s = generator_path.read_text(encoding='utf-8')
    start = s.find("style = r'''")
    end = s.find('app_js =', start)
    if start != -1 and end != -1:
        before = s[:start]
        after = s[end:]
        generator_path.write_text(before + "style = r'''\n" + css.rstrip() + "\n'''\n\n" + after, encoding='utf-8')

print('multilang_css_synced=true')
