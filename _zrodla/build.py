#!/usr/bin/env python3
"""Generator stron HTML Zonik Automation. Uruchom z katalogu repo: python _zrodla/build.py
Generuje pliki .html w katalogu głównym. style.css i script.js edytuje się ręcznie."""
import json, re, os, html

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)  # katalog główny repozytorium
SITE = 'https://zonikautomation.pl'
TEL, TEL_H = '+48511357787', '+48 511 357 787'
MAIL = 'kontakt@zonikautomation.pl'
FORM = 'https://formspree.io/f/mzdylbea'
LEGAL_NAME = 'Zonik Automation Aleks Zonik'
NIP = '7133147668'
REG_ADDR = 'Jabłonna Druga 147H, 23-114'

# ---------------------------------------------------------------- icons
I = {
 'arrow': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 'phone': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg>',
 'mail': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>',
 'pin': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>',
 'clock': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>',
 'check': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="m8 12 3 3 5-6"/></svg>',
 # services
 'cabinet': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="2" width="16" height="20" rx="1.5"/><path d="M4 8h16M4 14h16M8 5h3M8 11h2M14 11h2M8 17h2M14 17h2"/></svg>',
 'code': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="3" width="20" height="14" rx="2"/><path d="m9 8-2.5 2.5L9 13M15 8l2.5 2.5L15 13M8 21h8M12 17v4"/></svg>',
 'meter': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="5" y="2" width="14" height="20" rx="2"/><rect x="8" y="5" width="8" height="5" rx="1"/><circle cx="12" cy="15.5" r="2.5"/><path d="M12 15.5l1.5-1.5"/></svg>',
 'plan': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h3l1.5-2 2 4 1.5-2H17M8 18h8"/></svg>',
 # industries
 'water': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2.7S5.5 9.6 5.5 14a6.5 6.5 0 0 0 13 0c0-4.4-6.5-11.3-6.5-11.3z"/><path d="M9 15a3 3 0 0 0 3 3"/></svg>',
 'pharma': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10.5 20.5 3.5 13.5a5 5 0 0 1 7-7l7 7a5 5 0 0 1-7 7z"/><path d="m8.5 8.5 7 7"/></svg>',
 'food': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 7c-4 0-7 3-7 7s3 8 7 8 7-4 7-8-3-7-7-7z"/><path d="M12 7c0-2 1-4 3-5M12 7c-1-1.5-3-2-4.5-1.5"/></svg>',
 'block': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="5" y="2" width="14" height="20" rx="1"/><path d="M9 6h1M14 6h1M9 10h1M14 10h1M9 14h1M14 14h1M10 22v-4h4v4"/></svg>',
 'gear': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/></svg>',
 'line': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 20h20M4 20v-6h4v6M10 20V9h4v11M16 20V4h4v16"/></svg>',
}

FONTS = ('<link rel="preload" href="fonts/syne-latin-700-normal.woff2" as="font" type="font/woff2" crossorigin>'
         '<link rel="preload" href="fonts/dm-sans-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>')

SERVICES = [
  dict(slug='automatyka-przemyslowa.html', ico='cabinet', name='Automatyka przemysłowa', short='Automatyka',
       desc='Prefabrykacja szaf sterowniczych i rozdzielnic oraz okablowanie maszyn i linii produkcyjnych — od schematu po uruchomienie.',
       bullets=['Prefabrykacja szaf sterowniczych i rozdzielnic', 'Okablowanie maszyn, linii i instalacji', 'Podłączenie i uruchomienie na obiekcie']),
  dict(slug='programowanie-plc.html', ico='code', name='Programowanie PLC i HMI', short='Programowanie',
       desc='Oprogramowanie sterowników i paneli operatorskich — nowe aplikacje, zmiany w istniejących programach i diagnostyka.',
       bullets=['Siemens S7-1200 / S7-1500, TIA Portal', 'Allen-Bradley', 'Panele HMI, wizualizacja SCADA, komunikacja przemysłowa']),
  dict(slug='pomiary-elektryczne.html', ico='meter', name='Pomiary elektryczne', short='Pomiary',
       desc='Pomiary odbiorcze i okresowe instalacji elektrycznych — z protokołem, który przyjmie inspektor, ubezpieczyciel i dział UR.',
       bullets=['Pomiary odbiorcze nowych instalacji', 'Pomiary okresowe dużych instalacji', 'Czytelne protokoły pomiarowe']),
  dict(slug='schematy-elektryczne.html', ico='plan', name='Projekty i dokumentacja', short='Projekty',
       desc='Schematy szaf sterowniczych i rozdzielnic, projekty wykonawcze instalacji i dokumentacja powykonawcza w EPLAN i AutoCAD.',
       bullets=['Schematy zasilania i obwodów sterowania', 'Dokumentacja powykonawcza, listy I/O, BOM', 'Odtworzenie i aktualizacja starej dokumentacji']),
]

INDUSTRIES = [
  ('water', 'Uzdatnianie wody', 'Szafy sterownicze, okablowanie i programowanie dla stacji uzdatniania wody.'),
  ('gear', 'Producenci maszyn', 'Szafy sterownicze i okablowanie dla firm, które budują maszyny.'),
  ('food', 'Przetwórstwo owoców i warzyw', 'Automatyka maszyn do mycia, sortowania i obróbki.'),
  ('line', 'Linie produkcyjne', 'Okablowanie, programowanie i uruchomienie linii.'),
  ('block', 'Budynki wielorodzinne', 'Pomiary elektryczne odbiorcze i okresowe.'),
]

# Realizacje — dodaj tu nowe prace (zdjęcie w images/realizacje/<img>.jpg i <img>-m.jpg)
WORKS = [
  dict(img='plyta-montazowa-prefabrykacja', title='Prefabrykacja płyty montażowej szafy sterowniczej',
       tags=['Automatyka', 'Prefabrykacja'],
       desc='Kompletna płyta montażowa: zasilanie, zabezpieczenia, styczniki i przekaźniki, listwy zaciskowe. Okablowanie w korytach, przewody opisane zgodnie ze schematem.'),
  dict(img='szafa-sterownicza-s7-1200', title='Szafa sterownicza z PLC Siemens S7-1200',
       tags=['Siemens S7-1200', 'Programowanie'],
       desc='Projekt, montaż i uruchomienie szafy sterowniczej z modułami I/O, zasilaniem 24 V DC i zabezpieczeniami obwodów.'),
  dict(img='szafa-sterownicza-montaz', title='Rozdzielnica z automatyką — montaż na obiekcie',
       tags=['Montaż', 'Uruchomienie'],
       desc='Montaż, podłączenie i uruchomienie rozdzielnicy z modułami automatyki. Oznaczone obwody i dokumentacja powykonawcza.'),
  dict(img='szafa-sterownicza-okablowanie', title='Szafa wolnostojąca — okablowanie i uruchomienie',
       tags=['Automatyka', 'Okablowanie'],
       desc='Okablowanie szafy wolnostojącej z modułami wejść/wyjść, uporządkowane trasy kablowe i rezerwa miejsca na rozbudowę.'),
]

