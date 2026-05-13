# Kapitel 6 – CSS Grid och kortlayouter

Historik över kapitel 6 där vi introducerade CSS Grid som layoutsystem för rutnät och kortdesign.

---

## Lektioner i kronologisk ordning

| Datum | Mapp | Vad vi gjorde |
|-------|------|---------------|
| 2025-11-12 | raspberrypi | Nästlade grids för e-handelsprodukter (Raspberry Pi) |
| 2025-11-19 | burger-meny | Rutnätslayout för hamburgermeny med hover-animationer |

---

## Begrepp vi lärt oss

### CSS
`display: grid`, `grid-template-columns`, `1fr`, `gap`, `repeat()`, `transition`, `linear-gradient()`, `background-position` (animerad), `background-size`, `grid-template-rows`, nästlad grid (grid inuti grid), `justify-content: space-between` (i flex-nav), `box-shadow` på hover

---

## Exempel från lektionerna

### Enkel grid-layout (burger-meny)
```css
.rutnat {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
}
```

### Hover-animation med transition
```css
.box {
    background: linear-gradient(to bottom, #f9d423, #ff4e50);
    transition: all 0.3s ease;
}
.box:hover {
    background: linear-gradient(to bottom, #ff4e50, #f9d423);
    background-size: 200% 200%;
    background-position: right bottom;
}
```

### Nästlad grid (raspberrypi)
```css
.kolumner-3 {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
}
.kolumn {
    display: grid;
    grid-template-rows: auto auto 1fr auto;
    border-radius: 10px;
    box-shadow: 2px 2px 8px rgba(0,0,0,0.2);
    transition: box-shadow 0.3s;
}
.kolumn:hover {
    box-shadow: 4px 4px 16px rgba(0,0,0,0.4);
}
```

---

## Viktiga detaljer

- `1fr` är en **flexibel enhet** som delar tillgängligt utrymme lika mellan kolumner.
- `gap` sätter avstånd mellan grid-celler (både rader och kolumner).
- `transition` måste sättas på **grund-elementet** (inte på hover) för att animationen ska bli mjuk åt båda hållen.
- Grid kan nästlas: ett grid-element inuti ett annat grid-element.

---

## Koppling till centralt innehåll

- **Märkspråk och DOM:** CSS Grid som modernt layoutsystem, tvådimensionell kontroll.
- **Interoperabilitet:** Grid stöds av alla moderna webbläsare och ger konsekvent layout.
- **Riktlinjer för god praxis:** `.rutnat` som konsekvent klassnamn, nästlade grids för komplexa kort.
- **Applikationer oberoende av användaragent:** Grid fungerar likadant i Chrome, Firefox, Safari och Edge.
