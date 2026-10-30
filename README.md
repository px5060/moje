# MOJE — wszystkie moje gry

Aplikacja (PWA) pod `https://px5060.github.io/moje/`. Zbiera w jednym miejscu modele, które grasz, i zapisane zakłady
ze wszystkich aplikacji SZUKAJ, SZUKAJ+ i SZUKAJ BUST (T50 i T60). Czyta wspólną pamięć telefonu (ten sam adres px5060.github.io).

- **TERAZ** — wpis kodów T50/T60 (ostatni kod + kiedy wpisany), grupy: GRAJ TERAZ · ZA 2–3 WIERSZE · BUST · W GRZE · ZAKOŃCZONE.
- **ZAKŁADY** — wszystkie zapisane zakłady i wynik.
- **MODEL** — opis modelu słowami, statystyki na całej tabeli, bank +3 / +5, ostatnie 30 wierszy.
- **BANK** — bank +3 / +5 (bez limitu) dla modeli dodanych do listy BANK (➕ Dodaj do BANK): GRAJ BANK · ZA CHWILĘ ·
  🎯 bank +3 na k4–k6, stawki 8 · 8 · 16 · 32 · 64 · 128 · 256 · 512 (dalej ×2), szanse na kolejnych krokach z historii modelu,
  🔎 wyszukiwarka dowolnego modelu z SZUKAJ / SZUKAJ+ / SZUKAJ LOST (pule czytane z tych aplikacji). Zasady: `RULES.md`.

- **☁ Kopia w GitHub** (KODY, 1.33.0) — kody i listy z telefonu do pliku `stan.json` w prywatnym repo (np. `px5060/kody`), sama po zmianach (także po poprawce kodu — urządzenie ze starszymi kodami jej nie nadpisze); Claude czyta go w nowej rozmowie, „Przywróć” wczytuje ten stan na innym urządzeniu. Zasady: `RULES.md`.
- **☁ Kilka urządzeń** (1.35.0) — telefon, tablet, komputer z tym samym kluczem: MOJE łączy zmiany (modele, kody, ZESZYT) w obie strony. Zasady: `RULES.md`.
- **🔍 OCENY** (1.36.0) — oceny modeli od Claude (`oceny.json` w tym samym repo): historia, uczciwa szansa, symulacja, nakładanie, werdykt; „＋ Dodaj”. Zasady: `RULES.md`.
- **📥 Od Claude** (TERAZ, 1.34.0) — propozycje modeli od Claude z pliku `od_claude.json` w tym samym repo: „＋ Dodaj” wpisuje model do MOJE, BANK albo ZESZYTU, „Odrzuć” chowa; nic nie dodaje się samo. Zasady: `RULES.md`.

Budowa: `python3 build.py` (z `moje_template.html` + `seed_t50.txt` / `seed_t60.txt`) → `index.html`. Ikony: `python3 make_icons.py`.
Silnik = ten sam co w SZUKAJ+ (SZUKAJ i BUST to SZUKAJ+ z 1 TRIGGEREM i bez STEP2).
