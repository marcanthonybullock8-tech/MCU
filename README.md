# MCU

An alternate-history, real-world chronicle of the birth of the Marvel Cinematic Universe, starting in 2007.

- [Franchise Bible](story/00_FRANCHISE_BIBLE.md): locked canon
- [Chapter One (2007)](story/01_CHAPTER_ONE_2007.md): mockumentary pilot draft (🔒 story not started)
- [Cast Bible](story/02_CAST_BIBLE.md): 🔓 unlocked
- [Film Dossier Template](story/04_FILM_DOSSIER_TEMPLATE.md): required fields for every MCU film
- [Phase 1 Slate](story/05_PHASE_ONE_SLATE.md)
  - [Film #1: Iron Man](story/films/P1-01_IRON_MAN.md)
  - [Film #2: The Incredible Hulk](story/films/P1-02_THE_INCREDIBLE_HULK.md)
  - [Film #3: Thor](story/films/P1-03_THOR.md)
  - [Film #4: Ant-Man and the Wasp](story/films/P1-04_ANT-MAN_AND_THE_WASP.md)
  - [Film #5: Iron Man 2](story/films/P1-05_IRON_MAN_2.md)
  - [Film #6: Captain America](story/films/P1-06_CAPTAIN_AMERICA.md)
  - [Film #7: X-Men](story/films/P1-07_X-MEN.md)
  - [Film #8: The Avengers](story/films/P1-08_THE_AVENGERS.md)
- [Phase 2 Slate](story/06_PHASE_TWO_SLATE.md)
  - [Film #9: Iron Man 3](story/films/P2-01_IRON_MAN_3.md)
- [Story Format Bible](story/03_STORY_FORMAT_BIBLE.md): format, structure, genre and rating for the real-world story (not started)

## PDFs
Every story document is also rendered as a PDF in [`pdf/`](pdf/). To regenerate them after editing or adding a chapter, run:

    pip install markdown && python3 tools/build_pdfs.py

## Standing rules
- Every story document gets a PDF in `pdf/`.
- **Film dossiers are written automatically** as soon as a film is added to the slate, without asking first.
