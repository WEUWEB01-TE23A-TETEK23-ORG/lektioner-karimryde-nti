# Projekt – Min blogg eller portfolio

**Sammanfattning:** Bygg en blogg eller portfolio med tre inlägg/projekt, CSS-variabler och flexbox.

---

## Vad ska du göra?

Du ska skapa en sida med tre innehållsboxar – antingen som blogginlägg om ett intresse, eller som en portfolio med tre "projekt" du visat upp. Du får en färdig kodstruktur (scaffold) att utgå från. Din uppgift är att:

- Välja ett tema (blogg eller portfolio)
- Hämta en färgpalett på [Coolors.co](https://coolors.co/) och använda den som CSS-variabler
- Byta ut alla platshållare mot ditt eget innehåll

---

## Scaffold – `index.html`

```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><!-- Din sidtitel, t.ex. "Min blogg" eller "Min portfolio" --></title>
    <!-- Byt ut Google Fonts-länken mot ett typsnitt du gillar: https://fonts.google.com -->
    <link href="https://fonts.googleapis.com/css2?family=Lato&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <div class="kontainer">

        <h1><!-- Din blogg/portfolio-rubrik --></h1>

        <!-- Flex-rad som håller inläggen sida vid sida -->
        <div class="flex-rad">

            <!-- Inlägg 1 -->
            <div class="inlagg" id="inlagg-1">
                <h2><!-- Rubrik för inlägg 1 --></h2>
                <span class="datum"><!-- Datum, t.ex. 14 april 2025 --></span>
                <p><!-- Skriv ditt innehåll här --></p>
            </div>

            <!-- Inlägg 2 -->
            <div class="inlagg" id="inlagg-2">
                <h2><!-- Rubrik för inlägg 2 --></h2>
                <span class="datum"><!-- Datum --></span>
                <p><!-- Skriv ditt innehåll här --></p>
            </div>

            <!-- Inlägg 3 -->
            <div class="inlagg" id="inlagg-3">
                <h2><!-- Rubrik för inlägg 3 --></h2>
                <span class="datum"><!-- Datum --></span>
                <p><!-- Skriv ditt innehåll här --></p>
            </div>

        </div><!-- slut .flex-rad -->

        <!-- Topp-3 lista med <ol> -->
        <h2><!-- Rubrik för din topp-3 lista, t.ex. "Mina tre favoriter" --></h2>
        <ol>
            <li><!-- Favoritpunkt 1 --></li>
            <li><!-- Favoritpunkt 2 --></li>
            <li><!-- Favoritpunkt 3 --></li>
        </ol>

    </div><!-- slut .kontainer -->

    <script src="script.js"></script>
</body>
</html>
```

---

## Scaffold – `style.css`

```css
/* Byt ut Google Fonts-importen om du valde ett annat typsnitt */
@import url('https://fonts.googleapis.com/css2?family=Lato&display=swap');

/* =====================================================
   CSS-VARIABLER – Hämta din färgpalett från coolors.co
   och byt ut färgerna nedan mot din palett
   ===================================================== */
:root {
    --primary: /* din primärfärg, t.ex. #264653 */ ;
    --accent:  /* din accentfärg, t.ex. #e9c46a */ ;
    --bakgrund: /* din bakgrundsfärg, t.ex. #f4f1de */ ;
    --text:    /* din textfärg, t.ex. #2d2d2d */ ;
}

/* CSS-reset */
*, *::before, *::after {
    box-sizing: border-box;
}

body {
    margin: 0;
    padding: 0;
    background-color: var(--bakgrund);
    font-family: 'Lato', sans-serif;
    color: var(--text);
}

h1, h2, h3, h4, h5, h6, p, ul, ol {
    margin: 0;
    padding: 0;
}

/* Centreringscontainer */
.kontainer {
    max-width: 900px;
    margin: auto;
    padding: 20px;
}

/* Flex-rad som ställer inläggen bredvid varandra */
.flex-rad {
    display: flex;
    gap: 20px;
    margin-bottom: 30px;
}

/* Enstaka inlägg/projekt-box */
.inlagg {
    background-color: var(--primary);
    color: white;
    padding: 20px;
    border-radius: 8px;
    flex: 1; /* Alla boxar tar lika mycket plats */
}

.inlagg h2 {
    margin-bottom: 8px;
}

/* Datum-styling med accentfärgen */
.datum {
    color: var(--accent);
    font-size: 0.9em;
    display: block;
    margin-bottom: 10px;
}

ol {
    margin-top: 10px;
    padding-left: 20px;
}

li {
    margin-bottom: 6px;
    list-style-type: decimal;
}
```

---

## Krav

Bocka av allt innan du lämnar in:

- [ ] CSS-reset (`box-sizing: border-box`, nollställd margin/padding)
- [ ] Minst tre CSS-variabler i `:root` (hämtade från Coolors.co)
- [ ] Minst tre `.inlagg`-boxar med eget innehåll
- [ ] `display: flex` för att rada upp inläggen
- [ ] En `<ol>` med minst tre punkter
- [ ] `.datum`-klass på alla datumtexter
- [ ] Allt eget innehåll — inga platshållar-kommentarer kvar i det du visar

---

## Bonusutmaningar

⭐ **Lätt** – Lägg till `background-attachment: fixed` på `body` med en bakgrundsbild (och justera textfärgen så den är läsbar).

⭐⭐ **Medel** – Lägg till en fjärde CSS-variabel `--rubrik` i `:root` och använd den som `color` på alla `h2`-rubriker inuti `.inlagg`. Ändra variabelns värde och se hur alla rubriker uppdateras på en gång.

⭐⭐⭐ **Svår** – Lägg till en `<nav>` högst upp med tre ankarlänkar (`<a href="#inlagg-1">`, `<a href="#inlagg-2">`, `<a href="#inlagg-3">`) och styla den med `display: flex` och `gap`. Se till att länkarna scrollar till rätt inlägg.
