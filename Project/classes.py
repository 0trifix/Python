class apparaat:
    def __init__(self, naam, merk) -> None:
        self.naam = naam
        self.merk = merk
        self.type = type
        self.status = False
    def __str__(self) -> str:
        return f"{self.naam} ({self.merk}) - {self.type} - {'Aan' if self.status else 'Uit'}"

class Lamp(apparaat):
    def __init__(self, naam, merk) -> None:
        super().__init__(naam, merk)
        self.helderheid = 0
        self.type = "lamp"
    def __str__(self) -> str:
        return f"{super().__str__()} - Helderheid: {self.helderheid}"
    
class Thermostaat(apparaat):
    def __init__(self, naam, merk, temperatuur) -> None:
        super().__init__(naam, merk)
        self.temperatuur = temperatuur
        self.type = "thermostaat"

class Deurslot(apparaat):
    def __init__(self, naam, merk) -> None:
        super().__init__(naam, merk)
        self.geopend = False
        self.type = "deurslot"

class Bewegingssensor(apparaat):
    def __init__(self, naam, merk) -> None:
        super().__init__(naam, merk)
        self.type = "bewegingssensor"

class Rookmelder(apparaat):
    def __init__(self, naam, merk) -> None:
        super().__init__(naam, merk)
        self.rook_detectie = False
        self.type = "rookmelder"

class Gordijn(apparaat):
    def __init__(self, naam, merk) -> None:
        super().__init__(naam, merk)
        self.open = False
        self.type = "gordijn"

class Kamer:
    def __init__(self, naam) -> None:
        self.naam = naam
        self.apparaten = []
    def voeg_apparaat_toe(self, apparaat):
        self.apparaten.append(apparaat)
    def __str__(self) -> str:
        apparaten_str = "\n".join([" + " + str(apparaat) for apparaat in self.apparaten])
        return f"{self.naam}\n________\nApparaten:\n{apparaten_str}\n________\n"

class Woning:
    def __init__(self, naam) -> None:
        self.naam = naam
        self.kamers = []
    def voeg_kamer_toe(self, kamer):
        self.kamers.append(kamer)
    def __str__(self) -> str:
        kamers_str = "\n".join([str(kamer) for kamer in self.kamers])
        return f"Woning: {self.naam}\nKamers:\n{kamers_str}"

class Bewoner:
    def __init__(self, naam) -> None:
        self.naam = naam
        self.kamer = None

class SmartHub:
    def __init__(self, naam) -> None:
        self.naam = naam
        self.apparaten = []
    def voeg_apparaat_toe(self, apparaat):
        self.apparaten.append(apparaat)

class Logger:
    def __init__(self, naam) -> None:
        self.naam = naam
        self.logs = []
    def log(self, bericht):
        self.logs.append(bericht)

class HTML_Generator:
    def __init__(self, naam) -> None:
        self.naam = naam
    def genereer_html(self, inhoud):
        with open(f"{self.naam}.html", "w") as f:
            f.write(inhoud)
