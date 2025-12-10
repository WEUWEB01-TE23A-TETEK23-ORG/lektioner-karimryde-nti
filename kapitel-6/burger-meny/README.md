# Lektion: burger-meny

**Datum:** 2025-11-20

**Sammanfattning:** Träning inför prov. Nästan klar. Klar med grunderna. Början.

## Kod

### index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Burger King meny</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="kontainer">
        <div class="meny">
            <img src="./bilder/header-logo.svg" alt="Logga">
            <a href="#">Meny</a>
            <a href="#">King Finder</a>
            <a href="#">Kampanjer</a>
            <a href="#">Karriär</a>
            <a href="#">Hemleverans</a>
            <a href="#">Kuponger</a>
            <a href="#">Real is King</a>

            <a href="#" class="hitta">Hitta Restaurang</a>
        </div>
        <div class="separator">
            <h1>Meny</h1>
        </div>
        <div class="innehall">
            <h2>News</h2>
            <div class="rutnat">
                <div class="box">
                    <img src="./bilder/ultimate-chedder-beef_fo_1100x1024.png" alt="Ultimate Cheddar Beef">
                    <p>Ultimate Cheddar Beef</p>
                </div>
                <div class="box">
                    <img src="./bilder/ultimate-chedder-doublebeef_fo_1100x1024.png" alt="Ultimate Cheddar Double Beef">
                    <p>Ultimate Cheddar Double Beef</p>
                </div>
                <div class="box">
                    <img src="./bilder/ultimate-chedder-chicken_fo_1100x1024.png" alt="Ultimate Cheddar Chicken">
                    <p>Ultimate Cheddar Chicken</p>
                </div>
                <div class="box">
                    <img src="./bilder/fo_xxl-dip_1100x1024.png" alt="Cheddar Dip XXL">
                    <p>Cheddar Dip XXL</p>
                </div>
                <div class="box">
                    <img src="./bilder/0924_mangobacon_fo_single_chicken_1920x1080.png" alt="Crispy Chicken Mango Bacon">
                    <p>Crispy Chicken Mango Bacon</p>
                </div>
                <div class="box">
                    <img src="./bilder/0924_mangobacon_fo_single_beef_1920x1080.png" alt="Mango Bacon Beef">
                    <p>Mango Bacon Beef</p>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
```

### style.css
```css
@import url('https://fonts.googleapis.com/css2?family=Chewy&display=swap');

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
    --Orange: #FF8732;
    --Brun: #502314;
    --Ljusbeige: #FBF7F1;
    --Beige: #F5EBDC;
    --Röd: #CC2200;
}

/* Sidans utseende */
body {
    background: var(--Ljusbeige)
}
.kontainer {
    width: 1200px;
    margin: auto;
    padding: 40px;
    font-family: "Chewy", system-ui;
    color: var(--Brun);
}

/* Sidhuvudets utseende */
.kontainer .meny {
    display: flex;
    justify-content: space-between;
    margin-bottom: 30px;
}
.kontainer .meny img {
    width: 70px;
}
.kontainer .meny a {
    color: var(--Brun);
    text-decoration: none;
    margin-top: 20px;
}
.kontainer .meny a.hitta {
    background-color: var(--Röd);
    color: var(--Ljusbeige);
    padding: 15px;
    border-radius: 10px;
    margin-top: 0;
    margin-left: 80px;
    height: 50px;
}

/* Separatorns utseende */
.kontainer .separator {
    background-color: var(--Orange);
    padding: 30px;
    margin-bottom: 30px;
}
.kontainer .separator h1 {
    color: var(--Ljusbeige);
}

/* Rutnätet med hamburgare osv.. */
.kontainer .innehall {}
.kontainer .innehall h2 {
    font-size: 50px;
    margin-bottom: 30px;
}
.kontainer .innehall .rutnat {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 30px;
}
.kontainer .innehall .rutnat .box {
    background: linear-gradient(to bottom, var(--Beige) 50%, transparent 50%);
    background-position: 0% 60%;
    background-size: 100% 200%;
    border-radius: 20px;
    text-align: center;
    padding: 30px;
    transition: background-position 0.5s;
}
.kontainer .innehall .rutnat .box:hover {
    background-position: 0 0;
}
.kontainer .innehall .rutnat .box img {
    width: 100%;
}
.kontainer .innehall .rutnat .box p {
    font-size: 25px;
}
```


