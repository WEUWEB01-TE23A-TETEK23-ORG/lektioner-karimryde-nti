# Labb 2 – filmkorten

I den här labben bygger du produktkort i ett CSS Grid — som en Netflix- eller Spotify-sida! Du lär dig animerade hover-effekter med `transition` och `linear-gradient`.

## Introduktion och mål

I den här labben tränar du på att:

* Skapa snygga produktkort i grid-layout.
* Använda `transition` för mjuka animationer.
* Skapa gradient-bakgrunder med `linear-gradient()`.
* Kombinera `.rutnat` och `.box` med hover-effekter.
* Repetition: `display: grid`, `grid-template-columns`, `gap`, CSS-variabler.

## Startkod

Skapa `index.html` och `style.css`. Lägg filmaffischer i `bilder/`.

**index.html:**

```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Filmkorten</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="kontainer">
        <h1>🎬 Topplistan</h1>
        <p class="intro">Mina favoritfilmer just nu</p>

        <div class="rutnat">
            <div class="box">
                <img src="bilder/film1.jpg" alt="Film 1">
                <div class="info">
                    <h3>Film 1</h3>
                    <p>Action / Äventyr</p>
                    <span class="betyg">⭐ 8.5</span>
                </div>
            </div>

            <div class="box">
                <img src="bilder/film2.jpg" alt="Film 2">
                <div class="info">
                    <h3>Film 2</h3>
                    <p>Komedi / Drama</p>
                    <span class="betyg">⭐ 7.2</span>
                </div>
            </div>

            <div class="box">
                <img src="bilder/film3.jpg" alt="Film 3">
                <div class="info">
                    <h3>Film 3</h3>
                    <p>Science Fiction</p>
                    <span class="betyg">⭐ 9.0</span>
                </div>
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
    --bakgrund: #0d1117;
    --text: #e6e6e6;
    --accent: #ff6b6b;
    --kort-bg: #161b22;
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
    text-align: center;
    margin-bottom: 5px;
}

.intro {
    text-align: center;
    color: #666;
    margin-bottom: 30px;
}

.rutnat {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 25px;
}

.box {
    background-color: var(--kort-bg);
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
    transition: 0.3s;
}

.box:hover {
    transform: translateY(-8px);
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.6);
}

.box img {
    transition: 0.3s;
}

.box:hover img {
    opacity: 0.85;
}

.info {
    padding: 15px;
}

.info h3 {
    margin-bottom: 5px;
}

.info p {
    color: #888;
    font-size: 0.9rem;
}

.betyg {
    display: inline-block;
    margin-top: 8px;
    color: var(--accent);
    font-weight: bold;
}
```

## Övningar och kodexempel

### Övning 1: transition

`transition` gör ändringar mjuka istället för plötsliga:

```css
.box {
    transition: 0.3s;  /* Alla ändringar animeras på 0.3 sekunder */
}

.box:hover {
    transform: translateY(-8px);  /* Kortet "lyfter" uppåt */
}
```

### Övning 2: linear-gradient

Skapa en gradient-bakgrund (en färg som övergår till en annan):

```css
body {
    background: linear-gradient(135deg, #0d1117, #1a1a2e);
}
```

Kan kombineras med hover:

```css
.box:hover {
    background: linear-gradient(135deg, var(--kort-bg), #1f2937);
}
```

## Uppgifter

### Nivå 1: uppvärmning (mycket enkelt)

**Uppgift 1: egna filmer**
Byt ut filmnamnen, genrerna och betygen till dina egna favoriter.

**Uppgift 2: egna bilder**
Lägg in egna filmaffischer (eller valfria bilder) i `bilder/` och uppdatera `src`.

### Nivå 2: fler kort (enkelt)

**Uppgift 3: sex filmkort**
Lägg till tre filmkort till så det blir sex totalt (två rader med tre kort).

**Uppgift 4: ändra hover**
Ändra hover-effekten: testa `transform: scale(1.05)` istället för `translateY`. Vilken gillar du bäst?

### Nivå 3: gradienter (medel)

**Uppgift 5: gradient på body**
Byt ut `background-color` på body mot en `linear-gradient`. Testa t.ex.:

```css
body {
    background: linear-gradient(to bottom, #0d1117, #1a1a2e);
    min-height: 100vh;
}
```

**Uppgift 6: gradient på kort vid hover**
Lägg till en gradient på `.box:hover`:

```css
.box:hover {
    background: linear-gradient(135deg, #1e293b, #334155);
}
```

### Nivå 4: navigering och struktur (avancerat)

**Uppgift 7: navigeringsmeny**
Lägg till en meny ovanför galleriet (t.ex. "Alla", "Action", "Komedi"). Styla den med `display: flex` och `justify-content: space-between`.

(Repetition: navigering och hover från kapitel 4!)

**Uppgift 8: mer info på korten**
Lägg till fler element i `.info`: t.ex. årtal, regissör eller en länk till trailer (stilad utan understrykning med accentfärg).

### Nivå 5: boss-nivån

**Uppgift 9: tolv filmkort**
Bygg ut till tolv kort (fyra rader). Testa med `grid-template-columns: repeat(4, 1fr)` för fyra kolumner.

**Uppgift 10: streamingtjänsten**
Gör sidan till en komplett streamingtjänst:

1. En meny med kategorier.
2. Minst åtta filmkort med bilder, titel, genre och betyg.
3. Hover-effekt med `transition` och `transform`.
4. Gradient-bakgrund på body.
5. CSS-variabler för hela färgtemat.
6. Google Font.
