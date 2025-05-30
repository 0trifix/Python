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

def main():
    wolf = Wolf("Willem", "grijs")
    schaap = Schaap("Sophie", "wit")
    slang = Slang("Slangy", "groen")
    papegaai = Papegaai("Polly", "rood")

    print(wolf)
    print(schaap)
    print(slang)
    print(papegaai)

if __name__ == "__main__":
    main()
