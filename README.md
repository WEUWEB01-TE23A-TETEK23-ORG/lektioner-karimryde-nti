# Webbutveckling 1 (WEUWEB01) – Kursöversikt

Detta är det samlade lektionsarkivet för gymnasiekursen **Webbutveckling 1** på TE23A. Arkivet innehåller all kod som producerats under lektionerna, organiserat kronologiskt i åtta kapitel från grundläggande HTML till interaktiv JavaScript.

---

## Kursens syfte

Kursen syftar till att ge eleverna grundläggande kunskaper i webbutveckling – från hur webben fungerar tekniskt till hur man bygger, stylar och publicerar egna webbplatser. Undervisningen följer en progressiv struktur där varje nytt moment bygger på tidigare kunskaper med extrem repetition och visuell feedback som pedagogisk grund.

---

## Kapitelöversikt

| Kapitel | Tema | Huvudsakliga tekniker |
|---------|------|----------------------|
| 1 | HTML-grunder och första CSS | HTML-struktur, rubriker, bilder, listor, tabeller, färger, typsnitt, bakgrunder |
| 2 | Bilder och layout-introduktion | `<figure>`, marginaler, text-transform, bakgrundspositionering |
| 3 | Div-boxar, klasser och layout | `<div>`, CSS-reset, klasser, `.kontainer`-mönstret, flexbox, CSS-variabler |
| 4 | Flersidig webbplats | Navigation, `.aktiv`-klass, hover-effekter, sammanhängande projekt |
| 6 | CSS Grid | `display: grid`, `1fr`, `gap`, nästlade grids, transition-animationer |
| 7 | Avancerade layouter och responsiv design | `grid-template-areas`, Holy Grail, `@media`-queries, semantisk HTML5 |
| 8 | JavaScript-introduktion | Variabler, funktioner, DOM-manipulering, `if`/`else`, användarinteraktion |

---

## 1. HTML-grunder (kapitel 1)

### Vad är HTML?
HTML (HyperText Markup Language) är webbens grundspråk – ett **märkspråk** som beskriver struktur och innehåll på en webbsida. HTML består av **element** (taggar) som talar om för webbläsaren vad som är rubriker, stycken, bilder och länkar.

### Grundstruktur för varje HTML-dokument
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sidtitel</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Min rubrik</h1>
    <p>Ett stycke text.</p>
    <script src="script.js"></script>  <!-- alltid sist i body -->
</body>
</html>
```

**Viktiga detaljer:**
- `<!DOCTYPE html>` talar om att dokumentet är HTML5.
- `<meta charset="UTF-8">` säkerställer att svenska tecken (åäö) visas korrekt – detta är **teckenkodning** i praktiken.
- `<script>` placeras **sist i `<body>`** för att sidan ska laddas klart innan JavaScript körs.
- CSS-filen länkas i `<head>` med `<link>`.

### Centrala HTML-element
| Tagg | Syfte | Exempel |
|------|-------|---------|
| `<h1>`–`<h6>` | Rubriker (h1 = viktigast) | `<h1>Välkommen</h1>` |
| `<p>` | Stycke | `<p>En text...</p>` |
| `<br>` | Radbrytning | `Rad 1<br>Rad 2` |
| `<a>` | Länk | `<a href="sida2.html">Klicka</a>` |
| `<img>` | Bild | `<img src="bilder/foto.jpg" alt="Beskrivning">` |
| `<ul>`/`<li>` | Punktlista | `<ul><li>Äpple</li></ul>` |
| `<table>` | Tabell | `<table><tr><td>Data</td></tr></table>` |
| `<strong>` | Fet text (semantisk) | `<strong>Viktigt</strong>` |
| `<em>` | Kursiv text (semantisk) | `<em>Betonat</em>` |

### Varför semantik?
Semantisk HTML betyder att vi använder rätt tagg för rätt innehåll. `<strong>` betyder "viktig text" (inte bara "fet"). Detta hjälper **skärmläsare** och **sökmotorer** att förstå innehållet – vilket är grunden för **tillgänglighet** och **interoperabilitet** (att sidan fungerar oavsett användaragent).

---

## 2. CSS – webbens designspråk (kapitel 1–4)

### Vad är CSS?
CSS (Cascading Style Sheets) är språket som ger HTML-sidan dess utseende. Med CSS styr vi färger, typsnitt, avstånd, bakgrunder och layout. CSS skrivs i en **separat fil** för att hålla innehåll (HTML) och presentation (CSS) åtskilda – en grundläggande princip för **god praxis inom webbutveckling**.

### Grundläggande CSS-egenskaper
```css
body {
    background-color: #f0f0f0;   /* Bakgrundsfärg */
    background-image: url(bilder/bg.jpg);  /* Bakgrundsbild */
    background-size: cover;      /* Täck hela ytan */
    font-family: sans-serif;     /* Typsnitt */
    color: #333;                 /* Textfärg */
}

