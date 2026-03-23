# Labb 1 – mitt band

Nu ska du bygga din första **flersidiga webbplats**! Sidan handlar om ett band (riktigt eller påhittat) och har tre sidor som delar på samma meny och CSS-fil.

## Introduktion och mål

I den här labben tränar du på att:

* Bygga en webbplats med flera HTML-sidor.
* Skapa en gemensam navigeringsmeny med `<a>`-taggar.
* Markera aktiv sida med klassen `.aktiv`.
* Använda `display: inline-block` för menylänkar.
* Repetition: `.kontainer`, CSS-reset, klasser, CSS-variabler.

## Startkod

Skapa tre HTML-filer och en CSS-fil: `sida1.html`, `sida2.html`, `sida3.html` och `style.css`.

**sida1.html:**

```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mitt band – Hem</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="kontainer">
        <div class="meny">
            <a href="sida1.html" class="aktiv">Hem</a>
            <a href="sida2.html">Medlemmar</a>
            <a href="sida3.html">Låtar</a>
        </div>

        <h1>Välkommen till Bandnamn!</h1>
        <p>Vi spelar musik som gör dig glad.</p>
    </div>
</body>
</html>
```

**sida2.html:**

```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mitt band – Medlemmar</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="kontainer">
        <div class="meny">
            <a href="sida1.html">Hem</a>
            <a href="sida2.html" class="aktiv">Medlemmar</a>
            <a href="sida3.html">Låtar</a>
        </div>

        <h1>Medlemmar</h1>
        <p>Här är vi som spelar i bandet.</p>
    </div>
</body>
</html>
```

**sida3.html:**

```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mitt band – Låtar</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="kontainer">
        <div class="meny">
            <a href="sida1.html">Hem</a>
            <a href="sida2.html">Medlemmar</a>
            <a href="sida3.html" class="aktiv">Låtar</a>
        </div>

        <h1>Våra låtar</h1>
        <p>Här är några av våra bästa låtar.</p>
    </div>
</body>
</html>
```

**style.css:**

```css
/* CSS-reset */
html { box-sizing: border-box; }
*, *:before, *:after { box-sizing: inherit; }
body, h1, h2, h3, p, ul { margin: 0; padding: 0; }

:root {
    --bakgrund: #2c3e50;
    --text: #ecf0f1;
    --accent: #e74c3c;
    --meny-bg: #1a252f;
}

body {
    font-family: 'Segoe UI', sans-serif;
    background-color: var(--bakgrund);
    color: var(--text);
}

.kontainer {
    width: 700px;
    margin: auto;
    padding: 20px;
}

.meny {
    background-color: var(--meny-bg);
    padding: 15px;
    border-radius: 8px;
    margin-bottom: 25px;
}

.meny a {
    color: var(--text);
    text-decoration: none;
    display: inline-block;
    padding: 8px 20px;
    border-radius: 5px;
    margin-right: 5px;
}

.meny a:hover {
    background-color: var(--accent);
}

.meny .aktiv {
    background-color: var(--accent);
    font-weight: bold;
}
```

## Övningar och kodexempel

### Övning 1: aktiv klass

På varje sida flyttar du `class="aktiv"` till rätt länk. På sida1 har "Hem" klassen, på sida2 har "Medlemmar" klassen, osv.

### Övning 2: inline-block

`display: inline-block` gör att länkarna hamnar bredvid varandra men fortfarande kan ha padding:

```css
.meny a {
    display: inline-block;
    padding: 8px 20px;
}
```

## Uppgifter

### Nivå 1: uppvärmning (mycket enkelt)

**Uppgift 1: byt bandnamn**
Ändra "Bandnamn" till ett eget bandnamn (riktigt eller påhittat) på alla tre sidor.

**Uppgift 2: kontrollera aktiv**
Klicka mellan sidorna i webbläsaren. Kontrollera att rätt menylänk är markerad på varje sida. Om inte, flytta `class="aktiv"` till rätt `<a>`.

### Nivå 2: innehåll (enkelt)

**Uppgift 3: medlemmarssidan**
På sida2, lägg till en lista (`<ul>`) med minst tre bandmedlemmar. Skriv ett kort stycke om varje person.

**Uppgift 4: låtsidan**
På sida3, lägg till en lista med minst tre låtar. Lägg till en länk till en YouTube-video eller liknande.

### Nivå 3: styling (medel)

**Uppgift 5: hover-effekt**
Se till att `.meny a:hover` har en annan bakgrundsfärg som skiljer sig från `.aktiv`. Testa att lägga till `transition: 0.2s` för mjuk övergång.

**Uppgift 6: byt färgtema**
Gå till [Coolors.co](https://coolors.co/) och generera en ny palett. Byt ut alla färger i `:root`.

### Nivå 4: bilder och mer innehåll (avancerat)

**Uppgift 7: bilder på medlemmarna**
Skapa en mapp `bilder/` och lägg in bilder. På sida2, lägg till en `<figure>` med bild och `<figcaption>` för varje medlem.

(Repetition: `<figure>`, `<figcaption>` från kapitel 2!)

**Uppgift 8: fjärde sidan**
Skapa `sida4.html` (t.ex. "Kontakt"). Glöm inte att:
1. Kopiera menyn och lägga till den nya länken.
2. Uppdatera menyn på alla fyra sidor.
3. Sätta `class="aktiv"` på rätt ställe.

### Nivå 5: boss-nivån

**Uppgift 9: fem sidor**
Bygg ut webbplatsen till minst fem sidor med unik innehåll på varje. Menyn ska finnas på varje sida med korrekt `.aktiv`.

**Uppgift 10: den kompletta bandsidan**
Gör sidan riktigt snygg:

1. Importera ett Google Font.
2. Lägg till bilder på minst två sidor.
3. Ge `h1` en `text-shadow`.
4. Ge `.kontainer` en `background-color` och `border-radius`.
5. Se till att hover-effekter och `.aktiv` fungerar korrekt på alla sidor.
