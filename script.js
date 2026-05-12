/* ============================================================
   ZONIK AUTOMATION — Main JS
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {

  /* ---- CUSTOM CURSOR ---- */
  const cursor = document.querySelector('.cursor');
  if (cursor && window.matchMedia('(hover: hover)').matches) {
    let mouseX = 0, mouseY = 0;
    document.addEventListener('mousemove', e => {
      mouseX = e.clientX; mouseY = e.clientY;
      cursor.style.left = mouseX + 'px';
      cursor.style.top  = mouseY + 'px';
    });
    document.querySelectorAll('a, button, [data-hover]').forEach(el => {
      el.addEventListener('mouseenter', () => cursor.classList.add('hovering'));
      el.addEventListener('mouseleave', () => cursor.classList.remove('hovering'));
    });
  }

  /* ---- HEADER SCROLL ---- */
  const header = document.querySelector('.header');
  const onScroll = () => {
    header && header.classList.toggle('scrolled', window.scrollY > 60);
    const btn = document.getElementById('scrollTopBtn');
    if (btn) btn.classList.toggle('visible', window.scrollY > 400);
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ---- SCROLL TO TOP ---- */
  const scrollBtn = document.getElementById('scrollTopBtn');
  if (scrollBtn) {
    scrollBtn.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
  }

  /* ---- MOBILE MENU ---- */
  const menuToggle = document.querySelector('.menu-toggle');
  const mobileNav  = document.querySelector('.mobile-nav');
  const spans = menuToggle ? menuToggle.querySelectorAll('span') : [];

  let menuOpen = false;
  function toggleMenu(force) {
    menuOpen = force !== undefined ? force : !menuOpen;
    if (mobileNav) mobileNav.classList.toggle('open', menuOpen);
    document.body.style.overflow = menuOpen ? 'hidden' : '';
    if (spans.length >= 3) {
      spans[0].style.transform = menuOpen ? 'translateY(6.5px) rotate(45deg)' : '';
      spans[1].style.opacity   = menuOpen ? '0' : '1';
      spans[2].style.transform = menuOpen ? 'translateY(-6.5px) rotate(-45deg)' : '';
    }
  }
  if (menuToggle) menuToggle.addEventListener('click', () => toggleMenu());
  if (mobileNav) {
    mobileNav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => toggleMenu(false)));
  }
  document.addEventListener('keydown', e => { if (e.key === 'Escape') toggleMenu(false); });

  /* ---- REVEAL ON SCROLL ---- */
  const reveals = document.querySelectorAll('.reveal');
  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.08, rootMargin: '0px 0px -60px 0px' });
  reveals.forEach(el => revealObserver.observe(el));

  /* ---- LIGHTBOX ---- */
  const lightbox  = document.getElementById('lightbox');
  const lbImg     = document.getElementById('lightbox-img');
  window.openLightbox = (img) => {
    if (!lightbox || !lbImg) return;
    lbImg.src = img.src; lbImg.alt = img.alt;
    lightbox.classList.add('open');
    document.body.style.overflow = 'hidden';
  };
  window.closeLightbox = () => {
    if (!lightbox) return;
    lightbox.classList.remove('open');
    document.body.style.overflow = '';
  };
  if (lightbox) {
    lightbox.addEventListener('click', e => { if (e.target === lightbox || e.target.classList.contains('lightbox-close')) closeLightbox(); });
    document.addEventListener('keydown', e => { if (e.key === 'Escape') closeLightbox(); });
  }

  /* ---- CONTACT FORM ---- */
  const form = document.getElementById('contact-form');
  if (form) {
    const msg = document.getElementById('form-message');
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const email = form.querySelector('#email');
      const message = form.querySelector('#message');
      if (msg) { msg.className = 'form-message'; msg.textContent = ''; }

      const emailRx = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
      if (!email || !emailRx.test(email.value.trim())) {
        if (msg) { msg.className = 'form-message error'; msg.textContent = 'Wpisz poprawny adres e-mail.'; }
        email && email.focus(); return;
      }
      if (!message || message.value.trim() === '') {
        if (msg) { msg.className = 'form-message error'; msg.textContent = 'Opisz zakres prac lub treść zapytania.'; }
        message && message.focus(); return;
      }

      const btn = form.querySelector('button[type=submit]');
      if (btn) { btn.disabled = true; btn.textContent = 'Wysyłanie…'; }

      try {
        const res = await fetch('https://formspree.io/f/mzdylbea', {
          method: 'POST', body: new FormData(form),
          headers: { Accept: 'application/json' }
        });
        if (res.ok) {
          if (msg) { msg.className = 'form-message success'; msg.textContent = 'Dziękujemy! Odpiszemy najszybciej jak to możliwe.'; }
          form.reset();
        } else throw new Error();
      } catch {
        if (msg) { msg.className = 'form-message error'; msg.textContent = 'Wystąpił błąd. Zadzwoń lub napisz bezpośrednio na e-mail.'; }
      } finally {
        if (btn) { btn.disabled = false; btn.textContent = 'Wyślij zapytanie'; }
      }
    });
  }

  /* ---- COUNTER ANIMATION ---- */
  const counters = document.querySelectorAll('[data-count]');
  const counterObserver = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      const el = entry.target;
      const target = parseInt(el.dataset.count, 10);
      const suffix = el.dataset.suffix || '';
      const duration = 1800;
      const start = performance.now();
      const tick = (now) => {
        const progress = Math.min((now - start) / duration, 1);
        const ease = 1 - Math.pow(1 - progress, 3);
        el.textContent = Math.round(target * ease) + suffix;
        if (progress < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
      counterObserver.unobserve(el);
    });
  }, { threshold: 0.5 });
  counters.forEach(el => counterObserver.observe(el));

  /* ---- PARALLAX on hero bg glow ---- */
  const glow = document.querySelector('.hero-bg-glow');
  if (glow) {
    window.addEventListener('scroll', () => {
      const y = window.scrollY;
      glow.style.transform = `translateY(${y * 0.15}px)`;
    }, { passive: true });
  }

});
