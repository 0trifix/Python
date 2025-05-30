from .apparaat import Apparaat

class Rookmelder(Apparaat):
    def __init__(self, naam, merk, logger=None) -> None:
        super().__init__(naam, merk, logger)
        self.type = "rookmelder"
        self.rook_detectie = False

    def detecteer_rook(self):
        self.rook_detectie = True
        for i in range(3):
            self.log("detecteert rook! Alarm gaat af!")
    
    def reset(self):
        self.rook_detectie = False
        self.log("is gereset en rookdetectie is uitgeschakeld.")
