## Att testa
Länk till sidan som ska testas: [exam-template](https://tap-ht24-testverktyg.github.io/exam-template/)

## Beskrivning
Projektet kommer köra tester med hjälp av Playwright och Behave. Det som testas beskrivs övergripande av User Stories, se STORIES.md.

## Instruktioner
1. Installera nödvändiga paket. Om du använder Visual Studio Code går det att öppna i Dev Container där allt är förberett, annars behövs: Python, beroenden i `requirements.txt` samt att köra `playwright install`.
2. Kör behave från rotkatalogen:
> behave src
