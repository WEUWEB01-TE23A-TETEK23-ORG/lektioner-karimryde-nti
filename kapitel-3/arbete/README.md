# Lektion: arbete

**Datum:** 2025-10-02

**Sammanfattning:** Tränat på div-box, länkar, klasser

## Kod

### arbete1.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>
<body class="sida1">
    <div>
        <h1>Arbete av Ulf Lundell</h1>

        <p>Om jag inte arbetade <br>
            vad i helvete skulle jag <br>
            göra då?</p>

        <p><a href="arbete2.html">&raquo;</a></p>
    </div>
</body>
</html>
```

### arbete2.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>
<body class="sida2">
    <div>
        <p><a href="arbete1.html">&laquo;</a></p>

        <p>Knarka kanske <br>
        Men det är ju också ett jobb <br>
        Ett jävla flängande med <br>
        inbrott och själva köpandet av <br>
        skiten och sen om igen <br>
        så det utesluter vi</p>

        <p><a href="arbete3.html">&raquo;</a></p>
    </div>
</body>
</html>
```

### arbete3.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>
<body class="sida3">
    <div>
        <p><a href="arbete2.html">&laquo;</a></p>

        <p>Jag kunde leva på andra <br>
        men risken finns ju <br>
        att också det är ett rätt så hårt <br>
        arbete</p>

        <p><a href="arbete4.html">&raquo;</a></p>
    </div>
</body>
</html>
```

### arbete4.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>
<body class="sida4">
    <div>
        <p><a href="arbete3.html">&laquo;</a></p>

        <p>Jag kunde lägga in mig på <br>
        sjukhus och bara ligga där <br>
        blickstilla <br>
        men jag kan ge mej fan på <br>
        att det också med tiden skulle kännas som ett <br>
        arbete</p>

        <p><a href="arbete5.html">&raquo;</a></p>
    </div>
</body>
</html>
```

### arbete5.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>
<body class="sida5">
    <div>
        <p><a href="arbete4.html">&laquo;</a></p>

        <p>Så jag arbetar väl på då <br>
            Jag har väl inget val</p>

        <p><a href="arbete6.html">&raquo;</a></p>
    </div>
</body>
</html>
```

### arbete6.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>
<body class="sida6">
    <div>
        <p><a href="arbete5.html">&laquo;</a></p>

        <p>Men någonting säger mej <br>
            att Gud från början <br>
            inte alls menade att vi skulle <br>
            syssla med nåt satans <br>
            arbete</p>
    </div>
</body>
</html>
```

### style.css
```css
@import url('https://fonts.googleapis.com/css2?family=Arvo:ital,wght@0,400;0,700;1,400;1,700&family=Playwrite+DE+SAS:wght@100..400&display=swap');

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

body.sida1 {
    background-image: url(./bilder/pattern1.jpg);
}
body.sida2 {
    background-image: url(./bilder/pattern2.jpg);
}
body.sida3 {
    background-image: url(./bilder/pattern3.webp);
}
body.sida4 {
    background-image: url(./bilder/pattern4.webp);
}
body.sida5 {
    background-image: url(./bilder/pattern5.jpg);
}
body.sida6 {
    background-image: url(./bilder/pattern3.webp);
}
div {
    font-family: "Arvo", serif;
    background-color: #fff;
    width: 500px;
    /* height: 400px; */
    border: 5px dotted #000;
    padding-top: 50px;
    padding-left: 50px;
    margin: auto;
    margin-top: 100px;
}
h1 {
    font-family: "Playwrite DE SAS", cursive;
    margin-bottom: 30px;
}
p {
    font-size: 25px;
    margin-bottom: 30px;
}
a {
    text-decoration: none;
    font-size: 40px;
    color: red;
}
```


