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
    for i, line in enumerate(lines):
        print(f"{i+1:>{grootste_getal}}. {line}", end="")
    return

def main():
    bestand = vraag_bestand()
    lines = lees_bestand(bestand)
    regelnummers(lines)

if __name__ == "__main__":
    main()
