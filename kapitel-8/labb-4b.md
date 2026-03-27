# Labb 4 – den vilsna miniräknaren

Glöm allt du lärt dig om logik och användarvänlighet. I den här labben ska vi bygga en miniräknare som har drabbats av en rejäl identitetskris. Den är girig, lider av social fobi och får panikångest när siffrorna blir för höga.

Här lär du dig hur du går från att skriva "snäll" kod till att skapa ett digitalt kaos som faktiskt lyder dina lagar.

## Introduktion och mål

Målet med den här labben är att bemästra hur vi kan styra webbsidans beteende i realtid. Du kommer att träna på att:

* **Händelsestyrning:** Reagera på musrörelser med `onmouseover`.
* **Visuella triggers:** Koppla samman JavaScript med CSS-animationer.
* **Destruktiv kodning:** Radera och skriva om sidans innehåll dynamiskt.
* **Villkorlig logik:** Använda `if` och `else` för att skapa personlighet i koden.

## Förberedelser (html & css)

Innan vi börjar med logiken måste vi förbereda vår arbetsyta. Vi använder **enbart klasser** för att hitta våra element.

### Steg 1: index.html
Börja med att se till att din HTML-fil har rätt knappar och klasser. Notera särskilt klasserna `blyg-knapp` och `exit-knapp`.

```html
<div class="container">
    <h1 class="rubrik">🤪 Den vilsna miniräknaren</h1>
    <p class="info-text">Varning: Räknaren är extremt instabil.</p>

    <div class="input-grupp">
        <input type="text" class="tal1" placeholder="Tal 1">
        <input type="text" class="tal2" placeholder="Tal 2">
    </div>

    <div class="knapp-panel">
        <button onclick="addera()">+ Addera</button>
        <button class="blyg-knapp" onmouseover="flyttaKnapp()">− Subtrahera</button>
        <button onclick="multiplicera()">× Multiplicera</button>
        <button onclick="sjalvforstorelse()" class="exit-knapp" style="background: #900;">💥 Självförstörelse</button>
    </div>

    <div class="resultat-ruta">
        <p class="resultat">Vågar du räkna?</p>
    </div>
</div>
```

### Steg 2: style.css
Lägg till dessa regler i din CSS-fil för att hantera "nervositet" och knapparnas rörelser.

```css
/* Animation för när räknaren får panik */
@keyframes skaka {
    0% { transform: translate(1px, 1px) rotate(0deg); }
    50% { transform: translate(-3px, -2px) rotate(1deg); }
    100% { transform: translate(1px, 1px) rotate(0deg); }
}

.skakis {
    animation: skaka 0.1s infinite;
    border: 5px solid #ff4d4d !important;
}

.blyg-knapp {
    position: relative;
    transition: 0.1s ease-out;
}
```

## Övningar och kodexempel

### Övning 1: den giriga räknaren
*Varför ska räknaren jobba gratis? I den här världen kostar varje plus-tecken pengar. Vi lär oss hur vi kan modifiera matematiska resultat innan de visas för användaren.*

1.  **Hämta:** Vi läser in värdena från input-fälten.
2.  **Omvandla:** Vi använder `Number()` för att kunna räkna.
3.  **Modifiera:** Vi lägger till en "serviceavgift" på 15 kr.

```javascript
function addera() {
    let siffra1 = Number(document.querySelector(".tal1").value);
    let siffra2 = Number(document.querySelector(".tal2").value);
    
    let summa = siffra1 + siffra2 + 15; 
    
    document.querySelector(".resultat").textContent = "Resultat: " + summa + " kr (inkl. avgift)";
}
```

### Övning 2: den blyga knappen
*Vissa knappar gillar helt enkelt inte uppmärksamhet. Genom att använda `onmouseover` i din HTML kan vi få knappen att fly undan så fort muspekaren närmar sig.*

1.  **Hitta:** Vi väljer knappen med klassen `.blyg-knapp`.
2.  **Flytta:** Vi ändrar marginalen för att knuffa bort den.

```javascript
function flyttaKnapp() {
    let knapp = document.querySelector(".blyg-knapp");
    // Varje gång musen nuddar knappen, hoppar den 100 pixlar åt höger
    knapp.style.marginLeft = "100px";
}
```

### Övning 3: rädd för stora tal
*När matematiken blir för svår får räknaren ett sammanbrott. Här lär vi oss att använda `if`-satser för att aktivera CSS-animationer.*

1.  **Kontrollera:** Vi kollar om produkten är större än 1000.
2.  **Aktivera:** Vi lägger till klassen `.skakis` på vår container.

```javascript
function multiplicera() {
    let siffra1 = Number(document.querySelector(".tal1").value);
    let siffra2 = Number(document.querySelector(".tal2").value);
    let produkt = siffra1 * siffra2;
    
    let container = document.querySelector(".container");
    
    if (produkt > 1000) {
        container.classList.add("skakis"); 
        document.querySelector(".resultat").textContent = "NEJ! FÖR STORT!";
    }
}
```

### Övning 4: dramatisk exit
*Ibland vill man bara radera allt och gå hem. Vi lär oss hur vi kan radera hela sidans innehåll och ersätta det med något annat med bara en rad kod.*

1.  **Töm:** Vi sätter `document.body.innerHTML` till en ny text.
2.  **Styla:** Vi gör bakgrunden svart för extra dramatik.

```javascript
function sjalvforstorelse() {
    document.body.innerHTML = "<h1 style='color:red; text-align:center;'>SYSTEMFEL: Hejdå!</h1>"; 
    document.body.style.backgroundColor = "black";
}
```

## Uppgifter – från vilsen till kaotisk

Här är det din tur att koda. Skriv dina lösningar i `script.js`.

### Nivå 1: skattmasen
**Uppgift 1: addera med dolda avgifter**
Gör klart funktionen `addera()`. Den ska fungera som i övning 1, men den här gången ska räknaren lägga till exakt 13 kronor på varje resultat.
* **Tips:** Använd `Number()` och visa resultatet i klassen `.resultat`.

### Nivå 2: flyktbeteende
**Uppgift 2: knappen som hoppar ner**
Bygg ut `flyttaKnapp()`. Istället för att bara flytta knappen åt höger (som i övning 2), ska den nu flytta sig 150 pixlar nedåt (`marginTop`).
* **Tips:** Använd `knapp.style.marginTop = "150px";`.

### Nivå 3: lugna ner räknaren
**Uppgift 3: rädd för multiplikation**
Gör klart `multiplicera()`. Om resultatet blir över 500 ska räknaren börja skaka, men om man räknar ut något litet (under 500) ska den lugna ner sig och sluta skaka.
* **Tips:** Använd `.classList.add("skakis")` om talet är stort, och `.classList.remove("skakis")` i en `else`-sats om det är litet.

### Nivå 4: sista varningen
**Uppgift 4: dramatisk exit med bekräftelse**
Gör klart `sjalvforstorelse()`. Innan sidan raderas ska användaren få en fråga: "Är du verkligen säker på att du vill radera internet?".
* **Tips:** Använd en `if`-sats med `confirm("Din text här")`.

### Nivå 5: boss-nivån
**Uppgift 5: den sarkastiska räknaren**
Bygg ut valfri funktion så att om resultatet blir exakt **2**, ändras texten i klassen `.rubrik` till: "Verkligen? Behövde du hjälp med den?".
* **Tips:** Kontrollera om ditt resultat `=== 2`. Använd `.textContent` för att ändra texten i rubriken.

---

**Snyggt jobbat! Vill du att jag visar hur du kan lägga till en funktion som gör att hela sidan börjar rotera långsamt om man råkar dividera med noll?**
