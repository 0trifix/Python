class Boek:
    def __init__(self, titel, auteur, prijs, dikte) -> None:
        self.titel = titel
        self.auteur = auteur
        self.prijs = prijs
        self.dikte = dikte

class Kast:
    def __init__(self, ruimte) -> None:
        self.boeken = []
        self.ruimte = ruimte
    def voeg_boek_toe(self, boek) -> None:
        self.boeken.append(boek)
    def verwijder_boek(self, boek) -> None:
        self.boeken.remove(boek)
    def totale_prijs(self) -> float:
        return sum(boek.prijs for boek in self.boeken)
    def bevat_boek(self, boek: str) -> bool:
        return boek in self.boeken
    def 
