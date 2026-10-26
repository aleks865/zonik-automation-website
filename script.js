/* ZONIK AUTOMATION — script.js */
(function () {
  document.documentElement.classList.remove('no-js');

  /* ---- Google Analytics (Consent Mode v2, ładowane po zgodzie) ---- */
  var GA_ID = 'G-9X9LQVGN8P';
  window.dataLayer = window.dataLayer || [];
  window.gtag = function () { dataLayer.push(arguments); };
  gtag('consent', 'default', { analytics_storage: 'denied', ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied', wait_for_update: 500 });
  var gaLoaded = false;
  function loadGA() {
    if (gaLoaded) return; gaLoaded = true;
    gtag('consent', 'update', { analytics_storage: 'granted' });
    var s = document.createElement('script');
    s.async = true; s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
    document.head.appendChild(s);
    gtag('js', new Date()); gtag('config', GA_ID);
  }
  function getConsent() { try { return localStorage.getItem('za_cookie_consent'); } catch (e) { return null; } }
  function setConsent(v) { try { localStorage.setItem('za_cookie_consent', v); } catch (e) {} }
  if (getConsent() === 'accepted') loadGA();
  function track(name, params) { try { gtag('event', name, params || {}); } catch (e) {} }

  document.addEventListener('DOMContentLoaded', function () {
    var body = document.body;

    /* Cookie banner */
    var cookie = document.getElementById('cookie');
    if (cookie && !getConsent()) cookie.classList.add('show');
    var acc = document.getElementById('cookie-accept'), rej = document.getElementById('cookie-reject');
    acc && acc.addEventListener('click', function () { setConsent('accepted'); cookie.classList.remove('show'); loadGA(); onScroll(); });
    rej && rej.addEventListener('click', function () { setConsent('rejected'); cookie.classList.remove('show'); onScroll(); });

    /* Header + mobile bar on scroll */
    var header = document.querySelector('.header');
    var mbar = document.querySelector('.mbar');
    function onScroll() {
      var y = window.scrollY;
      header && header.classList.toggle('is-solid', y > 40);
      mbar && mbar.classList.toggle('show', y > 500 && !(cookie && cookie.classList.contains('show')));
    }
    window.addEventListener('scroll', onScroll, { passive: true }); onScroll();

    /* Mobile menu */
    var burger = document.querySelector('.burger');
    function setMenu(open) {
      body.classList.toggle('menu-open', open);
      burger && burger.setAttribute('aria-expanded', open ? 'true' : 'false');
      body.style.overflow = open ? 'hidden' : '';
      header && header.classList.toggle('is-solid', open || window.scrollY > 40);
    }
    burger && burger.addEventListener('click', function () { setMenu(!body.classList.contains('menu-open')); });
    document.querySelectorAll('.mnav a').forEach(function (a) { a.addEventListener('click', function () { setMenu(false); }); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { setMenu(false); closeLb(); } });

    /* Reveal on scroll */
    var rv = document.querySelectorAll('.rv');
    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (en) {
        en.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
      }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });
      rv.forEach(function (el) { io.observe(el); });
    } else { rv.forEach(function (el) { el.classList.add('in'); }); }

    /* Lightbox */
    var lb = document.getElementById('lb');
    var lbImg = lb && lb.querySelector('img'), lbCap = lb && lb.querySelector('.lb__cap');
    var items = Array.prototype.slice.call(document.querySelectorAll('[data-full]'));
    var cur = 0;
    function show(i) {
      cur = (i + items.length) % items.length;
      var el = items[cur];
      lbImg.src = el.getAttribute('data-full');
      lbImg.alt = el.querySelector('img') ? el.querySelector('img').alt : '';
      lbCap.textContent = el.getAttribute('data-cap') || '';
    }
    function openLb(i) { if (!lb) return; show(i); lb.classList.add('open'); body.style.overflow = 'hidden'; track('view_project', { project: items[i].getAttribute('data-cap') }); }
    window.closeLb = function () { if (lb && lb.classList.contains('open')) { lb.classList.remove('open'); body.style.overflow = ''; } };
    var closeLb = window.closeLb;
    items.forEach(function (el, i) {
      el.addEventListener('click', function () { openLb(i); });
      el.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); openLb(i); } });
    });
    if (lb) {
      lb.querySelector('.lb__close').addEventListener('click', closeLb);
      lb.querySelector('.lb__nav--prev').addEventListener('click', function (e) { e.stopPropagation(); show(cur - 1); });
      lb.querySelector('.lb__nav--next').addEventListener('click', function (e) { e.stopPropagation(); show(cur + 1); });
      lb.addEventListener('click', function (e) { if (e.target === lb) closeLb(); });
      document.addEventListener('keydown', function (e) {
        if (!lb.classList.contains('open')) return;
        if (e.key === 'ArrowLeft') show(cur - 1);
        if (e.key === 'ArrowRight') show(cur + 1);
      });
    }

    /* Conversion tracking: phone / e-mail clicks */
    document.querySelectorAll('a[href^="tel:"]').forEach(function (a) { a.addEventListener('click', function () { track('click_phone', { location: a.getAttribute('data-loc') || '' }); }); });
    document.querySelectorAll('a[href^="mailto:"]').forEach(function (a) { a.addEventListener('click', function () { track('click_email'); }); });

    /* Contact form (Formspree, bez przeładowania strony) */
    var form = document.getElementById('contact-form');
    if (form) {
      var status = form.querySelector('.form__status');
      var btn = form.querySelector('button[type=submit]');
      form.addEventListener('submit', function (e) {
        e.preventDefault();
        if (!form.checkValidity()) { form.reportValidity(); return; }
        btn.disabled = true; var t = btn.textContent; btn.textContent = 'Wysyłanie…';
        status.className = 'form__status';
        fetch(form.action, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } })
          .then(function (r) {
            if (!r.ok) throw new Error();
            form.reset();
            status.className = 'form__status ok';
            status.textContent = 'Dziękujemy! Wiadomość została wysłana — odezwiemy się w ciągu 1 dnia roboczego.';
            track('generate_lead', { method: 'form' });
          })
          .catch(function () {
            status.className = 'form__status err';
            status.textContent = 'Nie udało się wysłać wiadomości. Zadzwoń: +48 511 357 787 lub napisz: kontakt@zonikautomation.pl';
          })
          .finally(function () { btn.disabled = false; btn.textContent = t; });
      });
    }

    /* Rok w stopce */
    var y = document.getElementById('year'); if (y) y.textContent = new Date().getFullYear();
  });
})();
