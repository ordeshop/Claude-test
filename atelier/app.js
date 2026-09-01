/* ============================================================================
   LEINWERK — Interaktion
   Rendert die Kollektion aus products.js, öffnet die Detail-Lightbox und
   steuert den Anfrage-Flow (Formular via Web3Forms + WhatsApp-Deeplink).
   Reines Vanilla-JS, kein Build-Step.
   ========================================================================== */
(function () {
  "use strict";

  /* --- Konfiguration -------------------------------------------------------
     Trage hier später deine echten Zugangsdaten ein. */
  var WEB3FORMS_KEY = "WEB3FORMS_KEY";          // Access Key von web3forms.com
  var WHATSAPP_NUMBER = "49XXXXXXXXXX";          // ohne + und ohne Leerzeichen, z.B. 4915112345678
  var EMPFAENGER_BETREFF = "Neue Anfrage über die LEINWERK-Website";

  var euro = function (n) {
    return new Intl.NumberFormat("de-DE", {
      style: "currency", currency: "EUR", minimumFractionDigits: 0, maximumFractionDigits: 0
    }).format(n);
  };
  var esc = function (s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  };
  var statusMeta = {
    "verkauft":   { cls: "is-sold",   badge: "badge--sold",    label: "Verkauft" },
    "auf Anfrage":{ cls: "is-request",badge: "badge--request", label: "Auf Anfrage" },
    "verfügbar":  { cls: "",          badge: "",               label: "" }
  };

  /* --- <picture>-Baustein: WebP + Fallback --------------------------------- */
  function pictureHTML(basePath, alt, sizesClass) {
    return (
      '<picture>' +
        '<source srcset="' + esc(basePath) + '.webp" type="image/webp">' +
        '<img src="' + esc(basePath) + '.jpg" alt="' + esc(alt) + '" ' +
             'width="800" height="1000" loading="lazy" decoding="async"' +
             (sizesClass ? ' class="' + sizesClass + '"' : '') + '>' +
      '</picture>'
    );
  }

  /* --- Kollektion rendern -------------------------------------------------- */
  var grid = document.getElementById("collection-grid");
  var products = (typeof PRODUCTS !== "undefined") ? PRODUCTS : [];

  products.forEach(function (p) {
    var meta = statusMeta[p.status] || statusMeta["verfügbar"];
    var card = document.createElement("button");
    card.type = "button";
    card.className = "card " + meta.cls;
    card.setAttribute("data-id", p.id);
    card.setAttribute("aria-haspopup", "dialog");
    card.setAttribute("aria-label", p.titel + " – Details ansehen");

    var badge = meta.label
      ? '<span class="badge ' + meta.badge + '">' + esc(meta.label) + '</span>'
      : "";
    var cover = (p.bilder && p.bilder[0]) || "images/placeholder-1";

    card.innerHTML =
      '<div class="card-media">' + badge + pictureHTML(cover, p.titel) + '</div>' +
      '<div class="card-body">' +
        '<h3 class="card-title serif">' + esc(p.titel) + '</h3>' +
        '<div class="card-meta">' +
          '<span class="card-price">' + euro(p.preis) + '</span>' +
          '<span class="card-size">' + esc(p.groesse) + '</span>' +
        '</div>' +
      '</div>';

    card.addEventListener("click", function () { openLightbox(p); });
    grid.appendChild(card);
  });

  /* --- Detail-Lightbox ----------------------------------------------------- */
  var lb        = document.getElementById("lightbox");
  var lbGallery = document.getElementById("lb-gallery");
  var lbThumbs  = document.getElementById("lb-thumbs");
  var lbTitle   = document.getElementById("lb-title");
  var lbPrice   = document.getElementById("lb-price");
  var lbDesc    = document.getElementById("lb-desc");
  var lbSpecs   = document.getElementById("lb-specs");
  var lbActions = document.getElementById("lb-actions");
  var lastFocused = null;

  function openLightbox(p) {
    lastFocused = document.activeElement;
    var imgs = (p.bilder && p.bilder.length) ? p.bilder : ["images/placeholder-1"];

    lbTitle.textContent = p.titel;
    lbPrice.textContent = euro(p.preis);
    lbDesc.textContent  = p.beschreibung;

    // Hauptbild
    lbGallery.innerHTML =
      '<img id="lb-main" src="' + esc(imgs[0]) + '.jpg" alt="' + esc(p.titel) + '" ' +
      'width="800" height="1000">';
    var mainImg = document.getElementById("lb-main");

    // Thumbnails nur bei mehreren Bildern
    lbThumbs.innerHTML = "";
    if (imgs.length > 1) {
      imgs.forEach(function (src, i) {
        var t = document.createElement("button");
        t.type = "button";
        t.setAttribute("aria-current", i === 0 ? "true" : "false");
        t.setAttribute("aria-label", "Bild " + (i + 1) + " anzeigen");
        t.innerHTML = '<img src="' + esc(src) + '.jpg" alt="" width="54" height="66">';
        t.addEventListener("click", function () {
          mainImg.src = src + ".jpg";
          Array.prototype.forEach.call(lbThumbs.children, function (c, ci) {
            c.setAttribute("aria-current", ci === i ? "true" : "false");
          });
        });
        lbThumbs.appendChild(t);
      });
    }

    // Spezifikationen
    var specs = [
      ["Größe", p.groesse],
      ["Material", p.material],
      ["Pflege", p.pflege],
      ["Status", p.status]
    ];
    lbSpecs.innerHTML = specs.filter(function (s) { return s[1]; }).map(function (s) {
      return '<li><span class="k">' + esc(s[0]) + '</span><span>' + esc(s[1]) + '</span></li>';
    }).join("");

    // Aktionen: Anfrage (Formular) + WhatsApp
    var waText = "Anfrage: " + p.titel + ", Größe " + p.groesse + " — ";
    var waHref = "https://wa.me/" + WHATSAPP_NUMBER + "?text=" + encodeURIComponent(waText);
    lbActions.innerHTML =
      '<button type="button" class="btn btn--solid" data-anfrage>Per Formular anfragen</button>' +
      '<a class="btn btn--ghost" href="' + waHref + '" target="_blank" rel="noopener">Über WhatsApp</a>';
    lbActions.querySelector("[data-anfrage]").addEventListener("click", function () {
      closeLightbox();
      prefillAndScroll(p);
    });

    lb.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
    // Fokus in den Dialog
    document.getElementById("lb-close").focus();
    document.addEventListener("keydown", onLbKey);
  }

  function closeLightbox() {
    lb.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
    document.removeEventListener("keydown", onLbKey);
    if (lastFocused && lastFocused.focus) lastFocused.focus();
  }

  function onLbKey(e) {
    if (e.key === "Escape") { closeLightbox(); return; }
    if (e.key === "Tab") {
      // einfacher Fokus-Trap innerhalb des Dialogs
      var f = lb.querySelectorAll('button, a[href], [tabindex]:not([tabindex="-1"])');
      if (!f.length) return;
      var first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    }
  }

  document.getElementById("lb-close").addEventListener("click", closeLightbox);
  lb.addEventListener("click", function (e) { if (e.target === lb) closeLightbox(); });

  /* --- Anfrage: Nachricht vorbefüllen + zum Formular scrollen --------------- */
  var form        = document.getElementById("anfrage-form");
  var msgField    = document.getElementById("f-nachricht");
  var contactSec  = document.getElementById("kontakt");

  function prefillAndScroll(p) {
    msgField.value = "Anfrage: " + p.titel + ", Größe " + p.groesse + " — ";
    contactSec.scrollIntoView({ behavior: prefersReducedMotion() ? "auto" : "smooth", block: "start" });
    // Cursor ans Ende setzen, sobald sichtbar
    setTimeout(function () {
      msgField.focus();
      var end = msgField.value.length;
      msgField.setSelectionRange(end, end);
    }, prefersReducedMotion() ? 0 : 500);
  }
  function prefersReducedMotion() {
    return window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  }

  /* --- Formular: Validierung + Web3Forms-Versand --------------------------- */
  var statusEl  = document.getElementById("form-status");
  var successEl = document.getElementById("form-success");

  function setError(id, message) {
    var input = document.getElementById(id);
    var errEl = document.getElementById(id + "-error");
    if (message) {
      input.setAttribute("aria-invalid", "true");
      if (errEl) errEl.textContent = message;
    } else {
      input.removeAttribute("aria-invalid");
      if (errEl) errEl.textContent = "";
    }
  }

  function validate() {
    var ok = true;
    var name = document.getElementById("f-name");
    var mail = document.getElementById("f-email");
    var msg  = document.getElementById("f-nachricht");
    var dsgvo = document.getElementById("f-dsgvo");

    if (!name.value.trim()) { setError("f-name", "Bitte gib deinen Namen an."); ok = false; }
    else setError("f-name", "");

    var mailRe = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!mail.value.trim()) { setError("f-email", "Bitte gib deine E-Mail-Adresse an."); ok = false; }
    else if (!mailRe.test(mail.value.trim())) { setError("f-email", "Diese E-Mail-Adresse sieht nicht gültig aus."); ok = false; }
    else setError("f-email", "");

    if (!msg.value.trim()) { setError("f-nachricht", "Bitte schreib uns kurz, worum es geht."); ok = false; }
    else setError("f-nachricht", "");

    if (!dsgvo.checked) { setError("f-dsgvo", "Bitte bestätige die Datenschutzerklärung."); ok = false; }
    else setError("f-dsgvo", "");

    return ok;
  }

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    statusEl.textContent = ""; statusEl.className = "form-status";

    // Honeypot: gefüllt = Bot → still verwerfen (Erfolg vortäuschen)
    if (document.getElementById("f-website").value) { showSuccess(); return; }

    if (!validate()) {
      statusEl.textContent = "Bitte prüf die markierten Felder.";
      statusEl.className = "form-status is-err";
      var firstInvalid = form.querySelector('[aria-invalid="true"]');
      if (firstInvalid) firstInvalid.focus();
      return;
    }

    var submitBtn = form.querySelector('[type="submit"]');
    submitBtn.disabled = true;
    statusEl.textContent = "Wird gesendet …"; statusEl.className = "form-status";

    var data = {
      access_key: WEB3FORMS_KEY,
      subject: EMPFAENGER_BETREFF,
      from_name: "LEINWERK Website",
      name: document.getElementById("f-name").value.trim(),
      email: document.getElementById("f-email").value.trim(),
      telefon: document.getElementById("f-telefon").value.trim(),
      message: document.getElementById("f-nachricht").value.trim(),
      botcheck: "" // Web3Forms-eigener Honeypot
    };

    fetch("https://api.web3forms.com/submit", {
      method: "POST",
      headers: { "Content-Type": "application/json", "Accept": "application/json" },
      body: JSON.stringify(data)
    })
      .then(function (r) { return r.json().then(function (j) { return { ok: r.ok, j: j }; }); })
      .then(function (res) {
        if (res.ok && res.j && res.j.success) {
          showSuccess();
        } else {
          var m = (res.j && res.j.message) ? res.j.message : "Unbekannter Fehler.";
          throw new Error(m);
        }
      })
      .catch(function (err) {
        statusEl.textContent =
          "Das hat leider nicht geklappt (" + err.message + "). " +
          "Bitte schreib direkt an die angegebene E-Mail oder per WhatsApp.";
        statusEl.className = "form-status is-err";
      })
      .finally(function () { submitBtn.disabled = false; });
  });

  function showSuccess() {
    form.hidden = true;
    successEl.classList.add("is-visible");
    successEl.setAttribute("tabindex", "-1");
    successEl.focus();
  }

  /* --- Jahr im Footer ------------------------------------------------------ */
  var yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = new Date().getFullYear();
})();
