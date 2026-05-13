# Kapitel 1 – HTML-grunder och första CSS

Här är historiken över allt vi gjort i kursens första kapitel. Vi gick från noll förkunskaper till att bygga kompletta, visuellt stilade webbsidor.

---

## Lektioner i kronologisk ordning

| Datum | Mapp | Vad vi gjorde |
|-------|------|---------------|
| 2025-08-22 | intro | Den allra första HTML-sidan – bara `<h1>` och `<h2>` |
| 2025-08-27 | pippi | Biografi om Pippi Långstrump med bilder, text och listor |
| 2025-08-28 | beatles | Första kontakten med CSS – Beatles-låttext med färg och bakgrundsbild |
| 2025-09-03 | oppna-landskap | Avancerad CSS: Google Fonts, `box-shadow`, `text-shadow`, `border-radius` |
| 2025-09-04 | veckomeny | Tabeller i HTML (`<table>`, `<tr>`, `<th>`, `<td>`) för en veckomeny |

---

## Begrepp vi lärt oss

### HTML
`<!DOCTYPE html>`, `<html>`, `<head>`, `<meta charset="UTF-8">`, `<title>`, `<body>`, `<h1>`–`<h2>`, `<p>`, `<br>`, `<a href="">`, `<img src="" alt="">`, `<strong>`, `<em>`, `<ul>`, `<li>`, `<table>`, `<caption>`, `<tr>`, `<th>`, `<td>`

### CSS
`color`, `font-size`, `font-family`, `background-image`, `background-size: cover`, `background-color`, `padding`, `width`, `margin: auto`, `border-radius`, `box-shadow`, `text-shadow`, `border-spacing`, `@import url()`

---

## Exempel från lektionerna

### Första HTML-sidan (intro)
```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <title>Min första sida</title>
</head>
<body>
    <h1>Hej världen!</h1>
    <p>Det här är min allra första webbsida.</p>
</body>
</html>
```

### Första CSS (beatles)
```css
body {
    background-image: url(./bilder/aziz-acharki-tLsOA0Vlvwk-unsplash.jpg);
    background-size: cover;
}
h1 {
    color: rgb(31, 226, 164);
    font-size: 100px;
    font-family: 'Franklin Gothic Medium', sans-serif;
}
p {
    color: rgb(255, 139, 178);
    font-size: 30px;
}
```

### Google Fonts och skuggor (oppna-landskap)
```css
@import url('https://fonts.googleapis.com/css2?family=Lobster&display=swap');

h1 {
    font-family: "Lobster", sans-serif;
    text-shadow: 3px 3px 0 rgba(0,0,0,0.3);
}
.kontainer {
    width: 600px;
    margin: auto;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 5px 5px 15px rgba(0,0,0,0.5);
}
```

### Tabell (veckomeny)
```html
<table>
    <caption>Veckomeny v.36</caption>
    <tr>
        <th>Dag</th>
        <th>Rätt</th>
    </tr>
    <tr>
        <td>Måndag</td>
        <td>Pannkakor</td>
    </tr>
</table>
```

---

## Koppling till centralt innehåll

- **Märkspråk och deras syntax och semantik:** HTML:s grundstruktur, taggar och deras betydelse.
- **Teckenkodning:** `<meta charset="UTF-8">` för korrekt hantering av åäö.
- **Bilder och media:** `<img>` med `alt`-attribut för tillgänglighet.
- **Riktlinjer för god praxis:** Separat CSS-fil, korrekt `<!DOCTYPE>`, `lang`-attribut.
