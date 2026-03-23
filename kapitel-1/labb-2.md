# Labb 2 – listor, länkar och bilder

Nu kan du rubriker och stycken — dags att lägga till mer innehåll! I den här labben bygger du en sida med listor, klickbara länkar och bilder.

## Introduktion och mål

I den här labben tränar du på att:

* Skapa punktlistor med `<ul>` och `<li>`.
* Länka till andra webbsidor med `<a>`.
* Visa bilder med `<img>`.
* Styla listor och länkar med CSS.
* Kombinera rubriker, stycken, listor och bilder på samma sida (repetition).

## Startkod

Skapa två filer: `index.html` och `style.css`. Skapa också en mapp som heter `bilder` och lägg in valfri bild (döp den till `bild1.jpg`).

**index.html:**

```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mina favoriter</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Mina favoriter</h1>
    <p>Här samlar jag allt jag gillar.</p>

    <h2>Favoritfilmer</h2>
    <ul>
        <li>Film 1</li>
        <li>Film 2</li>
        <li>Film 3</li>
    </ul>
</body>
</html>
```

**style.css:**

```css
body {
    font-family: Georgia, serif;
    background-color: #fff8e7;
    color: #333;
    padding: 20px;
}

h1 {
    color: #b8860b;
}

h2 {
    color: #556b2f;
}
```

## Övningar och kodexempel

### Övning 1: en punktlista

En lista skapas med `<ul>` (unordered list) och `<li>` (list item):

```html
<ul>
    <li>Äpplen</li>
    <li>Bananer</li>
    <li>Apelsiner</li>
</ul>
```

### Övning 2: en länk

En länk tar besökaren till en annan sida. `href` anger adressen:

```html
<a href="https://sv.wikipedia.org">Wikipedia</a>
```

### Övning 3: en bild

Bilder visas med `<img>`. `src` pekar på filen, `alt` beskriver bilden:

```html
<img src="bilder/bild1.jpg" alt="En beskrivning av bilden">
```

## Uppgifter

### Nivå 1: uppvärmning (mycket enkelt)

**Uppgift 1: byt filmerna**
Ändra de tre filmerna i listan till dina egna favoritfilmer.

**Uppgift 2: lägg till en länk**
Lägg till en länk under listan som leder till en filmsida (t.ex. IMDb). Texten ska vara "Hitta fler filmer här".

### Nivå 2: fler listor (enkelt)

**Uppgift 3: ny lista**
Lägg till en `<h2>`-rubrik som heter "Favoritlåtar". Skapa en ny `<ul>`-lista med minst fyra låtar.

**Uppgift 4: bild**
Lägg till en bild på sidan med `<img>`. Bilden ska ligga i mappen `bilder/`. Glöm inte `alt`-texten!

### Nivå 3: styling (medel)

**Uppgift 5: styla listan**
I CSS, ge `li`-elementen lite avstånd med `margin-bottom` och en annan `font-size`:

```css
li {
    margin-bottom: 8px;
    font-size: 18px;
}
```

**Uppgift 6: styla länken**
Ge `a`-taggen en egen färg och ta bort understrykningen:

```css
a {
    color: #b8860b;
    text-decoration: none;
}
```

Testa även att lägga till en hover-effekt:

```css
a:hover {
    text-decoration: underline;
}
```

### Nivå 4: kombinera allt (avancerat)

**Uppgift 7: tredje sektionen**
Lägg till en tredje sektion med `<h2>` (t.ex. "Favoritmat"). Den ska ha en lista, en bild och en länk till ett recept.

**Uppgift 8: styla bilden**
Ge bilden en fast bredd och rundade hörn i CSS:

```css
img {
    width: 300px;
    border-radius: 10px;
}
```

### Nivå 5: boss-nivån

**Uppgift 9: en riktig favoritsida**
Bygg ut sidan till minst fyra sektioner med olika teman. Varje sektion ska ha:

1. En `<h2>`-rubrik.
2. En `<ul>`-lista med minst tre punkter.
3. En bild.
4. En länk.

**Uppgift 10: gör det snyggt**
Styla hela sidan så den ser professionell ut:

1. Centrera allt innehåll med `text-align: center` eller `margin: auto` och en fast bredd.
2. Ge sidan en snygg bakgrundsfärg (eller bakgrundsbild).
3. Ge bilder en `box-shadow`.
4. Testa att importera ett Google Font och använda det.
