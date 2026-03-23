# Labb 3 – komplett responsiv webbplats

Den stora finalen för HTML och CSS! Du bygger en komplett webbplats med Holy Grail-layout som fungerar på dator, surfplatta och mobil. Här kombinerar du allt från hela kursen.

## Introduktion och mål

I den här labben repeterar och kombinerar du **allt** från kapitel 1–7:

* HTML-struktur: rubriker, stycken, listor, bilder, tabeller, länkar.
* Bilder: `<figure>`, `<figcaption>`.
* Layout: `<div>`, klasser, `.kontainer`, CSS-reset, CSS-variabler.
* Navigation: `.aktiv`, `:hover`, `display: inline-block`.
* CSS Grid: `grid-template-columns`, `grid-template-areas`, `gap`.
* Responsiv: `@media`-queries, breakpoints.
* Styling: Google Fonts, `box-shadow`, `transition`, `linear-gradient`.

## Startkod

Skapa `index.html` och `style.css`. Lägg bilder i `bilder/`.

**index.html:**

```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mitt magasin</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="kontainer">
        <header>
            <div class="logo">📰 Magasinet</div>
            <nav>
                <a href="#" class="aktiv">Hem</a>
                <a href="#">Artiklar</a>
                <a href="#">Galleri</a>
                <a href="#">Om oss</a>
            </nav>
        </header>

        <main>
            <h2>Dagens artikel</h2>
            <figure>
                <img src="bilder/bild1.jpg" alt="Huvudbild">
                <figcaption>Foto: Bildbeskrivning</figcaption>
            </figure>
            <p>Skriv din artikeltext här. Berätta om något intressant!</p>
            <p>Fyll på med mer text, bilder och listor när du jobbar med uppgifterna.</p>
        </main>

        <aside>
            <h3>Populärt</h3>
            <ul>
                <li>Artikel 1</li>
                <li>Artikel 2</li>
                <li>Artikel 3</li>
            </ul>
        </aside>

        <footer>
            <p>&copy; 2026 Magasinet | Skapad med HTML &amp; CSS</p>
        </footer>
    </div>
</body>
</html>
```

**style.css:**

```css
/* CSS-reset */
html { box-sizing: border-box; }
*, *:before, *:after { box-sizing: inherit; }
body, h1, h2, h3, p, ul { margin: 0; padding: 0; }
img { width: 100%; }

@import url('https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700&family=Open+Sans:wght@400;600&display=swap');

:root {
    --bakgrund: #f9f9f9;
    --text: #333;
    --accent: #d35400;
    --sidhuvud-bg: #2c3e50;
    --sidebar-bg: #ecf0f1;
    --sidfot-bg: #2c3e50;
    --kort-bg: #ffffff;
}

body {
    font-family: 'Open Sans', sans-serif;
    background-color: var(--bakgrund);
    color: var(--text);
}

/* === DESKTOP === */
.kontainer {
    width: 1100px;
    margin: auto;

    display: grid;
    grid-template-columns: 3fr 1fr;
    grid-template-areas:
        "sidhuvud sidhuvud"
        "innehåll sidebar"
        "sidfot   sidfot";
    gap: 0;
}

/* Header */
header {
    grid-area: sidhuvud;
    background: linear-gradient(135deg, var(--sidhuvud-bg), #34495e);
    color: white;
    padding: 15px 25px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo {
    font-family: 'Merriweather', serif;
    font-size: 1.5rem;
    font-weight: bold;
}

header nav a {
    color: rgba(255,255,255,0.8);
    text-decoration: none;
    padding: 8px 15px;
    border-radius: 5px;
    transition: 0.2s;
}

header nav a:hover,
header nav .aktiv {
    background-color: var(--accent);
    color: white;
}

/* Main */
main {
    grid-area: innehåll;
    background-color: var(--kort-bg);
    padding: 30px;
}

main h2 {
    font-family: 'Merriweather', serif;
    color: var(--accent);
    margin-bottom: 15px;
}

main p {
    margin-bottom: 12px;
    line-height: 1.7;
}

main figure {
    margin: 0 0 20px 0;
}

main img {
    border-radius: 8px;
}

main figcaption {
    font-style: italic;
    color: #888;
    font-size: 0.85rem;
    margin-top: 5px;
}

/* Sidebar */
aside {
    grid-area: sidebar;
    background-color: var(--sidebar-bg);
    padding: 25px;
}

aside h3 {
    color: var(--accent);
    margin-bottom: 12px;
}

aside ul {
    list-style: none;
}

aside li {
    padding: 10px 0;
    border-bottom: 1px solid rgba(0,0,0,0.1);
}

/* Footer */
footer {
    grid-area: sidfot;
    background-color: var(--sidfot-bg);
    color: rgba(255,255,255,0.7);
    text-align: center;
    padding: 20px;
}

/* === SURFPLATTA (max-width: 1200px) === */
@media (max-width: 1200px) {
    .kontainer {
        width: 100%;
        padding: 0 10px;
    }
}

/* === LITEN SURFPLATTA (max-width: 768px) === */
@media (max-width: 768px) {
    .kontainer {
        grid-template-columns: 1fr;
        grid-template-areas:
            "sidhuvud"
            "innehåll"
            "sidebar"
            "sidfot";
    }
}

/* === MOBIL (max-width: 576px) === */
@media (max-width: 576px) {
    header {
        flex-direction: column;
        text-align: center;
        padding: 15px;
    }

    header nav {
        margin-top: 10px;
    }

    header nav a {
        display: block;
        margin-bottom: 5px;
    }

    main {
        padding: 20px 15px;
    }
}
```

