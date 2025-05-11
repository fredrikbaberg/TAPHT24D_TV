Feature: Favoriter
    Som en användare av Läslistan
    Vill jag kunna favoritmarkera böcker
    För att kunna se mina favoriter

  Background:
    Given att jag är på hemsidan

  @Favorite
  Scenario: Listan är tom från början
    Given jag är på sidan "Mina böcker"
    Then finns "0" favoritmarkerade böcker

  @Favorite
  Scenario: Favoritmarkera bok
    Given jag är på sidan "Katalog"
    When jag trycker på "Kaffekokaren som visste för mycket" "1" gång(er)
    Then bör den vara favoritmarkerad

# @Favorite
# Scenario: Av-Favoritmarkera bok
# 	When jag trycker på "Kaffekokaren som visste för mycket" "2" gång(er)
# 	Then bör den inte vara favoritmarkerad

# @Favorite
# Scenario: Favoritmarkera tre gånger
# 	When jag trycker på "Kaffekokaren som visste för mycket" "3" gång(er)
# 	Then bör den vara favoritmarkerad
