Feature: Lägg till bok
    Som en användare av Läslistan
    Vill jag kunna lägga till en bok
    För att andra ska se mina förslag

    Background:
        Given att jag är på hemsidan
        And jag är på sidan "Lägg till bok"

    @AddBook
    Scenario Outline: Kan inte lägga till bok om titel eller författare saknas
        When jag fyller i "<titel>" av "<forfattare>"
        Then går det inte att trycka på "Lägg till ny bok"

        Examples:
            | titel    | forfattare |
            |          |            |
            | boktitel |            |
            |          | författare |

    @AddBook
    Scenario Outline: Lägga till böcker
        When jag fyller i "<titel>" av "<forfattare>"
        And jag trycker på knappen "Lägg till bok"
        And jag går till sidan "Katalog"
        Then bör boken "<titel>" av "<forfattare>" synas i katalogen

        Examples:
            | titel                       | forfattare                                  |
            | Imorgon när kriget kom      | John Marsden                            |
            | Lär dig Python från grunden | Linus Rundberg Streuli, Antonio Prgomet |

    @AddBook
    Scenario: Kan använda tabb för att navigera mellan fält
        When jag trycker på fältet för "Titel"
        And jag trycker på tangenten "Tab"
        Then bör fältet för "Författare" vara markerat

    # @AddBook
    # Scenario: Kan inte lägga till samma bok två gånger
    #     When jag fyller i "A" av "B"
    #     And jag trycker på knappen "Lägg till bok"
    #     And jag fyller i "A" av "B"
    #     And jag trycker på knappen "Lägg till bok"
    #     Then får jag meddelande att boken redan finns
