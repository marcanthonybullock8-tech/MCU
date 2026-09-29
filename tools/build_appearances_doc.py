"""Generate story/08_SAGA_APPEARANCES.md from the film dossiers."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import appearances as A

ROLES = {
 "Marc-Anthony Bullock":"Tony Stark / Iron Man","Tayia Boyd":"Pepper Potts","Amond Baker":"Bruce Banner / Hulk",
 "Esther Smilley":"Thor (and Ragnarok)","Tyler Chapman":"Hank Pym / Ant-Man / Yellowjacket","Elxa Bullock":"Janet van Dyne / Wasp",
 "Harmony Divine":"Natasha Romanoff / Black Widow","Arianna Cummings":"Claire Barton / Hawkeye","Tyrese Avery":"Steve Rogers / Captain America",
 "Grace Bullock":"Wanda Maximoff / Scarlet Witch",
 "Stan Lee":"Cameos","Aubrey Plaza":"Mistress Death","Josh Brolin":"Thanos","Samuel L. Jackson":"Nick Fury",
 "Maximiliano Hernández":"Jasper Sitwell","Pedro Pascal":"Reed Richards / The Maker","Don Cheadle":"Rhodey / War Machine","Evan Peters":"Quicksilver",
 "Joseph Quinn":"Johnny Storm","Paul Bettany":"The Vision","Laurence Fishburne":"Silver Surfer (voice) / Goliath","Ciarán Hinds":"Mephisto",
 "Sebastian Stan":"Bucky / Winter Soldier","Tenoch Huerta":"Namor","Vanessa Kirby":"Sue Storm","Ebon Moss-Bachrach":"Ben Grimm",
 "Tom Holland":"Peter Parker / Spider-Man","Zoe Saldaña":"Gamora","Chadwick Boseman":"T'Challa / Black Panther","Doug Jones":"Silver Surfer",
 "Tom Hiddleston":"Loki","Ray Stevenson":"Volstagg","Anthony Mackie":"Falcon","Chris Pratt":"Star-Lord","Dave Bautista":"Drax",
 "Bradley Cooper":"Rocket (voice)","Vin Diesel":"Groot","Will Poulter":"Adam Warlock / Magus","Pom Klementieff":"Mantis","Karen Gillan":"Nebula",
 "Benedict Cumberbatch":"Doctor Strange / Dormammu","Jon Favreau":"Happy Hogan","Michael Cera":"Rick Jones","Anthony Hopkins":"Odin",
 "Rene Russo":"Frigga","Natalie Portman":"Jane Foster","Idris Elba":"Heimdall","Jaimie Alexander":"Sif","Zachary Levi":"Fandral",
 "Tadanobu Asano":"Hogun","Patrick Stewart":"Charles Xavier","James D'Arcy":"Edwin Jarvis","Rosemary Harris":"Aunt May",
 "Hugh Jackman":"Logan / Wolverine","Paul Giamatti":"Egghead","Tony Leung":"The Mandarin","Hugo Weaving":"Red Skull",
 "Hayley Atwell":"Peggy Carter","Terry Crews":"Beta Ray Bill","Benicio del Toro":"The Collector","Robert Downey Jr.":"Doctor Doom",
 "Kerry Washington":"Alicia Masters","Jeffrey Wright":"Uatu the Watcher","Emily VanCamp":"Sharon Carter","Tony Revolori":"Flash Thompson",
 "Elizabeth Banks":"Betty Brant","J.K. Simmons":"J. Jonah Jameson","Sean Gunn":"Rocket (performance)","Andy Serkis":"Klaw",
 "Ralph Ineson":"Galactus","Benedict Wong":"Wong","Brie Larson":"Carol Danvers / Captain Marvel","Danny DeVito":"Pip the Troll",
 "Jeff Bridges":"Obadiah Stane","Shaun Toub":"Ho Yinsen","Tzi Ma":"Wong-Chu","Liv Tyler":"Betty Ross","William Hurt":"Thunderbolt Ross",
 "Tim Roth":"Abomination","Tim Blake Nelson":"Samuel Sterns","Colm Feore":"Laufey","Dennis Haysbert":"Vernon van Dyne",
 "Sam Rockwell":"Justin Hammer","Stanley Tucci":"Dr. Erskine","Tommy Lee Jones":"Gen. Phillips","Neal McDonough":"Dum Dum Dugan",
 "Derek Luke":"Gabe Jones","Christoph Waltz":"Baron Heinrich Zemo","Ian McKellen":"Magneto","Tye Sheridan":"Cyclops",
 "Sophie Turner":"Jean Grey","Nicholas Hoult":"Beast","Shawn Ashmore":"Iceman","Ben Hardy":"Angel","Ray Park":"Toad",
 "Peter Dinklage":"Bolivar Trask","Rebecca Hall":"Maya Hansen","Guy Pearce":"Aldrich Killian","James Badge Dale":"Mallen",
 "Christopher Eccleston":"Malekith","Adewale Akinnuoye-Agbaje":"Kurse","Paul Walter Hauser":"Mole Man","Mads Mikkelsen":"Aleksander Lukin",
 "Frank Grillo":"Crossbones","Martin Sheen":"Uncle Ben","Alfred Molina":"Doctor Octopus","Laura Harrier":"Liz Allan",
 "James Spader":"Ultron","Jeff Goldblum":"The Grandmaster","Walton Goggins":"The Ringmaster","Paul Rudd":"Scott Lang",
 "Julia Garner":"Shalla-Bal","Jon Bernthal":"The Punisher","Michael B. Jordan":"Killmonger","Lupita Nyong'o":"Nakia",
 "Danai Gurira":"Okoye","Angela Bassett":"Ramonda","Forest Whitaker":"Zuri","Daniel Kaluuya":"W'Kabi",
 "Winston Duke":"M'Baku","John Kani":"T'Chaka","Chiwetel Ejiofor":"Baron Mordo","Tilda Swinton":"The Ancient One",
 "Charlize Theron":"Clea","Liam Neeson":"J'son","Michael Rooker":"Yondu","Sylvester Stallone":"Starhawk","Tao Okamoto":"Mariko Yashida",
 "Hiroyuki Sanada":"Shingen Yashida","Rila Fukushima":"Yukio","Clancy Brown":"Surtur","Karl Urban":"Skurge","Cate Blanchett":"Hela",
 "Taika Waititi":"Korg","Lashana Lynch":"Caiera","Mark Strong":"The Red King","Anson Mount":"Black Bolt","Chris Evans":"Mar-Vell / Lord Mar-Vell",
 "Annette Bening":"Supreme Intelligence","Jude Law":"Yon-Rogg","Willem Dafoe":"Norman Osborn / Green Goblin","Emma Stone":"Gwen Stacy",
 "Dane DeHaan":"Harry Osborn","Denis Leary":"Capt. George Stacy","Zendaya":"Mary Jane Watson","Caleb Landry Jones":"Banshee","Blair Redford":"Thunderbird","Alexandra Shipp":"Storm","Daniel Cudmore":"Colossus","Kodi Smit-McPhee":"Nightcrawler","Ana de Armas":"Lady Dorma","Djimon Hounsou":"Attuma","Eva Green":"Llyra","Serinda Swan":"Medusa","Iwan Rheon":"Maximus","Ken Leung":"Karnak","Eme Ikwuakor":"Gorgon","Isabelle Cornish":"Crystal","Mike Moh":"Triton","Aaron Taylor-Johnson":"Kraven the Hunter","Richard Madden":"Ikaris","Gemma Chan":"Sersi","Angelina Jolie":"Thena","Kumail Nanjiani":"Kingo","Brian Tyree Henry":"Phastos / Jefferson Davis","Barry Keoghan":"Druig","Don Lee":"Gilgamesh","Kit Harington":"Dane Whitman","Bill Skarsgård":"Kro","Harry Styles":"Eros / Starfox","Salma Hayek":"Ajak","Lauren Ridloff":"Makkari","Lia McHugh":"Sprite","Kathryn Newton":"Cassie Lang","Lee Pace":"Ronan","Ben Mendelsohn":"Talos","Iman Vellani":"Kamala Khan / Ms. Marvel","Teyonah Parris":"Monica Rambeau","Donald Glover":"Aaron Davis / Prowler","Luna Lauren Vélez":"Rio Morales","Lewis Pullman":"The Sentry","Shameik Moore":"Miles Morales / Spider-Man","Rosamund Pike":"Morgan le Fay","Christian Bale":"Gorr the God Butcher","Oscar Isaac":"Moon Knight / Apocalypse","Omar Sy":"Bishop","Anna Paquin":"Rogue","Liev Schreiber":"Sabretooth","Fan Bingbing":"Blink","Dan Stevens":"Legion","F. Murray Abraham":"Khonshu (voice)","Gael García Bernal":"Jack Russell / Werewolf by Night","Cobie Smulders":"Maria Hill","Toby Jones":"Arnim Zola","Jake Gyllenhaal":"Mysterio","Tom Hardy":"Eddie Brock / Venom","Gabriel Luna":"Robbie Reyes / Ghost Rider","Nicolas Cage":"Johnny Blaze / Ghost Rider","Letitia Wright":"Shuri / Black Panther",
}

nums = {t: i + 1 for i, (_, t, _) in enumerate(A.films)}

def row(name, hits):
    per = [sum(1 for p, _ in hits if p == k) for k in PH]
    phases = sum(1 for c in per if c)
    films = ", ".join(f"#{nums[t]}" for _, t in hits)
    return f"| **{name}** | {ROLES.get(name,'')} | **{len(hits)}** | **{phases}** | " + " | ".join(str(c) for c in per) + f" | {films} |"

PH = sorted({p for p, _, _ in A.films})
HEAD = "| Actor | Role(s) | Films | Phases | " + " | ".join(f"P{p}" for p in PH) + " | Film #s |\n|" + "---|" * (5 + len(PH))
fic = sorted(A.tally(A.FICTIONAL), key=lambda x: (-len(x[1]), x[0]))
real = sorted(A.tally(A.REAL), key=lambda x: (-len(x[1]), x[0]))

out = ["# SAGA APPEARANCES: EVERY ACTOR, EVERY FILM",
       f"### Every MCU film so far: {len(A.films)} films, {len({p for p, _, _ in A.films})} phases",
       f"*Generated from the cast sections of the {len(A.films)} film dossiers (`tools/build_appearances_doc.py`). Voice roles, cameos, and mid- and post-credit appearances all count.*",
       "", "---", "", "## FILM KEY", "| # | Film | Phase |", "|---|---|---|"]
def nice(t):
    w = t.title().split(" ")
    return " ".join(x.lower() if i and x.lower() in ("and", "the", "of") and not w[i-1].endswith(":") else x for i, x in enumerate(w))
out += [f"| {nums[t]} | {nice(t)} | {p} |" for p, t, _ in A.films]
out += ["", "---", "", f"## THE FICTIONAL ENSEMBLE ({len(fic)} actors)", HEAD] + [row(n, h) for n, h in fic]
out += ["", "---", "", f"## REAL-LIFE ACTORS ({len(real)} actors)", HEAD] + [row(n, h) for n, h in real]
out += ["", "---", "", "## TOTALS",
        f"- **{len(fic) + len(real)} actors** across **{len(A.films)} films.**",
        f"- **Most appearances overall:** {real[0][0]}, in **{len(real[0][1])}** films.",
        f"- **Most appearances by a fictional ensemble actor:** {fic[0][0]}, **{len(fic[0][1])} films.**",
        f"- **In three or more phases:** " + ", ".join(n for n, h in fic + real if len({p for p, _ in h}) >= 3) + "."]
open(os.path.join(A.ROOT, "story", "08_SAGA_APPEARANCES.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
print("written")
