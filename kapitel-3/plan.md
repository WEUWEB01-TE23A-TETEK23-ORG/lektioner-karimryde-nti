# Modulplan: div-boxar, klasser och layout

Kapitlet introducerar `<div>` som layout-verktyg, CSS-klasser för återanvändbar styling och CSS-reset för konsekvent utgångspunkt. Eleverna bygger visitkort, bloggar, recept och bildgallerier med strukturerad layout.

## Mål

- Använda `<div>` för att gruppera och strukturera innehåll.
- Skapa och använda CSS-klasser (`.kontainer`, `.box`, `.inlagg`).
- Tillämpa en enkel CSS-reset för konsekvent utgångspunkt.
- Definiera färgpaletter med CSS-variabler (`:root`).
- Använda `display: flex` för enkel horisontell layout.
- Bygga flersidig navigation med relativa länkar.

## Förkunskaper

- Kapitel 1: HTML-grundstruktur, rubriker, stycken, bilder, grundläggande CSS.
- Kapitel 2: marginaler, bildhantering.

## Nya begrepp

### HTML
`<div>`, `class`-attributet, `<ol>`, HTML-entiteter (`&raquo;`, `&laquo;`), flersidig struktur (arbete1.html–arbete6.html)

### CSS
CSS-reset (`box-sizing: border-box`, nollställning av margin/padding), `:root`-variabler (`--färgnamn: #hex`), `.klass`-selektorer, `display: flex`, `background-attachment: fixed`, `list-style-type`

## Pedagogiska grundregler

- `.kontainer`-mönstret introduceras och repeteras i varje lektion.
- CSS-reseten introduceras i visitkort och används konsekvent i alla efterföljande lektioner.
- CSS-variabler med Coolors.co-paletter ger professionellt utseende och lär namngivning.
- Varierande teman håller motivationen uppe: visitkort, recept, blogg, fotogalleri.

## Lektioner

### Lektion 1: visitkort med bakgrundsbild (mappen: visitkort)
- **Innehåll:** CSS-reset, `<div>` med fast `width`/`height`, positionerad text med `padding-left`/`padding-top`.
- **Mål:** förstå `<div>` som en "låda" man kan styla, introducera CSS-reset.

### Lektion 2: flersidig navigation (mappen: arbete)
- **Innehåll:** 6 länkade HTML-filer, `class`-attribut på `<body>` (`.sida1`–`.sida6`), relativa länkar, HTML-entiteter för pilar.
- **Mål:** kunna länka mellan flera sidor och använda klasser för att ge varje sida unikt utseende.
- **Repetition:** `<a>`, `background-image` från kapitel 1.

### Lektion 3: receptsida (mappen: scones)
- **Innehåll:** `.kontainer`, `background-attachment: fixed`, `border`, `box-shadow`, `<ol>`, nästlade `<ul>`, `list-style-type: square`.
- **Mål:** bygga en strukturerad sida med flera sektioner och dekorativ styling.
- **Repetition:** CSS-reset, `<div>`, `padding`, bakgrundsbilder.

### Lektion 4: blogglayout (mappen: bloggen)
- **Innehåll:** `:root`-variabler med Coolors.co-palett, `.inlagg`-klassen (blogginlägg), `.datum`, `.kontainer` med responsiv bredd.
- **Mål:** använda CSS-variabler för konsekvent färgtema, strukturera upprepat innehåll med klasser.
- **Repetition:** CSS-reset, `.kontainer`, `padding`, `background-color`.

### Lektion 5: bildgalleri med flex (mappen: bildgalleri)
- **Innehåll:** `display: flex` för horisontell layout, `.box`-klassen, `:root`-variabler, `width: 50%` för bildskalning.
- **Mål:** använda flexbox för att placera element bredvid varandra.
- **Repetition:** CSS-reset, `.kontainer`, klasser, CSS-variabler.

## Vanliga misstag

- Glömmer CSS-reseten — leder till oförutsägbara marginaler och padding.
- Skriver `.kontainer` i HTML (ska vara `class="kontainer"`, utan punkt).
- Förväxlar klass-syntax: `.kontainer` i CSS vs `class="kontainer"` i HTML.
- Relativa sökvägar i flersidig navigation (`arbete2.html` fungerar bara om filerna ligger i samma mapp).
- Glömmer `:root`-blocket — CSS-variablerna fungerar inte utan det.

## Resurser

- [Coolors.co](https://coolors.co/) — generera färgpaletter med semantiska namn.
- [Google Fonts](https://fonts.google.com/) — typsnitt.
