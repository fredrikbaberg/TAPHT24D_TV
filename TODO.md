# Detta ska du göra
1. Skapa ett projekt med Python, pytest, Playwright och behave. Gör ett motsvarande, publikt repo på GitHub. (Det är tillåtet att använda fler moduler.)
2. Skapa filerna README.md och STORIES.md i projektets rotmapp. (Du får använda STORIES.txt om du hellre vill det.)
3. Formulera user stories för den funktionalitet som finns på webbsidan idag. Skriv ner dessa i STORIES.md.
4. Ta fram feature-filer utifrån dina user stories.
5. Bygg step-filer för alla features. Page-filer vid behov.
6. Skriv ner 1) vad du har testat, och 2) hur man startar projektet, i README.md. Nu kan du lämna in!


## För G krävs
1. Det finns user stories som täcker all funktionalitet.
2. Alla user stories har minst en feature. Alla features har minst ett scenario.
3. Det går att starta ditt projekt, efter instruktionerna du har skrivit i README.md.
4. Alla test är gröna.
## För VG krävs
5. Högre kvalitet och kod som återanvänds.
6. Du använder designmönstret Page Object.
7. Du använder Scenario Outline.
8. Dina features försöker täcka alla meningsfulla möjligheter för motsvarande user story.

Exempel på meningsfulla möjligheter: testa inte bara att det går att favoritmarkera, utan att det går att ta bort en favoritmarkering, och vad som händer om man klickar fler än två gånger.

## Tips
* Flera element på sidan har ett testid som du kan använda med Playwright.
* Använd headless när du kommit en bit och när du lämnar in uppgiften. Det snabbar upp testandet rejält.
* Kom ihåg att testa att alla vyer gör det de ska, och att navigeringen fungerar.
