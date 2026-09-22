from pathlib import Path
import shutil

root = Path('mines-seo-site')
files = ['index.html', 'promo.html', 'strategies.html', 'faq.html', 'apk.html', 'other.html']
needle = '<a class="" href="other.html"><span>🚀</span>Другие игры</a>'
insert = '<a class="" href="home-en.html"><span>📚</span>Гайды</a>'

for file_name in files:
    path = root / file_name
    html = path.read_text(encoding='utf-8')
    if 'href="home-en.html"' not in html:
        if needle in html:
            html = html.replace(needle, needle + '\n' + insert, 1)
        else:
            html = html.replace('</nav>', insert + '</nav>', 1)
        path.write_text(html, encoding='utf-8')
        print(f'{file_name}: added')
    else:
        print(f'{file_name}: already exists')

# Keep generator updated so the link is not lost after regeneration.
generator = root / 'generate_pages.py'
if generator.exists():
    source = generator.read_text(encoding='utf-8')
    entry = "('home-en.html', 'Гайды', '📚'),"
    if entry not in source:
        source = source.replace("('other.html', 'Другие игры', '🚀'),", "('other.html', 'Другие игры', '🚀'),\n    " + entry, 1)
        generator.write_text(source, encoding='utf-8')
        print('generate_pages.py: updated')
    else:
        print('generate_pages.py: already exists')

for file_name in files:
    html = (root / file_name).read_text(encoding='utf-8')
    print(f'{file_name}: guides_count={html.count("href=\"home-en.html\"")}')

print('home-en.html exists=' + str((root / 'home-en.html').exists()))

dest = Path(r'C:\Users\kompy\OneDrive\Desktop\сайт\mines\multilang-site')
if dest.exists():
    shutil.rmtree(dest)
shutil.copytree(root, dest)
print('copied_to=' + str(dest))
