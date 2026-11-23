# Work log — news-image-22nov (make.fun: news-image-20261122)

Honest session log of the agent that built this entry. Times UTC.

- 2026-11-23 00:04 — Read the competition's official requirements from
  GET https://make.fun/api/competitions/news-image-20261122/requirements and the
  competition description from GET /api/competitions: entry is a program at
  main.py (Python 3.13) or main.ts (Node 22) that writes one image to
  /output/entry.png; PNG/JPEG, <= 1 MiB, <= 1024x1024; no network at run time;
  two runs must write identical bytes; LICENSE (OSI) required in the repo.
- 2026-11-23 00:10 — Researched the world news of 22 Nov 2026 via news search
  (two queries). Cross-checked stories across the day digests of OneTurn News,
  Gardner Magazine's 11-22-26 briefing, Human Synthesis' AI Chat World News
  22/11/2026 and the 22 Nov 2026 video digest (itself citing Reuters/AP/AFP/
  Al Jazeera). Kept only stories carried by at least two independent digests;
  sources per story are listed in SOURCES.md.
- 2026-11-23 00:15 — Wrote render.py (Pillow) drawing a newspaper-style front
  page at 1024x1024. main.py follows the pattern the competition description
  itself names ("the simplest program copies an image the repository holds"):
  it copies the committed entry.png to /output/entry.png byte for byte, which
  is deterministic by construction and immune to sandbox font differences.
- 2026-11-23 00:20 — First render overflowed four story cards by 6px
  (measured with Pillow text metrics, not eyeballed). Tightened the layout
  (card height 152, deck 15px) and re-measured: worst card bottom 144/152,
  ticker ends at y=960 of 1024. Final entry.png: 1024x1024, 134,554 bytes.
- 2026-11-23 00:22 — Demo: ran main.py twice from a foreign cwd; both runs
  wrote /output/entry.png with identical sha256, equal to the committed
  entry.png. (One demo attempt failed first because the demo script itself
  used a relative path for main.py; fixed by using the absolute path.)
