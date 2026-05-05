# Projekt – Min sida om något jag gillar

**Sammanfattning:** Bygg en komplett webbsida om ett ämne du tycker om med hjälp av HTML och CSS.

---

## Vad ska du göra?

Du ska skapa en webbsida om något du gillar – ett band, en sport, ett spel, en maträtt, en stad, ett djur – vad som helst! Du får en färdig kodstruktur (scaffold) att utgå från. Din uppgift är att:

- Byta ut alla platshållare mot ditt eget innehåll
- Välja egna färger och typsnitt
- Lägga till egna bilder och texter

---

## Scaffold – `index.html`

```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><!-- Byt ut detta mot din sidtitel --></title>
    <!-- Byt ut Google Fonts-länken mot ett typsnitt du gillar: https://fonts.google.com -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <h1><!-- Byt ut detta mot din egen rubrik --></h1>
    <p><!-- Skriv ett kort stycke om ditt ämne här --></p>

    <!-- Byt ut img-källan mot din egen bild. Spara bilden i mappen bilder/ -->
    <img src="bilder/din-bild.jpg" alt="<!-- Beskriv bilden -->" class="bild">

    <h2><!-- Rubrik för din lista, t.ex. "Mina favoriter" --></h2>
    <ul>
        <li><!-- Punkt 1 --></li>
        <li><!-- Punkt 2 --></li>
        <li><!-- Punkt 3 --></li>
    </ul>

    <h2><!-- Rubrik för din tabell, t.ex. "Fakta" --></h2>
    <table>
        <tr>
            <th><!-- Kolumnrubrik 1 --></th>
            <th><!-- Kolumnrubrik 2 --></th>
        </tr>
        <tr>
            <td><!-- Rad 1, cell 1 --></td>
            <td><!-- Rad 1, cell 2 --></td>
        </tr>
        <tr>
            <td><!-- Rad 2, cell 1 --></td>
            <td><!-- Rad 2, cell 2 --></td>
        </tr>
        <tr>
            <td><!-- Rad 3, cell 1 --></td>
            <td><!-- Rad 3, cell 2 --></td>
        </tr>
    </table>

    <script src="script.js"></script>
</body>
</html>
```

---

## Scaffold – `style.css`

```css
/* Byt ut Google Fonts-importen om du valde ett annat typsnitt */
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

body {
    background-color: /* din bakgrundsfärg, t.ex. #f0e6ff */ ;
    font-family: /* din font, t.ex. 'Roboto', sans-serif */ ;
    padding: 20px;
}

h1 {
    color: /* din rubrikfärg, t.ex. #6a0dad */ ;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}

h2 {
    color: /* din h2-färg */ ;
}

p {
    color: /* din textfärg */ ;
}

.bild {
    border-radius: 12px;
    box-shadow: 4px 4px 8px rgba(0, 0, 0, 0.3);
    width: 300px;
}

ul {
    padding-left: 20px;
}

li {
    margin-bottom: 6px;
}

table {
    border-spacing: 8px;
    margin: auto;
}

th {
    background-color: /* din th-bakgrundsfärg */ ;
    color: /* din th-textfärg */ ;
    padding: 8px 16px;
}

td {
    padding: 6px 16px;
}
```

---

## Krav

Bocka av allt innan du lämnar in:

- [ ] Minst en `<h1>` och två `<h2>`
- [ ] Minst ett `<img>` med `alt`-attribut och klassen `bild`
- [ ] En `<ul>` med minst tre punkter
- [ ] En tabell med minst tre rader och rubriker (`<th>`)
- [ ] Bakgrundsfärg på sidan
- [ ] Google Font (importerat och använt i CSS)
- [ ] Allt eget innehåll — inga platshållar-kommentarer kvar i det du visar

---

## Bonusutmaningar

⭐ **Lätt** – Lägg till en länk (`<a>`) till en extern sida om ditt ämne (t.ex. Wikipedia).

⭐⭐ **Medel** – Styla tabellen med `background-color` på `<td>`-cellerna och lägg till `border-radius` på tabellen.

⭐⭐⭐ **Svår** – Lägg till en bakgrundsbild på `body` med `background-image: url(...)` och `background-size: cover`. Gör texten läsbar genom att lägga innehållet i en `<div class="innehall">` med `background-color: rgba(255, 255, 255, 0.8)` och `padding: 30px`.
