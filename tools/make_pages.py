# Writes the product pages for Wardwinter TD, Fourfront and Pulsefall in the shared ginger4le frame.
# Add a new game as another entry in GAMES, put icon and screenshots into <dir>/img/ and run: python3 tools/make_pages.py
import html, sys, os

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def t(de, en):
    return f'<span class="de">{de}</span><span class="en">{en}</span>'


GAMES = [
    {
        "dir": "wardwinter", "name": "Wardwinter TD", "mail": "wardwinter",
        "accent": "#8fb8ef", "on": "#0d1a30", "hero": "#121b2c",
        "title_de": "Wardwinter TD – Baut Labyrinthe, nicht nur Türme",
        "desc": "Kooperative Maze-Tower-Defense für 1 bis 12 Spieler: Baut Labyrinthe gegen die Weiße Flut.",
        "og": "Build mazes, not just towers. Co-op maze tower defense for 1 to 12 players.",
        "tagline": ("Baut Labyrinthe,<br>nicht nur Türme.", "Build mazes,<br>not just towers."),
        "intro": ("Die Weiße Flut kommt. Endlose Horden von Untoten strömen aus dem ewigen Winter – und nur euer Labyrinth hält sie auf.",
                  "The White Tide is coming. Endless hordes of undead pour out of the eternal winter – and only your maze stands in their way."),
        "status": ("In Entwicklung · PC und Android", "In development · PC and Android"),
        "shots": "wide",
        "images": [("img/01_white_keep_coop.jpg", "Sechs Baumeister verteidigen die Weiße Feste", "Six builders defend the White Keep", 1280, 720),
                   ("img/02_frost_creatures.jpg", "Frost-Baumeister mit Yeti gegen eine Welle", "Frost builder with a yeti against a wave", 1280, 720),
                   ("img/04_spring_bowl.jpg", "Frühlingskarte Blütenkessel", "Spring map Blossom Bowl", 1280, 720),
                   ("img/05_autumn_forest.jpg", "Herbstkarte Nebelwald", "Autumn map Misty Forest", 1280, 720)],
        "features": [
            (("Kein fester Weg", "No fixed path"), ("Jeder Turm ist eine Mauer. Lenke den Weg in Serpentinen und sieh in der Vorschau, um wie viele Felder er länger wird.",
                                                    "Every tower is a wall. Bend the route back on itself and watch the preview show how many cells longer it gets.")),
            (("Gemeinsam spielen", "Play together"), ("1 bis 12 Spieler teilen sich eine Feste und 50 Leben. Jeder Kill bringt allen Gold, KI-Baumeister füllen freie Plätze.",
                                                      "1 to 12 players share one fortress and 50 lives. Every kill pays everyone, AI builders fill empty seats.")),
            (("9 Baumeister, 99 Türme", "9 builders, 99 towers"), ("Frost, Glut, Stein, Sturm, Gift und Arkan – dazu Kreaturen vom Frostyeti bis zum Lich.",
                                                                  "Frost, ember, stone, storm, venom and arcane – plus creatures from the frost yeti to the lich.")),
            (("14 Karten, 4 Jahreszeiten", "14 maps, 4 seasons"), ("Vom Frostpass bis zur Weißen Feste, mit Kampagne, Hart, Endlos und täglicher Herausforderung.",
                                                                  "From the Frost Pass to the White Keep, with campaign, Hard, Endless and a daily challenge.")),
        ],
        "privacy": True,
    },
    {
        "dir": "fourfront", "name": "Fourfront", "mail": "fourfront",
        "accent": "#f0c35a", "on": "#2a1a04", "hero": "#171a2c",
        "title_de": "Fourfront: Heroes & Hordes",
        "desc": "Führe deinen Helden und deine Armee in schnelle Schlachten um vier Burgen.",
        "og": "Lead your hero and a growing army in fast battles for four castles.",
        "display": "Fourfront: Heroes &amp; Hordes",
        "tagline": ("Vier Burgen. Vier Armeen.<br>Nur eine bleibt stehen.", "Four castles. Four armies.<br>Only one stays standing."),
        "intro": ("Du steuerst einen Helden mitten in einer Schlacht, die nie stillsteht: Alle 15 Sekunden schickt deine Kaserne neue Soldaten. Führe sie an, halte die Stellung oder stürme die gegnerische Burg.",
                  "You control a hero in a battle that never stops: every 15 seconds your barracks send fresh soldiers. Lead them, hold the line or storm the enemy castle."),
        "status": ("Bald bei Google Play", "Coming soon to Google Play"),
        "shots": "wide",
        "images": [("img/01_ultimate.jpg", "Ein Held setzt seine Ultimate ein", "A hero unleashes an ultimate", 1280, 720),
                   ("img/02_battle.jpg", "Schlacht um die Burgen", "Battle for the castles", 1280, 720),
                   ("img/04_base.jpg", "Burg ausbauen", "Expanding the castle", 1280, 720),
                   ("img/05_heroes.jpg", "Heldenauswahl", "Hero selection", 1280, 720)],
        "features": [
            (("Helden mit Charakter", "Heroes with character"), ("20 Helden – Tanks, Assassinen, Magier, Schützen, Supports und Feldherren – mit je drei Fähigkeiten und einer Ultimate.",
                                                                "20 heroes – tanks, assassins, mages, marksmen, supports and warlords – each with three abilities and an ultimate.")),
            (("Deine Armee", "Your army"), ("Rüste die Kaserne auf, bau deine Burg aus und kaufe legendäre Ausrüstung für Held oder Armee.",
                                           "Upgrade your barracks, expand your castle and buy legendary gear for your hero or your army.")),
            (("Schnelle Matches", "Fast matches"), ("1v1, 2v2, jeder gegen jeden und 3v3v3v3, mit Bossen, Hinterhalten im hohen Gras und dem Hügel in der Mitte.",
                                                   "1v1, 2v2, free-for-all and 3v3v3v3, with bosses, ambushes from tall grass and the hill in the centre.")),
            (("Gemacht fürs Handy", "Made for mobile"), ("Joystick und Fähigkeiten-Knöpfe, Auto-Zielen per Antippen, offline spielbar gegen KI in drei Stärken.",
                                                        "Joystick and ability buttons, tap to auto-aim, play offline against the AI on three difficulty levels.")),
        ],
        "privacy": False,
    },
    {
        "dir": "pulsefall", "name": "Pulsefall", "mail": "pulsefall",
        "accent": "#5ee7f0", "on": "#08262a", "hero": "#1d1235",
        "title_de": "Pulsefall: Gem Merge",
        "desc": "Lass Gems fallen, verschmelze Zwillinge und zieh mit dem Puls ganze Ketten.",
        "og": "Drop gems, merge twins and pull whole chains together with the pulse.",
        "display": "Pulsefall",
        "tagline": ("Lass Gems fallen. Verschmelze Zwillinge.<br>Halte den Puls.", "Drop gems. Merge twins.<br>Hold the pulse."),
        "intro": ("Ein Merge-Puzzle mit echter Physik: Zwei gleiche Gems werden zu einem größeren. Klettere über zehn Stufen vom kleinen Diamanten bis zur Sonne – bevor das Glas überläuft.",
                  "A merge puzzle with real physics: two equal gems become a bigger one. Climb ten tiers from a tiny diamond all the way to the sun – before the glass overflows."),
        "status": ("Bald bei Google Play", "Coming soon to Google Play"),
        "shots": "tall",
        "images": [("img/shot_1_{l}.jpg", "Pulsefall Spielszene 1", "Pulsefall gameplay 1", 540, 960),
                   ("img/shot_2_{l}.jpg", "Pulsefall Spielszene 2", "Pulsefall gameplay 2", 540, 960),
                   ("img/shot_3_{l}.jpg", "Pulsefall Spielszene 3", "Pulsefall gameplay 3", 540, 960)],
        "features": [
            (("Der Puls", "The pulse"), ("Jede Fusion lädt den Puls. Halte einen Gem fest, und sein Zwilling gleitet quer durch den Stapel zu dir – ganze Ketten auf einmal.",
                                         "Every merge charges the pulse. Hold a gem and its twin glides through the pile to you – whole chains at once.")),
            (("Kurze Runden", "Short rounds"), ("Tippen zum Fallenlassen, ein Endlos-Modus, der enger wird, und jeden Tag eine neue Daily Challenge.",
                                               "Tap to drop, an endless mode that gets tighter and a new Daily Challenge every day.")),
            (("Spezial-Gems", "Special gems"), ("Joker, Laser, Magnet, Glitch und Mine, dazu Erfolge und sammelbare Gefäß-Designs.",
                                               "Joker, laser, magnet, glitch and mine, plus achievements and collectible vessel designs.")),
            (("Fair", "Fair"), ("Kein Konto, spielbar offline, Videos freiwillig. Pulse Plus ist ein Einmalkauf, kein Abo.",
                                "No account, plays offline, videos are optional. Pulse Plus is a one-time purchase, not a subscription.")),
        ],
        "privacy": False,
    },
]


