class Bewoner:
    def __init__(self, naam) -> None:
        self.naam = naam
        self.kamer = None

    def __str__(self) -> str:
        return f"Bewoner: {self.naam} - Kamer: {self.kamer.naam if self.kamer else 'Geen kamer toegewezen'}"
