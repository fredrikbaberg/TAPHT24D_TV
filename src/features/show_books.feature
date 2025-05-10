Feature: Lista katalog med böcker
	Som en användare av Läslistan
	Vill jag kunna se en lista över böcker i katalogen
	För att se tips på böcker att läsa

	Background:
		Given att jag är på hemsidan
		And jag är på sidan Katalog

	Scenario: Lista med böcker är inte tom
		When jag är på sidan Katalog
		Then bör jag se minst 7 sökresultat

	Scenario Outline: Listan med böcker innehåller givna titlar
		When är på sidan Katalog
		Then bör boken <titel> med <forfattare> synas i katalogen
    
		Examples:
			| titel        | forfattare |
			| Hur man tappar bort sin TV-fjärr 10 gånger om dagen | Bertil Flimmer |
			| Kaffekokaren som visste för mycket | Saga Espresson |
			| Min katt är min chef | Kattis Jamsson |
			| 100 sätt att undvika måndagar | Göran Snooze |
			| Gräv där du står – och hitta en pizzameny | Maja Skruv |
			| Jag trodde det var tisdag | Kim Vilsen |
			| Att prata med växter – och vad de egentligen tycker om dig | Flora Tistel |
