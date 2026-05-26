#!/usr/bin/env python3
from pathlib import Path
import json, html

SITE = Path(__file__).resolve().parents[1]
BASE = "https://recherche-fuite-eau-angers.fr"
PHONE_DISPLAY = "09 72 14 55 77"
PHONE_TEL = "+339****5577"

NAV = '<header class="nav"><div class="wrap navin"><a class="brand" href="/recherche-fuite-eau-angers/"><span class="mark">RF</span><span>Recherche Fuite Angers</span></a><nav class="links"><a href="/recherche-fuite-eau-angers/">Guide</a><a href="/recherche-fuite-non-destructive-angers/">Méthodes</a><a href="/recherche-fuite-assurance-angers/">Assurance</a><a href="/prix-recherche-fuite-eau-angers/">Prix</a><a class="btn phone-primary" href="tel:+339****5577">Appeler maintenant</a><a class="nav-form" href="/contact/">Formulaire</a></nav></div></header>'
FOOT = '<footer class="foot"><div class="wrap"><p>Service indépendant d’information et de mise en relation. Pas une entreprise de plomberie ou de recherche de fuite. Informations indicatives, à faire confirmer par un professionnel qualifié.</p><p><a href="/mentions-legales/">Mentions légales</a> · <a href="/politique-confidentialite/">Confidentialité</a> · <a href="/methodologie/">Méthodologie</a></p></div></footer><a class="sticky-call" href="tel:+339****5577" aria-label="Appeler le service d’orientation au 09 72 14 55 77">Appeler maintenant : 09 72 14 55 77</a>'

COMMON_LINKS = [
    ("/recherche-fuite-eau-angers/", "guide recherche de fuite à Angers"),
    ("/recherche-fuite-non-destructive-angers/", "localiser une fuite sans casser"),
    ("/prix-recherche-fuite-eau-angers/", "prix et facteurs de devis"),
    ("/recherche-fuite-assurance-angers/", "assurance et rapport"),
    ("/degat-des-eaux-angers/", "dégât des eaux"),
    ("/fuite-apres-compteur-angers/", "fuite après compteur"),
    ("/contact/", "décrire votre situation"),
]

