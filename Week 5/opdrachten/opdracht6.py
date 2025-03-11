import sys
from opdracht4 import lees_bestand

def meest_voorkomend_woord(lines):
    woorden = {}
    for i in lines:
        for j in i.split():
            if j in woorden:
                woorden[j] += 1
            else:
                woorden[j] = 1
    meest_voorkomend = ""
    for i in woorden:
        if woorden[i] > woorden.get(meest_voorkomend, 0): # get() returns the value of the specified key. If the key does not exist, the default value is returned.
            meest_voorkomend = i
    return meest_voorkomend

def main():
    bestand = sys.argv[1]
    lines = lees_bestand(bestand)
    print(f"Het meest voorkomende woord in het bestand is: {meest_voorkomend_woord(lines)}")

if __name__ == "__main__":
    main()
