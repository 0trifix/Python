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