h1 {
    font-size: 48px;             /* Textstorlek */
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);  /* Textskugga */
}

.kontainer {
    width: 800px;                /* Fast bredd */
    margin: auto;                /* Centrera horisontellt */
    padding: 30px;               /* Inre marginal */
    border-radius: 10px;         /* Rundade hörn */
    box-shadow: 5px 5px 15px rgba(0,0,0,0.5);  /* Lådskugga */
}
```

### CSS-reset – en konsekvent utgångspunkt
Olika webbläsare har olika förinställda marginaler och padding. En **CSS-reset** nollställer dessa för att ge en enhetlig grund:
```css
html { box-sizing: border-box; }
*, *:before, *:after { box-sizing: inherit; }
body, h1, h2, h3, h4, h5, h6, p, ul { margin: 0; padding: 0; }
img { width: 100%; }
```
Detta är ett exempel på **kvalitetssäkring** och **interoperabilitet** – koden ser likadan ut i Chrome, Firefox, Safari och Edge.

### CSS-variabler – centraliserad färghantering
Med `:root`-variabler kan vi definiera en färgpalett på ett ställe och återanvända den överallt:
```css
:root {
    --charcoal: #264653;
    --persian-green: #2a9d8f;
    --saffron: #e9c46a;
    --burnt-sienna: #e76f51;
}

body { background-color: var(--charcoal); }
.meny a { color: var(--saffron); }
.meny a.aktiv { background-color: var(--burnt-sienna); }
```
Detta visar på **god praxis**: en ändring i paletten slår igenom på hela webbplatsen.

---

## 3. Layout och positionering (kapitel 2–7)

### Boxmodellen – allt är lådor
I CSS är varje element en rektangulär låda bestående av (inifrån och ut): content → padding → border → margin. `<div>`-elementet är den universella "lådan" för att gruppera innehåll.

### Evolution av layout-tekniker
Kursen följer webbens historiska utveckling av layout-tekniker:

1. **Marginaler** (kapitel 2): `margin-left`, `margin-top` – manuell positionering.
2. **Div-boxar och `.kontainer`** (kapitel 3): `width: Xpx; margin: auto` – centrerat innehåll.
3. **Flexbox** (kapitel 3): `display: flex` – en-dimensionell layout (rad eller kolumn).
4. **CSS Grid** (kapitel 6): `display: grid` – två-dimensionell layout (rader och kolumner).
5. **Grid-template-areas** (kapitel 7): namngivna ytor för intuitiv layout.
6. **Responsiv design** (kapitel 7): `@media`-queries för anpassning till olika skärmar.

### Flexbox – element på rad
```css
.flex-rad {
    display: flex;
    gap: 20px;
}
```
Flexbox är idealiskt för **endimensionella** layouter som menyer och kortrader.

### CSS Grid – full kontroll i två dimensioner
```css
.rutnat {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
}
```
`1fr` är en flexibel enhet som automatiskt fördelar utrymmet. `repeat(3, 1fr)` skapar tre lika breda kolumner.

### Holy Grail-layout – branschstandard
Holy Grail är en klassisk layout med sidhuvud, innehåll, sidopanel och sidfot:
```css
.kontainer {
    display: grid;
    grid-template-columns: 3fr 1fr;
    gap: 30px;
    grid-template-areas:
        "sidhuvud sidhuvud"
        "innehåll sidebar"
        "sidfot sidfot";
}

