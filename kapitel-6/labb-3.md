# Labb 3 – restaurangmenyn

I den här labben bygger du en restaurangs menysida med en avancerad grid-layout. Du kombinerar allt från kapitel 6 och tränar på nested grid (grid inuti grid).

## Introduktion och mål

I den här labben tränar du på att:

* Använda nested grid (grid inuti grid) för kortens inre layout.
* Använda `grid-template-rows` för att styra vertikala proportioner.
* Kombinera grid med `transition`, `linear-gradient` och hover-effekter.
* Repetition: `display: grid`, `grid-template-columns`, `gap`, `.rutnat`, `.box`.
* Repetition: CSS-variabler, navigering, klasser.

## Startkod

Skapa `index.html` och `style.css`. Lägg matbilder i `bilder/`.

**index.html:**

```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Restaurangmenyn</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="kontainer">
        <nav class="meny">
            <span class="logo">🍽️ La Pasta</span>
            <div class="nav-lankar">
                <a href="#" class="aktiv">Meny</a>
                <a href="#">Om oss</a>
                <a href="#">Kontakt</a>
            </div>
        </nav>

        <div class="hero">
            <h1>Vår meny</h1>
            <p>Handgjord pasta med kärlek sedan 1998</p>
        </div>

        <h2 class="kategori">Förrätter</h2>
        <div class="rutnat">
            <div class="box">
                <img src="bilder/ratt1.jpg" alt="Bruschetta">
                <div class="ratt-info">
                    <h3>Bruschetta</h3>
                    <p>Rostat bröd med tomater, basilika och olivolja.</p>
                    <span class="pris">89 kr</span>
                </div>
            </div>

            <div class="box">
                <img src="bilder/ratt2.jpg" alt="Vitlöksbröd">
                <div class="ratt-info">
                    <h3>Vitlöksbröd</h3>
                    <p>Nybakat bröd med vitlökssmör och örter.</p>
                    <span class="pris">69 kr</span>
                </div>
            </div>

            <div class="box">
                <img src="bilder/ratt3.jpg" alt="Caprese">
                <div class="ratt-info">
                    <h3>Caprese</h3>
                    <p>Mozzarella, tomat och färsk basilika.</p>
                    <span class="pris">95 kr</span>
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
    --bakgrund: #fdf6ec;
    --text: #333;
    --accent: #c0392b;
    --kort-bg: #fff;
    --meny-bg: #2c3e50;
}

body {
    font-family: Georgia, serif;
    background-color: var(--bakgrund);
    color: var(--text);
}

.kontainer {
    width: 950px;
    margin: auto;
}

/* Navigation */
.meny {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: var(--meny-bg);
    padding: 15px 25px;
}

.logo {
    color: white;
    font-size: 1.4rem;
    font-weight: bold;
}

.nav-lankar a {
    color: #ccc;
    text-decoration: none;
    padding: 8px 15px;
    border-radius: 5px;
    transition: 0.2s;
}

.nav-lankar a:hover {
    color: white;
    background-color: var(--accent);
}

.nav-lankar .aktiv {
    color: white;
    background-color: var(--accent);
}

/* Hero */
.hero {
    background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('bilder/bakgrund.jpg');
    background-size: cover;
    background-position: center;
    color: white;
    text-align: center;
    padding: 80px 20px;
}

.hero h1 {
    font-size: 2.5rem;
    text-shadow: 2px 2px 6px rgba(0, 0, 0, 0.4);
}

/* Kategori */
.kategori {
    color: var(--accent);
    text-align: center;
    margin: 30px 0 15px 0;
    font-size: 1.5rem;
}

/* Grid */
.rutnat {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 25px;
    padding: 0 20px 30px 20px;
}

.box {
    background-color: var(--kort-bg);
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    transition: 0.3s;

    /* Nested grid för kortets inre layout */
    display: grid;
    grid-template-rows: auto 1fr;
}

.box:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
}

.ratt-info {
    padding: 15px;
    display: grid;
    grid-template-rows: auto auto 1fr;
}

.ratt-info h3 {
    color: var(--accent);
    margin-bottom: 5px;
}

.ratt-info p {
    color: #666;
    font-size: 0.9rem;
}

.pris {
    font-weight: bold;
    font-size: 1.1rem;
    color: var(--accent);
    align-self: end;
    margin-top: 10px;
}
```

## Övningar och kodexempel

### Övning 1: nested grid

Kortet självt är en grid, och dess innehåll har också en grid. Detta gör att priset alltid hamnar längst ner:

```css
.box {
    display: grid;
    grid-template-rows: auto 1fr;  /* Bilden tar sin plats, info tar resten */
}

.ratt-info {
    display: grid;
    grid-template-rows: auto auto 1fr;  /* Rubrik, text, pris (som trycks ner) */
}

.pris {
    align-self: end;  /* Priset hamnar alltid längst ner */
}
```

### Övning 2: gradient-overlay på bild

Skapa en mörkare overlay ovanpå en bakgrundsbild med `linear-gradient`:

```css
.hero {
    background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('bilder/bakgrund.jpg');
}
```

## Uppgifter

### Nivå 1: uppvärmning (mycket enkelt)

**Uppgift 1: egna rätter**
Byt ut rätterna till egna — byt namn, beskrivning och pris. Byt bilder.

**Uppgift 2: ändra restaurangnamn**
Byt logon och hero-texten till din egen restaurang.

### Nivå 2: fler rätter (enkelt)

**Uppgift 3: ny kategori**
Lägg till en ny `<h2 class="kategori">` (t.ex. "Huvudrätter") med en ny `.rutnat`-sektion med tre rätter.

**Uppgift 4: ännu en kategori**
Lägg till en tredje kategori (t.ex. "Desserter") med tre kort.

### Nivå 3: styla och förbättra (medel)

**Uppgift 5: bättre hover**
Lägg till en `linear-gradient`-effekt vid hover på korten:

```css
.box:hover .ratt-info {
    background: linear-gradient(to bottom, #fff, #fef9f0);
}
```

**Uppgift 6: ändra färgtema**
Byt ut alla CSS-variabler i `:root` till ett nytt tema. Testa t.ex. ett japanskt tema (mörkare färger) eller ett mexikanskt tema (varma färger).

### Nivå 4: extra funktioner (avancerat)

**Uppgift 7: footer**
Lägg till en footer längst ner med restaurangens adress, telefon och öppettider. Styla med samma bakgrundsfärg som menyn.

**Uppgift 8: bildgalleri**
Lägg till en sektion "Våra lokaler" med ett grid-galleri (3 bilder bredvid varandra) med `<figure>` och `<figcaption>`.

(Repetition: `<figure>`, `<figcaption>` från kapitel 2!)

### Nivå 5: boss-nivån

**Uppgift 9: komplett menysida**
Bygg en komplett restaurangsmeny med:

1. Minst tre kategorier (förrätter, huvudrätter, desserter).
2. Minst tre rätter per kategori.
3. Alla kort har bild, namn, beskrivning och pris.
4. Hover-effekter på alla kort.

**Uppgift 10: restaurangens webbplats**
Gör sidan till en komplett restaurangsida:

1. Navigation med `.aktiv` och hover-effekter.
2. Hero-sektion med bakgrundsbild och gradient-overlay.
3. Fullständig meny med nested grid-kort.
4. Bildgalleri med grid-layout.
5. Footer med kontaktinformation.
6. CSS-variabler och Google Font.
