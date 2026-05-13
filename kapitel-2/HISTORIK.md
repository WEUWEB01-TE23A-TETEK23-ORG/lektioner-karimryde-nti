# Kapitel 2 – Bilder och layout-introduktion

Historik över kapitel 2 där vi fördjupade arbetet med bilder och introducerade hur man positionerar element med marginaler.

---

## Lektioner i kronologisk ordning

| Datum | Mapp | Vad vi gjorde |
|-------|------|---------------|
| 2025-09-08 | fiji-reklam | Reklamsida för Fiji – "fusk-knappar" med CSS, bakgrundsbilder och textplacering |
| 2025-09-11 | portratt | Porträttgalleri med `<figure>` och `<figcaption>` (påbörjad) |

---

## Begrepp vi lärt oss

### HTML
`<figure>`, `<figcaption>`

### CSS
`margin-left`, `margin-top`, `text-transform: uppercase`, `background-position`, `text-decoration: none`, `padding` på inline-element (länkar som knappar)

---

## Exempel från lektionerna

### Hero-sektion med bakgrundsbild (fiji-reklam)
```css
.hero {
    background-image: url('bilder/strand.jpg');
    background-size: cover;
    background-position: center;
    height: 400px;
}
```

### Länk stylad som knapp
```css
a.knapp {
    text-decoration: none;
    text-transform: uppercase;
    padding: 10px 20px;
    background-color: #e76f51;
    color: #fff;
    border-radius: 5px;
}
```

### Figur med bildtext (portratt)
```html
<figure>
    <img src="bilder/portratt.jpg" alt="Porträtt">
    <figcaption>Ett vackert porträtt från Fiji</figcaption>
</figure>
```

---

## Koppling till centralt innehåll

- **Märkspråk och semantik:** `<figure>` och `<figcaption>` ger semantisk mening åt bilder.
- **Bilder och media:** Bakgrundsbilder som designelement, `background-position` för bildplacering.
- **Riktlinjer för god praxis:** Separat CSS-fil, semantiska HTML-element.
