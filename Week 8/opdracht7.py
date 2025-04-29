class Dier:
    def __init__(self, naam: str, kleur: str) -> None:
        self.naam = naam
        self.kleur = kleur
        self.soort = self.__class__.__name__
        self.poten = 4

    def __str__(self) -> str:
        return f"{self.naam} (Kleur: {self.kleur}, Soort: {self.soort}, Poten: {self.poten})"

class Wolf(Dier):
    def __init__(self, naam: str, kleur: str) -> None:
        super().__init__(naam, kleur)
        self.poten = 4

class Schaap(Dier):
    def __init__(self, naam: str, kleur: str) -> None:
        super().__init__(naam, kleur)
        self.poten = 4

class Slang(Dier):
    def __init__(self, naam: str, kleur: str) -> None:
        super().__init__(naam, kleur)
        self.poten = 0

class Papegaai(Dier):
    def __init__(self, naam: str, kleur: str) -> None:
        super().__init__(naam, kleur)
        self.poten = 2
        self.vleugels = 2

    def __str__(self) -> str:
        return f"{self.naam} (Kleur: {self.kleur}, Soort: {self.soort}, Poten: {self.poten}, Vleugels: {self.vleugels})"

class Kooi:
    def __init__(self, identificatienummer: int) -> None:
        self.identificatienummer = identificatienummer
        self.dieren = []

    def voeg_dieren_toe(self, *nieuwe_dieren) -> None:
        for dier in nieuwe_dieren:
            self.dieren.append(dier)

    def __str__(self) -> str:
        return str.join(", ", [str(dier) for dier in self.dieren])

class Dierentuin:
    def __init__(self) -> None:
        self.kooien = []

    def voeg_kooien_toe(self, *nieuwe_kooien) -> None:
        for kooi in nieuwe_kooien:
            self.kooien.append(kooi)
    
    def dieren_met_kleur(self, kleur: str) -> list:
        dieren_met_kleur = []
        for kooi in self.kooien:
            for dier in kooi.dieren:
                if dier.kleur == kleur:
                    dieren_met_kleur.append(dier)
        return dieren_met_kleur

    def dieren_met_aantal_poten(self, aantal_poten: int) -> list:
        dieren_met_aantal_poten = []
        for kooi in self.kooien:
            for dier in kooi.dieren:
                if dier.poten == aantal_poten:
                    dieren_met_aantal_poten.append(dier)
        return dieren_met_aantal_poten

    def totaal_aantal_poten(self) -> int:
        totaal = 0
        for kooi in self.kooien:
            for dier in kooi.dieren:
                totaal += dier.poten
        return totaal

    def __str__(self) -> str:
        return str.join("\n", [f"Kooi {kooi.identificatienummer}: {kooi}" for kooi in self.kooien])

def main():
    wolf = Wolf("Willem", "grijs")
    schaap = Schaap("Sophie", "wit")
    slang = Slang("Slangy", "groen")
    papegaai = Papegaai("Polly", "rood")

    print(wolf)
    print(schaap)
    print(slang)
    print(papegaai)

    kooi = Kooi(1)
    kooi.voeg_dieren_toe(wolf, schaap, slang, papegaai)
    print(f"Kooi {kooi.identificatienummer} bevat de dieren: {kooi}")

    dierentuin = Dierentuin()
    dierentuin.voeg_kooien_toe(kooi)
    print(f"Alle dieren in de dierentuin:\n{dierentuin}")
    print(f"Dieren met kleur 'wit': {[str(dier) for dier in dierentuin.dieren_met_kleur('wit')]}")
    print(f"Dieren met 4 poten: {[str(dier) for dier in dierentuin.dieren_met_aantal_poten(4)]}")
    print(f"Totaal aantal poten in de dierentuin: {dierentuin.totaal_aantal_poten()}")

if __name__ == "__main__":
    main()
