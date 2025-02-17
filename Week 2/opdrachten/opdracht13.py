def toegangsprijs(leeftijd_lijst):
    prijslijst = []
    for leeftijd in leeftijd_lijst:
        if leeftijd < 3:
            prijs = 0
        elif leeftijd <= 12:
            prijs = 15
        elif leeftijd >= 65:
            prijs = 20
        else:
            prijs = 30
        prijslijst.append(prijs)

    return prijslijst


leeftijd_lijst = []
while True:
    leeftijd = input("Geef leeftijd: ")
    if leeftijd == "":
        break
    leeftijd = int(leeftijd)
    leeftijd_lijst.append(leeftijd)

print(toegangsprijs(leeftijd_lijst))