PAGES = {
"recherche-fuite-eau-angers": {
 "title":"Recherche fuite eau Angers : guide indépendant et orientation",
 "h1":"Recherche de fuite d’eau à Angers : comprendre, qualifier, être orienté",
 "meta":"Guide indépendant pour recherche de fuite d’eau à Angers : symptômes, méthodes de localisation, assurance, prix et orientation avec prudence.",
 "lead":"Ce guide aide propriétaires, locataires et syndics à décrire une fuite d’eau à Angers avant de demander une recherche. Le site est un service indépendant d’information et d’orientation : il ne prétend pas être une entreprise locale de plomberie.",
 "sections":[
  ("Symptômes à prendre au sérieux", ["Compteur qui tourne alors que tous les robinets sont fermés.", "Tache au plafond ou mur humide qui progresse.", "Baisse de pression, odeur d’humidité ou sol anormalement chaud.", "Dégât des eaux chez un voisin, en copropriété ou après une période de pluie."]),
  ("Que faire avant d’appeler", ["Coupez l’eau si la fuite est active et accessible.", "Photographiez les traces visibles et notez l’heure d’apparition.", "Relevez le compteur avant/après une période sans consommation.", "Préparez votre statut : propriétaire, locataire, syndic ou gestionnaire."]),
  ("Méthodes possibles", ["Caméra thermique pour repérer certains écarts de température.", "Gaz traceur ou électro-acoustique selon le réseau et l’accès.", "Humidimètre et inspection visuelle pour cadrer la zone.", "La bonne méthode dépend du bâtiment : aucune technique n’est universelle."]),
  ("Limites et clarté", ["Aucun délai, tarif ou remboursement assurance n’est annoncé par ce site avant qualification.", "L’objectif est de préparer une demande claire et d’éviter les mauvaises orientations.", "Un professionnel qualifié doit confirmer le diagnostic et le devis."])
 ],
 "faq":[("Qui appeler pour une recherche de fuite à Angers ?","Vous pouvez appeler un professionnel spécialisé ou utiliser ce service d’orientation indépendant pour préparer la demande. Ce site ne se présente pas comme une entreprise de plomberie."),("Peut-on toujours localiser une fuite sans casser ?","Non. L’objectif est souvent de limiter les ouvertures inutiles, mais la méthode dépend de l’accès, du type de réseau et du symptôme."),("Faut-il appeler l’assurance avant la recherche ?","En cas de dégât des eaux, il est prudent de contacter votre assurance ou syndic. La prise en charge dépend du contrat et n’est pas garantie.")]
},
"recherche-fuite-non-destructive-angers": {
 "title":"Localiser une fuite sans casser à Angers : méthodes et limites",
 "h1":"Localiser une fuite sans casser à Angers : méthodes, usages et limites",
 "meta":"Comprendre comment localiser une fuite sans casser inutilement à Angers : caméra thermique, gaz traceur, électro-acoustique, limites et questions à poser.",
 "lead":"L’objectif est de localiser la fuite sans casser inutilement. Cela reste un diagnostic technique : la méthode dépend du réseau, du matériau, de l’accès et des symptômes.",
 "sections":[
  ("Quand c’est pertinent", ["Fuite invisible après compteur ou sur réseau encastré.", "Humidité sans origine claire dans un mur, sol ou plafond.", "Besoin de limiter la casse avant réparation.", "Dossier assurance où un rapport peut aider à expliquer la situation."]),
  ("Méthodes fréquentes", ["Caméra thermique : repère certains écarts de température.", "Gaz traceur : utile selon accessibilité et étanchéité du réseau.", "Électro-acoustique : écoute de bruits de fuite sur certains réseaux.", "Inspection caméra : plutôt pour évacuations ou canalisations accessibles."]),
  ("Questions à poser", ["Quelle méthode est prévue et pourquoi ?", "Le rapport écrit est-il inclus ?", "Que se passe-t-il si la fuite n’est pas localisable sans ouverture ?", "Le devis distingue-t-il recherche, réparation et remise en état ?"])
 ],
 "faq":[("Peut-on toujours éviter de casser ?","Non. Le diagnostic peut réduire le risque d’ouverture inutile, mais certaines situations exigent une ouverture ou une réparation ciblée."),("Quelle méthode est la meilleure ?","Il n’y a pas de méthode universelle : caméra thermique, gaz traceur ou écoute dépendent du réseau et du symptôme."),("Un rapport est-il nécessaire ?","Il peut être utile pour l’assurance ou le syndic, mais son usage dépend du dossier et du contrat.")]
},
"prix-recherche-fuite-eau-angers": {
 "title":"Prix recherche fuite eau Angers : facteurs de devis et prudence",
 "h1":"Prix d’une recherche de fuite d’eau à Angers : comprendre ce qui fait varier le devis",
 "meta":"Prix recherche fuite eau Angers : facteurs qui influencent le devis, méthodes, rapport, assurance et limites. Pas de tarif annoncé sans qualification.",
 "lead":"Le coût d’une recherche de fuite dépend du type de fuite, de l’accès, de la méthode et du besoin de rapport. Cette page aide à préparer les bonnes questions sans avancer de montant avant qualification.",
 "sections":[
  ("Facteurs qui font varier le prix", ["Type de réseau : alimentation, évacuation, chauffage, toiture ou infiltration.", "Accessibilité : apparent, encastré, sous dalle, étage, copropriété.", "Méthode : caméra thermique, gaz traceur, électro-acoustique ou inspection.", "Besoin d’un rapport écrit pour assurance, syndic ou propriétaire."]),
  ("Ce qu’un devis doit clarifier", ["Le périmètre exact : recherche seulement ou réparation incluse.", "Le prix du déplacement et les conditions d’annulation.", "Le type de rapport fourni et son délai.", "Les limites si la fuite n’est pas localisée immédiatement."]),
  ("Assurance et remboursement", ["La prise en charge dépend du contrat, de la cause et du dossier.", "Demandez à l’assurance les justificatifs attendus avant intervention si possible.", "Attendez une confirmation écrite avant de considérer une prise en charge comme acquise."])
 ],
 "faq":[("Existe-t-il un prix fixe pour une recherche de fuite à Angers ?","Non. Le tarif dépend de la situation, de la méthode et du besoin de rapport."),("L’assurance rembourse-t-elle la recherche de fuite ?","Parfois, selon contrat et circonstances. Il faut vérifier les garanties et les justificatifs demandés."),("La réparation est-elle comprise ?","Pas toujours. Demandez si le devis couvre uniquement la recherche ou aussi la réparation et la remise en état.")]
},
"recherche-fuite-assurance-angers": {
 "title":"Recherche fuite assurance Angers : rapport, contrat, démarches",
 "h1":"Recherche de fuite et assurance à Angers : préparer un dossier clair",
 "meta":"Recherche fuite assurance Angers : comprendre rapport, déclaration dégât des eaux, syndic, contrat et prise en charge à confirmer.",
 "lead":"Après un dégât des eaux, l’assurance peut demander des éléments précis. Cette page aide à préparer les informations utiles sans annoncer de remboursement ni de prise en charge automatique.",
 "sections":[
  ("Éléments à rassembler", ["Photos datées des traces d’eau ou dégâts visibles.", "Relevés de compteur si une fuite après compteur est suspectée.", "Échanges avec voisin, syndic, propriétaire ou locataire.", "Contrat d’assurance et éventuelle déclaration de sinistre."]),
  ("Rapport de recherche de fuite", ["Un rapport peut préciser la zone, la méthode utilisée et les limites du diagnostic.", "Demandez si le rapport est inclus et s’il convient à un dossier assurance.", "Le rapport ne suffit pas à lui seul pour obtenir un remboursement."]),
  ("Copropriété et location", ["En copropriété, informez le syndic si les parties communes ou un voisin sont concernés.", "Un locataire doit prévenir propriétaire ou agence selon le cas.", "Gardez des traces écrites des démarches et appels importants."])
 ],
 "faq":[("L’assurance prend-elle en charge la recherche de fuite ?","Cela dépend du contrat, de la cause et des conditions prévues. Ce site n’annonce aucune prise en charge."),("Faut-il un rapport écrit ?","Il est souvent utile, surtout en dégât des eaux, mais demandez à votre assurance ce qu’elle attend."),("Qui contacte le syndic ?","Si la copropriété ou un voisin est concerné, le syndic doit être informé rapidement par la personne responsable du dossier.")]
},
"degat-des-eaux-angers": {
 "title":"Dégât des eaux Angers : recherche de fuite et étapes utiles",
 "h1":"Dégât des eaux à Angers : quoi faire avant une recherche de fuite",
 "meta":"Dégât des eaux à Angers : étapes utiles, sécurité, assurance, syndic, recherche de fuite et informations à confirmer.",
 "lead":"Un dégât des eaux demande d’abord de limiter les dommages, documenter les faits et comprendre l’origine possible. Cette page aide à structurer les premières étapes avant une recherche de fuite.",
 "sections":[
  ("Premières actions", ["Coupez l’arrivée d’eau si la fuite est active et accessible.", "Sécurisez les appareils électriques si une zone est humide.", "Prévenez voisin, syndic, propriétaire ou assurance selon votre situation.", "Prenez des photos avant nettoyage si cela ne crée pas de risque."]),
  ("Origines possibles", ["Canalisation encastrée, joint de salle de bain, évacuation, toiture ou infiltration.", "Fuite après compteur avec surconsommation.", "Infiltration par façade, toiture ou balcon selon météo.", "Cause à confirmer par un diagnostic adapté."]),
  ("Préparer la recherche de fuite", ["Décrivez les pièces touchées et l’évolution des traces.", "Notez les travaux récents, épisodes de pluie ou changement de consommation.", "Demandez si un rapport écrit est possible pour le dossier."])
 ],
 "faq":[("Que faire en premier lors d’un dégât des eaux ?","Limiter le dommage si possible, sécuriser, prévenir les personnes concernées et documenter la situation."),("La recherche de fuite répare-t-elle le dégât ?","Pas forcément. Recherche, réparation et remise en état peuvent être trois étapes distinctes."),("Faut-il contacter l’assurance ?","Oui si un sinistre est possible, mais les modalités dépendent de votre contrat et de votre statut.")]
},
"contact": {
 "title":"Contact recherche fuite Angers : décrire une situation",
 "h1":"Décrire une fuite à Angers avant orientation",
 "meta":"Contact recherche fuite Angers : appelez le 09 72 14 55 77 ou préparez les informations utiles. Service indépendant, formulaire secondaire non connecté.",
 "lead":"Appelez le service indépendant d’orientation au 09 72 14 55 77 pour décrire une fuite, un dégât des eaux ou un besoin de rapport. Le formulaire reste secondaire et non connecté.",
 "sections":[
  ("Informations à préparer", ["Adresse ou quartier à Angers, sans publier d’information sensible.", "Type de bien : maison, appartement, local, copropriété.", "Symptôme principal : compteur, plafond, mur, sol, toiture, salle de bain.", "Urgence réelle : dégât actif, voisin touché, besoin planifié ou simple information."]),
  ("Ce que l’appel ne promet pas", ["Disponibilité à confirmer après qualification.", "Tarif à confirmer après devis ou qualification.", "Prise en charge assurance à confirmer avec l’assureur.", "Pas de transmission sans consentement clair."]),
  ("Pour faciliter une future mise en relation", ["Expliquez si vous êtes propriétaire, locataire, syndic ou gestionnaire.", "Précisez si l’assurance a déjà été contactée.", "Indiquez si un rapport écrit est nécessaire."])
 ],
 "faq":[("Le formulaire envoie-t-il des données ?","Non, le formulaire est secondaire et non connecté dans cette version locale."),("À quoi sert le numéro affiché ?","Oui, le numéro affiché sert à qualifier la demande avant toute mise en relation."),("Ce service est-il une entreprise de plomberie ?","Non, c’est un service indépendant d’information et d’orientation.")]
}
}

