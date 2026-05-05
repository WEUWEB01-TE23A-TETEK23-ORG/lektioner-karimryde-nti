# Dagbok - Projekt: Interaktiva sidor och kaos-labb

Vi avslutar med JavaScript-projekt där vi gör sidorna levande. Vi har även introducerat "Den vilsna miniräknaren" för att träna på händelsehantering på ett roligt sätt.

### Nya begrepp och verktyg
- **DOM-manipulering:** Att ändra text (`textContent`) eller stilar (`style`) via JavaScript.
- **Input-hantering:** Att läsa in vad användaren skriver med `.value`.
- **Event-lyssnare:** Att trigga kod via `onclick` eller `onmouseover` direkt i HTML.

### Kodexempel: Läsa input och ändra text
```javascript
function halsa() {
    let namn = document.querySelector("#namn-input").value;
    document.querySelector("#resultat").textContent = "Hej " + namn + "!";
}
```