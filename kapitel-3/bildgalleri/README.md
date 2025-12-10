# Lektion: bildgalleri

**Datum:** 2025-10-13

**Sammanfattning:** Tränat på div-boxar, klasser, flex för höger-placering

## Kod

### index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bildgalleri</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="kontainer">
        <h1>Nasa Moon Gallery</h1>
        <p class="intro">NASA explores the unknown in air and space, innovates for the benefit of humanity, and inspires the world through discovery.</p>
        <div class="box">
            <img src="./bilder/as11-40-5875~large.jpg" alt="Buzz Aldrin Stands Beside the U.S. Flag on the Moon">
            <p class="bildtext">Astronaut Edwin "Buzz" Aldrin poses for a photograph beside the U.S. flag during an Apollo 11 extravehicular activity (EVA) on the lunar surface.</p>
        </div>
        <div class="box">
            <img src="./bilder/27410471634-20aa91b309-o.webp" alt="Hubble and the Moon">
            <p class="bildtext">One of the STS-103 astronauts inside Discovery's cabin took this image of the full moon backdropped against the blackness of space over Earth's horizon. The top of the berthed Hubble Space Telescope (HST) appears in the frame.</p>
        </div>
        <div class="box">
            <img src="./bilder/2-apollo-15-on-moon-1.webp" alt="Apollo Astronaut James B. Irwin,">
            <p class="bildtext">Apollo Astronaut James B. Irwin, lunar module pilot, works at the Lunar Roving Vehicle during the first Apollo 15 lunar surface extravehicular activity (EVA) at the Hadley-Apennine landing site. The shadow of the Lunar Module "Falcon" is in the foreground. This view is looking northeast, with Mount Hadley in the background. This photograph was taken by astronaut David R. Scott, commander.</p>
        </div>
    </div>
</body>
</html>
```

### style.css
```css
@import url('https://fonts.googleapis.com/css2?family=Audiowide&family=Noto+Sans:ital,wght@0,100..900;1,100..900&display=swap');
:root {
    /* CSS HEX */
    --cordovan: #952F3Cff;
    --eerie-black: #171814ff;
    --french-gray: #C8C8CCff;
    --davys-gray: #5D5C5Cff;
    --dim-gray: #747474ff;
}

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

body {
    background-color: var(--eerie-black);
}
.kontainer {
    width: 700px;
    padding: 30px;
    margin: auto;
    font-family: "Noto Sans", sans-serif;
    color: var(--french-gray);
}
h1 {
    font-family: "Audiowide", sans-serif;
    margin-bottom: 30px;
}
p.intro {
    margin-bottom: 30px;
}
.box {
    display: flex;
    padding: 30px;
    background-color: var(--davys-gray);
    margin-bottom: 30px;
}
img {
    width: 50%;
    margin-right: 20px;
}
p.bildtext {}
```


