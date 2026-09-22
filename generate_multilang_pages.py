from pathlib import Path
from html import escape
import re
import json

SOURCE_BASE = Path(r'C:\Users\kompy\OneDrive\Desktop\сайт\mines')
OUT = Path('mines-seo-site')
OFFER = 'https://lkzq.cc/644450'
SITE = 'https://minesneon.ru/'

LANGS = {
    'ru': {'label': 'Русский', 'short': 'RU', 'html': 'ru', 'flag': 'https://flagcdn.com/w40/ru.png', 'flag2x': 'https://flagcdn.com/w80/ru.png'},
    'en': {'label': 'English', 'short': 'EN', 'html': 'en', 'flag': 'https://flagcdn.com/w40/gb.png', 'flag2x': 'https://flagcdn.com/w80/gb.png'},
    'es': {'label': 'Español', 'short': 'ES', 'html': 'es', 'flag': 'https://flagcdn.com/w40/es.png', 'flag2x': 'https://flagcdn.com/w80/es.png'},
    'de': {'label': 'Deutsch', 'short': 'DE', 'html': 'de', 'flag': 'https://flagcdn.com/w40/de.png', 'flag2x': 'https://flagcdn.com/w80/de.png'},
    'ph': {'label': 'Filipino', 'short': 'PH', 'html': 'fil', 'flag': 'https://flagcdn.com/w40/ph.png', 'flag2x': 'https://flagcdn.com/w80/ph.png'},
}

SECTIONS = [
    {'dir': 'аналог', 'slug': 'analog', 'labels': {'ru': 'Аналоги', 'en': 'Alternatives', 'es': 'Alternativas', 'de': 'Alternativen', 'ph': 'Mga Alternatibo'}, 'icon': '🧩'},
    {'dir': 'бонус', 'slug': 'bonus', 'labels': {'ru': 'Бонус', 'en': 'Bonus', 'es': 'Bono', 'de': 'Bonus', 'ph': 'Bonus'}, 'icon': '🎁'},
    {'dir': 'главная', 'slug': 'home', 'labels': {'ru': 'Главная', 'en': 'Home', 'es': 'Inicio', 'de': 'Startseite', 'ph': 'Home'}, 'icon': '🏠'},
    {'dir': 'демо', 'slug': 'demo', 'labels': {'ru': 'Демо', 'en': 'Demo', 'es': 'Demo', 'de': 'Demo', 'ph': 'Demo'}, 'icon': '🎮'},
    {'dir': 'промокод', 'slug': 'promocode', 'labels': {'ru': 'Промокод', 'en': 'Promo code', 'es': 'Código promo', 'de': 'Promo-Code', 'ph': 'Promo code'}, 'icon': '💎'},
    {'dir': 'регистрация', 'slug': 'registration', 'labels': {'ru': 'Регистрация', 'en': 'Registration', 'es': 'Registro', 'de': 'Registrierung', 'ph': 'Registration'}, 'icon': '📝'},
    {'dir': 'стратегии', 'slug': 'strategies', 'labels': {'ru': 'Стратегии', 'en': 'Strategies', 'es': 'Estrategias', 'de': 'Strategien', 'ph': 'Mga Strategy'}, 'icon': '📈'},
    {'dir': 'donwload', 'slug': 'download', 'labels': {'ru': 'Скачать', 'en': 'Download', 'es': 'Descargar', 'de': 'Download', 'ph': 'Download'}, 'icon': '📲'},
    {'dir': 'hack', 'slug': 'hack', 'labels': {'ru': 'Предиктор', 'en': 'Predictor', 'es': 'Predictor', 'de': 'Predictor', 'ph': 'Predictor'}, 'icon': '🛡️'},
    {'dir': 'mines игра', 'slug': 'mines-game', 'labels': {'ru': 'Игра Mines', 'en': 'Mines game', 'es': 'Juego Mines', 'de': 'Mines Spiel', 'ph': 'Mines game'}, 'icon': '💣'},
]