def shots(g):
    if g["shots"] == "tall":
        out = []
        for lang in ("de", "en"):
            imgs = "\n".join(
                f'    <img src="{src.format(l=lang)}" alt="{de if lang == "de" else en}" width="{w}" height="{h}">'
                for src, de, en, w, h in g["images"])
            out.append(f'  <div class="pshots {lang}">\n{imgs}\n  </div>')
        return "\n".join(out)
    cls = "wshots single" if g["shots"] == "wide-single" else "wshots"
    imgs = "\n".join(f'    <img src="{src}" alt="{de}" width="{w}" height="{h}" loading="lazy">' for src, de, en, w, h in g["images"])
    return f'  <div class="{cls}">\n{imgs}\n  </div>'


def page(g):
    name = g.get("display", g["name"])
    feats = "\n".join(f'    <div><h3>{t(*h)}</h3><p>{t(*p)}</p></div>' for h, p in g["features"])
    mail = f'ginger4le.dev+{g["mail"]}@gmail.com'
    privacy = f'\n  <a href="privacy.html">{t("Datenschutz", "Privacy policy")}</a>' if g["privacy"] else ""
    first = g["images"][0][0].format(l="en")
    return f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(g["title_de"])}</title>
<meta name="description" content="{html.escape(g["desc"])}">
<meta name="theme-color" content="{g["hero"]}">
<meta property="og:title" content="{html.escape(g["title_de"].split(" – ")[0])}">
<meta property="og:description" content="{html.escape(g["og"])}">
<meta property="og:image" content="https://ginger4le.github.io/{g["dir"]}/{first}">
<link rel="icon" href="img/icon.png">
<link rel="stylesheet" href="../style.css">
<script src="../assets/lang.js"></script>
</head>
<body style="--accent:{g["accent"]}; --on-accent:{g["on"]}; --hero:{g["hero"]};">
<header class="top"><div class="wrap">
  <a class="logo" href="../">ginger4le</a>
  <nav class="nav">
    <a href="../#spiele" class="hide-sm">{t("Alle Spiele und Apps", "All games and apps")}</a>
    <span class="lang"><button data-set="de" aria-label="Deutsch">DE</button><button data-set="en" aria-label="English">EN</button></span>
  </nav>
