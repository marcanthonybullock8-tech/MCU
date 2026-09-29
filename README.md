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
  - [Film #10: Thor: Stormbreaker](story/films/P2-02_THOR_STORMBREAKER.md)
  - [Film #11: Fantastic Four](story/films/P2-03_FANTASTIC_FOUR.md)
  - [Film #12: Captain America: The Winter Soldier](story/films/P2-04_CAPTAIN_AMERICA_THE_WINTER_SOLDIER.md)
  - [Film #13: The Amazing Spider-Man](story/films/P2-05_THE_AMAZING_SPIDER-MAN.md)
  - [Film #14: Guardians of the Galaxy](story/films/P2-06_GUARDIANS_OF_THE_GALAXY.md)
  - [Film #15: Avengers: Ultron Unlimited](story/films/P2-07_AVENGERS_ULTRON_UNLIMITED.md)
  - [Film #16: Ant-Man and the Wasp: Yellowjacket](story/films/P2-08_ANT-MAN_AND_THE_WASP_YELLOWJACKET.md)
  - [Film #17: Silver Surfer](story/films/P2-09_SILVER_SURFER.md)
- [Phase 3 Slate](story/07_PHASE_THREE_SLATE.md)
  - [Film #18: Captain America: Civil War](story/films/P3-01_CAPTAIN_AMERICA_CIVIL_WAR.md)
  - [Film #19: Black Panther](story/films/P3-02_BLACK_PANTHER.md)
  - [Film #20: Doctor Strange](story/films/P3-03_DOCTOR_STRANGE.md)
  - [Film #21: Guardians of the Galaxy: Cosmic Avengers](story/films/P3-04_GUARDIANS_OF_THE_GALAXY_COSMIC_AVENGERS.md)
  - [Film #22: Wolverine](story/films/P3-05_WOLVERINE.md)
  - [Film #23: Thor: The Twilight Sword](story/films/P3-06_THOR_THE_TWILIGHT_SWORD.md)
  - [Film #24: Planet Hulk](story/films/P3-07_PLANET_HULK.md)
  - [Film #25: Avengers: The Infinity Gauntlet](story/films/P3-08_AVENGERS_THE_INFINITY_GAUNTLET.md)
  - [Film #26: Captain Marvel](story/films/P3-09_CAPTAIN_MARVEL.md)
  - [Film #27: Warlock](story/films/P3-10_WARLOCK.md)
  - [Film #28: Avengers Forever](story/films/P3-11_AVENGERS_FOREVER.md)
  - [Film #29: The Amazing Spider-Man 2](story/films/P3-12_THE_AMAZING_SPIDER-MAN_2.md)
- [Saga Appearances](story/08_SAGA_APPEARANCES.md): every actor's film and phase count
- [Saga Two Bible: The Secret Wars Saga](story/09_SAGA_TWO_BIBLE.md): Phases 4–6, Doctor Doom
- [Story Format Bible](story/03_STORY_FORMAT_BIBLE.md): format, structure, genre and rating for the real-world story (not started)

## PDFs
Every story document is also rendered as a PDF in [`pdf/`](pdf/). To regenerate them after editing or adding a chapter, run:

    pip install markdown && python3 tools/build_pdfs.py

## Standing rules
- Every story document gets a PDF in `pdf/`.
- **Film dossiers are written automatically** as soon as a film is added to the slate, without asking first.
