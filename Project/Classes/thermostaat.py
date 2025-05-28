from apparaat import Apparaat

class Thermostaat(Apparaat):
    def __init__(self, naam, merk, temperatuur, logger=None) -> None:
        super().__init__(naam, merk, logger)
        self.temperatuur = temperatuur
        self.type = "thermostaat"
