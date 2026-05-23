from pathlib import Path
import re, sys
root = Path(__file__).resolve().parents[1]
BASE='/recherche-fuite-eau-angers'
html = list(root.glob('*.html')) + list(root.glob('*/index.html'))

def exists_target(href):
    if href.startswith(BASE):
        href = href[len(BASE):] or '/'
    if href in ['/styles.css','styles.css']:
        return (root/'styles.css').exists()
    if href == '/':
        return (root/'index.html').exists()
    path = href.strip('/').split('#')[0].split('?')[0]
    if not path:
        return True
    return (root/path).exists() or (root/(path + '.html')).exists() or (root/path/'index.html').exists()
missing=[]
for f in html:
    text=f.read_text(encoding='utf-8')
    if '<title>' not in text or 'meta name="description"' not in text:
        print(f'Missing title/meta: {f}')
        sys.exit(1)
    for href in re.findall(r'href="([^"]+)"', text):
        if href.startswith(('http','#','mailto:','tel:')) or href.startswith('https://fonts'):
            continue
        if not exists_target(href):
            missing.append((str(f.relative_to(root)), href))
if missing:
    print('Missing links:', missing)
    sys.exit(1)
print(f'OK: {len(html)} HTML files including clean URL copies, internal links valid')