NEW_PAGES = {
"recherche-fuite-enterree-angers": ("Recherche fuite enterrée Angers : signes et méthodes", "Recherche de fuite enterrée à Angers : signes, limites et orientation", "Fuite enterrée à Angers : surconsommation, sol humide, canalisation extérieure, méthodes possibles et questions à poser avant devis.", ["Surconsommation inexpliquée malgré robinets fermés.", "Zone extérieure anormalement humide ou affaissement localisé.", "Baisse de pression ou compteur qui tourne la nuit."], ["Gaz traceur selon réseau et accès.", "Écoute électro-acoustique si conditions adaptées.", "Ouverture ciblée seulement après hypothèse technique."]),
"fuite-chauffage-angers": ("Fuite chauffage Angers : pression chaudière et réseau", "Fuite de chauffage à Angers : pression, traces et diagnostic", "Fuite chauffage Angers : baisse de pression chaudière, radiateurs, plancher chauffant, localisation de fuite et limites du diagnostic.", ["Pression chaudière qui baisse régulièrement.", "Trace humide près d’un radiateur ou d’un plancher chauffant.", "Appoint d’eau fréquent sur le circuit."], ["Contrôler pression et fréquence des appoints.", "Repérer zones chaudes/froides anormales.", "Demander si la méthode convient au chauffage." ]),
"fuite-plafond-angers": ("Fuite plafond Angers : tache, voisin, toiture ou canalisation", "Fuite au plafond à Angers : comprendre l’origine possible", "Fuite plafond Angers : tache, goutte, voisin du dessus, toiture, salle de bain, assurance et recherche de fuite adaptée.", ["Tache qui s’étend après douche, pluie ou utilisation d’un appareil.", "Goutte active ou auréole ancienne réactivée.", "Voisin, toiture ou réseau encastré à vérifier."], ["Photographier l’évolution.", "Prévenir voisin/syndic si copropriété.", "Ne pas repeindre avant diagnostic si assurance impliquée."]),
"fuite-compteur-eau-angers": ("Fuite compteur eau Angers : test simple et démarches", "Fuite au compteur d’eau à Angers : vérifier avant de conclure", "Fuite compteur eau Angers : test compteur, surconsommation, fuite après compteur, responsabilité et questions utiles avant intervention.", ["Compteur qui tourne sans consommation.", "Facture d’eau anormalement élevée.", "Suspicion entre compteur, réseau privé et équipements."], ["Fermer tous les points d’eau puis observer le compteur.", "Noter les index à heure fixe.", "Demander si la fuite est avant ou après compteur." ]),
"recherche-fuite-urgence-angers": ("Recherche fuite urgence Angers : agir avec prudence", "Recherche de fuite urgente à Angers : prioriser avec tri de la situation", "Recherche fuite urgence Angers : quoi faire en cas de dégât actif, qui prévenir et comment demander une orientation avec tri de la situation.", ["Dégât actif, voisin touché ou eau proche d’un équipement électrique.", "Besoin de limiter les dommages rapidement.", "Situation stressante nécessitant un tri clair."], ["Couper l’eau si possible.", "Contacter assurance/syndic/propriétaire selon cas.", "Appeler un professionnel adapté si danger ou dégât actif." ]),
"recherche-fuite-appartement-angers": ("Recherche fuite appartement Angers : locataire, propriétaire, syndic", "Recherche de fuite en appartement à Angers : rôle de chacun", "Recherche fuite appartement Angers : locataire, propriétaire, syndic, voisin du dessus, dégâts des eaux et préparation du dossier.", ["Tache plafond ou mur mitoyen.", "Voisin du dessus ou parties communes possibles.", "Besoin de coordination propriétaire/syndic."], ["Informer les personnes concernées par écrit.", "Documenter photos et dates.", "Clarifier qui commande la recherche selon le contexte." ]),
"recherche-fuite-maison-angers": ("Recherche fuite maison Angers : intérieur, extérieur, compteur", "Recherche de fuite en maison à Angers : symptômes et priorités", "Recherche fuite maison Angers : compteur, canalisation enterrée, salle de bain, toiture, chauffage et orientation indépendante.", ["Surconsommation ou compteur qui tourne.", "Humidité mur/sol, plafond ou salle de bain.", "Réseau extérieur ou chauffage à vérifier."], ["Identifier si la fuite semble intérieure ou extérieure.", "Préparer photos, compteur et historique.", "Demander les limites de la méthode proposée." ]),
"recherche-fuite-thermographie-angers": ("Thermographie fuite eau Angers : intérêt et limites", "Thermographie pour fuite d’eau à Angers : quand est-ce utile ?", "Thermographie fuite eau Angers : comprendre caméra thermique, cas utiles, limites et complément avec autres méthodes de localisation.", ["Écart de température suspect sur mur, sol ou plafond.", "Réseau chaud ou chauffage potentiellement concerné.", "Besoin de localiser une zone avant ouverture."], ["La caméra thermique ne voit pas tout.", "Elle complète souvent d’autres méthodes.", "Demandez comment les résultats seront interprétés." ])
}

