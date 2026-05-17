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

  /* ---- THEME SWITCHER ---- */
  const themes = [
    {
      name: 'Industrial Red',
      swatch: '#e63312',
      vars: {
        '--black':      '#080808',
        '--white':      '#f5f3ef',
        '--accent':     '#e63312',
        '--accent2':    '#ff6b4a',
        '--gray':       '#9a9a8e',
        '--gray-mid':   '#3a3a34',
        '--gray-light': '#c8c8bc',
        '--border':     'rgba(245,243,239,0.10)',
      }
    },
    {
      name: 'Electric Blue',
      swatch: '#0066ff',
      vars: {
        '--black':      '#060810',
        '--white':      '#eef2ff',
        '--accent':     '#0066ff',
        '--accent2':    '#3d8bff',
        '--gray':       '#8a90a8',
        '--gray-mid':   '#2a2e42',
        '--gray-light': '#b8bdd4',
        '--border':     'rgba(200,210,255,0.10)',
      }
    },
    {
      name: 'Neon Green',
      swatch: '#00e676',
      vars: {
        '--black':      '#050805',
        '--white':      '#edfff3',
        '--accent':     '#00c853',
        '--accent2':    '#00e676',
        '--gray':       '#8aa890',
        '--gray-mid':   '#1e3028',
        '--gray-light': '#b8d4bc',
        '--border':     'rgba(200,255,210,0.10)',
      }
    },
    {
      name: 'Gold Premium',
      swatch: '#c9a84c',
      vars: {
        '--black':      '#090806',
        '--white':      '#f8f4ec',
        '--accent':     '#c9a84c',
        '--accent2':    '#e8c56a',
        '--gray':       '#9a9080',
        '--gray-mid':   '#3a3020',
        '--gray-light': '#c8bca8',
        '--border':     'rgba(240,220,180,0.10)',
      }
    },
    {
      name: 'Purple Dark',
      swatch: '#8b5cf6',
      vars: {
        '--black':      '#07060e',
        '--white':      '#f0eeff',
        '--accent':     '#8b5cf6',
        '--accent2':    '#a78bfa',
        '--gray':       '#8a88a0',
        '--gray-mid':   '#28253a',
        '--gray-light': '#bab8d0',
        '--border':     'rgba(200,195,255,0.10)',
      }
    },
    {
      name: 'Monochrome',
      swatch: '#ffffff',
      vars: {
        '--black':      '#050505',
        '--white':      '#f0f0f0',
        '--accent':     '#e8e8e8',
        '--accent2':    '#ffffff',
        '--gray':       '#888888',
        '--gray-mid':   '#333333',
        '--gray-light': '#bbbbbb',
        '--border':     'rgba(255,255,255,0.12)',
      }
    },
  ];

  // Inject switcher HTML
  const switcherHTML = `
    <div id="theme-switcher">
      <div id="theme-panel">
        <h6>Motyw kolorów</h6>
        ${themes.map((t, i) => `
          <button class="theme-preset${i === 0 ? ' active' : ''}" data-index="${i}">
            <span class="theme-swatch" style="background:${t.swatch}"></span>
            ${t.name}
          </button>
        `).join('')}
      </div>
      <button id="theme-toggle-btn" aria-label="Zmień motyw">
        <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.41-1.41M17.66 6.34l1.41-1.41"/></svg>
      </button>
    </div>
  `;
  document.body.insertAdjacentHTML('beforeend', switcherHTML);

  const panel = document.getElementById('theme-panel');
  const toggleBtn = document.getElementById('theme-toggle-btn');

  function applyTheme(index) {
    const t = themes[index];
    const root = document.documentElement;
    Object.entries(t.vars).forEach(([k, v]) => root.style.setProperty(k, v));
    document.querySelectorAll('.theme-preset').forEach((btn, i) => {
      btn.classList.toggle('active', i === index);
    });
    localStorage.setItem('za-theme', index);
  }

  toggleBtn.addEventListener('click', () => panel.classList.toggle('open'));
  document.addEventListener('click', e => {
    if (!e.target.closest('#theme-switcher')) panel.classList.remove('open');
  });
  document.querySelectorAll('.theme-preset').forEach(btn => {
    btn.addEventListener('click', () => {
      applyTheme(parseInt(btn.dataset.index));
    });
  });

  // Restore saved theme
  const saved = localStorage.getItem('za-theme');
  if (saved !== null) applyTheme(parseInt(saved));

  // Add theme presets to cursor hover
  document.querySelectorAll('.theme-preset, #theme-toggle-btn').forEach(el => {
    el.addEventListener('mouseenter', () => cursor && cursor.classList.add('hovering'));
    el.addEventListener('mouseleave', () => cursor && cursor.classList.remove('hovering'));
  });

});
