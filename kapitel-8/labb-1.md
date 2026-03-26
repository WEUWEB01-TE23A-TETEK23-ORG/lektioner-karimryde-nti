# Labb 1 – magi med javascript och design

Välkommen till din första JavaScript-labb! Hittills har du byggt webbsidor med HTML (strukturen) och CSS (designen). Idag ska vi lägga till JavaScript (hjärnan) för att få sidan att reagera när du gör saker, till exempel klickar på knappar.

## Introduktion och mål

I den här labben ska vi lära oss hur vi kan ändra sidans utseende i realtid. Du kommer att träna på att:

* Lyssna efter klick och andra händelser med HTML-attributet `onclick`.
* Skapa funktioner i JavaScript som körs när man klickar.
* Ändra hela sidans bakgrund med `document.body.style`.
* Hitta specifika element och ändra deras design med `document.querySelector()`.
* Trolla fram och gömma element med `display: none` och `display: block`.

## Startkod för webbsidan

Börja med att skapa tre filer: `index.html`, `style.css` och `script.js`. Kopiera in koden nedan. Sidan är ett enkelt kontrollrum som du ska få att fungera.

**index.html:**

```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Design-kontrollrummet</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>Design-kontrollrummet</h1>
        <p class="info-text">Här styr vi webbsidans utseende med kod.</p>
        
        <div class="knapp-panel">
            <button onclick="andraBakgrund()">Ändra bakgrund</button>
            <button onclick="andraRubrik()">Ändra rubrik</button>
            <button onclick="gomText()">Göm texten</button>
            <button onclick="visaText()">Visa texten</button>
            </div>

        <div class="hemlig-lada">
            <h2>Du hittade den hemliga lådan! 🎁</h2>
            <p>Denna var osynlig från början.</p>
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

**style.css:**

```css
body {
    font-family: sans-serif;
    background-color: #f4f4f9;
    color: #333;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
}

.container {
    background: white;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    text-align: center;
}

.knapp-panel {
    margin: 20px 0;
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    justify-content: center;
}

button {
    padding: 10px 15px;
    border: none;
    border-radius: 5px;
    background-color: #007bff;
    color: white;
    cursor: pointer;
    font-weight: bold;
}

button:hover {
    background-color: #0056b3;
}

.hemlig-lada {
    display: none;
    margin-top: 20px;
    padding: 15px;
    background-color: #ffde59;
    border-radius: 8px;
}
```

## Övningar och kodexempel

Innan du ger dig på uppgifterna, läs igenom dessa tre exempel. Du kan skriva in dem i din `script.js` för att se hur de fungerar! När du klickar på en knapp i HTML letar webbläsaren efter en funktion med samma namn i din JavaScript-fil.

### Övning 1: ändra hela sidans bakgrund

För att ändra något på hela sidan pratar vi direkt med `document.body`. I HTML-koden har vi redan skrivit `onclick="andraBakgrund()"` på den första knappen.

```javascript
// Funktionen som körs när man klickar på knappen "Ändra bakgrund"
function andraBakgrund() {
    // Ändra bakgrundsfärgen (märk att det är camelCase, backgroundColor)
    document.body.style.backgroundColor = "lightgreen"
}
```

### Övning 2: ändra stil på ett specifikt element

Vill du ändra en rubrik eller en paragraf? Då letar du först upp den med `querySelector()`.

```javascript
// Funktionen kopplad till knappen "Ändra rubrik"
function andraRubrik() {
    document.querySelector("h1").style.color = "red"
    document.querySelector("h1").style.fontSize = "40px"
}
```

### Övning 3: gömma och visa element

I CSS kan man använda `display: none` för att ett element inte ska ta någon plats alls. I JavaScript kan vi ändra detta för att skapa coola effekter.

```javascript
// Funktionen kopplad till knappen "Göm texten"
function gomText() {
    document.querySelector(".info-text").style.display = "none" // Gömmer texten helt
}
```

## Uppgifter – från nybörjare till webbmagiker

Skriv alla dina funktioner i `script.js`. Om du behöver nya knappar för en uppgift, lägg till dem i `index.html` inuti din `.knapp-panel` och ge dem ett `onclick`-attribut.

### Nivå 1: interaktivitet (enkelt)

**Uppgift 1: framkalla den hemliga lådan**

* Det finns en div i din HTML som heter `.hemlig-lada`. Den har `display: none` från början. 
* Skapa en knapp och en funktion som ändrar lådans display till `"block"` så att den poppar fram!

### Nivå 2: mer styling (medel)

**Uppgift 2: större och fetare**

* Skapa en knapp som ändrar designen på den hemliga lådan. 
* När man klickar ska lådans text bli större (`fontSize = "24px"`) och dess bakgrundsfärg ändras till `"hotpink"`.

**Uppgift 3: händelsen onmouseenter**

* Man måste inte klicka för att saker ska hända! Skapa en knapp i HTML som heter "Rör mig inte". 
* Istället för `onclick`, använd attributet `onmouseenter="musOver()"`.
* När muspekaren dras över knappen ska funktionen köras och sidans bakgrundsfärg bli röd.

**Uppgift 4: händelsen onmouseleave**

* Bygg vidare på Uppgift 3. Lägg till ytterligare ett attribut på samma knapp: `onmouseleave="musUt()"`. 
* Skapa funktionen som gör att när musen lämnar knappen så ska bakgrundsfärgen bli vit igen.

### Nivå 3: bygga logik (avancerat)

**Uppgift 5: målarfärgen från användaren**

* Skapa en knapp som heter "Välj färg" med tillhörande funktion. När man klickar på den ska du använda `prompt("Vilken bakgrundsfärg vill du ha?")`.
* Spara svaret i en variabel och använd variabeln för att sätta värdet på `document.body.style.backgroundColor`.
* Testa att skriva in "orange" eller "purple" i rutan!

**Uppgift 6: av/på-knappen (toggle)**

* Kan du använda *samma* knapp för att både gömma och visa den hemliga lådan? 
* Skapa en knapp som heter "Växla låda".
* Tips: Använd en if-sats inuti din funktion!  
  `if (document.querySelector(".hemlig-lada").style.display === "none") { ... } else { ... }`

### Nivå 4: boss-nivån (hacker)

**Uppgift 7: party mode!**
Skapa en stor knapp som heter "PARTY MODE". När användaren klickar på den ska en funktion köras där flera saker händer exakt samtidigt:

1. Sidans bakgrund ska bli svart.
2. Huvudrubriken ska bli neongrön.
3. Den hemliga lådan ska visas (om den var gömd).
4. Knappen i sig (Party-knappen) ska försvinna från sidan (`display = "none"`), för festen går inte att stänga av!

