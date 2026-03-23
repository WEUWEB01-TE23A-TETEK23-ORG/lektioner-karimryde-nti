# Labb 1 – namngivna grid-areas

I den här labben lär du dig "rita" din layout i CSS med `grid-template-areas`. Istället för att räkna kolumner och rader ger du varje del av sidan ett namn!

## Introduktion och mål

I den här labben tränar du på att:

* Skapa layout med `grid-template-areas` och namngivna areas.
* Namnge areas på svenska: `sidhuvud`, `innehåll`, `sidebar`, `sidfot`.
* Använda `grid-area` för att placera element i rätt area.
* Använda semantiska HTML-element: `<header>`, `<main>`, `<aside>`, `<footer>`.
* Repetition: `display: grid`, `1fr`, `gap`.

## Startkod

Skapa `index.html` och `style.css`.

**index.html:**

```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Grid areas</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="kontainer">
        <header>
            <h1>Min webbplats</h1>
            <nav>
                <a href="#" class="aktiv">Hem</a>
                <a href="#">Om</a>
                <a href="#">Kontakt</a>
            </nav>
        </header>

        <main>
            <h2>Välkommen!</h2>
            <p>Det här är huvudinnehållet på sidan. Här skulle artiklar, blogginlägg eller annan viktig information finnas.</p>
            <p>Med grid-template-areas kan vi "rita" vår layout direkt i CSS. Mycket enklare att förstå!</p>
        </main>

        <aside>
            <h3>Sidebar</h3>
            <ul>
                <li>Länk 1</li>
                <li>Länk 2</li>
                <li>Länk 3</li>
            </ul>
        </aside>

        <footer>
            <p>&copy; 2026 Min webbplats</p>
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

:root {
    --bakgrund: #f4f4f4;
    --accent: #2d6a4f;
    --sidhuvud-bg: #2d6a4f;
    --sidebar-bg: #d8f3dc;
    --sidfot-bg: #1b4332;
}

body {
    font-family: 'Segoe UI', sans-serif;
    background-color: var(--bakgrund);
}

.kontainer {
    width: 960px;
    margin: auto;

    display: grid;
    grid-template-columns: 3fr 1fr;
    grid-template-areas:
        "sidhuvud sidhuvud"
        "innehåll sidebar"
        "sidfot   sidfot";
    gap: 0;
}

header {
    grid-area: sidhuvud;
    background-color: var(--sidhuvud-bg);
    color: white;
    padding: 20px 25px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

header nav a {
    color: rgba(255,255,255,0.8);
    text-decoration: none;
    padding: 8px 15px;
    border-radius: 5px;
    transition: 0.2s;
}

header nav a:hover {
    background-color: rgba(255,255,255,0.2);
    color: white;
}

header nav .aktiv {
    background-color: rgba(255,255,255,0.2);
    color: white;
    font-weight: bold;
}

main {
    grid-area: innehåll;
    background-color: white;
    padding: 30px;
}

main h2 {
    color: var(--accent);
    margin-bottom: 15px;
}

main p {
    margin-bottom: 12px;
    line-height: 1.6;
}

aside {
    grid-area: sidebar;
    background-color: var(--sidebar-bg);
    padding: 25px;
}

aside h3 {
    color: var(--accent);
    margin-bottom: 10px;
}

aside ul {
    list-style: none;
}

aside li {
    padding: 8px 0;
    border-bottom: 1px solid rgba(0,0,0,0.1);
}

footer {
    grid-area: sidfot;
    background-color: var(--sidfot-bg);
    color: white;
    text-align: center;
    padding: 15px;
}
```

## Övningar och kodexempel

### Övning 1: hur grid-template-areas fungerar

Du "ritar" layouten i CSS med strängar. Varje rad är en sträng, varje ord är en area:

```css
.kontainer {
    display: grid;
    grid-template-columns: 3fr 1fr;
    grid-template-areas:
        "sidhuvud sidhuvud"     /* Rad 1: sidhuvud spänner över båda kolumnerna */
        "innehåll sidebar"     /* Rad 2: innehåll till vänster, sidebar till höger */
        "sidfot   sidfot";     /* Rad 3: sidfot spänner över båda kolumnerna */
}
```

### Övning 2: koppla element till areas

Varje element tilldelas sin area med `grid-area`:

```css
header  { grid-area: sidhuvud; }
main    { grid-area: innehåll; }
aside   { grid-area: sidebar; }
footer  { grid-area: sidfot; }
```

## Uppgifter

### Nivå 1: uppvärmning (mycket enkelt)

**Uppgift 1: eget innehåll**
Byt ut all text på sidan till eget innehåll — ändra rubrik, stycken och sidebarlänkar.

**Uppgift 2: ändra färgtema**
Byt ut alla CSS-variabler i `:root` till ett nytt tema.

### Nivå 2: ändra layouten (enkelt)

**Uppgift 3: sidebar till vänster**
Ändra `grid-template-areas` så att sidebar hamnar till vänster:

```css
grid-template-areas:
    "sidhuvud sidhuvud"
    "sidebar  innehåll"
    "sidfot   sidfot";
```

Ändra även `grid-template-columns` till `1fr 3fr`.

**Uppgift 4: bredare sidebar**
Ändra `grid-template-columns` till `2fr 1fr`. Se hur proportionerna ändras.

### Nivå 3: mer innehåll (medel)

**Uppgift 5: bild i main**
Lägg till en `<figure>` med bild och `<figcaption>` i `<main>`. Ge bilden `width: 100%` och `border-radius`.

(Repetition: `<figure>`, `<figcaption>` från kapitel 2!)

**Uppgift 6: fler sidebarlänkar**
Gör sidebar-listan till riktiga `<a>`-taggar. Styla utan understrykning och med en hover-effekt som ändrar bakgrundsfärg.

### Nivå 4: extra sektioner (avancerat)

**Uppgift 7: tre kolumner**
Ändra layouten till tre kolumner:

```css
grid-template-columns: 1fr 3fr 1fr;
grid-template-areas:
    "sidhuvud  sidhuvud  sidhuvud"
    "sidebar   innehåll  sidopanel"
    "sidfot    sidfot    sidfot";
```

Skapa ett nytt `<aside>`-element för den högra sidopanelen och ge det `grid-area: sidopanel`.

**Uppgift 8: mer i main**
Fyll `<main>` med rikare innehåll: minst tre stycken, en bild, en lista och en tabell.

### Nivå 5: boss-nivån

**Uppgift 9: helt egen layout**
Rita en egen layout med `grid-template-areas`. Den ska ha minst fyra areas (t.ex. sidhuvud, nav, innehåll, sidfot) och unika proportioner.

**Uppgift 10: webbplatsen komplett**
Bygg en komplett webbplats med grid-areas:

1. `<header>` med navigation (`.aktiv` + hover).
2. `<main>` med minst tre stycken, bilder och en lista.
3. `<aside>` med sidolänkar.
4. `<footer>` med kontaktinformation.
5. CSS-variabler, Google Font och `box-shadow`.
6. Alla areas är namngivna på svenska.
