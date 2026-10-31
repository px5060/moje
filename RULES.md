# RULES — rodzina aplikacji SZUKAJ (stan ustaleń)

Ten plik jest wspólny dla repo: `szukaj50`, `szukaj60`, `szukaj50plus`, `szukaj60plus`, `szukajbust50`, `szukajbust60`.
Zapisuje reguły i ustalenia z rozmów, żeby przetrwały streszczenie (kompakcję) kontekstu i nowe sesje.

## Sposób pracy

- **Na ekranie zamiast „BUST” piszemy „LOST”** (BUST-y → LOST-y, busty → losty) we wszystkich SZUKAJ, MOJE i RAZEM 50/60 — tylko napisy (funkcja `LOSTIFY`), dane / zapisy / obliczenia bez zmian. Wyjątek: tabela i modele „BUST” w RAZEM T60 (BUST 012, BUST ODM, np. B0A). Nazwa appki SZUKAJ BUST, adres i ikona bez zmian.

- Rozmowa po polsku, prosto, bez żargonu. Symbole z `x` (np. `x1x`, `00x`) zostają — użytkownik je rozumie.
- **PR scalany dopiero po słowie „scal”** od użytkownika. Nigdy samodzielnie.
- Gałąź robocza: `ccr-70037d68-ntwxyk` (po scaleniu: odtworzyć od `origin/main`).
- Edytuje się `szukaj/szukaj_template.html`, potem build: `cd szukaj && python3 build_szukaj.py t50|t60` → `../index.html`.
  Para 50/60 ma identyczny szablon — zmiana w jednym = skopiować do drugiego (BUST i SZUKAJ+ mają własne szablony).
- Przy każdej zmianie podbić `APP_VER` (nagłówek pokazuje wersję; appka sama proponuje odświeżenie).
- Zmiana „dla wszystkich SZUKAJ” = SZUKAJ 50/60 + SZUKAJ+ 50/60 (+ BUST 50/60, jeśli funkcja tam istnieje).
- Test przed PR: Playwright z Chromium (`/opt/pw-browsers/chromium`), sprawdzić brak błędów JS i wynik na danych.
- Adresy: `https://px5060.github.io/<repo>/`. Kody wspólne z RAZEM (`t50razem_v1_added` / `t60razem_v1_added`).
- **T60 RAZEM: przełącznik „BET xx1 ⇄ / x1x”** — na xx1 widać PIKOFF, BUST, TRÓJKA, MIX3, SZUKAJ (tylko modele BET xx1); na x1x tylko TOP5 i TOP7.
- RAZEM: T50 = repo `all50` (src + build.py → `index.html`, `pages/t50razem/` kopiowane do repo `t50razem`), T60 = repo `all60` (sam `index.html`, appki jako JSON w `APPS = […]`).

## Model i gra

- Model: STEP (SERIA ×x albo UKŁAD p→q) → TRIGGER → zakład na wierszu TRIGGER + offset. SZUKAJ+: dodatkowo STEP2 i TRIGGER ×2/×3.
- Cel: T50 `x1x`; T60 `x1x` lub `xx1`. Kurs 3,0. WIN = +2 × stawka.
- Progresja K8 trwała: 8 · 8 · 16 · 32 · 64 · 128 · 256 · 512 zł. WIN → krok 1. **BUST = przegrany krok 8 (512 zł bez trafienia)** → krok 1.
- **Cykl** = gra modelu do WIN albo BUST (to NIE są wiersze; jeden cykl trwa różną liczbę wierszy).
- Kryteria (domyślne): do 200 cykli max 5 BUST, do 300 max 9, do 400 max 11, ponad 400 max 11, min. 100 cykli.
- Pula modeli liczona w chmurze (`search.py`); w telefonie każdy kod przelicza całą pulę. Szukanie w telefonie wyłączone.

## Ekran GRA (SZUKAJ / SZUKAJ+)

