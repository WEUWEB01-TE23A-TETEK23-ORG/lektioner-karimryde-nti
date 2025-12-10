# Lektion: fiji-reklam

**Datum:** 2025-09-08

**Sammanfattning:** Tränat på margin och padding, uppercase, html-entities

## Kod

### index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fiji</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Drömsemester</h1>
    <h2>På Fiji-öarna &#x2600;</h2>
    <p><a href="#">Se mer &rsaquo;</a></p>
</body>
</html>
```

### style.css
```css
body {
    background-image: url(./bilder/mohamed-saushan-hZ6tMbkAIMk-unsplash.jpg);
    background-size: cover;
    background-position: 0 -100px;
}
h1 {
    font-family: sans-serif;
    font-size: 70px;
    color: #42a4ff;
    text-shadow: 3px 3px 1px plum;
    text-transform: uppercase;
    margin-top: 50px;
    margin-left: 100px;
}
h2 {
    font-family: sans-serif;
    font-size: 40px;
    color: #42a4ff;
    text-shadow: 3px 3px 1px plum;
    margin-top: 50px;
    margin-left: 100px;
}
p {
    font-family: sans-serif;
    font-size: 25px;
    margin-top: 200px;
    margin-left: 500px;
}
a {
    background-color: plum;
    color: #FFF;
    text-decoration: none;
    padding: 10px 50px 10px 50px;
    border-radius: 5px;
    border: 1px solid #FFF;
}
```


