# Labb 5 – quizet

Du har nu alla verktyg: du kan ändra färger, byta text, läsa input och växla CSS-klasser. Nu ska vi kombinera allt och bygga ett riktigt quiz! Här handlar det om logik — ditt program ska fatta beslut baserat på vad användaren svarar.

## Introduktion och mål

I den här labben bygger vi en interaktiv frågesport. Du kommer att träna på att:

* Använda `if`/`else if`/`else` för att jämföra svar.
* Läsa svar från input-fält med `.value` (repetition).
* Visa rätt/fel med `.textContent` och `.style` (repetition).
* Växla CSS-klasser för visuell feedback med `.classList` (repetition).
* Hålla koll på poäng med en variabel.

## Startkod för webbsidan

Skapa tre filer: `index.html`, `style.css` och `script.js`. Kopiera in koden nedan.

**index.html:**

```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quizet</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>🧠 Det stora quizet</h1>
        <p class="info-text">Svara på frågorna och se hur många poäng du får!</p>

        <div class="poang-ruta">
            <p>Poäng: <span class="poang">0</span></p>
        </div>

        <div class="fraga-kort fraga1">
            <h2>Fråga 1</h2>
            <p>Vad heter Sveriges huvudstad?</p>
            <input type="text" class="svar1" placeholder="Ditt svar">
            <button onclick="kollaFraga1()">Svara</button>
            <p class="resultat resultat1">...</p>
        </div>

        <div class="fraga-kort fraga2">
            <h2>Fråga 2</h2>
            <p>Hur många ben har en spindel?</p>
            <input type="text" class="svar2" placeholder="Ditt svar">
            <button onclick="kollaFraga2()">Svara</button>
            <p class="resultat resultat2">...</p>
        </div>

        <div class="fraga-kort fraga3">
            <h2>Fråga 3</h2>
            <p>Vilket år landade första människan på månen?</p>
            <input type="text" class="svar3" placeholder="Ditt svar">
            <button onclick="kollaFraga3()">Svara</button>
            <p class="resultat resultat3">...</p>
        </div>

        <div class="slutresultat">
            <h2>Resultat</h2>
            <p class="slut-text">...</p>
        </div>

        <button class="stor-knapp" onclick="visaResultat()">Visa mitt resultat!</button>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

**style.css:**

```css
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #667eea;
    color: #333;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    margin: 0;
}

.container {
    background: white;
    padding: 40px;
    border-radius: 15px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    text-align: center;
    max-width: 550px;
    width: 90%;
}

.poang-ruta {
    background-color: #667eea;
    color: white;
    padding: 10px 20px;
    border-radius: 50px;
    display: inline-block;
    font-size: 1.2rem;
    font-weight: bold;
    margin-bottom: 20px;
}

.fraga-kort {
    background-color: #f8f9fa;
    border: 2px solid #e0e0e0;
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 15px;
    transition: 0.3s;
}

.fraga-kort input {
    padding: 10px;
    border: 2px solid #ddd;
    border-radius: 8px;
    font-size: 1rem;
    text-align: center;
    width: 200px;
    margin-right: 10px;
}

.fraga-kort input:focus {
    border-color: #667eea;
    outline: none;
}

.fraga-kort button {
    padding: 10px 20px;
    border: none;
    border-radius: 8px;
    background-color: #667eea;
    color: white;
    cursor: pointer;
    font-weight: bold;
    transition: 0.2s;
}

.fraga-kort button:hover {
    background-color: #5a6fd6;
}

.resultat {
    font-weight: bold;
    margin-top: 10px;
    min-height: 20px;
}

.stor-knapp {
    padding: 15px 30px;
    border: none;
    border-radius: 10px;
    background-color: #28a745;
    color: white;
    cursor: pointer;
    font-weight: bold;
    font-size: 1.1rem;
    margin-top: 10px;
    transition: 0.2s;
}

.stor-knapp:hover {
    background-color: #218838;
    transform: scale(1.05);
}

.slutresultat {
    display: none;
    background-color: #e8f5e9;
    border: 2px solid #4caf50;
    border-radius: 10px;
    padding: 20px;
    margin: 20px 0;
}

/* Klasser för rätt/fel */
.ratt {
    border-color: #4caf50;
    background-color: #e8f5e9;
}

