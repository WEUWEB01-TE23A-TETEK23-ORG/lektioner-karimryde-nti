# Lektion: oppna-landskap

**Datum:** 2025-09-03

**Sammanfattning:** Tränat html, css som width, padding, radius, shadow, Google fonts

## Kod

### index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Öppna landskap</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Öppna landskap</h1>
    <p>Jag trivs bäst i öppna landskap, nära havet vill jag bo <br>
    Några månader om året, så att själen kan få ro  <br>
    Jag trivs bäst i öppna landskap, där vindarna får fart  <br>
    Där lärkorna står högt i skyn och sjunger underbart  <br>
    Där bränner jag mitt brännvin själv och kryddar med Johannesört  <br>
    Och dricker det med välbehag, till sill och hembakt vört  <br>
    Jag trivs bäst i öppna landskap, nära havet vill jag bo </p>
    <p>Jag trivs bäst i fred och frihet, för både kropp och själ <br>
    Ingen kommer i min närhet, som stänger in och stjäl <br>
    Jag trivs bäst när dagen bräcker, när fälten fylls av ljus <br>
    När tuppar gal på avstånd, när det är långt till närmsta hus <br>
    Men ändå så pass nära att en tyst och stilla natt <br>
    När man sitter under stjärnorna, kan höra festens skratt <br>
    Jag trivs bäst i fred och frihet, för både kropp och själ</p>
    <p>Jag trivs bäst när havet svallar och måsarna ger skri <br>
    När stranden fylls av snäckskal med havsmusik uti <br>
    När det klara och det enkla får råda som det vill <br>
    När ja är ja och nej är nej och tvivlet tiger still <br>
    Då binder jag en krans av löv och lägger den vid närmaste sten <br>
    Där runor ristats för vår skull, nå'n gång för länge sen <br>
    Jag trivs bäst när havet svallar och måsarna ger skri</p>
    <p>Jag trivs bäst i öppna landskap <br>
    Nära havet vill jag bo</p>
    <p>Källa: <a href="https://www.musixmatch.com/pro/">Musixmatch</a></p>
</body>
</html>
```

### style.css
```css
@import url('https://fonts.googleapis.com/css2?family=Irish+Grover&family=Niconne&display=swap');
body {
    background-image: url(./bilder/bakgrund.jpg);
    padding: 50px;
}
h1 {
    color: #FFF;
    font-family: "Irish Grover", system-ui;
    font-size: 50px;
    text-shadow: 5px 5px 5px #111;
}
p {
    font-family: "Niconne", cursive;
    font-size: 20px;
    color: #FFF;
    background-color: #54618699;
    width: 550px;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 5px 5px 5px #111;
}
a {
    color: #FFF;
}
```


