def vraagBestandsNaam():
    bestandsNaam = input("Geef de bestandsnaam: ")
    return bestandsNaam

def main():
    aantalRegels = 0
    maxAantalRegels = 10
    bestandsNaam = vraagBestandsNaam()
    try:
        bestand = open(bestandsNaam, "r")
        for regel in bestand:
            if aantalRegels == maxAantalRegels:
                break
            else:
                print(regel, end="")
                aantalRegels += 1
    except FileNotFoundError:
        print(f"Het bestand '{bestandsNaam}' is niet gevonden.")
        quit()

if __name__ == "__main__":
    main()
