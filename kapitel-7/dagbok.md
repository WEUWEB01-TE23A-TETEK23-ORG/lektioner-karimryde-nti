# Dagbok: Kapitel 7 – Grid Areas och Responsiv Webbutveckling

## Lektion 1: fem-favoriter (2026-01-15)

**Ämne:** Semantiska taggar och sidlayout (Fem svenska desserter)

**Nya begrepp:**
- Karta och områden för Grid Layout (`grid-template-areas`) introduceras som upplägg men den riktiga strukturen läggs här med Flex-navigering.

**Vad vi gjorde:**
Vi byggde en trevlig design för fem traditionella svenska desserter. Vi övade på att strukturera en sidhuvud-meny där länkarna justerades snyggt bredvid varandra. Repetitionen fokuserade mycket på box-strukturerna vi lärt oss i klassrummet.

**Nyckelexempel:**
```html
<nav>
    <a href="#">Semla</a>
    <a href="#">Prinsesstårta</a>
</nav>
```

---

## Lektion 2: holygrail (2026-01-21)

**Ämne:** Ap-bloggen och "Holy Grail"-layouten

**Nya begrepp:**
- `grid-template-areas` – Sätter ut namn för unika "zoner" i fönstret: `sidhuvud`, `sidebar`, `innehåll`, `sidfot`.
- `grid-area` – Kopplar in ett HTML-element till en zon beskriven ovan.
- Holy Grail Layout – Ett branschstandardmönster (header överst, innehåll + sidofält i mitten, och footer underst).

**Vad vi gjorde:**
Vi skapade layouten för en blogg som handlade om primater. Istället för att räkna rader och spalter (som i kapitel 6) använde vi namn på delarna och ritade upp dem i CSS. Vi gav HTML-taggarna sina respektive `grid-area` att infinna sig på.

**Nyckelexempel:**
```css
.kontainer {
    display: grid;
    grid-template-columns: 3fr 1fr;
    grid-template-areas: 
      "sidhuvud sidhuvud"
      "innehall sidebar"
      "sidfot sidfot";
    gap: 20px;
}
.header { grid-area: sidhuvud; }
.main { grid-area: innehall; }
.aside { grid-area: sidebar; }
.footer { grid-area: sidfot; }
```

---

## Lektion 3: neon-nudlar (2026-01-28)

**Ämne:** Uppstart – Neon Nudlar

**Nya begrepp:**
- Repetition av layoutstrategin.

**Vad vi gjorde:**
Vi skapade startfilerna och ett grundläggande skelett (index.html, style.css) för vad som skulle kunna bli en webbplats för en asiatisk neon-restaurang, som grund för att sedan bygga CSS Grid layouten i egna moment.

---

## Lektion 4: responsiv-sida (2026-02-11)

**Ämne:** Makak-apa och CSS Breakpoints

**Nya begrepp:**
- `@media (max-width: Xpx)` – Media Queries som "känner av" skärmens storlek, och därefter skriver om CSS.
- Mobilanpassad visning (Responsiv Design)
- Omsortering av grid – Exempelvis, göra att en tidigare `3fr 1fr` uppdelning kraschar ner i en enda rak pelare för mobilskärmar.

**Vad vi gjorde:**
Vi tog ett projekt som handlade om en "monkey selfie" och lärde fönstret att se annorlunda ut beroende på om besökaren var på dator, surfplatta eller mobiltelefon. När användaren krympte skärmen under 768px lades navigeringen i vertikala knappar istället för på en rad, och layouten omdefinierades från en två-spalts grid till singel-spalt.

**Nyckelexempel:**
```css
/* Grunddesignen (Desktop först) */
.kontainer {
    grid-template-areas: "meny innehall sidebar";
}

/* Om fönstret blir mindre än 768px (ex surfplatta/mobil) */
@media (max-width: 768px) {
    .kontainer {
        grid-template-areas: 
           "meny"
           "innehall"
           "sidebar";
    }
}
```
