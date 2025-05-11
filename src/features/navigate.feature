Feature: Bläddra mellan vyer
    Som en användare av Läslistan
    Vill jag kunna navigera mellan vyer
    För att bara se relevant information

    Background:
        Given att jag är på hemsidan

    @Navigate
    Scenario Outline: Kan navigera till en sida jag inte redan är på
        Given jag är på sidan "<nuvarande_sida>"
        Then kan jag navigera till "<nasta_sida>"

        Examples:
            | nuvarande_sida | nasta_sida    |
            | Katalog        | Lägg till bok |
            | Katalog        | Mina böcker   |
            | Lägg till bok  | Katalog       |
            | Lägg till bok  | Mina böcker   |
            | Mina böcker    | Katalog       |
            | Mina böcker    | Lägg till bok |

    @Navigate
    Scenario Outline: Kan inte navigera till en sida jag redan är på
        Given jag är på sidan "<nuvarande_sida>"
        Then kan jag inte navigera till "<nuvarande_sida>"

        Examples:
            | nuvarande_sida |
            | Katalog        |
            | Lägg till bok  |
            | Mina böcker    |
