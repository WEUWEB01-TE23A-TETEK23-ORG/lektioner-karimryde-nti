# Kapitel 3 – Div-boxar, klasser och layout

Historik över kapitel 3 där vi introducerade `<div>` som layout-verktyg, CSS-klasser, CSS-reset och flexbox.

---

## Lektioner i kronologisk ordning

| Datum | Mapp | Vad vi gjorde |
|-------|------|---------------|
| 2025-09-29 | visitkort | Digitalt visitkort – CSS-reset, `<div>`-boxar med fast bredd/höjd |
| 2025-10-02 | arbete | Länkning mellan sex HTML-filer, `class`-attribut per sida |
| 2025-10-06 | scones | Receptsida med `.kontainer`, `background-attachment: fixed`, `<ol>` |
| 2025-10-09 | bloggen | CSS-variabler (`:root`) med Coolors.co-palett, `.inlagg`-klass |
| 2025-10-13 | bildgalleri | NASA-bildgalleri med `display: flex` – första flexbox! |

---

## Begrepp vi lärt oss

### HTML
`<div>`, `class`-attributet, `<ol>`, HTML-entiteter (`&raquo;`, `&laquo;`), flersidig struktur

### CSS
CSS-reset (`box-sizing: border-box`), `:root`-variabler (`--primar: #hex`), `.klass`-selektorer, `display: flex`, `background-attachment: fixed`, `list-style-type`, `gap`

---

## Exempel från lektionerna

### CSS-reset (visitkort och framåt)
```css
html { box-sizing: border-box; }
*, *:before, *:after { box-sizing: inherit; }
body, h1, h2, h3, h4, h5, h6, p, ul { margin: 0; padding: 0; }
img { width: 100%; }
```

### CSS-variabler med Coolors.co-palett (bloggen)
```css
:root {
    --charcoal: #264653;
    --persian-green: #2a9d8f;
    --saffron: #e9c46a;
    --sandy-brown: #f4a261;
    --burnt-sienna: #e76f51;
}

body {
    background-color: var(--charcoal);
    color: var(--saffron);
}
```

### Flexbox (bildgalleri)
```css
.flex-rad {
    display: flex;
    gap: 20px;
}

.box {
    width: 50%;
    padding: 15px;
    background-color: var(--persian-green);
}
```

### Flersidig navigation (arbete)
```html
<!-- arbete1.html -->
<a href="arbete2.html">&raquo;</a>

<!-- arbete2.html -->
<a href="arbete1.html">&laquo;</a>
<a href="arbete3.html">&raquo;</a>
```

---

## Koppling till centralt innehåll

- **Märkspråk och DOM:** `<div>` som strukturell byggsten, klass-baserad styling.
- **Kvalitetssäkring och validering:** CSS-reset för konsekvent rendering över webbläsare.
- **Interoperabilitet:** `box-sizing: border-box` ger förutsägbar layout oavsett användaragent.
- **Riktlinjer för god praxis:** `.kontainer`-mönstret, semantiska klassnamn.
