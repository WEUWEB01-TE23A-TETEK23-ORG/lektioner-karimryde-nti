# Lektion: bloggen

**Datum:** 2025-10-09

**Sammanfattning:** Tränat på div-boxar och klasser

## Kod

### index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Min blogg</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="kontainer">
        <h1>Min fina blogg</h1>
        <div class="inlagg">
            <img src="./bilder/torbjorn-helgesen-BZUymMFrIrY-unsplash.jpg" alt="Grilla korv">
            <h2>Grill!</h2>
            <p class="datum">Söndag 5:e oktober 2025</p>
            <p class="text">Kul och gott att grilla korv. Vi tog en utflykt till en skog i närheten och grillade korv. Barnen älskade det!</p>
        </div>
        <div class="inlagg">
            <img src="./bilder/markus-spiske-XHTBZpRBoi0-unsplash.jpg" alt="Bandy på is">
            <h2>Bandyturnering i Uppsala</h2>
            <p class="datum">Lördag 4:e oktober 2025</p>
            <p class="text">Idag åkte barnen till Uppsalas Recover hall. De spelade bandy tillsammans med Hammarby mot lag som Sirius.</p>
        </div>
        <div class="inlagg">
            <img src="./bilder/krisztian-tabori-ZQf4jzkpz1k-unsplash.jpg" alt="Tacos">
            <h2>Tacofredag</h2>
            <p class="datum">Fredag 3:e oktober 2025</p>
            <p class="text">Ikväll åt vi tacos igen - äntligen något som alla gillar. Vi kör en buffé med grönsaker med vegofärs och köttfärs.</p>
        </div>
    </div>
</body>
</html>
```

### style.css
```css
@import url('https://fonts.googleapis.com/css2?family=BBH+Sans+Bogle&family=Roboto:ital,wght@0,100..900;1,100..900&display=swap');

/* Enkel CSS-reset */
html {
    box-sizing: border-box;
}
*, *:before, *:after {
    box-sizing: inherit;
}
body, h1, h2, h3, h4, h5, h6, p, ul {
    margin: 0;
    padding: 0;
}

:root {
    --buff: #cb997eff;
    --desert-sand: #ddbea9ff;
    --champagne-pink: #ffe8d6ff;
    --ash-gray: #b7b7a4ff;
    --sage: #a5a58dff;
    --reseda-green: #6b705cff;
}

body {
    background-color: #000;
}
div.kontainer {
    background-color: var(--reseda-green);
    width: 800px;
    padding: 50px;
    margin: auto;
    font-family: "Roboto", sans-serif;
}
h1 {
    font-family: "BBH Sans Bogle", sans-serif;
    font-size: 80px;
    color: var(--champagne-pink);
    margin-bottom: 30px;
}
div.inlagg {
    background-color: var(--ash-gray);
    padding: 30px;
    margin-bottom: 30px;
}
img {
    width: 500px;
    border: 20px solid #fff;
    border-radius: 10px;
    margin-bottom: 20px;
}
h2 {
    margin-bottom: 20px;
    font-size: 40px;
}
p.datum {
    margin-bottom: 20px;
    font-weight: bold;
}
p.text {
    margin-bottom: 20px;
}
```


