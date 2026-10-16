# MOJE — wszystkie moje gry

Aplikacja (PWA) pod `https://px5060.github.io/moje/`. Zbiera w jednym miejscu modele, które grasz, i zapisane zakłady
ze wszystkich aplikacji SZUKAJ, SZUKAJ+ i SZUKAJ BUST (T50 i T60). Czyta wspólną pamięć telefonu (ten sam adres px5060.github.io).

- **TERAZ** — wpis kodów T50/T60 (ostatni kod + kiedy wpisany), grupy: GRAJ TERAZ · ZA 2–3 WIERSZE · BUST · W GRZE · ZAKOŃCZONE.
- **ZAKŁADY** — wszystkie zapisane zakłady i wynik.
- **MODEL** — opis modelu słowami, statystyki na całej tabeli, bank +3 / +5, ostatnie 30 wierszy.
- **BANK** — bank +3 / +5 (bez limitu) dla moich modeli z SZUKAJ, SZUKAJ+ i SZUKAJ LOST: GRAJ BANK na następnym wierszu,
  🎯 bank +3 na k4–k6, stawki do zmiany (domyślnie 8 · 8 · 16 · 32 · 64 · 128 · 256 · 512, dalej ×2), szanse z historii modelu. Zasady: `RULES.md`.

Budowa: `python3 build.py` (z `moje_template.html` + `seed_t50.txt` / `seed_t60.txt`) → `index.html`. Ikony: `python3 make_icons.py`.
Silnik = ten sam co w SZUKAJ+ (SZUKAJ i BUST to SZUKAJ+ z 1 TRIGGEREM i bez STEP2).
