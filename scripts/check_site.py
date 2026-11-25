#!/usr/bin/env python3
"""Check generated pages and local HTML asset/link targets before publishing."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys

ROOT = Path(__file__).resolve().parents[1] / '_site'
errors = []


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.targets = []

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ('href', 'src') and value:
                self.targets.append(value)


for required in ('index.html', 'publications/index.html', 'cv/index.html', 'news/index.html'):
    if not (ROOT / required).is_file():
        errors.append(f'Missing page: {required}')

html_files = list(ROOT.rglob('*.html'))
for page in html_files:
    parser = Links()
    contents = page.read_text(encoding='utf-8')
    parser.feed(contents)
    for raw in parser.targets:
        if '{{' in raw or '}}' in raw:
            errors.append(f'{page.relative_to(ROOT)}: unresolved template in URL {raw}')
            continue
        url = urlsplit(raw)
        if url.scheme or url.netloc or not url.path:
            continue
        target = (ROOT / unquote(url.path).lstrip('/')) if url.path.startswith('/') else page.parent / unquote(url.path)
        if target.is_dir():
            target = target / 'index.html'
        if not target.exists():
            errors.append(f'{page.relative_to(ROOT)}: missing {raw}')
    if any(person in contents.lower() for person in ('yifanyu4@', 'cv_yifanyu', 'prof_pic.jpg', 'albert einstein')):
        errors.append(f'{page.relative_to(ROOT)}: copied personal/demo content remains')

if errors:
    print('\n'.join(sorted(set(errors))), file=sys.stderr)
    sys.exit(1)
print(f'Checked {len(html_files)} generated pages: required pages and local HTML links/assets pass.')