header  { grid-area: sidhuvud; }
main    { grid-area: innehåll; }
aside   { grid-area: sidebar; }
footer  { grid-area: sidfot; }
```
Layoutens area-namn skrivs på **svenska** i enlighet med kursens konventioner.

### Responsiv design – en sida för alla enheter
Med `@media`-queries anpassas layouten efter skärmens bredd:
```css
/* Desktop (standard) */
.kontainer { grid-template-columns: repeat(3, 1fr); }

/* Surfplatta */
@media (max-width: 768px) {
    .kontainer { grid-template-columns: 1fr 1fr; }
}

/* Mobil */
@media (max-width: 576px) {
    .kontainer { grid-template-columns: 1fr; }
    .meny a { display: block; width: 100%; }
}
```
Detta är **interoperabilitet** i praktiken – applikationer som fungerar oberoende av val av användaragent, operativsystem eller hårdvaruplattform.

---

## 4. JavaScript – interaktivitet (kapitel 8)

### Vad är JavaScript?
JavaScript är ett **Ecmascript**-språk som körs i webbläsaren (klientsidan). Via **DOM** (Document Object Model) kan JavaScript läsa och ändra HTML och CSS i realtid – utan att sidan behöver laddas om. Detta är grunden för **samspelet mellan klient och server**: HTML/CSS/JS är klientens verktygslåda.

### Grundläggande byggstenar
```javascript
// Variabel – lagrar ett värde
let namn = "Karim";

// Input från användaren
let alder = prompt("Hur gammal är du?");

// Visa meddelande
alert("Hej " + namn + "! Du är " + alder + " år.");

// Funktion – en namngiven kodsekvens
function halsa() {
    alert("Hej på dig!");
}
```

### DOM-manipulering – ändra sidan med kod
```javascript
// Hämta ett element med querySelector (CSS-selektorer)
let rubrik = document.querySelector("h1");

// Ändra text
rubrik.textContent = "Ny rubrik!";

