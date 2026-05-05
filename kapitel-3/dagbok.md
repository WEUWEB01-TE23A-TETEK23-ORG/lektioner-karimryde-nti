# Dagbok - Projekt: Min blogg eller portfolio

Lektionen handlade om att strukturera flera inlägg på rad med hjälp av Flexbox och att hålla koden ren med CSS-variabler.

### Nya begrepp och verktyg
- **CSS-variabler:** Att spara färger i `:root` för att enkelt kunna ändra tema på hela sidan.
- **Flexbox:** Användning av `display: flex` och `gap` för att rada upp element snyggt.
- **CSS Reset:** Grundläggande inställningar som `box-sizing: border-box` för att undvika problem med marginaler.

### Kodexempel: Variabler och Flex
```css
:root {
    --primary-color: #264653;
}

.flex-rad {
    display: flex;
    gap: 20px;
}
```