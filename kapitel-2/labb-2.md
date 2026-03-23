# Labb 2 – stiliga länkar och text

I den här labben lär du dig göra snygga "knapp-länkar" utan understrykning, jobba med versaler och placera text ovanpå bakgrundsbilder. Du repeterar också bilder och marginaler från labb 1.

## Introduktion och mål

I den här labben tränar du på att:

* Ta bort understrykning på länkar med `text-decoration: none`.
* Styla länkar som knappar med `padding` och `background-color`.
* Använda `text-transform: uppercase` för versaler.
* Placera bakgrundsbilder med `background-position`.
* Repetition: `<figure>`, `<figcaption>`, marginaler.

## Startkod

Skapa två filer: `index.html` och `style.css`. Lägg en bakgrundsbild (`bakgrund.jpg`) i en mapp `bilder/`.

**index.html:**

```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Drömresan</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="hero">
        <h1>Drömresan</h1>
        <p>Upptäck världens vackraste platser</p>
        <a href="https://sv.wikipedia.org" class="knapp">Läs mer</a>
    </div>

    <div class="innehall">
        <h2>Populära resmål</h2>
        <p>Här är några platser vi rekommenderar.</p>

        <figure>
            <img src="bilder/bakgrund.jpg" alt="En vacker plats">
            <figcaption>En underbar destination</figcaption>
        </figure>
    </div>
</body>
</html>
```

**style.css:**

```css
body {
    font-family: 'Segoe UI', sans-serif;
    margin: 0;
    color: #333;
}

.hero {
    background-image: url('bilder/bakgrund.jpg');
    background-size: cover;
    background-position: center;
    color: white;
    padding: 100px 40px;
    text-align: center;
}

.hero h1 {
    font-size: 3rem;
    text-shadow: 2px 2px 6px rgba(0, 0, 0, 0.5);
}

.hero p {
    font-size: 1.2rem;
}

.knapp {
    display: inline-block;
    color: white;
    background-color: #e74c3c;
    padding: 15px 30px;
    text-decoration: none;
    text-transform: uppercase;
    font-weight: bold;
    border-radius: 5px;
    margin-top: 20px;
}

.innehall {
    padding: 40px;
}

img {
    width: 100%;
    max-width: 500px;
    border-radius: 10px;
}

figure {
    margin: 20px 0;
}

figcaption {
    font-style: italic;
    color: #777;
}
```

## Övningar och kodexempel

### Övning 1: en stilig länk

Gör en länk som ser ut som en knapp — ingen understrykning, med bakgrundsfärg och padding:

```css
.knapp {
    text-decoration: none;
    background-color: #e74c3c;
    color: white;
    padding: 15px 30px;
}
```

### Övning 2: versaler med text-transform

Gör all text versaler automatiskt:

```css
.knapp {
    text-transform: uppercase;
}
```

### Övning 3: bakgrundsposition

Styr vilken del av bilden som syns med `background-position`:

```css
.hero {
    background-position: center top;  /* Visar toppen av bilden */
}
```

Andra värden att testa: `center bottom`, `left center`, `right top`.

## Uppgifter

### Nivå 1: uppvärmning (mycket enkelt)

**Uppgift 1: ändra knapptext**
Ändra texten i `<a class="knapp">` till något annat (t.ex. "Boka nu" eller "Se bilder").

**Uppgift 2: ändra knappfärg**
I CSS, ändra `.knapp` `background-color` till en annan färg (t.ex. `#2ecc71` för grön eller `#3498db` för blå).

### Nivå 2: fler länkar (enkelt)

**Uppgift 3: hover på knappen**
Lägg till en hover-effekt som ändrar färgen när man håller musen över knappen:

```css
.knapp:hover {
    background-color: #c0392b;
}
```

**Uppgift 4: en till knapp**
Lägg till en andra `<a class="knapp">` i hero-sektionen. Den ska länka till en annan sida och ha en annan text.

### Nivå 3: text och bakgrund (medel)

**Uppgift 5: ändra bakgrundsposition**
Testa att ändra `background-position` i `.hero` till minst tre olika värden. Vilken ser bäst ut med din bild?

**Uppgift 6: text-transform på rubriken**
Lägg till `text-transform: uppercase` på `.hero h1` i CSS. Se hur rubriken ändras.

### Nivå 4: kombinera med figurer (avancerat)

**Uppgift 7: tre resmål**
Lägg till tre `<figure>`-block i `.innehall`, ett för varje resmål. Varje figur ska ha:
- En bild med `alt`-text.
- En `<figcaption>` med platsens namn.
- Ändra `margin-left` på varannan figur för att skapa variation.

(Repetition: `<figure>`, `<figcaption>`, `margin-left` från labb 1!)

**Uppgift 8: länk under varje bild**
Lägg till en `<a class="knapp">` under varje figur som leder till en relevant webbsida. Styla den med en annan bakgrundsfärg.

### Nivå 5: boss-nivån

**Uppgift 9: resesidan komplett**
Bygg en komplett resesida med:

1. En hero-sektion med bakgrundsbild, rubrik och knapp.
2. Minst tre resmåls-sektioner med `<figure>`, `<figcaption>` och en "Läs mer"-knapp.
3. Alla länkar är stilade utan understrykning.
4. Minst en rubrik med `text-transform: uppercase`.

**Uppgift 10: nytt tema**
Byt tema helt! Istället för resor, gör sidan om till t.ex. en matblogg, ett band eller en sportsida. Behåll samma teknik (bakgrundsbild, knapplänkar, figurer) men med nytt innehåll och nya färger.
