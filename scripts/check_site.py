from pathlib import Path
import re, sys
root = Path(__file__).resolve().parents[1]
html = list(root.glob('*.html'))

def exists_target(href):
    if href in ['/styles.css','styles.css']:
        return (root/'styles.css').exists()
    if href == '/':
        return (root/'index.html').exists()
    path = href.strip('/').split('#')[0].split('?')[0]
    if not path:
        return True
    if (root/path).exists():
        return True
    if (root/(path + '.html')).exists():
        return True
    return False

missing=[]
for f in html:
    text=f.read_text(encoding='utf-8')
    if '<title>' not in text or 'meta name="description"' not in text:
        print(f'Missing title/meta: {f.name}')
        sys.exit(1)
    for href in re.findall(r'href="([^"]+)"', text):
        if href.startswith(('http','#','mailto:','tel:')) or href.startswith('https://fonts'):
            continue
        if not exists_target(href):
            missing.append((f.name, href))
if missing:
    print('Missing links:', missing)
    sys.exit(1)
print(f'OK: {len(html)} HTML files, internal links valid')
