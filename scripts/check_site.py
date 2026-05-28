from pathlib import Path
import json
import re, sys
root = Path(__file__).resolve().parents[1]
html = list(root.glob('*.html')) + list(root.glob('*/index.html'))
PHONE_DISPLAY = '09 72 14 55 77'
PHONE_TEL = '+339****5577'


def exists_target(href):
    if href in ['/styles.css','styles.css']:
        return (root/'styles.css').exists()
    if href == '/':
        return (root/'index.html').exists()
    path = href.strip('/').split('#')[0].split('?')[0]
    if not path:
        return True
    return (root/path).exists() or (root/(path + '.html')).exists() or (root/path/'index.html').exists()

missing=[]
semantic=[]
for f in html:
    text=f.read_text(encoding='utf-8')
    rel=str(f.relative_to(root))
    if '<title>' not in text or 'meta name="description"' not in text:
        print(f'Missing title/meta: {f}')
        sys.exit(1)
    if len(re.findall(r'<h1\b', text)) != 1:
        semantic.append((rel, 'expected exactly one H1'))
    if 'Angers Détection Fuite Pros' in text:
        semantic.append((rel, 'invented hero label: Angers Détection Fuite Pros'))
    if 'ENVOYER</a>' in text or '<a class="form-button" href="tel:' in text:
        semantic.append((rel, 'submit-looking or form-button CTA points to tel'))
    if 'l’objectif est simple : limiter les dégâts' in text and 'l’appel doit d’abord permettre de sécuriser' in text:
        semantic.append((rel, 'redundant homepage emergency lead sentence'))
    for match in re.findall(r'<script[^>]+type="application/ld\+json"[^>]*>(.*?)</script>', text, flags=re.S):
        try:
            json.loads(match)
        except Exception as exc:
            semantic.append((rel, f'JSON-LD invalid: {exc}'))
    for img_src, alt in re.findall(r'<img[^>]+src="([^"]+)"[^>]*alt="([^"]*)"', text):
        if not alt.strip():
            semantic.append((rel, f'empty image alt: {img_src}'))
        if img_src.startswith('/') and not (root/img_src.lstrip('/')).exists():
            semantic.append((rel, f'missing image: {img_src}'))
    for href in re.findall(r'href="([^"]+)"', text):
        if href.startswith('tel:') and href != f'tel:{PHONE_TEL}':
            semantic.append((rel, f'tel mismatch: {href}'))
        if href in ('#', 'javascript:void(0)', 'javascript:;') or href.lower().startswith('javascript:'):
            semantic.append((rel, f'empty/javascript link: {href}'))
        if href.startswith(('http','#','mailto:','tel:')) or href.startswith('https://fonts'):
            continue
        if not exists_target(href):
            missing.append((rel, href))
if missing:
    print('Missing links:', missing)
    sys.exit(1)
if semantic:
    print('Semantic/site quality issues:', semantic[:50])
    sys.exit(1)
print(f'OK: {len(html)} HTML files including clean URL copies, internal links and semantic checks valid')
