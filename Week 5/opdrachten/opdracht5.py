from opdracht4 import lees_bestand
import sys

def main():
    bestand = sys.argv[1]
    lines = lees_bestand(bestand)
    langste_woord = ""
    for i in lines:
        for j in i.split():
            if len(j) > len(langste_woord):
                langste_woord = j
    print(f"Het langste woord in het bestand is: {langste_woord}")

if __name__ == "__main__":
    main()
