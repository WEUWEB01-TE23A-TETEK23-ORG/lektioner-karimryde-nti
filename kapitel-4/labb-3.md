# Labb 3 – min portfolio

Den här labben är en stor sammanfattning av allt från kapitel 1–4. Du bygger en komplett portfolio-webbplats med flera sidor helt på egen hand.

## Introduktion och mål

I den här labben repeterar och kombinerar du **alla koncept** från kapitel 1–4:

* HTML-struktur: rubriker, stycken, listor, bilder, tabeller, länkar.
* Bilder: `<figure>`, `<figcaption>`, bildhantering.
* Layout: `<div>`, klasser, `.kontainer`, CSS-reset, CSS-variabler.
* Navigation: flersidig webbplats, `.aktiv`, `:hover`, `display: inline-block`.
* Styling: Google Fonts, `box-shadow`, `text-shadow`, `border-radius`, `text-transform`.

## Instruktioner

Det finns **ingen startkod** i den här labben! Du bygger allt från grunden. Använd det du lärt dig.

Skapa följande filer:
- `sida1.html` (Om mig)
- `sida2.html` (Mina projekt)
- `sida3.html` (Kontakt)
- `style.css`
- Mappen `bilder/`

## Uppgifter

### Nivå 1: grundstrukturen (mycket enkelt)

**Uppgift 1: HTML-boilerplate**
Skapa `sida1.html` med korrekt HTML-grundstruktur (`<!DOCTYPE html>`, `<html>`, `<head>`, `<body>`). Länka till `style.css`.

**Uppgift 2: CSS-reset och variabler**
Skriv CSS-reseten i `style.css`:

```css
html { box-sizing: border-box; }
*, *:before, *:after { box-sizing: inherit; }
body, h1, h2, h3, p, ul { margin: 0; padding: 0; }
```

Skapa en `:root`-sektion med minst tre CSS-variabler (bakgrund, text, accent).

### Nivå 2: navigeringen (enkelt)

**Uppgift 3: menyn**
Skapa en `<div class="meny">` med tre `<a>`-taggar som pekar på `sida1.html`, `sida2.html` och `sida3.html`. Styla med `display: inline-block`, `text-decoration: none` och `padding`.

**Uppgift 4: aktiv sida**
Ge rätt länk klassen `aktiv` på varje sida. Styla `.aktiv` med en annan bakgrundsfärg. Lägg till `:hover` som ändrar färg.

### Nivå 3: innehåll (medel)

**Uppgift 5: om mig-sidan**
Fyll `sida1.html` med:
- En `<h1>` med ditt namn.
- Ett `<p>` med en kort presentation.
- En `<figure>` med bild och `<figcaption>`.
- En `<ul>`-lista med dina intressen.

**Uppgift 6: projekt-sidan**
Fyll `sida2.html` med minst tre "projekt" (riktiga eller påhittade). Varje projekt ska ha en `<h2>`, ett stycke och en bild.

### Nivå 4: kontakt och styling (avancerat)

**Uppgift 7: kontaktsidan**
Fyll `sida3.html` med kontaktinformation:
- E-post (som en `<a href="mailto:...">`-länk).
- En tabell med "sociala medier" (namn + länk).
- Styla tabellen med `<th>`-rubriker och bakgrundsfärg.

**Uppgift 8: visuell polish**
Gör sidan snygg:
- Importera ett Google Font.
- Ge `.kontainer` en `background-color`, `border-radius` och `box-shadow`.
- Ge `h1` en `text-shadow`.
- Ge alla bilder `border-radius`.

### Nivå 5: boss-nivån

**Uppgift 9: två extra sidor**
Lägg till ytterligare två sidor (t.ex. "Hobbyer" och "Galleri"). Uppdatera menyn på alla sidor.

**Uppgift 10: portfolion du är stolt över**
Gör denna webbplats till något du vill visa upp:

1. Minst fem sidor med unik innehåll.
2. Alla sidor har korrekt meny med `.aktiv`.
3. Minst tre `<figure>`-bilder med `<figcaption>`.
4. Minst en tabell.
5. Minst en stilad knapp-länk.
6. Konsekvent CSS-tema med `:root`-variabler.
7. Google Font.
8. Hover-effekter på meny och länkar.
