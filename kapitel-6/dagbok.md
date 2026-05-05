# Dagbok - Projekt: Mitt rutnät

I det här projektet använder vi CSS Grid för att skapa komplexa layouter som ser professionella ut, med fokus på kort-design.

### Nya begrepp och verktyg
- **CSS Grid:** Ett kraftfullt tvådimensionellt system för att placera element i rader och kolumner.
- **Transitions:** Animationer som gör att t.ex. en förstoring (`scale`) sker mjukt.
- **Object-fit:** Hur bilder ska bete sig inuti en behållare med fasta mått.

### Kodexempel: Enkel Grid-layout
```css
.rutnat {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
}
```