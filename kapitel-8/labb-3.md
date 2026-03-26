# Labb 3 – rotera bilder och spela upp media

Snyggt jobbat med de tidigare labbarna! Nu har du lärt dig att ändra färger och byta ut text på en webbsida. I den här labben ska vi göra sidan ännu roligare och mer levande. Vi ska bygga en hyllning till den klassiska humorsketschen "Ministry of silly walks" med John Cleese. 

## Introduktion och mål

I den här labben kommer vi att kombinera JavaScript med bilder, ljud och video. Du kommer att träna på att:

* Ändra en bilds rotation och utseende med CSS-egenskapen `transform`.
* Spela upp ljudfiler genom att styra ett HTML `<audio>`-element med JavaScript.
* Bädda in och visa en YouTube-video (en så kallad "iframe").
* Använda variabler för att låta en bild rotera mer och mer för varje klick.

## Startkod för webbsidan

Skapa tre nya filer: `index.html`, `style.css` och `script.js`. Kopiera in koden nedan. (I HTML-koden använder vi redan en färdig bildlänk på John Cleese och ett enkelt test-ljud).

**index.html:**

```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ministry of silly walks</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>Ministry of silly walks</h1>
        <p>Hjälp John Cleese att få till den perfekta, galna gångstilen!</p>
        
        <img src="https://upload.wikimedia.org/wikipedia/en/0/0d/Monty_Python%27s_The_Ministry_of_Silly_Walks_video_game_cover.jpeg" alt="John Cleese gör en silly walk">
        
        <audio src="https://s3.amazonaws.com/freecodecamp/simonSound1.mp3"></audio>

        <div class="knapp-panel">
            <button onclick="roteraBild()">Rotera bilden</button>
            <button onclick="spelaLjud()">Spela ljud</button>
            <button onclick="visaVideo()">Visa originalklippet</button>
        </div>

        <div class="video-lada">
            <h2>Se originalet! 🎩</h2>
            <iframe width="100%" height="250" src="[https://www.youtube.com/embed/5ptUMe9eqYE](https://www.youtube.com/embed/5ptUMe9eqYE)" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

**style.css:**

```css
body {
    font-family: 'Courier New', Courier, monospace;
    background-color: #2c3e50;
    color: #ecf0f1;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    margin: 0;
}

.container {
    background: #34495e;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 8px 15px rgba(0,0,0,0.3);
    text-align: center;
    max-width: 500px;
}

img {
    width: 250px;
    border: 5px solid #ecf0f1;
    border-radius: 10px;
    margin: 20px 0;
    /* Transition gör att rotationen sker mjukt! */
    transition: transform 0.5s ease; 
}

.knapp-panel {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    justify-content: center;
    margin-bottom: 20px;
}

button {
    padding: 10px 15px;
    border: none;
    border-radius: 5px;
    background-color: #e74c3c;
    color: white;
    cursor: pointer;
    font-weight: bold;
    font-size: 1rem;
}

button:hover {
    background-color: #c0392b;
}

.video-lada {
    display: none;
    background-color: #2c3e50;
    padding: 15px;
    border-radius: 8px;
    margin-top: 20px;
}
```

## Övningar och kodexempel

Läs igenom dessa exempel för att förstå hur vi styr media med JavaScript. Skriv gärna in dem i din `script.js` och testa.

### Övning 1: rotera en bild med transform

För att snurra en bild använder vi egenskapen `transform` i JavaScript, precis som i CSS. 

```javascript
// Funktionen kopplad till knappen "Rotera bilden"
function roteraBild() {
    // Roterar bilden 90 grader
    document.querySelector("img").style.transform = "rotate(90deg)"
}
```

### Övning 2: spela upp ett ljud

HTML-taggen `<audio>` syns inte på skärmen, men vi kan be JavaScript att starta den genom att använda metoden `.play()`.

```javascript
// Funktionen kopplad till knappen "Spela ljud"
function spelaLjud() {
    // Hämtar ljudelementet och spelar upp det
    document.querySelector("audio").play()
}
```

## Uppgifter – från nybörjare till media-mästare

Dags att skriva din egen kod! Lägg all JavaScript i `script.js`. Lägg till fler knappar i `index.html` om uppgifterna ber om det.

### Nivå 1: grundläggande rotation (enkelt)

**Uppgift 1: upp och ner**

* Den färdiga funktionen `roteraBild()` roterar bara till 90 grader. Ändra den så att John Cleese hamnar helt upp och ner (180 grader).

**Uppgift 2: visa YouTube-klippet**

* Skriv funktionen `visaVideo()` som är kopplad till knappen "Visa originalklippet".
* Funktionen ska ändra `display` på `.video-lada` till `"block"` så att iframe-videon med Monty Python-klippet dyker upp på skärmen!

### Nivå 2: galnare bildhantering (medel)

**Uppgift 3: spegelvänd bilden**

* Skapa en ny knapp i HTML som heter "Spegelvänd". Koppla den till en ny funktion, till exempel `spegelvand()`.
* I funktionen ska du använda `transform` för att vända på bilden horisontellt. 
* *(Tips: Använd `style.transform = "scaleX(-1)"` för att spegelvända en bild).*

**Uppgift 4: byta ut bilden**

* Skapa en knapp som heter "Vanlig promenad".
* Skriv en funktion som ändrar källan (`src`) på bilden så det ser ut som en vanlig gubbe. 
* *(Tips: `document.querySelector("img").src = "länk-till-en-annan-bild.jpg"`)*

### Nivå 3: bygga logik med variabler (avancerat)

**Uppgift 5: snurra mer för varje klick**

Problemet med `rotate(90deg)` är att bilden fastnar där. Om du klickar igen händer ingenting. Vi vill att den ska snurra lite till för varje klick!

* Längst upp i din `script.js` (utanför alla funktioner), skapa en variabel: `let vinkel = 0`
* Skapa en knapp "Snurra vidare!" och en tillhörande funktion.
* I funktionen: Öka variabeln med 45 för varje klick (`vinkel = vinkel + 45`).
* Använd sedan variabeln i koden: `document.querySelector("img").style.transform = "rotate(" + vinkel + "deg)"`

### Nivå 4: boss-nivån

**Uppgift 6: the ultimate silly walk**

* Skapa en gigantisk knapp som heter "SILLY MODE".
* När knappen klickas ska följande hända samtidigt:
    1. Ljudet (`audio`) ska spelas upp.
    2. Bilden ska snurra snabbt (till exempel `rotate(720deg)` för två hela varv).
    3. YouTube-videon ska visas.
    4. Texten i `p` ska bytas ut till `"MINISTRY OF SILLY WALKS ÄR NU AKTIVERAT!"`.
    5. Sidans bakgrundsfärg (`document.body.style.backgroundColor`) ska bli knallgul (`"yellow"`).
    6. Huvudrubriken ska ändra färg till svart.
