def main():
    from opdracht1 import vraagBestandsNaam
    aantalRegels = 1
    maxAantalRegels = 10
    bestandsNaam = vraagBestandsNaam()
    regels = []
    try:
        bestand = open(bestandsNaam, "r")
        for regel in bestand:
            if aantalRegels == maxAantalRegels:
                break
            else:
                regels.append(regel) 
                aantalRegels += 1
        
        print(regels)

        for i in range(len(regels)):
            print(regels[len(regels)-maxAantalRegels+i], end="")
    except FileNotFoundError:
        print(f"Het bestand '{bestandsNaam}' is niet gevonden.")
        quit()

if __name__ == "__main__":
    main()
