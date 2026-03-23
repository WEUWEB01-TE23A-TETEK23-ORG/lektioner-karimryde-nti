# Modulplan: flersidig webbplats med navigation

Kapitlet sammanfogar allt från kapitel 1–3 i ett projekt: en komplett flersidig webbplats med gemensam navigation, hover-effekter och aktiv sida-markering.

## Mål

- Bygga en flersidig webbplats (5+ sidor) med gemensam navigeringsmeny.
- Markera aktiv sida med klassen `.aktiv`.
- Skapa hover-effekter på navigeringslänkar med `:hover`.
- Använda `display: inline-block` för menystruktur.
- Tillämpa CSS-variabler med semantiska färgnamn från Coolors.co.

## Förkunskaper

- Kapitel 1: HTML-grundstruktur, rubriker, stycken, bilder, länkar.
- Kapitel 2: marginaler, bildhantering med `<figure>`.
- Kapitel 3: `<div>`, CSS-klasser, `.kontainer`, CSS-reset, flersidig navigation.

## Nya begrepp

### HTML
Navigation med `<div class="meny">`, manuell `.aktiv`-klass per sida

### CSS
`display: inline-block`, `:hover`-pseudoklass, CSS-variabler med Coolors.co-namn (`--charcoal`, `--persian-green`, `--saffron`, `--sandy-brown`, `--burnt-sienna`), `figure`-styling med `border` och `padding`

## Pedagogiska grundregler

- Hela kapitlet kretsar kring ett enda tematiskt projekt — inte flera isolerade övningar.
- `.aktiv`-klassen flyttas manuellt till rätt länk på varje sida — detta tvingar eleverna att förstå HTML-strukturen.
- Repetitionslektionen (rep-webbplats) fungerar som provförberedelse.

## Lektioner

### Lektion 1: flersidig webbplats (mappen: webbplats)
- **Innehåll:** 5 HTML-sidor (`sida1.html`–`sida5.html`) med gemensam `.meny`, `.aktiv`-klass, hover-effekter, `<figure>`/`<figcaption>`, CSS-variabler.
- **Mål:** kunna bygga en komplett webbplats med konsekvent navigation och styling.
- **Repetition:** `.kontainer`, CSS-reset, `<a>`, `<img>`, bakgrundsfärger, klasser.

### Lektion 2: repetition inför prov (mappen: rep-webbplats)
- **Innehåll:** eleverna bygger en flersidig webbplats självständigt som repetition.
- **Mål:** befästa alla koncept från kapitel 1–4 utan lärarstöd.
- **Repetition:** samtliga koncept från kapitel 1–4.

## Vanliga misstag

- Glömmer att flytta `class="aktiv"` till rätt `<a>`-tagg på varje sida (alla sidor pekar på samma länk).
- Hover-effekten och `.aktiv`-stilen matchar inte — ser inkonsekvent ut.
- Kopierar menyn till alla sidor men glömmer uppdatera länkarna.
- Sätter `<a>`-taggar i menyn som `display: block` istället för `inline-block`.
- Skriver `:active` (CSS-pseudoklass) istället för `.aktiv` (egen klass).

## Resurser

- [Coolors.co](https://coolors.co/) — färgpaletter.
- [Google Fonts](https://fonts.google.com/) — typsnitt.
