# Dagbok - Projekt: Min responsiva tidning

Fokus för den här lektionen är responsiv design – att sidan automatiskt anpassar sig för mobiler, surfplattor och datorer.

### Nya begrepp och verktyg
- **Media Queries:** CSS-regler som bara körs vid vissa skärmstorlekar (`@media`).
- **Grid Template Areas:** Att döpa delar av sitt rutnät (t.ex. "header", "main") för att enkelt flytta runt dem.
- **Semantiska element:** Att använda `<header>`, `<main>`, `<aside>` och `<footer>` för bättre struktur.

### Kodexempel: Media Query
```css
@media (max-width: 768px) {
    .wrapper {
        grid-template-columns: 1fr;
        grid-template-areas: "innehall" "sidebar";
    }
}
```