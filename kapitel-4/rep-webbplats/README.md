# Lektion: rep-webbplats

**Datum:** 2025-11-20

**Sammanfattning:** Träning inför prov

## Kod

### sida1.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="kontainer">
        <h1>Fem filmer</h1>
        <div class="meny">
            <a href="sida1.html" class="aktiv">Sida 1</a>
            <a href="sida2.html">Sida 2</a>
            <a href="sida3.html">Sida 3</a>
            <a href="sida4.html">Sida 4</a>
        </div>
        <h2>Lalaland</h2>
        <figure>
            <img src="" alt="">
            <figcaption>lknc lksjckn</figcaption>
        </figure>
        <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Dolore ipsam nobis fugit ipsum natus error, illo non hic nam quaerat minus est, praesentium harum rem temporibus delectus, quisquam neque? Molestiae?</p>
    </div>
</body>
</html>
```

### style.css
```css
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

body {}
.kontainer {
    background: #000;
    width: 800px;
    padding: 20px;
    margin: auto;
}
.kontainer h1 {}
.kontainer .meny {}
.kontainer .meny a {}
.kontainer .meny a:hover {}
.kontainer .meny a.aktiv {}
.kontainer h2 {}
.kontainer figure {}
.kontainer figure img {}
.kontainer figure figcaption {}
.kontainer p {}
```


