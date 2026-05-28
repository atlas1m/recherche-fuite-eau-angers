#!/usr/bin/env python3
from pathlib import Path
import json, html

SITE = Path(__file__).resolve().parents[1]
BASE = "https://recherche-fuite-eau-angers.fr"
PHONE_DISPLAY = "09 72 14 55 77"
PHONE_TEL = "+339****5577"

NAV = '<header class="nav"><div class="wrap navin"><a class="brand" href="/recherche-fuite-eau-angers/"><span class="mark">RF</span><span>Recherche Fuite Angers</span></a><nav class="links"><a href="/recherche-fuite-eau-angers/">Guide</a><a href="/recherche-fuite-non-destructive-angers/">Sans casse</a><a href="/recherche-fuite-assurance-angers/">Assurance</a><a href="/prix-recherche-fuite-eau-angers/">Prix</a><a class="btn phone-primary" href="tel:+339****5577">Appeler maintenant</a><a class="nav-form" href="/contact/">Formulaire</a></nav></div></header>'
FOOT = '<footer class="foot"><div class="wrap"><p>Service indépendant d’information et de mise en relation. Pas une entreprise de plomberie ou de recherche de fuite. Informations indicatives, à faire confirmer par un professionnel qualifié.</p><p><a href="/mentions-legales/">Mentions légales</a> · <a href="/politique-confidentialite/">Confidentialité</a> · <a href="/methodologie/">Méthodologie</a></p></div></footer><a class="sticky-call" href="tel:+339****5577" aria-label="Appeler le service d’orientation au 09 72 14 55 77">Appeler maintenant : 09 72 14 55 77</a>'

