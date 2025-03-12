# Deze code is niet volledig zoals er gevraagd werd in de opgave
def vraag_bestand():
    bestand = input("Welk bestand wilt u openen? ")
    return bestand

def lees_bestand(bestand):
    try:
        lines = []
        with open(bestand) as f:
            for line in f.readlines():
                lines.append(line)
        return lines
    except FileNotFoundError:
        print("Bestand niet gevonden")
        quit()

def regelnummers(lines):
    grootste_getal = len(str(len(lines)))
    lines = [f"{i+1:>{grootste_getal}}: {line}" for i, line in enumerate(lines)]
    return lines

def bestand_schrijven(lines):
    bestand = input("Welk naam wilt u voor het nieuwe bestand? ")
    try:
        with open(bestand, "w") as f:
            for line in lines:
                f.write(line)
    except FileNotFoundError:
        print("Bestand niet gevonden")
        quit()

def main():
    bestand = vraag_bestand()
    lines = lees_bestand(bestand)
    bestand = vraag_bestand
    bestand_schrijven(regelnummers(lines))

if __name__ == "__main__":
    main()