- „krok:” — **k1 8 zł, k2 8 zł, 16 … 512 zł** (k1…k8); domyślnie 64/128/256. Pokazuje modele po TRIGGERZE na wybranych krokach.
- „cykle:” — przedziały 100–200 · 201–300 · 301–400 · ★ 401+ oraz **BUST**.
- **BUST** (lista) — tylko modele, których **ostatni zakończony cykl to BUST i od BUST-u nie było WIN** (po WIN model znika).
  Filtrowana po krokach jak przedziały (zaraz po BUST-cie model jest na k1).
  - „poprz. BUST: **≤ 20 cykli**” / „**21–40 cykli**” — odstęp **w cyklach** od poprzedniego BUST-u modelu (model z jednym BUST-em nie wchodzi).
  - „**po BUST**” — model w cyklu zaraz po BUST-cie, GRA na następnym wierszu albo zakład za 2–3 wiersze.
  - Model z zakładem (na kroku) ma pod wierszem BUST-u kartę jak pozostałe (pomarańczowa przy GRA na następnym).
- Biało-czerwona ramka karty = model w cyklu zaraz po BUST-cie (`sinceB === 0`).
- Znaczki jak w RAZEM: **pomarańczowy** = ile modeli gra na następnym wierszu, **żółty** = GRA za 2–3 wiersze
  (przycisk BUST, „moje · busty”, dolny przycisk MOJE).

## MOJE

- **MOJE tylko w aplikacji MOJE**: w SZUKAJ, SZUKAJ+, SZUKAJ LOST i RAZEM 50/60 nie ma już zakładek MOJE / MOJE GRY / MOJE ZAKŁADY / „w grze” / „losty”. Zostaje tylko przycisk dodania modelu do MOJE (okno statystyk). Dane (listy, zakłady) bez zmian — czyta je aplikacja MOJE.

- „▶ moje” na GRA: podzakładki **gry** · **busty** · **w grze** (w BUST: „▶ MOJE”: gry · w grze).
- **gry** — modele dodane „▶ Gram ten model”, śledzone do WIN albo kroku 8.
- **busty** — BUST-y moich modeli od dodania; **zostają po usunięciu modelu z MOJE** (✕ usuwa wpis); znikają po WIN modelu.
- **w grze** — zapisane zakłady (MOJE ZAKŁADY): postawione i czekające na wynik + przegrane, gdy progresja modelu trwa.
- Dolny przycisk MOJE: żółty = za ile wierszy GRA w moich modelach, pomarańczowy = ile gra na następnym; świeci, gdy jest zakład.

## TABELA i inne

- TABELA chronologicznie; dotknięcie wiersza → łańcuch STEP/TRIGGER, ponowne → zamyka; przytrzymanie → STATYSTYKI.
- Dotknięcie wiersza WIN/przegrana → okienko z wynikami wszystkich modeli na tym wierszu.
- Po wpisaniu kodu na wierszu gry: okienko WIN/PRZEGRANA, przejście do tabeli i rozbłysk wiersza.
- Statystyki: pasek „Ostatnie N cykli” to cykle (W krok / BUST), nie wiersze.
- RAZEM: okno „Statystyki modelu” musi mieć białą czcionkę w każdej tabeli (TRÓJKA, 2-SLOT, MIX3 miały czarną — poprawione);
  T60 MIX3 → STATY w układzie TRÓJKI (T50Stat).

## Aplikacja MOJE (repo `moje`, adres `/moje/`)

- Na pasku aplikacji przycisk **📓 ZESZYT** (`/zeszyt/`, repo `zeszyt`) — karty z papierowego zeszytu TRÓJKA.

- Zbiera MOJE (modele, które gram) i MOJE ZAKŁADY ze wszystkich SZUKAJ / SZUKAJ+ / BUST, T50 i T60 — czyta wspólną pamięć telefonu, nic nie kopiuje.
- Przycisk w oknie statystyk SZUKAJ / SZUKAJ+ „⇢ Gram — dodaj do MOJE i otwórz” zastąpił dawne „Dodaj do RAZEM — zakładka SZUKAJ”.
- Poza tym przyciskiem aplikacji źródłowych **nie zmieniamy** pod MOJE.
- W aplikacji MOJE są też modele z MOJE GRY w RAZEM 50/60 (stan liczy RAZEM w ukrytej ramce).
- Wpis kodów w MOJE: przy każdej tabeli ostatni kod i kiedy wpisany („5 minut temu”, „2 dni temu”).

## Kolejność stanów w MOJE (aplikacja MOJE)

