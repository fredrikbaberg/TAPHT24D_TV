Feature: Favoriter
    Som en användare av Läslistan
    Vill jag kunna favoritmarkera böcker
    För att visa att dom är viktiga för mig

  Background:
    Given att jag är på hemsidan

  @Favorite
  Scenario: Listan är tom från början
    Given jag är på sidan "Mina böcker"
    Then finns "0" favoritmarkerade böcker

  @Favorite
  Scenario Outline: Udda antal tryck favoritmarkerar böcker
    Given jag är på sidan "Katalog"
    When jag trycker <antal> gånger på favoritmarkera "Kaffekokaren som visste för mycket"
    Then bör "Kaffekokaren som visste för mycket" vara favoritmarkerad

    Examples:
      | antal |
      | 1     |
      | 3     |
      | 5     |

  @Favorite
  Scenario Outline: Jämnt antal tryck av-favoritmarkerar böcker
    Given jag är på sidan "Katalog"
    When jag trycker <antal> gånger på favoritmarkera "Kaffekokaren som visste för mycket"
    Then bör inte "Kaffekokaren som visste för mycket" vara favoritmarkerad

    Examples:
      | antal |
      | 0     |
      | 2     |
      | 4     |

  @Favorite
  Scenario: Favoritmarkerade böcker finns under Mina böcker
    Given jag är på sidan "Katalog"
    When jag trycker "1" gånger på favoritmarkera "Kaffekokaren som visste för mycket"
    And jag trycker "1" gånger på favoritmarkera "100 sätt att undvika måndagar"
    And jag går till sidan "Mina böcker"
    Then finns "2" favoritmarkerade böcker

  @Favorite
  Scenario: Av-favoritmarkerade böcker försvinner från Mina böcker
    Given jag är på sidan "Katalog"
    When jag trycker "2" gånger på favoritmarkera "Kaffekokaren som visste för mycket"
    And jag går till sidan "Mina böcker"
    Then finns "0" favoritmarkerade böcker
