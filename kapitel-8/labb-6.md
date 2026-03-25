# Labb 6 – min profil (slutlabb)

Grattis — du har kommit till sista labben! Här bygger du en interaktiv profilsida och använder **alla** JavaScript-verktyg du lärt dig. Det är dags att visa vad du kan!

## Introduktion och mål

I den här labben bygger du "Min profil" — en sida där användaren fyller i information om sig själv och sidan uppdateras i realtid. Du repeterar och kombinerar:

* `.textContent` – ändra text (från labb 1–2).
* `.style` – ändra färger och storlekar (från labb 1–2).
* `.value` och `Number()` – läsa input (från labb 3).
* `.classList` – växla klasser (från labb 4).
* `if`/`else if`/`else` – logik och beslut (från labb 5).
* `prompt()` – hämta information från användaren (från labb 2).

## Startkod för webbsidan

Skapa tre filer: `index.html`, `style.css` och `script.js`. Kopiera in koden nedan.

**index.html:**

```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Min profil</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>Min profil</h1>

        <div class="profil-kort" class="profil-kort">
            <div class="avatar" class="avatar">?</div>
            <h2 class="visningsnamn">Ditt namn här</h2>
            <p class="bio">Skriv lite om dig själv...</p>
            <p class="alder-text">Ålder: <span class="visa-alder">?</span></p>
        </div>

        <div class="formulär">
            <h2>Fyll i dina uppgifter</h2>

            <div class="falt">
                <label>Namn:</label>
                <input type="text" class="namn-input" placeholder="Ditt namn">
                <button onclick="uppdateraNamn()">Uppdatera namn</button>
            </div>

            <div class="falt">
                <label>Bio:</label>
                <input type="text" class="bio-input" placeholder="Beskriv dig själv">
                <button onclick="uppdateraBio()">Uppdatera bio</button>
            </div>

            <div class="falt">
                <label>Ålder:</label>
                <input type="text" class="alder-input" placeholder="Din ålder">
                <button onclick="uppdateraAlder()">Uppdatera ålder</button>
            </div>

            <div class="falt">
                <label>Favorifärg:</label>
                <input type="text" class="farg-input" placeholder="T.ex. red, blue, #ff6600">
                <button onclick="bytFarg()">Byt färg</button>
            </div>

            <div class="falt tema-knappar">
                <label>Tema:</label>
                <button onclick="bytTema('ljust')">☀️ Ljust</button>
                <button onclick="bytTema('morkt')">🌙 Mörkt</button>
                <button onclick="bytTema('fest')">🎉 Fest</button>
            </div>
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
    transition: 0.5s;
}

.container {
    background: white;
    padding: 40px;
    border-radius: 15px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    max-width: 500px;
    width: 90%;
    transition: 0.5s;
}

.profil-kort {
    text-align: center;
    padding: 30px;
    border-radius: 15px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    margin-bottom: 30px;
    transition: 0.5s;
}

.avatar {
    width: 80px;
    height: 80px;
    background-color: rgba(255,255,255,0.3);
    border-radius: 50%;
    margin: 0 auto 15px auto;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 2rem;
    font-weight: bold;
}

.alder-text {
    font-size: 0.9rem;
    opacity: 0.9;
}

.formulär h2 {
    margin-bottom: 15px;
    font-size: 1.2rem;
}

.falt {
    margin-bottom: 15px;
}

.falt label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
    font-size: 0.9rem;
}

.falt input {
    padding: 10px;
    border: 2px solid #ddd;
    border-radius: 8px;
    font-size: 1rem;
    width: 200px;
    margin-right: 10px;
}

.falt input:focus {
    border-color: #667eea;
    outline: none;
}

.falt button, .tema-knappar button {
    padding: 10px 15px;
    border: none;
    border-radius: 8px;
    background-color: #667eea;
    color: white;
    cursor: pointer;
    font-weight: bold;
    transition: 0.2s;
}

.falt button:hover, .tema-knappar button:hover {
    background-color: #5a6fd6;
    transform: scale(1.05);
}

.tema-knappar button {
    margin-right: 5px;
    margin-top: 5px;
}

/* Tema-klasser */
.morkt-tema {
    background-color: #1a1a2e;
    color: #e0e0e0;
}

.morkt-tema .container {
    background-color: #16213e;
    color: #e0e0e0;
}

.morkt-tema .profil-kort {
    background: linear-gradient(135deg, #0f3460 0%, #533483 100%);
}

.fest-tema {
    background-color: #ff6b6b;
    color: white;
}

.fest-tema .container {
    background-color: #feca57;
    color: #333;
}

.fest-tema .profil-kort {
    background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
}

/* Speciell klass för vuxen/barn */
.vuxen {
    border: 3px solid gold;
}

.barn {
    border: 3px solid #00cec9;
}
```

