class apparaat:
    def __init__(self, naam, merk) -> None:
        self.naam = naam
        self.merk = merk
        self.type = type
        self.status = False

class Lamp(apparaat):
    def __init__(self, naam, merk) -> None:
        super().__init__(naam, merk)
        self.helderheid = 0
        self.type = "lamp"
    
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

class Woning:
    def __init__(self, naam) -> None:
        self.naam = naam
        self.kamers = []
    def voeg_kamer_toe(self, kamer):
        self.kamers.append(kamer)

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
