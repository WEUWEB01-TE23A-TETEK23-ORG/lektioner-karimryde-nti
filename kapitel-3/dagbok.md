# Dagbok: Kapitel 3 – Boxmodellen, Flexbox och Div

## Lektion 1: visitkort (2025-09-29)

**Ämne:** Digitalt visitkort med boxar

**Nya begrepp:**
- `<div>` – En generell block-container för att gruppera element
- CSS-reset (`box-sizing: border-box`) – Lättare hantering av boxens bredd/storlek
- Google Fonts – Importera typsnitt

**Vad vi gjorde:**
Vi konstruerade ett digitalt visitkort centrerat på en bakgrundsbild. Det här var första gången vi använde `<div>`-taggen för att bygga en behållare och klasser för att rikta CSS mot just den. Vi gick igenom varför och hur en CSS-reset används i moderna projekt.

**Nyckelexempel:**
```html
<div class="kort">
    <h1>Namn Efternamn</h1>
    <p>Webbutvecklare</p>
</div>
```
```css
html {
    box-sizing: border-box;
}
*, *:before, *:after {
    box-sizing: inherit;
}
.kort {
    width: 400px;
    margin: 100px auto; /* Centrerar boxen i mitten */
}
```

---

## Lektion 2: arbete (2025-10-02)

**Ämne:** Relativ navigering och sidornas klassning (6 sidor)

**Nya begrepp:**
- Relativa länkar – Att hoppa mellan filer i samma mapp
- `class` på `<body>` – Möjlighet att ge varje sida en unik look via klasser på `body`
- HTML-entiteter (`&raquo;`, `&laquo;`) – Navigationspilar
- Extern CSS användning för flera sidor

**Vad vi gjorde:**
Vi tog Ulf Lundells låt "Öppna landskap" (eller "Arbete") och styckade upp verserna på 6 separata HTML-sidor för att förstå navigationskonceptet fullt ut i mappar.

**Nyckelexempel:**
```html
<body class="sida2">
    <a href="arbete1.html">&laquo; Föregående</a>
    <a href="arbete3.html">Nästa &raquo;</a>
</body>
```

---

## Lektion 3: scones (2025-10-06)

**Ämne:** Engelskt recept med nestlade listor

**Nya begrepp:**
- `.kontainer`-mönstret – Vanlig teknik för att begränsa bredden på text och centrera
- `background-attachment: fixed` – Bakgrundsbilden fastnar i fönstret vid scroll
- `<ol>` – Ordrad, numrerad lista
- Nestlade listor – En lista inuti en annan lista (`<ul>` i `<ul>`)
- `list-style-type` – Byta punkterna i en lista till tex `square`

**Vad vi gjorde:**
Vi byggde en trevlig receptsida för scones. Här stötte vi på skillnaderna mellan numrerade "steg" och "ingredienslistor", och lät fönsterbakgrunden vara fixerad medan receptets `.kontainer` scrollar över.

**Nyckelexempel:**
```css
.kontainer {
    width: 600px;
    margin: auto;
    background-color: white;
}
body {
    background-image: url('bilder/scones-bg.jpg');
    background-attachment: fixed;
}
```

---

## Lektion 4: bloggen (2025-10-09)

**Ämne:** Färgpaletter, variabler och blogg-layout

**Nya begrepp:**
- `:root` – Central plats för CSS-variabler
- CSS-variabler (`--huvudfärg`, `var()`) – Lättare att byta färgschema på hela sidan
- `.inlagg`, `.datum` – CSS-klasser för att strukturera blogginlägg

**Vad vi gjorde:**
Vi använde Coolors.co för att hämta en sammanhängande färgpalett till vårt blogg-projekt. Vi definierade dessa färger som CSS-variabler överst i koden, och använde ett konsekvent mönster där varje `.inlagg`-box fick samma utseende.

**Nyckelexempel:**
```css
:root {
    --bakgrund: #f4f4f9;
    --textfärg: #333;
    --accenter: #e63946;
}

body {
    background-color: var(--bakgrund);
    color: var(--textfärg);
}

.datum {
    color: var(--accenter);
}
```

---

## Lektion 5: bildgalleri (2025-10-13)

**Ämne:** Flexbox-intro med NASA Moon Gallery

**Nya begrepp:**
- `display: flex` – Flexbox-containern, låter sina underliggande boxar ligga i rad
- `.box`-klass – Ett standardiserat återkommande kort
- `flex-wrap: wrap` – Tvingar radbrytning av flex-element

**Vad vi gjorde:**
Lektionen var en renodlad introduktion till CSS Flexbox. Vi byggde ett bildgalleri över Månen, där `display: flex` skapade ett rutnät som svarade bra på utrymme, i kombination med procentuella bredder.

**Nyckelexempel:**
```html
<div class="galleri">
    <div class="box"><img src="..."></div>
    <div class="box"><img src="..."></div>
</div>
```
```css
.galleri {
    display: flex;
    flex-wrap: wrap;
}

.box {
    width: 30%; /* Boxar tar upp max-plats */
    margin: 1%;
}
```
