# Kapitel 4 – Flersidig webbplats med navigation

Historik över kapitel 4 där vi sammanfogade allt från tidigare kapitel till kompletta webbplatser med gemensam navigering.

---

## Lektioner i kronologisk ordning

| Datum | Mapp | Vad vi gjorde |
|-------|------|---------------|
| 2025-11-06 | webbplats | Fem favoritband – 5-sidig webbplats med `.meny`, `.aktiv`-klass, hover-effekter |
| 2025-11-20 | rep-webbplats | Genrepetition inför praktiskt prov – "5 biofilmer" |

---

## Begrepp vi lärt oss

### HTML
Navigation med `<div class="meny">`, manuell `.aktiv`-klass per sida, `<figure>` och `<figcaption>`

### CSS
`display: inline-block`, `:hover`-pseudoklass, CSS-variabler med Coolors.co-namn, `figure`-styling med `border` och `padding`

---

## Exempel från lektionerna

### Navigationsmeny med aktiv klass och hover
```html
<div class="meny">
    <a class="aktiv" href="sida1.html">ABBA</a>
    <a href="sida2.html">REM</a>
    <a href="sida3.html">Midnight Oil</a>
    <a href="sida4.html">The Doors</a>
    <a href="sida5.html">Manfred Mann</a>
</div>
```

```css
.meny a {
    display: inline-block;
    padding: 10px 15px;
    text-decoration: none;
    color: var(--charcoal);
    background-color: var(--saffron);
}
.meny a:hover {
    background-color: var(--sandy-brown);
    color: #fff;
}
.meny a.aktiv {
    background-color: var(--burnt-sienna);
    color: #fff;
}
```

### CSS-variabler från Coolors.co
```css
:root {
    --charcoal: #264653;
    --persian-green: #2a9d8f;
    --saffron: #e9c46a;
    --sandy-brown: #f4a261;
    --burnt-sienna: #e76f51;
}
```

---

## Viktig detalj
- `.aktiv` är en **egen klass** (inte CSS-pseudoklassen `:active`).
- Klassen flyttas **manuellt** till rätt `<a>`-tagg på varje sida.
- Hover-effekten och `.aktiv`-stilen bör vara visuellt konsekventa.

---

## Koppling till centralt innehåll

- **Processen för ett webbutvecklingsprojekt:** Planering av sidstruktur, konsekvent navigation, testning av länkar.
- **Riktlinjer för god praxis:** Återanvändbar meny, semantiska klassnamn, konsekvent styling.
- **Kvalitetssäkring:** Alla sidor delar samma `style.css` – en ändring slår igenom överallt.