- Grupy 🟧 GRAJ TERAZ, 🟨 ZA CHWILĘ, 🟦 CZEKAJĄ (i ✅ ZAKOŃCZONE, ⏸ CZEKAJĄ NA BANK) na TERAZ, LOST i BANK można zwijać i rozwijać (dotknięcie nagłówka). Stan każdej grupy jest zapamiętany (`moje_v1_fold`) i zostaje po wpisaniu kodu / odświeżeniu. Domyślnie: GRAJ TERAZ i ZA CHWILĘ rozwinięte, CZEKAJĄ na TERAZ zwinięte.

- Model po dodaniu: 🟦 CZEKAJĄ (na STEP / TRIGGER) → 🟨 ZA CHWILĘ (TRIGGER był) → 🟧 GRAJ TERAZ (zakład na następnym wierszu).
- Przegrany krok (np. k2 nie wszedł) → model wraca do CZEKAJĄ → ZA CHWILĘ → GRAJ TERAZ na kolejnym kroku (do k8).
- **WIN → ✅ ZAKOŃCZONE** (koniec gry modelu).
- **BUST (przegrany k8) → ✅ ZAKOŃCZONE (✖ BUST k8) i jednocześnie zakładka BUST** (biało-czerwona ramka), dopóki po BUST-cie nie ma WIN. W zakładce BUST model gra normalnie dalej na kolejnych krokach: 🟦 CZEKAJĄ → 🟨 ZA CHWILĘ → 🟧 GRAJ TERAZ (ten sam układ co TERAZ).
- Zakładka BUST ma dwie części: **💥 MOJE MODELE** (BUST-y modeli z SZUKAJ, SZUKAJ+, RAZEM) i **🅱 SZUKAJ BUST** (BUST-y modeli z aplikacji SZUKAJ BUST) — oddzielnie.

## Zakładka BANK (aplikacja MOJE) — bank +3 / +5

