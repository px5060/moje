// MOJE — praca bez internetu. Strona i pliki zawsze najpierw z sieci (nowa wersja od razu), kopia zapisana w telefonie;
// bez internetu — kopia. Bierzemy wszystko z tego samego adresu: MOJE i pule modeli z SZUKAJ / SZUKAJ+ / SZUKAJ LOST
// (wyszukiwarka modeli w MOJE działa offline na pulach z ostatniego otwarcia). Wystarczy raz otworzyć MOJE z internetem.
const C = 'moje-offline-v1';
const NA_START = ['./', './moje.webmanifest', './moje-192.png'];
self.addEventListener('install', e => {
  self.skipWaiting();
  e.waitUntil(caches.open(C).then(c => Promise.all(NA_START.map(u => c.add(new Request(u, { cache: 'no-store' })).catch(() => {})))));
});
self.addEventListener('activate', e => e.waitUntil(self.clients.claim()));
self.addEventListener('fetch', e => {
  const r = e.request; if (r.method !== 'GET') return;
  const u = new URL(r.url); if (u.origin !== location.origin) return;
  const nav = r.mode === 'navigate', klucz = nav ? u.origin + u.pathname : r;
  e.respondWith((async () => {
    const c = await caches.open(C);
    try {
      const res = nav ? await fetch(r.url, { cache: 'no-store' }) : await fetch(r, { cache: 'no-store' });
      if (res.ok) c.put(klucz, res.clone()).catch(() => {});
      return res;
    } catch (err) {
      const m = await c.match(klucz, { ignoreSearch: true });
      if (m) return m;
      throw err;
    }
  })());
});
