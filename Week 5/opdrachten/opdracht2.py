def main():
    import sys
    AantalRegels = int(sys.argv[2])
    bestandsNaam = sys.argv[1] 
    regels = []
    try:
        bestand = open(bestandsNaam, "r")
        for regel in bestand:
            regels.append(regel) 
        
        for i in range(AantalRegels):
            print(regels[-AantalRegels + i], end="")

        # for i in range(len(regels)):
        #     if not i < len(regels) - AantalRegels:
        #         print(regels[i], end="")

    except FileNotFoundError:
        print(f"Het bestand '{bestandsNaam}' is niet gevonden.")
        quit()

if __name__ == "__main__":
    main()
