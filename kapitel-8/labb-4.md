# Labb 4 – dark mode och tema-växlare

Du kan nu ändra färger, byta text och läsa input. Men hittills har vi ändrat design med `style` direkt i JavaScript — en egenskap i taget. Det finns ett smidigare sätt: att växla hela CSS-klasser på en gång! Då skriver man designen i CSS och styr den med JavaScript.

## Introduktion och mål

I den här labben bygger vi en sida med tema-växlare. Du kommer att träna på att:

* Lägga till CSS-klasser med `.classList.add()`.
* Ta bort CSS-klasser med `.classList.remove()`.
* Växla klasser av och på med `.classList.toggle()`.
* Kombinera `.classList` med `.textContent` och `.value` (repetition).
* Använda `if`/`else` för att reagera på användarens val (repetition).

## Startkod för webbsidan

Skapa tre filer: `index.html`, `style.css` och `script.js`. Kopiera in koden nedan.

**index.html:**

```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tema-växlaren</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1 class="huvudrubrik">🎨 Tema-växlaren</h1>
        <p class="info-text">Klicka på knapparna för att byta utseende!</p>

        <div class="kort">
            <img src="https://picsum.photos/400/200?random=1" alt="Slumpbild">
            <h2 class="kort-rubrik">Mitt fina kort</h2>
            <p class="kort-text">Det här kortet kan ändra utseende med classList!</p>
        </div>

        <div class="knapp-panel">
            <button onclick="darkMode()">🌙 Dark mode</button>
            <button onclick="lightMode()">☀️ Light mode</button>
            <button onclick="toggleDark()">🔄 Växla</button>
        </div>

        <div class="knapp-panel">
            <button onclick="temaCyber()">💜 Cyber</button>
            <button onclick="temaNatur()">🌿 Natur</button>
            <button onclick="temaRetro()">🕹️ Retro</button>
        </div>

        <div class="extra-sektion">
            <h2>Välj tema med text</h2>
            <input type="text" class="tema-input" placeholder="Skriv ett temanamn">
            <button onclick="valjTema()">Aktivera tema</button>
            <p class="tema-status">...</p>
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
    background-color: #f0f0f0;
    color: #333;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    margin: 0;
    transition: 0.4s;
}

.container {
    background: white;
    padding: 40px;
    border-radius: 15px;
    box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    text-align: center;
    max-width: 500px;
    width: 90%;
    transition: 0.4s;
}

.kort {
    border: 2px solid #ddd;
    border-radius: 10px;
    overflow: hidden;
    margin: 20px 0;
    transition: 0.4s;
}

.kort img {
    width: 100%;
}

.kort h2, .kort p {
    padding: 0 15px;
}

.knapp-panel {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    justify-content: center;
    margin-bottom: 15px;
}

button {
    padding: 12px 18px;
    border: none;
    border-radius: 8px;
    background-color: #6c757d;
    color: white;
    cursor: pointer;
    font-weight: bold;
    font-size: 1rem;
    transition: 0.2s;
}

button:hover {
    transform: scale(1.05);
    background-color: #5a6268;
}

input {
    padding: 12px;
    border: 2px solid #ddd;
    border-radius: 8px;
    font-size: 1rem;
    text-align: center;
    width: 200px;
    margin-bottom: 10px;
}

.extra-sektion {
    border-top: 1px solid #ddd;
    padding-top: 20px;
    margin-top: 10px;
}

/* ===== TEMAKLASSER ===== */

/* Dark mode */
body.dark {
    background-color: #1a1a1a;
    color: #e0e0e0;
}

body.dark .container {
    background-color: #2d2d2d;
    box-shadow: 0 10px 20px rgba(0,0,0,0.5);
}

body.dark .kort {
    border-color: #444;
}

body.dark input {
    background-color: #333;
    color: white;
    border-color: #555;
}

/* Cybertema */
body.cyber {
    background-color: #0a0a23;
    color: #00ffff;
}

body.cyber .container {
    background-color: #1a1a3e;
    border: 1px solid #00ffff;
}

body.cyber .kort {
    border-color: #ff00ff;
}

body.cyber button {
    background-color: #ff00ff;
}

/* Naturtema */
body.natur {
    background-color: #2d5016;
    color: #e8f5e9;
}

body.natur .container {
    background-color: #1b5e20;
}

body.natur .kort {
    border-color: #81c784;
}

body.natur button {
    background-color: #4caf50;
}

/* Retrotema */
body.retro {
    background-color: #fff3cd;
    color: #6d4c41;
}

body.retro .container {
    background-color: #ffe0b2;
    border: 3px dashed #e65100;
}

body.retro .kort {
    border-color: #e65100;
}

body.retro button {
    background-color: #e65100;
}

/* Ram runt kort */
.kort.ram {
    border: 4px solid gold;
    box-shadow: 0 0 15px rgba(255, 215, 0, 0.5);
}

/* Markering */
.kort.markerad {
    background-color: #fff9c4;
}
```

