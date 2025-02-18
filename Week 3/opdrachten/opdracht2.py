def taxi_tarieven_A(afstand, nacht):
    PRIJS_PER_KM = 2.5
    STARTTARIEF = 2.5
    totaal = 0
    if nacht:
        totaal += 2.5
    totaal += STARTTARIEF
    totaal += PRIJS_PER_KM * afstand
    return totaal

def taxi_tarieven_B(afstand, nacht):
    PRIJS_PER_KM = 2.5
    STARTTARIEF = 7.5
    totaal = 0
    if nacht:
        totaal += 2.5
    totaal += STARTTARIEF
    totaal += PRIJS_PER_KM * afstand
    return totaal
def taxi_tarieven_C(afstand, nacht):
    PRIJS_PER_KM = 2.5
    STARTTARIEF = 85
    totaal = 0
    if nacht:
        totaal += 2.5
    totaal += STARTTARIEF
    if afstand > 50:
        totaal += (afstand - 50) * PRIJS_PER_KM
    return totaal

def main():
    afstand = int(input("Geef de afstand in kilometers: "))
    nacht = input("Is het nacht? (ja/nee): ").lower() == "ja"
    print(f"De prijs voor taxi A is {taxi_tarieven_A(afstand, nacht)}")
    print(f"De prijs voor taxi B is {taxi_tarieven_B(afstand, nacht)}")
    print(f"De prijs voor taxi C is {taxi_tarieven_C(afstand, nacht)}")

if __name__ == "__main__":
    main()
