Feature: Lägg till bok
  Som en användare av Läslistan
  Vill jag kunna lägga till en bok
  För att andra ska se mina förslag

#   Background:
#     Given att jag är på hemsidan
#     And jag är på sidan Lägg till bok

#   @AddBook
#   Scenario Outline: Kan inte lägga till bok om titel eller författare saknas
#     When jag lägger till boken "<title>" av "<author>"

#   # @AddBook
#   # Scenario: Kan använda tabb för att navigera mellan fält
#   #   When jag trycker på titel
#   #   And jag trycker på tabb
#   #   Then bör fältet författare vara valt

#   @AddBook
#   Scenario Outline: Lägga till böcker
#     When jag lägger till boken "<title>" av "<author>"
#     And jag går till sidan Katalog
#     Then bör boken "<title>" av "<author>" synas i katalogen
    
#     Examples:
#       | title        | author |
#       | Imorgon när kriget kom   | John Marsden             |
#       | Lär dig Python från grunden | Linus Rundberg Streuli, Antonio Prgomet            |

#   # Scenario: Kan inte lägga till samma bok två gånger

