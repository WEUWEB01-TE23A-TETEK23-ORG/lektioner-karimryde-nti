# Projekt – Mitt rutnät

**Sammanfattning:** Bygg en kortgrid med CSS Grid, hover-animationer och transition.

---

## Vad ska du göra?

Du ska skapa en sida med sex kort placerade i ett rutnät. Du väljer själv temat – favoritfilmer, maträtter, städer, spel, djur eller något annat! Du får en färdig kodstruktur (scaffold) att utgå från. Din uppgift är att:

- Välja tema och eget innehåll
- Byta ut alla platshållare mot dina egna bilder, rubriker och texter
- Välja egna färger

---

## Scaffold – `index.html`

```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><!-- Din sidtitel, t.ex. "Mina favoritfilmer" --></title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <h1><!-- Rubrik för sidan, t.ex. "Mina favoritfilmer" --></h1>

    <div class="rutnat">

        <!-- Kort 1 – byt ut bild, rubrik och text -->
        <div class="box">
            <img src="bilder/bild1.jpg" alt="<!-- Beskriv bilden -->">
            <h3><!-- Kortets rubrik --></h3>
            <p><!-- Kortets text --></p>
        </div>

        <!-- Kort 2 – byt ut bild, rubrik och text -->
        <div class="box">
            <img src="bilder/bild2.jpg" alt="<!-- Beskriv bilden -->">
            <h3><!-- Kortets rubrik --></h3>
            <p><!-- Kortets text --></p>
        </div>

        <!-- Kort 3 – byt ut bild, rubrik och text -->
        <div class="box">
            <img src="bilder/bild3.jpg" alt="<!-- Beskriv bilden -->">
            <h3><!-- Kortets rubrik --></h3>
            <p><!-- Kortets text --></p>
        </div>

        <!-- Kort 4 – byt ut bild, rubrik och text -->
        <div class="box">
            <img src="bilder/bild4.jpg" alt="<!-- Beskriv bilden -->">
            <h3><!-- Kortets rubrik --></h3>
            <p><!-- Kortets text --></p>
        </div>

        <!-- Kort 5 – byt ut bild, rubrik och text -->
        <div class="box">
            <img src="bilder/bild5.jpg" alt="<!-- Beskriv bilden -->">
            <h3><!-- Kortets rubrik --></h3>
            <p><!-- Kortets text --></p>
        </div>

        <!-- Kort 6 – byt ut bild, rubrik och text -->
        <div class="box">
            <img src="bilder/bild6.jpg" alt="<!-- Beskriv bilden -->">
            <h3><!-- Kortets rubrik --></h3>
            <p><!-- Kortets text --></p>
        </div>

    </div><!-- slut .rutnat -->

    <script src="script.js"></script>
</body>
</html>
```

---

## Scaffold – `style.css`

```css
body {
    margin: 0;
    padding: 20px;
    background-color: /* din bakgrundsfärg, t.ex. #f5f5f5 */ ;
    font-family: sans-serif;
}

h1 {
    text-align: center;
    margin-bottom: 30px;
    color: /* din rubrikfärg */ ;
}

/* Rutnätslayout */
.rutnat {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 20px;
    max-width: 1000px;
    margin: auto;
    padding: 20px;
}

/* Enstaka kort */
.box {
    background-color: /* din kortfärg, t.ex. #ffffff */ ;
    border-radius: 10px;
    overflow: hidden;
    /* transition gör att hover-effekten animeras mjukt */
    transition: transform 0.3s;
}

/* Hover-effekt – kortet lyfter lite */
.box:hover {
    transform: scale(1.03);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
}

/* Bilden fyller kortets bredd och har fast höjd */
.box img {
    width: 100%;
    height: 180px;
    object-fit: cover;
}

/* Rubrik och text inuti kortet */
.box h3 {
    padding: 0 16px;
    margin-top: 12px;
    color: /* din kortrubriks-färg */ ;
}

.box p {
    padding: 0 16px 16px 16px;
    color: /* din korttext-färg */ ;
    font-size: 0.9em;
}
```

---

## Krav

Bocka av allt innan du lämnar in:

- [ ] Minst sex kort i ett grid med tre kolumner
- [ ] `gap` mellan korten
- [ ] Hover-effekt med `transition` och `transform: scale()`
- [ ] Varje kort har bild (`<img>`), rubrik (`<h3>`) och text (`<p>`)
- [ ] Eget tema – inga platshållar-kommentarer kvar i det du visar

---

## Bonusutmaningar

⭐ **Lätt** – Byt `1fr 1fr 1fr` mot `repeat(3, 1fr)` i `grid-template-columns` – samma resultat men snyggare kod.

⭐⭐ **Medel** – Lägg till en `linear-gradient`-overlay som visas vid hover. Exempel: ändra `.box:hover` att ha `background: linear-gradient(to bottom, transparent, rgba(0,0,0,0.5))` – eller lägg en halvtransparent gradient som bakgrund på `.box h3`.

⭐⭐⭐ **Svår** – Gör gridet responsivt genom att byta `grid-template-columns: 1fr 1fr 1fr` mot `grid-template-columns: repeat(auto-fit, minmax(250px, 1fr))`. Testa att dra ihop webbläsarfönstret – korten ska automatiskt byta till en eller två kolumner.
