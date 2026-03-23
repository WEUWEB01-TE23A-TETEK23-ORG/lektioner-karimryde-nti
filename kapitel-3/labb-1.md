# Labb 1 – färgglada boxar

Välkommen till kapitel 3! Här lär du dig använda `<div>` som en "låda" du kan styla. Du lär dig också om CSS-klasser och den viktiga CSS-reseten.

## Introduktion och mål

I den här labben tränar du på att:

* Använda `<div>` för att gruppera innehåll i boxar.
* Skapa och använda CSS-klasser (`.box`, `.stor`, `.liten`).
* Använda en CSS-reset för att nollställa marginal och padding.
* Styla boxar med `width`, `height`, `padding`, `background-color` och `border-radius`.

## Startkod

Skapa två filer: `index.html` och `style.css`.

**index.html:**

```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Färgglada boxar</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Mina boxar</h1>

    <div class="box rod">
        <h2>Box 1</h2>
        <p>Jag är en röd box.</p>
    </div>

    <div class="box bla">
        <h2>Box 2</h2>
        <p>Jag är en blå box.</p>
    </div>

    <div class="box gron">
        <h2>Box 3</h2>
        <p>Jag är en grön box.</p>
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

body {
    font-family: sans-serif;
    background-color: #f0f0f0;
    padding: 20px;
}

h1 {
    text-align: center;
    margin-bottom: 20px;
}

.box {
    width: 300px;
    padding: 20px;
    margin-bottom: 15px;
    border-radius: 10px;
    color: white;
}

.rod {
    background-color: #e74c3c;
}

.bla {
    background-color: #3498db;
}

.gron {
    background-color: #27ae60;
}
```

## Övningar och kodexempel

### Övning 1: vad är en div?

En `<div>` är en osynlig "låda" som du kan fylla med innehåll och styla med CSS:

```html
<div class="box">
    <p>Jag är inne i en box!</p>
</div>
```

### Övning 2: CSS-klasser

En klass skrivs med `class="namn"` i HTML och `.namn` i CSS:

```html
<div class="box rod">Röd box</div>
```

```css
.rod {
    background-color: #e74c3c;
}
```

Ett element kan ha flera klasser (separerade med mellanslag).

### Övning 3: CSS-reset

Reseten tar bort webbläsarens standardmarginaler så att allt börjar från noll:

```css
html { box-sizing: border-box; }
*, *:before, *:after { box-sizing: inherit; }
body, h1, h2, h3, p, ul { margin: 0; padding: 0; }
```

## Uppgifter

### Nivå 1: uppvärmning (mycket enkelt)

**Uppgift 1: ändra färger**
Byt ut färgerna på de tre boxarna till valfria färger. Använd t.ex. `#9b59b6` (lila), `#f39c12` (orange) eller `#1abc9c` (turkos).

**Uppgift 2: ändra texten**
Byt rubrikerna och texten i varje box till egna texter.

### Nivå 2: fler boxar (enkelt)

**Uppgift 3: lägg till en fjärde box**
Skapa en ny `<div class="box gul">` med en ny färgklass `.gul` i CSS.

**Uppgift 4: ändra storlek**
Skapa två nya klasser: `.stor` (med `width: 500px`) och `.liten` (med `width: 200px`). Ge någon box klassen `.stor` och en annan `.liten`.

### Nivå 3: styla mer (medel)

**Uppgift 5: skuggor**
Lägg till `box-shadow` på `.box`-klassen:

```css
.box {
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}
```

**Uppgift 6: centrerade boxar**
Centrera alla boxar horisontellt med `margin: 0 auto 15px auto` på `.box`.

### Nivå 4: kombinera med bilder (avancerat)

**Uppgift 7: bild i en box**
Lägg till en bild inuti en av boxarna. Ge bilden `width: 100%` så den fyller boxen. Lägg till `border-radius` på bilden.

(Repetition: `<img>`, `border-radius` från kapitel 1–2!)

**Uppgift 8: lista i en box**
Lägg till en `<ul>` med minst tre `<li>` inuti en box. Styla listan med `padding-left: 20px` och `color: white`.

(Repetition: `<ul>`, `<li>` från kapitel 1!)

### Nivå 5: boss-nivån

**Uppgift 9: sex boxar**
Skapa totalt sex boxar med olika färger. Varje box ska ha en rubrik, text och minst ett extra element (bild, lista eller länk).

**Uppgift 10: dashboard**
Organisera dina boxar som ett "dashboard" (instrumentpanel):

1. Ge alla boxar samma bredd och centrera dem.
2. Varje box har ett unikt tema (t.ex. "Väder", "Nyheter", "Sport").
3. Minst en box har en bild, en har en lista, och en har en länk.
4. Ge sidan en snygg bakgrundsfärg och ett Google Font.
5. Alla boxar ska ha `box-shadow` och `border-radius`.
