def main():
    from opdracht1 import vraagBestandsNaam
    AantalRegels = 10
    bestandsNaam = vraagBestandsNaam()
    regels = []
    try:
        bestand = open(bestandsNaam, "r")
        for regel in (bestand.readlines()[-AantalRegels:]):
            print(regel, end="")

    except FileNotFoundError:
        print(f"Het bestand '{bestandsNaam}' is niet gevonden.")
        quit()

if __name__ == "__main__":
    main()
