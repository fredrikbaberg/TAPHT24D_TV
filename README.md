# Instruktioner

Projektet används för att testa [exam-template](https://tap-ht24-testverktyg.github.io/exam-template/). Projektet kommer köra tester med hjälp av Playwright och Behave. Fallen jag valt att fokusera på framgår av `STORIES.md`.

Jag hade önskat lägga till test att samma bok inte kan läggas till flera gånger, men eftersom sidan tillåter det har jag inte lagt till något sånt test. Annars hade jag skapat ett test som inte hade lyckats, vilket enligt uppgiften inte är godkänt.

Instruktioner för att köra följer nedan.

## Instruktioner
1. Installera nödvändiga paket. Använder du Visual Studio Code finns det en Dev Container du kan använda. Annars behöver du: python, beroenden i `requirements.txt` samt köra `playwright install`.

2. Kör behave från rotkatalogen:
    > behave src/
