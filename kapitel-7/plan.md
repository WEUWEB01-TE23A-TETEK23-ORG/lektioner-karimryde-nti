# Modulplan: avancerade layouter och responsiv design

Kapitlet bygger vidare på CSS Grid med namngivna template areas (Holy Grail-layout) och introducerar responsiv design med media queries. Eleverna lär sig bygga sidor som anpassar sig till olika skärmstorlekar.

## Mål

- Skapa Holy Grail-layout med `grid-template-areas` och namngivna areas.
- Använda `fr`-enheter för proportionella kolumner.
- Göra en layout responsiv med `@media`-queries.
- Anpassa grid-layout för tre breakpoints: desktop, surfplatta och mobil.
- Använda semantiska HTML5-element: `<header>`, `<main>`, `<aside>`, `<footer>`.

## Förkunskaper

- Kapitel 6: `display: grid`, `grid-template-columns`, `1fr`, `gap`.
- Kapitel 1–4: HTML-struktur, CSS-klasser, `.kontainer`, navigation, hover-effekter.

## Nya begrepp

### HTML
`<header>`, `<main>`, `<aside>`, `<footer>`, `<nav>` (semantiska element)

### CSS
`grid-template-areas`, namngivna areas (`sidhuvud`, `innehåll`, `sidebar`/`sidopanel`, `sidfot`), `grid-area`, `@media (max-width: ...)`, breakpoints (1200px, 768px, 576px), `background-attachment: fixed`, gradient-navigation

## Pedagogiska grundregler

- Grid-areas namnges på **svenska**: `sidhuvud`, `innehåll`, `sidebar`, `sidfot`.
- Holy Grail-layouten är ett klassiskt webbdesignmönster — eleverna lär sig "det verkliga sättet" att strukturera en sida.
- Responsiv design visas med tre tydliga steg: desktop → surfplatta → mobil.
- `background-attachment: fixed` och gradient-navigation ger visuellt imponerande resultat.

## Lektioner

### Lektion 1: Holy Grail-layout (mappen: holygrail)
- **Innehåll:** `grid-template-areas` med `sidhuvud`, `innehåll`, `sidebar`, `sidfot`. `grid-template-columns: 3fr 1fr`, `<header>`, `<main>`, `<aside>`, `<footer>`, gradient-navigation med `:hover` och `.aktiv`.
- **Mål:** förstå namngivna grid-areas som ett sätt att "rita" layouten i CSS.
- **Repetition:** `display: grid`, `gap`, `.kontainer`, navigering, hover-effekter.

### Lektion 2: favoritlista (mappen: fem-favoriter)
- **Innehåll:** Holy Grail-layout tillämpad på en tematisk sida, fast bredd med `margin: auto`.
- **Mål:** repetera grid-areas i ett nytt sammanhang.
- **Repetition:** `grid-template-areas`, namngivna areas, `<header>`, `<main>`, `<aside>`, `<footer>`.

### Lektion 3: responsiv sida (mappen: responsiv-sida)
- **Innehåll:** `@media`-queries för tre breakpoints: `max-width: 1200px` (full bredd), `max-width: 768px` (en kolumn), `max-width: 576px` (mobil-anpassning). Ändrar `grid-template-columns` och `grid-template-areas` per breakpoint. Block-navigation på mobil.
- **Mål:** kunna göra en befintlig layout responsiv med media queries.
- **Repetition:** `grid-template-areas`, `grid-template-columns`, `.kontainer`.

### Lektion 4: neon-nudlar (mappen: neon-nudlar)
- **Innehåll:** ytterligare repetition av grid-layout och styling.
- **Mål:** befästa grid-areas och responsiv design.
- **Repetition:** samtliga grid-koncept från lektion 1–3.

## Vanliga misstag

- Felaktig `grid-template-areas`-syntax: varje rad måste ha lika många kolumner och vara en sträng inom citattecken.
- Glömmer `grid-area: sidhuvud` på `<header>` — elementet hamnar inte på rätt plats.
- Media queries i fel ordning — `max-width` ska gå från störst till minst.
- Glömmer `width: 100%` i responsiv variant — sidan scrollar horisontellt.
- Skriver `grid-template-area` (singular) istället för `grid-template-areas` (plural).
- Använder engelska area-namn (`header`, `content`) istället för svenska (`sidhuvud`, `innehåll`).

## Resurser

- [Google Fonts](https://fonts.google.com/) — typsnitt.