UI_TEXT = {
    'ru': {'menu': 'Меню', 'change_lang': 'Сменить язык', 'brand': 'Демо • сигналы • бонус', 'footer': 'информационный сайт и демо-симулятор. Материалы не являются финансовой рекомендацией. Играйте ответственно. 18+.'},
    'en': {'menu': 'Menu', 'change_lang': 'Change language', 'brand': 'Demo • signals • bonus', 'footer': 'informational site and demo simulator. Content is not financial advice. Play responsibly. 18+.'},
    'es': {'menu': 'Menú', 'change_lang': 'Cambiar idioma', 'brand': 'Demo • señales • bono', 'footer': 'sitio informativo y simulador demo. El contenido no es asesoramiento financiero. Juega con responsabilidad. 18+.'},
    'de': {'menu': 'Menü', 'change_lang': 'Sprache ändern', 'brand': 'Demo • Signale • Bonus', 'footer': 'Informationsseite und Demo-Simulator. Inhalte sind keine Finanzberatung. Spielen Sie verantwortungsvoll. 18+.'},
    'ph': {'menu': 'Menu', 'change_lang': 'Palitan ang wika', 'brand': 'Demo • signals • bonus', 'footer': 'informational site at demo simulator. Hindi financial advice ang content. Maglaro nang responsable. 18+.'},
}

CTA_TEXT = {
    'ru': ('ЗАБРАТЬ БОНУС', 'Перейти в казино', 'PIXELWIN: бонус 500%', 'Готовы перейти к реальной игре?', 'Активируйте PIXELWIN и получите бонус до 500%.'),
    'en': ('CLAIM BONUS', 'Go to casino', 'PIXELWIN: 500% bonus', 'Ready to play for real?', 'Activate PIXELWIN and claim up to 500% bonus.'),
    'es': ('OBTENER BONO', 'Ir al casino', 'PIXELWIN: bono 500%', '¿Listo para jugar en real?', 'Activa PIXELWIN y recibe hasta 500% de bono.'),
    'de': ('BONUS HOLEN', 'Zum Casino', 'PIXELWIN: 500% Bonus', 'Bereit fur echtes Spiel?', 'Aktivieren Sie PIXELWIN und erhalten Sie bis zu 500% Bonus.'),
    'ph': ('KUNIN ANG BONUS', 'Pumunta sa casino', 'PIXELWIN: 500% bonus', 'Ready na sa real game?', 'I-activate ang PIXELWIN at kumuha ng hanggang 500% bonus.'),
}

def read_md(path: Path) -> str:
    for enc in ('utf-8-sig', 'utf-8', 'cp1251'):
        try:
            return path.read_text(encoding=enc)
        except UnicodeDecodeError:
            continue
    return path.read_text(errors='ignore')

