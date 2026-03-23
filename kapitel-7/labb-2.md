# Labb 2 – responsiv layout

Nu lär du dig göra en sida som **anpassar sig** till olika skärmstorlekar! Med `@media`-queries kan din sida se bra ut på både dator, surfplatta och mobil.

## Introduktion och mål

I den här labben tränar du på att:

* Använda `@media (max-width: ...)` för att ändra layout vid olika skärmbredder.
* Anpassa `grid-template-columns` och `grid-template-areas` per breakpoint.
* Arbeta med tre breakpoints: 1200px, 768px och 576px.
* Repetition: `grid-template-areas`, namngivna areas, `<header>`, `<main>`, `<aside>`, `<footer>`.

## Startkod

Skapa `index.html` och `style.css`.

**index.html:**

```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Responsiv sida</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="kontainer">
        <header>
            <h1>Nyheter</h1>
            <nav>
                <a href="#" class="aktiv">Start</a>
                <a href="#">Sport</a>
                <a href="#">Kultur</a>
                <a href="#">Teknik</a>
            </nav>
        </header>

        <main>
            <article>
                <h2>Senaste nytt</h2>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vel magna in velit dignissim fermentum. Integer varius felis nec ante iaculis, at volutpat nulla convallis.</p>
                <p>Duis eget ex vitae lectus pulvinar dictum non sit amet justo. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae.</p>
            </article>

            <article>
                <h2>Teknik i framkant</h2>
                <p>Nya innovationer presenterades vid årets teknikmässa. Bland nyheterna finns smarta glasögon och ultrasnabb laddning för elbilar.</p>
            </article>
        </main>

        <aside>
            <h3>Populärt</h3>
            <ul>
                <li>Artikel 1</li>
                <li>Artikel 2</li>
                <li>Artikel 3</li>
                <li>Artikel 4</li>
            </ul>
        </aside>

        <footer>
            <p>&copy; 2026 Nyhetssidan</p>
        </footer>
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
    --accent: #1a73e8;
    --sidhuvud-bg: #1a73e8;
    --sidebar-bg: #e8f0fe;
    --sidfot-bg: #202124;
}

body {
    font-family: 'Segoe UI', sans-serif;
    background-color: #f1f3f4;
}

/* === DESKTOP (default) === */
.kontainer {
    width: 1100px;
    margin: auto;

    display: grid;
    grid-template-columns: 3fr 1fr;
    grid-template-areas:
        "sidhuvud sidhuvud"
        "innehåll sidebar"
        "sidfot   sidfot";
    gap: 0;
}

header {
    grid-area: sidhuvud;
    background-color: var(--sidhuvud-bg);
    color: white;
    padding: 15px 25px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

header nav a {
    color: rgba(255,255,255,0.8);
    text-decoration: none;
    padding: 8px 15px;
    border-radius: 5px;
    transition: 0.2s;
}

header nav a:hover,
header nav .aktiv {
    background-color: rgba(255,255,255,0.2);
    color: white;
}

main {
    grid-area: innehåll;
    background-color: white;
    padding: 30px;
}

main h2 {
    color: var(--accent);
    margin-bottom: 10px;
}

main p {
    margin-bottom: 12px;
    line-height: 1.6;
}

article {
    margin-bottom: 25px;
}

aside {
    grid-area: sidebar;
    background-color: var(--sidebar-bg);
    padding: 25px;
}

aside h3 {
    color: var(--accent);
    margin-bottom: 10px;
}

aside ul {
    list-style: none;
}

aside li {
    padding: 10px 0;
    border-bottom: 1px solid rgba(0,0,0,0.1);
}

footer {
    grid-area: sidfot;
    background-color: var(--sidfot-bg);
    color: white;
    text-align: center;
    padding: 15px;
}

/* === SURFPLATTA (max-width: 1200px) === */
@media (max-width: 1200px) {
    .kontainer {
        width: 100%;
    }
}

/* === LITEN SURFPLATTA (max-width: 768px) === */
@media (max-width: 768px) {
    .kontainer {
        grid-template-columns: 1fr;
        grid-template-areas:
            "sidhuvud"
            "innehåll"
            "sidebar"
            "sidfot";
    }
}

/* === MOBIL (max-width: 576px) === */
@media (max-width: 576px) {
    header {
        flex-direction: column;
        text-align: center;
    }

    header nav {
        margin-top: 10px;
    }

    header nav a {
        display: block;
        margin-bottom: 5px;
    }
}
```

## Övningar och kodexempel

### Övning 1: media queries

En media query aktiveras vid en viss skärmbredd:

```css
/* Gäller när skärmen är 768px eller smalare */
@media (max-width: 768px) {
    .kontainer {
        grid-template-columns: 1fr;  /* En kolumn istället för två */
    }
}
```

### Övning 2: testa responsivitet

Öppna sidan i webbläsaren och **ändra fönsterbredden** genom att dra i kanten. Se hur layouten ändras vid 1200px, 768px och 576px.

Du kan också använda webbläsarens **utvecklarverktyg** (F12) och klicka på mobil-ikonen.

## Uppgifter

### Nivå 1: uppvärmning (mycket enkelt)

**Uppgift 1: testa breakpoints**
Öppna sidan och testa alla tre breakpoints genom att ändra fönsterbredden. Beskriv (för dig själv) vad som händer vid varje breakpoint.

**Uppgift 2: eget innehåll**
Byt ut all text till eget innehåll — ändra rubriker, artiklar och sidebarlänkar.

### Nivå 2: ändra breakpoints (enkelt)

**Uppgift 3: ny breakpoint**
Lägg till en breakpoint vid `max-width: 480px` som gör texten mindre:

```css
@media (max-width: 480px) {
    body {
        font-size: 14px;
    }

    main {
        padding: 15px;
    }
}
```

**Uppgift 4: ändra färg vid mobil**
I mobil-breakpointen (576px), ändra sidhuvudets färg till en mörkare variant. Det gör det tydligt att media queryn fungerar.

### Nivå 3: mer innehåll (medel)

**Uppgift 5: bild i artikeln**
Lägg till en `<figure>` med bild i en av artiklarna. Ge bilden `width: 100%` så den skalas med.

(Repetition: `<figure>` + responsiva bilder!)

**Uppgift 6: sidebar-länkar**
Gör sidebar-listan till riktiga `<a>`-taggar. Styla utan understrykning med hover-effekt.

### Nivå 4: förbättra responsiviteten (avancerat)

**Uppgift 7: sidebar ovanför main på mobil**
Ändra `grid-template-areas` i 768px-breakpointen så att sidebar hamnar *ovanför* main:

```css
grid-template-areas:
    "sidhuvud"
    "sidebar"
    "innehåll"
    "sidfot";
```

**Uppgift 8: göm sidebar på mobil**
I 576px-breakpointen, göm sidebar helt med `display: none`.

### Nivå 5: boss-nivån

**Uppgift 9: tre artiklar**
Lägg till en tredje artikel. På desktop, visa artiklarna i ett grid med `grid-template-columns: 1fr 1fr`. På mobil ska de visas under varandra.

**Uppgift 10: komplett nyhetsida**
Bygg en komplett responsiv nyhetsida:

1. `<header>` med navigation som blir vertikal på mobil.
2. `<main>` med minst tre artiklar med bilder.
3. `<aside>` med populära artiklar.
4. `<footer>` med kontaktinfo.
5. Tre breakpoints som ändrar layout.
6. CSS-variabler och Google Font.
7. Sidan ska se bra ut på alla storlekar!
