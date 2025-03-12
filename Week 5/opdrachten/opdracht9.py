import sys

def twee_woorden_uit_bestand(bestand):
    try:
        bestand = open(bestand, "r")
        lines = bestand.readlines()
        bestand.close()
    except FileNotFoundError:
        print(f"Het bestand '{bestand}' is niet gevonden.")
        quit()
    woorden = []
    for i in lines:
        for j in i.split():
            woorden.append(j)
    return woorden

def wachtwoord_genereren(woorden):
    import random
    wachtwoord = ""
    for i in range(2):
        wachtwoord += random.choice(woorden)
    if len(wachtwoord)<12 or len(wachtwoord)>15:
        wachtwoord = wachtwoord_verlengen(wachtwoord)
        return wachtwoord
    return wachtwoord

def wachtwoord_verlengen(wachtwoord):
    import random
    while len(wachtwoord) < 12:
        wachtwoord += str(random.randint(0, 9))
    return wachtwoord[:15]

def main():
    if len(sys.argv) != 2:
        print("Gebruik: python opdracht9.py <bestand>")
        quit()
    woorden = twee_woorden_uit_bestand(sys.argv[1])
    wachtwoord = wachtwoord_genereren(woorden)
    print(wachtwoord)

if __name__ == "__main__":
    main()
