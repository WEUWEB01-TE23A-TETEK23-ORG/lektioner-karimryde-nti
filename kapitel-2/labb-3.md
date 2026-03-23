# Labb 3 – reklamaffischen

Det är dags att kombinera allt du lärt dig i kapitel 1 och 2! Du bygger en snygg reklamaffisch med bakgrundsbilder, bilder med bildtext, stiliga knapplänkar och versaler.

## Introduktion och mål

I den här labben repeterar och kombinerar du:

* Bakgrundsbilder med `background-size` och `background-position` (repetition).
* `<figure>` och `<figcaption>` (repetition från labb 1).
* Stilade länkar utan understrykning (repetition från labb 2).
* `text-transform: uppercase` (repetition från labb 2).
* Rubriker, stycken, listor, bilder och tabeller (repetition från kapitel 1).
* CSS-effekter: `box-shadow`, `text-shadow`, `border-radius` (repetition).

## Startkod

Skapa `index.html` och `style.css`. Lägg bilder i mappen `bilder/`.

**index.html:**

```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sommarcampen</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="topp">
        <h1>Sommarcampen 2026</h1>
        <p>Den bästa sommaren börjar här!</p>
        <a href="#info" class="knapp">Anmäl dig nu</a>
    </div>

    <div class="info" id="info">
        <h2>Vad ingår?</h2>
        <ul>
            <li>Simning och kanotpaddling</li>
            <li>Grillkväll varje fredag</li>
            <li>Utflykter i naturen</li>
        </ul>
    </div>

    <div class="galleri">
        <h2>Bilder från förra året</h2>
        <figure>
            <img src="bilder/bild1.jpg" alt="Barn som simmar">
            <figcaption>Simtävling i sjön</figcaption>
        </figure>
    </div>

    <div class="priser">
        <h2>Priser</h2>
        <table>
            <tr>
                <th>Paket</th>
                <th>Pris</th>
            </tr>
            <tr>
                <td>En vecka</td>
                <td>2 500 kr</td>
            </tr>
            <tr>
                <td>Två veckor</td>
                <td>4 000 kr</td>
            </tr>
        </table>
    </div>
</body>
</html>
```

**style.css:**

```css
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;700;900&display=swap');

body {
    font-family: 'Nunito', sans-serif;
    margin: 0;
    color: #333;
    background-color: #f9f9f9;
}

.topp {
    background-image: url('bilder/bakgrund.jpg');
    background-size: cover;
    background-position: center;
    color: white;
    text-align: center;
    padding: 120px 20px;
}

.topp h1 {
    font-size: 3rem;
    text-transform: uppercase;
    text-shadow: 3px 3px 8px rgba(0, 0, 0, 0.5);
}

.topp p {
    font-size: 1.3rem;
}

.knapp {
    display: inline-block;
    background-color: #ff6b35;
    color: white;
    padding: 15px 35px;
    text-decoration: none;
    text-transform: uppercase;
    font-weight: bold;
    border-radius: 50px;
    margin-top: 20px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
}

.knapp:hover {
    background-color: #e55a2b;
}

.info, .galleri, .priser {
    padding: 40px;
    max-width: 700px;
    margin: auto;
}

ul {
    padding-left: 20px;
}

li {
    margin-bottom: 8px;
    font-size: 1.1rem;
}

figure {
    margin: 20px 0;
}

img {
    width: 100%;
    border-radius: 10px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

figcaption {
    font-style: italic;
    color: #666;
    margin-top: 8px;
}

table {
    width: 100%;
    border-spacing: 0;
    margin-top: 15px;
}

th, td {
    padding: 12px 15px;
    text-align: left;
}

th {
    background-color: #ff6b35;
    color: white;
}

tr:nth-child(even) {
    background-color: #f0f0f0;
}
```

## Uppgifter

Det finns ingen övningssektion den här gången — du kan allt som behövs! Använd det du lärt dig i labb 1 och labb 2.

### Nivå 1: uppvärmning (mycket enkelt)

**Uppgift 1: byt tema**
Ändra texterna så att sidan handlar om något annat (t.ex. en sportcup, en musikfestival eller en matfestival). Ändra rubriken, stycketexten och listan.

**Uppgift 2: byt bakgrundsbild**
Byt ut `bakgrund.jpg` till en egen bild som passar ditt tema.

### Nivå 2: fler bilder (enkelt)

**Uppgift 3: tre bilder i galleriet**
Lägg till totalt tre `<figure>`-block i galleriet. Varje bild ska ha en beskrivande `alt`-text och `<figcaption>`.

**Uppgift 4: styla bildtexterna**
Ge `figcaption` en egen `font-size`, ta bort `font-style: italic` om du vill, och testa en annan `color`.

### Nivå 3: tabellen och listan (medel)

**Uppgift 5: utöka pristabellen**
Lägg till minst två nya rader i tabellen (t.ex. "Helgpaket" och "VIP"). Lägg också till en kolumn "Inkluderar" som beskriver vad man får.

**Uppgift 6: fler listpunkter**
Utöka listan i info-sektionen till minst sex punkter. Använd `<strong>` för att markera det viktigaste ordet i varje punkt.

### Nivå 4: nya sektioner (avancerat)

**Uppgift 7: kontaktsektion**
Lägg till en ny sektion `<div class="kontakt">` med:
1. En `<h2>`-rubrik: "Kontakta oss".
2. Ett stycke med kontaktinfo.
3. En `<a class="knapp">` som leder till en e-postadress (t.ex. `mailto:info@camp.se`).

**Uppgift 8: styla nytt**
Ge `.kontakt`-sektionen en egen `background-color` och `padding`. Ge den en `border-radius` och `box-shadow` så den sticker ut från resten av sidan.

### Nivå 5: boss-nivån

**Uppgift 9: komplett affisch**
Bygg om hela sidan till en komplett affisch för ditt eget event. Den ska innehålla:

1. En hero-sektion med bakgrundsbild, stor rubrik (med `text-shadow` och `text-transform`), och minst en knapp.
2. En info-sektion med en lista.
3. Ett bildgalleri med minst tre `<figure>`.
4. En pristabell.
5. En kontaktsektion med minst en stilig länk.

**Uppgift 10: designutmaning**
Gör sidan så snygg som möjligt:

1. Välj ett eget Google Font och importera det.
2. Välj ett konsekvent färgtema (ändra knappar, tabellrubriker och bakgrunder).
3. Ge alla bilder `box-shadow` och `border-radius`.
4. Ge rubriker `text-shadow`.
5. Se till att allt är centrerat och ser bra ut.