## Övningar och kodexempel

### Övning 1: lägga till en klass

Med `.classList.add()` lägger vi till en CSS-klass på ett element. Det är som att skriva `class="dark"` direkt i HTML — fast vi gör det med JavaScript!

```javascript
function darkMode() {
    document.body.classList.add("dark")
}
```

### Övning 2: ta bort en klass

Med `.classList.remove()` tar vi bort klassen igen:

```javascript
function lightMode() {
    document.body.classList.remove("dark")
}
```

### Övning 3: växla en klass av och på

Med `.classList.toggle()` slipper du skriva två funktioner. Den lägger till klassen om den saknas, och tar bort den om den redan finns:

```javascript
function toggleDark() {
    document.body.classList.toggle("dark")
}
```

## Uppgifter – från nybörjare till temamästare

Skriv alla funktioner i `script.js`.

### Nivå 1: uppvärmning (mycket enkelt)

**Uppgift 1: aktivera cybertema**

* Skriv funktionen `temaCyber()` som lägger till klassen `"cyber"` på body.
* Kopiera mönstret från övning 1.

**Uppgift 2: aktivera naturtema**

* Skriv funktionen `temaNatur()` som lägger till klassen `"natur"` på body.

### Nivå 2: byta mellan teman (enkelt)

**Uppgift 3: rensa före byte**

* Problemet med uppgift 1–2 är att klasserna staplas! Om du klickar “Cyber” och sedan “Natur” har body *båda* klasserna.
* Fixa alla temafunktioner så att de först tar bort alla andra temaklasser med `classList.remove()` innan de lägger till sin. Exempel:

```javascript
function temaCyber() {
    document.body.classList.remove("dark")
    document.body.classList.remove("cyber")
    document.body.classList.remove("natur")
    document.body.classList.remove("retro")
    document.body.classList.add("cyber")
}
```

**Uppgift 4: retrotema**

* Skriv funktionen `temaRetro()` som (precis som uppgift 3) rensar alla teman och sedan lägger till `"retro"`.

### Nivå 3: kombinera classList med text (medel)

**Uppgift 5: ram runt kortet**

* Skapa en knapp "Gyllene ram" i HTML.
* Skriv en funktion som växlar klassen `"ram"` på kortet (`.kort`) med `classList.toggle()`.
* Varje klick ska slå av eller på ramen.

**Uppgift 6: uppdatera statustext**

* Bygg vidare på temafunktionerna.
* Varje gång ett tema aktiveras, uppdatera `.info-text` med vilket tema som är aktivt, t.ex. `"Aktivt tema: Cyber 💜"`. *(Repetition: `.textContent` från labb 2!)*

### Nivå 4: input och logik (avancerat)

**Uppgift 7: välj tema med input**

* Skriv funktionen `valjTema()` som läser texten från `.tema-input` med `.value`. *(Repetition från labb 3!)*
* Använd `if`/`else if`/`else`:
  * Om texten är `"dark"` → aktivera dark mode.
  * Om texten är `"cyber"` → aktivera cybertema.
  * Om texten är `"natur"` → aktivera naturtema.
  * Om texten är `"retro"` → aktivera retrotema.
  * Annars → visa `"Okänt tema!"` i `.tema-status` och ändra dess färg till röd.
* *(Tips: Glöm inte att rensa alla teman först!)*

**Uppgift 8: markera kortet**

* Skapa en knapp "Markera" i HTML. Funktionen ska:

1. Växla klassen `"markerad"` på kortet.
2. Ändra texten i `.kort-text` till `"Detta kort är markerat! ⭐"` om klassen lades till, eller tillbaka till originaltexten om den togs bort.

* *(Tips: `if (document.querySelector(".kort-text").textContent == "Detta kort är markerat! ⭐") { ... } else { ... }`)*

### Nivå 5: boss-nivån

**Uppgift 9: din egen designpanel**

* Bygg ut sidan med en hel kontrollpanel:

1. Ett input-fält där användaren skriver en ny rubrik → uppdatera `.huvudrubrik` med `.textContent`.
2. Ett input-fält för bakgrundsfärg → ändra `document.body.style.backgroundColor` direkt.
3. En knapp som aktiverar "disco-mode": byt bakgrundsfärg, lägg till klassen `"cyber"`, ändra rubriken till `"🪩 DISCO! 🪩"` och göm alla temaknappar med `style.display = "none"`.