- **TERAZ albo BANK — nigdy oba.** Model jest albo na TERAZ / LOST (prosta progresja k1–k8, MOJE GRY aplikacji źródłowej), albo w BANK (`moje_v1_bank`). Model z listy BANK nie jest pokazywany na TERAZ / LOST (zapis w MOJE zostaje). Przełącznik przy modelu (ekran modelu z MOJE, ekran banku modelu, wyszukiwarka): **🏦 Przenieś do BANK** / **🟧 Przenieś do TERAZ** (model z wyszukiwarki → MOJE GRY aplikacji źródłowej, start = bieżący wiersz). „✕ usuń z BANK” usuwa całkiem (z BANK i z MOJE). Tryb gry TERAZ / BANK / OBA (1.18.0) wycofany.
- Na TERAZ grupy **🟥 PO BUST (LOST)** i **🏦 BANK +3** — zwijane jak pozostałe (domyślnie rozwinięte, stan zapamiętany); w środku tylko modele, które grają **na następnym wierszu** (LOST w wyglądzie jak na zakładce LOST, BANK jak na liście BANK); znaczki żółty / pomarańczowy w nagłówku. **Krótkie dotknięcie** nagłówka zwija / rozwija, **przytrzymanie** (~0,5 s) przenosi do zakładki LOST / BANK.
- Biorę po kolei wszystkie cykle modelu na całej tabeli (od Nr 1). **W** = krok, na którym model wygrał; LOST modelu = brak WIN w każdym oknie.
- **Bank +3** gra w każdym cyklu tylko pierwsze 3 zakłady modelu, **bank +5** — pierwsze 5.
- Model trafi w tych zakładach → **WIN banku na kroku = przeniesione kroki + W**, bank wraca na k1.
- Model nie trafi → bank przegrywa swoje 3 (5) kroki i **czeka** (dalszych zakładów modelu w tym cyklu nie gramy); w następnym cyklu gra dalej (+3 / +5). Przeniesienia się sumują.
- **Bez limitu** (ustalone: interesuje nas gra do k4–k6). Przykłady: W7, W1 → +3: WIN k4, +5: WIN k6 · W5, W3 → +3: W6 · W4, W5, W2 → +3: W8 · W6, W7, W1 → +3: W7, +5: W11.
- Stawki banku stałe: **8 · 8 · 16 · 32 · 64 · 128 · 256 · 512** (jak progresja modelu), bez limitu dalej ×2 (k9 1024, k10 2048 …). Ramki zmiany stawek już nie ma. WIN zakładu = +2 × stawka; „seria” = wynik od k1 banku z przegranymi krokami.
- Szanse: z historii modelu; w bieżącym cyklu tylko cykle, w których model też przegrał już tyle zakładów (np. +5 po 3 przegranych: W4–W5 wśród cykli z W ≥ 4). „Do k…” = to okno albo następne.
- Wyników banku po kolei (kafelki W / L) nie pokazujemy — zostają okna z szansami i „Gdzie bank się zamykał” w %.
- Tabela szans: tylko okna, nie każdy krok — od obecnego okna banku: bank +3 3 okna (np. k4–6 · k7–9 · k10–12), bank +5 2 okna (np. k1–5 · k6–10); przy oknie stawki (od–do), szansa zamknięcia w tym oknie i łącznie, który to cykl modelu (ten / następny / za 2 cykle). „Gdzie bank się zamykał” = % WIN-ów banku w oknach k1–3 · k4–6 · k7–9 … (dla +5: k1–5 · k6–10 …). Przy szansie w nawiasie, jasnoniebieskim, **(od k1)** = od początku gry: % serii banku zamkniętych na krokach k1 do końca tego okna (suma okien, np. k1–6 = k1–3 + k4–6).
- **🔎 Wyszukiwarka** (na górze BANK): nazwa modelu z SZUKAJ / SZUKAJ+ / SZUKAJ LOST (np. P1037; „S+…”, „L…”, „S…” zawęża aplikację) → statystyki modelu, ostatnie cykle i bank +3 / +5. Pule wczytywane na żądanie z aplikacji (ten sam adres, `const POOLS`), więc nazwy zgadzają się z bieżącą wersją SZUKAJ.
- Lista jak na TERAZ (zwarte wiersze: model, krok i stawka banku), osobno dla **BANK +3 / BANK +5** (przełącznik, `moje_v1_bkw`). Stany wybranego banku: 🟦 **CZEKAJĄ** (okno trwa, model czeka na STEP / TRIGGER; podgrupy wg kroku banku) → 🟨 **ZA CHWILĘ** (zakład banku za 2+ wiersze) → 🟧 **GRAJ TERAZ** (zakład banku na następnym wierszu, „razem … zł”). WIN → bank od k1 → CZEKAJĄ. Okno przegrane w tym cyklu → **⏸ CZEKAJĄ NA BANK** (model gra dalej bez banku), aż model skończy cykl (WIN albo LOST) → znowu CZEKAJĄ na kolejnym oknie. Znaczki jak na TERAZ (żółty = za ile wierszy, pomarańczowy = ile na następnym) przy BANK, T50 / T60 i +3 / +5. Dotknięcie wiersza → ekran banku modelu.
- Model po LOST-cie (ostatni zakończony cykl to LOST, od niego bez WIN — `sinceB === 0`) ma w BANK **biało-czerwoną ramkę** jak na LOST (wiersz listy i ekran banku modelu) oraz dopisek „po LOST (Nr …)”.

## Praca bez internetu (od 1.30.2)
- Prośba użytkownika: MOJE działa offline. `moje-sw.js` (generowany przez build.py): każde pobranie z tego samego adresu — strona MOJE
  i pule modeli z SZUKAJ / SZUKAJ+ / SZUKAJ LOST — najpierw z sieci (zawsze najnowsza wersja), kopia w pamięci `moje-offline-v1`;
  bez sieci — kopia. Wystarczy raz otworzyć MOJE z internetem. Kody i tak są w pamięci telefonu, więc wpisywanie offline działa.
- Po starcie zielony komunikat na 3,5 s: „✓ Pobrane — działa też bez internetu”, a bez sieci „📴 Bez internetu — działa z pamięci telefonu”.

## Ekran modelu: 📊 Statystyki ⇄ 📓 Zeszyt (1.31.0)
- Pod „Jak gra ten model” dwa przyciski: Statystyki (statystyki + ostatnie 20 wierszy) albo Zeszyt — bieżąca gra na kartach ZESZYTU (ramka `/zeszyt/…?znacz=`), z nazwami meczów. Jak w S+50 / S+60.
- Tylko modele z SZUKAJ / SZUKAJ+ / LOST (nie karty RAZEM). W trybie zeszytu bez odświeżania co 30 s (ramka by się przeładowywała).
- Modele RAZEM (R50 / R60) też mają przełącznik (1.32.0): łańcuch zakładu z RAZEM (`UT.znacz(mi)` w ramce tabeli) → ZESZYT `?znacz=`.

