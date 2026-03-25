# Labb 3 – miniräknaren

Snyggt jobbat med de första labbarna! Du kan nu ändra färger, gömma element och byta ut text med JavaScript. Men hittills har vi inte läst in något som användaren *skriver* på sidan. Det är dags att ändra på det!

## Introduktion och mål

I den här labben bygger vi en miniräknare där användaren skriver in data direkt på sidan via `<input>`-fält. Du kommer att träna på att:

* Läsa text från ett input-fält med `.value`.
* Omvandla text till siffror med `Number()`.
* Visa resultat på sidan med `.textContent` (repetition).
* Ändra stil med `.style` beroende på resultat (repetition).
* Använda `if`/`else` för att hantera specialfall.

## Startkod för webbsidan

Skapa tre filer: `index.html`, `style.css` och `script.js`. Kopiera in koden nedan.

**index.html:**

```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Miniräknaren</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1 class="huvudrubrik">🔢 Miniräknaren</h1>
        <p class="info-text">Skriv in värden och klicka för att räkna!</p>

        <div class="input-grupp">
            <input type="text" class="tal1" placeholder="Första talet">
            <input type="text" class="tal2" placeholder="Andra talet">
        </div>

        <div class="knapp-panel">
            <button onclick="addera()">+ Addera</button>
            <button onclick="subtrahera()">− Subtrahera</button>
            <button onclick="multiplicera()">× Multiplicera</button>
            <button onclick="dividera()">÷ Dividera</button>
        </div>

        <div class="resultat-ruta">
            <p class="resultat">Resultatet visas här</p>
        </div>

        <div class="extra-sektion">
            <h2>Namnhälsaren</h2>
            <input type="text" class="namn-input" placeholder="Skriv ditt namn">
            <button onclick="halsning()">Hälsa!</button>
            <p class="halsning-text">...</p>
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

**style.css:**

```css
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #1a1a2e;
    color: #eee;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    margin: 0;
}

.container {
    background: #16213e;
    padding: 40px;
    border-radius: 15px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.4);
    text-align: center;
    max-width: 500px;
    width: 90%;
}

h1 {
    margin-bottom: 5px;
}

#info-text {
    color: #aaa;
    margin-bottom: 20px;
}

.input-grupp {
    display: flex;
    gap: 10px;
    justify-content: center;
    margin-bottom: 15px;
}

input {
    padding: 12px;
    border: 2px solid #0f3460;
    border-radius: 8px;
    background: #1a1a2e;
    color: white;
    font-size: 1.1rem;
    text-align: center;
    width: 140px;
}

input:focus {
    border-color: #e94560;
    outline: none;
}

.knapp-panel {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    justify-content: center;
    margin-bottom: 20px;
}

button {
    padding: 12px 20px;
    border: none;
    border-radius: 8px;
    background-color: #0f3460;
    color: white;
    cursor: pointer;
    font-weight: bold;
    font-size: 1rem;
    transition: 0.2s;
}

button:hover {
    background-color: #e94560;
    transform: scale(1.05);
}

.resultat-ruta {
    background-color: #0f3460;
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 30px;
}

#resultat {
    font-size: 1.5rem;
    font-weight: bold;
    margin: 0;
}

.extra-sektion {
    border-top: 1px solid #0f3460;
    padding-top: 20px;
}

