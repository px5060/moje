"""Ikony MOJE: zielone tło, lista z ptaszkami, napis MOJE."""
import pathlib
from PIL import Image, ImageDraw, ImageFont
out = pathlib.Path(__file__).resolve().parent
for size in (192, 512):
    s = size / 512
    im = Image.new('RGB', (size, size), '#1f8a4c'); d = ImageDraw.Draw(im)
    for j, y in enumerate((90, 175, 260)):
        d.rounded_rectangle([90*s, y*s, 150*s, (y+60)*s], radius=int(10*s), fill='#ff6600' if j == 0 else 'white')
        d.rounded_rectangle([180*s, (y+18)*s, 420*s, (y+42)*s], radius=int(10*s), fill='white')
    f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', int(110*s))
    d.text((256*s, 420*s), 'MOJE', font=f, fill='white', anchor='mm')
    im.save(out / f'moje-{size}.png')
print('ikony zapisane')
