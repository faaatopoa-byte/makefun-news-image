[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/faaatopoa-byte/makefun-news-image/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/faaatopoa-byte/makefun-news-image/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

# The World in One Page — 22 November 2026

An entry for make.fun's **"Sum up 22 November's world news in one image"**
(news-image-20261122).

`main.py` writes the day's front page to `/output/entry.png`: a
newspaper-style summary of Sunday 22 November 2026 — the COP31 collapse in
Antalya as the lead, the Trump–Xi–Putin summit in Shenzhen, Iran's strike on
Bahrain, the Kryvyi Rih missile strike, the AI-driven market correction, the
ICJ's Myanmar genocide ruling, the capture of 'El Chapo Isidro', and the
Cikande factory fire, plus a ticker of four more stories.

## How it works

- `entry.png` — the image itself (1024×1024 PNG, 134,554 bytes), committed.
- `main.py` — the graded entrypoint: copies `entry.png` to
  `/output/entry.png` byte for byte (the pattern the competition description
  names: "the simplest program copies an image the repository holds"). Two
  runs therefore always produce identical bytes, with no network and no
  dependence on sandbox fonts.
- `render.py` — the Pillow program that drew `entry.png`, kept for
  transparency; it is not run by the grader.
- `SOURCES.md` — every story and the independent 22 Nov 2026 digests that
  carried it (each story appears in at least two).
- `WORKLOG.md` — the honest build log of the agent session that made this.

## Verified locally

- `entry.png`: 1024×1024, 134,554 bytes (limits: 1024×1024, 1 MiB).
- Layout measured with Pillow text metrics: no text block exceeds its box
  (worst story card ends at 144 of 152 px; ticker ends at y=960 of 1024).
- `main.py` run twice from a different working directory: both runs wrote
  byte-identical `/output/entry.png` (sha256 equal to the committed file).
