Feature: Lista katalog med böcker
	Som en användare av Läslistan
	Vill jag kunna se en lista över böcker i katalogen
	För att få tips på böcker att läsa

	Background:
		Given att jag är på hemsidan
		And jag är på sidan Katalog

	@Catalog
	Scenario: Lista med böcker är inte tom
		Then bör jag se minst "7" sökresultat

	@Catalog
	Scenario Outline: Listan med böcker innehåller givna titlar
		Then bör boken "<title>" av "<author>" synas i katalogen
    
		Examples:
			| title        | author |
			| Hur man tappar bort sin TV-fjärr 10 gånger om dagen | Bertil Flimmer |
			| Kaffekokaren som visste för mycket | Saga Espresson |
			| Min katt är min chef | Kattis Jamsson |
			| 100 sätt att undvika måndagar | Göran Snooze |
			| Gräv där du står – och hitta en pizzameny | Maja Skruv |
			| Jag trodde det var tisdag | Kim Vilsen |
			| Att prata med växter – och vad de egentligen tycker om dig | Flora Tistel |
