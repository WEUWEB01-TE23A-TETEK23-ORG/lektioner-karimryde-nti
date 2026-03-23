# Labb 3 – bildgalleriet med flex

Den här labben kombinerar allt från kapitel 3! Du bygger ett bildgalleri där bilderna ligger bredvid varandra med `display: flex`.

## Introduktion och mål

I den här labben tränar du på att:

* Placera element bredvid varandra med `display: flex`.
* Kombinera flex med klasser (`.rutnat`, `.box`).
* Repetition: CSS-reset, `.kontainer`, `:root`-variabler, klasser.
* Repetition: `<figure>`, `<figcaption>`, bilder, box-shadow.

## Startkod

Skapa `index.html` och `style.css`. Lägg bilder i mappen `bilder/` (minst tre stycken).

**index.html:**

```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bildgalleriet</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="kontainer">
        <h1>Bildgalleriet</h1>
        <p class="intro">En samling av mina bästa bilder.</p>

        <div class="rutnat">
            <div class="box">
                <img src="bilder/bild1.jpg" alt="Bild 1">
                <h3>Bild 1</h3>
                <p>En kort beskrivning.</p>
            </div>
            <div class="box">
                <img src="bilder/bild2.jpg" alt="Bild 2">
                <h3>Bild 2</h3>
                <p>En kort beskrivning.</p>
            </div>
            <div class="box">
                <img src="bilder/bild3.jpg" alt="Bild 3">
                <h3>Bild 3</h3>
                <p>En kort beskrivning.</p>
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
    --bakgrund: #1a1a2e;
    --text: #e0e0e0;
    --accent: #e94560;
    --kort-bg: #16213e;
}

body {
    font-family: 'Segoe UI', sans-serif;
    background-color: var(--bakgrund);
    color: var(--text);
}

.kontainer {
    width: 900px;
    margin: auto;
    padding: 40px 20px;
}

h1 {
    color: var(--accent);
    text-align: center;
    margin-bottom: 5px;
}

.intro {
    text-align: center;
    color: #888;
    margin-bottom: 30px;
}

.rutnat {
    display: flex;
    gap: 20px;
}

.box {
    background-color: var(--kort-bg);
    border-radius: 10px;
    padding: 15px;
    width: 50%;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
}

.box img {
    border-radius: 8px;
    margin-bottom: 10px;
}

.box h3 {
    color: var(--accent);
    margin-bottom: 5px;
}
```

## Övningar och kodexempel

### Övning 1: display flex

`display: flex` placerar barnelement bredvid varandra:

```css
.rutnat {
    display: flex;
    gap: 20px;
}
```

`gap` lägger till avstånd mellan elementen.

### Övning 2: lika bredd

Ge alla barn samma bredd med procent:

```css
.box {
    width: 50%;  /* Ger plats för två bredvid varandra */
}
```

Med tre boxar, använd `width: 33%` eller ta bort `width` helt och låt flex fördela.

## Uppgifter

### Nivå 1: uppvärmning (mycket enkelt)

**Uppgift 1: egna bilder**
Byt ut bilderna till dina egna. Ändra rubrikerna och beskrivningarna.

**Uppgift 2: ändra färgtema**
Gå till [Coolors.co](https://coolors.co/) och generera en ny palett. Byt ut värdena i `:root`.

### Nivå 2: utöka galleriet (enkelt)

**Uppgift 3: fyra bilder**
Lägg till en fjärde `.box`. Justera `width` om det behövs (testa utan fast bredd).

**Uppgift 4: hover-effekt**
Lägg till en hover-effekt på `.box`:

```css
.box:hover {
    transform: scale(1.02);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);
}
```

Lägg också till `transition: 0.3s` på `.box` för mjuk animation.

### Nivå 3: kombinera koncept (medel)

**Uppgift 5: figure istället för img**
Byt ut `<img>` + `<h3>` + `<p>` mot en `<figure>` med `<figcaption>` i varje box.

(Repetition: `<figure>`, `<figcaption>` från kapitel 2!)

**Uppgift 6: länk under varje bild**
Lägg till en `<a>`-länk i varje box som går till bildkällan. Styla den utan understrykning med en accentfärg.

(Repetition: stilade länkar från kapitel 2!)

### Nivå 4: extra sektioner (avancerat)

**Uppgift 7: två rader**
Skapa en andra `.rutnat`-div med tre nya boxar under den första. Nu har du ett galleri med sex bilder i två rader.

**Uppgift 8: rubriksektion**
Lägg till en hero-sektion ovanför galleriet med bakgrundsbild, stor rubrik och `text-shadow`. Använd `text-transform: uppercase` på rubriken.

(Repetition: bakgrundsbild, `text-shadow`, `text-transform` från kapitel 1–2!)

### Nivå 5: boss-nivån

**Uppgift 9: nio bilder**
Bygg ett galleri med nio bilder i tre rader (tre `.rutnat`-divs med tre boxar vardera). Ge varje rad ett eget tema eller kategori.

**Uppgift 10: portfolio**
Bygg om sidan till en portfolio-sida:

1. Hero-sektion med bakgrundsbild och ditt namn.
2. Galleri-sektion med minst sex bilder i flex-layout.
3. Varje bild ska ha en rubrik, beskrivning och länk.
4. Alla kort ska ha hover-effekt och `box-shadow`.
5. Använd CSS-variabler för hela färgtemat.
6. Importera ett Google Font.
