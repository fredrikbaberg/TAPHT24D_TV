Feature: Lägg till bok
  Som en användare av Läslistan
  Vill jag kunna lägga till en bok
  För att andra ska se mina förslag

  Background:
    Given att jag är på hemsidan

  Scenario Outline: Lägga till böcker
    When jag lägger till en bok med "<titel>" och "<forfattare>"
    Then bör boken synas i katalogen
    
    Examples:
      | titel        | forfattare |
      | Imorgon när kriget kom   | John Marsden             |
      | Michael Jackson | 8            |
      | Avicii        | 5              |
      | Håkan Hellström | 7            |
