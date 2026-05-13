# Kapitel 8 – JavaScript-introduktion

Historik över kapitel 8 där vi introducerade JavaScript – språket som gör webbsidor interaktiva och levande.

---

## Lektioner i kronologisk ordning

| Datum | Mapp | Vad vi gjorde |
|-------|------|---------------|
| 2026-03-12 | intro | Första JavaScript: `let`, `prompt()`, `alert()` och enkel `if`-sats |
| 2026-03-18 | grunder / kaboom | Egendefinierade funktioner kopplade till `onclick` och `onmouseover` |
| 2026-03-19 | stilar / stilar-tagg | Ändra CSS och design direkt via `document.querySelector()` |
| 2026-03-31 | labbar | Labb 1–3: DOM-manipulering, `.textContent`, `.value`, `Number()` |
| 2026-04-15+ | labbar-facit | Fördjupning: `.classList`, `if`/`else if`/`else`, avancerade övningar |

---

## Begrepp vi lärt oss

### JavaScript (hård begränsning – inga loopar, arrayer eller objekt)
`let`, `prompt()`, `alert()`, `console.log()`, `function`, `onclick` (HTML-attribut), `onmouseover`, `document.body.style`, `document.querySelector()`, `.style`, `.textContent`, `.value`, `Number()`, `.classList.add()`, `.classList.remove()`, `.classList.toggle()`, `if`, `else if`, `else`, `==` (jämförelse)

---

## Exempel från lektionerna

### Första JavaScript-programmet (intro)
```javascript
let namn = prompt("Ange ett namn");
alert("Hej på dig " + namn);
```

### Funktioner med onclick (grunder / kaboom)
```html
<button onclick="kaboom()">Klicka inte mig!</button>
<p onmouseover="hemlig()">>>> Varning för hemlig text! <<<</p>
```
```javascript
function kaboom() {
    alert("AJ aj!!!");
}
function hemlig() {
    alert("Sverige, Sverige, hur är det fatt...");
}
```

### Ändra CSS med JavaScript (stilar)
```javascript
function bytFarg() {
    document.querySelector("h1").style.color = "red";
    document.body.style.backgroundColor = "black";
}
```

### Läsa input och uppdatera text (labbar)
```html
<input id="namn-input" type="text" placeholder="Ditt namn">
<button onclick="halsa()">Hälsa!</button>
<p id="resultat"></p>
```
```javascript
function halsa() {
    let namn = document.querySelector("#namn-input").value;
    document.querySelector("#resultat").textContent = "Hej " + namn + "!";
}
```

### Enkel logik med if/else
```javascript
function kollaAlder() {
    let alder = Number(document.querySelector("#alder").value);
    if (alder >= 18) {
        document.querySelector("#svar").textContent = "Du är myndig!";
    } else {
        document.querySelector("#svar").textContent = "Du är inte myndig än.";
    }
}
```

### Växla CSS-klass med classList
```javascript
function togglaMorktLage() {
    document.body.classList.toggle("morkt");
}
```
```css
.morkt {
    background-color: #222;
    color: #eee;
}
```

---

## Pedagogisk strategi

- **Extrem repetition:** Varje nytt koncept övas 3–5 gånger och repeteras i kommande lektioner.
- **Visuell feedback:** Varje rad kod ger en direkt, synlig effekt på webbsidan.
- **Hård begränsning:** Inga loopar, arrayer, objekt eller `addEventListener`. Vi stannar vid `let`, `if`/`else`, `querySelector`, `.textContent`, `.value`, `.classList`, `Number()`, `prompt()`, `alert()` och namngivna funktioner via `onclick`.

---

## Koppling till centralt innehåll

- **Ecmascript och DOM:** JavaScript är Ecmascript-implementationen, DOM är bryggan mellan JS och HTML.
- **Samspelet mellan klient och server:** JavaScript körs på klientsidan (i webbläsaren) och ger omedelbar interaktivitet.
- **Säkerhet:** `prompt()` och `alert()` är säkra metoder som inte kan manipuleras av tredje part.
- **Kvalitetssäkring:** Vi testar varje funktion direkt i webbläsaren – omedelbar återkoppling.
- **Processen för webbutvecklingsprojekt:** HTML (struktur) → CSS (utseende) → JavaScript (interaktivitet).
