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

- **Lista BANK** jest osobna od MOJE: tylko modele dodane przyciskiem **➕ Dodaj do BANK** (w banku modelu — w wyszukiwarce i na ekranie modelu z MOJE); zapis `moje_v1_bank` ({t, a, tg, m, id, t0}). Ten sam przycisk usuwa (✓ Jest na liście BANK — usuń). Modele z RAZEM — nie (ich cykle liczy RAZEM).
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