</div></header>

<section class="phero"><div class="wrap">
  <img class="appicon" src="img/icon.png" alt="" width="88" height="88">
  <h1>{name}</h1>
  <p class="tagline">{t(*g["tagline"])}</p>
  <p class="intro">{t(*g["intro"])}</p>
  <span class="status">{t(*g["status"])}</span>
</div></section>

<main class="wrap">
{shots(g)}

  <div class="features">
{feats}
  </div>

  <section class="support">
    <h2>{t("Gefällt dir " + g["name"] + "?", "Enjoying " + g["name"] + "?")}</h2>
    <p>{t("Ich entwickle meine Spiele allein in meiner Freizeit. Wenn du magst, was du siehst, freue ich mich über einen Kaffee – oder über dein Feedback.",
          "I make my games on my own in my spare time. If you like what you see, a coffee makes my day – and so does your feedback.")}</p>
    <div class="actions" style="justify-content:center">
      <a class="btn accent" href="https://ko-fi.com/artembruner" rel="noopener">☕ {t("Spendier mir einen Kaffee", "Buy me a coffee")}</a>
      <a class="btn" href="mailto:{mail}?subject={g["name"].replace(" ", "%20")}">{t("Feedback schreiben", "Send feedback")}</a>
    </div>
  </section>
</main>

<footer class="foot"><div class="wrap">
  <span>© 2026 Ginger4le · Artem Bruner</span>{privacy}
  <a href="mailto:{mail}">{t("Kontakt", "Contact")}</a>
  <a href="https://ko-fi.com/artembruner" rel="noopener">Ko-fi</a>
  <a class="sp" href="../">{t("Alle Spiele und Apps", "All games and apps")}</a>
</div></footer>
</body>
</html>
'''


for g in GAMES:
    path = os.path.join(SITE, g["dir"], "index.html")
    with open(path, "w") as f:
        f.write(page(g))
    print("wrote", path)