## ☁ Kopia w GitHub — dla Claude i drugiego urządzenia (1.33.0)
- Prośba użytkownika: Claude ma widzieć dopisywane kody i modele z telefonu bez ręcznych eksportów. KODY → „☁ Kopia w GitHub”:
  repo (domyślnie `px5060/kody`, **prywatne**) + klucz *fine-grained* tylko do tego repo (Contents: Read and write). Klucz tylko w telefonie
  (`moje_v1_gh`), nigdy nie jest wysyłany.
- Plik `stan.json`: `t50` / `t60` = `{n, kody}` (pełny ciąg od Nr 1, 3 cyfry na kod), `modele` (lista MOJE: tabela, app, cel, nazwa, id, model `m`,
  krok, faza, Nr zakładu, bank, lost), `storage` = kopia pamięci px5060.github.io (MOJE GRY, BANK, ZAKŁADY, RAZEM, ZESZYT…) bez klucza GitHub
  i bez ustawień ekranu; od 1.33.1 też bez `oc_v1/…` (zapamiętane oceny GRAĆ / OBSERWUJ w SZUKAJ — appka je przelicza; ok. 1/4
  pliku mniej danych przy każdej wysyłce). Wysyłka sama: po zmianach (15 s po ostatniej, przy każdym `reload`) i przy otwarciu, tylko gdy stan się zmienił (skrót).
  Przy wyjściu z MOJE (`visibilitychange` → ukryta, `pagehide`) czekająca wysyłka idzie od razu.
- **Poprawki kodów** (prośba użytkownika: poprawiony kod ma trafić do repo): cofnięty i wpisany na nowo kod (MOJE ↶, RAZEM ⟲), zmiana kodu
  w ZESZYCIE (dopisany kod — wspólna lista; kod z bazy — `zeszyt_v1_poprawki_<t>`) zmieniają stan → wysyłka jak wyżej. Każde urządzenie pamięta
  **bazę** (`moje_v1_gh.base`: n, skrót ciągu, ostatnie 600 kodów, poprawki ZESZYTU — to, co ostatnio wysłało albo wczytało) i względem niej
  opisuje zmiany: `stan.json → zmiany` (ta wysyłka), dziennik `moje_v1_kodzm` (ostatnie 100, jedzie w `storage`), opis zapisu w GitHub
  („poprawka T50 Nr …: 001→010”) i dymek „☁ Poprawka kodu wysłana”. KODY pokazują 3 ostatnie poprawki.
- Konflikt (plik w GitHub zapisało inne urządzenie, 409/422): nadpisuję tylko, gdy ostatni zapis jest z tego urządzenia (`urzadzenie.id`,
  `moje_v1_ghid` — nie jedzie w `storage`) albo kody w GitHub = baza (zmiany są tylko tutaj). Inaczej, gdy w GitHub są kody, których tu nie
  ma (więcej kodów, inny kod w tym samym Nr, inne poprawki ZESZYTU) — auto: nie nadpisuje (błąd w KODY), ręcznie: pyta z listą różnic.
  Urządzenie ze starszymi kodami nie skasuje więc poprawki z telefonu. „⬇ Przywróć z GitHub” wczytuje stan na tym urządzeniu (np. komputer),
  ustawia bazę i sha, a przed podmianą pokazuje, co zniknie (więcej kodów albo inne kody tutaj). „✕ Usuń klucz” zatrzymuje wysyłkę.
- Claude czyta `stan.json` w projekcie `all50/analiza` (narzędzia przyjmują `--stan`).

## ☁ Kilka urządzeń — łączenie zmian (1.35.0)
- Prośba użytkownika: telefon, tablet i komputer mają mieć te same modele (MOJE, ZESZYT…) i kody — dodane gdziekolwiek trafiają na resztę.
  Na każdym urządzeniu MOJE z tym samym repo i kluczem; nic nie trzeba instalować (appki z px5060.github.io w przeglądarce).
