from pathlib import Path
import shutil

ROOT = Path('mines-seo-site')
CSS = ROOT / 'assets' / 'style.css'
DEST = Path(r'C:\Users\kompy\OneDrive\Desktop\сайт\mines\multilang-site')

keyword_css = r'''

/* Light Theme Bottom Keyword Contrast Fix */
html[data-theme="light"] .seo-block,html[data-theme="light"] .article-content{
  color:#182f45;
}
html[data-theme="light"] .seo-block *,html[data-theme="light"] .article-content *{
  color:inherit;
}
html[data-theme="light"] .seo-block p,html[data-theme="light"] .seo-block li,html[data-theme="light"] .seo-block span,html[data-theme="light"] .seo-block div,html[data-theme="light"] .article-content p,html[data-theme="light"] .article-content li,html[data-theme="light"] .article-content span,html[data-theme="light"] .article-content div{
  color:#182f45;
}
html[data-theme="light"] .seo-block strong,html[data-theme="light"] .article-content strong,html[data-theme="light"] .seo-block b,html[data-theme="light"] .article-content b{
  color:#061b31;
}
html[data-theme="light"] .seo-block h2,html[data-theme="light"] .seo-block h3,html[data-theme="light"] .seo-block h4,html[data-theme="light"] .article-content h2,html[data-theme="light"] .article-content h3,html[data-theme="light"] .article-content h4{
  color:#081522;
}
html[data-theme="light"] .seo-block a,html[data-theme="light"] .article-content a{
  color:#043f78;
}
html[data-theme="light"] .seo-block li::marker,html[data-theme="light"] .article-content li::marker{
  color:#0a579e;
}
html[data-theme="light"] .seo-block code,html[data-theme="light"] .article-content code{
  color:#061b31;
  background:rgba(19,74,119,.10);
  border:1px solid rgba(19,74,119,.16);
}
html[data-theme="light"] .footer,html[data-theme="light"] .footer p,html[data-theme="light"] .footer strong{
  color:#334f66;
}
'''

css = CSS.read_text(encoding='utf-8')
if '/* Light Theme Bottom Keyword Contrast Fix */' not in css:
    CSS.write_text(css.rstrip() + keyword_css + '\n', encoding='utf-8')

if DEST.exists():
    shutil.rmtree(DEST)
shutil.copytree(ROOT, DEST)

print('bottom_keyword_contrast_fix=' + str('Light Theme Bottom Keyword Contrast Fix' in CSS.read_text(encoding='utf-8')))
print('copied_to=' + str(DEST))
