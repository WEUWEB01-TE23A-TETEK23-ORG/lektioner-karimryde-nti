# Modulplan: HTML-grunder och första CSS

Kapitlet introducerar HTML från grunden — hur en webbsida är uppbyggd, vilka taggar som finns och hur man börjar styla med CSS. Eleverna bygger enkla sidor med text, bilder, länkar och tabeller.

## Mål

- Förstå HTML-dokumentets grundstruktur (`<!DOCTYPE html>`, `<html>`, `<head>`, `<body>`).
- Skapa rubriker, stycken och radbrytningar.
- Länka till andra sidor med `<a>`.
- Visa bilder med `<img>`.
- Bygga listor med `<ul>` och `<li>`.
- Skapa enkla tabeller med `<table>`, `<tr>`, `<th>` och `<td>`.
- Styla text med CSS: färg, typsnitt, storlek och bakgrund.
- Importera och använda Google Fonts.
- Använda dekorativa CSS-egenskaper: `box-shadow`, `text-shadow`, `border-radius`.

## Förkunskaper

Inga. Detta är kursens första kapitel.

## Nya begrepp

### HTML
`<!DOCTYPE html>`, `<html>`, `<head>`, `<meta>`, `<title>`, `<body>`, `<h1>`, `<h2>`, `<p>`, `<br>`, `<a>`, `<ul>`, `<li>`, `<img>`, `<strong>`, `<em>`, `<table>`, `<caption>`, `<tr>`, `<th>`, `<td>`

### CSS
`color`, `font-size`, `font-family`, `background-image`, `background-size`, `background-color`, `padding`, `width`, `margin: auto`, `border-radius`, `box-shadow`, `text-shadow`, `border-spacing`, `@import url()`

## Pedagogiska grundregler

- Varje lektion producerar en komplett, visuellt tilltalande sida — aldrig "kal" HTML.
- Engagerande innehåll: Beatles-texter, Pippi Långstrump, svenska sånger, matrecept.
- Nya taggar introduceras gradvis (2–3 per lektion) och repeteras i efterföljande lektioner.
- CSS introduceras redan i andra lektionen för att ge omedelbar visuell feedback.

## Lektioner

### Lektion 1: första HTML-sidan (mappen: intro)
- **Innehåll:** HTML-boilerplate, `<h1>`, `<h2>`.
- **Mål:** förstå att en webbsida är en textfil med taggar och kunna skapa en minimal sida.

### Lektion 2: text, länkar och första CSS (mappen: beatles)
- **Innehåll:** `<p>`, `<br>`, `<a>`, extern CSS-fil, `background-image`, `color`, `font-size`, `font-family`.
- **Mål:** kunna styla text och bakgrund, länka till andra sidor.
- **Repetition:** `<h1>` från lektion 1.

### Lektion 3: listor, bilder och semantik (mappen: pippi)
- **Innehåll:** `<ul>`, `<li>`, `<img>`, `<strong>`, `<em>`, `<h2>`.
- **Mål:** strukturera innehåll med listor och bilder.
- **Repetition:** `<h1>`, `<p>` från lektion 1–2.

### Lektion 4: avancerad CSS-styling (mappen: oppna-landskap)
- **Innehåll:** Google Fonts (`@import`), `padding`, `width`, `border-radius`, `box-shadow`, `text-shadow`, hex-färger, rgba-hex.
- **Mål:** skapa en visuellt polerad sida med dekorativa CSS-effekter.
- **Repetition:** `<h1>`, `<p>`, `background-image` från lektion 2–3.

### Lektion 5: tabeller (mappen: veckomeny)
- **Innehåll:** `<table>`, `<caption>`, `<tr>`, `<th>`, `<td>`, `border-spacing`, `margin: auto`, `width: 100%` på bilder.
- **Mål:** presentera data i tabellform och centrera innehåll med `margin: auto`.
- **Repetition:** CSS-styling, `<img>` från lektion 2–4.

## Vanliga misstag

- Glömmer avslutande taggar (`</p>`, `</h1>`).
- Blandar ihop `<br>` (radbrytning) och `<p>` (nytt stycke).
- Felaktig sökväg till bilder (`bilder/bild.jpg` vs `./bilder/bild.jpg`).
- Skriver CSS i HTML-filen istället för i `style.css`.
- Glömmer `<link rel="stylesheet" href="style.css">` i `<head>`.

## Resurser

- [Google Fonts](https://fonts.google.com/) — typsnitt som importeras i CSS.
