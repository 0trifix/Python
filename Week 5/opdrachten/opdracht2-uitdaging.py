def main():
    import sys
    AantalRegels = int(sys.argv[2])
    bestandsNaam = sys.argv[1] 
    try:
        bestand = open(bestandsNaam, "r")
        for regel in (bestand.readlines()[-AantalRegels:]):
            print(regel, end="")

    except FileNotFoundError:
        print(f"Het bestand '{bestandsNaam}' is niet gevonden.")
        quit()

if __name__ == "__main__":
    main()
