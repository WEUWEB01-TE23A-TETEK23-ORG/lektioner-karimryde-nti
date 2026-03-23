# Modulplan: javascript-introduktion (webbutveckling 1)

Denna plan speglar genomförda lektioner och sätter kursen för kommande moment. Varje lektion börjar med repetition av föregående lektion för att befästa kunskapen genom extrem mängdträning och visuell feedback.

## Mål

- Förstå att JavaScript kan manipulera en webbsida i realtid.
- Använda `let` för att lagra värden i variabler.
- Hämta input från användaren med `prompt()` och visa resultat med `alert()`.
- Skapa namngivna funktioner och koppla dem till HTML via `onclick`.
- Ändra sidans utseende med `document.body.style` och `document.querySelector().style`.
- Uppdatera text på sidan med `.textContent`.
- Läsa formulärdata med `.value` och konvertera med `Number()`.
- Växla CSS-klasser med `.classList.add()`, `.remove()` och `.toggle()`.
- Skriva enkel logik med `if`, `else if` och `else`.

## Förkunskaper

- Kapitel 1–7: HTML-struktur, CSS-klasser, CSS Grid, responsiv design.
- Eleverna ska kunna bygga en komplett flersidig webbplats med styling innan JavaScript introduceras.

## Nya begrepp

### JavaScript
`let`, `prompt()`, `alert()`, `console.log()`, `function`, `onclick` (HTML-attribut), `onmouseover`, `document.body.style`, `document.querySelector()`, `.style`, `.textContent`, `.value`, `Number()`, `.classList.add()`, `.classList.remove()`, `.classList.toggle()`, `if`, `else if`, `else`, `==` (jämförelse)

## Pedagogiska grundregler
* **Meningsversal:** endast första ordet i rubriker börjar med stor bokstav.
* **Extrem repetition:** varje nytt koncept övas 3–5 gånger.
* **Visuell feedback:** varje rad kod ska ge en direkt och synlig effekt på webbsidan.
* **Hård begränsning:** inga loopar, arrayer eller komplexa funktioner. Vi stannar vid variabler, if-satser, `.textContent`, `.value`, `.classList` och enkel DOM-manipulering.

---

## Genomförda lektioner (referensmaterial i mappar)

### Lektion 1: intro till js (mappen: intro)
* **Innehåll:** hur man skriver JS, `alert()`, variabler (`let`), `prompt()`, strängkonkatenering och en första enkel `if`-sats.
* **Mål:** förstå att JS kan prata med användaren via popup-rutor.

### Lektion 2: inmatning & funktioner (mappar: grunder, kaboom)
* **Innehåll:** mer träning på `prompt()` och variabler. Introduktion av funktioner (`function`) för att gruppera kod som körs vid händelser.
* **Mål:** lära sig att "paketera" kod och anropa den (t.ex. via `onclick`).

### Lektion 3: styra utseende med js (mappar: stilar, stilar-tagg)
* **Innehåll:** `document.body.style` och `document.querySelector().style`. Ändra färger, bilder, typsnitt och marginaler.
* **Mål:** förstå att JS kan manipulera CSS direkt för att ändra sidans utseende.

---

## Kommande lektioner (framåtplanering)

### Lektion 4: hejdå alert, hej .textContent!
* **Repetition (från lektion 3):** ändra färger och styling på element via knappar.
* **Nytt koncept:** `document.querySelector().textContent` för att skriva text på sidan.
* **Lektionens skelett:**
    1. **Demo:** en knapp som ändrar både bakgrundsfärg (repetition) och texten i en rubrik (nytt).
    2. **Övning 1:** skapa en knapp som ändrar texten i en paragraf.
    3. **Övning 2:** skapa en knapp som ändrar texten i en `h2`.
    4. **Övning 3:** skapa en knapp som byter ut texten i tre olika rutor samtidigt.
    5. **Övning 4 (kombination):** en knapp som ändrar färg på en ruta och skriver ut "Färgen är nu röd" i rutan.

### Lektion 5: .value & number() – läsa från formulär
* **Repetition (från lektion 4):** uppdatera text på sidan med `.textContent`.
* **Nytt koncept:** `<input>`, `.value` och `Number()` för att hämta data från användaren.
* **Lektionens skelett:**
    1. **Demo:** läs ett namn från en input och visa det i en hälsning via `.textContent`.
    2. **Övning 1 (härmapan):** skriv i en input och visa texten i en paragraf när man klickar på en knapp.
    3. **Övning 2 (färgväljaren):** skriv ett färgnamn (t.ex. "red") i en input och ändra sidans bakgrundsfärg.
    4. **Övning 3 (enkel addition):** två input-fält för siffror. Visa summan på sidan med `Number()`.
    5. **Övning 4 (kombination):** mata in ett namn och en favoritfärg. Uppdatera en ruta med både namnet och färgen.

### Lektion 6: .classList – proffsig styling
* **Repetition (från lektion 5):** läsa data från input-fält (`.value`) och visa resultat.
* **Nytt koncept:** `.classList.add()`, `.remove()` och `.toggle()` för att växla mellan färdiga CSS-klasser.
* **Lektionens skelett:**
    1. **Demo:** skriv "mörkt" i en input för att lägga till klassen `.dark` på body.
    2. **Övning 1:** en knapp som tänder/släcker en ram runt en bild med `.toggle('ram')`.
    3. **Övning 2:** tre knappar ("Varning", "Succé", "Info") som lägger till olika CSS-klasser på en ruta.
    4. **Övning 3:** en knapp som både byter klass och uppdaterar texten i en ruta.
    5. **Övning 4 (kombination):** om användaren skriver "hemligt" i en input, lägg till en klass som visar ett dolt meddelande.

### Lektion 7: logik & kombination (finalen)
* **Repetition (från lektion 6):** växla mellan CSS-klasser via `.classList`.
* **Nytt koncept:** fördjupning i `if`, `else if` och `else` för att skapa smartare appar.
* **Lektionens skelett:**
    1. **Demo:** en "dörrvakt" – om åldern i input är under 18, lägg till klassen `.red` och ändra texten till "Nekad".
    2. **Övning 1 (betygskollen):** mata in poäng (0-100). visa betyg och ändra färg på resultatet (grön för godkänt, röd för F).
    3. **Övning 2 (gissa ordet):** en enkel ordgissning. om rätt ord skrivs in, visa en vinstbild och byt tema på sidan.
    4. **Övning 3 (bmi-kalkylator):** en enkel räknare som ger olika textmeddelanden beroende på resultatet.
    5. **Övning 4 (fritt skapande):** eleverna bygger en egen liten interaktiv app som kombinerar allt de lärt sig.

---

## Vanliga misstag

- Skriver `=` (tilldelning) istället för `==` (jämförelse) i `if`-satser.
- Glömmer `Number()` vid beräkningar — `"5" + "3"` blir `"53"` istället för `8`.
- Felaktig `querySelector`-syntax: glömmer punkt för klass (`.klass`) eller citattecken.
- HTML:en refererar till en funktion som inte finns i `script.js` (stavfel i funktionsnamn).
- Glömmer `<script src="script.js"></script>` sist i `<body>`.
- Blandar ihop `.textContent` (text) och `.value` (formulärfält).
- Skriver `classList.add(klass)` utan citattecken: ska vara `classList.add("klass")`.

## Pedagogisk strategi (från gemini.md)
1. **Extrem repetition:** varje nytt koncept övas 3–5 gånger.
2. **Visuell feedback:** varje rad kod ska synas på skärmen.
3. **Inga avancerade koncept:** inga loopar, arrayer eller komplexa objekt.
