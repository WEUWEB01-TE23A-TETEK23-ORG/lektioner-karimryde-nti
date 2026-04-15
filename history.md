# Kurshistorik – Webbutveckling 1 (WEUWEB01)

Här är vår gemensamma, kronologiska dagbok över allt vi har gjort under kursens gång. Om du undrar när vi gick igenom ett visst begrepp eller letar efter kodexempel från en specifik lektion är det här rätt plats att titta!

**Tips:** Klicka dig in i kapitel-mapparna för att hitta sidornas källkod och läsa lektionens hela `dagbok.md`.

---

## Sammanfattning: Lektion för lektion

| Datum | Kapitel | Lektion (Mapp) | Vad vi gjorde |
|-------|---------|----------------|---------------|
| 2025-08-22 | Kap 1 | intro | Första HTML-sidan någonsin (Namn och adress) |
| 2025-08-27 | Kap 1 | pippi | Biografi över Pippi (Bilder, text och listor) |
| 2025-08-28 | Kap 1 | beatles | Vår första introduktion till CSS (Beatles) |
| 2025-09-03 | Kap 1 | oppna-landskap | Externt typsnitt och layout-skuggor |
| 2025-09-04 | Kap 1 | veckomeny | Veckomeny uppbyggd med HTML-tabeller |
| 2025-09-08 | Kap 2 | fiji-reklam | Reklamsida, fusk-knappar med CSS och bakgrunder |
| 2025-09-11 | Kap 2 | portratt | Porträttgalleri med Figure och Figcaption |
| 2025-09-29 | Kap 3 | visitkort | Digitalt visitkort, vi testade CSS-Reset och Div-boxar |
| 2025-10-02 | Kap 3 | arbete | Länkning mellan sex olika HTML-filer ("Arbete") |
| 2025-10-06 | Kap 3 | scones | Engelskt scones-recept (`ol`/`ul`-listor i en Kontainer) |
| 2025-10-09 | Kap 3 | bloggen | Färgpaletter med CSS-variabler (`:root`) i en blogg |
| 2025-10-13 | Kap 3 | bildgalleri | Bildgalleri för NASA och introduktion till Flexbox |
| 2025-11-06 | Kap 4 | webbplats | Skarp flersidig webbplats med en designad navigationsmeny |
| 2025-11-12 | Kap 6 | raspberrypi | Nästlade grids för att lösa e-handelsprodukter |
| 2025-11-19 | Kap 6 | burger-meny | Rutnätslayout för en hamburgermeny med CSS Grid och Hover-effekt |
| 2025-11-20 | Kap 4 | rep-webbplats | Genreps-lektion inför praktiskt prov, vi stylade upp "5 biofilmer" |
| 2026-01-15 | Kap 7 | fem-favoriter | Layoutträning med "5 svenska desserter" och Flex-meny |
| 2026-01-21 | Kap 7 | holygrail | Branschstandard-layout (Holy Grail med `grid-template-areas`) |
| 2026-01-28 | Kap 7 | neon-nudlar | Start av nytt projekt, grundskelett |
| 2026-02-11 | Kap 7 | responsiv-sida | Vi gjorde vår webbsida anpassningsbar för mobiler (`@media` min-width) |
| 2026-03-12 | Kap 8 | intro | Introduktion till JavaScript! `let`, `prompt` och `alert`. |
| 2026-03-18 | Kap 8 | grunder / kaboom | Egendefinierade funktioner för knappar (`onclick="funktion()"`) |
| 2026-03-19 | Kap 8 | stilar / tagg | Att byta CSS och design direkt med JS (`document.querySelector`) |
| 2026-03-31 | Kap 8 | automation | Uppgradering av AI-modellen för automatisk dokumentation |
| 2026-04-15 | Kap 8 | automation-v2 | Miljövariabler och robustare hantering av konfiguration |

---

## Detaljerad tidslinje

Här beskrivs i lite mer detalj hur vi bit för bit byggt upp vår webbutvecklingskompetens.

### Höstterminen 2025 – Från noll till hela webbplatser

**Augusti: Den första koden (HTML:s födelse)**
- **(22 aug) Intro:** Allt började med en väldigt enkel vit sida där vi satte in *h1* (och h2). Vi lärde oss grundbulten av `<!DOCTYPE html>`.
- **(27 aug) Pippi:** Nu krävdes det bilder. Vi lade in `<img>` och kombinerade med `<ul>` onumrerade listor. Sidan saknade fortfarande kläder.
- **(28 aug) Beatles:** Vår allra första kontakt med `style.css`. All kod för utseendet bröts därmed loss från HTML-filen i ett eget ekosystem, där vi justerade bakgrund, färg och typsnitt.