.extra-sektion input {
    width: 200px;
    margin-bottom: 10px;
}
```

## Övningar och kodexempel

### Övning 1: läsa text från ett input-fält

Varje `<input>`-fält i HTML har en egenskap som heter `.value`. Den innehåller det som användaren just nu har skrivit i fältet. Så här läser man ut det:

```javascript
function halsning() {
    // 1. Hämta input-fältet
    let namnFalt = document.querySelector(".namn-input");

    // 2. Läs ut vad som står i fältet
    let namn = namnFalt.value;

    // 3. Visa en hälsning med textContent (repetition!)
    let text = document.querySelector(".halsning-text");
    text.textContent = "Hej på dig, " + namn + "! Välkommen hit!";
}
```

### Övning 2: räkna med Number()

Allt som kommer från ett input-fält är **text** (en sträng). Om du skriver `"5" + "3"` får du `"53"`, inte `8`! Därför måste vi omvandla med `Number()`:

```javascript
function addera() {
    // 1. Hämta värdena från input-fälten
    let a = document.querySelector(".tal1").value;
    let b = document.querySelector(".tal2").value;

    // 2. Omvandla från text till siffror
    let siffra1 = Number(a);
    let siffra2 = Number(b);

    // 3. Räkna ut summan
    let summa = siffra1 + siffra2;

    // 4. Visa resultatet på sidan
    document.querySelector(".resultat").textContent = "Summan är: " + summa;
}
```

## Uppgifter – från nybörjare till matteproffs

Skriv alla funktioner i `script.js`. Startkoden har redan knappar och input-fält redo att användas.

### Nivå 1: uppvärmning (mycket enkelt)

**Uppgift 1: subtrahera**
Skriv funktionen `subtrahera()` som läser de två talen från input-fälten, omvandlar dem med `Number()` och visar skillnaden i `#resultat`. Kopiera mönstret från övning 2 — byt bara ut `+` mot `-`.

**Uppgift 2: hälsning med stil**
Bygg vidare på `halsning()`-funktionen. Förutom att visa hälsningen, ändra också textfärgen på `.halsning-text` till grön. (Repetition: `style.color` från labb 1–2!)

### Nivå 2: fler räknesätt (enkelt)

**Uppgift 3: multiplicera**
Skriv funktionen `multiplicera()` som visar produkten av de två talen. Multiplikationstecknet i JavaScript är `*`.

**Uppgift 4: dividera**
Skriv funktionen `dividera()` som visar kvoten. Divisionstecknet i JavaScript är `/`.

### Nivå 3: smartare resultat (medel)

**Uppgift 5: färgkodade resultat**
Bygg ut valfri räknefunktion så att resultat-rutan ändrar bakgrundsfärg beroende på svaret:
- Om resultatet är positivt (större än 0): grön bakgrund.
- Om resultatet är negativt (mindre än 0): röd bakgrund.
- Om resultatet är exakt 0: gul bakgrund.

*(Tips: `if (summa > 0) { ... } else if (summa < 0) { ... } else { ... }`)*

**Uppgift 6: nollkontroll vid division**
Bygg ut `dividera()` med en `if`-sats. Om det andra talet är `0`, visa texten `"Kan inte dela med noll!"` och ändra resultatfärgen till röd. Annars visa resultatet som vanligt.

### Nivå 4: kombination (avancerat)

**Uppgift 7: färgväljaren**
Lägg till ett nytt input-fält i HTML med class `farg-input` och en ny knapp "Byt färg". Skriv en funktion som läser färgnamnet (t.ex. "purple") och ändrar hela sidans bakgrund till det. (Repetition: `document.body.style.backgroundColor` från labb 1!)

**Uppgift 8: namnbyte på rubriken**
Skapa en knapp "Döp om sidan". Funktionen ska använda `prompt()` för att fråga användaren om ett nytt namn och sedan uppdatera `.huvudrubrik` med svaret. (Repetition: `prompt()` och `.textContent` från labb 2!)

### Nivå 5: boss-nivån

**Uppgift 9: temperaturomvandlaren**
Lägg till ett nytt input-fält och en knapp "Räkna om °C → °F". Funktionen ska:

1. Läsa grader Celsius från input-fältet.
2. Omvandla till Fahrenheit med formeln: `fahrenheit = celsius * 9 / 5 + 32`.
3. Visa resultatet i `#resultat`, t.ex. `"25°C = 77°F"`.
4. Ändra bakgrundsfärg på resultat-rutan: blå om det är under 0°C, grön om 0–25°C, röd om över 25°C.

**Uppgift 10: den ultimata räknaren**
Bygg ut miniräknaren så att:

1. Rubriken ändras till `"Senaste beräkningen:"` varje gång man räknar.
2. Resultat-rutan visar hela uträkningen, t.ex. `"12 + 8 = 20"`.
3. Om svaret är över 100, ändra resultat-textens färg till guld (`"gold"`).
4. Om svaret är negativt, ändra textfärgen till röd och visa texten `"⚠️ Negativt resultat!"` i `.info-text`.
