from pathlib import Path
import re

ROOT = Path('mines-seo-site')

CORE = {
    'ru': [
        ('index.html', '🎮', 'Демо + сигналы'),
        ('promo.html', '💎', 'Промокод 500%'),
        ('strategies.html', '📈', 'Стратегии'),
        ('faq.html', '❓', 'FAQ'),
        ('apk.html', '📲', 'Скачать APK'),
    ],
    'en': [
        ('index.html', '🎮', 'Demo + signals'),
        ('promo.html', '💎', 'Promo 500%'),
        ('strategies.html', '📈', 'Strategies'),
        ('faq.html', '❓', 'FAQ'),
        ('apk.html', '📲', 'Download APK'),
    ],
    'es': [
        ('index.html', '🎮', 'Demo + señales'),
        ('promo.html', '💎', 'Promo 500%'),
        ('strategies.html', '📈', 'Estrategias'),
        ('faq.html', '❓', 'FAQ'),
        ('apk.html', '📲', 'Descargar APK'),
    ],
    'de': [
        ('index.html', '🎮', 'Demo + Signale'),
        ('promo.html', '💎', 'Promo 500%'),
        ('strategies.html', '📈', 'Strategien'),
        ('faq.html', '❓', 'FAQ'),
        ('apk.html', '📲', 'APK Download'),
    ],
    'ph': [
        ('index.html', '🎮', 'Demo + signals'),
        ('promo.html', '💎', 'Promo 500%'),
        ('strategies.html', '📈', 'Mga strategy'),
        ('faq.html', '❓', 'FAQ'),
        ('apk.html', '📲', 'Download APK'),
    ],
}

GUIDES = [
    ('home', '🏠', {'ru': 'Главная', 'en': 'Home', 'es': 'Inicio', 'de': 'Startseite', 'ph': 'Home'}),
    ('demo', '🎮', {'ru': 'Демо', 'en': 'Demo', 'es': 'Demo', 'de': 'Demo', 'ph': 'Demo'}),
    ('bonus', '🎁', {'ru': 'Бонус', 'en': 'Bonus', 'es': 'Bono', 'de': 'Bonus', 'ph': 'Bonus'}),
    ('promocode', '💎', {'ru': 'Промокод', 'en': 'Promo code', 'es': 'Código promo', 'de': 'Promo-Code', 'ph': 'Promo code'}),
    ('registration', '📝', {'ru': 'Регистрация', 'en': 'Registration', 'es': 'Registro', 'de': 'Registrierung', 'ph': 'Registration'}),
    ('strategies', '📈', {'ru': 'Стратегии гайда', 'en': 'Guide strategies', 'es': 'Estrategias guía', 'de': 'Guide-Strategien', 'ph': 'Guide strategies'}),
    ('download', '📲', {'ru': 'Скачать', 'en': 'Download', 'es': 'Descargar', 'de': 'Download', 'ph': 'Download'}),
    ('analog', '🧩', {'ru': 'Аналоги', 'en': 'Alternatives', 'es': 'Alternativas', 'de': 'Alternativen', 'ph': 'Mga alternatibo'}),
    ('hack', '🛡️', {'ru': 'Предиктор', 'en': 'Predictor', 'es': 'Predictor', 'de': 'Predictor', 'ph': 'Predictor'}),
    ('mines-game', '💣', {'ru': 'Игра Mines', 'en': 'Mines game', 'es': 'Juego Mines', 'de': 'Mines Spiel', 'ph': 'Mines game'}),
]

UI = {
    'ru': {'guides': 'Гайды', 'open': 'Открыть гайды', 'close': 'Скрыть гайды'},
    'en': {'guides': 'Guides', 'open': 'Open guides', 'close': 'Hide guides'},
    'es': {'guides': 'Guías', 'open': 'Abrir guías', 'close': 'Ocultar guías'},
    'de': {'guides': 'Guides', 'open': 'Guides öffnen', 'close': 'Guides ausblenden'},
    'ph': {'guides': 'Guides', 'open': 'Buksan ang guides', 'close': 'Itago ang guides'},
}

NAV_RE = re.compile(r'<nav class="nav" id="site-nav">.*?</nav>', re.S)
PAGE_LANG_RE = re.compile(r'^(.+)-(ru|en|es|de|ph)\.html$')


def detect(path: Path) -> tuple[str, str | None]:
    match = PAGE_LANG_RE.match(path.name)
    if match:
        return match.group(2), match.group(1)
    return 'ru', None


def guide_href(slug: str, lang: str) -> str:
    target = ROOT / f'{slug}-{lang}.html'
    if target.exists():
        return f'{slug}-{lang}.html'
    if (ROOT / f'{slug}-en.html').exists():
        return f'{slug}-en.html'
    return 'home-en.html'


def build_nav(current_file: str, lang: str, current_slug: str | None) -> str:
    core_links = []
    for href, icon, label in CORE.get(lang, CORE['en']):
        cls = 'active' if href == current_file else ''
        core_links.append(f'<a class="{cls}" href="{href}"><span>{icon}</span>{label}</a>')

    guide_active = current_slug is not None
    guide_links = []
    for slug, icon, labels in GUIDES:
        href = guide_href(slug, lang)
        cls = 'active' if current_slug == slug else ''
        label = labels.get(lang, labels['en'])
        guide_links.append(f'<a class="{cls}" href="{href}"><span>{icon}</span>{label}</a>')

    ui = UI.get(lang, UI['en'])
    group_cls = 'nav-group guides-group open' if guide_active else 'nav-group guides-group'
    expanded = 'true' if guide_active else 'false'
    return (
        '<nav class="nav" id="site-nav">' + '\n'.join(core_links) + '\n'
        f'<div class="{group_cls}">'
        f'<button class="nav-subtoggle" type="button" aria-expanded="{expanded}" data-open="{ui["open"]}" data-close="{ui["close"]}"><span>📚</span><b>{ui["guides"]}</b><i>⌄</i></button>'
        '<div class="nav-submenu">' + '\n'.join(guide_links) + '</div></div></nav>'
    )


def main() -> None:
    updated = 0
    for path in ROOT.glob('*.html'):
        text = path.read_text(encoding='utf-8-sig')
        lang, slug = detect(path)
        nav = build_nav(path.name, lang, slug)
        new_text = NAV_RE.sub(nav, text, count=1)
        if new_text != text:
            path.write_text(new_text, encoding='utf-8')
            updated += 1
    print(f'updated {updated} html files')


if __name__ == '__main__':
    main()