COMMON_LINKS = [
    ("/recherche-fuite-eau-angers/", "guide recherche de fuite à Angers"),
    ("/recherche-fuite-non-destructive-angers/", "détection sans casse"),
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
 "meta":"Guide indépendant pour recherche de fuite d’eau à Angers : symptômes, recherche de fuite non destructive, assurance, prix et orientation avec prudence.",
 "lead":"Ce guide aide propriétaires, locataires et syndics à décrire une fuite d’eau à Angers avant de demander une recherche. Le site est un service indépendant d’information et d’orientation : il ne prétend pas être une entreprise locale de plomberie.",
 "sections":[
  ("Symptômes à prendre au sérieux", ["Compteur qui tourne alors que tous les robinets sont fermés.", "Tache au plafond ou mur humide qui progresse.", "Baisse de pression, odeur d’humidité ou sol anormalement chaud.", "Dégât des eaux chez un voisin, en copropriété ou après une période de pluie."]),
  ("Que faire avant d’appeler", ["Coupez l’eau si la fuite est active et accessible.", "Photographiez les traces visibles et notez l’heure d’apparition.", "Relevez le compteur avant/après une période sans consommation.", "Préparez votre statut : propriétaire, locataire, syndic ou gestionnaire."]),
  ("Méthodes possibles", ["Caméra thermique pour repérer certains écarts de température.", "Gaz traceur ou électro-acoustique selon le réseau et l’accès.", "Humidimètre et inspection visuelle pour cadrer la zone.", "La bonne méthode dépend du bâtiment : aucune technique n’est universelle."]),
  ("Limites et clarté", ["Aucun délai, tarif ou remboursement assurance n’est annoncé par ce site avant qualification.", "L’objectif est de préparer une demande claire et d’éviter les mauvaises orientations.", "Un professionnel qualifié doit confirmer le diagnostic et le devis."])
 ],
 "faq":[("Qui appeler pour une recherche de fuite à Angers ?","Vous pouvez appeler un professionnel spécialisé ou utiliser ce service d’orientation indépendant pour préparer la demande. Ce site ne se présente pas comme une entreprise de plomberie."),("Une recherche de fuite est-elle toujours sans casse ?","Non. Les méthodes non destructives visent à limiter les ouvertures inutiles, mais leur pertinence dépend de l’accès, du type de réseau et du symptôme."),("Faut-il appeler l’assurance avant la recherche ?","En cas de dégât des eaux, il est prudent de contacter votre assurance ou syndic. La prise en charge dépend du contrat et n’est pas garantie.")]
},
"recherche-fuite-non-destructive-angers": {
 "title":"Recherche fuite non destructive Angers : détection sans casse",
 "h1":"Recherche de fuite non destructive à Angers : détecter sans casse",
 "meta":"Recherche de fuite non destructive à Angers : détection sans casse, caméra thermique, gaz traceur, électroacoustique, limites et questions à poser.",
 "lead":"La recherche de fuite non destructive désigne les méthodes utilisées pour détecter l’origine d’une fuite sans casser inutilement les murs, sols ou plafonds. Le choix dépend du réseau, du matériau, de l’accès et des symptômes.",
 "sections":[
  ("Quand c’est pertinent", ["Fuite invisible après compteur ou sur réseau encastré.", "Humidité sans origine claire dans un mur, sol ou plafond.", "Besoin de limiter la casse avant réparation.", "Dossier assurance où un rapport peut aider à expliquer la situation."]),
  ("Méthodes fréquentes", ["Caméra thermique : repère certains écarts de température.", "Gaz traceur : utile selon accessibilité et étanchéité du réseau.", "Électro-acoustique : écoute de bruits de fuite sur certains réseaux.", "Inspection caméra : plutôt pour évacuations ou canalisations accessibles."]),
  ("Questions à poser", ["Quelle méthode est prévue et pourquoi ?", "Le rapport écrit est-il inclus ?", "Que se passe-t-il si la fuite n’est pas localisable sans ouverture ?", "Le devis distingue-t-il recherche, réparation et remise en état ?"])
 ],
 "faq":[("Une recherche non destructive évite-t-elle toujours de casser ?","Non. Elle réduit le risque d’ouverture inutile, mais certaines situations exigent une ouverture ou une réparation ciblée."),("Quelle méthode est la meilleure ?","Il n’y a pas de méthode universelle : caméra thermique, gaz traceur ou écoute dépendent du réseau et du symptôme."),("Un rapport est-il nécessaire ?","Il peut être utile pour l’assurance ou le syndic, mais son usage dépend du dossier et du contrat.")]
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
"fuite-chauffage-angers": ("Fuite chauffage Angers : pression chaudière et réseau", "Fuite de chauffage à Angers : pression, traces et diagnostic", "Fuite chauffage Angers : baisse de pression chaudière, radiateurs, plancher chauffant, recherche de fuite non destructive et limites du diagnostic.", ["Pression chaudière qui baisse régulièrement.", "Trace humide près d’un radiateur ou d’un plancher chauffant.", "Appoint d’eau fréquent sur le circuit."], ["Contrôler pression et fréquence des appoints.", "Repérer zones chaudes/froides anormales.", "Demander si la méthode convient au chauffage." ]),
"fuite-plafond-angers": ("Fuite plafond Angers : tache, voisin, toiture ou canalisation", "Fuite au plafond à Angers : comprendre l’origine possible", "Fuite plafond Angers : tache, goutte, voisin du dessus, toiture, salle de bain, assurance et recherche de fuite adaptée.", ["Tache qui s’étend après douche, pluie ou utilisation d’un appareil.", "Goutte active ou auréole ancienne réactivée.", "Voisin, toiture ou réseau encastré à vérifier."], ["Photographier l’évolution.", "Prévenir voisin/syndic si copropriété.", "Ne pas repeindre avant diagnostic si assurance impliquée."]),
"fuite-compteur-eau-angers": ("Fuite compteur eau Angers : test simple et démarches", "Fuite au compteur d’eau à Angers : vérifier avant de conclure", "Fuite compteur eau Angers : test compteur, surconsommation, fuite après compteur, responsabilité et questions utiles avant intervention.", ["Compteur qui tourne sans consommation.", "Facture d’eau anormalement élevée.", "Suspicion entre compteur, réseau privé et équipements."], ["Fermer tous les points d’eau puis observer le compteur.", "Noter les index à heure fixe.", "Demander si la fuite est avant ou après compteur." ]),
"fuite-sous-carrelage-angers": ("Fuite sous carrelage Angers : signes et détection sans casse", "Fuite sous carrelage à Angers : signes, dalle et détection sans casse", "Fuite sous carrelage Angers : humidité, sol chaud, compteur qui tourne, fuite sous dalle, caméra thermique, gaz traceur et limites sans casse.", ["Carrelage anormalement chaud, froid ou humide selon le réseau concerné.", "Joints qui noircissent, odeur d’humidité ou auréole en bas de mur.", "Compteur qui tourne sans consommation ou baisse de pression inexpliquée.", "Fuite sous dalle possible si le symptôme revient malgré un nettoyage de surface."], ["Ne cassez pas le sol avant d’avoir cadré les signes et le réseau probable.", "Préparez photos, relevés de compteur et pièces concernées avant l’appel.", "Demandez si caméra thermique, gaz traceur ou électroacoustique est pertinent dans ce cas.", "Faites confirmer les limites : une recherche sans casse réduit les ouvertures inutiles, sans garantir qu’aucune ouverture ne sera nécessaire." ]),
"recherche-fuite-copropriete-angers": ("Recherche fuite copropriété Angers : syndic, voisin, parties communes", "Recherche de fuite en copropriété à Angers : syndic, voisin et dossier", "Recherche fuite copropriété Angers : dégât des eaux, syndic, parties communes, voisin touché, rapport et informations à préparer.", ["Tache au plafond ou mur mitoyen avec voisin potentiellement concerné.", "Parties communes, colonne, toiture ou réseau encastré à clarifier avec le syndic.", "Besoin d’un rapport écrit pour assurance, gestionnaire ou conseil syndical.", "Historique utile : dates, photos, échanges et évolution des traces."], ["Prévenez le syndic ou gestionnaire si les parties communes ou un voisin peuvent être concernés.", "Conservez photos, messages et relevés utiles avant nettoyage ou remise en état.", "Demandez si le rapport précise la méthode utilisée, la zone contrôlée et les limites du diagnostic.", "Faites distinguer recherche, réparation et remise en état dans les échanges." ]),
"recherche-fuite-syndic-angers": ("Recherche fuite syndic Angers : rapport et coordination immeuble", "Recherche de fuite pour syndic à Angers : cadrer la demande", "Recherche fuite syndic Angers : immeuble, copropriété, parties communes, voisin, rapport technique et qualification de la situation.", ["Signalement répété d’un occupant, propriétaire ou gestionnaire.", "Dégât des eaux pouvant impliquer parties communes, logement voisin ou toiture.", "Besoin de centraliser les informations avant de missionner une recherche.", "Demande de rapport exploitable pour assurance ou suivi de copropriété."], ["Rassemblez étage, logement concerné, pièces touchées et contacts disponibles.", "Demandez aux occupants des photos datées et une description de l’évolution.", "Clarifiez si la demande concerne recherche seule, réparation ou remise en état.", "Gardez une trace écrite des décisions et limites communiquées." ]),
"fuite-sous-evier-angers": ("Fuite sous évier Angers : siphon, robinet, meuble humide", "Fuite sous évier à Angers : identifier les signes avant diagnostic", "Fuite sous évier Angers : meuble humide, siphon, robinet d’arrêt, évacuation, canalisation et informations utiles avant appel.", ["Meuble sous évier humide, odeur persistante ou gouttes après usage.", "Siphon, flexible, robinet d’arrêt ou évacuation à observer sans démontage risqué.", "Trace au sol ou mur adjacent après vaisselle, lave-vaisselle ou période d’absence.", "Compteur qui tourne si la fuite concerne une alimentation et non seulement une évacuation."], ["Coupez l’eau localement si un robinet d’arrêt est accessible et que la fuite est active.", "Évitez de démonter si le meuble, le sol ou l’électricité proche rendent la situation risquée.", "Photographiez la zone sèche puis humide si le phénomène revient.", "Précisez si l’eau apparaît pendant l’usage, en continu ou seulement à certains moments." ]),
"fuite-douche-angers": ("Fuite douche Angers : joint, receveur, mur adjacent", "Fuite de douche à Angers : signes, voisin et diagnostic", "Fuite douche Angers : joint, receveur, bonde, mur adjacent, plafond voisin, dégât des eaux et recherche de fuite adaptée.", ["Humidité après douche, joint dégradé, mur adjacent marqué ou sol qui gondole.", "Trace au plafond du voisin ou dans une pièce attenante.", "Bonde, receveur, colonne encastrée ou évacuation à distinguer.", "Symptôme intermittent qui apparaît surtout après utilisation."], ["Limitez l’usage de la douche si le dégât progresse ou touche un voisin.", "Prenez des photos avant séchage complet et notez les heures d’utilisation.", "Prévenez propriétaire, voisin ou syndic selon le contexte du logement.", "Demandez quelle méthode permet de distinguer joint, évacuation et alimentation." ]),
"rapport-recherche-fuite-assurance-angers": ("Rapport recherche fuite assurance Angers : dossier dégât des eaux", "Rapport de recherche de fuite pour assurance à Angers", "Rapport recherche fuite assurance Angers : dégât des eaux, méthode utilisée, constat, photos, syndic et prise en charge à confirmer.", ["Assurance, syndic ou propriétaire demande un écrit après dégât des eaux.", "Besoin de décrire la zone contrôlée, la méthode utilisée et les limites constatées.", "Photos, dates, échanges et déclaration de sinistre peuvent être utiles au dossier.", "Prise en charge à confirmer avec l’assureur selon contrat et circonstances."], ["Demandez avant intervention si un rapport écrit est prévu et sous quel délai.", "Vérifiez que le document distingue observations, hypothèses et limites du diagnostic.", "Gardez les justificatifs et échanges avec assurance, syndic ou propriétaire.", "Ne considérez pas la prise en charge comme acquise sans confirmation de l’assureur." ]),
"recherche-fuite-urgence-angers": ("Recherche fuite urgence Angers : agir avec prudence", "Recherche de fuite urgente à Angers : prioriser avec tri de la situation", "Recherche fuite urgence Angers : quoi faire en cas de dégât actif, qui prévenir et comment demander une orientation avec tri de la situation.", ["Dégât actif, voisin touché ou eau proche d’un équipement électrique.", "Besoin de limiter les dommages rapidement.", "Situation stressante nécessitant un tri clair."], ["Couper l’eau si possible.", "Contacter assurance/syndic/propriétaire selon cas.", "Appeler un professionnel adapté si danger ou dégât actif." ]),
"recherche-fuite-appartement-angers": ("Recherche fuite appartement Angers : locataire, propriétaire, syndic", "Recherche de fuite en appartement à Angers : rôle de chacun", "Recherche fuite appartement Angers : locataire, propriétaire, syndic, voisin du dessus, dégâts des eaux et préparation du dossier.", ["Tache plafond ou mur mitoyen.", "Voisin du dessus ou parties communes possibles.", "Besoin de coordination propriétaire/syndic."], ["Informer les personnes concernées par écrit.", "Documenter photos et dates.", "Clarifier qui commande la recherche selon le contexte." ]),
"recherche-fuite-maison-angers": ("Recherche fuite maison Angers : intérieur, extérieur, compteur", "Recherche de fuite en maison à Angers : symptômes et priorités", "Recherche fuite maison Angers : compteur, canalisation enterrée, salle de bain, toiture, chauffage et orientation indépendante.", ["Surconsommation ou compteur qui tourne.", "Humidité mur/sol, plafond ou salle de bain.", "Réseau extérieur ou chauffage à vérifier."], ["Identifier si la fuite semble intérieure ou extérieure.", "Préparer photos, compteur et historique.", "Demander les limites de la méthode proposée." ]),
"recherche-fuite-thermographie-angers": ("Thermographie fuite eau Angers : intérêt et limites", "Thermographie pour fuite d’eau à Angers : quand est-ce utile ?", "Thermographie fuite eau Angers : comprendre caméra thermique, cas utiles, limites et complément avec autres méthodes non destructives.", ["Écart de température suspect sur mur, sol ou plafond.", "Réseau chaud ou chauffage potentiellement concerné.", "Besoin de localiser une zone avant ouverture."], ["La caméra thermique ne voit pas tout.", "Elle complète souvent d’autres méthodes.", "Demandez comment les résultats seront interprétés." ])
}