def normalize_text(text: str) -> str:
    text = text.replace('\ufeff', '').replace('\r\n', '\n').replace('\r', '\n')
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def inline_md(text: str) -> str:
    text = escape(text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
    return text

def md_to_html(md: str) -> tuple[str, str, str]:
    md = normalize_text(md)
    lines = md.split('\n')
    html = []
    title = ''
    description_parts = []
    paragraph = []
    list_items = []
    ordered_items = []

    def flush_paragraph():
        nonlocal paragraph, description_parts
        if paragraph:
            text = ' '.join(x.strip() for x in paragraph if x.strip())
            if text:
                html.append(f'<p>{inline_md(text)}</p>')
                if len(description_parts) < 2 and not text.startswith('#'):
                    description_parts.append(re.sub(r'[*_`#>\-]', '', text))
            paragraph = []

    def flush_list():
        nonlocal list_items, ordered_items
        if list_items:
            html.append('<ul>' + ''.join(f'<li>{inline_md(item)}</li>' for item in list_items) + '</ul>')
            list_items = []
        if ordered_items:
            html.append('<ol>' + ''.join(f'<li>{inline_md(item)}</li>' for item in ordered_items) + '</ol>')
            ordered_items = []

    for raw in lines:
        line = raw.strip()
        if not line:
            flush_paragraph(); flush_list(); continue
        if line == '---':
            flush_paragraph(); flush_list(); html.append('<hr>'); continue
        h = re.match(r'^(#{1,6})\s+(.+)$', line)
        if h:
            flush_paragraph(); flush_list()
            level = min(len(h.group(1)), 4)
            text = h.group(2).strip()
            if level == 1 and not title:
                title = re.sub(r'[*_`]', '', text)
                html.append(f'<h2>{inline_md(text)}</h2>')
            else:
                html.append(f'<h{level}>{inline_md(text)}</h{level}>')
            continue
        bullet = re.match(r'^[-*+]\s+(.+)$', line)
        if bullet:
            flush_paragraph(); ordered_items = []
            list_items.append(bullet.group(1).strip())
            continue
        ordered = re.match(r'^\d+[.)]\s+(.+)$', line)
        if ordered:
            flush_paragraph(); list_items = []
            ordered_items.append(ordered.group(1).strip())
            continue
        paragraph.append(line)

    flush_paragraph(); flush_list()
    desc = ' '.join(description_parts).strip()
    desc = re.sub(r'\s+', ' ', desc)[:158]
    if not title:
        title = desc[:80] or 'Mines'
    return '\n'.join(html), title, desc

def detect_lang(path: Path) -> str:
    m = re.search(r'-(ru|en|es|de|ph)\.md$', path.name, re.I)
    if m:
        return m.group(1).lower()
    return 'ru'

def find_md(section):
    folder = SOURCE_BASE / section['dir']
    return sorted(folder.glob('*.md')) if folder.exists() else []

def page_name(slug, lang):
    return f'{slug}-{lang}.html'

def section_label(section, lang):
    return section.get('labels', {}).get(lang) or section.get('label') or section['slug'].replace('-', ' ').title()


def nav_html(current_slug, current_lang):
    links = []
    for sec in SECTIONS:
        cls = 'active' if sec['slug'] == current_slug else ''
        links.append(f'<a class="{cls}" href="{page_name(sec["slug"], current_lang)}"><span>{sec["icon"]}</span>{escape(section_label(sec, current_lang))}</a>')
    return '\n'.join(links)

def flag_img(lang):
    data = LANGS[lang]
    return f'<img src="{data["flag"]}" srcset="{data["flag2x"]} 2x" width="40" height="30" loading="lazy" alt="{escape(data["label"])} flag">'


def lang_switcher(current_slug, current_lang, available):
    items = []
    for lang in ['ru', 'en', 'es', 'de', 'ph']:
        if lang not in available:
            continue
        data = LANGS[lang]
        cls = 'active' if lang == current_lang else ''
        current = ' aria-current="true"' if lang == current_lang else ''
        items.append(
            f'<a class="{cls}" hreflang="{data["html"]}" href="{page_name(current_slug, lang)}"{current}>'
            f'<span class="lang-flag">{flag_img(lang)}</span><span class="lang-code">{data["short"]}</span><span class="lang-name">{data["label"]}</span></a>'
        )
    active = LANGS[current_lang]
    return (
        '<div class="lang-switcher" data-lang-switcher aria-label="Language switcher">'
        f'<button class="lang-switcher-toggle" type="button" aria-expanded="false">'
        f'<span class="lang-flag">{flag_img(current_lang)}</span><span class="lang-current"><strong>{active["label"]}</strong><small>{escape(UI_TEXT[current_lang]["change_lang"])}</small></span><span class="lang-chevron">⌄</span></button>'
        '<div class="lang-options">' + ''.join(items) + '</div></div>'
    )

def hreflangs(slug, available):
    out = []
    for lang in available:
        out.append(f'  <link rel="alternate" hreflang="{LANGS[lang]["html"]}" href="{SITE}{page_name(slug, lang)}">')
    if 'en' in available:
        out.append(f'  <link rel="alternate" hreflang="x-default" href="{SITE}{page_name(slug, "en")}">')
    return '\n'.join(out)

def render_page(slug, lang, section, title, desc, body_html, available):
    cta = CTA_TEXT[lang]
    canonical = SITE + page_name(slug, lang)
    json_ld = json.dumps({
        '@context': 'https://schema.org',
        '@type': 'Article',
        'headline': title,
        'description': desc,
        'url': canonical,
        'inLanguage': LANGS[lang]['html'],
        'isPartOf': {'@type': 'WebSite', 'name': 'MinesNeon', 'url': SITE},
    }, ensure_ascii=False)
    return f'''<!DOCTYPE html>
<html lang="{LANGS[lang]['html']}" prefix="og: https://ogp.me/ns#">
<head>
  <script type="text/javascript">
    (function(m,e,t,r,i,k,a){{m[i]=m[i]||function(){{(m[i].a=m[i].a||[]).push(arguments)}};m[i].l=1*new Date();for(var j=0;j<document.scripts.length;j++){{if(document.scripts[j].src===r){{return;}}}}k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)}})(window,document,'script','https://mc.yandex.ru/metrika/tag.js?id=106419573','ym');
    ym(106419573,'init',{{ssr:true,webvisor:true,clickmap:true,ecommerce:"dataLayer",referrer:document.referrer,url:location.href,accurateTrackBounce:true,trackLinks:true}});
  </script>
  <noscript><div><img src="https://mc.yandex.ru/watch/106419573" style="position:absolute;left:-9999px;" alt=""></div></noscript>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=5,user-scalable=yes,viewport-fit=cover">
  <title>{escape(title)} | MinesNeon</title>
  <meta name="description" content="{escape(desc)}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <meta name="theme-color" content="#070a12">
  <link rel="canonical" href="{canonical}">
{hreflangs(slug, available)}
  <link rel="stylesheet" href="assets/style.css">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{canonical}">
  <meta property="og:title" content="{escape(title)}">
  <meta property="og:description" content="{escape(desc)}">
  <meta property="og:site_name" content="MinesNeon">
  <script type="application/ld+json">{json_ld}</script>
  <script src="https://analytics.ahrefs.com/analytics.js" data-key="5+Aq5cTCiHoUIdAWGMQ1dg" async></script>
</head>
<body>
  <div class="site">
    <aside class="sidebar" aria-label="Site navigation">
      <a class="brand" href="index.html" aria-label="MinesNeon">
        <span class="brand-logo">💣</span><span><strong>MinesNeon</strong><span>{escape(UI_TEXT[lang]['brand'])}</span></span>
      </a>
      <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav" data-open="{escape(UI_TEXT[lang]['menu'])}" data-close="{escape(UI_TEXT[lang]['menu'])}"><span></span><span></span><span></span><b>{escape(UI_TEXT[lang]['menu'])}</b></button>
      <nav class="nav" id="site-nav">{nav_html(slug, lang)}</nav>
      <div class="side-cta"><b>{escape(cta[2])}</b><a class="btn btn-pulse" href="{OFFER}" rel="nofollow sponsored noopener" target="_blank">{escape(cta[0])}</a></div>
    </aside>
    <main class="main">
      <header class="topbar">
        <small>MinesNeon · {escape(section_label(section, lang))} · {LANGS[lang]['label']}</small>
        <a class="btn btn-pulse" href="{OFFER}" rel="nofollow sponsored noopener" target="_blank">{escape(cta[1])}</a>
      </header>
      <div class="container">
        <section class="hero article-hero">
          <div class="section-kicker">{escape(section_label(section, lang))} • {LANGS[lang]['label']}</div>
          <h1>{escape(title)}</h1>
          <p class="lead">{escape(desc)}</p>
          {lang_switcher(slug, lang, available)}
        </section>
        <article class="seo-block article-content">
          {body_html}
        </article>
        <section class="cta-strip" aria-label="Casino offer">
          <div><strong>{escape(cta[3])}</strong><span>{escape(cta[4])}</span></div>
          <a class="btn btn-pulse" href="{OFFER}" rel="nofollow sponsored noopener" target="_blank">{escape(cta[0])}</a>
        </section>
      </div>
      <footer class="footer"><p><strong>MinesNeon</strong> — {escape(UI_TEXT[lang]['footer'])}</p></footer>
    </main>
  </div>
  <script src="assets/app.js" defer></script>
</body>
</html>
'''

def main():
    generated = []
    for section in SECTIONS:
        files = find_md(section)
        by_lang = {detect_lang(p): p for p in files}
        available = [l for l in ['ru', 'en', 'es', 'de', 'ph'] if l in by_lang]
        for lang, path in by_lang.items():
            body, title, desc = md_to_html(read_md(path))
            if not desc:
                desc = title
            out = OUT / page_name(section['slug'], lang)
            out.write_text(render_page(section['slug'], lang, section, title, desc, body, available), encoding='utf-8')
            generated.append(out)
    print(f'generated={len(generated)}')
    for p in generated:
        print(p.as_posix())

if __name__ == '__main__':
    main()