TECH = ['Siemens S7-1200', 'Siemens S7-1500', 'TIA Portal', 'Allen-Bradley', 'Panele HMI', 'SCADA', 'Profinet', 'Modbus RTU / TCP',
        'Falowniki', 'EPLAN', 'AutoCAD', 'Schneider Electric', 'ABB', 'Eaton', 'Rittal', 'Aplisens']

FAQ = [
  ('Na jakim terenie działacie?', 'Bazujemy w Warszawie, ale realizujemy projekty w całej Polsce. Prefabrykację szaf wykonujemy u siebie, a na obiekt przyjeżdżamy na montaż, uruchomienie i pomiary.'),
  ('Czy możecie zmienić program PLC napisany przez kogoś innego?', 'Tak. Regularnie modyfikujemy i rozbudowujemy istniejące programy — także bez dokumentacji. Zaczynamy od kopii zapasowej i analizy programu, a po zmianach przekazujemy zaktualizowany projekt.'),
  ('Czy wystawiacie protokoły z pomiarów elektrycznych?', 'Tak. Po każdym pomiarze otrzymujesz protokół z wynikami i oceną.'),
  ('Czy przygotujecie dokumentację do istniejącej szafy lub maszyny?', 'Tak — odtwarzamy schematy na podstawie stanu faktycznego i przygotowujemy aktualną dokumentację w EPLAN lub AutoCAD.'),
  ('Jak wygląda wycena?', 'Opisz zakres w formularzu lub zadzwoń. Przy prostszych zleceniach wycenę przygotowujemy na podstawie opisu i zdjęć, przy większych — po rozmowie lub wizji lokalnej. Wycena jest bezpłatna.'),
  ('Czy zapewniacie wsparcie po uruchomieniu?', 'Tak. Po zakończeniu projektu pozostajemy dostępni — pomagamy w diagnostyce, zmianach w programie i rozbudowie układu.'),
]

# ---------------------------------------------------------------- partials
def head(title, desc, path, extra_ld=None, robots='index, follow'):
    url = SITE + '/' + ('' if path == 'index.html' else path)
    ld = [{
        "@context": "https://schema.org", "@type": "ProfessionalService", "@id": SITE + "/#firma",
        "name": "Zonik Automation", "legalName": LEGAL_NAME, "taxID": NIP, "url": SITE + "/", "image": SITE + "/images/og.jpg", "logo": SITE + "/favicon.svg",
        "description": "Automatyka przemysłowa, programowanie PLC, pomiary elektryczne oraz projekty i dokumentacja elektryczna.",
        "telephone": TEL, "email": MAIL,
        "address": {"@type": "PostalAddress", "addressLocality": "Warszawa", "addressRegion": "mazowieckie", "addressCountry": "PL"},
        "areaServed": [{"@type": "Country", "name": "Polska"}],
        "openingHours": "Mo-Fr 08:00-18:00",
        "knowsAbout": ["Automatyka przemysłowa", "Programowanie PLC", "Siemens TIA Portal", "Szafy sterownicze", "Pomiary elektryczne", "Schematy elektryczne", "EPLAN"],
    }]
    if extra_ld: ld += extra_ld
    ld_html = ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    return f'''<!DOCTYPE html>
<html lang="pl" class="no-js">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="pl_PL">
<meta property="og:site_name" content="Zonik Automation">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/images/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0e1013">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="images/apple-touch-icon.png">
{FONTS}
<link rel="stylesheet" href="style.css?v=4">
{ld_html}
<script src="script.js?v=4" defer></script>
</head>
<body>
<a class="skip" href="#main">Przejdź do treści</a>
'''

def B(href, text, cls='btn--light', extra=''):
    return f'<a class="btn {cls}" href="{href}"{extra}><span class="btn__t">{text}</span><span class="btn__i">{I["arrow"]}</span></a>'

def header(active=''):
    links = [('index.html#uslugi', 'Usługi'), ('index.html#branze', 'Branże'), ('index.html#realizacje', 'Realizacje'),
             ('index.html#proces', 'Jak pracujemy'), ('index.html#kontakt', 'Kontakt')]
    nav = ''.join(f'<a href="{h}">{t}</a>' for h, t in links)
    mitems = [(s['slug'], s['name']) for s in SERVICES] + [('index.html#realizacje', 'Realizacje'), ('index.html#kontakt', 'Kontakt')]
    mnav = ''.join(f'<a class="mnav__link" href="{h}">{t}<small>0{i+1}</small></a>' for i, (h, t) in enumerate(mitems))
    return f'''<header class="header">
  <div class="wrap header__in">
    <a href="index.html" class="logo" aria-label="Zonik Automation — strona główna">
      <span class="logo__mark">ZA</span>
      <span class="logo__txt"><span class="logo__name">Zonik Automation</span><span class="logo__sub">Automatyka przemysłowa</span></span>
    </a>
    <nav class="nav" aria-label="Główne menu">{nav}</nav>
    <div class="header__cta">
      <a class="header__tel ulink" href="tel:{TEL}" data-loc="header">{TEL_H}</a>
      {B('index.html#kontakt', 'Bezpłatna wycena')}
      <button class="burger" aria-label="Menu" aria-expanded="false" aria-controls="mnav"><span></span></button>
    </div>
  </div>
</header>
<nav class="mnav" id="mnav" aria-label="Menu mobilne">
  {mnav}
  {B('index.html#kontakt', 'Bezpłatna wycena')}
  <div class="mnav__contact"><a href="tel:{TEL}" data-loc="menu">{TEL_H}</a><a href="mailto:{MAIL}">{MAIL}</a></div>
</nav>
'''

