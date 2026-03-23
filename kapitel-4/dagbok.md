# Dagbok: Kapitel 4 – Webbplats, Länkar och Sidor

## Lektion 1: webbplats (2025-11-06)

**Ämne:** Fem favoritband på en gemensam webbplats

**Nya begrepp:**
- Knavigering (`<div class="meny">`) – En delad, horisontell meny för flera sidor
- `.aktiv` – Ett UI-mönster för att via CSS visa vilken sida besökaren är på för stunden
- `:hover` – En pseudo-klass som aktiveras när muspekaren hålls över ett element
- `display: inline-block` – Gjorde att länkarna låg bredvid varandra istället för staplade nedåt

**Vad vi gjorde:**
Vi knöt ihop allt från föregående kapitel och skapade vår första sammanhängande webbplats bestående av 5 sidor, var och en tillägnad en musikgrupp. Samma globala navigationsmeny fanns överst i alla filer, och genom att flytta klassen `.aktiv` i HTML-koden på respektive sida, såg det ut som att menyn var dynamisk.

**Nyckelexempel:**
```html
<!-- Exempel från sida2.html -->
<div class="meny">
    <a href="sida1.html">Startsida</a>
    <a href="sida2.html" class="aktiv">AC/DC</a>
    <a href="sida3.html">Metallica</a>
</div>
```
```css
.meny a {
    display: inline-block;
    padding: 10px 20px;
    text-decoration: none;
    color: white;
}
.meny a.aktiv, .meny a:hover {
    background-color: var(--highlight-färg);
}
```

---

## Lektion 2: rep-webbplats (2025-11-20)

**Ämne:** Repetition inför prov (Fem filmer)

**Nya begrepp:**
- Ingen direkt ny tagg introducerades, fokuset låg helt på repetition, färdighet och snabbhet.

**Vad vi gjorde:**
Detta var ett genrep inför ett praktiskt prov. Vi använde samma mångsidiga navigationsmönster (`.aktiv`), färgvariabler och centrala `.kontainer` layout som vi lärts oss tidigare, men med ämnet "5 biofilmer" istället.

**Nyckelexempel:**
```css
/* Träning i att tillämpa befintlig kunskap snabbt på tomma CSS-selektorer */
:root {
   --huvud: #0f172a;
   --text: #f8fafc;
}
.kontainer {
   margin: auto;
   width: 800px;
}
```
