# Projektöversikt: JavaScript-laborationer för Webbutveckling 1

Detta projekt innehåller en serie laborationsinstruktioner designade för att lära ut grundläggande JavaScript och DOM-manipulering inom ramen för kursen Webbutveckling 1. Materialet är strukturerat för att gradvis introducera elever till hur man skapar interaktivitet på webbsidor med hjälp av HTML, CSS och JavaScript.

## Instruktioner för AI-interaktion

*   **Språkregler:** Använd svenska skrivregler i all textproduktion. I rubriker ska endast det första ordet börja med versal (meningsversal), såvida det inte innehåller egennamn eller andra ord som enligt svensk grammatik kräver stor bokstav.
*   **Pedagogisk strategi:** 
    1.  **Extrem repetition:** Varje nytt koncept måste övas 3–5 gånger under samma lektion och repeteras konsekvent mellan lektioner. Tidigare moment (t.ex. variabler) ska alltid ingå i nya övningar.
    2.  **Visuell feedback:** Fokusera på praktiska, roliga och visuella exempel (ändra färger, bilder, texter) som ger omedelbar respons på skärmen.
    3.  **Hård begränsning:** Inga abstrakta eller avancerade koncept som arrayer, loopar eller avancerade funktioner. Modulen stannar vid: variabler, if-satser, `.textContent`, `.value`, `.classList` och grundläggande DOM-manipulering.

## Katalogöversikt

Katalogen fungerar som ett arkiv för instruktionsmaterial i Markdown-format. Varje fil representerar en specifik laboration med tydliga mål, startkod och uppgifter uppdelade i olika svårighetsnivåer (från nybörjare till "boss-nivå").

## Viktiga filer

*   **labb-1.md:** Introduktion till JavaScript-händelser (`onclick`), grundläggande styling via `document.body.style` och val av element med `document.querySelector()`. Fokus ligger på att ändra utseendet på en sida genom knapptryck.
*   **labb-2.md:** Fördjupning i textmanipulering med egenskapen `textContent`. Laborationen kombinerar färgändringar med innehållsuppdateringar och introducerar enkel logik med if-satser samt användarinteraktion via `prompt()`.

## Användning

Instruktionerna är tänkta att följas stegvis av en användare:
1.  Skapa en lokal arbetskatalog för laborationen.
2.  Skapa filerna `index.html`, `style.css` och `script.js` baserat på startkoden i respektive Markdown-fil.
3.  Implementera funktionerna i `script.js` för att lösa de angivna uppgifterna.
4.  Testa resultatet genom att öppna `index.html` i en webbläsare.

## Utvecklingskonventioner

*   **Språk:** Allt instruktionsmaterial är skrivet på svenska. Alla ord efter kolon med gemena, helt enligt svenska skrivregler. Alla rubriker följer principen om meningsversal.
*   **Pedagogik:** Uppgifterna är nivågrupperade för att möjliggöra differentierad undervisning och progression.
*   **Kodstil:** Fokus ligger på tydlig och läsbar JavaScript-kod som är anpassad för nybörjare, med användning av moderna metoder som `let` och `querySelector`.
