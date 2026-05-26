#!/usr/bin/env python3
from pathlib import Path
import json, re, sys, urllib.parse
ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT
BASE = 'https://recherche-fuite-eau-angers.fr'
FORBIDDEN_PATTERNS = [
    r'notre\s+entreprise\s+de\s+plomberie', r'nos\s+plombiers', r'nos\s+artisans',
    r'adresse\s*:\s*\d', r'24\s*/\s*7', r'24h\s*/\s*24', r'24\s+h\s*/\s*24',
    r'intervention\s+immédiate\s+garantie', r'prix\s+fixe\s+garanti',
    r'remboursement\s+assurance\s+garanti', r'avis\s+client\s*[:\-]'
]

def strip_tags(x): return re.sub(r'<[^>]*>', ' ', x or '').strip()
def attr(html, pattern):
    m=re.search(pattern, html, re.I|re.S)
    return m.group(1).strip() if m else ''
def canonical_slug_from_file(path):
    rel=path.relative_to(SITE)
    if rel.name == 'index.html':
        if len(rel.parts)==1: return '/'
        return '/' + '/'.join(rel.parts[:-1]) + '/'
    if rel.suffix == '.html':
        return '/' + str(rel.with_suffix('')).replace('index','').strip('/') + '/'
    return '/' + str(rel).strip('/')
def target_exists(href):
    if href.startswith(('http://','https://','#','mailto:','tel:')) or href.startswith('https://fonts'):
        return True
    path = href.split('#')[0].split('?')[0]
    if path in ('','/'): return (SITE/'index.html').exists()
    path = path.strip('/')
    return (SITE/path).exists() or (SITE/(path+'.html')).exists() or (SITE/path/'index.html').exists()
def audit():
    files=sorted([p for p in SITE.rglob('*.html') if '.git' not in p.parts])
    rows=[]; errors=[]; titles={}; metas={}; canonicals=[]
    for f in files:
        html=f.read_text(encoding='utf-8',errors='ignore')
        rel=str(f.relative_to(SITE))
        title=strip_tags(attr(html,r'<title>(.*?)</title>'))
        meta=attr(html,r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']') or attr(html,r'<meta\s+content=["\'](.*?)["\']\s+name=["\']description["\']')
        canon=attr(html,r'<link\s+rel=["\']canonical["\']\s+href=["\'](.*?)["\']') or attr(html,r'<link\s+href=["\'](.*?)["\']\s+rel=["\']canonical["\']')
        h1=[strip_tags(x) for x in re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.I|re.S)]
        h2=[strip_tags(x) for x in re.findall(r'<h2[^>]*>(.*?)</h2>', html, re.I|re.S)]
        jsonlds=re.findall(r'<script[^>]+application/ld\+json[^>]*>(.*?)</script>', html, re.I|re.S)
        jsonld_ok=True; jsonld_types=[]
        for block in jsonlds:
            try:
                data=json.loads(block)
                graph=data.get('@graph',[data]) if isinstance(data,dict) else data
                if isinstance(graph,dict): graph=[graph]
                for item in graph:
                    if isinstance(item,dict): jsonld_types.append(item.get('@type'))
            except Exception as e:
                jsonld_ok=False; errors.append(f'{rel}: JSON-LD invalide: {e}')
        links=re.findall(r'href=["\']([^"\']+)["\']', html)
        missing=[href for href in links if not target_exists(href)]
        if missing: errors.append(f'{rel}: liens internes manquants {missing[:5]}')
        img_tags=re.findall(r'<img\b[^>]*>', html, re.I|re.S)
        for tag in img_tags:
            src=attr(tag, r'src=["\']([^"\']+)["\']')
            alt=attr(tag, r'alt=["\']([^"\']*)["\']')
            if not alt.strip(): errors.append(f'{rel}: image sans alt descriptif {src}')
            if src.startswith('/') and not (SITE/src.strip('/')).exists(): errors.append(f'{rel}: image manquante {src}')
        expected=BASE+canonical_slug_from_file(f)
        if not title: errors.append(f'{rel}: title manquant')
        if not meta: errors.append(f'{rel}: meta description manquante')
        if not h1: errors.append(f'{rel}: H1 manquant')
        if not canon: errors.append(f'{rel}: canonical manquant')
        elif canon != expected and not (rel.endswith('.html') and canon == BASE + canonical_slug_from_file(f)):
            # flat duplicate should point to folder canonical; canonical_slug_from_file already does.
            errors.append(f'{rel}: canonical inattendu {canon} != {expected}')
        if not jsonlds: errors.append(f'{rel}: JSON-LD absent')
        if not jsonld_ok: pass
        if not any(t=='BreadcrumbList' for t in jsonld_types): errors.append(f'{rel}: BreadcrumbList absent')
        if 'tel:' not in html: errors.append(f'{rel}: CTA tel absent')
        bad=[]
        low=html.lower()
        for pat in FORBIDDEN_PATTERNS:
            if re.search(pat, low, re.I): bad.append(pat)
        if bad: errors.append(f'{rel}: claim interdit possible {bad}')
        titles.setdefault(title,[]).append(rel); metas.setdefault(meta,[]).append(rel); canonicals.append(canon)
        rows.append({'file':rel,'title':title,'meta_len':len(meta),'canonical':canon,'h1_count':len(h1),'h2_count':len(h2),'jsonld_blocks':len(jsonlds),'jsonld_types':jsonld_types,'faq': 'FAQPage' in json.dumps(jsonld_types), 'breadcrumb': 'BreadcrumbList' in json.dumps(jsonld_types),'tel': 'tel:' in html,'links':len(links),'missing_links':missing})
    dup_titles={k:v for k,v in titles.items() if k and len(v)>1 and not all(x.endswith('/index.html') or x.endswith('.html') for x in v)}
    # duplicates are expected for flat/folder pairs, flag only non-pairs crudely
    duplicate_title_groups={k:v for k,v in titles.items() if k and len(v)>2}
    duplicate_meta_groups={k:v for k,v in metas.items() if k and len(v)>2}
    sitemap=(SITE/'sitemap.xml').read_text(encoding='utf-8') if (SITE/'sitemap.xml').exists() else ''
    sitemap_urls=re.findall(r'<loc>(.*?)</loc>', sitemap)
    canonical_folder_urls=sorted(set(r['canonical'] for r in rows if r['canonical'] and not r['file'].endswith('.html')))
    missing_sitemap=[u for u in canonical_folder_urls if u not in sitemap_urls]
    if missing_sitemap: errors.append(f'sitemap: URLs canoniques absentes {missing_sitemap[:10]}')
    robots=(SITE/'robots.txt').read_text(encoding='utf-8') if (SITE/'robots.txt').exists() else ''
    if 'Sitemap:' not in robots: errors.append('robots.txt: Sitemap absent')
    return {'html_count':len(rows),'rows':rows,'errors':errors,'duplicate_title_groups':duplicate_title_groups,'duplicate_meta_groups':duplicate_meta_groups,'sitemap_url_count':len(sitemap_urls),'sitemap_urls':sitemap_urls,'robots_has_sitemap':'Sitemap:' in robots}
if __name__ == '__main__':
    result=audit()
    out=json.dumps(result,ensure_ascii=False,indent=2)
    if '--json' in sys.argv: print(out)
    else:
        print(f"HTML: {result['html_count']} | sitemap URLs: {result['sitemap_url_count']} | errors: {len(result['errors'])}")
        for e in result['errors'][:80]: print('-', e)
    if result['errors']: sys.exit(1)
