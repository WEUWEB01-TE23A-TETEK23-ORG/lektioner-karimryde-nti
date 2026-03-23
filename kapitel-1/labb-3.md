# Labb 3 – tabellen och den snygga sidan

Du kan nu rubriker, stycken, listor, bilder och länkar. I den här labben lägger vi till **tabeller** och piffar upp allt med avancerad CSS som Google Fonts, skuggor och rundade hörn.

## Introduktion och mål

I den här labben tränar du på att:

* Skapa tabeller med `<table>`, `<tr>`, `<th>` och `<td>`.
* Lägga till en tabellrubrik med `<caption>`.
* Importera och använda Google Fonts.
* Använda CSS-effekter: `box-shadow`, `text-shadow`, `border-radius`.
* Centrera innehåll med `margin: auto` och `width`.
* Kombinera alla koncept från kapitel 1 (repetition).

## Startkod

Skapa två filer: `index.html` och `style.css`.

**index.html:**

```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Veckans schema</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="sida">
        <h1>Veckans schema</h1>
        <p>Här är mitt schema för veckan.</p>

        <table>
            <caption>Måndag – fredag</caption>
            <tr>
                <th>Tid</th>
                <th>Måndag</th>
                <th>Tisdag</th>
                <th>Onsdag</th>
            </tr>
            <tr>
                <td>08:00</td>
                <td>Matte</td>
                <td>Svenska</td>
                <td>Engelska</td>
            </tr>
            <tr>
                <td>10:00</td>
                <td>Idrott</td>
                <td>Teknik</td>
                <td>Webb</td>
            </tr>
        </table>
    </div>
</body>
</html>
```

**style.css:**

```css
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');

body {
    font-family: 'Poppins', sans-serif;
    background-color: #e8eaf6;
    color: #333;
    padding: 20px;
}

.sida {
    width: 600px;
    margin: auto;
    background-color: white;
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

table {
    width: 100%;
    border-spacing: 0;
    margin-top: 20px;
}

th, td {
    padding: 12px;
    text-align: left;
}

th {
    background-color: #3f51b5;
    color: white;
}

tr:nth-child(even) {
    background-color: #f5f5f5;
}
```

## Övningar och kodexempel

### Övning 1: en tabell

En tabell byggs med `<table>`, `<tr>` (rad), `<th>` (rubrikcell) och `<td>` (datacell):

```html
<table>
    <tr>
        <th>Namn</th>
        <th>Poäng</th>
    </tr>
    <tr>
        <td>Anna</td>
        <td>85</td>
    </tr>
</table>
```

### Övning 2: Google Fonts

Importera ett typsnitt överst i CSS-filen och använd det:

```css
@import url('https://fonts.googleapis.com/css2?family=Poppins&display=swap');

body {
    font-family: 'Poppins', sans-serif;
}
```

### Övning 3: skuggor och rundade hörn

Ge element djup med `box-shadow` och mjukare form med `border-radius`:

```css
.sida {
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    border-radius: 15px;
}
```

Ge rubriker en textskugga:

```css
h1 {
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
}
```

## Uppgifter

### Nivå 1: uppvärmning (mycket enkelt)

**Uppgift 1: fyll i schemat**
Ändra ämnena i tabellen till dina riktiga ämnen (eller hitta på roliga ämnen).

**Uppgift 2: lägg till rader**
Lägg till minst en `<tr>` med en ny tid (t.ex. 12:00 med lunch).

### Nivå 2: utöka tabellen (enkelt)

**Uppgift 3: fler dagar**
Lägg till kolumner för torsdag och fredag. Kom ihåg att varje `<tr>` måste ha lika många celler.

**Uppgift 4: rubriktext**
Lägg till en `<caption>` om det inte redan finns, och ändra texten till något beskrivande (t.ex. "Mitt skolschema 2025").

### Nivå 3: styla tabellen (medel)

**Uppgift 5: ändra färgtema**
Byt ut `background-color` på `th` till en annan färg (t.ex. `#388e3c` för grönt, `#d32f2f` för rött). Välj en färg som du tycker ser bra ut.

**Uppgift 6: textskugga på rubriken**
Lägg till `text-shadow` på `h1`-taggen. Testa olika värden tills det ser snyggt ut:

```css
h1 {
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
}
```

### Nivå 4: kombinera allt (avancerat)

**Uppgift 7: bild och lista**
Lägg till en sektion under tabellen med:
1. En `<h2>`-rubrik (t.ex. "Favoritämnen").
2. En `<ul>`-lista med dina tre favoritämnen.
3. En bild som passar temat.

(Repetition: `<ul>`, `<li>`, `<img>` från labb 2!)

**Uppgift 8: länk till schema**
Lägg till en `<a>`-länk som leder till din skolas webbplats. Styla den utan understrykning och med en hover-effekt.

(Repetition: `<a>`, `text-decoration: none` från labb 2!)

### Nivå 5: boss-nivån

**Uppgift 9: ny tabell**
Skapa en helt ny tabell under den första. Temat är valfritt — det kan vara en poängtabell, en prislista, statistik från ett spel, eller vad du vill.

**Uppgift 10: den kompletta sidan**
Gör sidan till en riktig "skolportal" med:

1. En snygg centrerad rubrik med `text-shadow`.
2. Schemat i en tabell.
3. En sektion med favoritämnen (lista + bild).
4. En sektion med nyttiga länkar.
5. Allt centrerat med `.sida` (fast bredd + `margin: auto`).
6. Välj ett eget Google Font och minst en egen färg.
