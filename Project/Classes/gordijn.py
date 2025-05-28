from apparaat import Apparaat

class Gordijn(Apparaat):
    def __init__(self, naam, merk, logger=None) -> None:
        super().__init__(naam, merk, logger)
        self.open = False
        self.type = "gordijn"

    def __str__(self) -> str:
        return f"{super().__str__()} - {'Open' if self.open else 'Gesloten'}"
