# Dagbok: Kapitel 2 – Layout-grunder och bilder

## Lektion 1: fiji-reklam (2025-09-08)

**Ämne:** Fiji-reklamsida

**Nya begrepp:**
- `margin-left`, `margin-top` – Box-modellens yttre marginaler
- `text-transform: uppercase` – Transformerar all text till versaler
- `background-position` – Styr hur en bakgrundsbild placeras
- `text-decoration: none` – Tar bort understrykningen från länkar
- HTML-entiteter – Specialtecken, exempelvis pil (`&raquo;`)

**Vad vi gjorde:**
I den här lektionen byggde vi en annonssida för en resa till Fiji. Vi tittade på hur man centrerar en rubrik över en specifik del av bakgrunden, tog bort länkar och omvandlade dem till "knappar" visuellt.

**Nyckelexempel:**
```html
<a href="#" class="knapp">Läs mer &raquo;</a>
```
```css
a {
    text-transform: uppercase;
    text-decoration: none;
    margin-top: 50px;
}
body {
    background-image: url('bilder/fiji.jpg');
    background-position: center top;
}
```

---

## Lektion 2: portratt (2025-09-11)

**Ämne:** Porträttbilder och bildtexter

**Nya begrepp:**
- `<figure>` – Semantisk tagg som kapslar in medieinnehåll
- `<figcaption>` – Relaterad bildtext till en `<figure>`

**Vad vi gjorde:**
Vi påbörjade en lektion om att strukturera upp bilder för ett galleri eller personporträtt med HTML-elementen `<figure>` och `<figcaption>`.

**Nyckelexempel:**
```html
<figure>
    <img src="bilder/profil.jpg" alt="Porträtt">
    <figcaption>Bild över personen</figcaption>
</figure>
```
