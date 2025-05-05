class apparaat:
    def __init__(self, naam, merk, type) -> None:
        self.naam = naam
        self.merk = merk
        self.type = type

class Lamp(apparaat):
    def __init__(self, naam, merk, type) -> None:
        super().__init__(naam, merk, type)
        self.type = "lamp"

class Thermostaat(apparaat):
    def __init__(self, naam, merk, type, temperatuur) -> None:
        super().__init__(naam, merk, type)
        self.temperatuur = temperatuur

class Deurslot(apparaat):
    def __init__(self, naam, merk, type, status) -> None:
        super().__init__(naam, merk, type)
        self.status = status

class Bewegingssensor(apparaat):
    def __init__(self, naam, merk, type, beweging) -> None:
        super().__init__(naam, merk, type)
        self.beweging = beweging

class Rookmelder(apparaat):
    def __init__(self, naam, merk, type, rook) -> None:
        super().__init__(naam, merk, type)
        self.rook = rook

class Gordijn(apparaat):
    def __init__(self, naam, merk, type, open_status) -> None:
        super().__init__(naam, merk, type)
        self.open_status = open_status

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
