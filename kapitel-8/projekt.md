# Projekt – Min interaktiva sida

**Sammanfattning:** Bygg en interaktiv sida med JavaScript – läs input, uppdatera text och använd if/else-logik.

---

## Vad ska du göra?

Du ska skapa en sida med tre interaktiva sektioner. Du väljer själv temat – quiz, kalkylator, hälsnings-app, humörmätare eller något annat! Du får en färdig HTML-struktur och ett JS-skelett att utgå från. Din uppgift är att:

- Skriva klart de tre JavaScript-funktionerna
- Byta ut alla platshållare mot dina egna texter och rubriker
- Välja egna CSS-klasser för "rätt"/"fel" eller liknande feedback

---

## Scaffold – `index.html`

```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><!-- Fyll i din egen sidtitel --></title>
    <style>
        body {
            font-family: sans-serif;
            background-color: /* din bakgrundsfärg, t.ex. #f0f4f8 */ ;
            padding: 30px;
        }

        h1 {
            color: /* din rubrikfärg */ ;
        }

        .sektion {
            background-color: white;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 24px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }

        input {
            padding: 8px;
            font-size: 1em;
            margin-right: 8px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        button {
            padding: 8px 16px;
            font-size: 1em;
            background-color: /* din knappfärg, t.ex. #4a90e2 */ ;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        button:hover {
            opacity: 0.85;
        }

        /* Klass för godkänt resultat – byt ut färgen om du vill */
        .godkant {
            color: green;
            font-weight: bold;
        }

        /* Klass för underkänt resultat */
        .underkant {
            color: red;
            font-weight: bold;
        }

        /* Klass för dolt element – visas med .classList.toggle() */
        .dold {
            display: none;
        }
    </style>
</head>
<body>

    <h1><!-- Fyll i din egen rubrik --></h1>

    <!-- SEKTION 1: Hälsning -->
    <div class="sektion">
        <h2><!-- Rubrik, t.ex. "Hälsa på mig!" --></h2>
        <input type="text" id="namn-input" placeholder="<!-- T.ex. Skriv ditt namn -->">
        <!-- Din funktion anropas här via onclick -->
        <button onclick="halsaPaAnvandaren()"><!-- T.ex. "Hälsa" --></button>
        <p id="halsa-resultat"></p>
    </div>

    <!-- SEKTION 2: Färgväxlare -->
    <div class="sektion">
        <h2><!-- Rubrik, t.ex. "Byt bakgrundsfärg" --></h2>
        <input type="text" id="farg-input" placeholder="<!-- T.ex. Skriv en färg: red, blue, #ff0 -->">
        <!-- Din funktion anropas här -->
        <button onclick="bytFarg()"><!-- T.ex. "Byt färg" --></button>
        <p id="farg-resultat"></p>
    </div>

    <!-- SEKTION 3: Poängkoll med if/else -->
    <div class="sektion">
        <h2><!-- Rubrik, t.ex. "Kolla om du är godkänd" --></h2>
        <input type="number" id="poang-input" placeholder="<!-- T.ex. Skriv din poäng (0–100) -->">
        <!-- Din funktion anropas här -->
        <button onclick="kollaPoang()"><!-- T.ex. "Kolla poäng" --></button>
        <div id="poang-resultat"></div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

---

## Scaffold – `script.js`

```js
// FUNKTION 1: Hälsar på användaren
// Läs värdet från input med id="namn-input"
// Visa hälsningen i elementet med id="halsa-resultat"
function halsaPaAnvandaren() {
    // Skriv din kod här
}

// FUNKTION 2: Färgväxlare
// Läs värdet från input med id="farg-input"
// Sätt document.body.style.backgroundColor till det värdet
// Visa en bekräftelse i elementet med id="farg-resultat"
function bytFarg() {
    // Skriv din kod här
}

// FUNKTION 3: Poängkollen (if/else)
// Läs värdet från input med id="poang-input", konvertera med Number()
// Om poäng >= 70: visa "Godkänt! 🎉" och lägg till klassen "godkant" på resultat-div
// Annars: visa "Underkänt 😢" och lägg till klassen "underkant" på resultat-div
// Tips: ta bort den gamla klassen först med .classList.remove() innan du lägger till en ny
function kollaPoang() {
    // Skriv din kod här
}
```

---

## Krav

Bocka av allt innan du lämnar in:

- [ ] Minst en funktion som läser från `<input>` med `.value`
- [ ] Minst en funktion som uppdaterar text med `.textContent`
- [ ] Minst en `if/else`-sats
- [ ] Minst en `.classList`-operation (`.add()`, `.remove()` eller `.toggle()`)
- [ ] Alla tre funktioner är kopplade till knappar via `onclick`
- [ ] Eget innehåll – inga platshållar-kommentarer kvar i det du visar

---

## Bonusutmaningar

⭐ **Lätt** – Lägg till en "Rensa"-knapp som tömmer alla tre resultat-fält (sätt `.textContent = ""`) och tar bort CSS-klasserna `godkant` och `underkant`.

⭐⭐ **Medel** – Lägg till ett fjärde input-fält: om användaren skriver rätt lösenord (ett du väljer), visa ett dolt meddelande via `.classList.toggle('dold')`. Börja med att ge meddelandet klassen `dold` i HTML.

⭐⭐⭐ **Svår** – Bygg en enkel räknare med tre knappar: **+1**, **−1** och **Nollställ**. Spara nuvarande tal i en `let`-variabel och uppdatera ett `<p>`-element med `.textContent` varje gång en knapp klickas. Använd inga `prompt()`, loopar eller arrayer.
