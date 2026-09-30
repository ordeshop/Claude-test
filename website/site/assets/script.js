// Mobile-Menü
(function () {
  var burger = document.querySelector('.burger');
  var nav = document.getElementById('nav');
  if (!burger || !nav) return;

  burger.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    burger.setAttribute('aria-label', open ? 'Menü schließen' : 'Menü öffnen');
  });

  nav.addEventListener('click', function (e) {
    if (e.target.tagName === 'A') {
      nav.classList.remove('open');
      burger.setAttribute('aria-expanded', 'false');
    }
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && nav.classList.contains('open')) {
      nav.classList.remove('open');
      burger.setAttribute('aria-expanded', 'false');
      burger.focus();
    }
  });
})();

// FAQ: immer nur eine Antwort offen
(function () {
  var items = document.querySelectorAll('.faq details');
  items.forEach(function (d) {
    d.addEventListener('toggle', function () {
      if (!d.open) return;
      items.forEach(function (o) { if (o !== d) o.open = false; });
    });
  });
})();

// Einblenden beim Scrollen
(function () {
  var els = document.querySelectorAll('.reveal');
  if (!els.length) return;

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduced || !('IntersectionObserver' in window)) {
    els.forEach(function (el) { el.classList.add('in'); });
    return;
  }

  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('in');
      io.unobserve(entry.target);
    });
  }, { rootMargin: '0px 0px -10% 0px', threshold: 0.08 });

  els.forEach(function (el) { io.observe(el); });
})();

// Demos im Handy-Rahmen durchwechseln
(function () {
  var slides = document.querySelectorAll('.pslide');
  var label = document.getElementById('phoneLabel');
  if (slides.length < 2) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  var i = 0;
  var takt = null;

  function weiter() {
    slides[i].classList.remove('is-active');
    i = (i + 1) % slides.length;
    slides[i].classList.add('is-active');
    if (label) label.innerHTML = slides[i].getAttribute('data-label') || '';
  }

  function start() { if (!takt) takt = setInterval(weiter, 4200); }
  function stopp() { clearInterval(takt); takt = null; }

  // Nur laufen lassen, solange der Rahmen sichtbar ist und der Tab offen ist
  var rahmen = document.querySelector('.phone');
  if (rahmen && 'IntersectionObserver' in window) {
    new IntersectionObserver(function (e) {
      e[0].isIntersecting ? start() : stopp();
    }, { threshold: 0.2 }).observe(rahmen);
  } else {
    start();
  }
  document.addEventListener('visibilitychange', function () {
    document.hidden ? stopp() : start();
  });
})();

/* ============================================================
   Zusätzliche Bewegung
   ============================================================ */
(function () {
  var ruhig = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Fortschrittsbalken beim Scrollen
  var bar = document.createElement('div');
  bar.className = 'progress';
  document.body.appendChild(bar);

  // Nach-oben-Knopf
  var top = document.createElement('button');
  top.className = 'toTop';
  top.type = 'button';
  top.setAttribute('aria-label', 'Nach oben');
  top.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5M5 12l7-7 7 7"/></svg>';
  top.addEventListener('click', function () {
    window.scrollTo({ top: 0, behavior: ruhig ? 'auto' : 'smooth' });
  });
  document.body.appendChild(top);

  var head = document.querySelector('.site-head');
  var laeuft = false;
  function beiScroll() {
    var y = window.scrollY || document.documentElement.scrollTop;
    var hoehe = document.documentElement.scrollHeight - window.innerHeight;
    bar.style.transform = 'scaleX(' + (hoehe > 0 ? Math.min(y / hoehe, 1) : 0) + ')';
    if (head) head.classList.toggle('scrolled', y > 12);
    top.classList.toggle('show', y > 600);
    laeuft = false;
  }
  window.addEventListener('scroll', function () {
    if (laeuft) return;
    laeuft = true;
    window.requestAnimationFrame(beiScroll);
  }, { passive: true });
  beiScroll();

  // Zahlen im Hero hochzählen
  var zahlen = document.querySelectorAll('.facts strong');
  if (zahlen.length && !ruhig && 'IntersectionObserver' in window) {
    var zio = new IntersectionObserver(function (eintraege) {
      eintraege.forEach(function (e) {
        if (!e.isIntersecting) return;
        zio.unobserve(e.target);
        var el = e.target, roh = el.textContent;
        var treffer = roh.match(/[\d.]+/);
        if (!treffer) return;
        var ziel = parseFloat(treffer[0].replace(/\./g, ''));
        if (!ziel) return;
        var start = performance.now(), dauer = 900;
        function schritt(jetzt) {
          var p = Math.min((jetzt - start) / dauer, 1);
          var wert = Math.round(ziel * (1 - Math.pow(1 - p, 3)));
          el.textContent = roh.replace(treffer[0], wert.toLocaleString('de-DE'));
          if (p < 1) requestAnimationFrame(schritt);
          else el.textContent = roh;
        }
        requestAnimationFrame(schritt);
      });
    }, { threshold: .5 });
    zahlen.forEach(function (z) { zio.observe(z); });
  }

  // Tabellenzeilen nacheinander einblenden
  var zeilen = document.querySelectorAll('.compare tbody tr');
  if (zeilen.length) {
    if (ruhig || !('IntersectionObserver' in window)) {
      zeilen.forEach(function (r) { r.classList.add('in'); });
    } else {
      var tio = new IntersectionObserver(function (eintraege) {
        eintraege.forEach(function (e) {
          if (!e.isIntersecting) return;
          var i = Array.prototype.indexOf.call(zeilen, e.target);
          setTimeout(function () { e.target.classList.add('in'); }, Math.min(i, 12) * 45);
          tio.unobserve(e.target);
        });
      }, { threshold: .15 });
      zeilen.forEach(function (r) { tio.observe(r); });
    }
  }
})();


