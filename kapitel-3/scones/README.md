# Lektion: scones

**Datum:** 2025-10-06

**Sammanfattning:** Tränat på div som kontainer

## Kod

### index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Scones recept</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="kontainer">
        <h1>Engelska scones</h1>
        <img src="https://assets.icanet.se/e_sharpen:80,q_auto,dpr_1.25,w_718,h_718,c_lfill/imagevaultfiles/id_42689/cf_259/engelska_scones.jpg"
            alt="Engelska scones">
        <p>Engelska scones är en riktig klassiker och med det här receptet bakar du härliga och smarriga scones med
            bland annat choklad och vispgrädde! Fabulöst och fantastiskt gott! Perfekt att lyxa till helgfrukosten med.
        </p>
        <h2>Ingredienser</h2>
        <ul>
            <li>4 dl vetemjöl</li>
            <li>1 tsk salt</li>
            <li>1 tsk bakpulver</li>
            <li>1/2 dl hackad, mörk choklad eller russin</li>
            <li>50 g rumsvarmt smör</li>
            <li>1 1/2 dl vispgrädde</li>
            <li>2 msk vispgrädde till pensling</li>
        </ul>
        <h2>Gör så här</h2>
        <ol>
            <li>Sätt ugnen på 225°C.</li>
            <li>Nyp ihop mjöl, salt, bakpulver och choklad eller russin med smöret.</li>
            <li>Tillsätt grädden och knåda snabbt ihop till en smidig deg.</li>
            <li>Platta ut degen till en 2 cm tjock platta och ta ut portionsstora rundlar med hjälp av mått eller glas.
            </li>
            <li>Lägg dem på en bakpappersklädd plåt. Pensla dem med grädde.</li>
            <li>Grädda mitt i ugnen ca 10 minuter, tills de fått fin färg. Servera nybakta. Pudra ev över florsocker.
            </li>
        </ol>
        <p>Text och bild från <a href="https://www.ica.se/recept/">ICA.se</a></p>
    </div>
</body>
</html>
```

### style.css
```css
@import url('https://fonts.googleapis.com/css2?family=Fjalla+One&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&display=swap');

/* Enkel CSS-reset */
html {
    box-sizing: border-box;
}

*,
*:before,
*:after {
    box-sizing: inherit;
}

body,
h1,
h2,
h3,
h4,
h5,
h6,
p,
ul {
    margin: 0;
    padding: 0;
}

/* Färgpaletten:
https://coolors.co/palette/606c38-283618-fefae0-dda15e-bc6c25
*/

/* Sidans utseende */
body {
    background-image: url(./bilder/mohamed-hassouna-N4gtuEZ5gWc-unsplash.jpg);
    background-size: cover;
    background-attachment: fixed;
    /* Inte skrolla! */
}

/* Sidans utseende */
div.kontainer {
    width: 700px;
    padding: 50px;
    background-color: #fefae0f3;
    border: 10px solid #DDA15E;
    margin: auto;
    margin-top: 50px;
    border-radius: 10px;
    font-family: "Libre Baskerville", serif;
    color: #283618;
}

h1 {
    font-family: "Fjalla One", sans-serif;
    font-size: 80px;
    margin-bottom: 20px;
}

img {
    width: 400px;
    border: 20px solid #FFF;
    box-shadow: 5px 5px 10px #888;
    margin-bottom: 20px;
}

h2 {
    font-family: "Fjalla One", sans-serif;
    margin-bottom: 20px;
}

ol {
    margin-bottom: 20px;
}

ul {
    margin-bottom: 20px;
    margin-left: 30px;
    list-style-type: square;
}

p {
    font-size: 16px;
    margin-bottom: 20px;
}

a {
    text-decoration: none;
    color: #606C38;
    font-weight: bold;
    border-bottom: 3px solid #606C38;
}
```


