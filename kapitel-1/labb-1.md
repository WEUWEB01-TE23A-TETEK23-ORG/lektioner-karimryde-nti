# Labb 1 – min första webbsida

Välkommen till din första labb! Här ska du bygga en riktig webbsida från grunden. Du kommer att skriva HTML-kod och se resultatet direkt i webbläsaren.

## Introduktion och mål

I den här labben tränar du på att:

* Skapa ett HTML-dokument med rätt grundstruktur.
* Använda rubriker (`<h1>`, `<h2>`) och stycken (`<p>`).
* Göra radbrytningar med `<br>`.
* Fetmarkera text med `<strong>` och kursivera med `<em>`.
* Koppla en CSS-fil och ändra färger och typsnitt.

## Startkod

Skapa två filer: `index.html` och `style.css`. Kopiera in koden nedan.

**index.html:**

```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Min första webbsida</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Hej världen!</h1>
    <p>Det här är min allra första webbsida.</p>
</body>
</html>
```

**style.css:**

```css
body {
    font-family: sans-serif;
    background-color: #f0f0f0;
    color: #333;
}
```

## Övningar och kodexempel

### Övning 1: lägga till en rubrik och ett stycke

En rubrik skrivs med `<h1>` (störst) eller `<h2>` (näst störst). Ett stycke skrivs med `<p>`:

```html
<h1>Min rubrik</h1>
<p>Det här är ett stycke text.</p>
```

### Övning 2: radbrytning

Om du vill ha en ny rad utan att starta ett nytt stycke, använd `<br>`:

```html
<p>Rad ett<br>Rad två<br>Rad tre</p>
```

### Övning 3: fetstil och kursiv

Markera viktiga ord med `<strong>` (fetstil) och `<em>` (kursiv):

```html
<p>Jag tycker om <strong>pizza</strong> och <em>glass</em>.</p>
```

## Uppgifter

### Nivå 1: uppvärmning (mycket enkelt)

**Uppgift 1: byt rubrik**
Ändra texten i `<h1>` till ditt eget namn. Spara och ladda om sidan i webbläsaren.

**Uppgift 2: lägg till ett stycke**
Lägg till ett `<p>`-stycke under rubriken där du skriver en mening om dig själv.

### Nivå 2: mer text (enkelt)

**Uppgift 3: underrubrik**
Lägg till en `<h2>`-rubrik som heter "Mina intressen". Under den, skriv ett `<p>`-stycke om vad du gillar.

**Uppgift 4: flera stycken**
Lägg till minst tre `<p>`-stycken under varandra. Varje stycke ska handla om olika saker (t.ex. din favoritsport, din favoritmat, din favoritfilm).

### Nivå 3: formatering (medel)

**Uppgift 5: fetstil och kursiv**
I ett av dina stycken, gör minst ett ord **fetstilt** med `<strong>` och ett ord *kursivt* med `<em>`.

**Uppgift 6: radbrytningar**
Skriv en kort dikt (eller hitta en) med `<br>` för att bryta raderna. Allt ska vara inuti en enda `<p>`-tagg.

### Nivå 4: CSS-styling (avancerat)

**Uppgift 7: ändra färger**
I `style.css`, ändra `background-color` till en valfri färg (t.ex. `lightblue`, `#ffe0b2`, `peachpuff`). Ändra `color` till en mörk färg som är lätt att läsa.

**Uppgift 8: ändra typsnitt och storlek**
Testa att byta `font-family` till `Georgia` eller `'Courier New'`. Lägg till `font-size: 18px` på `p`-taggen i CSS:

```css
p {
    font-size: 18px;
}
```

### Nivå 5: boss-nivån

**Uppgift 9: styla rubriken**
Ge `<h1>`-taggen en egen stil i CSS. Ändra `color`, `font-size` och testa `text-align: center` för att centrera den.

**Uppgift 10: hela presentationssidan**
Bygg ut sidan till en komplett presentation av dig själv med:

1. En stor rubrik med ditt namn (centrerad och i valfri färg).
2. Minst två `<h2>`-underrubriker (t.ex. "Om mig", "Mina intressen").
3. Minst fyra `<p>`-stycken med text.
4. Använd `<strong>` och `<em>` minst tre gånger.
5. Ge sidan en snygg bakgrundsfärg och ett typsnitt du gillar.
