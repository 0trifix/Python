class Drank:
    def __init__(self, naam, temperatuur=20):
        self.naam = naam
        self.temperatuur = temperatuur
    def __str__(self) -> str:
        return f"Naam: {self.naam} \nIdeale temperatuur:{self.temperatuur}°C"
    def log(self) -> None:
        log = LogFile("drank.log")
        log.schrijf(f"Naam: {self.naam} \nIdeale temperatuur:{self.temperatuur}°C")
        log.sluit()

class LogFile:
    def __init__(self, naam: str) -> None:
        self.bestandsnaam = naam
        self.bestand = open(naam, "a")
    def schrijf(self, tekst: str) -> None:
        self.bestand.write(tekst + "\n")
    def sluit(self) -> None:
        self.bestand.close()

def main():
    cola = Drank("Cola", 5)
    koffie = Drank("Koffie", 90)
    thee = Drank("Thee", 80)
    water = Drank("Water")

    print(cola)
    print(koffie)
    print(thee)
    print(water)

    cola.log()
    koffie.log()
    thee.log()
    water.log()

if __name__ == "__main__":
    main()
