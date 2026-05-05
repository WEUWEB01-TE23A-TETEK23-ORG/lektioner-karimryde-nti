# Projekt – Min reklamsida

**Sammanfattning:** Bygg en reklamsida för något du vill "sälja" – en plats, ett event, ett spel, en produkt eller något helt annat du hittar på.

---

## Vad ska du göra?

Du ska skapa en reklamsida med en stor hero-bild, en slogan och en länkknapp. Du får en färdig kodstruktur (scaffold) att utgå från. Din uppgift är att:

- Välja vad du vill "reklamiera" för
- Byta ut alla platshållare mot ditt eget innehåll
- Välja egna färger och bakgrundsbilder

---

## Scaffold – `index.html`

```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><!-- Byt ut mot din sidtitel, t.ex. "Kom till Fiji!" --></title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <!-- Hero-sektion med stor bakgrundsbild -->
    <div class="hero">
        <h1><!-- Din slogan i versaler, t.ex. "Upplev paradiset" --></h1>
        <p><!-- En kort beskrivning, 1–2 meningar --></p>
        <!-- Länkknappen: byt ut href och texten -->
        <a href="#" class="knapp"><!-- T.ex. "Läs mer" eller "Boka nu" --></a>
    </div>

    <!-- Produktbild med bildtext -->
    <figure>
        <!-- Byt ut src mot din egen bild. Spara bilden i mappen bilder/ -->
        <img src="bilder/din-bild.jpg" alt="<!-- Beskriv bilden -->">
        <figcaption><!-- En kort bildtext som beskriver vad bilden visar --></figcaption>
    </figure>

    <script src="script.js"></script>
</body>
</html>
```

---

## Scaffold – `style.css`

```css
body {
    margin: 0;
    font-family: sans-serif;
}

/* Hero-sektionen med stor bakgrundsbild */
.hero {
    /* Byt ut url() mot sökvägen till din bakgrundsbild, t.ex. bilder/strand.jpg */
    background-image: url(/* din bild, t.ex. bilder/strand.jpg */);
    background-size: cover;
    background-position: center;
    height: 400px;
}

.hero h1 {
    margin-top: 120px;
    margin-left: 60px;
    color: white;
    text-transform: uppercase;
    /* Gör texten lättare att läsa mot bakgrunden */
    text-shadow: 2px 2px 6px rgba(0, 0, 0, 0.7);
}

.hero p {
    margin-left: 60px;
    color: white;
    font-size: 1.2em;
}

/* Länkknapp – ser ut som en knapp */
.knapp {
    display: inline-block;
    text-decoration: none;
    padding: 12px 24px;
    background-color: /* din knappfärg, t.ex. #e63946 */ ;
    color: white;
    border-radius: 6px;
    margin-left: 60px;
    margin-top: 16px;
    font-weight: bold;
}

/* Svagt hover-sken på knappen */
.knapp:hover {
    opacity: 0.85;
}

/* Produktbild-sektion */
figure {
    margin-left: 60px;
    margin-top: 40px;
}

figure img {
    width: 300px;
    border-radius: 8px;
}

figcaption {
    color: /* din bildtextfärg, t.ex. #555 */ ;
    font-style: italic;
    margin-top: 6px;
}
```

---

## Krav

Bocka av allt innan du lämnar in:

- [ ] En hero-sektion (`.hero`) med bakgrundsbild via CSS
- [ ] Slogan i versaler med `text-transform: uppercase`
- [ ] En länkknapp med `text-decoration: none` och `padding`
- [ ] En `<figure>` med `<figcaption>`
- [ ] Text placerad med `margin-left` och `margin-top`
- [ ] Allt eget innehåll — inga platshållar-kommentarer kvar i det du visar

---

## Bonusutmaningar

⭐ **Lätt** – Lägg till en andra knapp med en annan bakgrundsfärg (t.ex. "Kontakta oss") bredvid den första.

⭐⭐ **Medel** – Lägg till `background-attachment: fixed` på `.hero` för en parallax-effekt när du scrollar.

⭐⭐⭐ **Svår** – Skapa tre `<figure>`-kort sida vid sida under hero-sektionen. Ge varje `<figure>` `display: inline-block` och lite `margin` så de hamnar på rad.
