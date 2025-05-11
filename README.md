# Instruktioner

Det här projektet används för att testa [exam-template](https://tap-ht24-testverktyg.github.io/exam-template/). Tester kommer köras med hjälp av Playwright och Behave

Fallen jag valt att fokusera på framgår av `STORIES.md`. Det är navigation mellan vyer, att böcker är synliga, att det går att lägga till böcker och att böcker kan favoritmarkeras vilket inkluderar att de syns under Mina böcker.

Jag hade önskat lägga till ett test att samma bok inte får läggas till flera gånger, men avstod från det. Dels eftersom sidan tillåter det, dels eftersom alla test ska vara gröna.

## Instruktioner
För att köra testerna behöver du:
1. Installera nödvändiga paket.
    Använder du Visual Studio Code och har Docker installerat finns en Dev Container du kan använda. Annars behöver du: python, beroenden i `requirements.txt` samt köra `playwright install`.
2. Anropa behave från rotkatalogen:
    > behave src/

Som en bonus finns en GitHub Action som kör behave, den triggas däremot endast vid push.
