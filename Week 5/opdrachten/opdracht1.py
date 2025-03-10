def main():
    import sys
    aantalRegels = 0
    maxAantalRegels = int(sys.argv[2])
    bestandsNaam = sys.argv[1]
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
