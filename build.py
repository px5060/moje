#!/usr/bin/env python3
"""Buduje index.html (appka MOJE) z moje_template.html + seed_t50.txt / seed_t60.txt (MASTER_SEED appek RAZEM, od Nr 1).
Uruchom:  python3 build.py"""
import json, re, pathlib
HERE = pathlib.Path(__file__).resolve().parent
TABS = {
    't50': dict(name='T50', key='t50razem_v1_added', alph=[a + b + c for a in '01' for b in '01' for c in '01'], targets=['x1x']),
    't60': dict(name='T60', key='t60razem_v1_added', alph=[a + b + c for a in '0123' for b in '01' for c in '01'], targets=['x1x', 'xx1']),
}
for t, a in TABS.items():
    a['seed'] = re.sub(r'\D', '', (HERE / f'seed_{t}.txt').read_text())
    import subprocess
    a['seedDate'] = subprocess.run(['git', 'log', '-1', '--format=%cs', '--', f'seed_{t}.txt'], cwd=HERE, capture_output=True, text=True).stdout.strip()
    assert len(a['seed']) % 3 == 0 and all(s in a['alph'] for s in re.findall('...', a['seed'])), t
html = (HERE / 'moje_template.html').read_text().replace('__TABS__', json.dumps(TABS, separators=(',', ':')))
(HERE / 'index.html').write_text(html)
man = {'id': 'moje-v1', 'name': 'MOJE — wszystkie moje gry (SZUKAJ, SZUKAJ+, BUST)', 'short_name': 'MOJE', 'start_url': './', 'scope': './',
       'display': 'standalone', 'orientation': 'portrait', 'background_color': '#12151c', 'theme_color': '#1b1f2a',
       'icons': [{'src': f'moje-{n}.png', 'sizes': f'{n}x{n}', 'type': 'image/png', 'purpose': 'any'} for n in (192, 512)]}
(HERE / 'moje.webmanifest').write_text(json.dumps(man, ensure_ascii=False, indent=1))
(HERE / 'moje-sw.js').write_text(
    "// MOJE: nawigacje zawsze z sieci (bez starej wersji z pamięci)\n"
    "self.addEventListener('install', () => self.skipWaiting());\n"
    "self.addEventListener('activate', e => e.waitUntil(self.clients.claim()));\n"
    "self.addEventListener('fetch', e => {\n"
    "  if (e.request.mode !== 'navigate') return;\n"
    "  e.respondWith(fetch(e.request.url, { cache: 'no-store' }).catch(() => fetch(e.request)));\n"
    "});\n")
print('zapisano index.html', len(html) // 1024, 'KB')
