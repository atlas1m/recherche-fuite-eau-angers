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

SERVICE_ROWS = [
    ('/recherche-fuite-eau-angers/', 'Recherche de fuite à Angers', 'Qualifier les signes visibles, l’urgence, le statut du logement et le besoin éventuel d’un rapport avant d’orienter la demande.'),
    ('/recherche-fuite-non-destructive-angers/', 'Détection non destructive', 'Structurer les cas où caméra thermique, gaz traceur, électro-acoustique ou inspection peuvent éviter une casse inutile.'),
    ('/fuite-apres-compteur-angers/', 'Fuite après compteur', 'Préparer les relevés d’index, la surconsommation et les éléments utiles avant de demander un diagnostic.'),
    ('/degat-des-eaux-angers/', 'Dégât des eaux & assurance', 'Rassembler photos, déclaration, syndic ou propriétaire, et comprendre ce qu’un rapport peut ou non prouver.'),
    ('/prix-recherche-fuite-eau-angers/', 'Prix d’une recherche de fuite', 'Identifier ce qui influence le devis sans annoncer de tarif non vérifié : accès, méthode, rapport, urgence et réparation.'),
    ('/recherche-fuite-urgence-angers/', 'Urgence fuite : quoi faire', 'Prioriser sécurité, coupure d’eau, voisin touché et premier tri avant toute promesse de disponibilité.'),
]

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
        'title': 'À propos : information indépendante recherche fuite Angers',
        'h1': 'À propos de ce guide indépendant',
        'meta': 'À propos du service indépendant d’information et d’orientation pour recherche de fuite à Angers.',
        'lead': 'Ce site organise l’information utile avant une demande de recherche de fuite. Il ne publie pas d’adresse locale, d’avis ou de promesse non vérifiés.',
        'sections': [('Positionnement', ['Information locale structurée.', 'Qualification de la situation avant orientation.', 'Pas de fausse adresse, pas de faux avis, pas de tarif inventé.'])],
        'faq': []
    },
    'locations': {
        'title': 'Secteurs recherche fuite Angers et alentours',
        'h1': 'Secteurs couverts autour d’Angers',
        'meta': 'Pages par secteurs autour d’Angers pour préparer une demande de recherche de fuite ou dégât des eaux.',
        'lead': 'Les pages de secteur servent à cadrer la demande selon la commune, le type de bâtiment et les contraintes de déplacement à confirmer.',
        'sections': [('Secteurs à consulter', [label for _, label in AREA_LINKS])],
        'faq': []
    },
    'mentions-legales': {
        'title': 'Mentions légales',
        'h1': 'Mentions légales',
        'meta': 'Mentions légales du site recherche-fuite-eau-angers.fr.',
        'lead': 'Site indépendant d’information et d’orientation. Les informations opérationnelles doivent être confirmées par un professionnel qualifié.',
        'sections': [('Transparence', ['Pas une entreprise de plomberie.', 'Pas d’adresse locale affichée sans vérification.', 'Pas d’avis clients affichés sans source.'])],
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
    items = ''.join(f'<li><a href="{href}">{html.escape(label)}</a></li>' for href, label in REFERENCE_NAV)
    return f'''<header class="site-header"><div class="topline wrap"><a class="phone-wordmark" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><nav aria-label="Navigation principale"><ul>{items}</ul></nav></div></header>'''

def _quote_form():
    return f'''<aside class="quote-box" aria-label="Formulaire de demande"><div class="quote-ribbon">Demande rapide</div><p class="required">* champs indicatifs — formulaire non connecté</p><form><label>Nom *<input name="name" autocomplete="name"></label><label>Téléphone *<input name="phone" autocomplete="tel"></label><label>Email *<input name="email" autocomplete="email"></label><label>Commentaire *<textarea name="comment" rows="5"></textarea></label><a class="submit-like" href="tel:{PHONE_TEL}">Appeler / qualifier</a></form></aside>'''

def _lead_capture(heading):
    return f'''<section class="lead-capture"><div class="wrap split"><div class="lead-media"><h2>{html.escape(heading)}</h2><img src="/assets/images/artisan-recherche-fuite.png" alt="Recherche de fuite d’eau avec matériel de diagnostic" width="1024" height="576"><a class="call-now" href="tel:{PHONE_TEL}">APPELER</a></div>{_quote_form()}</div></section>'''

def _intro(cfg):
    return f'''<section class="intro wrap"><h1>{html.escape(cfg['h1'])}</h1><p>{html.escape(cfg['lead'])}</p><p><strong>À propos</strong><br>Ce site sert à transformer une situation floue — compteur qui tourne, tache au plafond, mur humide, dégât des eaux — en demande claire. Il garde une position prudente : pas de fausse adresse, pas de faux avis, pas de promesse de délai ou de prix sans qualification.</p><p><strong>Services</strong><br>Les pages ci-dessous reprennent les cas les plus fréquents : recherche non destructive, assurance, fuite après compteur, prix, urgence, copropriété et secteurs autour d’Angers.</p></section>'''

def _service_rows():
    out = ['<section class="service-rows wrap" aria-label="Services principaux">']
    for i, (href, title, text) in enumerate(SERVICE_ROWS):
        img = '<div class="service-img"><img src="/assets/images/artisan-recherche-fuite.png" alt="Diagnostic humidité et canalisation" loading="lazy"></div>'
        copy = f'<div class="service-copy"><h2>{html.escape(title)}</h2><p>{html.escape(text)}</p><p><a href="{href}">Lire la page</a></p></div>'
        out.append(f'<article class="service-row">{img + copy if i % 2 == 0 else copy + img}</article>')
    out.append('</section>')
    return ''.join(out)

def _faq_links(cfg):
    faq = cfg.get('faq') or home_cfg.get('faq') or []
    items = ''.join(f'<li><a href="#{i}">{html.escape(q)}</a></li>' for i, (q, _) in enumerate(faq[:6], 1))
    if not items:
        items = ''.join(f'<li><a href="{href}">{html.escape(label)}</a></li>' for href, label, _ in SERVICE_ROWS[:6])
    return f'<section class="faq-list wrap"><h2>Questions fréquentes</h2><ul>{items}</ul></section>'

def _areas():
    items = ''.join(f'<li><a href="{href}">{html.escape(label)}</a></li>' for href, label in AREA_LINKS)
    return f'<section class="areas"><div class="wrap"><h2>Recherche de fuite autour d’Angers</h2><ul>{items}</ul></div></section>'

def _contact_strip():
    return f'''<section class="contact-strip wrap"><h2>Contactez-nous pour qualifier la situation</h2><p>Préparez le quartier, le type de bien, le symptôme principal, le niveau d’urgence et le contexte assurance ou syndic.</p><div class="thumb-row"><img src="/assets/images/artisan-recherche-fuite.png" alt="Contrôle humidité" loading="lazy"><img src="/assets/images/artisan-recherche-fuite.png" alt="Inspection canalisation" loading="lazy"><img src="/assets/images/artisan-recherche-fuite.png" alt="Diagnostic non destructif" loading="lazy"></div></section>'''

def _proof_block():
    return f'''<section class="proof"><div class="wrap"><h2>Transparence avant mise en relation</h2><div class="proof-cols"><p>Pas de faux avis : les preuves client ne seront affichées qu’après collecte vérifiable.</p><p>Pas de fausse adresse : aucune implantation locale n’est publiée sans validation.</p><p>Pas de tarif inventé : prix, disponibilité et prise en charge assurance restent à confirmer.</p></div><p><a class="call-now dark" href="tel:{PHONE_TEL}">APPELER</a></p></div></section>'''

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

def _footer():
    return f'''<footer class="site-footer"><div class="wrap footer-grid"><div><h2>Accueil</h2><p><a href="/">Accueil</a></p><p><a href="/services/">Services</a></p><p><a href="/about/">À propos</a></p><p><a href="/contact/">Contact</a></p></div><div><h2>Services</h2><p><a href="/recherche-fuite-non-destructive-angers/">Sans casse</a></p><p><a href="/recherche-fuite-assurance-angers/">Assurance</a></p><p><a href="/prix-recherche-fuite-eau-angers/">Prix</a></p></div><div><h2>Contact</h2><p><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p><p><a href="/mentions-legales/">Mentions légales</a></p><p><a href="/politique-confidentialite/">Confidentialité</a></p></div></div></footer><a class="sticky-call" href="tel:{PHONE_TEL}">APPELER : {PHONE_DISPLAY}</a>'''

def render_reference(slug, cfg):
    url = BASE + ('/' if slug == '' else f'/{slug}/')
    title = cfg['title']; meta = cfg['meta']
    head = f'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title><meta name="description" content="{html.escape(meta)}"><link rel="canonical" href="{url}"><meta property="og:type" content="website"><meta property="og:locale" content="fr_FR"><meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(meta)}"><meta property="og:url" content="{url}"><link rel="stylesheet" href="/styles.css"><script type="application/ld+json">{jsonld_for(slug, title, meta, cfg.get('faq') or [])}</script></head><body>'''
    if slug == '':
        body = _nav_html() + _lead_capture('Angers Détection Fuite Pros') + _intro(cfg) + _service_rows() + _faq_links(cfg) + _areas() + _contact_strip() + _proof_block() + _footer()
    elif slug in ('services',):
        body = _nav_html() + _lead_capture('Services recherche de fuite') + _intro(cfg) + _service_rows() + _faq_links(cfg) + _areas() + _contact_strip() + _proof_block() + _footer()
    elif slug in ('locations',):
        body = _nav_html() + _lead_capture('Secteurs autour d’Angers') + _intro(cfg) + _areas() + _detail_sections(cfg) + _contact_strip() + _proof_block() + _footer()
    else:
        body = _nav_html() + _lead_capture(cfg['h1']) + _intro(cfg) + _detail_sections(cfg) + _faq_links(cfg) + _areas() + _contact_strip() + _proof_block() + _footer()
    return head + body + '</body></html>\n'

# Build canonical slug set, including the reference navigation pages.
autoglass_slugs = [''] + sorted(set(slugs + ['services', 'about', 'locations']))
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
