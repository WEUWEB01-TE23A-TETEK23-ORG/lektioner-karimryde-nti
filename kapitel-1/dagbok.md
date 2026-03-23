# Dagbok: Kapitel 1 – HTML och CSS-grunder

## Lektion 1: intro (2025-08-22)

**Ämne:** Namn och adress (HTML-boilerplate)

**Nya begrepp:**
- `<h1>`, `<h2>` – Olika nivåer av rubriker
- HTML-boilerplate – Den grundläggande strukturen på en webbsida

**Vad vi gjorde:**
I den här lektionen gick vi igenom grundstrukturen för ett HTML-dokument. Vi skapade en enkel sida som presenterade vårt namn och adress med hjälp av olika rubriknivåer.

**Nyckelexempel:**
```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <title>Min första sida</title>
</head>
<body>
    <h1>Karim</h1>
    <h2>Gata 1</h2>
</body>
</html>
```

---

## Lektion 2: pippi (2025-08-27)

**Ämne:** Pippi Långstrump-biografi

**Nya begrepp:**
- `<img>` – Lägger till bilder på sidan
- `<p>` – Skapar ett stycke text
- `<ul>`, `<li>` – Skapar en onumrerad punktlista
- `<strong>`, `<em>` – Gör text fet respektive kursiv

**Vad vi gjorde:**
Vi byggde en enkel biografisida om Pippi Långstrump med ren HTML. Vi tränade på att formatera text i stycken, markera viktiga ord och använda listor för att presentera egenskaperna hos karaktären. Bildarbetet introducerades. Ingen CSS användes.

**Nyckelexempel:**
```html
<h1>Pippi Långstrump</h1>
<img src="bilder/pippi.jpg" alt="Pippi">
<p>Pippi är <strong>starkast</strong> i världen.</p>
<ul>
    <li>Herr Nilsson</li>
    <li>Lilla Gubben</li>
</ul>
```

---

## Lektion 3: beatles (2025-08-28)

**Ämne:** Beatles-låttext och första CSS:en

**Nya begrepp:**
- `<br>` – Tvingar fram en radbrytning
- `<a>` – Skapar klickbara länkar
- Extern CSS, `background-image`, `color`, `font-size`, `font-family` – Stilregler i `style.css`

**Vad vi gjorde:**
Vi kopplade ett externt CSS-dokument till vår HTML för att ge stil åt en Beatles-låttext. Vi satte en bakgrundsbild på `body`, ändrade textens färg och storlek samt använde radbrytningar för att texten skulle bevara sitt utseende.

**Nyckelexempel:**
```html
<p>
    Yesterday,<br>
    all my troubles seemed so far away<br>
</p>
```
```css
body {
    background-image: url('bilder/beatles.jpg');
    color: white;
    font-family: Arial, sans-serif;
}
```

---

## Lektion 4: oppna-landskap (2025-09-03)

**Ämne:** Öppna landskap med mer avancerad CSS

**Nya begrepp:**
- Google Fonts (`@import`) – För att använda externa typsnitt
- `padding`, `width`, `border-radius` – Box-modellens inre rymd, bredd och rundade hörn
- `box-shadow`, `text-shadow` – Skuggor på boxar och text
- `rgba()` – Färger med transparens (alpha-kanal)

**Vad vi gjorde:**
Vi lade in texten till "Öppna landskap" och fortsatte att arbeta med stilarna. Lektionen fokuserade på att importera typsnitt från Google Fonts, använda transparens och skuggor för att skapa snygga, läsbara layoutboxar över en bakgrundsbild.

**Nyckelexempel:**
```css
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

p {
    font-family: 'Roboto', sans-serif;
    padding: 20px;
    background-color: rgba(255, 255, 255, 0.8);
    border-radius: 10px;
    box-shadow: 2px 2px 5px black;
}
```

---

## Lektion 5: veckomeny (2025-09-04)

**Ämne:** En veckomeny presenterad med tabeller

**Nya begrepp:**
- `<table>`, `<caption>`, `<tr>`, `<th>`, `<td>` – Tabellstrukturens taggar
- `border-spacing` – Avstånd mellan tabellceller
- `margin: auto` – Centrerar boxar (som till exempel en tabell)
- `width: 100%` på bilder – Får bilder att fylla sitt utrymme

**Vad vi gjorde:**
Vi använde HTML-tabeller för att visa upp en veckomeny för skolan. Fokus låg på att formatera raderna med varannan-färgning pseudo-klassning, och att centrera hela tabellen på sidan med `margin: auto`.

**Nyckelexempel:**
```html
<table>
    <caption>Skolans Veckomeny</caption>
    <tr>
        <th>Måndag</th>
        <td>Köttbullar</td>
    </tr>
</table>
```
```css
table {
    margin: auto;
    border-spacing: 0;
}
```
