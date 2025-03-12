from opdracht4 import lees_bestand
import sys

def verwijder_commentaar(lines):
    return [line for line in lines if not line.startswith("#")]

def bestand_schrijven(bestand, lines):
    try:
        with open(bestand, "w") as f:
            for line in lines:
                f.write(line)
    except FileNotFoundError:
        print("Bestand niet gevonden")
        quit()

def main():
    bestand = sys.argv[1]
    lines = lees_bestand(bestand)
    bestand_schrijven(sys.argv[2], verwijder_commentaar(lines))

if __name__ == "__main__":
    main()
