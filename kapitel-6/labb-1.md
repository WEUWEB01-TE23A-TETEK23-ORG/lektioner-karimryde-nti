# Labb 1 – bildrutnätet

Välkommen till CSS Grid! Här lär du dig placera element i ett rutnät — rader och kolumner som du styr med CSS.

## Introduktion och mål

I den här labben tränar du på att:

* Skapa en grid-layout med `display: grid`.
* Definiera kolumner med `grid-template-columns` och `1fr`.
* Styra avstånd med `gap`.
* Använda klassen `.rutnat` som grid-container och `.box` som grid-barn.
* Repetition: CSS-reset, `.kontainer`, CSS-variabler, klasser.

## Startkod

Skapa `index.html` och `style.css`. Lägg bilder i mappen `bilder/`.

**index.html:**

```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bildrutnätet</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="kontainer">
        <h1>Bildrutnätet</h1>
        <p class="intro">Ett galleri med CSS Grid.</p>

        <div class="rutnat">
            <div class="box">
                <img src="bilder/bild1.jpg" alt="Bild 1">
                <p>Bild 1</p>
            </div>
            <div class="box">
                <img src="bilder/bild2.jpg" alt="Bild 2">
                <p>Bild 2</p>
            </div>
            <div class="box">
                <img src="bilder/bild3.jpg" alt="Bild 3">
                <p>Bild 3</p>
            </div>
            <div class="box">
                <img src="bilder/bild4.jpg" alt="Bild 4">
                <p>Bild 4</p>
            </div>
            <div class="box">
                <img src="bilder/bild5.jpg" alt="Bild 5">
                <p>Bild 5</p>
            </div>
            <div class="box">
                <img src="bilder/bild6.jpg" alt="Bild 6">
                <p>Bild 6</p>
            </div>
        </div>
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

:root {
    --bakgrund: #f5f5f5;
    --text: #333;
    --accent: #6c5ce7;
    --kort-bg: #ffffff;
}

body {
    font-family: 'Segoe UI', sans-serif;
    background-color: var(--bakgrund);
    color: var(--text);
}

.kontainer {
    width: 900px;
    margin: auto;
    padding: 30px 20px;
}

h1 {
    text-align: center;
    color: var(--accent);
    margin-bottom: 5px;
}

.intro {
    text-align: center;
    color: #888;
    margin-bottom: 25px;
}

.rutnat {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 20px;
}

.box {
    background-color: var(--kort-bg);
    border-radius: 10px;
    padding: 10px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.box img {
    border-radius: 8px;
}

.box p {
    text-align: center;
    margin-top: 8px;
    font-weight: bold;
}
```

## Övningar och kodexempel

### Övning 1: grid-grunderna

`display: grid` gör en div till en grid-container. Alla barn hamnar i rutnätet:

```css
.rutnat {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;  /* Tre lika kolumner */
    gap: 20px;                            /* Avstånd mellan rutorna */
}
```

`1fr` betyder "en del av tillgängligt utrymme". Tre `1fr` = tre lika stora kolumner.

### Övning 2: ändra antal kolumner

Vill du ha två kolumner? Ändra till:

```css
grid-template-columns: 1fr 1fr;
```

Fyra kolumner:

```css
grid-template-columns: 1fr 1fr 1fr 1fr;
```

Eller med `repeat()`:

```css
grid-template-columns: repeat(4, 1fr);
```

## Uppgifter

### Nivå 1: uppvärmning (mycket enkelt)

**Uppgift 1: egna bilder**
Byt ut bilderna till dina egna. Ändra texterna under varje bild.

**Uppgift 2: två kolumner**
Ändra `grid-template-columns` till `1fr 1fr` och se hur layouten ändras.

### Nivå 2: ändra grid (enkelt)

**Uppgift 3: fyra kolumner**
Ändra till `grid-template-columns: repeat(4, 1fr)`. Lägg till fler boxar om det behövs.

**Uppgift 4: ändra gap**
Testa att ändra `gap` till `5px`, `30px` och `50px`. Vilken ser bäst ut?

### Nivå 3: styla korten (medel)

**Uppgift 5: hover-effekt**
Lägg till en hover-effekt på `.box`:

```css
.box {
    transition: 0.3s;
}

.box:hover {
    transform: scale(1.03);
    box-shadow: 0 6px 16px rgba(0, 0, 0, 0.2);
}
```

**Uppgift 6: figurer**
Byt ut `<img>` + `<p>` mot `<figure>` och `<figcaption>` i varje box.

(Repetition: `<figure>`, `<figcaption>` från kapitel 2!)

### Nivå 4: avancerad grid (avancerat)

**Uppgift 7: nio bilder**
Bygg ut galleriet till nio bilder (3 × 3) i tre kolumner.

**Uppgift 8: navigering**
Lägg till en navigeringsmeny ovanför galleriet med `display: flex` och `justify-content: space-between`. Styla med `:hover` och en accentfärg.

(Repetition: meny och hover från kapitel 4!)

### Nivå 5: boss-nivån

**Uppgift 9: blandade storlekar**
Skapa en grid med blandade kolumnbredder. T.ex. `grid-template-columns: 2fr 1fr 1fr` — den första kolumnen blir dubbelt så bred.

**Uppgift 10: komplett galleri-webbplats**
Bygg en galleri-webbplats med:

1. En meny med minst tre länkar.
2. Ett grid-galleri med minst nio bilder.
3. Hover-effekter på alla kort.
4. CSS-variabler för färgtema.
5. Google Font.
6. `<figure>` och `<figcaption>` i varje kort.
