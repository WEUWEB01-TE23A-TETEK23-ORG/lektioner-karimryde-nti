# Labb 2 – ändra text och design

Bra jobbat med Labb 1! Nu när du kan klicka på knappar och ändra färger är det dags att ta kontroll över själva innehållet på sidan. I den här labben ska vi bygga en interaktiv "Anslagstavla" där vi kombinerar färgändringar med att byta ut texten på skärmen.

## Introduktion och mål

I den här labben övar vi vidare på det du lärde dig i Labb 1, men vi lägger till en ny, superviktig egenskap: `textContent`. Du kommer att träna på att:

* Använda `onclick` för att anropa funktioner.
* Ändra textinnehållet i HTML-element med hjälp av `textContent`.
* Kombinera textändringar med `style` för att skapa coola effekter.
* Ändra texten på själva knappen man just klickade på!

## Startkod för webbsidan

Skapa tre nya filer: `index.html`, `style.css` och `script.js`. Kopiera in koden nedan.

**index.html:**

```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Anslagstavlan</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>Dagens meddelande</h1>
        
        <div class="meddelande-ruta">
            <p class="info-text">Klicka på knapparna nedan för att ändra denna text!</p>
        </div>
        
        <div class="knapp-panel">
            <button onclick="gorGlad()">Gör mig glad</button>
            <button onclick="gorArg()">Gör mig arg</button>
            <button class="btn-hemlig" onclick="visaHemlighet()">Visa hemlighet</button>
            </div>

        <div class="hemlig-lada">
            <p>Detta är en hemlig text som ingen får se.</p>
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
    background-color: #e0e5ec;
    color: #333;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
}

.container {
    background: white;
    padding: 40px;
    border-radius: 15px;
    box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    text-align: center;
    max-width: 500px;
}

.meddelande-ruta {
    background-color: #f8f9fa;
    border-left: 5px solid #007bff;
    padding: 20px;
    margin: 20px 0;
    font-size: 1.2rem;
    min-height: 80px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.knapp-panel {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    justify-content: center;
    margin-bottom: 20px;
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
    background-color: #5a6268;
    transform: scale(1.05);
}

.hemlig-lada {
    display: none;
    background-color: #ffcccb;
    padding: 15px;
    border-radius: 8px;
    border: 2px dashed red;
}
```

## Övningar och kodexempel

Läs igenom dessa två exempel innan du börjar med uppgifterna. Skriv gärna in dem i din `script.js` för att se hur det fungerar!

### Övning 1: ändra text med textContent

För att byta ut texten inuti ett HTML-element (till exempel en `<p>` eller en `<h1>`) använder vi `.textContent`. Det fungerar precis som när vi ändrar `style`, men här ändrar vi själva orden.

```javascript
function gorGlad() {
    document.querySelector(".info-text").textContent = "Idag är en helt fantastisk dag! ☀️"
}
```

### Övning 2: kombinera text och färg

Ofta vill vi att en händelse ska göra flera saker samtidigt. Kanske både byta ut texten *och* byta färg på den.

```javascript
function gorArg() {
    document.querySelector(".info-text").textContent = "NÄ NU BLIR JAG RIKTIGT ARG! 😡"
    document.querySelector(".info-text").style.color = "red"
    document.querySelector(".info-text").style.fontWeight = "bold"
}
```

## Uppgifter – från nybörjare till text-mästare

Nu är det din tur. Skriv funktionerna i `script.js`. Om du behöver lägga till fler knappar för en uppgift, gör det i `index.html` inuti `<div class="knapp-panel">`.

### Nivå 1: grundläggande textändringar

**Uppgift 1: förändra rubriken**

* Skapa en ny knapp i HTML med texten "Byt rubrik" och attributet `onclick="bytRubrik()"`.
* Skapa funktionen `bytRubrik()` och ändra texten i `h1` till `"Viktigt meddelande!"`.

**Uppgift 2: trolla fram hemligheten**

* Det finns en knapp med `onclick="visaHemlighet()"` och en låda med class `hemlig-lada` (som är dold med `display: none`).
* Skriv funktionen som gör att lådans display ändras till `"block"` så texten syns.

### Nivå 2: interaktivitet och stil

**Uppgift 3: ändra knappens egen text**

* Bygg vidare på funktionen `visaHemlighet()` från uppgift 2.
* Hämta knappen med `querySelector(".btn-hemlig")` och ändra dess `textContent` från `"Visa hemlighet"` till `"Hemlighet visad!"`.

**Uppgift 4: varningstext**

* Skapa en knapp i HTML och koppla den till en ny funktion. När funktionen körs ska:

1. Texten i `.info-text` ändras till `"VARNING! Något gick fel!"`.
2. Hela sidans bakgrundsfärg (`document.body.style.backgroundColor`) ska bli orange (`"orange"`).

### Nivå 3: användarens egna ord

**Uppgift 5: din egen hälsning**

* Skapa en knapp "Skriv en hälsning" och en tillhörande funktion.
* Använd `prompt("Skriv en hälsning här:")` och spara svaret i `let svar = prompt(...)`.
* Använd variabeln för att sätta `.textContent` på `.info-text` till det användaren skrev.
### Nivå 4: bygga logik (avancerat)

**Uppgift 6: dubbelkollen (if-sats)**

* Skapa en knapp "Är det farligt?" kopplad till en funktion.
* I funktionen, kolla vad som står i `.info-text` med en `if`-sats.
* *(Tips: `if (document.querySelector(".info-text").textContent === "VARNING! Något gick fel!") { ... }`)*

### Nivå 5: boss-nivån

**Uppgift 7: hacker-attacken**

* Skapa en röd knapp "HACKA SIDAN". När knappen klickas ska:

1. Sidans bakgrund ändras till svart.
2. Textfärgen (`color`) på hela `body` bli neongrön (`"#39ff14"`).
3. Rubriken `h1` bytas ut till `"SYSTEMET ÄR ÖVERTAGET"`.
4. Texten i `.info-text` bytas ut till `"Alla dina filer är nu krypterade..."`.
5. Om den hemliga lådan är framme, ändra texten inuti den till `"Inga hemligheter är säkra längre!"`.

