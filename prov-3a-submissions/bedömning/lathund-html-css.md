# Lathund – HTML & CSS

## HTML
  
### Grundläggande HTML

All HTML skrivs inuti `<body>`-taggen. Här är en enkel HTML-struktur:
```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Min Webbplats</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>Välkommen!</h1>
  <p>Detta är en snabblathund.</p>
</body>
</html>
```

- Vanliga taggar:
  - `<h1>`, `<h2>`, `<h3>`... – rubriker
  - `<p>` – stycke/text
  - `<br>` – radbrytning (t.ex. i låttexter)
  - `<img src="..." alt="beskrivning">` – bild
  - `<a href="...">...</a>` – länk
  - `<ul>`, `<li>` – punktlistor
  - `<ol>`, `<li>` – numrerad lista

### Tabell

Skapa tabeller för att visa data:

```html
<table>
  <tr>
    <th>Namn</th>
    <th>Ålder</th>
  </tr>
  <tr>
    <td>Alice</td>
    <td>30</td>
  </tr>
...
</table>
```

### Formulär

Skapa formulär för inmatning av data:

```html
<form action="/submit" method="post">
  <fieldset>
    <legend>Kontaktformulär</legend>
    <label for="name">Namn:</label>
    <input type="text" id="name" name="name"><br>
    ...
    <button type="submit">Skicka</button>
  </fieldset>
</form>
```

### Menyer

Skapa navigationsmenyer med länkar:

```html
<a href="index.html">Hem</a>
<a href="om.html">Om oss</a>
...
```

## CSS

### Grundläggande CSS

```html
<div class="top">
  <h1>Hej världen!</h1>
</div>
```

```css
h1 {
  font-size: 24px;
  color: navy;
}
.top {
  margin: 20px;
  padding: 10px;
}
```

- Vanliga CSS-egenskaper:
  - `background-color: #121212;` – bakgrundsfärg
  - `color: #ffffff;` – textfärg
  - `font-size: 16px;` – textstorlek
  - `font-family: 'Open Sans', sans-serif;` – typsnitt
  - `text-align: center;` – textjustering
  - `width` och `height` – bredd och höjd
  - `margin: 20px;` – yttre avstånd
  - `padding: 10px;` – inre avstånd
  - `border: 1px solid #000;` – kantlinje
  - `border-radius: 5px;` – rundade hörn
  - `box-shadow: 2px 2px 5px rgba(0,0,0,0.3);` – skugga runt element
  - `text-decoration: underline;` – understrykning av länkar
  - `:hover` – stil vid muspekare över element

### CSS Flexbox

* Placera element horisontellt till vänster, höger eller centrerat:

```css
.meny {
  display: flex;
  justify-content: space-between; /* jämnt fördelade */
  gap: 10px;
}
```

### CSS Grid

* Bygg rutnät med flera kolumner:

```css
.rutnät {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr; /* tex 4 kolumner */
  gap: 20px;
}
```

## Semantisk HTML

* Använd **semantiska taggar** för tydlig struktur:
  - `<header>` – sidhuvud
  - `<nav>` – navigering/meny
  - `<main>` – huvudinnehåll
  - `<footer>` – sidfot
  - `<figure>` och `<figcaption>` - bild + bildtext.

## Responsiv design

* Gör sidan anpassningsbar för mobil, platta och dator med **media queries**:

```css
/* Mobil först */
.rutnät {
  grid-template-columns: 1fr;
}
@media (min-width: 768px) {
  .rutnät {
    grid-template-columns: 1fr 1fr;
  }
}
@media (min-width: 1024px) {
  .rutnät {
    grid-template-columns: 1fr 1fr 1fr;
  }
}
```