- Synchronizacja (`ghSend`): najpierw mały zapytanie o ostatni commit `stan.json` (`/commits?path=…&per_page=1`); ten sam co po ostatniej
  synchronizacji → bez pobierania. Inny (zapisało inne urządzenie, albo pierwsza synchronizacja tutaj) → pobierz i połącz trójstronnie:
  baza `moje_v1_ghbase` (storage po ostatniej synchronizacji, nie jedzie w stan.json) / tutaj / GitHub. Listy (tablice obiektów: MOJE GRY,
  BANK, ZAKŁADY, ZESZYT, rodziny, RAZEM…) element po elemencie — dodane tu i tam zostają, usunięte po jednej stronie znikają; obiekty
  (decyzje 📥, poprawki ZESZYTU) klucz po kluczu; kody: dłuższy ciąg, gdy drugi jest jego początkiem, poprawka po jednej stronie wygrywa,
  różne kody po obu stronach = konflikt (auto nie wysyła, ręcznie pyta — jak dotąd); inne wartości: zmiana z jednej strony wygrywa.
  Potem wysyłka połączonego stanu z sha z GitHub; 409 (ktoś zapisał w międzyczasie) → raz od nowa. Dymek „☁ Z Android: T50 +2 kodów …”.
- Kiedy: po zmianach (15 s), przy otwarciu i powrocie do MOJE (2–3 s), co 3 min, gdy MOJE jest na ekranie. Nowe urządzenie: repo + klucz →
  „Zapisz i wyślij” pobiera wszystko (baza pusta = suma list). „Przywróć” zostaje jako ręczne zastąpienie bez łączenia.

## 🔍 OCENY — propozycje i oceny od Claude (1.36.0, zastępuje 📥 Od Claude z 1.34.0)
- Prośba użytkownika: Claude ocenia modele bardziej zaawansowanie i każda ocena trafia do MOJE z decyzją użytkownika. Dwa rodzaje:
  - **propozycja Claude** (`rodzaj: propozycja`): Claude wybiera modele z pul SZUKAJ / S+ / LOST i z ZESZYTU wg kryteriów, każdy kandydat
    przechodzi pełną ocenę, do telefonu idą najlepsi → **＋ Dodaj do MOJE / ZESZYTU** (zapis jak „Gram — dodaj do MOJE” / „Przenieś do
    zeszytu”, `inDodajP`) albo **Usuń analizę**;
  - **ocena Twojego modelu** (`rodzaj: moj`): użytkownik sam dodał model do MOJE / ZESZYTU i poprosił o ocenę → **Zostaw w MOJE** albo
    **Usuń z MOJE** (z listy MOJE GRY appki i z BANK albo z ZESZYTU, po potwierdzeniu, `ocUsun`).
- Plik `oceny.json` w tym samym repo (pisze `all50/analiza/narzedzia/ocena.py`); MOJE pobiera go przy otwarciu (co najmniej 2 min przerwy)
  i przyciskiem „🔍 Sprawdź propozycje i oceny od Claude” w KODY. Ocena: `{id, rodzaj, nazwa, gdzie, tabela, …model…, data, kody_do, krok,
  stawka, zaklad, werdykt (GRAĆ / OBSERWUJ / NIE GRAĆ), krotko, sekcje: [{tytul, wiersze}], liczby}`; zła ocena → komunikat i „Usuń analizę”.
- Zakładka **OCENY**: „📥 Propozycje Claude”, „🔍 Oceny Twoich modeli”, na dole „Załatwione”. Karta: werdykt (kolor), kiedy i na jakich kodach,
  krok „teraz” liczony przez MOJE (SZUKAJ), jedna linia, „Cała ocena” (stan, historia do k8 / limitu i w 3 krokach, uczciwa szansa,
  symulacja, nakładanie, czym się kierował), decyzja. TERAZ: pasek „📥 Od Claude: … czeka na decyzję — OCENY ›”; na przycisku OCENY liczba
  czekających.
- Decyzje `moje_v1_ocdec` `{id|data: {d: 'dodane' | 'usunieta' | 'zostaw' | 'usuniety', t}}` jadą w stan.json (łączone między urządzeniami,
  Claude je widzi); pobrany plik (`moje_v1_ghoc`) nie jedzie. Nowa ocena tego samego modelu (inna data) znowu czeka na decyzję. Nic nie
  dodaje się ani nie usuwa samo; zakładów Claude nie ustawia. Dolny pasek: 7 przycisków, szerokość wg napisu (12 px) — mieści się na 360 px.

## 🔍 OCENY: sposób gry — prosta progresja czy BANK (1.38.0)
- Prośba użytkownika: po ocenie modelu sugestia, czy lepiej grać go bankiem, czy prostą progresją, i wybór, gdzie zapisać: MOJE (TERAZ),
  LOST (tylko model po LOST — od LOST-u bez WIN) albo BANK.
