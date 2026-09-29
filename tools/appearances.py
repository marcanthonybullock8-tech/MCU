"""Count each actor's film and phase appearances from the dossiers' Section 2 (Ownership/cast)."""
import glob, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FICTIONAL = ["Marc-Anthony Bullock", "Tayia Boyd", "Amond Baker", "Esther Smilley", "Tyler Chapman",
             "Elxa Bullock", "Harmony Divine", "Arianna Cummings", "Tyrese Avery", "Grace Bullock"]
REAL = """Samuel L. Jackson|Don Cheadle|Jeff Bridges|Jon Favreau|Shaun Toub|Tzi Ma|Maximiliano Hernández|Stan Lee|Aubrey Plaza|
Liv Tyler|William Hurt|Tim Roth|Michael Cera|Tim Blake Nelson|Tom Hiddleston|Anthony Hopkins|Rene Russo|Natalie Portman|Idris Elba|
Jaimie Alexander|Ray Stevenson|Zachary Levi|Tadanobu Asano|Colm Feore|Dennis Haysbert|Paul Giamatti|Tony Leung|Sam Rockwell|
Hugo Weaving|Stanley Tucci|Sebastian Stan|Hayley Atwell|Tommy Lee Jones|Neal McDonough|Derek Luke|Christoph Waltz|Tenoch Huerta|
Patrick Stewart|Ian McKellen|Tye Sheridan|Sophie Turner|Nicholas Hoult|Shawn Ashmore|Ben Hardy|Evan Peters|Ray Park|Peter Dinklage|
James D'Arcy|Josh Brolin|Rebecca Hall|Guy Pearce|James Badge Dale|Terry Crews|Christopher Eccleston|Adewale Akinnuoye-Agbaje|
Benicio del Toro|Pedro Pascal|Vanessa Kirby|Joseph Quinn|Ebon Moss-Bachrach|Robert Downey Jr.|Kerry Washington|Paul Walter Hauser|
Jeffrey Wright|Anthony Mackie|Emily VanCamp|Mads Mikkelsen|Frank Grillo|Tom Holland|Rosemary Harris|Martin Sheen|Tony Revolori|
Elizabeth Banks|J.K. Simmons|Alfred Molina|Laura Harrier|Chris Pratt|Zoe Saldaña|Dave Bautista|Bradley Cooper|Sean Gunn|Vin Diesel|
Will Poulter|Pom Klementieff|Karen Gillan|James Spader|Paul Bettany|Andy Serkis|Chadwick Boseman|Jeff Goldblum|Walton Goggins|
Paul Rudd|Doug Jones|Laurence Fishburne|Ralph Ineson|Julia Garner|Ciarán Hinds|Jon Bernthal|Michael B. Jordan|Lupita Nyong'o|
Danai Gurira|Letitia Wright|Angela Bassett|Forest Whitaker|Daniel Kaluuya|Winston Duke|John Kani|Benedict Cumberbatch|
Chiwetel Ejiofor|Benedict Wong|Tilda Swinton|Charlize Theron|Liam Neeson|Michael Rooker|Sylvester Stallone|Hugh Jackman|Tao Okamoto|
Hiroyuki Sanada|Rila Fukushima|Clancy Brown|Karl Urban|Cate Blanchett|Taika Waititi|Lashana Lynch|Mark Strong|Anson Mount|Brie Larson|
Chris Evans|Annette Bening|Jude Law|Danny DeVito|Willem Dafoe|Emma Stone|Dane DeHaan|Denis Leary|Zendaya|Caleb Landry Jones|Blair Redford|Alexandra Shipp|Daniel Cudmore|Kodi Smit-McPhee|Ana de Armas|Djimon Hounsou|Eva Green|Serinda Swan|Iwan Rheon|Ken Leung|Eme Ikwuakor|Isabelle Cornish|Mike Moh|Aaron Taylor-Johnson|Richard Madden|Gemma Chan|Angelina Jolie|Kumail Nanjiani|Brian Tyree Henry|Barry Keoghan|Don Lee|Kit Harington|Bill Skarsgård|Harry Styles|Salma Hayek|Lauren Ridloff|Lia McHugh|Kathryn Newton|Lee Pace|Ben Mendelsohn|Iman Vellani|Teyonah Parris|Donald Glover|Luna Lauren Vélez|Lewis Pullman""".replace("\n", "").split("|")

def cast_section(text):
    m = re.search(r"## 2\. OWNERSHIP(.*?)\n## 3\.", text, re.S)
    if not m:
        return ""
    # count only cast-table rows and cast lists, not italic casting notes
    return "\n".join(l for l in m.group(1).splitlines() if l.lstrip().startswith(("|", "- **")))

films = []
for path in sorted(glob.glob(os.path.join(ROOT, "story", "films", "P*.md"))):
    text = open(path, encoding="utf-8").read()
    title = re.search(r"# FILM DOSSIER: (.+)", text).group(1).strip()
    phase = int(os.path.basename(path)[1])
    films.append((phase, title, cast_section(text)))

def tally(names):
    rows = []
    for n in names:
        hits = [(p, t) for p, t, c in films if n in c]
        if hits:
            rows.append((n, hits))
    return rows

if __name__ == "__main__":
    import json
    out = {"fictional": tally(FICTIONAL), "real": tally(REAL)}
    print(json.dumps(out, ensure_ascii=False))
