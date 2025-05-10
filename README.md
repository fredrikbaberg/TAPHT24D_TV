# Instruktioner

Projektet används för att testa [exam-template](https://tap-ht24-testverktyg.github.io/exam-template/). Projektet kommer köra tester med hjälp av Playwright och Behave. Fallen jag valt att fokusera på framgår av `STORIES.md`.

Instruktioner för att köra följer nedan.

## Instruktioner
1. Installera nödvändiga paket. Använder du Visual Studio Code finns det en Dev Container du kan använda. Annars behöver du: Python, beroenden i `requirements.txt` samt köra `playwright install`.

2. Kör behave från rotkatalogen:
    > behave src/