- ocena.py (modele SZUKAJ / S+ / LOST) liczy sekcję „Sposób gry” jak MOJE: prosta progresja (krok, do k8, skala 9 pkt) i BANK +3 / +5
  (`bankOf`: krok banku teraz z przeniesionymi krokami, okno, szansa w oknie i w 2 oknach, ile serii wygranych w 1. oknie, najdłuższa seria,
  serie > k9 / k10, skala 9 pkt banku). Sugestia BANK +w **tylko przy lepszych szansach banku jako modelu** (prośba użytkownika): w całej historii
  seria banku kończy się WIN do k8 częściej niż cykl prostej progresji o ≥ 2 pp (≥ 30 serii), skala banku ≥ 7 i nie niższa niż prostej, krok banku
  teraz ≤ k5; inaczej prosta progresja (TERAZ, a model po LOST — LOST). Zwykle bank przekracza k8 częściej (i gra dalej: 1024, 2048 zł). W ocenie pole `gra: {zalecana: TERAZ | LOST | BANK, bank: 3 | 5, po_lost, tx}`.
- Karta OCENY: ramka „▶ Sugestia: …” (i gdzie model jest teraz). Propozycja: **＋ Do MOJE (TERAZ)** albo **＋ Do LOST** (model po LOST —
  liczone w telefonie, `r.sinceB === 0`; trafia do MOJE GRY i sam jest w zakładce LOST) i **＋ Do BANK** (`moje_v1_bank`; którym bankiem
  prowadzić listę — przełącznik +3 / +5 w BANK); sugestia podświetlona. Twój model (1.38.1, prośba użytkownika — jak przy propozycji):
  na TERAZ / LOST — **✓ Zostaw w MOJE (TERAZ)** (albo w LOST) i **🏦 Do BANK**; w BANK — **🟧 Do MOJE (TERAZ)** (albo LOST) i **✓ Zostaw w BANK**;
  podświetlona ta zgodna z sugestią; obok ✕ Usuń z MOJE. Przeniesienie — `moveTo`. Decyzje: `dodane_bank`, `do_banku`, `do_teraz`.
- ZESZYT bez zmian (bank jest tylko dla modeli SZUKAJ). Stara ocena bez `gra` — jak dotąd (jeden przycisk „＋ Dodaj do MOJE”).

## 🔍 OCENY bez powielania (1.37.0) — prośba użytkownika: „żeby nam się te oceny nie powielały”
- **Jedna ocena na model**: stałe id (`app|tabela|cel|P{nr}`, ZESZYT `Z|t50|…` / `Z|t60|…` jak `zid` w ocena.py); ocena.py `nowe` ocenia tylko
  modele z telefonu bez oceny, ponowna ocena tylko na prośbę.
- **Decyzje tylko w MOJE → OCENY.** ZESZYT (1.26.0) pokazuje przy modelu werdykt i „Całą ocenę” tylko do odczytu (czyta `moje_v1_ghoc`).
- **Zamykanie samo** (`ocStan`, bez zapisu w `moje_v1_ocdec`): ocena Twojego modelu, którego już nie ma w MOJE GRY / BANK / ZESZYCIE
  (usunięty poza OCENAMI) → Załatwione „nie ma go już”; propozycja, której model dodano samodzielnie → Załatwione „＋ dodany — poza OCENAMI”.
  Model wraca → ocena znowu czeka. Liczy się bez symulacji (porównanie modelu), pamięć `_ocC` czyszczona przy reload / zmianie ocen / decyzji.
- **Znaczek 🔍 GRAĆ / OBSERWUJ / NIE GRAĆ** przy karcie modelu (TERAZ / ZAKŁADY / LOST, BANK, lista BANK) — najnowsza ocena tego modelu (`clTag`).
- „＋ Dodaj do ZESZYTU” zaznacza nowy model na karcie i otwiera listę „Modele” (jak „Przenieś do zeszytu”); „Usuń z MOJE” (ZESZYT) usuwa go też
  z zaznaczonych.
- Sprzątanie `oceny.json` na starcie sesji: `ocena.py wyczysc` (decyzje starsze niż 14 dni i oceny Twoich modeli, których nie ma już w telefonie).