def footer():
    svc = ''.join(f'<li><a class="ulink" href="{s["slug"]}">{s["name"]}</a></li>' for s in SERVICES)
    return f'''<footer class="footer">
  <div class="wrap">
    <div class="footer__grid">
      <div class="footer__brand">
        <a href="index.html" class="logo"><span class="logo__mark">ZA</span><span class="logo__txt"><span class="logo__name">Zonik Automation</span><span class="logo__sub">Automatyka przemysłowa</span></span></a>
        <p>Automatyka przemysłowa, programowanie PLC, pomiary elektryczne oraz projekty i dokumentacja. Warszawa i cała Polska.</p>
        <p class="footer__legal">{LEGAL_NAME}<br>NIP {NIP}</p>
      </div>
      <div><h4>Usługi</h4><ul>{svc}</ul></div>
      <div><h4>Firma</h4><ul>
        <li><a class="ulink" href="index.html#realizacje">Realizacje</a></li>
        <li><a class="ulink" href="index.html#branze">Branże</a></li>
        <li><a class="ulink" href="poradnik-automatyka-przemyslowa.html">Poradnik automatyki</a></li>
        <li><a class="ulink" href="polityka-prywatnosci.html">Polityka prywatności</a></li>
      </ul></div>
      <div><h4>Kontakt</h4><ul>
        <li><a class="ulink" href="tel:{TEL}" data-loc="footer">{TEL_H}</a></li>
        <li><a class="ulink" href="mailto:{MAIL}">{MAIL}</a></li>
        <li>Pon–Pt 8:00–18:00</li>
        <li>Warszawa i cała Polska</li>
      </ul></div>
    </div>
    <div class="footer__word" aria-hidden="true">Zonik</div>
    <div class="footer__bot"><span>© <span id="year">2026</span> {LEGAL_NAME}</span><a href="polityka-prywatnosci.html">Polityka prywatności</a></div>
  </div>
</footer>
<div class="mbar" aria-label="Szybki kontakt">
  <a class="btn btn--ghost btn--noi" href="tel:{TEL}" data-loc="mobile-bar">{I['phone']}Zadzwoń</a>
  <a class="btn btn--light btn--noi" href="index.html#kontakt">Wycena</a>
</div>
<div class="cookie" id="cookie" role="dialog" aria-label="Zgoda na cookies">
  <p>Używamy Google Analytics, aby sprawdzać, jak korzystasz ze strony. Dane są anonimowe. <a href="polityka-prywatnosci.html">Polityka prywatności</a></p>
  <div class="cookie__btns"><button class="btn btn--light btn--noi" id="cookie-accept">Akceptuję</button><button class="btn btn--ghost" id="cookie-reject">Odrzuć</button></div>
</div>
</body>
</html>
'''

def cta(title='Masz projekt lub problem do rozwiązania?', text='Opisz krótko zakres — odpowiemy w ciągu 1 dnia roboczego i przygotujemy bezpłatną wycenę.'):
    return f'''<section class="cta">
  <div class="wrap cta__in">
    <div class="rv"><h2>{title}</h2><p>{text}</p></div>
    <div class="cta__btns rv rv-d1">
      {B('index.html#kontakt', 'Poproś o wycenę')}
      <a class="btn btn--ghost" href="tel:{TEL}" data-loc="cta">{TEL_H}</a>
    </div>
  </div>
</section>
'''

def works_html(items):
    out = []
    for w in items:
        chips = ''.join(f'<span class="chip{" chip--a" if i == 0 else ""}">{t}</span>' for i, t in enumerate(w['tags']))
        out.append(f'''<article class="work rv">
  <div class="work__img" role="button" tabindex="0" aria-label="Powiększ zdjęcie: {w['title']}" data-full="images/realizacje/{w['img']}.jpg" data-cap="{w['title']}">
    <img src="images/realizacje/{w['img']}-m.jpg" alt="{w['title']} — Zonik Automation" loading="lazy" width="800" height="660">
  </div>
  <div class="work__body"><div class="work__meta">{chips}</div><h3>{w['title']}</h3><p>{w['desc']}</p></div>
</article>''')
    return '\n'.join(out)

LIGHTBOX = '''<div class="lb" id="lb" role="dialog" aria-modal="true" aria-label="Podgląd zdjęcia">
  <button class="lb__close" aria-label="Zamknij">×</button>
  <button class="lb__nav lb__nav--prev" aria-label="Poprzednie">‹</button>
  <img src="" alt="">
  <button class="lb__nav lb__nav--next" aria-label="Następne">›</button>
  <p class="lb__cap"></p>
</div>'''

def write(path, s):
    p = os.path.join(OUT, path); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8', newline='\n').write(s)

# ---------------------------------------------------------------- index
SVC_IMG = ['plyta-montazowa-prefabrykacja', 'szafa-sterownicza-s7-1200', 'szafa-sterownicza-montaz', 'szafa-sterownicza-okablowanie']

def works_home(items):
    out = []
    for i, w in enumerate(items):
        out.append(f'''<article class="witem rv">
  <div class="witem__img" role="button" tabindex="0" aria-label="Powiększ zdjęcie: {w['title']}" data-full="images/realizacje/{w['img']}.jpg" data-cap="{w['title']}">
    <img src="images/realizacje/{w['img']}-m.jpg" srcset="images/realizacje/{w['img']}-m.jpg 800w, images/realizacje/{w['img']}.jpg 1800w" sizes="(max-width: 760px) 100vw, 55vw" alt="{w['title']} — Zonik Automation" loading="lazy">
  </div>
  <div class="witem__meta"><span>R—{i+1:02d}</span><span>{' · '.join(w['tags'])}</span></div>
  <h3>{w['title']}</h3>
  <p>{w['desc']}</p>
</article>''')
    return '\n'.join(out)

