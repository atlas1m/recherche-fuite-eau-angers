#!/usr/bin/env python3
from pathlib import Path
import json, re, sys, urllib.parse
ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT
BASE = 'https://recherche-fuite-eau-angers.fr'
FORBIDDEN_PATTERNS = [
    r'notre\s+entreprise\s+de\s+plomberie', r'nos\s+plombiers', r'nos\s+artisans',
    r'adresse\s*:\s*\d', r'24\s*/\s*7', r'24h\s*/\s*24', r'24\s+h\s*/\s*24',
    r'intervention\s+immédiate\s+garantie', r'garantie\s+d[’\']intervention\s+immédiate', r'prix\s+fixe\s+garanti',
    r'remboursement\s+assurance\s+garanti', r'avis\s+client\s*[:\-]',
    r'fausse\s+promesse', r'\bsans\s+promesse\b', r'\bpromesse\b',
    r'\bschéma\b', r'\billustration\b', r'visuel\s+informatif',
    r'\binvent[ée]e?\b', r'\btransparent\b', r'\btransparence\b',
    r'\bOVH\b', r'\bTwilio\b', r'\bRetell\b', r'\bfallback\b',
    # Anti-boulettes: never expose generator/audit/SEO filler language to visitors.
    r'\btemplate\b', r'\bmots-cl[ée]s\b', r'photo\s+associ[ée]e', r'angle\s+pr[ée]cis',
    r'cette\s+couche', r'r[ée]p[ée]ter\s+m[ée]caniquement', r'r[ée]p[ée]tition\s+m[ée]canique',
    r'pr[ée]sence\s+locale\s+non\s+v[ée]rifi[ée]e'
]

