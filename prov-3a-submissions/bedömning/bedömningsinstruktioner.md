# Bedömningsinstruktioner för Prov 3a

Filer som ska bedömas:
- html-filer
- css-filer

Gå igenom varje av de fyra huvudkategorierna och deras kriterier. Notera vad som är uppfyllt och vad som saknas eller kan förbättras med 1p eller 0.5p där det är lämpligt. 

---

## Bedömningsmatris: Prov 3a (Totalt 20 poäng)

### 1. Grundläggande HTML & innehåll (5 poäng)
*Fokus: Finns allt material med och är det korrekt uppmärkt enligt genomgångarna?*

* **1p – Grundstruktur:** Dokumentet har korrekt `<!DOCTYPE html>`, `<html>`, `<head>` och `<body>` utan allvarliga syntaxfel.
* **1p – Innehåll:** Rubriker, brödtext och bilder stämmer överens med instruktionerna/materialet.
* **1p – Bildkomponent:** Bild och bildtext är uppmärkta med `<figure>` och `<figcaption>` (krav då detta gåtts igenom på lektion).
* **1p – Sidfot:** En länk till Wikipedia finns i sidfoten (att länken leder till `#` eller en skarp adress godkänns lika).
* **1p – Fem undersidor:** Alla 5 sidor är skapade och korrekt länkade till varandra i menyn.

### 2. Layout & utseende (5 poäng)
*Fokus: Ser sidan ut som på målbilden?*

* **1p – Kontainer:** Huvudinnehållet är inbäddat i en kontainer som är **700px** bred och **centrerad** i webbläsarfönstret.
* **1p – Meny:** Menyn ligger horisontellt (radvis) ovanför bilden.
* **1p – Luft & rymd:** Det finns tydlig padding (luft) runt innehållet inuti kontainern, så text/bild inte ligger klistrat mot kanten.
* **1p – Designelement:** Bakgrundsfärger, rundade hörn och skuggor (`box-shadow`) stämmer väl överens med skärmdumpen i uppgiften.
* **1p – Stabilitet:** Layouten håller ihop; element (t.ex. bilder eller menyval) hoppar inte runt eller krockar med varandra.

### 3. Styling & detaljer (5 poäng)
*Fokus: Har eleven följt de specifika designinstruktionerna?*

* **1p – Typsnitt rubrik/meny:** Typsnittet **Montserrat** importeras och används korrekt på rubriker och i menyn.
* **1p – Typsnitt brödtext:** Övrig text (p-taggar etc.) visas i **sans-serif**.
* **1p – Färger:** Menyns knappar har rätt bakgrundsfärg (mörkgrå) och textfärg (vit).
* **1p – Aktiv sida:** Den länk i menyn som motsvarar sidan man besöker är tydligt markerad (t.ex. ljusare färg eller annan stil).
* **1p – Bildanpassning:** Bilderna är stilade så de inte är bredare än sin behållare.

### 4. Kodkvalitet & struktur (5 poäng)
*Fokus: Är koden logisk, ren och enkel att arbeta med?*

* **1p – Indentering & kommentarer:** Både HTML och CSS har snygg indragning (indentering) som gör koden lättläst. Kommentarer finns där det behövs för att förklara delar av koden.
* **1p – Korrekta avstånd:** Eleven använder inte '<br>' eller flera mellanslag för att skapa avstånd i layouten. Istället används CSS-egenskaper som `margin` och `padding`.
* **1p – DRY (Don't Repeat Yourself):** Eleven undviker onödig upprepning. Exempelvis sätts typsnitt på `body` istället för på varje enskild paragraf.
* **1p – Logiska lösningar:** Eleven använder robusta metoder för layout.
    * *Bra:* `text-align: center`, `margin: 0 auto`, `display: flex`.
    * *Dåligt:* "Magic numbers" (t.ex. `padding-left: 320px` för att tvinga in en text i mitten – detta ger poängavdrag här).
* **1p – Val av selektorer:** Eleven använder specifika CSS-selektorer (t.ex. `.kontainer .meny a` istället för bara `a`) för att styla sidan på ett säkert och tydligt sätt, enligt instruktion.

## Mall för feedback till elev

Skriv ut summa poäng och ge kort feedback baserat på ovanstående kriterier. Fokusera på vad som är bra och vad som kan förbättras till nästa gång. Var specifik med exempel från elevens kod när det är möjligt.

**Total poäng: X/20**

**Sammanfattning:**

- Styrkor: (exempelvis "Bra användning av `<figure>` och `<figcaption>` för bilder.")
- Förbättringsområden: (exempelvis "Undvik att använda `<
br>` för layout; använd istället `margin` och `padding` i CSS.")

---