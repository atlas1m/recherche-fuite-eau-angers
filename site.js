/* ===========================================================
   Angers Détection Fuite - shared header + footer injector
   ===========================================================
   PLACEHOLDER : remplacer le numéro 09 72 14 55 77 et l'email
   contact@recherche-fuite-eau-angers.fr par les coordonnées réelles avant mise
   en ligne. Une ligne qui ne répond pas = leads perdus. Ces valeurs
   sont centralisées ci-dessous (PHONE_DISPLAY / PHONE_HREF / EMAIL)
   pour un remplacement global ; garder la même valeur partout.
   =========================================================== */
(function () {
  var PHONE_DISPLAY = "09 72 14 55 77";
  var PHONE_HREF = "tel:+339****5577";
  var EMAIL = "contact@recherche-fuite-eau-angers.fr";

  var SERVICES = [
    ["/recherche-de-fuite/", "Recherche de fuite d'eau"],
    ["/detection-non-destructive/", "Détection non destructive"],
    ["/camera-thermique/", "Caméra thermique infrarouge"],
    ["/gaz-traceur/", "Gaz traceur"],
    ["/inspection-camera/", "Inspection caméra / endoscopie"],
    ["/fuite-piscine/", "Recherche de fuite piscine"],
    ["/intervention-urgence/", "Intervention d'urgence"]
  ];
  var ZONES = [
    ["/angers/", "ANGERS"],
    ["/avrille/", "AVRILLÉ"],
    ["/ponts-de-ce/", "LES PONTS-DE-CÉ"]
  ];

  var page = (document.body.getAttribute("data-page") || "").toLowerCase();
  function act(file, key) { return page === key ? " active" : ""; }

  var dropIcon =
    '<svg class="drop" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">' +
    '<path d="M24 4C24 4 8 22 8 32a16 16 0 0 0 32 0C40 22 24 4 24 4Z" fill="#1f7fc4"/>' +
    '<path d="M24 4C24 4 8 22 8 32a16 16 0 0 0 32 0C40 22 24 4 24 4Z" fill="url(#dg)" opacity=".35"/>' +
    '<path d="M30 30a6 6 0 0 1-6 6" stroke="#fff" stroke-width="3" stroke-linecap="round" fill="none"/>' +
    '<defs><linearGradient id="dg" x1="8" y1="4" x2="40" y2="48" gradientUnits="userSpaceOnUse">' +
    '<stop stop-color="#3c9ee5"/><stop offset="1" stop-color="#0a3d62"/></linearGradient></defs></svg>';

  var caret = '<svg class="caret" viewBox="0 0 16 16" fill="none"><path d="M4 6l4 4 4-4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
  function svg(p){return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'+p+'</svg>';}
  var icPhone = svg('<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.9.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92Z"/>');
  var icMail = svg('<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 6-10 7L2 6"/>');
  var icPin = svg('<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0Z"/><circle cx="12" cy="10" r="3"/>');
  var icClock = svg('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>');

  /* ---------- submenus ---------- */
  var svcSub = SERVICES.map(function (s) { return '<a href="' + s[0] + '">' + s[1] + '</a>'; }).join("");
  var zoneSub = ZONES.map(function (z) { return '<a href="' + z[0] + '">' + z[1] + '</a>'; }).join("");

  /* ---------- TOPBAR + HEADER ---------- */
  var header =
    '<div class="topbar"><div class="wrap">' +
      '<div class="tb-left">' + icPin + '<span>Mise en relation avec des spécialistes de la recherche de fuite à Angers &amp; dans le Maine-et-Loire (49)</span></div>' +
      '<div class="tb-right">' +
        '<a href="' + PHONE_HREF + '">' + icPhone + PHONE_DISPLAY + '</a>' +
        /* [À CONFIRMER] '7j/7' retiré tant que la disponibilité n'est pas garantie par les partenaires. */
        '<a href="/contact/">' + icClock + 'Devis gratuit</a>' +
      '</div>' +
    '</div></div>' +
    '<header class="site-header"><div class="wrap">' +
      '<a class="brand" href="/">' + dropIcon +
        '<span>Angers Détection Fuite<small>Angers · Détection de fuite</small></span></a>' +
      '<nav class="nav">' +
        '<a href="/" class="' + act('','home').trim() + '">Accueil</a>' +
        '<div class="has-sub"><a href="/services/" class="' + act('','services').trim() + '">Services ' + caret + '</a>' +
          '<div class="submenu">' + svcSub + '</div></div>' +
        '<a href="/about/" class="' + act('','about').trim() + '">À propos</a>' +
        '<div class="has-sub"><a href="/zones/" class="' + act('','zones').trim() + '">Zones ' + caret + '</a>' +
          '<div class="submenu">' + zoneSub + '</div></div>' +
        '<a href="/contact/" class="' + act('','contact').trim() + '">Contact</a>' +
      '</nav>' +
      '<a class="btn btn--amber nav-cta" href="' + PHONE_HREF + '">' + icPhone + PHONE_DISPLAY + '</a>' +
      '<button class="hamburger" aria-label="Menu" id="hbtn"><span></span><span></span><span></span></button>' +
    '</div></header>' +
    /* mobile drawer */
    '<div class="mnav" id="mnav"><div class="mnav__scrim" data-close></div><div class="mnav__panel">' +
      '<button class="close" data-close aria-label="Fermer">×</button>' +
      '<a href="/">Accueil</a>' +
      '<h4>Services</h4>' +
      '<a href="/services/">Tous nos services</a>' +
      SERVICES.map(function(s){return '<a class="sub" href="'+s[0]+'">'+s[1]+'</a>';}).join("") +
      '<a href="/about/">À propos</a>' +
      '<h4>Zones d\'intervention</h4>' +
      '<a href="/zones/">Toutes les zones</a>' +
      ZONES.map(function(z){return '<a class="sub" href="'+z[0]+'">'+z[1]+'</a>';}).join("") +
      '<a href="/contact/">Contact</a>' +
      '<a class="btn btn--amber" href="' + PHONE_HREF + '">' + icPhone + PHONE_DISPLAY + '</a>' +
    '</div></div>';

  /* ---------- FOOTER ---------- */
  var footer =
    '<footer class="site-footer"><div class="wrap footer-main">' +
      '<div>' +
        '<div class="foot-brand">' + dropIcon + '<span>Angers Détection Fuite<small>Angers · Détection de fuite</small></span></div>' +
        '<p>Angers Détection Fuite est un service de mise en relation avec des spécialistes qualifiés de la recherche de fuite d\'eau non destructive à Angers et dans le Maine-et-Loire. Nous ne réalisons pas les interventions : nous vous orientons vers un professionnel partenaire près de chez vous.</p>' +
        '<div class="fcontact">' + icPhone + '<a href="' + PHONE_HREF + '">' + PHONE_DISPLAY + '</a></div>' +
        '<div class="fcontact">' + icMail + '<a href="mailto:' + EMAIL + '">' + EMAIL + '</a></div>' +
      '</div>' +
      '<div><h4>Services</h4>' + SERVICES.map(function(s){return '<a href="'+s[0]+'">'+s[1]+'</a>';}).join("") + '</div>' +
      '<div><h4>Zones</h4>' +
        ZONES.map(function(z){return '<a href="'+z[0]+'">'+z[1].charAt(0)+z[1].slice(1).toLowerCase()+'</a>';}).join("") +
        '<a href="/zones/">Toutes les communes →</a>' +
      '</div>' +
      '<div><h4>Informations</h4>' +
        '<a href="/about/">À propos</a>' +
        '<a href="/services/">Nos services</a>' +
        '<a href="/que-faire-fuite-eau/">Conseils &amp; FAQ</a>' +
        '<a href="/mentions-legales/">Mentions légales</a>' +
        '<a href="/confidentialite/">Confidentialité</a>' +
        /* [À CONFIRMER] disponibilité 7j/7 à réactiver si garantie */
        '<div class="fcontact" style="margin-top:14px">' + icClock + '<span>Mise en relation<br>Réponse rapide</span></div>' +
      '</div>' +
    '</div>' +
    '<div class="wrap"><div class="footer-bottom">' +
      '<span>© ' + new Date().getFullYear() + ' Angers Détection Fuite - Service de mise en relation. Tous droits réservés.</span>' +
      '<span>Tarifs indicatifs · devis écrit obligatoire au-delà de 150 € TTC · <a href="/mentions-legales/">Mentions légales</a> · <a href="/confidentialite/">Confidentialité</a></span>' +
    '</div></div></footer>';

  /* ---------- inject ---------- */
  var hMount = document.getElementById("site-header");
  if (hMount) hMount.outerHTML = header; else document.body.insertAdjacentHTML("afterbegin", header);
  var fMount = document.getElementById("site-footer");
  if (fMount) fMount.outerHTML = footer; else document.body.insertAdjacentHTML("beforeend", footer);

  /* ---------- sticky mobile call bar ---------- */
  var callBar =
    '<div class="callbar">' +
      '<a class="callbar__call" href="' + PHONE_HREF + '">' + icPhone + 'Appeler un spécialiste</a>' +
      '<a class="callbar__quote" href="/contact/">Devis gratuit</a>' +
    '</div>';
  document.body.insertAdjacentHTML("beforeend", callBar);

  /* mobile nav toggle */
  var mnav = document.getElementById("mnav");
  var hbtn = document.getElementById("hbtn");
  if (hbtn) hbtn.addEventListener("click", function () { mnav.classList.add("open"); document.body.style.overflow = "hidden"; });
  if (mnav) mnav.addEventListener("click", function (e) {
    if (e.target.hasAttribute("data-close")) { mnav.classList.remove("open"); document.body.style.overflow = ""; }
  });

  /* FAQ accordions */
  document.querySelectorAll(".faq-q").forEach(function (q) {
    q.addEventListener("click", function () { q.closest(".faq-item").classList.toggle("open");
      var a = q.nextElementSibling;
      if (q.closest(".faq-item").classList.contains("open")) { a.style.maxHeight = a.scrollHeight + "px"; }
      else { a.style.maxHeight = 0; }
    });
  });

  /* map facade: load iframe only on click (better CWV, fewer 3rd-party cookies) */
  document.querySelectorAll(".map-facade").forEach(function (m) {
    function load() {
      var url = m.getAttribute("data-map");
      if (!url || m.dataset.loaded) return;
      m.dataset.loaded = "1";
      var f = document.createElement("iframe");
      f.src = url; f.loading = "lazy"; f.title = m.getAttribute("aria-label") || "Carte";
      f.setAttribute("referrerpolicy", "no-referrer-when-downgrade");
      m.appendChild(f);
    }
    m.addEventListener("click", load);
    m.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); load(); } });
  });

  /* fake form submit */
  document.querySelectorAll("form[data-quote]").forEach(function (f) {
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      var ok = f.querySelector(".form-ok");
      f.querySelectorAll(".field,.btn").forEach(function (el) { el.style.display = "none"; });
      if (ok) ok.style.display = "block";
    });
  });
})();