/* ============================================================
   Intro beim ersten Aufruf der Seite
   Läuft nur auf der Startseite, nur einmal je Sitzung,
   und wird bei "Bewegung reduzieren" übersprungen.
   ============================================================ */
(function () {
  var ruhig = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (ruhig) return;

  // Nur auf der Startseite
  var pfad = location.pathname.split('/').pop();
  if (pfad && pfad !== 'index.html' && pfad !== '') return;

  // Nur beim ersten Aufruf in dieser Sitzung
  try {
    if (sessionStorage.getItem('orde-intro')) return;
    sessionStorage.setItem('orde-intro', '1');
  } catch (e) { /* ohne Speicher trotzdem zeigen */ }

  var wort = 'ORDÉ';
  var buchstaben = '';
  for (var i = 0; i < wort.length; i++) {
    buchstaben += '<span style="animation-delay:' + (i * 0.14) + 's">' + wort[i] + '</span>';
  }

  var el = document.createElement('div');
  el.id = 'intro';
  el.setAttribute('aria-hidden', 'true');
  el.innerHTML =
    '<div class="mitte">' +
      '<div class="wort">' + buchstaben + '</div>' +
      '<div class="strich"></div>' +
      '<p class="unter">Sch&ouml;n geordnet</p>' +
    '</div>';

  document.documentElement.classList.add('startet');
  document.body.classList.add('startet');
  document.body.appendChild(el);

  var weg = false;
  function schliessen() {
    if (weg) return;
    weg = true;
    el.classList.add('weg');
    document.body.classList.remove('startet');
    document.body.classList.add('los');
    setTimeout(function () { el.remove(); }, 800);
  }

  // Nach 2,5 Sekunden weg. Überspringen ist möglich, aber erst nach gut einer
  // Sekunde – sonst reißt schon die erste Scroll-Bewegung das Intro weg.
  var timer = setTimeout(schliessen, 2500);
  setTimeout(function () {
    ['pointerdown', 'keydown', 'wheel', 'touchstart'].forEach(function (ev) {
      window.addEventListener(ev, function () {
        clearTimeout(timer);
        schliessen();
      }, { once: true, passive: true });
    });
  }, 1100);

  // Sicherheitsnetz: spätestens wenn alles geladen ist, plus kurz
  window.addEventListener('load', function () {
    setTimeout(schliessen, 2500);
  });
})();

/* Fehlerhinweis am Formular zeigen, wenn kontakt.php zurueckschickt */
(function () {
  if (!/[?&]fehler=1/.test(location.search)) return;
  var box = document.getElementById('formFehler');
  if (!box) return;
  box.hidden = false;
  box.setAttribute('role', 'alert');
  box.scrollIntoView({ behavior: 'smooth', block: 'center' });
})();
