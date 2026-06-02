// ===== HEADER SCROLL =====
const header = document.querySelector('.header');
if (header) {
  window.addEventListener('scroll', () => {
    header.style.borderBottomColor = window.scrollY > 20
      ? 'rgba(255,255,255,0.1)'
      : 'rgba(255,255,255,0.05)';
  }, { passive: true });
}

// ===== MOBILE MENU =====
const menuToggle = document.querySelector('.menu-toggle');
if (menuToggle) {
  menuToggle.addEventListener('click', () => {
    const open = document.body.classList.toggle('menu-open');
    menuToggle.setAttribute('aria-expanded', open);
    menuToggle.setAttribute('aria-label', open ? 'Zamknij menu' : 'Otwórz menu');
  });
  document.querySelectorAll('.mobile-nav a').forEach(a => {
    a.addEventListener('click', () => document.body.classList.remove('menu-open'));
  });
}

// ===== FADE IN ON SCROLL =====
const observer = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('visible');
      observer.unobserve(e.target);
    }
  });
}, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));

// ===== ACTIVE TOC LINK =====
const tocLinks = document.querySelectorAll('.sidebar-toc a');
const headings = document.querySelectorAll('.article-content h2, .article-content h3');
if (tocLinks.length && headings.length) {
  const headingObserver = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        tocLinks.forEach(l => l.classList.remove('active'));
        const active = document.querySelector(`.sidebar-toc a[href="#${e.target.id}"]`);
        if (active) active.classList.add('active');
      }
    });
  }, { rootMargin: '-20% 0px -60% 0px' });
  headings.forEach(h => { if (h.id) headingObserver.observe(h); });
}