def jsonld_for(slug, title, desc, faq):
    url = BASE + ('/' if slug == '' else f'/{slug}/')
    graph=[{"@type":"WebSite","@id":BASE+"/#website","url":BASE+"/","name":"Recherche Fuite Eau Angers","inLanguage":"fr-FR","description":"Service indépendant d’information et de mise en relation pour demandes de recherche de fuite à Angers et alentours."},
           {"@type":"WebPage","@id":url+"#webpage","url":url,"name":title,"description":desc,"isPartOf":{"@id":BASE+"/#website"},"inLanguage":"fr-FR"},
           {"@type":"BreadcrumbList","@id":url+"#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Accueil","item":BASE+"/"},{"@type":"ListItem","position":2,"name":title,"item":url}]},
           {"@type":"Service","@id":url+"#service","name":title,"serviceType":"Information et orientation pour recherche de fuite d’eau","areaServed":{"@type":"City","name":"Angers"},"provider":{"@id":BASE+"/#website"},"description":"Service indépendant d’information et d’orientation, avec qualification préalable."}]
    if faq:
        graph.append({"@type":"FAQPage","@id":url+"#faq","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]})
    return json.dumps({"@context":"https://schema.org","@graph":graph},ensure_ascii=False,separators=(',',':'))

def related(exclude):
    items=[]
    for href,label in COMMON_LINKS:
        if href.strip('/') != exclude:
            items.append(f'<li><a href="{href}">{html.escape(label)}</a></li>')
    for slug in list(NEW_PAGES)[:4]:
        if slug != exclude:
            items.append(f'<li><a href="/{slug}/">{html.escape(NEW_PAGES[slug][1])}</a></li>')
    return '<section class="section alt"><div class="wrap"><h2>Situations proches à lire aussi</h2><ul class="check">' + ''.join(items[:8]) + '</ul></div></section>'

def render(slug, cfg):
    title,h1,meta,lead,sections,faq = cfg['title'],cfg['h1'],cfg['meta'],cfg['lead'],cfg['sections'],cfg['faq']
    url = BASE + f'/{slug}/'
    head=f'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title><meta name="description" content="{html.escape(meta)}"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"><link rel="stylesheet" href="/styles.css">
<!-- BEGIN AGENT SEO HEAD -->
<link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:locale" content="fr_FR"><meta property="og:site_name" content="Recherche Fuite Eau Angers"><meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(meta)}"><meta property="og:url" content="{url}"><meta name="twitter:card" content="summary"><meta name="twitter:title" content="{html.escape(title)}"><meta name="twitter:description" content="{html.escape(meta)}">
<script type="application/ld+json">{jsonld_for(slug,title,meta,faq)}</script>
<!-- END AGENT SEO HEAD --></head><body>'''
    toc=''.join(f'<a href="#{i}">{html.escape(h)}</a>' for i,(h,_) in enumerate(sections,1)) + '<a href="/contact/">Décrire ma fuite</a>'
    body=f'{NAV}<main><section class="pagehead"><div class="wrap"><div class="crumb"><a href="/">Accueil</a> / {html.escape(h1)}</div><h1>{html.escape(h1)}</h1><p class="lead">{html.escape(lead)}</p><div class="toc">{toc}</div></div></section>'
    if slug == '':
        body += f'<section class="section urgent-intake"><div class="wrap"><div class="card call-card"><p class="eyebrow">Fuite en cours, compteur qui tourne, dégât des eaux</p><h2>Commencez par l’appel si la situation évolue.</h2><p>Un appel court sert à qualifier ce qui se passe, le niveau d’urgence, le contexte assurance ou syndic, puis les informations à transmettre.</p><p class="phone-big"><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p><p><a class="btn" href="tel:{PHONE_TEL}">Appeler maintenant</a> <a class="btn secondary" href="/contact/">Préparer les informations</a></p><p class="note">Aucune disponibilité n’est annoncée sans qualification préalable. Si la zone présente un danger électrique ou un dégât actif important, sécurisez d’abord la situation.</p></div></div></section>'
        body += '<section class="visual-seo" aria-label="Photo de recherche de fuite"><div class="wrap"><figure class="seo-figure"><img src="/assets/images/artisan-recherche-fuite.png" alt="Artisan effectuant une recherche de fuite d’eau sur une canalisation" width="1024" height="576" loading="eager" decoding="async"><figcaption>Recherche de fuite sur canalisation : contrôle visuel, zone humide et matériel de diagnostic.</figcaption></figure></div></section>'
    for i,(h, bullets) in enumerate(sections,1):
        cls='section alt' if i%2 else 'section'
        body += f'<section class="{cls}" id="{i}"><div class="wrap"><h2>{html.escape(h)}</h2><div class="grid">'
        for b in bullets:
            body += f'<article class="card"><p>{html.escape(b)}</p></article>'
        body += '</div></div></section>'
    body += '<section class="section"><div class="wrap"><h2>Questions fréquentes</h2><div class="grid">'
    for q,a in faq:
        body += f'<article class="card"><h3>{html.escape(q)}</h3><p>{html.escape(a)}</p></article>'
    body += '</div></div></section>' + related(slug)
    body += f'<section class="section"><div class="wrap"><div class="card"><h2>Préparer l’appel</h2><p>Pour gagner du temps, préparez la ville/quartier, le type de fuite, l’urgence, votre statut et le besoin éventuel d’un rapport assurance.</p><p><a class="btn" href="tel:{PHONE_TEL}">Appeler le {PHONE_DISPLAY}</a> <a class="btn ghost" href="/contact/">Voir les informations à préparer</a></p><p class="note">Le numéro affiché sert à qualifier la demande avant toute mise en relation.</p></div></div></section></main>{FOOT}</body></html>\n'
    return head+body

def render_new(slug, data):
    title,h1,meta,signs,steps=data
    cfg={"title":title,"h1":h1,"meta":meta,"lead":"Page d’information locale pour préparer une demande liée à ce type de fuite à Angers. Le site reste un service indépendant d’orientation, avec qualification préalable.","sections":[("Signes typiques", signs),("Actions utiles avant diagnostic", steps),("Questions à poser avant devis", ["Quelle méthode de recherche est adaptée à ce symptôme ?", "Le rapport écrit est-il inclus si assurance ou syndic impliqué ?", "Quelles sont les limites si la fuite n’est pas localisée immédiatement ?", "La recherche est-elle distincte de la réparation ?"])],"faq":[("Cette page remplace-t-elle un diagnostic ?","Non. Elle aide à préparer les informations avant l’avis d’un professionnel qualifié."),("Une intervention rapide est-elle annoncée ?","Non. La disponibilité doit être confirmée après qualification de la situation."),("Pourquoi appeler avant de choisir une méthode ?","Parce que le symptôme, l’accès et le contexte assurance orientent fortement la méthode pertinente.")]}
    return render(slug,cfg)

# Write P0 pages and new pages, with flat/folder sync
for slug,cfg in PAGES.items():
    content=render(slug,cfg)
    (SITE/slug).mkdir(exist_ok=True)
    (SITE/slug/'index.html').write_text(content,encoding='utf-8')
    (SITE/f'{slug}.html').write_text(content,encoding='utf-8')
for slug,data in NEW_PAGES.items():
    content=render_new(slug,data)
    (SITE/slug).mkdir(exist_ok=True)
    (SITE/slug/'index.html').write_text(content,encoding='utf-8')
    (SITE/f'{slug}.html').write_text(content,encoding='utf-8')

# Homepage hub
home_cfg={"title":"Recherche fuite eau Angers : fuite active, compteur, dégât des eaux", "h1":"Recherche de fuite d’eau à Angers", "meta":"Recherche de fuite d’eau à Angers : appel de qualification pour fuite active, compteur qui tourne, dégât des eaux, méthode, prix et assurance.", "lead":"Si l’eau coule encore, si le compteur tourne sans consommation ou si un voisin est touché, l’objectif est simple : limiter les dégâts, qualifier la situation et joindre le bon interlocuteur.", "sections":[("À traiter en premier", ["Eau qui coule encore : coupez l’arrivée d’eau si elle est accessible.", "Eau proche d’une prise ou d’un tableau : sécurisez la zone et évitez tout contact électrique.", "Voisin, plafond ou copropriété touchés : prévenez la personne concernée et gardez des photos datées.", "Compteur qui tourne sans robinet ouvert : notez l’index et l’heure avant l’appel." ]),("Pourquoi appeler", ["Décrire rapidement le symptôme principal : compteur, mur, plafond, sol, salle de bain, toiture ou réseau enterré.", "Identifier si la demande relève d’une urgence, d’un dossier assurance ou d’un diagnostic planifié.", "Préparer les informations nécessaires avant une éventuelle méthode de localisation adaptée.", "Éviter de perdre du temps avec une méthode ou un interlocuteur inadapté." ]),("Informations à avoir sous la main", ["Adresse ou quartier à Angers, type de logement et statut : propriétaire, locataire, syndic ou gestionnaire.", "Moment d’apparition, évolution de la trace, présence d’eau active ou surconsommation.", "Photos, relevé compteur, échanges avec assurance, propriétaire, voisin ou syndic."] )], "faq":[("Quand faut-il appeler ?","Appelez si la fuite semble active, si le compteur tourne sans consommation, si un dégât des eaux progresse ou si un voisin est concerné."),("Que faire avant l’appel ?","Coupez l’eau si possible, sécurisez la zone humide, prenez des photos et notez les informations utiles : compteur, pièce touchée, statut du logement."),("Est-ce une entreprise de plomberie ?","Non. C’est un service indépendant d’information et d’orientation pour qualifier la demande avant une éventuelle mise en relation.")]}
(SITE/'index.html').write_text(render('', home_cfg).replace(BASE+'//',BASE+'/'),encoding='utf-8')

# Methodologie hub
method_cfg={"title":"Méthodologie : fonctionnement du service d’orientation", "h1":"Méthodologie du site", "meta":"Méthodologie du service indépendant : information, orientation, limites, qualification des demandes et critères de contenu local.", "lead":"Cette page explique comment le site traite les demandes de recherche de fuite à Angers : information utile, qualification de la situation et orientation éventuelle.", "sections":[("Ce que le site fait", ["Organiser l’information utile par situation : fuite, assurance, prix, méthodes.", "Aider à préparer un appel ou une demande claire.", "Qualifier le symptôme, le niveau d’urgence et le contexte logement.", "Conserver un langage prudent tant qu’aucun partenaire n’est validé." ]),("Limites du service", ["Pas d’adresse locale publiée sans vérification.", "Pas d’avis clients affichés sans source vérifiable.", "Disponibilité, tarif et prise en charge assurance à confirmer après qualification.", "Le site ne se présente pas comme une entreprise de plomberie." ]),("Contrôle qualité", ["Chaque page doit avoir title, meta, H1, canonical et JSON-LD parsable.", "Les pages importantes doivent recevoir des liens internes contextuels.", "Les contenus doivent aider un propriétaire, locataire ou syndic à Angers."] )], "faq":[("Pourquoi éviter LocalBusiness ?","Parce que le site ne doit pas publier une adresse, des avis ou une identité d’entreprise sans vérification."),("Pourquoi parler d’orientation ?","Parce que le site sert à qualifier et diriger les demandes avant une éventuelle mise en relation."),("Comment le site évoluera ?","Le numéro et le parcours d’appel doivent rester testés avant toute évolution du routage.")]}
for slug in ['methodologie']:
    content=render(slug,method_cfg)
    (SITE/slug).mkdir(exist_ok=True)
    (SITE/slug/'index.html').write_text(content,encoding='utf-8')
    (SITE/f'{slug}.html').write_text(content,encoding='utf-8')

# Sitemap canonical folder URLs only
slugs=[''] + sorted(set(list(PAGES.keys())+list(NEW_PAGES.keys())+['detection-fuite-eau-angers','fuite-apres-compteur-angers','fuite-canalisation-angers','fuite-salle-de-bain-angers','fuite-toiture-angers','humidite-mur-angers','mentions-legales','methodologie','politique-confidentialite','recherche-fuite-avrille','recherche-fuite-les-ponts-de-ce','recherche-fuite-maine-et-loire','recherche-fuite-trelaze']))
priorities={"":1.0,"recherche-fuite-eau-angers":1.0,"contact":0.9,"recherche-fuite-non-destructive-angers":0.9,"prix-recherche-fuite-eau-angers":0.9,"recherche-fuite-assurance-angers":0.9,"degat-des-eaux-angers":0.8}
urls=[]
for slug in slugs:
    loc=BASE+'/' if slug=='' else f'{BASE}/{slug}/'
    pr=priorities.get(slug,0.7)
    urls.append(f'  <url><loc>{loc}</loc><priority>{pr:.1f}</priority></url>')
sitemap='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+'\n'.join(urls)+'\n</urlset>\n'
(SITE/'sitemap.xml').write_text(sitemap,encoding='utf-8')
(SITE/'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: https://recherche-fuite-eau-angers.fr/sitemap.xml\n',encoding='utf-8')
print(f'Wrote {len(PAGES)} P0 pages, {len(NEW_PAGES)} new topical pages, homepage/methodologie, sitemap with {len(slugs)} URLs.')
