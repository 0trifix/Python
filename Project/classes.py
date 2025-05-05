class apparaat:
    def __init__(self, naam, merk, type) -> None:
        self.naam = naam
        self.merk = merk
        self.type = type

    def __str__(self) -> str:
        return f"Apparaat: {self.naam}, Merk: {self.merk}, Type: {self.type}"

class Lamp(apparaat):
    def __init__(self, naam, merk, type, kleur) -> None:
        super().__init__(naam, merk, type)
        self.kleur = kleur

    def __str__(self) -> str:
        return f"{super().__str__()}, Kleur: {self.kleur}"

class Thermostaat(apparaat):
    def __init__(self, naam, merk, type, temperatuur) -> None:
        super().__init__(naam, merk, type)
        self.temperatuur = temperatuur

    def __str__(self) -> str:
        return f"{super().__str__()}, Temperatuur: {self.temperatuur}"

class Deurslot(apparaat):
    def __init__(self, naam, merk, type, status) -> None:
        super().__init__(naam, merk, type)
        self.status = status

    def __str__(self) -> str:
        return f"{super().__str__()}, Status: {self.status}"

class Bewegingssensor(apparaat):
    def __init__(self, naam, merk, type, beweging) -> None:
        super().__init__(naam, merk, type)
        self.beweging = beweging

    def __str__(self) -> str:
        return f"{super().__str__()}, Beweging: {self.beweging}"

class Rookmelder(apparaat):
    def __init__(self, naam, merk, type, rook) -> None:
        super().__init__(naam, merk, type)
        self.rook = rook

    def __str__(self) -> str:
        return f"{super().__str__()}, Rook: {self.rook}"

class Gordijn(apparaat):
    def __init__(self, naam, merk, type, open_status) -> None:
        super().__init__(naam, merk, type)
        self.open_status = open_status

    def __str__(self) -> str:
        return f"{super().__str__()}, Open Status: {self.open_status}"

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

    def __str__(self) -> str:
        return f"Woning: {self.naam}, Kamers: {[kamer.naam for kamer in self.kamers]}"

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

    def __str__(self) -> str:
        return f"SmartHub: {self.naam}, Apparaten: {[str(apparaat) for apparaat in self.apparaten]}"

class Logger:
    def __init__(self, naam) -> None:
        self.naam = naam
        self.logs = []

    def log(self, bericht):
        self.logs.append(bericht)

    def __str__(self) -> str:
        return f"Logger: {self.naam}, Logs: {self.logs}"

class HTML_Generator:
    def __init__(self, naam) -> None:
        self.naam = naam

    def genereer_html(self, inhoud):
        with open(f"{self.naam}.html", "w") as f:
            f.write(inhoud)
