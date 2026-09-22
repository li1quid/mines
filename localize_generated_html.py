from pathlib import Path
import re

ROOT = Path('mines-seo-site')

LANG_UI = {
    'en': {
        'menu': 'Menu',
        'change': 'Change language',
        'brand': 'Demo • signals • bonus',
        'footer': 'informational site and demo simulator. Content is not financial advice. Play responsibly. 18+.',
        'labels': {
            'Аналоги': 'Alternatives',
            'Бонус': 'Bonus',
            'Главная': 'Home',
            'Демо': 'Demo',
            'Промокод': 'Promo code',
            'Регистрация': 'Registration',
            'Стратегии': 'Strategies',
            'Скачать': 'Download',
            'Download': 'Download',
            'Predictor': 'Predictor',
            'Mines игра': 'Mines game',
            'Игра Mines': 'Mines game',
        },
    },
    'es': {
        'menu': 'Menú',
        'change': 'Cambiar idioma',
        'brand': 'Demo • señales • bono',
        'footer': 'sitio informativo y simulador demo. El contenido no es asesoramiento financiero. Juega con responsabilidad. 18+.',
        'labels': {
            'Аналоги': 'Alternativas',
            'Бонус': 'Bono',
            'Главная': 'Inicio',
            'Демо': 'Demo',
            'Промокод': 'Código promo',
            'Регистрация': 'Registro',
            'Стратегии': 'Estrategias',
            'Скачать': 'Descargar',
            'Download': 'Descargar',
            'Predictor': 'Predictor',
            'Mines игра': 'Juego Mines',
            'Игра Mines': 'Juego Mines',
        },
    },
    'de': {
        'menu': 'Menü',
        'change': 'Sprache ändern',
        'brand': 'Demo • Signale • Bonus',
        'footer': 'Informationsseite und Demo-Simulator. Inhalte sind keine Finanzberatung. Spielen Sie verantwortungsvoll. 18+.',
        'labels': {
            'Аналоги': 'Alternativen',
            'Бонус': 'Bonus',
            'Главная': 'Startseite',
            'Демо': 'Demo',
            'Промокод': 'Promo-Code',
            'Регистрация': 'Registrierung',
            'Стратегии': 'Strategien',
            'Скачать': 'Download',
            'Download': 'Download',
            'Predictor': 'Predictor',
            'Mines игра': 'Mines Spiel',
            'Игра Mines': 'Mines Spiel',
        },
    },
    'ph': {
        'menu': 'Menu',
        'change': 'Palitan ang wika',
        'brand': 'Demo • signals • bonus',
        'footer': 'informational site at demo simulator. Hindi financial advice ang content. Maglaro nang responsable. 18+.',
        'labels': {
            'Аналоги': 'Mga Alternatibo',
            'Бонус': 'Bonus',
            'Главная': 'Home',
            'Демо': 'Demo',
            'Промокод': 'Promo code',
            'Регистрация': 'Registration',
            'Стратегии': 'Mga Strategy',
            'Скачать': 'Download',
            'Download': 'Download',
            'Predictor': 'Predictor',
            'Mines игра': 'Mines game',
            'Игра Mines': 'Mines game',
        },
    },
}

PAGE_RE = re.compile(r'-(en|es|de|ph)\.html$')
BRAND_RE = re.compile(r'(<span class="brand-logo">💣</span><span><strong>MinesNeon</strong><span>).*?(</span></span>)')
MENU_RE = re.compile(r'<button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav"(?: data-open="[^"]*" data-close="[^"]*")?><span></span><span></span><span></span><b>.*?</b></button>')
LANG_CURRENT_RE = re.compile(r'<span class="lang-current"><strong>(.*?)</strong><small>.*?</small></span>')
FOOTER_RE = re.compile(r'<footer class="footer"><p><strong>MinesNeon</strong> — .*?</p></footer>')


def localize_file(path: Path, lang: str) -> bool:
    data = LANG_UI[lang]
    text = path.read_text(encoding='utf-8-sig')
    old = text

    text = BRAND_RE.sub(r'\1' + data['brand'] + r'\2', text)
    text = MENU_RE.sub(
        '<button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav" '
        f'data-open="{data["menu"]}" data-close="{data["menu"]}">'
        f'<span></span><span></span><span></span><b>{data["menu"]}</b></button>',
        text,
    )
    text = LANG_CURRENT_RE.sub(r'<span class="lang-current"><strong>\1</strong><small>' + data['change'] + r'</small></span>', text)

    for source, target in data['labels'].items():
        text = text.replace(f'>{source}</a>', f'>{target}</a>')
        text = text.replace(f'· {source} ·', f'· {target} ·')
        text = text.replace(f'>{source} •', f'>{target} •')

    text = FOOTER_RE.sub(f'<footer class="footer"><p><strong>MinesNeon</strong> — {data["footer"]}</p></footer>', text)

    if text != old:
        path.write_text(text, encoding='utf-8')
        return True
    return False


def main() -> None:
    updated = 0
    for path in ROOT.glob('*.html'):
        match = PAGE_RE.search(path.name)
        if not match:
            continue
        if localize_file(path, match.group(1)):
            updated += 1
    print(f'updated {updated} html files')


if __name__ == '__main__':
    main()