## Uppgifter

Det finns inga övningar den här gången — du kan allt som behövs!

### Nivå 1: uppvärmning (mycket enkelt)

**Uppgift 1: eget innehåll**
Byt ut all text till ditt eget tema. Välj vad magasinet ska handla om (sport, teknik, mat, musik, mode...).

**Uppgift 2: testa responsivitet**
Öppna sidan och dra i fönstrets bredd. Kontrollera att layouten ändras vid 1200px, 768px och 576px.

### Nivå 2: fyll main-sektionen (enkelt)

**Uppgift 3: mer artikeltext**
Skriv minst tre stycken (`<p>`) i artikeln med riktig text (inte lorem ipsum).

**Uppgift 4: bilder**
Lägg till minst två `<figure>` med bilder och `<figcaption>` i `<main>`.

### Nivå 3: förbättra sidebaren (medel)

**Uppgift 5: riktiga länkar**
Gör sidebar-listan till riktiga `<a>`-taggar. Styla utan understrykning med hover-effekt som ändrar bakgrundsfärg.

**Uppgift 6: kontaktinfo i footer**
Utöka `<footer>` med mer innehåll: e-postlänk, adress, och eventuellt sociala medier-länkar.

### Nivå 4: nytt innehåll (avancerat)

**Uppgift 7: artikelgrid**
Lägg till en sektion i `<main>` med tre "relaterade artiklar" i ett eget grid bredvid varandra (`grid-template-columns: 1fr 1fr 1fr`). Varje artikel-kort ska ha en bild och rubrik.

Vid mobil (768px), ändra till en kolumn.

(Repetition: grid-kort från kapitel 6!)

**Uppgift 8: tabell i main**
Lägg till en tabell (t.ex. "Statistik", "Resultat" eller "Priser") i `<main>`. Styla med bakgrundsfärg på `<th>`.

(Repetition: tabeller från kapitel 1!)

### Nivå 5: boss-nivån

**Uppgift 9: hero-sektion**
Lägg till en hero-sektion mellan `<header>` och `<main>` med bakgrundsbild, `linear-gradient`-overlay, rubrik och en knapp. Uppdatera `grid-template-areas` för att inkludera en ny area `"hero"`.

**Uppgift 10: magasinet komplett**
Bygg din dröm-webbplats med allt du kan:

1. `<header>` med nav (.aktiv + hover).
2. Hero med bakgrundsbild och gradient-overlay.
3. `<main>` med artiklar, bilder, lista och tabell.
4. Artikelgrid med minst tre kort.
5. `<aside>` med populära länkar och hover.
6. `<footer>` med kontaktinfo.
7. Responsiv med tre breakpoints.
8. CSS-variabler, Google Font och konsekvent tema.
9. Sidan ska se bra ut på dator, surfplatta och mobil!
