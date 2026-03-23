# Dagbok: Kapitel 8 – JavaScript Grunder

## Lektion 1: intro (2026-03-12)

**Ämne:** Introduktion till JavaScript

**Nya begrepp:**
- `let` – Skapar en variabel för att spara information (som en låda) i minnet
- `prompt()` – Öppnar en popup-ruta där besökaren kan skriva in text
- `alert()` – En enkel popup-ruta som skickar en notis till skärmen
- `console.log()` – Skapar loggar man kan se om man gör felsökning i webbläsaren ("Inspektera")
- `if`/`else if`/`else` och `==` – Villkorslogik för att datorn ska kunna ta beslut

**Vad vi gjorde:**
Det här var vårt absoluta första möte med JavaScript-programmering! Vi lärde oss skillnaden mellan HTML (skelettet), CSS (kläderna) och slutligen JavaScript (musklerna/hjärnan). Vi byggde ett enkelt matematik-quiz med `prompt()` som frågade om vad "10 - 2" var, och programmet utvärderade sedan med en `if/else`-sats huruvida svaret var `8` eller om de gissade fel.

**Nyckelexempel:**
```javascript
let namn = prompt("Vad heter du?");
let gissning = prompt(namn + "! Pippi har en apa som heter?");

if (gissning == "herr nilsson") {
    alert("Helt rätt!");
} else {
    alert("Nja, det var fel.");
}
```

---

## Lektion 2: grunder & kaboom (2026-03-18)

**Ämne:** Strängkonkatenering och händelsestyrda funktioner

**Nya begrepp:**
- Strängkonkatenering (`+`) – Sätta ihop text med lagrade variabler.
- `function` – Ett fristående block med kod som bara körs när man ber den att göra det ("kalla" på den).
- `onclick` och `onmouseover` – HTML-attribut som talar om för HTML-koden exakt *vilken* funktion ur JS-filen som tillhör vilket klick.

**Vad vi gjorde:**
Vi flyttade oss från klick-säker JavaScript som bara körde igång automatiskt när sidan laddades in (vilket är ganska irriterande för besökaren) till interaktiva program. Genom att bygga enkla metoder med namngivna `function` kunde vi ge valfria HTML-knappar ett `onclick=""` in i sin tagg.

**Nyckelexempel:**
```html
<button onclick="visaMeddelande()">Klicka här!</button>
```
```javascript
function visaMeddelande() {
    let alder = prompt("Hur gammal är du?");
    alert("Du är " + alder + " år!");
}
```

---

## Lektion 3: stilar (2026-03-19)

**Ämne:** Manipulera webbsidans `body`-layout direkt ur minnet

**Nya begrepp:**
- DOM-manipulation – Att "styra över HTML-noden med CSS" från ett JavaScript program.
- `document.body.style` – En specifik inbyggd JS-genväg till sidans element
- CSS-egenskaper i JS: I JavaScript tas bindestrecket `-` (t.ex CSS: `background-color`) bort, och man använder "camelCase", dvs börjar andra ordet med stor bokstav: `.backgroundColor`.

**Vad vi gjorde:**
Istället för att bara skjuta popups, visade vi hur snabbt ett knapptryck fysiskt kan koda in nya färger, bilder eller textjusteringar live på sidan. Vi skapade knappar där användaren med `onclick` bytte om `.body.style` från ljus läge, till ett blått mörkt läge.

**Nyckelexempel:**
```javascript
function andraBakgrund() {
    document.body.style.backgroundColor = "black";
    document.body.style.color = "white";
}
```

---

## Lektion 4: stilar-tagg (2026-03-19)

**Ämne:** Målsöka specifika element på sidan 

**Nya begrepp:**
- `document.querySelector('TAGGNAMN')` – Jägar-verktyget man skickar ut på sidan för att hämta ner en enstaka H1, P, eller en speciell ID-klass.
- Ändra egenskaper på de valda noderna

**Vad vi gjorde:**
Ett steg till framåt. Istället för att bara drabba hela `body` (och därmed hela sidans inredning), riktade vi in oss exakt och specifikare. Till exempel fångade vi in en `<h1>`-rubrik in i skriptet och sminkade om bara den enskilda noden med stylingen, för att därefter använda en annan funktion som helt stängde av den med `display: none` och tog fram den med `display: block` igen.

**Nyckelexempel:**
```javascript
function doljRubrik() {
    // Fångar in första <h1> på hela sidan
    let minRubrik = document.querySelector('h1');
    
    // Använder CSS 'display' för att få den att försvinna
    minRubrik.style.display = 'none';
}
```