// Ändra CSS
rubrik.style.color = "red";
document.body.style.backgroundColor = "black";
```

### Läsa formulärdata med .value
```html
<input id="namn" type="text" placeholder="Ditt namn">
<button onclick="visaNamn()">Visa</button>
<p id="resultat"></p>
```
```javascript
function visaNamn() {
    let namn = document.querySelector("#namn").value;
    document.querySelector("#resultat").textContent = "Hej " + namn + "!";
}
```

### Logik med if/else
```javascript
function kollaAlder() {
    let alder = Number(document.querySelector("#alder").value);
    if (alder >= 18) {
        document.querySelector("#svar").textContent = "Du är myndig!";
    } else if (alder >= 15) {
        document.querySelector("#svar").textContent = "Du får köra moped.";
    } else {
        document.querySelector("#svar").textContent = "Du är barn.";
    }
}
```
`Number()` konverterar text (från `.value`) till siffror – nödvändigt för matematiska jämförelser.

### Växla utseende med classList
```javascript
function togglaMorkt() {
    document.body.classList.toggle("morkt");
}
```
```css
.morkt {
    background-color: #111;
    color: #eee;
}
```

### Händelsehantering via onclick
Alla händelser kopplas via HTML-attribut (inte `addEventListener`):
```html
<button onclick="bytFarg()">Byt färg</button>
<p onmouseover="visaHemlighet()">Håll musen här</p>
```

### Pedagogisk begränsning
Kursen stannar vid **grundläggande byggstenar**: variabler (`let`), funktioner, `if`/`else`, `querySelector`, `.textContent`, `.value`, `.classList`, `Number()`, `prompt()`, `alert()`. Inga loopar, arrayer eller objekt introduceras – fokus ligger på att befästa grunderna genom extrem repetition och direkt visuell feedback.

---

## Viktiga begrepp och deras syfte

| Begrepp | Förklaring | Varför viktigt |
|---------|-----------|----------------|
| **Märkspråk** | Språk som beskriver struktur (HTML) eller utseende (CSS) | Grunden för all webb – skiljer innehåll från presentation |
| **DOM** | Document Object Model – trädstruktur av HTML-element | Bryggan mellan HTML och JavaScript |
| **Semantik** | Att använda rätt tagg för rätt innehåll | Tillgänglighet, SEO, interoperabilitet |
| **CSS-reset** | Nollställning av webbläsares förinställda stilar | Konsekvent utseende över alla webbläsare |
| **Flexbox** | Endimensionellt layoutsystem | Enkel och robust positionering av element på rad |
| **CSS Grid** | Tvådimensionellt layoutsystem | Modern standard för kompletta sidlayouter |
| **Responsiv design** | Design som anpassar sig till skärmstorlek | Fungerar på mobil, surfplatta och desktop |
| **Teckenkodning** | Hur tecken lagras digitalt (t.ex. UTF-8) | Korrekt visning av åäö och specialtecken |
| **Klient-server** | Klienten (webbläsaren) begär, servern svarar | Grundmodellen för hur webben fungerar |
| **Kvalitetssäkring** | Testning och validering av kod | Fungerande, felfri och underhållbar kod |

---

## Koppling till kursens centrala innehåll

### Webben som plattform
Genom hela kursen bygger vi på webbens grundmodell: HTML för struktur, CSS för presentation, JavaScript för interaktivitet. Vi använder **webbläsaren som plattform** och ser hur samma kod fungerar oavsett operativsystem – detta är **interoperabilitet**.

### Teknisk orientering
- **Protokoll:** Vi använder `https://` för externa resurser (Google Fonts, bilder) och relativa sökvägar för interna filer.
- **Adresser:** URL-strukturen förstås genom `<a href="">` och relativa vs absoluta sökvägar.
- **Säkerhet:** `prompt()` och `alert()` är säkra, sandlådade funktioner. Vi diskuterar aldrig `eval()` eller osäkra metoder.
- **Klient-server:** All vår kod körs på klientsidan; vi nämner att servern levererar filerna men fördjupar oss inte i serversidans kod.

### Märkspråk och deras roller
- **HTML:** Struktur och innehåll – "vad som visas".
- **CSS:** Presentation och layout – "hur det ser ut".
- **JavaScript (Ecmascript):** Beteende och interaktivitet – "vad som händer".
- **DOM:** Trädstrukturen som binder samman alla tre.

### Teckenkodning
`<meta charset="UTF-8">` i varje HTML-dokument säkerställer att Unicode används – den globala standarden för teckenkodning som stöder alla språk inklusive svenska tecken (åäö).

### Bilder och media
- `<img>` med `alt`-attribut för tillgänglighet.
- Bakgrundsbilder via CSS (`background-image`) som designelement.
- `<figure>` och `<figcaption>` för semantisk bildhantering.
- `background-size: cover` och `object-fit` för bildoptimering.

### Processen för webbutvecklingsprojekt
Kursen följer en metodisk process:
1. **Planering:** Varje kapitel inleds med `plan.md` som definierar mål och begrepp.
2. **Struktur och design:** HTML-skelett byggs först, sedan CSS-styling.
3. **Kodning:** Eleverna skriver kod steg för steg med läraren.
4. **Optimering:** CSS-reset, variabler, återanvändbara klasser.
5. **Testning:** Sidorna öppnas i webbläsaren för direkt visuell verifiering.
6. **Dokumentation:** `README.md`, `dagbok.md` och `HISTORIK.md` dokumenterar varje steg.
7. **Uppföljning:** Repetitionslektioner och projekt befäster kunskaperna.

### Riktlinjer för god praxis
- **Separation av innehåll och presentation:** HTML i `.html`, CSS i `.css`, JS i `.js`.
- **Konsekvent namngivning:** `.kontainer`, `.meny`, `.rutnat`, `.aktiv` – svenska klassnamn i kebab-case.
- **CSS-reset** för enhetlig rendering.
- **`<script>` sist i `<body>`** för snabbare sidladdning.
- **Semantisk HTML** för tillgänglighet och SEO.
- **Kommentarer** i kod för att förklara syfte.

