# Labb 1 – bilder med bildtext

I den här labben jobbar du med bilder, bildtexter och marginaler. Du lär dig att visa bilder på ett proffsigt sätt med `<figure>` och `<figcaption>`.

## Introduktion och mål

I den här labben tränar du på att:

* Visa bilder med `<img>` (repetition).
* Använda `<figure>` och `<figcaption>` för bild med bildtext.
* Flytta element med `margin-left` och `margin-top`.
* Styla bilder med `border-radius` och `box-shadow` (repetition).

## Startkod

Skapa två filer: `index.html` och `style.css`. Skapa en mapp `bilder/` och lägg in tre valfria bilder (`bild1.jpg`, `bild2.jpg`, `bild3.jpg`).

**index.html:**

```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bildgalleriet</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Mitt bildgalleri</h1>

    <figure>
        <img src="bilder/bild1.jpg" alt="Beskrivning av bild 1">
        <figcaption>Bild 1 – min första bild</figcaption>
    </figure>
</body>
</html>
```

**style.css:**

```css
body {
    font-family: Georgia, serif;
    background-color: #fafafa;
    color: #333;
    padding: 20px;
}

h1 {
    color: #2c3e50;
}

figure {
    margin: 0;
    margin-bottom: 30px;
}

img {
    width: 400px;
    border-radius: 10px;
}

figcaption {
    font-style: italic;
    color: #777;
    margin-top: 5px;
}
```

## Övningar och kodexempel

### Övning 1: figure och figcaption

`<figure>` grupperar en bild med sin beskrivning. `<figcaption>` är bildtexten:

```html
<figure>
    <img src="bilder/bild1.jpg" alt="En vacker vy">
    <figcaption>En solnedgång vid havet</figcaption>
</figure>
```

### Övning 2: marginaler

`margin-left` flyttar ett element åt höger. `margin-top` flyttar det nedåt:

```css
figure {
    margin-left: 50px;
    margin-top: 30px;
}
```

## Uppgifter

### Nivå 1: uppvärmning (mycket enkelt)

**Uppgift 1: byt bild**
Byt ut bilden till en egen bild. Ändra `alt`-texten och `<figcaption>` så de beskriver din bild.

**Uppgift 2: lägg till en bild**
Lägg till en andra `<figure>` med en ny bild, en `alt`-text och en `<figcaption>`.

### Nivå 2: fler bilder (enkelt)

**Uppgift 3: tre bilder**
Se till att du har minst tre `<figure>`-block på sidan. Varje bild ska ha en unik bildtext.

**Uppgift 4: styla bildtexten**
Ändra `figcaption` i CSS: testa en annan `color`, `font-size` och ta bort `font-style: italic` om du vill.

### Nivå 3: marginaler och placering (medel)

**Uppgift 5: flytta en bild**
Ge en av dina `<figure>`-block en klass (t.ex. `class="indragen"`) och i CSS, ge den `margin-left: 100px`.

**Uppgift 6: avstånd mellan bilder**
Ge alla `figure`-element `margin-bottom: 40px` och `margin-top: 20px` så att det blir luftigt.

### Nivå 4: snygga till det (avancerat)

**Uppgift 7: bildskugga**
Lägg till `box-shadow` på `img` för att ge bilderna djup:

```css
img {
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}
```

(Repetition: `box-shadow` från kapitel 1!)

**Uppgift 8: rubrik och stycke**
Lägg till en `<h2>`-rubrik och ett `<p>`-stycke ovanför varje figur som introducerar bilden. Använd `<strong>` för att markera viktiga ord.

(Repetition: `<h2>`, `<p>`, `<strong>` från kapitel 1!)

### Nivå 5: boss-nivån

**Uppgift 9: bildgalleri med tema**
Välj ett tema (t.ex. "Mina husdjur", "Favoritplatser", "Bästa matbilderna") och bygg ett galleri med minst fyra bilder. Varje bild ska ha en rubrik, beskrivande text och bildtext.

**Uppgift 10: styla som ett proffs**
Gör sidan extra snygg:

1. Importera ett Google Font och använd det.
2. Centrera allt med `text-align: center`.
3. Ge bilder en maxbredd (t.ex. `max-width: 500px`) och `border-radius: 15px`.
4. Ge sidan en bakgrundsfärg som passar temat.
5. Lägg till `text-shadow` på rubriken.
