# Labb 2 – receptsamlingen

Nu kan du boxar och klasser — dags att bygga en snygg sida med en kontainer, CSS-variabler och upprepade klasser! Du bygger en receptsamling där varje recept har samma struktur.

## Introduktion och mål

I den här labben tränar du på att:

* Använda `.kontainer` för att centrera innehåll.
* Definiera färgpaletter med CSS-variabler (`:root`).
* Skapa återanvändbara klasser (`.kort`, `.kontainer`).
* Styla med `border`, `background-color` och `padding`.
* Repetition: CSS-reset, `<div>`, klasser, `box-shadow`.

## Startkod

Skapa två filer: `index.html` och `style.css`.

**index.html:**

```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Receptsamlingen</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="kontainer">
        <h1>Receptsamlingen</h1>
        <p class="intro">Mina bästa recept samlade på ett ställe.</p>

        <div class="kort">
            <h2>Pannkakor</h2>
            <p class="beskrivning">Klassiska svenska pannkakor — enkla och goda!</p>
            <h3>Ingredienser</h3>
            <ul>
                <li>3 dl mjöl</li>
                <li>6 dl mjölk</li>
                <li>3 ägg</li>
                <li>1 nypa salt</li>
            </ul>
        </div>

        <div class="kort">
            <h2>Pasta med pesto</h2>
            <p class="beskrivning">Snabb middag på under 15 minuter.</p>
            <h3>Ingredienser</h3>
            <ul>
                <li>400 g pasta</li>
                <li>2 msk pesto</li>
                <li>Parmesan</li>
            </ul>
        </div>
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
    --bakgrund: #fdf6e3;
    --text: #333;
    --accent: #cb4b16;
    --kort-bg: #ffffff;
    --kort-kant: #e0d5c1;
}

body {
    font-family: Georgia, serif;
    background-color: var(--bakgrund);
    color: var(--text);
}

.kontainer {
    width: 650px;
    margin: auto;
    padding: 30px 20px;
}

h1 {
    color: var(--accent);
    margin-bottom: 5px;
}

.intro {
    color: #777;
    margin-bottom: 30px;
}

.kort {
    background-color: var(--kort-bg);
    border: 2px solid var(--kort-kant);
    border-radius: 10px;
    padding: 25px;
    margin-bottom: 20px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.kort h2 {
    color: var(--accent);
    margin-bottom: 5px;
}

.kort h3 {
    margin-top: 15px;
    margin-bottom: 8px;
}

.beskrivning {
    font-style: italic;
    color: #666;
}

ul {
    padding-left: 25px;
}

li {
    margin-bottom: 4px;
}
```

## Övningar och kodexempel

### Övning 1: kontainer

`.kontainer` centrerar innehållet och ger det en fast bredd:

```css
.kontainer {
    width: 650px;
    margin: auto;
    padding: 30px 20px;
}
```

### Övning 2: CSS-variabler

Definiera färger en gång i `:root` och använd dem överallt:

```css
:root {
    --accent: #cb4b16;
}

h1 {
    color: var(--accent);
}
```

Om du ändrar `--accent` ändras alla element som använder den!

## Uppgifter

### Nivå 1: uppvärmning (mycket enkelt)

**Uppgift 1: egna recept**
Byt ut recepten till dina egna (eller hitta på nya). Ändra rubriker, beskrivningar och ingredienser.

**Uppgift 2: ändra färgtema**
Gå till [Coolors.co](https://coolors.co/) och generera en ny palett. Byt ut värdena i `:root`.

### Nivå 2: fler kort (enkelt)

**Uppgift 3: tredje receptet**
Lägg till ett tredje `.kort` med ett nytt recept. Följ samma HTML-struktur som de andra.

**Uppgift 4: fjärde receptet**
Lägg till ett fjärde kort. Notera hur `.kort`-klassen ger alla kort samma utseende automatiskt!

### Nivå 3: styla mer (medel)

**Uppgift 5: hover-effekt på kort**
Lägg till en hover-effekt som ändrar kantfärgen eller skuggan:

```css
.kort:hover {
    border-color: var(--accent);
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
}
```

**Uppgift 6: tillagningsordning**
I ett av recepten, byt ut `<ul>` mot `<ol>` (numrerad lista) och skriv tillagningsstegen i ordning.

### Nivå 4: extra innehåll (avancerat)

**Uppgift 7: bilder i recepten**
Lägg till en `<figure>` med bild och `<figcaption>` i varje receptkort. Ge bilden `width: 100%` och `border-radius: 8px`.

(Repetition: `<figure>`, `<figcaption>` från kapitel 2!)

**Uppgift 8: bakgrundsbild**
Ge `body` en bakgrundsbild istället för en bakgrundsfärg. Använd `background-attachment: fixed` så bilden inte scrollar med.

### Nivå 5: boss-nivån

**Uppgift 9: sex recept**
Bygg ut samlingen till minst sex receptkort. Variera innehållet — minst ett recept ska ha en bild och tillagningssteg med `<ol>`.

**Uppgift 10: den kompletta kokboken**
Gör sidan till en riktig kokbok:

1. Importera ett Google Font som passar temat.
2. Ge sidan en fin bakgrundsbild med `background-attachment: fixed`.
3. Alla kort ska ha bilder, ingredienser och tillagningssteg.
4. Lägg till en "Om mig"-sektion i toppen med en `<figure>` (ditt "kockfoto").
5. Minst en länk till en extern receptsida (stilad som knapp, utan understrykning).
