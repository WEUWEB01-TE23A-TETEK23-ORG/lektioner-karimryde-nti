# Modulplan: CSS Grid och kortlayouter

Kapitlet introducerar CSS Grid som layoutsystem. Eleverna bygger kortbaserade sidor (menyrutor, produktkort) med rutnät, hover-animationer och kombinerad flex- och grid-layout.

## Mål

- Skapa rutnätslayout med `display: grid` och `grid-template-columns`.
- Använda `1fr`-enheten för jämna kolumner.
- Styra avstånd i grid med `gap`.
- Skapa hover-animationer med `transition` och `linear-gradient`.
- Kombinera flexbox (navigation) och grid (innehåll) i samma sida.
- Använda nested grids (grid inuti grid).

## Förkunskaper

- Kapitel 1–3: HTML-struktur, CSS-klasser, `.kontainer`, CSS-reset.
- Kapitel 4: navigation, `.aktiv`-klass, hover-effekter.

## Nya begrepp

### CSS
`display: grid`, `grid-template-columns`, `1fr`, `gap`, `repeat()`, `transition`, `linear-gradient()`, `background-position` (animerad), `background-size`, `grid-template-rows`, nested grid, `justify-content: space-between` (i flex-nav)

## Pedagogiska grundregler

- Grid introduceras med verkliga exempel (Burger King-meny, Raspberry Pi-produkter) — inte abstrakta rutor.
- `.rutnat`-klassen används konsekvent som namn för grid-containern.
- `.box` eller `.kolumn` används för individuella kort.
- Hover-effekter ger omedelbar visuell feedback vid interaktion.

## Lektioner

### Lektion 1: burgarmeny med grid (mappen: burger-meny)
- **Innehåll:** `display: grid`, `grid-template-columns: 1fr 1fr 1fr`, `gap`, `.rutnat`, `.box`, `linear-gradient` med `transition` för hover-animation, flexbox-navigation med `justify-content: space-between`.
- **Mål:** förstå CSS Grid som ett rutnätssystem och skapa kortlayouter.
- **Repetition:** CSS-reset, `.kontainer`, klasser, hover-effekter, navigering.

### Lektion 2: produktsida med nested grid (mappen: raspberrypi)
- **Innehåll:** `.kolumner-3` grid-container, `.kolumn` med `grid-template-rows: auto auto 1fr auto`, nested grid för kortets interna layout, `box-shadow` på hover.
- **Mål:** använda grid för både övergripande layout och kortens inre struktur.
- **Repetition:** `display: grid`, `1fr`, `gap`, hover-effekter, `.kontainer`.

## Vanliga misstag

- Förväxlar `grid-template-columns` och `grid-template-rows`.
- Glömmer `gap` — korten klibbar ihop.
- Skriver `1fr 1fr 1f` (stavfel i enheten).
- Sätter `display: grid` på varje kort istället för enbart på containern.
- Glömmer `transition`-egenskapen — hover-effekten blir hackig istället för mjuk.
