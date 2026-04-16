# Projekt – Min responsiva tidning

**Sammanfattning:** Bygg en responsiv layoutsida med `grid-template-areas`, semantiska element och media queries.

---

## Vad ska du göra?

Du ska skapa en responsiv sida som ser ut som en tidning eller nyhetssida. Du väljer själv temat – sport, gaming, musik, mode, mat eller något annat! Du får en färdig kodstruktur (scaffold) att utgå från. Din uppgift är att:

- Välja tema och eget innehåll
- Byta ut alla platshållare mot dina egna texter
- Välja egna färger med CSS-variabler
- Testa att sidan ser bra ut både på stor och liten skärm

---

## Scaffold – `index.html`

```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><!-- Din tidnings namn, t.ex. "Gaming News" --></title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <!-- Sidhuvud med tidningens namn och navigation -->
    <header class="sidhuvud">
        <h1><!-- Tidningens namn --></h1>
        <nav>
            <a href="#"><!-- Avdelning 1, t.ex. "Nyheter" --></a>
            <a href="#"><!-- Avdelning 2, t.ex. "Recensioner" --></a>
            <a href="#"><!-- Avdelning 3, t.ex. "Om oss" --></a>
        </nav>
    </header>

    <!-- Grid-wrapper för innehåll och sidebar -->
    <div class="wrapper">

        <!-- Huvudinnehåll -->
        <main class="innehall">
            <h2><!-- Rubrik för huvudartikeln --></h2>
            <p><!-- Stycke 1 – inledning av artikeln --></p>
            <p><!-- Stycke 2 – mer innehåll --></p>
            <p><!-- Stycke 3 – avslutning --></p>
        </main>

        <!-- Sidopanel -->
        <aside class="sidebar">
            <h3><!-- Sidopanelens rubrik, t.ex. "Relaterat" eller "Topplistor" --></h3>
            <ul>
                <li><!-- Punkt 1 --></li>
                <li><!-- Punkt 2 --></li>
                <li><!-- Punkt 3 --></li>
            </ul>
        </aside>

    </div><!-- slut .wrapper -->

    <!-- Sidfot -->
    <footer class="sidfot">
        <p><!-- Copyright-text, t.ex. "© 2025 Gaming News" --></p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

---

## Scaffold – `style.css`

```css
/* =====================================================
   CSS-VARIABLER – Byt ut färgerna mot din palett
   ===================================================== */
:root {
    --sidhuvud-bg:  /* sidhuvudets bakgrundsfärg, t.ex. #1a1a2e */ ;
    --sidhuvud-text: /* sidhuvudets textfärg, t.ex. #ffffff */ ;
    --innehall-bg:  /* huvudinnehållets bakgrundsfärg, t.ex. #ffffff */ ;
    --sidebar-bg:   /* sidopanelens bakgrundsfärg, t.ex. #f0f0f0 */ ;
    --sidfot-bg:    /* sidfotens bakgrundsfärg, t.ex. #1a1a2e */ ;
    --sidfot-text:  /* sidfotens textfärg, t.ex. #ffffff */ ;
    --accent:       /* accentfärg för rubriker, t.ex. #e94560 */ ;
}

/* CSS-reset */
*, *::before, *::after {
    box-sizing: border-box;
}

body {
    margin: 0;
    padding: 0;
    font-family: sans-serif;
}

h1, h2, h3, p, ul {
    margin: 0;
    padding: 0;
}

/* Sidhuvud */
.sidhuvud {
    background-color: var(--sidhuvud-bg);
    color: var(--sidhuvud-text);
    padding: 20px 40px;
}

.sidhuvud h1 {
    font-size: 2em;
    margin-bottom: 10px;
}

/* Navigation i sidhuvudet */
.sidhuvud nav {
    display: flex;
    gap: 16px;
}

.sidhuvud nav a {
    color: var(--sidhuvud-text);
    text-decoration: none;
    padding: 6px 12px;
}

.sidhuvud nav a:hover {
    background-color: var(--accent);
    border-radius: 4px;
}

/* Grid-wrapper – desktop: två kolumner */
.wrapper {
    display: grid;
    grid-template-columns: 3fr 1fr;
    grid-template-areas: "innehall sidebar";
    gap: 20px;
    max-width: 1100px;
    margin: auto;
    padding: 20px;
}

/* Koppla grid-areas till elementen */
.innehall {
    grid-area: innehall;
    background-color: var(--innehall-bg);
    padding: 20px;
    border-radius: 8px;
}

.innehall h2 {
    color: var(--accent);
    margin-bottom: 16px;
}

.innehall p {
    margin-bottom: 12px;
    line-height: 1.6;
}

.sidebar {
    grid-area: sidebar;
    background-color: var(--sidebar-bg);
    padding: 20px;
    border-radius: 8px;
}

.sidebar h3 {
    color: var(--accent);
    margin-bottom: 12px;
}

.sidebar ul {
    list-style: disc;
    padding-left: 20px;
}

.sidebar li {
    margin-bottom: 8px;
}

/* Sidfot */
.sidfot {
    background-color: var(--sidfot-bg);
    color: var(--sidfot-text);
    text-align: center;
    padding: 20px;
    margin-top: 20px;
}

/* =====================================================
   MEDIA QUERIES – gör sidan responsiv
   ===================================================== */

/* Surfplatta (max 768px) – en kolumn, sidebar under innehållet */
@media (max-width: 768px) {
    .wrapper {
        grid-template-columns: 1fr;
        grid-template-areas:
            "innehall"
            "sidebar";
    }
}

/* Mobil (max 480px) – mindre text och padding */
@media (max-width: 480px) {
    .sidhuvud {
        padding: 12px 16px;
    }

    .sidhuvud h1 {
        font-size: 1.4em;
    }

    .sidhuvud nav {
        flex-direction: column;
        gap: 8px;
    }

    .wrapper {
        padding: 10px;
        gap: 10px;
    }

    .innehall,
    .sidebar {
        padding: 12px;
    }
}
```

---

## Krav

Bocka av allt innan du lämnar in:

- [ ] Korrekt `grid-template-areas` med svenska namn (`innehall`, `sidebar`)
- [ ] Alla fyra semantiska element: `<header>`, `<main>`, `<aside>`, `<footer>`
- [ ] Minst två breakpoints med `@media`
- [ ] Sidan ser bra ut i desktop, surfplatta och mobilläge
- [ ] CSS-variabler för alla färger
- [ ] Eget innehåll – inga platshållar-kommentarer kvar i det du visar

---

## Bonusutmaningar

⭐ **Lätt** – Lägg till `background-attachment: fixed` på `body` med en bakgrundsbild och anpassa textfärgerna så allt är läsbart.

⭐⭐ **Medel** – Lägg till en `<figure>` med en bild och `<figcaption>` inuti `.innehall`. Styla den med `float: right`, `width: 40%`, `margin-left: 20px` och `border-radius: 8px` så att texten flödar runt bilden.

⭐⭐⭐ **Svår** – Lägg till en tredje media query för `max-width: 1200px` som ändrar kolumnproportion till `2fr 1fr`. Dölj dessutom sidopanelen helt på mobil (`display: none` i 480px-breakpointen) och visa ett meddelande i sidfoten istället.
