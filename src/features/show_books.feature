Feature: Lista katalog med böcker
  Som en användare av Läslistan
  Vill jag kunna se en lista över böcker i katalogen
  För att se tips på böcker

  Background:
    Given att jag är på hemsidan

  Scenario: Lista med böcker är inte tom
    When jag är på sidan Katalog
    Then bör jag se minst 7 sökresultat

  Scenario: Lista med böcker innehåller bok om katt
    When jag är på sidan Katalog
    Then bör jag se minst en bok
    AND en titel är "Min katt är min chef"