from apparaat import Apparaat

class Bewegingssensor(Apparaat):
    def __init__(self, naam, merk, logger=None) -> None:
        super().__init__(naam, merk, logger)
        self.beweging = False
        self.type = "bewegingssensor"
