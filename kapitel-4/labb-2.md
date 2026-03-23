# Labb 2 – djurparken

Du bygger en flersidig webbplats om en djurpark. Varje sida handlar om ett djur. Du repeterar navigation, `.aktiv`-klass och hover — och lägger till mer innehåll per sida.

## Introduktion och mål

I den här labben tränar du på att:

* Bygga en flersidig webbplats med 4+ sidor.
* Använda `.aktiv` och `:hover` konsekvent (repetition).
* Skapa rikare innehåll: bilder, listor och tabeller.
* Repetition: `.kontainer`, CSS-reset, CSS-variabler, `<figure>`.

## Startkod

Skapa fyra HTML-filer: `sida1.html` (start), `sida2.html` (lejon), `sida3.html` (pingvin), `sida4.html` (elefant). Plus `style.css` och en mapp `bilder/`.

**sida1.html:**

```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Djurparken – Start</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="kontainer">
        <div class="meny">
            <a href="sida1.html" class="aktiv">Start</a>
            <a href="sida2.html">Lejon</a>
            <a href="sida3.html">Pingvin</a>
            <a href="sida4.html">Elefant</a>
        </div>

        <h1>🦁 Välkommen till djurparken!</h1>
        <p>Utforska våra fantastiska djur genom att klicka i menyn.</p>

        <div class="info-box">
            <h2>Öppettider</h2>
            <table>
                <tr>
                    <th>Dag</th>
                    <th>Tid</th>
                </tr>
                <tr>
                    <td>Måndag – fredag</td>
                    <td>10:00 – 17:00</td>
                </tr>
                <tr>
                    <td>Lördag – söndag</td>
                    <td>09:00 – 18:00</td>
                </tr>
            </table>
        </div>
    </div>
</body>
</html>
```

**sida2.html:**

```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Djurparken – Lejon</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="kontainer">
        <div class="meny">
            <a href="sida1.html">Start</a>
            <a href="sida2.html" class="aktiv">Lejon</a>
            <a href="sida3.html">Pingvin</a>
            <a href="sida4.html">Elefant</a>
        </div>

        <h1>🦁 Lejon</h1>
        <p>Lejonet är djungelns kung. Här är fakta om lejon.</p>

        <h2>Fakta</h2>
        <ul>
            <li><strong>Vikt:</strong> 150–250 kg</li>
            <li><strong>Livslängd:</strong> 10–14 år i det vilda</li>
            <li><strong>Föda:</strong> kött (zebror, gnuer, antiloper)</li>
        </ul>
    </div>
</body>
</html>
```

Skapa `sida3.html` och `sida4.html` själv med samma menystruktur (se uppgifterna!).

**style.css:**

```css
/* CSS-reset */
html { box-sizing: border-box; }
*, *:before, *:after { box-sizing: inherit; }
body, h1, h2, h3, p, ul { margin: 0; padding: 0; }

:root {
    --bakgrund: #f5f0e8;
    --text: #333;
    --accent: #2d6a4f;
    --meny-bg: #1b4332;
    --meny-text: #d8f3dc;
}

body {
    font-family: 'Segoe UI', sans-serif;
    background-color: var(--bakgrund);
    color: var(--text);
}

.kontainer {
    width: 700px;
    margin: auto;
    padding: 20px;
}

.meny {
    background-color: var(--meny-bg);
    padding: 12px;
    border-radius: 8px;
    margin-bottom: 25px;
}

.meny a {
    color: var(--meny-text);
    text-decoration: none;
    display: inline-block;
    padding: 8px 18px;
    border-radius: 5px;
    margin-right: 5px;
    transition: 0.2s;
}

.meny a:hover {
    background-color: var(--accent);
}

.meny .aktiv {
    background-color: var(--accent);
    font-weight: bold;
}

h1 {
    margin-bottom: 10px;
}

h2 {
    color: var(--accent);
    margin-top: 25px;
    margin-bottom: 10px;
}

ul {
    padding-left: 25px;
}

li {
    margin-bottom: 6px;
}

.info-box {
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    margin-top: 25px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

table {
    width: 100%;
    border-spacing: 0;
    margin-top: 10px;
}

th, td {
    padding: 10px;
    text-align: left;
}

th {
    background-color: var(--accent);
    color: white;
}

tr:nth-child(even) {
    background-color: #f0f0f0;
}
```

## Uppgifter

### Nivå 1: uppvärmning (mycket enkelt)

**Uppgift 1: skapa sida3 och sida4**
Skapa `sida3.html` (Pingvin) och `sida4.html` (Elefant). Kopiera menystrukturen från `sida2.html` och flytta `class="aktiv"` till rätt länk. Skriv en rubrik, ett stycke och en faktalista.

**Uppgift 2: kontrollera menyn**
Klicka dig igenom alla fyra sidor. Kontrollera att:
- Menyn ser likadan ut på varje sida.
- Rätt länk är markerad med `.aktiv`.
- Alla länkar fungerar.

### Nivå 2: mer innehåll (enkelt)

**Uppgift 3: bilder på djuren**
Lägg till en bild (med `<figure>` och `<figcaption>`) på varje djursida. Lägg bilderna i `bilder/`.

**Uppgift 4: fakta-tabell**
På en av djursidorna, byt ut faktalistan mot en tabell. Använd `<table>`, `<th>` och `<td>`.

### Nivå 3: förbättra designen (medel)

**Uppgift 5: info-boxar**
Ge faktainformationen på varje djursida en vit bakgrund med `.info-box`-klassen (samma stil som startsidans öppettider).

**Uppgift 6: nytt färgtema**
Byt alla färger i `:root` till ett helt nytt tema. Testa t.ex. ett havsblått tema eller ett ökentema.

### Nivå 4: utöka webbplatsen (avancerat)

**Uppgift 7: femte sidan**
Skapa `sida5.html` (t.ex. "Karta" eller "Om oss"). Uppdatera menyn på **alla fem sidor**.

**Uppgift 8: länk till extern källa**
Lägg till en stilad länk (utan understrykning, med padding och bakgrundsfärg) på varje djursida som leder till t.ex. Wikipedia-artikeln om djuret.

(Repetition: stilade länkar från kapitel 2!)

### Nivå 5: boss-nivån

**Uppgift 9: sex djur**
Bygg ut webbplatsen till minst sex djursidor plus startsidan. Varje djursida ska ha bild, fakta och extern länk.

**Uppgift 10: den ultimata djurparken**
Gör webbplatsen komplett:

1. Importera ett Google Font.
2. Ge startsidan en hero-sektion med bakgrundsbild.
3. Alla djursidor har bild, faktalista (eller tabell) och länk.
4. Ge alla bilder `border-radius` och `box-shadow`.
5. Menyn fungerar perfekt med `.aktiv` på alla sidor.
6. Sidan har ett konsekvent färgtema via `:root`.
