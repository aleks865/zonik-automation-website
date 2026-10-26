# Notatka o stronie zonikautomation.pl (dla Claude)

Przeczytaj to na początku nowej rozmowy o stronie. Folder z `_` na początku nie jest publikowany przez GitHub Pages.

## Firma
- Zonik Automation Aleks Zonik, NIP 7133147668, tel. +48 511 357 787, kontakt@zonikautomation.pl
- Adres rejestrowy (tylko w polityce prywatności): Jabłonna Druga 147H, 23-114
- Obszar: Warszawa i cała Polska, Pon–Pt 8–18. Formularz: Formspree (mzdylbea). GA4: G-9X9LQVGN8P (po zgodzie cookies).

## Zakres (pisz tylko o tym)
Okablowanie, prefabrykacja szaf sterowniczych i rozdzielnic, projekty i schematy (EPLAN, AutoCAD), pomiary elektryczne (odbiorcze przy instalacjach, okresowe dużych instalacji, budynki wielorodzinne), programowanie PLC/HMI (Siemens S7-1200/1500, TIA Portal, Allen-Bradley).
Branże: uzdatnianie wody, producenci maszyn, przetwórstwo owoców i warzyw, linie produkcyjne, budynki wielorodzinne.

## Zasady od właściciela — WAŻNE
- Nie pisz, czego firma NIE robi (żadnych „nie realizujemy”, „pojedynczych mieszkań nie…”).
- Nie wspominaj o partnerach / podwykonawcach.
- Nie wspominaj o SEP ani uprawnieniach.
- Bez farmacji. Bez lat doświadczenia i bez „100% zadowolonych”. Bez opisu właściciela („o mnie”).
- Bez zbyt szczegółowych, dziwnie konkretnych opisów. Nie zmyślaj opinii klientów.
- Narracja w formie „my” (firma). „130+ zrealizowanych projektów” jest OK.
- Przed większymi zmianami treści pokaż podgląd i zapytaj o zgodę.
- Właściciel lubi czcionki Syne (nagłówki/logo) i DM Sans (tekst) oraz efekty po najechaniu myszką. Wyskakujących zdjęć przy kursorze nie chce.

## Budowa strony
- Statyczna strona na GitHub Pages (repo aleks865/zonik-automation-website, domena w CNAME).
- `_zrodla/build.py` generuje WSZYSTKIE pliki .html (treści, usługi, branże, FAQ, realizacje są na górze pliku jako listy).
  Uruchom z katalogu repo: `python _zrodla/build.py`. Nie edytuj .html ręcznie — zmień build.py i wygeneruj ponownie.
- `style.css` i `script.js` edytuje się ręcznie. Po zmianie podbij wersję `?v=` w build.py (FONTS/head: `style.css?v=4`, `script.js?v=4`).
- Czcionki są lokalnie w `fonts/` (bez Google Fonts).
- Zdjęcia realizacji: `images/realizacje/<nazwa>.jpg` (max ~1800 px) i `<nazwa>-m.jpg` (~800 px), jakość ~80.

## Jak dodać realizację
1. Zmniejsz zdjęcie do dwóch plików jak wyżej (PIL, z obrotem wg EXIF).
2. Dopisz do listy `WORKS` w build.py: `dict(img='nazwa', title='…', tags=['…','…'], desc='…')`.
3. `python _zrodla/build.py`, sprawdź podgląd, zapisz pliki.
Obecne 4 zdjęcia mają ogólne opisy — właściciel ma dostarczyć nowe zdjęcia z opisami.

## Wysyłanie na stronę
Właściciel robi to sam w GitHub Desktop: Commit to main → Push origin. Nie klikać „Discard changes”.
Folder „Claude outputs” jest w .gitignore.