**September: Layout, tabeller & klassbeteckningar**
- **(3 sep) Öppna landskap:** Förfinade utseendet med att dra in skuggor och `padding` och lånade in typsnittet Roboto från Google Fonts.
- **(4 sep) Veckomeny:** Vi strukturerade data, här i form av en skolans matsedel i en klassisk `<table>`.
- **(8 sep) Fiji-reklam:** Vi lärde oss styra text, tvinga fram VERSALER (`text-transform`) och bygga designade länkar som såg ut som massiva stora klickknappar.
- **(29 sep) Visitkort:** `<div>`-lådan dök upp på scenen! Från och med nu packade vi in allt vi byggde i logiska boxar via strukturen `.kort {}`.

**Oktober: Multipla sidor, variabler och Flexbox**
- **(2 okt) Sidor & länkningar:** Vi lärde oss hoppa fram och tillbaka mellan `sida1.html` -> `sida3.html`.
- **(6 okt) Scones:** Vi lät en snygg bakgrundsbild låsa sig (`background-attachment: fixed`) medan det centrerade vita .kontainer innehållet rullade förbi över bilden.
- **(9 okt) Bloggen:** Magin med `:root`. Istället för att klistra in `#e63946` på 80 ställen, sparade vi färgen i en gemensam färgvariabel som styrde hela bloggens färgtema.
- **(13 okt) NASA Bildgalleri:** *Flexbox* presenterades, som lätt är det populäraste sättet att hantera linjära layouter i nutidens webbdesign. Sätt `display: flex` och elementen lägger sig snällt på rad.

**November: Grid och Provförberedelser**
- **(6 nov) Fem favoritband:** Ett fullskaligt projekt vi lade mycket tid på att färdigställa och gav en "Navigationsmeny" som ljyste gul på den `.aktiv`:a sidan användaren besökte.
- **(12-19 nov) CSS Grid:** Här lärde vi oss bygga riktiga rutnät för Raspberry Pi-produkter och en simulerad Burger King-meny (`display: grid`, med `grid-template-columns: 1fr 1fr 1fr`). Vi tillfogade mjuk Animation `transition` när muspekaren nuddade en burgare.

---

### Vårterminen 2026 – Responsiv layout & JavaScript

**Januari: Holy Grail och struktur i Grid**
- **(15 jan) Fem desserter:** Träning att fräscha upp minnet efter jullovet.
- **(21 jan) Holy Grail:** Här introducerades metoden att rentav döpa de olika layout-delarna och diktera upp en visuell tavla (exempel: `"header header"`, `"main aside"`, `"footer footer"`) för att blixtsnabbt skissa upp bloggar och e-handlar.

**Februari: Responsivitet (Mobilanpassning)**
- **(11 feb) Responsiva makaker:** Via kommandot `@media (max-width: 768px)` sade vi åt CSS:en att blixtsnabbt avbryta och skriva över alla tidigare färg- och positionsregler sekunden som skärmen drogs ihop från datormonitor, till en liten telefonskärm. Navigeringen lade sig därmed på höjden under varandra istället för på bredden.

**Mars: JavaScript och Moderna Arbetsflöden**
- **(12-18 mar) Hjärnan i verket / Funktioner:** Vi slutade rita mallar och började skriva rader som faktiskt *gjorde* saker (Logik). Via `prompt` fick eleverna mata in namn och värden, som vi sedan snappade upp i minnet ifrån våra metoder. Vi gav knapparna `onclick='funktion()'` och om användaren svarade fel använde vi `if / else` logik.
- **(19 mar) Styla om sidan live:** Genom DOM-manipulering lärde vi oss att manövreringsverktyget `document.querySelector('h1')` kunde infånga vilken HTML-tagg som helst i koden och injicera in ny `.style.color` till den direkt.
- **(31 mar) Automation med AI:** Vi avslutade mars med att titta på hur vi kan automatisera våra projekt. Vi lärde oss att GitHub Actions kan sköta tråkiga uppgifter åt oss och hur vi enkelt kan uppgradera kraftfulla AI-modeller (som Gemini) genom att bara ändra en rad i en konfigurationsfil.

**April: Avancerad kodstruktur**
- **(15 apr) Robustare verktyg och miljövariabler:** Vi förfinade vår dokumentationsprocess ytterligare. Genom att bygga smartare logik i Python lärde vi oss hur man använder miljövariabler för att konfigurera program utan att ändra i koden. Detta gör våra skript säkrare och mer professionella, då vi nu kan byta AI-modell utan att riskera att gå sönder koden. Vi diskuterade också vikten av att filtrera bort metadata och systemfiler för att hålla våra projekt rena.