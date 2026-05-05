# Dagbok - Projekt: Min reklamsida

Idag har vi fokuserat på visuell layout och hur man skapar en "Hero"-sektion (en stor välkomnande toppbild) som fångar besökarens intresse direkt.

### Nya begrepp och verktyg
- **Background Image:** Att sätta bilder som bakgrund i CSS istället för att använda `<img>`-taggen.
- **Hero-sektion:** En stor banner längst upp på en webbsida.
- **Semantic HTML:** Användning av `<figure>` och `<figcaption>` för att gruppera bilder med tillhörande text.

### Kodexempel: Bakgrundsbild i CSS
```css
.hero {
    background-image: url('bilder/strand.jpg');
    background-size: cover;
    background-position: center;
    height: 400px;
}
```