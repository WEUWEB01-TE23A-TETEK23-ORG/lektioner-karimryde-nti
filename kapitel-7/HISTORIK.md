# Kapitel 7 – Avancerade layouter och responsiv design

Historik över kapitel 7 där vi byggde vidare på CSS Grid med namngivna template areas (Holy Grail) och lärde oss responsiv design med media queries.

---

## Lektioner i kronologisk ordning

| Datum | Mapp | Vad vi gjorde |
|-------|------|---------------|
| 2026-01-15 | fem-favoriter | Layoutträning med "5 svenska desserter" och flex-meny |
| 2026-01-21 | holygrail | Branschstandard-layout: Holy Grail med `grid-template-areas` |
| 2026-01-28 | neon-nudlar | Nytt projekt – grundskelett med grid-layout |
| 2026-02-11 | responsiv-sida | Responsiv design med `@media`-queries för tre breakpoints |

---

## Begrepp vi lärt oss

### HTML
`<header>`, `<main>`, `<aside>`, `<footer>`, `<nav>` – semantiska HTML5-element

### CSS
`grid-template-areas`, namngivna areas (`sidhuvud`, `innehåll`, `sidebar`, `sidfot`), `grid-area`, `@media (max-width: ...)`, breakpoints (1200px, 768px, 576px), `background-attachment: fixed`, gradient-navigation

---

## Exempel från lektionerna

### Holy Grail med grid-template-areas (holygrail)
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

### Responsiv design med media queries (responsiv-sida)
```css
/* Desktop: 3 kolumner */
.kontainer {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
}

/* Surfplatta: 2 kolumner */
@media (max-width: 768px) {
    .kontainer {
        grid-template-columns: 1fr 1fr;
    }
}

/* Mobil: 1 kolumn */
@media (max-width: 576px) {
    .kontainer {
        grid-template-columns: 1fr;
    }
    .meny a {
        display: block;
        width: 100%;
    }
}
```

### Gradient-navigation
```css
header nav {
    background: linear-gradient(to bottom, #bfd255 0%, #8eb92a 50%, #72aa00 51%, #9ecb2d 100%);
    padding: 10px;
    border-radius: 5px;
}
header nav a:hover {
    background: linear-gradient(to bottom, #e6f0a3 0%, #d2e638 50%, #c3d825 51%, #dbf043 100%);
    color: #344e00;
}
```

---

## Viktiga detaljer

- **Grid-template-areas syntax:** Varje rad måste ha lika många kolumner och skrivas som en sträng inom citattecken.
- **Grid-area:** Varje element måste tilldelas en area med `grid-area: namn`.
- **Media queries-ordning:** Med `max-width` går man från störst till minst skärm (desktop först).
- **Svenska area-namn:** Vi använder `sidhuvud`, `innehåll`, `sidebar`, `sidfot` – inte engelska.
- **Semantiska element:** `<header>`, `<main>`, `<aside>`, `<footer>`, `<nav>` ger bättre struktur och tillgänglighet.

---

## Koppling till centralt innehåll

- **Interoperabilitet:** Responsiv design säkerställer att sidan fungerar på alla enheter (mobil, surfplatta, desktop).
- **Tillgänglighet:** Semantiska HTML5-element hjälper skärmläsare och sökmotorer.
- **Applikationer oberoende av plattform:** `@media`-queries anpassar layouten efter skärmstorlek, inte enhetstyp.
- **Testning:** Vi testar på olika skärmstorlekar för att verifiera responsiviteten.