def index():
    rows = '\n'.join(f'''<a class="srow" href="{s['slug']}">
  <span class="srow__n">(0{i+1})</span>
  <span class="srow__t">{s['name']}</span>
  <span class="srow__d">{s['desc']}<span>{' / '.join(s['bullets'][:2])}</span></span>
  <span class="srow__a">{I['arrow']}</span>
</a>''' for i, s in enumerate(SERVICES))
    floats = ''.join(f'<img src="images/realizacje/{im}-m.jpg" alt="" loading="lazy">' for im in SVC_IMG)
    inds = '\n'.join(f'<div class="bt bt--{i+1} rv rv-d{i%3}"><div class="bt__top"><span class="bt__n">0{i+1}</span><span class="bt__ico">{I[ic]}</span></div><div class="bt__body"><h3>{n}</h3><p>{d}</p></div></div>' for i, (ic, n, d) in enumerate(INDUSTRIES))
    deliv = [
      ('Schematy i dokumentacja powykonawcza', 'Aktualne schematy zgodne ze stanem faktycznym, lista I/O i zestawienie aparatury — w PDF i w wersji edytowalnej.'),
      ('Protokoły z pomiarów', 'Rzetelnie wykonane pomiary z czytelnym protokołem, gotowym do odbioru.'),
      ('Kopia programu PLC i HMI', 'Pełny, opisany projekt oprogramowania. Nie zostajesz zależny od jednej osoby ani jednego laptopa.'),
      ('Porządek w szafie', 'Opisane przewody i aparaty, uporządkowane trasy kablowe i rezerwa miejsca na rozbudowę.'),
      ('Uruchomienie i przeszkolenie', 'Testujemy układ na obiekcie i pokazujemy operatorom oraz utrzymaniu ruchu, jak z niego korzystać.'),
      ('Wsparcie po odbiorze', 'Pomagamy w diagnostyce, zmianach w programie i rozbudowie — także po zakończeniu projektu.'),
    ]
    deliv_h = '\n'.join(f'<div class="dv rv rv-d{i%3}"><p class="dv__n">0{i+1}</p><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(deliv))
    steps = [
      ('Rozmowa i analiza', 'Poznajemy obiekt, problem i oczekiwania. W razie potrzeby przyjeżdżamy na wizję lokalną.'),
      ('Projekt i wycena', 'Konkretny zakres, dobór aparatury i harmonogram. Bez niespodzianek w trakcie realizacji.'),
      ('Prefabrykacja i montaż', 'Szafy budujemy i testujemy w warsztacie, a na obiekcie montujemy je sprawnie i czysto.'),
      ('Uruchomienie i testy', 'Programowanie, testy funkcjonalne, pomiary elektryczne i odbiór z Twoim zespołem.'),
      ('Dokumentacja i wsparcie', 'Komplet dokumentacji, kopia programu i nasza dostępność po odbiorze.'),
    ]
    steps_h = '\n'.join(f'<li class="pstep rv"><span class="pstep__n">0{i+1}</span><div><h3>{t}</h3><p>{d}</p></div></li>' for i, (t, d) in enumerate(steps))
    mq = ''.join(f'<span>{t}</span>' for t in ['Siemens S7-1500', 'TIA Portal', 'Allen-Bradley', 'EPLAN', 'Profinet', 'Pomiary elektryczne', 'Szafy sterownicze', 'HMI · SCADA'] * 2)
    tech_h = ''.join(f'<span>{t}</span>' for t in TECH)
    faq_h = '\n'.join(f'<details><summary><span class="q-n">0{i+1}</span><span>{q}</span></summary><p>{a}</p></details>' for i, (q, a) in enumerate(FAQ))
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage",
              "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}
    opts = ''.join(f'<option>{s["name"]}</option>' for s in SERVICES)

    s = head('Automatyka przemysłowa, programowanie PLC i pomiary elektryczne | Zonik Automation',
             'Szafy sterownicze, programowanie PLC (Siemens TIA Portal), pomiary elektryczne z protokołem oraz projekty i dokumentacja. Uzdatnianie wody, producenci maszyn, przetwórstwo spożywcze. Warszawa i cała Polska.',
             'index.html', [faq_ld])
    s += header()
    s += f'''<main id="main">
<section class="hero">
  <div class="wrap">
    <div class="hero__meta fade-up"><span>Zonik Automation — Automatyka · PLC · Pomiary · Projekty</span><span>Warszawa / cała Polska</span></div>
    <h1 aria-label="Automatyka przemysłowa, PLC i pomiary">
      <span class="ln"><span>Automatyka</span></span>
      <span class="ln"><span>przemysłowa</span></span>
      <span class="ln"><span>PLC <em>&amp;</em> pomiary</span></span>
    </h1>
    <div class="hero__bot fade-up">
      <p class="hero__lead">Projektujemy, budujemy i uruchamiamy układy sterowania dla zakładów produkcyjnych, producentów maszyn i stacji uzdatniania wody. Od schematu, przez program PLC, po protokół z pomiarów.</p>
      <div class="hero__btns">
        {B('#kontakt', 'Bezpłatna wycena')}
        <a class="btn btn--ghost" href="#realizacje">Zobacz realizacje</a>
      </div>
      <div class="scroll-ind"><i></i>Przewiń</div>
    </div>
  </div>
</section>

<div class="band">
  <div class="band__frame">
    <img src="images/realizacje/plyta-montazowa-prefabrykacja.jpg" alt="Płyta montażowa szafy sterowniczej wykonana przez Zonik Automation" width="1800" height="1541">
    <div class="band__cap"><span>R—01 / Prefabrykacja szafy sterowniczej</span><span>Projekt · Montaż · Uruchomienie</span></div>
  </div>
</div>

<section class="section section--dark" id="o-firmie">
  <div class="wrap">
    <p class="tag">O firmie</p>
    <p class="statement">Łączymy projekt, prefabrykację, programowanie i pomiary w jednym miejscu. Pracujemy tam, gdzie przestój kosztuje, a dokumentacja jest wymagana — i oddajemy układy, które da się serwisować przez lata.</p>
    <div class="stats">
      <div class="stat rv"><div class="stat__v">130+</div><div class="stat__l">zrealizowanych projektów</div></div>
      <div class="stat rv rv-d1"><div class="stat__v">PL</div><div class="stat__l">realizacje w całej Polsce</div></div>
      <div class="stat rv rv-d2"><div class="stat__v">4</div><div class="stat__l">obszary: automatyka, PLC, pomiary, projekty</div></div>
      <div class="stat rv rv-d3"><div class="stat__v">24h</div><div class="stat__l">odpowiedź na zapytanie w dni robocze</div></div>
    </div>
  </div>
</section>

<section class="section section--white" id="uslugi">
  <div class="wrap">
    <div class="sec-head">
      <div><p class="tag">Usługi</p><h2>Co robimy<span class="count">(04)</span></h2></div>
      <p>Jeden wykonawca — od projektu po uruchomienie. Nie musisz koordynować kilku firm: odpowiadamy za całość i przekazujemy kompletną dokumentację.</p>
    </div>
    <div class="slist">
{rows}
    </div>
  </div>
</section>

<div class="marquee" aria-hidden="true"><div class="marquee__track">{mq}</div></div>

<section class="section" id="branze">
  <div class="wrap">
    <div class="sec-head">
      <div><p class="tag">Branże</p><h2>Branże, które znamy<span class="count">({len(INDUSTRIES):02d})</span></h2></div>
      <p>Pracujemy tam, gdzie liczy się niezawodność, porządek i dokumentacja.</p>
    </div>
    <div class="bento">
{inds}
    </div>
  </div>
</section>

<section class="section section--dark" id="realizacje">
  <div class="wrap">
    <div class="sec-head">
      <div><p class="tag">Realizacje</p><h2>Wybrane projekty<span class="count">({len(WORKS):02d})</span></h2></div>
      <p>Każda szafa i każdy układ przechodzi przez nasze ręce od projektu do uruchomienia. Kliknij zdjęcie, aby je powiększyć.</p>
    </div>
    <div class="wgrid">
{works_home(WORKS)}
    </div>
  </div>
</section>

<section class="section section--white" id="standard">
  <div class="wrap">
    <div class="sec-head">
      <div><p class="tag">Standard wykonania</p><h2>Co dostajesz w każdym projekcie</h2></div>
      <p>Układ, który działa dziś, to połowa sukcesu. Druga połowa to możliwość jego serwisu i rozbudowy za kilka lat — także przez kogoś innego.</p>
    </div>
    <div class="deliv">
{deliv_h}
    </div>
  </div>
</section>

<section class="section section--dark" id="proces">
  <div class="wrap proc">
    <div class="proc__head">
      <p class="tag">Jak pracujemy</p>
      <h2>Przejrzysty proces, bez niespodzianek</h2>
      <p>Na każdym etapie wiesz, co się dzieje i co będzie dalej. Terminy ustalamy na starcie i trzymamy się ich.</p>
    </div>
    <ol class="proc__list">
{steps_h}
    </ol>
  </div>
</section>

<section class="section" id="technologie">
  <div class="wrap">
    <div class="sec-head">
      <div><p class="tag">Sprzęt i oprogramowanie</p><h2>Sprawdzone standardy</h2></div>
      <p>Dobieramy sterowniki i aparaturę, które są dostępne, serwisowalne i znane działom utrzymania ruchu.</p>
    </div>
    <div class="tech rv">{tech_h}</div>
  </div>
</section>

<section class="section section--white" id="faq">
  <div class="wrap">
    <div class="sec-head"><div><p class="tag">FAQ</p><h2>Najczęstsze pytania</h2></div><p>Nie znalazłeś odpowiedzi? Zadzwoń: <a class="ulink" href="tel:{TEL}" data-loc="faq"><strong>{TEL_H}</strong></a></p></div>
    <div class="faq">
{faq_h}
    </div>
  </div>
</section>

<section class="section section--dark" id="kontakt">
  <div class="wrap">
    <p class="tag">Kontakt</p>
    <h2 class="contact__big rv-ln"><span class="ln"><span>Porozmawiajmy</span></span><span class="ln"><span>o projekcie.</span></span></h2>
    <a class="contact__mail" href="mailto:{MAIL}"><span>{MAIL}</span></a>
    <div class="contact">
      <div>
        <p>Opisz obiekt, zakres i termin. Odpowiemy w ciągu 1 dnia roboczego i przygotujemy bezpłatną wycenę. Możesz też od razu zadzwonić.</p>
        <div class="cinfo" style="margin-top:28px">
          <a href="tel:{TEL}" data-loc="contact"><small>Telefon</small><span>{TEL_H}</span></a>
          <a href="mailto:{MAIL}"><small>E-mail</small><span>{MAIL}</span></a>
          <div><small>Obszar</small><span>Warszawa i cała Polska</span></div>
          <div><small>Godziny</small><span>Pon–Pt 8:00–18:00</span></div>
          <div><small>Firma</small><span>{LEGAL_NAME}<br>NIP {NIP}</span></div>
        </div>
      </div>
      <form class="form" id="contact-form" action="{FORM}" method="POST">
        <div class="form__row">
          <div class="field"><label for="f-name">Imię i nazwisko / firma</label><input id="f-name" name="name" autocomplete="name" placeholder="Jan Kowalski, ABC Sp. z o.o."></div>
          <div class="field"><label for="f-tel">Telefon</label><input id="f-tel" name="phone" type="tel" autocomplete="tel" placeholder="+48 …"></div>
        </div>
        <div class="form__row">
          <div class="field"><label for="f-mail">E-mail *</label><input id="f-mail" name="email" type="email" required autocomplete="email" placeholder="adres@firma.pl"></div>
          <div class="field"><label for="f-svc">Temat</label><select id="f-svc" name="service"><option value="">Wybierz…</option>{opts}<option>Serwis / awaria</option><option>Inne</option></select></div>
        </div>
        <div class="field"><label for="f-msg">Opis projektu *</label><textarea id="f-msg" name="message" required placeholder="Obiekt, zakres prac, termin. Możesz dodać link do zdjęć lub dokumentacji."></textarea></div>
        <input type="hidden" name="_subject" value="Zapytanie ze strony zonikautomation.pl">
        <input type="text" name="_gotcha" style="display:none" tabindex="-1" autocomplete="off">
        <div class="form__status" role="status" aria-live="polite"></div>
        <div class="form__foot">
          <p class="form__note">Wysyłając formularz, akceptujesz <a href="polityka-prywatnosci.html">politykę prywatności</a>. Dane wykorzystamy tylko do odpowiedzi na zapytanie.</p>
          <button class="btn btn--light" type="submit"><span class="btn__t">Wyślij zapytanie</span><span class="btn__i">{I['arrow']}</span></button>
        </div>
      </form>
    </div>
  </div>
</section>
</main>
{LIGHTBOX}
'''
    s += footer()
    write('index.html', s)

# ---------------------------------------------------------------- service pages
def service_page(sv, h1, lead, title, mdesc, intro_h, intro_p, boxes, split_img, split_h, split_p, checks, works_sel, faq=None):
    crumbs_ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Strona główna", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": sv['name'], "item": SITE + "/" + sv['slug']}]}
    svc_ld = {"@context": "https://schema.org", "@type": "Service", "name": sv['name'], "description": mdesc,
              "provider": {"@id": SITE + "/#firma"}, "areaServed": "Polska"}
    lds = [crumbs_ld, svc_ld]
    if faq:
        lds.append({"@context": "https://schema.org", "@type": "FAQPage",
                    "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]})
    s = head(title, mdesc, sv['slug'], lds)
    s += header()
    boxes_h = '\n'.join(f'<div class="box rv"><h3>{t}</h3><p>{d}</p>{"<ul>" + "".join(f"<li>{x}</li>" for x in li) + "</ul>" if li else ""}</div>' for t, d, li in boxes)
    checks_h = ''.join(f'<li>{I["check"]}<span>{c}</span></li>' for c in checks)
    rel = ''.join(f'<a href="{o["slug"]}">{o["name"]}{I["arrow"]}</a>' for o in SERVICES if o is not sv)
    ws = [w for w in WORKS if w['img'] in works_sel]
    works_sec = f'''<section class="section section--alt">
  <div class="wrap">
    <div class="sec-head"><div><p class="tag">Realizacje</p><h2>Przykłady naszej pracy</h2></div><p><a class="link-arrow" href="index.html#realizacje">Wszystkie realizacje {I['arrow']}</a></p></div>
    <div class="works">{works_html(ws)}</div>
  </div>
</section>''' if ws else ''
    faq_sec = ''
    if faq:
        faq_h = '\n'.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in faq)
        faq_sec = f'''<section class="section"><div class="wrap"><div class="sec-head sec-head--center"><div><p class="tag">FAQ</p><h2>Pytania i odpowiedzi</h2></div></div><div class="faq faq--simple">{faq_h}</div></div></section>'''
    s += f'''<main id="main">
<section class="phero">
  <div class="wrap">
    <nav class="crumbs" aria-label="Okruszki"><a href="index.html">Strona główna</a><span>/</span><a href="index.html#uslugi">Usługi</a><span>/</span><span>{sv['name']}</span></nav>
    <p class="tag">{sv['name']}</p>
    <h1>{h1}</h1>
    <p>{lead}</p>
    <div class="hero__btns">
      {B('index.html#kontakt', 'Bezpłatna wycena')}
      <a class="btn btn--ghost" href="tel:{TEL}" data-loc="service-hero">{TEL_H}</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head"><div><p class="tag">Zakres</p><h2>{intro_h}</h2></div><p>{intro_p}</p></div>
    <div class="cols">
{boxes_h}
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap split">
    <div class="split__img rv"><img src="images/realizacje/{split_img}.jpg" alt="{split_h} — Zonik Automation" loading="lazy" width="1400" height="1600"></div>
    <div>
      <p class="tag">Dlaczego my</p>
      <h2>{split_h}</h2>
      <p style="margin-top:16px">{split_p}</p>
      <ul class="checks">{checks_h}</ul>
    </div>
  </div>
</section>
{works_sec}
{faq_sec}
<section class="section{' section--alt' if faq else ''}">
  <div class="wrap">
    <div class="sec-head"><div><p class="tag">Pozostałe usługi</p><h2>Zobacz też</h2></div></div>
    <div class="related">{rel}</div>
  </div>
</section>
{cta()}
</main>
{LIGHTBOX}
'''
    s += footer()
    write(sv['slug'], s)

def services():
    A, P, M, D = SERVICES
    service_page(A,
      'Szafy sterownicze i automatyka maszyn',
      'Projektujemy, prefabrykujemy i uruchamiamy układy sterowania dla maszyn, linii produkcyjnych i instalacji technologicznych — dla producentów maszyn, zakładów spożywczych i stacji uzdatniania wody.',
      'Automatyka przemysłowa i szafy sterownicze | Zonik Automation',
      'Projekt, prefabrykacja i uruchomienie szaf sterowniczych. Modernizacja maszyn i linii produkcyjnych, falowniki, układy bezpieczeństwa. Warszawa i cała Polska.',
      'Kompletny układ sterowania z jednej ręki',
      'Bierzemy odpowiedzialność za całość: od doboru aparatury, przez budowę szafy, po program i uruchomienie na obiekcie.',
      [('Projekt i prefabrykacja szaf', 'Szafy sterownicze i zasilające budowane w warsztacie, testowane przed wysyłką na obiekt.', ['Dobór aparatury i obudowy (IP, materiał, chłodzenie)', 'Okablowanie w korytach, opisane przewody', 'Rezerwa miejsca i I/O na rozbudowę']),
       ('Modernizacja maszyn (retrofit)', 'Wymiana przestarzałych sterowników i aparatury bez budowy maszyny od nowa.', ['Migracja starszych sterowników na aktualne platformy', 'Wymiana napędów i zabezpieczeń', 'Aktualizacja dokumentacji']),
       ('Napędy i pomiary procesowe', 'Integracja falowników, czujników i przetworników z układem sterowania.', ['Falowniki i softstarty', 'Sygnały analogowe 4–20 mA, PT100', 'Przepływomierze, przetworniki ciśnienia i poziomu']),
       ('Montaż i uruchomienie na obiekcie', 'Montaż, podłączenie urządzeń polowych, testy funkcjonalne i odbiór.', ['Uruchomienie i testy sekwencji', 'Pomiary elektryczne z protokołem', 'Szkolenie operatorów i UR'])],
      'szafa-sterownicza-s7-1200', 'Szafa, którą da się serwisować za 10 lat',
      'Dobrze zbudowana szafa skraca każdą przyszłą awarię. Dlatego pracujemy według stałego standardu — niezależnie od wielkości projektu.',
      ['Każdy przewód i aparat opisany zgodnie ze schematem', 'Rozdzielone trasy sygnałowe i siłowe — mniej zakłóceń', 'Dokumentacja powykonawcza i kopia programu w komplecie', 'Doświadczenie w uzdatnianiu wody, przetwórstwie spożywczym i budowie maszyn'],
      ['plyta-montazowa-prefabrykacja', 'szafa-sterownicza-s7-1200', 'szafa-sterownicza-okablowanie'],
      [('Czy budujecie szafy według cudzego projektu?', 'Tak. Możemy wykonać prefabrykację na podstawie dostarczonej dokumentacji albo przygotować projekt samodzielnie.'),
       ('Ile trwa wykonanie szafy sterowniczej?', 'Zależy od wielkości i dostępności aparatury. Termin podajemy w wycenie i trzymamy się go — o ewentualnych zmianach informujemy z wyprzedzeniem.'),
       ('Czy możecie zmodernizować starą maszynę?', 'Tak. Najpierw oceniamy stan maszyny i dokumentacji, a potem proponujemy zakres modernizacji, który ma sens ekonomiczny.')])

    service_page(P,
      'Programowanie sterowników PLC i paneli HMI',
      'Piszemy nowe aplikacje, modyfikujemy istniejące programy i diagnozujemy problemy w układach sterowania — Siemens TIA Portal, Allen-Bradley, panele HMI.',
      'Programowanie PLC Siemens TIA Portal i HMI | Zonik Automation',
      'Programowanie sterowników PLC Siemens S7-1200/S7-1500 (TIA Portal) i Allen-Bradley, panele HMI, SCADA, modyfikacja istniejących programów i diagnostyka. Cała Polska.',
      'Czytelny program to krótszy przestój',
      'Program PLC jest sercem maszyny. Piszemy go tak, żeby był zrozumiały dla każdego automatyka, który będzie go serwisował.',
      [('Nowe aplikacje PLC', 'Oprogramowanie maszyn i instalacji od zera, na podstawie opisu procesu.', ['Siemens S7-1200 / S7-1500 w TIA Portal', 'Allen-Bradley', 'Struktura modułowa, tryby ręczny i automatyczny']),
       ('Modyfikacje i rozbudowa', 'Zmiany w istniejących programach — także napisanych przez innych i bez dokumentacji.', ['Analiza i kopia zapasowa przed zmianami', 'Nowe funkcje, receptury, sekwencje', 'Przekazanie zaktualizowanego projektu']),
       ('Panele HMI i wizualizacja', 'Czytelne ekrany operatorskie z diagnostyką, która mówi, co się stało i gdzie.', ['Panele operatorskie HMI', 'Wizualizacja SCADA', 'Alarmy z opisem przyczyny']),
       ('Komunikacja i diagnostyka', 'Integracja urządzeń w sieci przemysłowej i szybkie szukanie przyczyn awarii.', ['Profinet, Modbus RTU / TCP', 'Falowniki i rozproszone I/O', 'Diagnostyka zdalna lub na obiekcie'])],
      'szafa-sterownicza-s7-1200', 'Program, który rozumie każdy automatyk',
      'Nie zostawiamy „czarnej skrzynki”. Otrzymujesz opisany, uporządkowany projekt i kopię zapasową — Twój dział utrzymania ruchu nie jest zależny od nas.',
      ['Modułowa struktura programu i komentarze', 'Alarmy z opisem przyczyny zamiast samych kodów', 'Tryb ręczny i serwisowy dla UR', 'Pełna kopia projektu PLC i HMI po każdej zmianie'],
      ['szafa-sterownicza-s7-1200'],
      [('Na jakich sterownikach pracujecie?', 'Głównie Siemens S7-1200 i S7-1500 w TIA Portal oraz Allen-Bradley. Zapytaj także o inne platformy.'),
       ('Czy możecie poprawić program bez dokumentacji?', 'Tak. Zaczynamy od kopii zapasowej i analizy programu, a po zmianach przekazujemy opisany projekt.')])

    service_page(M,
      'Pomiary elektryczne z protokołem',
      'Wykonujemy pomiary odbiorcze i okresowe instalacji elektrycznych w zakładach, obiektach i budynkach wielorodzinnych. Każdy pomiar kończy się protokołem.',
      'Pomiary elektryczne z protokołem | Zonik Automation',
      'Pomiary elektryczne odbiorcze i okresowe zakładów, obiektów i budynków wielorodzinnych (bloków): izolacja, pętla zwarcia, RCD, uziemienia. Protokoły pomiarowe. Warszawa i cała Polska.',
      'Pomiary instalacji i obiektów',
      'Pomiary przy odbiorze nowych instalacji oraz pomiary okresowe dużych instalacji — w zakładach, obiektach i budynkach wielorodzinnych.',
      [('Pomiary ochrony przeciwporażeniowej', 'Sprawdzenie skuteczności ochrony przed porażeniem prądem.', ['Impedancja pętli zwarcia', 'Wyłączniki różnicowoprądowe (RCD)', 'Ciągłość przewodów ochronnych i wyrównawczych']),
       ('Rezystancja izolacji', 'Pomiary izolacji przewodów, kabli, silników i aparatury.', ['Obwody instalacji', 'Kable zasilające i sterownicze', 'Silniki i maszyny']),
       ('Uziemienia', 'Pomiary rezystancji uziemień ochronnych i roboczych.', ['Uziemienia rozdzielnic i obiektów', 'Uziemienia urządzeń technologicznych']),
       ('Budynki wielorodzinne', 'Pomiary odbiorcze i okresowe instalacji w budynkach.', ['Przeglądy okresowe', 'Komplet protokołów'])],
      'szafa-sterownicza-montaz', 'Protokół, który przejdzie każdą kontrolę',
      'Pomiary wykonujemy rzetelnie i dokumentujemy tak, aby protokół był czytelny dla inspektora, ubezpieczyciela i Twojego działu utrzymania ruchu.',
      ['Doświadczenie w pomiarach dużych instalacji', 'Protokół z wynikami i oceną po każdym pomiarze', 'Wskazanie nieprawidłowości i propozycja naprawy', 'Możliwość połączenia pomiarów z usunięciem usterek'],
      [],
      [('Jak często wykonywać pomiary okresowe?', 'Częstotliwość zależy od rodzaju obiektu i warunków pracy instalacji. Podpowiemy, jaki termin obowiązuje w Twoim przypadku.'),
       ('Czy usuwacie usterki wykryte podczas pomiarów?', 'Tak — możemy od razu przygotować wycenę naprawy i wykonać ponowne pomiary po jej zakończeniu.')])

    service_page(D,
      'Projekty i dokumentacja elektryczna',
      'Schematy elektryczne, projekty szaf sterowniczych i dokumentacja powykonawcza w EPLAN i AutoCAD — dla nowych układów i do istniejących maszyn.',
      'Schematy elektryczne i dokumentacja (EPLAN, AutoCAD) | Zonik Automation',
      'Projekty szaf sterowniczych, schematy elektryczne, dokumentacja powykonawcza, listy I/O i BOM w EPLAN i AutoCAD. Odtwarzanie dokumentacji istniejących maszyn.',
      'Dokumentacja, z której da się korzystać',
      'Dobry schemat oszczędza godziny przy montażu i każdej późniejszej awarii. Tworzymy dokumentację czytelną dla każdego elektryka i automatyka.',
      [('Projekty szaf sterowniczych', 'Kompletna dokumentacja do prefabrykacji szafy.', ['Schematy zasilania i obwodów sterowania', 'Rozmieszczenie aparatury na płycie', 'Listy zacisków i przewodów']),
       ('Dokumentacja powykonawcza', 'Dokumentacja zgodna z tym, co faktycznie zostało zbudowane.', ['Schematy po zmianach z uruchomienia', 'Lista wejść/wyjść PLC', 'Zestawienie aparatury (BOM)']),
       ('Odtwarzanie dokumentacji', 'Schematy dla istniejących maszyn i szaf, do których dokumentacja zaginęła lub jest nieaktualna.', ['Inwentaryzacja na obiekcie', 'Opracowanie w EPLAN lub AutoCAD']),
       ('Formaty i archiwizacja', 'Dokumentację przekazujemy w PDF i w wersji edytowalnej.', ['EPLAN, AutoCAD', 'Oznaczenia zgodne z normami PN-EN', 'Cyfrowe archiwum projektu'])],
      'plyta-montazowa-prefabrykacja', 'Schemat zgodny ze stanem faktycznym',
      'Projektujemy, budujemy i uruchamiamy — więc wiemy, czego potrzebuje elektryk na obiekcie i automatyk przy awarii. Dokumentacja zawsze odzwierciedla to, co faktycznie jest w szafie.',
      ['Spójne oznaczenia na schemacie i w szafie', 'Wersja PDF i edytowalna w komplecie', 'Aktualizacja dokumentacji po zmianach', 'Możliwość połączenia z prefabrykacją i uruchomieniem'],
      ['plyta-montazowa-prefabrykacja'],
      [('Czy przygotujecie dokumentację do istniejącej szafy?', 'Tak — odtwarzamy schematy na podstawie stanu faktycznego i przygotowujemy aktualną dokumentację.'),
       ('W jakich programach pracujecie?', 'Dokumentację przygotowujemy w EPLAN i AutoCAD, a przekazujemy w PDF i w wersji edytowalnej.')])

# ---------------------------------------------------------------- article
def article():
    body = open(os.path.join(HERE, 'poradnik_tresc.html'), encoding='utf-8').read()
    body = body.replace('zakłócenia zakłócają komunikację', 'zakłócenia psują komunikację').replace('nieprzemy­ślana', 'nieprzemyślana')
    s = head('Automatyka przemysłowa — jak zaplanować układ sterowania? Poradnik | Zonik Automation',
             'Jak zaplanować automatykę maszyny lub linii: lista I/O, dobór PLC, projekt szafy sterowniczej, program i dokumentacja. Praktyczny poradnik od automatyków.',
             'poradnik-automatyka-przemyslowa.html',
             [{"@context": "https://schema.org", "@type": "Article", "headline": "Automatyka przemysłowa — od czego zacząć planowanie układu?",
               "author": {"@type": "Organization", "name": "Zonik Automation"}, "publisher": {"@id": SITE + "/#firma"}, "datePublished": "2025-02-15", "dateModified": "2026-10-26"}])
    s += header()
    s += f'''<main id="main">
<section class="phero"><div class="wrap">
  <nav class="crumbs" aria-label="Okruszki"><a href="index.html">Strona główna</a><span>/</span><a href="automatyka-przemyslowa.html">Automatyka przemysłowa</a><span>/</span><span>Poradnik</span></nav>
  <p class="tag">Poradnik</p>
  <h1>Automatyka przemysłowa — od czego zacząć planowanie układu?</h1>
  <p>Lista sygnałów, dobór sterownika, projekt szafy, program i dokumentacja — krok po kroku.</p>
</div></section>
<section class="section"><div class="wrap"><article class="prose">
{body}
<div class="note"><h3>Planujesz automatyzację maszyny lub linii?</h3><p>Projektujemy szafy sterownicze, piszemy oprogramowanie PLC i dostarczamy pełną dokumentację techniczną. Opisz projekt — przygotujemy bezpłatną wycenę.</p>{B('index.html#kontakt', 'Poproś o wycenę')}</div>
</article></div></section>
</main>
'''
    s += footer()
    write('poradnik-automatyka-przemyslowa.html', s)

# ---------------------------------------------------------------- privacy
def privacy():
    s = head('Polityka prywatności | Zonik Automation', 'Informacje o przetwarzaniu danych osobowych i plikach cookies na stronie zonikautomation.pl.', 'polityka-prywatnosci.html')
    s += header()
    s += f'''<main id="main">
<section class="phero"><div class="wrap">
  <nav class="crumbs" aria-label="Okruszki"><a href="index.html">Strona główna</a><span>/</span><span>Polityka prywatności</span></nav>
  <h1>Polityka prywatności</h1>
  <p>Informacje o przetwarzaniu danych osobowych przez Zonik Automation. Ostatnia aktualizacja: październik 2026.</p>
</div></section>
<section class="section"><div class="wrap"><div class="prose">
<h2>1. Administrator danych</h2>
<p>Administratorem danych osobowych jest {LEGAL_NAME}, {REG_ADDR}, NIP {NIP}. Kontakt w sprawach ochrony danych: <a href="mailto:{MAIL}">{MAIL}</a>, tel. {TEL_H}.</p>
<h2>2. Jakie dane zbieramy</h2>
<p>Zbieramy wyłącznie dane, które sam(a) nam przekazujesz — przez formularz kontaktowy, e-mail lub telefon:</p>
<ul><li>imię i nazwisko lub nazwa firmy,</li><li>adres e-mail,</li><li>numer telefonu (opcjonalnie),</li><li>treść zapytania.</li></ul>
<h2>3. Cel i podstawa przetwarzania</h2>
<ul>
<li>odpowiedź na zapytanie i przygotowanie wyceny oraz podjęcie działań przed zawarciem umowy (art. 6 ust. 1 lit. b RODO),</li>
<li>realizacja umowy (art. 6 ust. 1 lit. b RODO),</li>
<li>prawnie uzasadniony interes administratora, np. kontakt w sprawie zapytania i dochodzenie roszczeń (art. 6 ust. 1 lit. f RODO),</li>
<li>analiza ruchu na stronie — wyłącznie po wyrażeniu zgody (art. 6 ust. 1 lit. a RODO).</li>
</ul>
<p>Nie sprzedajemy danych i nie wykorzystujemy ich do marketingu bez Twojej zgody.</p>
<h2>4. Okres przechowywania</h2>
<ul><li>dane z zapytań — do 12 miesięcy od ostatniego kontaktu,</li><li>dane związane z realizacją umowy — przez okres wymagany przepisami prawa.</li></ul>
<h2>5. Twoje prawa</h2>
<p>Masz prawo dostępu do swoich danych, ich sprostowania, usunięcia, ograniczenia przetwarzania, przenoszenia, wniesienia sprzeciwu oraz cofnięcia zgody w dowolnym momencie. Przysługuje Ci także prawo wniesienia skargi do Prezesa Urzędu Ochrony Danych Osobowych.</p>
<h2>6. Pliki cookies i Google Analytics</h2>
<p>Po wyrażeniu zgody w banerze cookies strona korzysta z Google Analytics 4 (Google Ireland Ltd.) do anonimowej analizy ruchu — np. liczby odwiedzin i najczęściej oglądanych podstron. Bez zgody narzędzie nie jest ładowane. Swój wybór zapisujemy w pamięci przeglądarki; aby go zmienić, wyczyść dane strony w przeglądarce — baner pojawi się ponownie.</p>
<h2>7. Usługi zewnętrzne</h2>
<p>Formularz kontaktowy korzysta z serwisu Formspree (formspree.io), który przekazuje nam wiadomość e-mailem. Czcionki są przechowywane na naszym serwerze — nie korzystamy z Google Fonts. Strona jest hostowana w serwisie GitHub Pages.</p>
</div></div></section>
</main>
'''
    s += footer()
    write('polityka-prywatnosci.html', s)

# ---------------------------------------------------------------- redirects, 404, sitemap, misc
REDIRECTS = {
  'smart-home.html': 'index.html', 'smart-home-instalacja.html': 'index.html', 'smart-home-koszty.html': 'index.html',
  'knx-loxone-home-assistant.html': 'index.html', 'instalacje-elektryczne.html': 'pomiary-elektryczne.html',
  'blog/smart-home-instalacja.html': '../index.html',
}
def redirects():
    for src, dst in REDIRECTS.items():
        abs_dst = SITE + '/' + dst.replace('../', '').replace('index.html', '')
        write(src, f'''<!DOCTYPE html><html lang="pl"><head><meta charset="UTF-8"><meta name="robots" content="noindex, follow">
<title>Zonik Automation</title><link rel="canonical" href="{abs_dst}"><meta http-equiv="refresh" content="0; url={dst}">
<script>location.replace("{dst}")</script></head><body><p>Strona została przeniesiona: <a href="{dst}">przejdź dalej</a>.</p></body></html>
''')

def notfound():
    s = head('Nie znaleziono strony | Zonik Automation', 'Strona nie istnieje.', '404.html', robots='noindex')
    s = s.replace('href="favicon.svg"', 'href="/favicon.svg"').replace('href="style.css', 'href="/style.css').replace('src="script.js', 'src="/script.js')
    s += header().replace('href="index.html', 'href="/index.html').replace('href="automatyka', 'href="/automatyka').replace('href="programowanie', 'href="/programowanie').replace('href="pomiary', 'href="/pomiary').replace('href="schematy', 'href="/schematy')
    s += f'''<main id="main"><section class="phero" style="min-height:70vh"><div class="wrap">
<p class="tag">Błąd 404</p><h1>Nie znaleźliśmy tej strony</h1><p>Strona mogła zostać przeniesiona. Zobacz nasze usługi lub wróć na stronę główną.</p>
<div class="hero__btns">{B('/', 'Strona główna')}<a class="btn btn--ghost" href="/#kontakt">Kontakt</a></div>
</div></section></main>'''
    f = footer()
    for a in ['index.html', 'automatyka', 'programowanie', 'pomiary', 'schematy', 'polityka', 'poradnik']:
        f = f.replace(f'href="{a}', f'href="/{a}')
    s += f
    write('404.html', s)

def sitemap():
    pages = [('', '1.0'), ('automatyka-przemyslowa.html', '0.9'), ('programowanie-plc.html', '0.9'), ('pomiary-elektryczne.html', '0.9'),
             ('schematy-elektryczne.html', '0.9'), ('poradnik-automatyka-przemyslowa.html', '0.6'), ('polityka-prywatnosci.html', '0.2')]
    x = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    x += ''.join(f'  <url><loc>{SITE}/{p}</loc><lastmod>2026-10-26</lastmod><priority>{pr}</priority></url>\n' for p, pr in pages)
    x += '</urlset>\n'
    write('sitemap.xml', x)
    write('robots.txt', f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')
    write('CNAME', 'zonikautomation.pl')
    write('favicon.svg', '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#e63312"/><text x="32" y="42" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-weight="800" font-size="27" fill="#fff" letter-spacing="-1">ZA</text></svg>\n')

if __name__ == '__main__':
    index(); services(); article(); privacy(); redirects(); notfound(); sitemap()
    print('OK')
