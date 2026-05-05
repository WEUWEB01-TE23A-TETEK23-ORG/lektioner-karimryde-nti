# Dagbok - Projekt: Min webbplats (3 sidor)

Vi har nu tagit steget till att bygga riktiga webbplatser med flera sammanlänkade HTML-filer och en gemensam navigeringsmeny.

### Nya begrepp och verktyg
- **Navigationsmeny:** En konsekvent meny på alla sidor.
- **Aktiv länk:** Att använda en CSS-klass (t.ex. `.aktiv`) för att visa användaren vilken sida de befinner sig på för tillfället.
- **Hover-effekter:** Att ändra utseende på länkar när muspekaren hålls över dem.

### Kodexempel: Aktiv klass i menyn
```html
<div class="meny">
    <a href="index.html" class="aktiv">Hem</a>
    <a href="sida2.html">Om oss</a>
</div>
```