### Interoperabilitet
Vi skriver **standard-enlig kod** (HTML5, CSS3, ES6) som fungerar i alla moderna webbläsare. CSS-reset, responsiv design och testning på olika enheter säkerställer att applikationerna fungerar oberoende av användaragent, operativsystem eller hårdvaruplattform.

### Tillgänglighet
- `alt`-attribut på alla bilder.
- Semantiska element (`<header>`, `<main>`, `<nav>`, `<footer>`).
- Tydlig rubrikhierarki (`<h1>` → `<h2>` → `<h3>`).
- Tillräcklig färgkontrast genom medveten färgpalett.

### Kvalitetssäkring och validering
- Varje sida testas direkt i webbläsaren.
- CSS-reset säkerställer konsekvent rendering.
- Kod granskas gemensamt på tavlan innan eleverna skriver.
- Felhantering i JavaScript med `if`/`else` fångar oväntad input.

### Säkerhet
- Vi använder endast säkra, inbyggda JavaScript-metoder.
- Ingen användardata sparas eller skickas – allt sker i webbläsaren.
- Vi diskuterar `.gitignore` för att undvika att känslig information (som API-nycklar) versionhanteras.

### Lagar och bestämmelser
- **GDPR / personuppgiftslagen** berörs i diskussion om formulärdata.
- **Lagen om elektronisk kommunikation** nämns i samband med cookies och spårning.
- **Upphovsrätt:** Vi använder Creative Commons-bilder (Unsplash) och anger alltid källa.

### Terminologi
Kursen bygger upp ett svenskt fackspråk inom webbutveckling: *märkspråk, element, tagg, attribut, selektor, deklaration, egenskap, värde, DOM, boxmodellen, grid, flexbox, responsiv, semantisk, renderingsmotor, klient-server, protokoll, teckenkodning, tillgänglighet, interoperabilitet*.

---

## Filstruktur och konventioner

```
lektioner-karimryde-nti/
├── README.md              ← Denna fil (kursöversikt)
├── history.md             ← Kronologisk dagbok, lektion för lektion
├── PEDAGOGIK.md           ← Pedagogisk strategi för AI-interaktion
├── .github/
│   └── copilot-instructions.md
├── kapitel-1/             ← HTML-grunder och första CSS
│   ├── plan.md
│   ├── dagbok.md
│   ├── HISTORIK.md        ← Kapitelhistorik
│   ├── intro/             ← Lektion 1: första HTML-sidan
│   ├── beatles/           ← Lektion 2: första CSS
│   ├── pippi/             ← Lektion 3: listor och bilder
│   ├── oppna-landskap/    ← Lektion 4: avancerad CSS
│   └── veckomeny/         ← Lektion 5: tabeller
├── kapitel-2/             ← Bilder och layout
├── kapitel-3/             ← Div-boxar, klasser och flexbox
├── kapitel-4/             ← Flersidig webbplats
├── kapitel-6/             ← CSS Grid
├── kapitel-7/             ← Avancerade layouter och responsiv design
└── kapitel-8/             ← JavaScript-introduktion
```

---

## Resurser som använts i kursen

- [Google Fonts](https://fonts.google.com/) – kostnadsfria typsnitt
- [Coolors.co](https://coolors.co/) – färgpalettgenerator
- [Unsplash](https://unsplash.com/) – fria bilder (Creative Commons)
- [Wikipedia](https://sv.wikipedia.org/) – textinnehåll för övningssidor
- [CSS Gradient](https://cssgradient.io/) – gradient-generator
- [W3Schools](https://www.w3schools.com/) – referensdokumentation
- [MDN Web Docs](https://developer.mozilla.org/) – teknisk dokumentation

---

*Kursen genomfördes läsåret 2025–2026 på NTI Gymnasiet, TE23A. Lärare: Karim Ryde.*
