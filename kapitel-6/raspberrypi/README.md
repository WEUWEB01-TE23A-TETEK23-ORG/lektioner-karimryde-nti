# Lektion: raspberrypi

**Datum:** 2025-11-13

**Sammanfattning:** CSS grid. Tränat på verklig sida med kolumner och CSS grid.

## Kod

### index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Think it. Build it.</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="kontainer">
        <h1>Think it. Build it.</h1>
        <p class="intro">Raspberry Pi gives you the tools you need to make the tech you want, at a price you’ll like.</p>
        <div class="kolumner-3">
            <div class="kolumn">
                <img src="./bilder/Cluster-800x533.webp" alt="Raspberry Pi cluster">
                <h2>How to build a Raspberry Pi cluster</h2>
                <p>A Raspberry Pi cluster is a low-cost, versatile system you can use for all kinds of clustered-computing related technologies, and you have total control over the machines that constitute it.</p>
                <a href="#">Read more →</a>
            </div>
            <div class="kolumn">
                <img src="./bilder/hero.webp" alt="Wi-Fi hotspot">
                <h2>Host a Wi-Fi hotspot with a Raspberry Pi</h2>
                <p>This Raspberry Pi-hosted Wi-Fi hotspot connects to a guest Wi-Fi network, then runs a separate private Wi-Fi network for all of your devices.</p>
                <a href="#">Read more →</a>
            </div>
            <div class="kolumn">
                <img src="./bilder/router.webp" alt="Pi-hole">
                <h2>Block ads at home with Pi-hole</h2>
                <p>Pi-hole blocks internet ads at your router, removing bandwidth-sucking and privacy-invading ads from your whole network.</p>
                <a href="#">Read more →</a>
            </div>
        </div>
    </div>
</body>
</html>
```

### style.css
```css
@import url('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100..900;1,100..900&display=swap');

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
    background-image: url(./bilder/red-right-dbf3ede240dcea450fd48e7116aa6424.svg);
}
.kontainer {
    width: 1000px;
    margin: auto;
    padding: 20px;
    background-color: #f8f8f8;
    font-family: "Roboto", sans-serif;
    font-style: normal;
}
.kontainer h1 {
    text-align: center;
    margin-bottom: 30px;
}
.kontainer .intro {
    text-align: center;
    margin-bottom: 20px;
}
.kontainer .kolumner-3 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 30px;
}
.kontainer .kolumner-3 .kolumn {
    border-radius: 20px;
    background-color: #fff;
    display: grid;
    grid-template-rows: auto auto 1fr auto;
}
.kontainer .kolumner-3 .kolumn:hover {
    box-shadow: 0 10px 10px #999;
}
.kontainer .kolumn  img {
    width: 100%;
    border-radius: 20px 20px 0 0;
    margin-bottom: 15px;
}
.kontainer .kolumn  h2 {
    font-size: 16px;
    margin: 15px 10px;
}
.kontainer .kolumn  p {
    font-size: 13px;
    margin: 15px 10px;
    color: #555;
}
.kontainer .kolumn  a {
    font-size: 13px;
    margin: 15px 10px;
}
```


