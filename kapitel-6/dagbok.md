# Dagbok: Kapitel 6 – CSS Grid Layout

## Lektion 1: burger-meny (2025-11-19)

**Ämne:** Meny i kortformat med CSS Grid (Burger King)

**Nya begrepp:**
- `display: grid` – Slår på rutnätsbaserad layout för ett element
- `grid-template-columns: 1fr 1fr 1fr` – Skapar tre lika stora spalter i rutnätet
- `gap` – CSS-egenskapen som sätter ett automatiskt avstånd mellan spalter och rader
- `linear-gradient` – En CSS-funktion som skapar en färgövergång i bakgrunden
- `transition` – Animerar en förändring mellan två tillstånd (t.ex hover) mjuka

**Vad vi gjorde:**
Vi återskapade stilen från en digital meny (likt Burger King) där olika rätter låg som "kort" i ett strikt rutnät byggt med CSS Grid. Vi lade också till snygga gradient-fyllningar och en hover-effekt som gjorde att lådorna försiktigt skalade upp (`transition`) när musen var över dem.

**Nyckelexempel:**
```html
<div class="rutnat">
    <div class="box"><h3>Vempper</h3></div>
    <div class="box"><h3>Chili Cheese</h3></div>
</div>
```
```css
.rutnat {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 20px;
}
.box {
    background: linear-gradient(135deg, white, #ffebd6);
    transition: 0.3s;
}
.box:hover {
    transform: scale(1.05); /* Skalar upp något */
}
```

---

## Lektion 2: raspberrypi (2025-11-12)

**Ämne:** Nästlade grid-strukturer för e-handelsprodukter

**Nya begrepp:**
- Nästlat Grid (`display: grid` inuti en annan `display: grid`)
- `grid-template-rows: auto auto 1fr auto` – Styr rutnätets rader, där `1fr` tvingar element isär för att fylla ut utrymmet jämt (perfekt för kort-innehåll).

**Vad vi gjorde:**
I det här projektet byggde vi en "e-handelssida" för Raspberry Pi-produkter. Fokus låg på problemet att produktbeskrivningar kan ha olika längd. Hela produktkortet blev i sig ett `grid`, och dess "rader" tvingades anpassa sig så knappen (Köp) alltid hamnade snyggt längst ner, oavsett hur lång texten i kortet var.

**Nyckelexempel:**
```css
.kolumn {
    /* Gör själv kortet till ett grid */
    display: grid;
    /* Bild, Rubrik, Text(flexibel), Knapp */
    grid-template-rows: auto auto 1fr auto; 
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    background-color: white;
}
```
