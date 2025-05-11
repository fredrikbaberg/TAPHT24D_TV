Feature: Bläddra mellan flikar
    Som en användare av Läslistan
    Vill jag kunna navigera mellan flikar
    För att få en enklare översikt.

	Background:
		Given att jag är på hemsidan

    @Navigate
    Scenario: Kan navigera till en sida jag inte redan är på
        When jag är på sidan "Katalog"
        Then kan jag navigera till "Lägg till bok"

    @Navigate
    Scenario: Kan inte navigera till en sida jag redan är på
        When jag är på sidan "Katalog"
        Then kan jag inte navigera till "Katalog"
