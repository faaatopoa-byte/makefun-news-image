#!/usr/bin/env python3
"""Render entry.png: the world news of Sunday 22 November 2026 on one page.

Deterministic: fixed layout, fixed fonts, no clock, no randomness, no network.
Run: python3 render.py  -> writes entry.png next to this file.
"""
from PIL import Image, ImageDraw, ImageFont
import os, textwrap

HERE = os.path.dirname(os.path.abspath(__file__))
FD = "/usr/share/fonts/truetype/dejavu"
SERIF_B = os.path.join(FD, "DejaVuSerif-Bold.ttf")
SERIF = os.path.join(FD, "DejaVuSerif.ttf")
SANS = os.path.join(FD, "DejaVuSans.ttf")
SANS_B = os.path.join(FD, "DejaVuSans-Bold.ttf")

W = H = 1024
PAPER = (247, 243, 234)
INK = (20, 20, 20)
GREY = (92, 88, 80)
ACCENT = (166, 20, 44)
CARD = (255, 253, 247)
BORDER = (206, 198, 182)
DARK = (28, 31, 38)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

def font(path, size):
    return ImageFont.truetype(path, size)

def wrap(text, fnt, width):
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if d.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            lines.append(cur); cur = word
    if cur: lines.append(cur)
    return lines

def text_block(x, y, text, fnt, fill, width, leading=1.22):
    for line in wrap(text, fnt, width):
        d.text((x, y), line, font=fnt, fill=fill)
        y += int(fnt.size * leading)
    return y

M = 42            # page margin
CW = W - 2 * M    # content width

# ---------- masthead ----------
d.text((M, 26), "THE WORLD IN ONE PAGE", font=font(SERIF_B, 55), fill=INK)
d.line([(M, 100), (W - M, 100)], fill=INK, width=4)
d.line([(M, 108), (W - M, 108)], fill=INK, width=1)
d.text((M, 118), "Sunday 22 November 2026", font=font(SANS_B, 21), fill=ACCENT)
sub = "The day's world news, summed up in a single image"
d.text((W - M - d.textlength(sub, font=font(SANS, 19)), 120), sub, font=font(SANS, 19), fill=GREY)

# ---------- lead story ----------
y = 148
d.rectangle([M, y, W - M, y + 160], fill=(238, 231, 216), outline=BORDER, width=1)
d.text((M + 20, y + 14), "CLIMATE  ·  ANTALYA, TÜRKIYE", font=font(SANS_B, 19), fill=ACCENT)
y2 = text_block(M + 20, y + 44, "COP31 climate talks collapse with no deal",
                font(SERIF_B, 37), INK, CW - 40, 1.15)
text_block(M + 20, y2 + 8,
           "The UN summit ran two days past its deadline and ended empty-handed after the EU "
           "rejected a final text that never mentioned fossil fuels.",
           font(SANS, 20), (52, 50, 46), CW - 40, 1.25)

# ---------- story grid: 2 columns x 3 rows ----------
stories = [
    ("DIPLOMACY · SHENZHEN", "Trump, Xi and Putin meet face to face",
     "The first US-China-Russia summit issued a joint call on nuclear risks - but no arms limits and no Ukraine breakthrough."),
    ("GULF · BAHRAIN", "Iran strikes US bases in Bahrain",
     "Missiles and drones hit a civilian industrial site, injuring two people. Tankers were also struck near the Strait of Hormuz."),
    ("UKRAINE · KRYVYI RIH", "Strike kills a child in Zelenskyy's hometown",
     "A Russian missile killed a boy of 7 and a woman of 20, wounding about 60; a drone-hit block near Kyiv left 14 missing."),
    ("MARKETS · NEW YORK", "AI sell-off tips stocks into correction",
     "The S&P 500 fell 3.7% and the Nasdaq 5.3% on Friday as the tech rout spread to bourses in Japan and South Korea."),
    ("JUSTICE · THE HAGUE", "World Court: Myanmar committed genocide",
     "The ICJ found Myanmar responsible for the 2017 genocide of the Rohingya - the first such ruling against a state."),
    ("MEXICO · SINALOA", "Cartel boss 'El Chapo Isidro' captured",
     "Special forces seized the FBI most-wanted trafficker in a raid that killed 11 people, four of them soldiers."),
]
gx, gy = M, 322
gap = 12
cw = (CW - gap) // 2
ch = 152
for i, (kick, head, deck) in enumerate(stories):
    x = gx + (i % 2) * (cw + gap)
    yy = gy + (i // 2) * (ch + gap)
    d.rectangle([x, yy, x + cw, yy + ch], fill=CARD, outline=BORDER, width=1)
    d.text((x + 16, yy + 12), kick, font=font(SANS_B, 16), fill=ACCENT)
    y3 = text_block(x + 16, yy + 36, head, font(SERIF_B, 22), INK, cw - 32, 1.14)
    text_block(x + 16, y3 + 5, deck, font(SANS, 15), (52, 50, 46), cw - 32, 1.18)

# ---------- disaster strip ----------
sy = gy + 3 * ch + 2 * gap + 16
d.rectangle([M, sy, W - M, sy + 72], fill=DARK)
d.text((M + 20, sy + 12), "DISASTER · CIKANDE, INDONESIA", font=font(SANS_B, 17), fill=(240, 180, 90))
d.text((M + 20, sy + 38), "Candy factory fire: 3 workers dead, dozens missing in the ruins",
       font=font(SERIF_B, 22), fill=(245, 243, 238))

# ---------- ticker ----------
ty = sy + 86
d.line([(M, ty), (W - M, ty)], fill=INK, width=2)
ticker = ("ALSO TODAY:  M6.7 earthquake in Peru's Andes  ·  Strikes kill 7 in Gaza despite the ceasefire  ·  "
          "BepiColombo reaches Mercury after 8 years  ·  EU and Indonesia sign a landmark trade deal")
text_block(M, ty + 12, ticker, font(SANS_B, 17), INK, CW, 1.3)

# ---------- footer ----------
foot = "Stories as reported on 22 Nov 2026 by Reuters, AP, AFP, Al Jazeera and BBC digests · One image, one day"
d.text((M, H - 34), foot, font=font(SANS, 14), fill=GREY)

img.save(os.path.join(HERE, "entry.png"), optimize=True)
print("wrote entry.png", img.size)