**script.js:**

```javascript
// Din kod börjar här!
```

## Övningar och kodexempel

### Övning 1: uppdatera text från input

Hämta text från ett input-fält och visa den någon annanstans (repetition från labb 3):

```javascript
function uppdateraNamn() {
    let namn = document.querySelector(".namn-input").value;
    document.querySelector(".visningsnamn").textContent = namn;
}
```

### Övning 2: byt tema med classList

Ta bort gamla teman och lägg till rätt klass på body (repetition från labb 4):

```javascript
function bytTema(tema) {
    // Ta bort alla teman först
    document.body.classList.remove("morkt-tema");
    document.body.classList.remove("fest-tema");

    // Lägg till rätt tema
    if (tema == "morkt") {
        document.body.classList.add("morkt-tema");
    } else if (tema == "fest") {
        document.body.classList.add("fest-tema");
    }
    // "ljust" = inga klasser = default
}
```

## Uppgifter – bygg din profil steg för steg

Skriv all kod i `script.js`.

### Nivå 1: textuppdatering (mycket enkelt)

**Uppgift 1: uppdatera namn**
Skriv funktionen `uppdateraNamn()` enligt övning 1. När man skriver sitt namn i fältet och klickar knappen ska texten i profilkortet ändras.

**Uppgift 2: uppdatera bio**
Skriv funktionen `uppdateraBio()` som läser från `.bio-input` och visar texten i `.bio`.

### Nivå 2: färg och stil (enkelt)

**Uppgift 3: byt favoritfärg**
Skriv funktionen `bytFarg()` som läser en färg från `.farg-input` och ändrar profilkortets `backgroundColor`:

```javascript
document.querySelector(".profil-kort").style.background = farg;
```

**Uppgift 4: första bokstaven i avataren**
Bygg vidare på `uppdateraNamn()`. Förutom att uppdatera namnet, visa den första bokstaven av namnet i avataren:

```javascript
let initial = namn[0];
document.querySelector(".avatar").textContent = initial;
```

(Om namnet är tomt, visa `"?"` istället – det kräver en `if`/`else`!)

### Nivå 3: ålder och logik (medel)

**Uppgift 5: visa ålder**
Skriv funktionen `uppdateraAlder()` som:

1. Läser `#alder-input` med `.value`.
2. Omvandlar till ett tal med `Number()`.
3. Visar åldern i `#visa-alder` med `.textContent`.

**Uppgift 6: vuxen eller barn?**
Bygg vidare på `uppdateraAlder()`. Använd `if`/`else` för att lägga till rätt CSS-klass på profilkortet:

- 18 år eller äldre: lägg till klassen `"vuxen"`, ta bort `"barn"`.
- Under 18: lägg till klassen `"barn"`, ta bort `"vuxen"`.

Visa även en text i `#bio` som säger `"Vuxen 🎓"` eller `"Ungdom 🌟"`.

### Nivå 4: byt tema (avancerat)

**Uppgift 7: tema-växlare**
Skriv funktionen `bytTema(tema)` enligt övning 2. Den ska hantera tre teman: `"ljust"`, `"morkt"` och `"fest"`.

**Uppgift 8: gömda funktioner**
Gör profilsidan mer dynamisk:

1. Om man skriver `"admin"` som namn, ändra bakgrundsfärgen på avataren till guld (`"gold"`).
2. Om åldern är exakt `100`, ändra biotexten till `"Legendarisk ✨"` och gör hela profilkortet guldigt.

### Nivå 5: boss-nivån

**Uppgift 9: prompt-hälsning**
Lägg till en knapp `"Hemligt meddelande"` i HTML. Skriv en funktion som:

1. Använder `prompt()` för att fråga efter ett hemligt lösenord.
2. Om lösenordet är rätt (t.ex. `"abc123"`), ändra rubrikens text till `"Välkommen tillbaka!"` och sätt fest-temat.
3. Om det är fel, visa `alert("Fel lösenord!")`.

**Uppgift 10: den kompletta profilen**
Gör profilen till din – välj själv och bygg klart:

1. Lägg till fler fält i HTML (t.ex. stad, hobby, favorit-emoji).
2. Varje fält ska ha en knapp som uppdaterar profilen.
3. Lägg till minst en `if`/`else if`/`else`-kedja (t.ex. olika hälsningar beroende på stad).
4. Använd `.classList.toggle()` minst en gång (t.ex. en knapp som togglar en speciell stil).
5. Byt minst en `.style`-egenskap baserat på input.
