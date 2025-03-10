def main():
    import sys
    for bestandsNaam in sys.argv[1:]:
        try:
            bestand = open(bestandsNaam, "r")
            print(bestand.read())
            bestand.close()
        except FileNotFoundError:
            print(f"Het bestand '{bestandsNaam}' is niet gevonden.")
            quit()

if __name__ == "__main__":
    main()
