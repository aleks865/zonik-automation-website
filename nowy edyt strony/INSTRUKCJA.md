# INSTRUKCJA — Jak wgrać pliki i zdjęcia na GitHub
===============================================================

## CZĘŚĆ 1 — JAK DODAĆ WŁASNE ZDJĘCIA

### Nazwy plików do zdjęcia hero (główne zdjęcie na stronie):
Utwórz folder `images/` w repo i dodaj tam plik:

  images/about.jpg          ← zdjęcie w sekcji "O firmie"

Wymiary: minimum 800×600px, najlepiej poziome (landscape).
Format: .jpg lub .webp

### Zdjęcia realizacji (już są, ale możesz dodać więcej):
  images/projekt-001.jpg    ← numeruj kolejno
  images/projekt-002.jpg
  ...itd

### Zdjęcie OG (pojawia się gdy ktoś udostępni link):
  images/og.jpg             ← 1200×630px, wymagane!

### Co fotografować żeby wyglądało dobrze:
- Rozdzielnice elektryczne (z otwartymi drzwiami, widać wnętrze)
- Szafy sterownicze
- Panele dotykowe / sterowanie Smart Home
- Instalacja w trakcie montażu
- Efekt końcowy (zamknięta szafa, oznakowanie)

### Wskazówki do zdjęć telefonem:
- Fotografuj przy dobrym świetle (dzienne > sztuczne)
- Trzymaj telefon poziomo (landscape)
- Wyczyść obiektyw przed zdjęciem
- Zrób kilka ujęć, wybierz najlepsze

===============================================================

## CZĘŚĆ 2 — JAK WGRAĆ PLIKI NA GITHUB (krok po kroku)

### Metoda A — Przez przeglądarkę (łatwiejsza, bez instalowania czegokolwiek)

1. Wejdź na https://github.com/aleks865/zonik-automation-website
2. Zaloguj się na swoje konto GitHub

**Wgrywanie pliku do folderu /blog:**
3. Kliknij na folder `blog` w liście plików
4. Kliknij przycisk `Add file` → `Upload files`
5. Przeciągnij pliki lub kliknij `choose your files`
6. Wybierz wszystkie pobrane pliki bloga:
   - index.html
   - smart-home-instalacja.html
   - automatyka-przemyslowa.html
   - smart-home-koszty.html
   - blog-style.css
   - blog.js
7. Na dole wpisz opis zmiany np. "Nowy wygląd bloga"
8. Kliknij `Commit changes`

**Wgrywanie plików do głównego folderu:**
9. Wróć do głównego folderu repo (kliknij nazwę repo na górze)
10. Kliknij `Add file` → `Upload files`
11. Wgraj:
    - index.html (UWAGA: zastąpi obecny — to jest celowe!)
    - sitemap.xml
    - robots.txt
12. Kliknij `Commit changes`

**Wgrywanie zdjęć:**
13. Kliknij `Add file` → `Upload files`
14. Wgraj swoje zdjęcia do folderu `images/`
    (jeśli folder nie istnieje, GitHub Pages go stworzy)

### Metoda B — Edytowanie pliku bezpośrednio na GitHub
1. Kliknij na plik który chcesz zmienić
2. Kliknij ikonę ołówka (Edit this file) w prawym górnym rogu
3. Wprowadź zmiany
4. Kliknij `Commit changes`

===============================================================

## CZĘŚĆ 3 — CO ZMIENIA TEN PLIK index.html vs poprzedni

Zmiany które wprowadzono:
1. ✅ Schema.org: zmieniono typ z "Electrician" na "LocalBusiness" + "ElectricalContractor"
2. ✅ Schema.org: dodano geo.coordinates (szerokość/długość geograficzna Warszawy)
3. ✅ Schema.org: dodano openingHoursSpecification (godziny pracy)
4. ✅ Schema.org: dodano prawdziwe linki Facebook i Instagram
5. ✅ Meta og:image z wymiarami (width/height)
6. ✅ Dodano og:site_name
7. ✅ Link do sitemap.xml w head
8. ✅ Blog → link zmieniony z "blog/index.html" na "blog/" (poprawny URL)
9. ✅ Dodano sekcję "Śledź nas" w stopce z Facebook i Instagram
10. ✅ Dodano przyciski social w sekcji kontakt
11. ✅ width i height na każdym <img> (poprawia Core Web Vitals)
12. ✅ loading="lazy" na zdjęciach poza hero
13. ✅ aria-label na linkach bez tekstu
14. ✅ <time datetime="..."> na datach bloga (lepsza semantyka)
15. ✅ novalidate na formularzu (żeby nie blokował wysyłki przed backendem)

===============================================================

## CZĘŚĆ 4 — CO JESZCZE MOŻNA POPRAWIĆ W PRZYSZŁOŚCI

Priorytetowe:
- Dodać prawdziwy backend do formularza (np. Formspree.io — darmowe)
- Dodać Google Analytics lub Plausible (darmowa alternatywa)
- Zgłosić sitemap.xml do Google Search Console

Opcjonalne:
- Dodać więcej artykułów na blogu (minimum 1 na miesiąc = lepsze SEO)
- Dodać stronę FAQ z pytaniami klientów