.fel {
    border-color: #f44336;
    background-color: #ffebee;
}
```

**script.js:**

```javascript
let poang = 0;
```

## Övningar och kodexempel

### Övning 1: kolla ett svar med if/else

Vi läser svaret från input, jämför det med rätt svar, och visar "Rätt!" eller "Fel!":

```javascript
function kollaFraga1() {
    let svar = document.querySelector(".svar1").value
    if (svar == "Stockholm") {
        document.querySelector(".resultat1").textContent = "Rätt! ✅"
        document.querySelector(".resultat1").style.color = "green"
    } else {
        document.querySelector(".resultat1").textContent = "Fel! ❌ Rätt svar är Stockholm."
        document.querySelector(".resultat1").style.color = "red"
    }
}
```

### Övning 2: uppdatera poäng

Vi har en variabel `poang` som börjar på 0 (se startkoden i `script.js`). Vi ökar den vid rätt svar och visar den på sidan:

```javascript
// Inuti if-blocket för rätt svar, lägg till:
poang = poang + 1
document.querySelector(".poang").textContent = poang
```

## Uppgifter – från nybörjare till quizmästare

Skriv alla funktioner i `script.js`. Variabeln `let poang = 0;` finns redan i startkoden.

### Nivå 1: uppvärmning (mycket enkelt)

**Uppgift 1: svara på fråga 1**

* Skriv funktionen `kollaFraga1()` enligt övning 1 ovan.
* Rätt svar är `"Stockholm"`. Visa `"Rätt!"` i grönt eller `"Fel!"` i rött.

**Uppgift 2: poäng vid rätt svar**

* Bygg vidare på uppgift 1.
* Om svaret är rätt, öka `poang` med 1 och uppdatera texten i `.poang`. *(Se övning 2.)*

### Nivå 2: fler frågor (enkelt)

**Uppgift 3: svara på fråga 2**

* Skriv funktionen `kollaFraga2()`. Rätt svar är `"8"`.
* Visa rätt/fel i `.resultat2` och uppdatera poängen.

**Uppgift 4: svara på fråga 3**

* Skriv funktionen `kollaFraga3()`. Rätt svar är `"1969"`.
* Samma mönster som ovan.

### Nivå 3: visuell feedback med classList (medel)

**Uppgift 5: markera rätt/fel med klass**

* Bygg vidare på alla tre frågefunktionerna.
* Förutom att ändra texten, lägg till CSS-klassen `"ratt"` eller `"fel"` på hela frågekortet. *(Repetition: `.classList.add()` från labb 4!)*

```javascript
document.querySelector(".fraga1").classList.add("ratt")
```

**Uppgift 6: lås frågan**

* När en fråga är besvarad, göm svarsknappen så att man inte kan svara flera gånger. *(Repetition: `style.display = "none"` från labb 1!)*

### Nivå 4: slutresultat (avancerat)

**Uppgift 7: visa slutresultat**

* Skriv funktionen `visaResultat()` som:

1. Visar den gömda `.slutresultat`-diven (`style.display = "block"`).
2. Använder `if`/`else if`/`else` för att visa ett meddelande i `.slut-text`:
   * 3 poäng: `"Perfekt! Du fick alla rätt! 🏆"`
   * 2 poäng: `"Bra jobbat! 2 av 3 rätt! 🎉"`
   * 1 poäng: `"Helt okej! 1 av 3 rätt. 👍"`
   * 0 poäng: `"Nollpoängare... men övning ger färdighet! 💪"`

**Uppgift 8: ändra hela sidans stil baserat på resultat**

* Bygg vidare på `visaResultat()`. Beroende på poäng, ändra `document.body.style.backgroundColor`:
  * 3 poäng: guld (`"#ffd700"`)
  * 2 poäng: ljusgrön (`"#90ee90"`)
  * 1 poäng: ljusorange (`"#ffdab9"`)
  * 0 poäng: ljusröd (`"#ffcccb"`)

### Nivå 5: boss-nivån

**Uppgift 9: egen fråga**

* Lägg till en fjärde fråga i HTML (kopiera strukturen från de andra frågorna).
* Hitta på en egen fråga, skriv funktionen, och se till att poängen räknas med.

**Uppgift 10: det ultimata quizet**

* Gör quizet extra snyggt:

1. Ändra rubriken `h1` till `"Quiz avslutat!"` när man klickar "Visa mitt resultat".
2. Om man får alla rätt, lägg till en effekt: ändra rubrikens färg till guld och gör texten större (`fontSize = "3rem"`).
3. Göm "Visa mitt resultat"-knappen efter den klickats (den ska bara gå att klicka en gång).
4. Visa en personlig hälsning: använd `prompt()` för att fråga användarens namn och skriv `"Grattis [namn], du fick X poäng!"` i `.slut-text`.
