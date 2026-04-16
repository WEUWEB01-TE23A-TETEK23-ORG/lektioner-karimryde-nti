# Projekt – Min webbplats (3 sidor)

**Sammanfattning:** Bygg en flersidig webbplats med gemensam navigation, aktiv-markering och hover-effekter.

---

## Vad ska du göra?

Du ska skapa en webbplats med tre sidor länkade till varandra via en gemensam meny. Du väljer själv temat – ett band, en hobbyorganisation, ett fiktivt företag, en favoritfilm osv. Din uppgift är att:

- Välja tema och eget innehåll
- Kopiera menyn till alla tre sidor och flytta `.aktiv`-klassen rätt
- Välja egna färger med CSS-variabler

> **Kom ihåg:** Flytta `class="aktiv"` till rätt länk på varje sida!

---

## Scaffold – `index.html`

```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><!-- Din webbplatstitel --> – Hem</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <!-- MENY – kopiera denna exakt till sida2.html och sida3.html -->
    <!-- Flytta class="aktiv" till rätt länk på varje sida! -->
    <div class="meny">
        <a href="index.html" class="aktiv">Hem</a>
        <a href="sida2.html"><!-- Sidnamn 2, t.ex. "Om oss" --></a>
        <a href="sida3.html"><!-- Sidnamn 3, t.ex. "Kontakt" --></a>
    </div>

    <div class="kontainer">
        <h1><!-- Rubrik för startsidan --></h1>
        <!-- Byt ut src mot din bild. Spara bilden i mappen bilder/ -->
        <img src="bilder/din-bild.jpg" alt="<!-- Beskriv bilden -->">
        <p><!-- Skriv ett stycke om din webbplats här --></p>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

---

## Scaffold – `sida2.html`

```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><!-- Din webbplatstitel --> – <!-- Sidnamn 2 --></title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <!-- MENY – .aktiv är nu på den andra länken -->
    <div class="meny">
        <a href="index.html">Hem</a>
        <a href="sida2.html" class="aktiv"><!-- Sidnamn 2 --></a>
        <a href="sida3.html"><!-- Sidnamn 3 --></a>
    </div>

    <div class="kontainer">
        <h1><!-- Rubrik för sida 2 --></h1>
        <p><!-- Innehåll för sida 2 --></p>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

---

## Scaffold – `sida3.html`

```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><!-- Din webbplatstitel --> – <!-- Sidnamn 3 --></title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <!-- MENY – .aktiv är nu på den tredje länken -->
    <div class="meny">
        <a href="index.html">Hem</a>
        <a href="sida2.html"><!-- Sidnamn 2 --></a>
        <a href="sida3.html" class="aktiv"><!-- Sidnamn 3 --></a>
    </div>

    <div class="kontainer">
        <h1><!-- Rubrik för sida 3 --></h1>
        <p><!-- Innehåll för sida 3 --></p>
    </div>

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
    --meny-bg:   /* menyns bakgrundsfärg, t.ex. #1a1a2e */ ;
    --meny-text: /* menyns textfärg, t.ex. #e0e0e0 */ ;
    --aktiv-bg:  /* aktiv länks bakgrundsfärg, t.ex. #e94560 */ ;
    --hover-bg:  /* hover-bakgrundsfärg, t.ex. #16213e */ ;
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

/* Meny */
.meny {
    background-color: var(--meny-bg);
    padding: 10px;
}

.meny a {
    display: inline-block;
    color: var(--meny-text);
    text-decoration: none;
    padding: 10px 20px;
}

/* Hover-effekt */
.meny a:hover {
    background-color: var(--hover-bg);
}

/* Aktiv länk */
.meny a.aktiv {
    background-color: var(--aktiv-bg);
}

/* Innehållscontainer */
.kontainer {
    max-width: 800px;
    margin: auto;
    padding: 20px;
}

img {
    max-width: 100%;
    border-radius: 8px;
}
```

---

## Krav

Bocka av allt innan du lämnar in:

- [ ] Tre HTML-filer (`index.html`, `sida2.html`, `sida3.html`) länkade till varandra
- [ ] Gemensam `.meny` kopierad till alla sidor
- [ ] `.aktiv`-klass korrekt placerad på rätt länk på varje sida
- [ ] Hover-effekt på menylänkarna (`:hover`)
- [ ] CSS-variabler för menyns färger
- [ ] Eget innehåll på alla tre sidor

---

## Bonusutmaningar

⭐ **Lätt** – Lägg till en fjärde sida (t.ex. `sida4.html` med "Om mig" eller "Kontakt") och länka den i menyn på alla fyra sidor.

⭐⭐ **Medel** – Styla den aktiva länken med `border-bottom: 3px solid white` istället för bakgrundsfärg – ta bort `--aktiv-bg` och skriv en ny CSS-regel.

⭐⭐⭐ **Svår** – Lägg till en `<figure>` med `<figcaption>` på minst en sida och styla den med `border: 2px solid`, `border-radius: 8px` och `padding: 10px`.