def strip_tags(x): return re.sub(r'<[^>]*>', ' ', x or '').strip()
def visible_word_count(html):
    html = re.sub(r'<script[^>]*>.*?</script>', ' ', html, flags=re.I|re.S)
    html = re.sub(r'<style[^>]*>.*?</style>', ' ', html, flags=re.I|re.S)
    text = re.sub(r'<[^>]*>', ' ', html)
    return len(re.findall(r"[\wÀ-ÖØ-öø-ÿ’'-]+", text))
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
    rows=[]; errors=[]; titles={}; metas={}; canonicals=[]; total_images=0
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
        total_images += len(img_tags)
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
        visible_for_dup = re.sub(r'\s+', ' ', strip_tags(re.sub(r'<script[^>]*>.*?</script>', ' ', html, flags=re.I|re.S))).strip()
        low=visible_for_dup.lower()
        for pat in FORBIDDEN_PATTERNS:
            if re.search(pat, low, re.I): bad.append(pat)
        if bad: errors.append(f'{rel}: claim/langage interne interdit possible {bad}')
        sector_sequence = 'Angers Avrillé Trélazé Les Ponts-de-Cé Maine-et-Loire'
        if visible_for_dup.count(sector_sequence) > 1:
            errors.append(f'{rel}: bloc secteurs dupliqué visible ({visible_for_dup.count(sector_sequence)} occurrences)')
        human_text = ' '.join([title, meta] + h1 + h2 + [strip_tags(re.sub(r'<script[^>]*>.*?</script>', ' ', html, flags=re.I|re.S))]).lower()
        if 'recherche-fuite-non-destructive-angers' in rel:
            required_source_backed = ['non destructive', 'sans casse', 'gaz traceur', 'caméra thermique']
            missing_source_backed = [term for term in required_source_backed if term not in human_text]
            if missing_source_backed:
                errors.append(f'{rel}: glossaire métier source-backed incomplet {missing_source_backed}')
            if 'sans casser inutilement' not in human_text and 'sans démolition' not in human_text and 'sans dégradation' not in human_text:
                errors.append(f'{rel}: explication humaine du terme non destructive manquante')
        titles.setdefault(title,[]).append(rel); metas.setdefault(meta,[]).append(rel); canonicals.append(canon)
        rows.append({'file':rel,'title':title,'meta_len':len(meta),'canonical':canon,'h1_count':len(h1),'h2_count':len(h2),'jsonld_blocks':len(jsonlds),'jsonld_types':jsonld_types,'faq': 'FAQPage' in json.dumps(jsonld_types), 'breadcrumb': 'BreadcrumbList' in json.dumps(jsonld_types),'tel': 'tel:' in html,'links':len(links),'missing_links':missing})
    dup_titles={k:v for k,v in titles.items() if k and len(v)>1 and not all(x.endswith('/index.html') or x.endswith('.html') for x in v)}
    # duplicates are expected for flat/folder pairs, flag only non-pairs crudely
    duplicate_title_groups={k:v for k,v in titles.items() if k and len(v)>2}
    duplicate_meta_groups={k:v for k,v in metas.items() if k and len(v)>2}
    sitemap=(SITE/'sitemap.xml').read_text(encoding='utf-8') if (SITE/'sitemap.xml').exists() else ''
    sitemap_urls=re.findall(r'<loc>(.*?)</loc>', sitemap)
    dup_sitemap=sorted([u for u in set(sitemap_urls) if sitemap_urls.count(u) > 1])
    if dup_sitemap: errors.append(f'sitemap: URLs dupliquées {dup_sitemap[:10]}')
    canonical_folder_urls=sorted(set(r['canonical'] for r in rows if r['canonical'] and not r['file'].endswith('.html')))
    missing_sitemap=[u for u in canonical_folder_urls if u not in sitemap_urls]
    if missing_sitemap: errors.append(f'sitemap: URLs canoniques absentes {missing_sitemap[:10]}')
    home=(SITE/'index.html').read_text(encoding='utf-8', errors='ignore').lower() if (SITE/'index.html').exists() else ''
    autoglass_components=['site-header','lead-capture','quote-box','intro','service-rows','faq-list','areas','contact-strip','proof','site-footer','sticky-call']
    def class_pos(token):
        m=re.search(r'class=["\'][^"\']*\b' + re.escape(token) + r'\b', home)
        return m.start() if m else -1
    positions={c: class_pos(c) for c in autoglass_components}
    missing_components=[c for c,p in positions.items() if p < 0]
    if missing_components: errors.append(f'homepage: composants template Autoglass manquants {missing_components}')
    ordered_components=['site-header','lead-capture','quote-box','intro','service-rows','faq-list','areas','contact-strip','proof','site-footer']
    if not missing_components:
        order_bad=[ordered_components[i]+'>'+ordered_components[i+1] for i in range(len(ordered_components)-1) if positions[ordered_components[i]] > positions[ordered_components[i+1]]]
        if order_bad: errors.append(f'homepage: ordre template Autoglass incorrect {order_bad}')
    service_rows=len(re.findall(r'class=["\']service-row\b', home))
    if service_rows < 6: errors.append(f'homepage: service rows insuffisantes pour template Autoglass ({service_rows})')
    home_words = visible_word_count(home)
    if home_words < 900:
        errors.append(f'homepage: densité éditoriale template insuffisante ({home_words} mots, minimum 900)')
    if home_words > 1400:
        errors.append(f'homepage: densité éditoriale template trop lourde ({home_words} mots, maximum 1400)')
    home_img_srcs = re.findall(r'<img\b[^>]*\bsrc=["\']([^"\']+)["\']', home, re.I|re.S)
    unique_home_imgs = sorted(set(home_img_srcs))
    if len(unique_home_imgs) < 8:
        errors.append(f'homepage: variété visuelle insuffisante ({len(unique_home_imgs)} photos uniques, minimum 8)')
    non_photo_home_imgs = [src for src in unique_home_imgs if src.startswith('/assets/images/') and not re.search(r'\.(jpe?g|png|webp)(?:$|[?#])', src, re.I)]
    if non_photo_home_imgs:
        errors.append(f'homepage: assets non-photo interdits dans la template {non_photo_home_imgs}')
    svg_home_imgs = [src for src in unique_home_imgs if re.search(r'\.svg(?:$|[?#])', src, re.I)]
    if svg_home_imgs:
        errors.append(f'homepage: SVG/illustrations interdits - copier la template photo {svg_home_imgs}')
    repeated_home_imgs = {src: home_img_srcs.count(src) for src in unique_home_imgs if home_img_srcs.count(src) > 2}
    if repeated_home_imgs:
        errors.append(f'homepage: photo répétée trop souvent {repeated_home_imgs}')
    # Above-the-fold guard: key navigation pages must not show the same hero/header photo.
    hero_pages=['index.html','services/index.html','about/index.html','locations/index.html','contact/index.html']
    hero_srcs={}
    for rel in hero_pages:
        f=SITE/rel
        if not f.exists():
            errors.append(f'{rel}: page clé absente pour contrôle hero')
            continue
        page_html=f.read_text(encoding='utf-8', errors='ignore')
        imgs=re.findall(r'<img\b[^>]*\bsrc=["\']([^"\']+)["\']', page_html, re.I|re.S)
        if not imgs:
            errors.append(f'{rel}: hero/header photo absente')
            continue
        hero_srcs[rel]=imgs[0]
    repeated_heroes={src:[rel for rel,s in hero_srcs.items() if s==src] for src in set(hero_srcs.values())}
    repeated_heroes={src:rels for src,rels in repeated_heroes.items() if len(rels)>1}
    if repeated_heroes:
        errors.append(f'pages clés: même photo hero/header réutilisée {repeated_heroes}')
    # Final template guard: strategic canonical pages need a deterministic keyword photo slot.
    exempt_keyword_slots={'/','/about/','/services/','/mentions-legales/','/politique-confidentialite/','/methodologie/'}
    for url in sitemap_urls:
        path=urllib.parse.urlparse(url).path or '/'
        if path in exempt_keyword_slots:
            continue
        rel='index.html' if path == '/' else path.strip('/') + '/index.html'
        f=SITE/rel
        if not f.exists():
            continue
        page_html=f.read_text(encoding='utf-8', errors='ignore')
        if 'data-keyword-slot=' not in page_html:
            errors.append(f'{rel}: photo keyword-slot absente')
        page_imgs=re.findall(r'<img\b[^>]*\bsrc=["\']([^"\']+)["\']', page_html, re.I|re.S)
        if len(set(page_imgs)) < 4:
            errors.append(f'{rel}: variété visuelle page insuffisante ({len(set(page_imgs))} images uniques, minimum 4)')
        w=visible_word_count(page_html)
        if w < 760:
            errors.append(f'{rel}: densité page topicale insuffisante ({w} mots, minimum 760)')
    human_urgency_terms=['compteur qui tourne','dégât des eaux','couper l’arrivée d’eau','appeler']
    missing_urgency=[term for term in human_urgency_terms if term not in home]
    if missing_urgency: errors.append(f'homepage: urgence humaine insuffisante {missing_urgency}')
    phone_signals=['phone-wordmark','call-now','tel:']
    missing_phone=[term for term in phone_signals if term not in home]
    if missing_phone: errors.append(f'homepage: CTA téléphone template manquant {missing_phone}')
    headings=' '.join(strip_tags(x) for x in re.findall(r'<h[1-6][^>]*>(.*?)</h[1-6]>', home, re.I|re.S)).lower()
    if re.search(r'recherche fuite eau angers|fuite eau angers', headings): errors.append('homepage: keyword stuffing exact dans les headings')
    robots=(SITE/'robots.txt').read_text(encoding='utf-8') if (SITE/'robots.txt').exists() else ''
    if 'Sitemap:' not in robots: errors.append('robots.txt: Sitemap absent')
    return {'html_count':len(rows),'rows':rows,'errors':errors,'duplicate_title_groups':duplicate_title_groups,'duplicate_meta_groups':duplicate_meta_groups,'sitemap_url_count':len(sitemap_urls),'sitemap_urls':sitemap_urls,'robots_has_sitemap':'Sitemap:' in robots,'homepage_words':home_words,'homepage_unique_images':len(unique_home_imgs)}
if __name__ == '__main__':
    result=audit()
    out=json.dumps(result,ensure_ascii=False,indent=2)
    if '--json' in sys.argv: print(out)
    else:
        print(f"HTML: {result['html_count']} | sitemap URLs: {result['sitemap_url_count']} | homepage words: {result['homepage_words']} | homepage unique images: {result['homepage_unique_images']} | errors: {len(result['errors'])}")
        for e in result['errors'][:80]: print('-', e)
    if result['errors']: sys.exit(1)
