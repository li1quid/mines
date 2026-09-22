from pathlib import Path
from html import escape
import re

LANGS = {
    'ru': {'label': 'Русский', 'short': 'RU', 'html': 'ru', 'flag': 'https://flagcdn.com/w40/ru.png', 'flag2x': 'https://flagcdn.com/w80/ru.png'},
    'en': {'label': 'English', 'short': 'EN', 'html': 'en', 'flag': 'https://flagcdn.com/w40/gb.png', 'flag2x': 'https://flagcdn.com/w80/gb.png'},
    'es': {'label': 'Español', 'short': 'ES', 'html': 'es', 'flag': 'https://flagcdn.com/w40/es.png', 'flag2x': 'https://flagcdn.com/w80/es.png'},
    'de': {'label': 'Deutsch', 'short': 'DE', 'html': 'de', 'flag': 'https://flagcdn.com/w40/de.png', 'flag2x': 'https://flagcdn.com/w80/de.png'},
    'ph': {'label': 'Filipino', 'short': 'PH', 'html': 'fil', 'flag': 'https://flagcdn.com/w40/ph.png', 'flag2x': 'https://flagcdn.com/w80/ph.png'},
}
ORDER = ['ru', 'en', 'es', 'de', 'ph']
UI_TEXT = {
    'ru': {'change_lang': 'Сменить язык'},
    'en': {'change_lang': 'Change language'},
    'es': {'change_lang': 'Cambiar idioma'},
    'de': {'change_lang': 'Sprache ändern'},
    'ph': {'change_lang': 'Palitan ang wika'},
}
ROOT = Path('mines-seo-site')
PAGE_RE = re.compile(r'(.+)-(ru|en|es|de|ph)\.html$')
OLD_SWITCHER_RE = re.compile(r'<div class="lang-switcher" aria-label="Language switcher">.*?</div>')


def page_name(slug: str, lang: str) -> str:
    return f'{slug}-{lang}.html'


def flag_img(lang: str) -> str:
    data = LANGS[lang]
    return (
        f'<img src="{data["flag"]}" srcset="{data["flag2x"]} 2x" '
        f'width="40" height="30" loading="lazy" alt="{escape(data["label"])} flag">'
    )


def lang_switcher(slug: str, current_lang: str, available: set[str]) -> str:
    items = []
    for lang in ORDER:
        if lang not in available:
            continue
        data = LANGS[lang]
        cls = 'active' if lang == current_lang else ''
        current = ' aria-current="true"' if lang == current_lang else ''
        items.append(
            f'<a class="{cls}" hreflang="{data["html"]}" href="{page_name(slug, lang)}"{current}>'
            f'<span class="lang-flag">{flag_img(lang)}</span>'
            f'<span class="lang-code">{data["short"]}</span>'
            f'<span class="lang-name">{data["label"]}</span></a>'
        )
    active = LANGS[current_lang]
    return (
        '<div class="lang-switcher" data-lang-switcher aria-label="Language switcher">'
        f'<button class="lang-switcher-toggle" type="button" aria-expanded="false">'
        f'<span class="lang-flag">{flag_img(current_lang)}</span>'
        f'<span class="lang-current"><strong>{active["label"]}</strong><small>{escape(UI_TEXT[current_lang]["change_lang"])}</small></span>'
        '<span class="lang-chevron">⌄</span></button>'
        '<div class="lang-options">' + ''.join(items) + '</div></div>'
    )


def main() -> None:
    files = list(ROOT.glob('*.html'))
    slugs: dict[str, set[str]] = {}
    for path in files:
        match = PAGE_RE.match(path.name)
        if match:
            slugs.setdefault(match.group(1), set()).add(match.group(2))

    updated = 0
    for path in files:
        match = PAGE_RE.match(path.name)
        if not match:
            continue
        slug, lang = match.group(1), match.group(2)
        text = path.read_text(encoding='utf-8-sig')
        new_text = OLD_SWITCHER_RE.sub(lang_switcher(slug, lang, slugs.get(slug, set())), text)
        if new_text != text:
            path.write_text(new_text, encoding='utf-8')
            updated += 1
    print(f'updated {updated} html files')


if __name__ == '__main__':
    main()