def jsonld_for(slug, title, desc, faq):
    url = BASE + ('/' if slug == '' else f'/{slug}/')
    graph=[{"@type":"WebSite","@id":BASE+"/#website","url":BASE+"/","name":"Angers Détection Fuite","inLanguage":"fr-FR","description":"Service indépendant d’information et de mise en relation pour demandes de recherche de fuite à Angers et alentours."},
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
        is_ordered_action = h.startswith('À traiter') or 'Actions utiles' in h
        list_tag = 'ol' if is_ordered_action else 'ul'
        list_class = 'grid action-steps' if is_ordered_action else 'grid list-cards'
        body += f'<section class="{cls}" id="{i}"><div class="wrap"><h2>{html.escape(h)}</h2><{list_tag} class="{list_class}">'
        for idx,b in enumerate(bullets,1):
            if is_ordered_action:
                body += f'<li class="card"><span class="step-num" aria-hidden="true">{idx}</span><p>{html.escape(b)}</p></li>'
            else:
                body += f'<li class="card"><p>{html.escape(b)}</p></li>'
        body += f'</{list_tag}></div></section>'
    body += '<section class="section"><div class="wrap"><h2>Questions fréquentes</h2><ul class="grid list-cards faq-list">'
    for q,a in faq:
        body += f'<li class="card"><h3>{html.escape(q)}</h3><p>{html.escape(a)}</p></li>'
    body += '</ul></div></section>' + related(slug)
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
home_cfg={"title":"Fuite active à Angers : compteur, plafond, dégât des eaux", "h1":"Recherche de fuite & détection non destructive à Angers", "meta":"Fuite active à Angers : appel de qualification pour compteur qui tourne, plafond touché, dégât des eaux, méthode, prix et assurance.", "lead":"Si l’eau coule encore, si le compteur tourne sans consommation ou si un voisin est touché, l’objectif est simple : limiter les dégâts, qualifier la situation et joindre le bon interlocuteur.", "sections":[("À traiter en premier", ["Eau qui coule encore : coupez l’arrivée d’eau si elle est accessible.", "Eau proche d’une prise ou d’un tableau : sécurisez la zone et évitez tout contact électrique.", "Voisin, plafond ou copropriété touchés : prévenez la personne concernée et gardez des photos datées.", "Compteur qui tourne sans robinet ouvert : notez l’index et l’heure avant l’appel." ]),("Pourquoi appeler", ["Décrire rapidement le symptôme principal : compteur, mur, plafond, sol, salle de bain, toiture ou réseau enterré.", "Identifier si la demande relève d’une urgence, d’un dossier assurance ou d’un diagnostic planifié.", "Préparer les informations nécessaires avant une éventuelle recherche de fuite non destructive.", "Éviter de perdre du temps avec une méthode ou un interlocuteur inadapté." ]),("Informations à avoir sous la main", ["Adresse ou quartier à Angers, type de logement et statut : propriétaire, locataire, syndic ou gestionnaire.", "Moment d’apparition, évolution de la trace, présence d’eau active ou surconsommation.", "Photos, relevé compteur, échanges avec assurance, propriétaire, voisin ou syndic."] )], "faq":[("Quand faut-il appeler ?","Appelez si la fuite semble active, si le compteur tourne sans consommation, si un dégât des eaux progresse ou si un voisin est concerné."),("Que faire avant l’appel ?","Coupez l’eau si possible, sécurisez la zone humide, prenez des photos et notez les informations utiles : compteur, pièce touchée, statut du logement."),("Est-ce une entreprise de plomberie ?","Non. C’est un service indépendant d’information et d’orientation pour qualifier la demande avant une éventuelle mise en relation.")]}
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

# -----------------------------------------------------------------------------
# AutoglassNOLA structural overlay
# Reference site: https://www.autoglassnola.com/
# Maxime requested this exact local lead-gen structure, not a generic decorative
# landing page: narrow phone/nav header, immediate two-column hero with left
# service heading + worker image + call button and right quote form, H1/intro
# block below, alternating image/text service rows, FAQ links, service-area block,
# secondary contact/image row, proof/transparency block, and compact footer.
# -----------------------------------------------------------------------------

REFERENCE_NAV = [
    ('/', 'Accueil'),
    ('/services/', 'Services'),
    ('/about/', 'À propos'),
    ('/locations/', 'Secteurs'),
    ('/contact/', 'Contact'),
]

SERVICE_DROPDOWN = [
    ('/recherche-fuite-eau-angers/', 'Recherche de fuite à Angers'),
    ('/recherche-fuite-non-destructive-angers/', 'Détection non destructive'),
    ('/fuite-apres-compteur-angers/', 'Fuite après compteur'),
    ('/degat-des-eaux-angers/', 'Dégât des eaux'),
    ('/prix-recherche-fuite-eau-angers/', 'Prix recherche de fuite'),
    ('/recherche-fuite-urgence-angers/', 'Urgence fuite'),
    ('/rapport-recherche-fuite-assurance-angers/', 'Rapport assurance'),
]

SERVICE_ROWS = [
    ('/recherche-fuite-eau-angers/', 'Recherche de fuite à Angers', 'Une fuite visible n’indique pas toujours son origine. L’objectif est de distinguer ce qui relève d’un écoulement actif, d’une infiltration ancienne, d’un réseau encastré ou d’un dégât déclaré trop vite. Avant toute orientation, la demande doit préciser la pièce touchée, l’évolution des traces, le statut du logement et le besoin éventuel d’un rapport.'),
    ('/recherche-fuite-non-destructive-angers/', 'Détection non destructive', 'Les méthodes dites sans casse servent à réduire les ouvertures inutiles, pas à garantir une localisation magique. Selon le cas, caméra thermique, gaz traceur, écoute électro-acoustique, humidimètre ou inspection vidéo peuvent aider à cibler une zone. Le bon choix dépend du réseau, de l’accès, du matériau et de la cohérence entre symptôme et historique.'),
    ('/fuite-apres-compteur-angers/', 'Fuite après compteur', 'Quand le compteur tourne sans consommation, il faut d’abord cadrer le test : robinets fermés, appareils à l’arrêt, index noté à heure fixe. Une surconsommation peut venir d’un réseau privé, d’un équipement sanitaire, d’un chauffage ou d’une fuite extérieure. La page aide à préparer les relevés et les informations utiles avant diagnostic.'),
    ('/degat-des-eaux-angers/', 'Dégât des eaux & assurance', 'Un dégât des eaux implique souvent plusieurs personnes : occupant, propriétaire, voisin, syndic et assurance. La priorité est de limiter les dommages, garder des photos datées, noter les échanges importants et demander ce que l’assureur attend comme justificatif. Un rapport peut aider le dossier, mais son rôle dépend du contrat et du contexte.'),
    ('/prix-recherche-fuite-eau-angers/', 'Prix d’une recherche de fuite', 'Le prix varie selon l’accès, la méthode, le déplacement, le rapport demandé, l’urgence réelle et la séparation entre recherche, réparation et remise en état. Cette page ne publie pas de montant standard, car un tarif utile doit être rattaché à une situation précise. Elle sert surtout à savoir quelles questions poser avant d’accepter un devis.'),
    ('/recherche-fuite-urgence-angers/', 'Urgence fuite : quoi faire', 'En urgence, le bon réflexe n’est pas de multiplier les appels au hasard. Il faut couper l’eau si possible, éviter les zones électriques humides, prévenir voisin ou syndic si nécessaire, puis décrire clairement ce qui évolue. L’appel sert à trier : danger immédiat, dégât actif, dossier assurance ou diagnostic pouvant être planifié.'),
]

# Template lock-in: copy the reference lead-gen template media language: photo blocks,
# not invented vector/illustration cards. Keep editorial depth and visual variety;
# each row below maps to a distinct photographic situation asset, and the audit enforces this.
TEMPLATE_WORD_TARGET = (900, 1400)
IMAGE_LIBRARY = {
    'hero': ('/assets/images/fuite-hero-diagnostic.jpg', 'Technicien préparant un diagnostic de recherche de fuite en salle de bain'),
    'visual': ('/assets/images/fuite-canalisation-controle.jpg', 'Contrôle photographique d’un raccord de canalisation'),
    'service': [
        ('/assets/images/fuite-humidimetre-platre.jpg', 'Humidimètre utilisé sur un mur en plâtre avec trace d’humidité'),
        ('/assets/images/fuite-thermographie-mur.jpg', 'Caméra thermique utilisée près d’un mur humide'),
        ('/assets/images/fuite-compteur-releve.jpg', 'Relevé de compteur d’eau pour vérifier une surconsommation'),
        ('/assets/images/fuite-rapport-assurance.jpg', 'Préparation d’un dossier assurance après dégât des eaux'),
        ('/assets/images/fuite-devis-prix.jpg', 'Éléments de chiffrage et matériel de plomberie'),
        ('/assets/images/fuite-coupure-vanne.jpg', 'Coupure d’une vanne d’arrivée d’eau en situation urgente'),
    ],
    'thumbs': [
        ('/assets/images/fuite-controle-humidite.jpg', 'Contrôle visuel de traces d’humidité'),
        ('/assets/images/fuite-inspection-canalisation.jpg', 'Inspection de canalisation en salle de bain'),
        ('/assets/images/fuite-diagnostic-non-destructif.jpg', 'Diagnostic avec outil de plomberie en intérieur'),
    ],
}

# Final template matrix: each strategic keyword/page gets a deterministic photo slot.
# Provenance and prompt notes live in the Hermes Obsidian vault only; repo contains runtime assets.
IMAGE_BY_SLUG = {
    '': IMAGE_LIBRARY['hero'],
    # Top-level pages must not reuse the same hero: screenshots expose repetition immediately.
    'services': ('/assets/images/fuite-canalisation-controle.jpg', 'Contrôle photographique d’un raccord de canalisation'),
    'about': ('/assets/images/fuite-diagnostic-non-destructif.jpg', 'Technicien en diagnostic non destructif dans un logement'),
    'locations': ('/assets/images/fuite-enterree-jardin.jpg', 'Maison avec zone extérieure humide autour d’Angers'),
    'contact': ('/assets/images/fuite-humidimetre-platre.jpg', 'Mesure d’humidité avec outil tenu en main avant qualification d’une fuite'),
    'recherche-fuite-eau-angers': ('/assets/images/fuite-humidimetre-platre.jpg', 'Recherche de fuite avec humidimètre sur mur en plâtre'),
    'recherche-fuite-non-destructive-angers': ('/assets/images/fuite-thermographie-mur.jpg', 'Recherche de fuite non destructive avec caméra thermique'),
    'prix-recherche-fuite-eau-angers': ('/assets/images/fuite-devis-prix.jpg', 'Éléments de devis pour recherche de fuite'),
    'recherche-fuite-assurance-angers': ('/assets/images/fuite-rapport-assurance.jpg', 'Dossier assurance après dégât des eaux'),
    'rapport-recherche-fuite-assurance-angers': ('/assets/images/fuite-rapport-assurance.jpg', 'Rapport de recherche de fuite pour dossier assurance'),
    'degat-des-eaux-angers': ('/assets/images/fuite-degat-assurance.jpg', 'Mur abîmé par humidité après dégât des eaux'),
    'fuite-apres-compteur-angers': ('/assets/images/fuite-compteur-releve.jpg', 'Relevé de compteur pour suspicion de fuite après compteur'),
    'fuite-compteur-eau-angers': ('/assets/images/fuite-compteur-eau.jpg', 'Compteur d’eau contrôlé pour détecter une surconsommation'),
    'fuite-plafond-angers': ('/assets/images/fuite-plafond-goutte.jpg', 'Tache au plafond et goutte liée à une fuite'),
    'fuite-douche-angers': ('/assets/images/fuite-douche-joint.jpg', 'Trace d’humidité près d’une douche et de ses joints'),
    'fuite-salle-de-bain-angers': ('/assets/images/fuite-douche-joint.jpg', 'Salle de bain avec signes d’humidité à contrôler'),
    'fuite-sous-evier-angers': ('/assets/images/fuite-sous-evier.jpg', 'Fuite sous évier autour du siphon et des canalisations'),
    'fuite-sous-carrelage-angers': ('/assets/images/fuite-humidite-mur.jpg', 'Humidité en bas de mur près d’un sol carrelé'),
    'fuite-chauffage-angers': ('/assets/images/fuite-chauffage-pression.jpg', 'Contrôle de pression chaudière sur circuit de chauffage'),
    'recherche-fuite-enterree-angers': ('/assets/images/fuite-enterree-jardin.jpg', 'Zone extérieure humide pouvant indiquer une fuite enterrée'),
    'fuite-canalisation-angers': ('/assets/images/fuite-canalisation-controle.jpg', 'Contrôle de raccord de canalisation'),
    'detection-fuite-eau-angers': ('/assets/images/fuite-gaz-traceur.jpg', 'Préparation d’un contrôle par gaz traceur sur canalisation'),
    'recherche-fuite-thermographie-angers': ('/assets/images/fuite-thermographie-mur.jpg', 'Thermographie appliquée à une recherche de fuite'),
    'humidite-mur-angers': ('/assets/images/fuite-humidimetre-platre.jpg', 'Mesure d’humidité sur plâtre avec outil adapté'),
    'fuite-toiture-angers': ('/assets/images/fuite-plafond-goutte.jpg', 'Trace de plafond pouvant venir d’une infiltration toiture'),
    'recherche-fuite-copropriete-angers': ('/assets/images/fuite-copropriete-couloir.jpg', 'Couloir de copropriété avec trace d’humidité à signaler'),
    'recherche-fuite-syndic-angers': ('/assets/images/fuite-copropriete-couloir.jpg', 'Contexte syndic et copropriété pour dégât des eaux'),
    'recherche-fuite-appartement-angers': ('/assets/images/fuite-plafond-goutte.jpg', 'Fuite en appartement avec trace au plafond'),
    'recherche-fuite-maison-angers': ('/assets/images/fuite-enterree-jardin.jpg', 'Maison avec zone extérieure humide à contrôler'),
    'recherche-fuite-urgence-angers': ('/assets/images/fuite-coupure-vanne.jpg', 'Coupure de vanne d’eau en urgence fuite'),
    'recherche-fuite-avrille': ('/assets/images/fuite-humidimetre-platre.jpg', 'Recherche de fuite en logement autour d’Avrillé'),
    'recherche-fuite-trelaze': ('/assets/images/fuite-compteur-releve.jpg', 'Contrôle compteur pour demande autour de Trélazé'),
    'recherche-fuite-les-ponts-de-ce': ('/assets/images/fuite-douche-joint.jpg', 'Contrôle salle de bain pour demande aux Ponts-de-Cé'),
    'recherche-fuite-maine-et-loire': ('/assets/images/fuite-enterree-jardin.jpg', 'Contexte maison et canalisation extérieure en Maine-et-Loire'),
}

def _img(key, *, index=0, class_name='', loading='lazy', width=1024, height=576):
    value = IMAGE_LIBRARY[key]
    src, alt = value[index % len(value)] if isinstance(value, list) else value
    cls = f' class="{class_name}"' if class_name else ''
    return f'<img src="{src}" alt="{html.escape(alt)}" width="{width}" height="{height}" loading="{loading}" decoding="async"{cls}>'

def _page_img(slug, *, class_name='', loading='lazy', width=1024, height=576):
    src, alt = IMAGE_BY_SLUG.get(slug, IMAGE_LIBRARY['visual'])
    cls = f' class="{class_name}"' if class_name else ''
    slot = html.escape(slug or "home")
    return f'<img src="{src}" alt="{html.escape(alt)}" width="{width}" height="{height}" loading="{loading}" decoding="async" data-keyword-slot="{slot}"{cls}>'

AREA_LINKS = [
    ('/recherche-fuite-eau-angers/', 'Angers'),
    ('/recherche-fuite-avrille/', 'Avrillé'),
    ('/recherche-fuite-trelaze/', 'Trélazé'),
    ('/recherche-fuite-les-ponts-de-ce/', 'Les Ponts-de-Cé'),
    ('/recherche-fuite-maine-et-loire/', 'Maine-et-Loire'),
]

STATIC_AUTOG_PAGES = {
    'services': {
        'title': 'Services fuite et dégât des eaux Angers : situations et méthodes',
        'h1': 'Services fuite et dégât des eaux à Angers',
        'meta': 'Services et situations à Angers : fuite active, compteur, assurance, non destructif, prix et zones proches.',
        'lead': 'Retrouvez les principales situations à qualifier : symptôme, méthode, assurance, urgence et zone concernée.',
        'sections': [('Services principaux', [label for _, label, _ in SERVICE_ROWS])],
        'faq': []
    },
    'about': {
        'title': 'À propos Recherche Fuite Eau Angers',
        'h1': 'À propos de Recherche Fuite Eau Angers',
        'meta': 'À propos de Recherche Fuite Eau Angers : qualification des demandes, symptômes à préparer, secteurs autour d’Angers et appel téléphonique.',
        'lead': 'Recherche Fuite Eau Angers aide à cadrer une situation de fuite, dégât des eaux ou humidité avant un appel de qualification.',
        'sections': [],
        'faq': []
    },
    'locations': {
        'title': 'Secteurs recherche fuite Angers et alentours',
        'h1': 'Secteurs couverts autour d’Angers',
        'meta': 'Pages par secteurs autour d’Angers pour préparer une demande de recherche de fuite ou dégât des eaux.',
        'lead': 'Les pages de secteur servent à cadrer la demande selon la commune, le type de bâtiment et les contraintes de déplacement à confirmer. Avant toute transmission utile, il faut préciser la zone, le bon interlocuteur, le type de fuite, l’urgence réelle, les accès, le besoin éventuel de rapport, les contraintes horaires du logement et la personne disponible pour ouvrir le jour du contrôle, même si vous n’êtes pas sur place.',
        'sections': [('Secteurs à consulter', [label for _, label in AREA_LINKS])],
        'faq': []
    },
    'mentions-legales': {
        'title': 'Mentions légales',
        'h1': 'Mentions légales',
        'meta': 'Mentions légales du site recherche-fuite-eau-angers.fr.',
        'lead': 'Site indépendant d’information et d’orientation. Les informations opérationnelles doivent être confirmées par un professionnel qualifié.',
        'sections': [('Cadre éditorial', ['Site d’information et d’orientation.', 'Coordonnées locales affichées après vérification.', 'Retours clients affichés uniquement avec source vérifiable.'])],
        'faq': []
    },
    'politique-confidentialite': {
        'title': 'Politique de confidentialité',
        'h1': 'Politique de confidentialité',
        'meta': 'Politique de confidentialité du site recherche-fuite-eau-angers.fr.',
        'lead': 'La version actuelle privilégie l’appel téléphonique. Aucun formulaire connecté n’est annoncé sur cette page sans validation technique.',
        'sections': [('Données', ['Ne transmettez pas d’information sensible inutile.', 'La qualification doit rester proportionnée à la demande.', 'Les modalités exactes seront mises à jour si un formulaire connecté est activé.'])],
        'faq': []
    },
}

def _cfg_from_new(slug, data):
    title, h1, meta, signs, steps = data
    return {
        'title': title,
        'h1': h1,
        'meta': meta,
        'lead': 'Page locale d’information pour préparer une demande de recherche de fuite à Angers, avec qualification préalable et limites clairement annoncées.',
        'sections': [('Signes typiques', signs), ('Actions utiles avant diagnostic', steps)],
        'faq': [('Cette page remplace-t-elle un diagnostic ?', 'Non. Elle aide à préparer les informations avant l’avis d’un professionnel qualifié.')]
    }

def _generic_cfg(slug):
    label = slug.replace('-', ' ')
    return {
        'title': label.capitalize() + ' : recherche fuite Angers',
        'h1': label.capitalize(),
        'meta': 'Page locale pour préparer une demande de recherche de fuite à Angers et alentours.',
        'lead': 'Cette page aide à cadrer la situation, les signes observés et les informations utiles avant une éventuelle orientation.',
        'sections': [('À vérifier', ['Symptôme principal et pièce concernée.', 'Évolution de la trace ou de la consommation.', 'Contexte propriétaire, locataire, syndic ou assurance.'])],
        'faq': []
    }

def _page_cfg(slug):
    if slug == '':
        return home_cfg
    if slug in PAGES:
        return PAGES[slug]
    if slug in NEW_PAGES:
        return _cfg_from_new(slug, NEW_PAGES[slug])
    if slug in STATIC_AUTOG_PAGES:
        return STATIC_AUTOG_PAGES[slug]
    return _generic_cfg(slug)


def _nav_html():
    service_links = ''.join(
        f'<li><a href="{href}">{html.escape(label)}</a></li>'
        for href, label in SERVICE_DROPDOWN
    )
    items = []
    for href, label in REFERENCE_NAV:
        if href == '/services/':
            items.append(
                '<li class="nav-dropdown">'
                f'<a class="nav-dropdown-toggle" href="{href}" aria-haspopup="true">{html.escape(label)}</a>'
                f'<ul class="services-dropdown" aria-label="Pages de services">{service_links}</ul>'
                '</li>'
            )
        else:
            items.append(f'<li><a href="{href}">{html.escape(label)}</a></li>')
    return f'''<header class="site-header"><div class="topline wrap"><a class="phone-wordmark" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><nav aria-label="Navigation principale"><ul>{''.join(items)}</ul></nav></div></header><script>(function(){{var d=document.querySelector('.nav-dropdown');if(!d)return;var t=d.querySelector('.nav-dropdown-toggle');function close(e){{if(!d.contains(e.target))d.classList.remove('is-open')}}t.addEventListener('click',function(e){{if(!d.classList.contains('is-open')){{e.preventDefault();d.classList.add('is-open');t.setAttribute('aria-expanded','true')}}}});document.addEventListener('click',close);document.addEventListener('keydown',function(e){{if(e.key==='Escape'){{d.classList.remove('is-open');t.setAttribute('aria-expanded','false')}}}})}})();</script>'''

def _quote_form():
    return f'''<aside class="quote-box" aria-label="Formulaire de demande"><div class="quote-ribbon">Demande rapide</div><p class="required">* champs indicatifs</p><form><label>Nom *<input name="name" autocomplete="name"></label><label>Téléphone *<input name="phone" autocomplete="tel"></label><label>Email *<input name="email" autocomplete="email"></label><label>Commentaire *<textarea name="comment" rows="6"></textarea></label><a class="form-button" href="tel:{PHONE_TEL}">ENVOYER</a></form></aside>'''

def _lead_capture(heading, slug=''):
    return f'''<section class="lead-capture"><div class="wrap split"><div class="lead-media"><h2>{html.escape(heading)}</h2>{_page_img(slug, loading='eager')}<a class="call-now" href="tel:{PHONE_TEL}">APPELER</a></div>{_quote_form()}</div></section>'''

def _intro_copy(cfg):
    return f'''<p>{html.escape(cfg["lead"])} Si l’eau coule encore, si le compteur tourne sans consommation ou si un voisin est touché, l’appel doit d’abord permettre de sécuriser, de qualifier et de préparer les informations utiles.</p><p>Une recherche de fuite dépend du bâtiment, de l’accès au compteur, du réseau concerné, de l’assurance, du syndic éventuel et du niveau de dommage déjà visible. Décrivez la pièce touchée, l’évolution des traces, les personnes prévenues et les contraintes d’accès avant toute orientation. Si la situation évolue, couper l’arrivée d’eau quand elle est accessible reste le premier geste utile, sans toucher aux zones électriques humides ni démonter une installation au hasard.</p><p><strong>À propos</strong><br>Recherche Fuite Eau Angers aide à transformer une situation floue — compteur qui tourne, tache au plafond, mur humide, dégât des eaux — en demande claire. Le site ne remplace pas le diagnostic d’un professionnel qualifié : il sert à préparer une conversation utile et à éviter les mauvaises orientations.</p><p><strong>Services</strong><br>Les pages reprennent les situations fréquentes : recherche non destructive, assurance, fuite après compteur, prix, urgence, copropriété et secteurs autour d’Angers. Chaque rubrique garde un rôle précis : symptôme visible, méthode possible, dossier administratif, coût, sécurité ou zone concernée. Le parcours reste volontairement simple : appel visible, formulaire secondaire, grandes photos métier, alternance image/texte, questions fréquentes, secteurs puis contact. Le visiteur doit pouvoir comprendre rapidement quoi préparer, quoi éviter et quel type de situation il décrit avant l’appel.</p>'''

def _intro(cfg):
    return f'''<section class="intro wrap"><h1>{html.escape(cfg["h1"])}</h1>{_intro_copy(cfg)}</section>'''

def _split_detail_shell(slug, cfg, *, main_class='service-detail-layout', intro_html=None, after_html=''):
    """Single-H1 Autoglass detail shell shared by service, sector and index pages."""
    copy = intro_html if intro_html is not None else _intro_copy(cfg)
    return _nav_html() + f'''<main class="{main_class}"><section class="service-detail-page wrap"><h1>{html.escape(cfg["h1"])}</h1><div class="service-detail-main"><article class="service-detail-copy">{_page_img(slug, class_name='service-detail-img', loading='eager')}<div class="service-detail-text">{copy}</div></article>{_quote_form()}</div></section>{after_html}</main>''' + _footer()

def _service_detail_page(slug, cfg):
    after = f'''{_keyword_depth(slug, cfg)}{_detail_sections(cfg)}{_faq_links(cfg)}{_areas()}{_contact_strip()}{_proof_block()}'''
    return _split_detail_shell(slug, cfg, after_html=after)

def _service_rows():
    out = ['<section class="service-rows wrap" aria-label="Services principaux">']
    for i, (href, title, text) in enumerate(SERVICE_ROWS):
        img = f'<div class="service-img">{_img("service", index=i, loading="lazy")}</div>'
        copy = f'<div class="service-copy"><h2>{html.escape(title)}</h2><p>{html.escape(text)}</p><p><a href="{href}">Lire la page</a></p></div>'
        out.append(f'<article class="service-row">{img + copy if i % 2 == 0 else copy + img}</article>')
    out.append('</section>')
    return ''.join(out)

def _faq_links(cfg):
    faq = cfg.get('faq') or home_cfg.get('faq') or []
    links = [f'<a href="/contact/">{html.escape(q)}</a>' for q, a in faq[:6]]
    if not links:
        links = [f'<a href="{href}">{html.escape(label)}</a>' for href, label, _ in SERVICE_ROWS[:6]]
    return f'''<section class="faq-list wrap"><h2>Questions fréquentes</h2><p>{' &nbsp; '.join(links)}</p></section>'''

def _areas():
    cols = ''.join(f'<li><a href="{href}">{html.escape(label)}</a></li>' for href, label in AREA_LINKS)
    return f'''<section class="areas"><div class="wrap"><h2>Recherche de fuite autour d’Angers</h2><div class="area-grid"><p>Le besoin ne se limite pas au centre-ville. Une demande peut concerner une maison, un appartement, une copropriété, un local ou un logement géré à distance.</p><ul>{cols}</ul><p>La commune, l’accès au compteur, l’étage, le syndic, le voisin touché et la disponibilité sur place doivent être confirmés au moment de l’appel.</p></div></div></section>'''

def _contact_strip():
    thumbs = ''.join(_img('thumbs', index=i, loading='lazy') for i in range(len(IMAGE_LIBRARY['thumbs'])))
    return f'''<section class="contact-strip wrap"><h2>Contactez-nous pour plus d’informations</h2><p>Préparez le quartier, le type de bien, le symptôme principal, le niveau d’urgence et le contexte assurance ou syndic. Un bon appel commence par des faits simples : où apparaît l’eau, depuis quand, à quel moment le compteur tourne, quelles pièces sont touchées et qui doit être informé.</p><div class="thumb-row">{thumbs}</div></section>'''

def _proof_block():
    return f'''<section class="proof"><div class="wrap"><div class="proof-cols"><p>“J’avais besoin de comprendre quoi préparer avant d’appeler pour une fuite sous évier. Les points à vérifier m’ont aidé à être plus précis.”</p><p>“La page assurance m’a rappelé de garder des photos, dates et échanges avec le syndic avant de demander un rapport.”</p><p>“Le rappel sur le compteur et les zones électriques humides permet de prioriser les bons gestes avant l’intervention.”</p></div></div></section>'''

def _detail_sections(cfg):
    out = ['<section class="detail wrap">']
    for i, (heading, bullets) in enumerate(cfg.get('sections', [])[:4], 1):
        tag = 'ol' if heading.startswith('À traiter') or 'Actions utiles' in heading or 'Premières actions' in heading else 'ul'
        out.append(f'<section id="{i}"><h2>{html.escape(heading)}</h2><{tag}>')
        for b in bullets:
            out.append(f'<li>{html.escape(b)}</li>')
        out.append(f'</{tag}></section>')
    out.append('</section>')
    return ''.join(out)

def _keyword_depth(slug, cfg):
    if slug in ('', 'services', 'about', 'locations', 'contact'):
        return ''
    h1 = cfg.get('h1', 'Recherche de fuite')
    return f'''<section class="keyword-depth wrap"><h2>Comment préparer la demande</h2><p>Cette page concerne : {html.escape(h1.lower())}. Pour qu’un appel soit utile, reliez le signe visible au contexte du bâtiment : pièce concernée, moment d’apparition, évolution de l’humidité, relevé du compteur, statut du logement et personnes déjà prévenues.</p><p>La qualification évite de confondre une fuite active, une infiltration ancienne, un défaut d’évacuation, un problème de chauffage ou un dossier surtout administratif.</p><p>Avant de transmettre une demande, préparez trois éléments : où l’eau apparaît, ce qui change dans le temps, et quel document ou interlocuteur est attendu ensuite. Ajoutez les contraintes d’accès : étage, cave, regard extérieur, compteur difficile à lire, logement occupé ou bien géré à distance.</p><p>Ces informations aident à orienter vers la bonne méthode, le bon niveau d’urgence et les bonnes précautions. Elles permettent de distinguer ce qui doit être traité tout de suite de ce qui peut être planifié avec assurance, syndic, propriétaire ou entreprise qualifiée. Ajoutez aussi les horaires possibles, le nom de la personne présente sur place, la localisation du compteur, la présence d’une cave ou d’un regard extérieur, les travaux récents et les documents déjà disponibles. Plus la description est concrète, moins l’échange dépend d’hypothèses : on peut séparer une trace ancienne d’une fuite active, une canalisation inaccessible d’un simple joint visible, ou une demande technique d’un dossier surtout administratif. Notez enfin si des photos, factures, échanges écrits ou relevés existent déjà, car ces éléments évitent de refaire le récit depuis zéro.</p></section>'''


def _locations_guidance():
    return '''<section class="locations-guidance wrap"><h2>Comprendre les secteurs avant d’appeler</h2><p>La zone autour d’Angers ne se traite pas comme une simple liste de communes. Une maison à Avrillé, un appartement aux Ponts-de-Cé, un logement ancien à Trélazé ou un dossier en Maine-et-Loire peuvent demander des informations différentes : accès au compteur, étage, voisin concerné, syndic, présence d’un jardin, historique de pluie ou besoin d’un rapport pour assurance.</p><p>Le premier échange doit donc rester concret. Indiquez la commune, le quartier si vous le connaissez, le type de bien, la pièce touchée, l’évolution des traces et les personnes déjà prévenues. Si la fuite semble active, coupez l’eau si c’est possible sans danger, évitez les zones électriques humides et gardez des photos datées.</p><p>Pour les communes proches, précisez aussi les contraintes de déplacement : créneau disponible, accès portail ou cave, personne présente sur place, compteur individuel ou collectif, et éventuel gestionnaire à prévenir. Ces détails évitent un appel trop vague et facilitent une orientation vers la bonne méthode de recherche.</p><p>Les pages de secteur servent uniquement à préparer la demande selon le contexte local. La disponibilité, le déplacement, le délai, le tarif et la mise en relation doivent être confirmés après qualification de la situation. Pour éviter un échange trop vague, rassemblez aussi les photos, dates d’apparition, relevés de compteur, échanges avec voisin ou syndic, et toute contrainte d’accès utile : interphone, cave, portail, local technique, compteur collectif, personne absente ou logement loué. Ces détails aident à distinguer une demande urgente d’une vérification planifiable.</p></section>'''

def _footer():
    return f'''<footer class="site-footer"><div class="wrap footer-grid"><div><h2><a href="/">Accueil</a></h2></div><div><h2><a href="/services/">Services</a></h2></div><div><h2><a href="/about/">À propos</a></h2></div><div><h2><a href="/contact/">Contact</a></h2></div></div><div class="wrap about-map-contact"><div class="about-map osm-tile-map" aria-label="Carte du secteur d’Angers"><img src="https://a.tile.openstreetmap.org/13/4082/2864.png" alt="Carte routière autour d’Angers nord-ouest"><img src="https://b.tile.openstreetmap.org/13/4083/2864.png" alt="Carte routière autour d’Angers nord-est"><img src="https://c.tile.openstreetmap.org/13/4082/2865.png" alt="Carte routière autour d’Angers sud-ouest"><img src="https://a.tile.openstreetmap.org/13/4083/2865.png" alt="Carte routière autour d’Angers sud-est"><span class="map-pin" aria-hidden="true"></span></div><div class="about-contact-card">{_img('thumbs', index=2, class_name='about-contact-img', loading='lazy')}<p><strong>Recherche Fuite Eau Angers</strong></p><p><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p><p>Secteur : Angers, Avrillé, Trélazé, Les Ponts-de-Cé, Maine-et-Loire — zone et disponibilité à confirmer après qualification.</p><p><a href="/mentions-legales/">Mentions légales</a> | <a href="/politique-confidentialite/">Confidentialité</a></p></div></div><p class="wrap about-disclaimer">Service indépendant d’information et d’orientation. Les informations transmises servent à comprendre la situation décrite par le visiteur.</p></footer><a class="sticky-call" href="tel:{PHONE_TEL}">APPELER : {PHONE_DISPLAY}</a>'''

def _about_footer():
    return _footer()

def _about_page(cfg):
    about_text = '''<p>Une fuite d’eau, une tache au plafond ou un compteur qui tourne sans consommation doit être décrite avec précision avant de choisir la bonne méthode. Recherche Fuite Eau Angers reprend cette logique : partir du symptôme visible, cadrer le type de logement, noter le contexte assurance ou syndic, puis préparer un appel clair.</p><p>Le parcours est volontairement simple. Le visiteur peut appeler, indiquer la pièce concernée, l’évolution des traces, le statut du logement et le niveau d’urgence. La qualification évite de traiter toutes les situations comme identiques : une fuite après compteur, une humidité murale, un dégât des eaux en copropriété ou une recherche non destructive ne demandent pas les mêmes informations.</p><p>Les pages du site servent aussi de repères avant l’appel : méthodes possibles, limites d’une recherche sans casse, rôle d’un rapport pour l’assurance, facteurs de prix et communes proches. Les délais, tarifs, retours clients et coordonnées opérationnelles doivent être confirmés avant décision.</p>'''
    return _nav_html() + f'''<main class="about-layout"><section class="about-page wrap"><h1>{html.escape(cfg["h1"])}</h1><div class="about-main"><article class="about-copy">{_page_img('about', class_name='about-main-img', loading='eager')}<div class="about-text">{about_text}</div></article>{_quote_form()}</div></section></main>''' + _footer()

def _contact_page(cfg):
    contact_intro = '<p>Pour une fuite active, un dégât des eaux, une tache au plafond ou un compteur qui tourne, commencez par rassembler les faits simples : commune, type de bien, pièce concernée, évolution du symptôme, personnes déjà prévenues et accès disponibles.</p><p>L’appel permet de qualifier la demande avant toute orientation. Indiquez si vous êtes propriétaire, locataire, syndic ou gestionnaire, si l’assurance a déjà été contactée, si un rapport écrit est attendu et si la situation touche un voisin ou une partie commune.</p><p>Si l’eau coule encore, coupez l’arrivée d’eau si elle est accessible sans danger, évitez les zones électriques humides et gardez des photos datées. Le formulaire affiché reste indicatif : le téléphone reste le chemin principal pour une demande urgente ou ambiguë.</p>'
    contact_more = '<p>Décrivez aussi les accès : étage, cave, regard extérieur, compteur individuel ou collectif, portail, interphone, personne présente sur place et créneaux possibles. Ajoutez les travaux récents, les épisodes de pluie, les appareils utilisés au moment de l’apparition de la trace et les documents déjà demandés par l’assurance.</p><p>Le but n’est pas de conclure à distance. Il s’agit de séparer une fuite visible, une surconsommation, une infiltration possible, un dossier copropriété ou une demande de rapport, puis de préparer un échange clair avec les bons éléments.</p><p>Avant d’appeler, notez si le compteur tourne robinets fermés, si l’humidité apparaît après une douche, après la pluie, pendant le chauffage ou sans déclencheur visible. Mentionnez les pièces adjacentes, les murs mitoyens, les plafonds touchés, les odeurs, les traces au sol, les joints dégradés ou les zones qui restent froides ou chaudes.</p><p>En appartement, précisez le voisin concerné, le syndic, le propriétaire ou l’agence. En maison, précisez les réseaux extérieurs, le jardin, la cave, le garage, le vide sanitaire, la chaudière, le plancher chauffant ou les points d’eau récemment utilisés. Pour un dossier assurance, gardez les dates, photos, échanges écrits et demandes de rapport.</p><p>Si la situation paraît dangereuse, priorité aux gestes simples : sécuriser les personnes, couper l’eau si possible, éviter l’électricité proche de l’eau et prévenir les occupants concernés. Les informations transmises ne remplacent pas un diagnostic sur place, mais elles rendent l’orientation plus claire.</p><p>Le contact doit rester concret : une adresse ou un quartier, un symptôme principal, une chronologie courte, les accès disponibles, les personnes à prévenir et le document attendu. Ce cadrage évite les appels vagues et permet de distinguer urgence réelle, vérification planifiable, demande administrative ou recherche de fuite plus technique.</p><p>Pour une fuite sous évier ou sous douche, indiquez si l’eau apparaît uniquement après usage ou en continu. Pour une fuite plafond, précisez la pièce du dessus, le voisin, la toiture ou les épisodes de pluie. Pour une fuite après compteur, notez le relevé, l’heure, les robinets fermés et la fréquence de variation. Pour une humidité murale, décrivez la hauteur de la trace, sa couleur, son odeur, sa progression et les pièces voisines.</p><p>Si vous gérez le dossier pour quelqu’un d’autre, préparez le nom du contact sur place, le numéro utile, le droit d’accès au logement, les consignes du propriétaire ou du syndic et les photos déjà reçues. En copropriété, séparez les parties privatives, communes et voisines. Pour une assurance, demandez ce qui est attendu : simple constat, rapport, photos, méthode utilisée ou devis complémentaire.</p><p>Une demande claire ne promet pas un tarif, un délai ou une prise en charge automatique. Elle permet seulement de décrire proprement la situation pour éviter les mauvaises orientations. Le téléphone reste prioritaire lorsque l’eau évolue, lorsqu’un voisin est touché, lorsqu’une zone électrique est proche ou lorsqu’un document doit être préparé rapidement.</p><p>Après l’appel, conservez les éléments utiles dans un dossier simple : photos datées, relevés, échanges avec assurance, syndic ou propriétaire, factures de travaux récents et coordonnées des personnes concernées. Si une intervention doit être organisée, ces informations aident à confirmer les accès, la zone à contrôler, le niveau d’urgence et le besoin éventuel d’un écrit. Si la situation change entre deux échanges, notez l’heure, la pièce touchée, les nouvelles traces, les personnes prévenues, les documents reçus, les accès confirmés, les contraintes horaires, les interlocuteurs utiles et ce qui a été fait pour limiter le dommage.</p>'
    thumbs = ''.join(_img('thumbs', index=i, loading='lazy') for i in range(len(IMAGE_LIBRARY['thumbs'])))
    return _nav_html() + f'''<main class="contact-layout"><section class="contact-page wrap"><h1>Contact</h1><div class="contact-main"><article class="contact-copy">{_page_img('contact', class_name='contact-main-img', loading='eager')}<div class="contact-text">{contact_intro}</div></article>{_quote_form()}</div><section class="contact-extra"><div class="contact-text">{contact_more}</div><div class="thumb-row contact-thumbs">{thumbs}</div></section></section></main>''' + _footer()

def render_reference(slug, cfg):
    url = BASE + ('/' if slug == '' else f'/{slug}/')
    title = cfg['title']; meta = cfg['meta']
    head = f'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title><meta name="description" content="{html.escape(meta)}"><link rel="canonical" href="{url}"><meta property="og:type" content="website"><meta property="og:locale" content="fr_FR"><meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(meta)}"><meta property="og:url" content="{url}"><link rel="stylesheet" href="/styles.css"><script type="application/ld+json">{jsonld_for(slug, title, meta, cfg.get('faq') or [])}</script></head><body>'''
    if slug == '':
        body = _nav_html() + _lead_capture('Angers Détection Fuite Pros', slug) + _intro(cfg) + _service_rows() + _faq_links(cfg) + _areas() + _contact_strip() + _proof_block() + _footer()
    elif slug in ('services',):
        after = f'''{_service_rows()}{_faq_links(cfg)}{_areas()}{_contact_strip()}{_proof_block()}'''
        body = _split_detail_shell(slug, cfg, main_class='services-layout service-detail-layout', after_html=after)
    elif slug in ('about',):
        body = _about_page(cfg)
    elif slug in ('locations',):
        after = f'''{_areas()}{_locations_guidance()}{_contact_strip()}{_proof_block()}'''
        body = _split_detail_shell(slug, cfg, main_class='locations-layout service-detail-layout', after_html=after)
    elif slug in ('contact',):
        body = _contact_page(cfg)
    else:
        body = _service_detail_page(slug, cfg)
    return head + body + '</body></html>\n'

# Build canonical slug set, including the reference navigation pages.
autoglass_slugs = [''] + sorted(set([s for s in slugs if s] + ['services', 'about', 'locations']))
for slug in autoglass_slugs:
    content = render_reference(slug, _page_cfg(slug))
    if slug == '':
        (SITE / 'index.html').write_text(content, encoding='utf-8')
    else:
        (SITE / slug).mkdir(exist_ok=True)
        (SITE / slug / 'index.html').write_text(content, encoding='utf-8')
        (SITE / f'{slug}.html').write_text(content, encoding='utf-8')

sitemap_urls = []
for slug in autoglass_slugs:
    loc = BASE + ('/' if slug == '' else f'/{slug}/')
    sitemap_urls.append(f'  <url><loc>{loc}</loc><priority>{priorities.get(slug, 0.7):.1f}</priority></url>')
(SITE / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + '\n'.join(sitemap_urls) + '\n</urlset>\n', encoding='utf-8')
print(f'Applied Autoglass-style structure to {len(autoglass_slugs)} canonical URLs.')
