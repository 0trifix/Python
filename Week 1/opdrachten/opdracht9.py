dagen = int(input("Geef een aantal dagen: "))
uren = int(input("Geef een aantal uren: "))
minuten = int(input("Geef een aantal minuten: "))
seconden = int(input("Geef een aantal seconden: "))

totaal_seconden= seconden + (minuten*60) + (uren*60*60) + (dagen*24*60*60)

print(totaal_seconden)