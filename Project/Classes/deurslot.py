from .apparaat import Apparaat

class Deurslot(Apparaat):
    def __init__(self, naam, merk, logger=None) -> None:
        super().__init__(naam, merk, logger)
        self.geopend = False
        self.type = "deurslot"
        self.pincode = None
        self.status = False
        self.pogingen = 0

    def pin_toevoegen(self, pincode):
        if isinstance(pincode, str) and len(pincode) == 4 and pincode.isdigit():
            self.pincode = pincode
            self.log(f"Pincode ingesteld: {self.pincode}")
        else:
            raise ValueError("Pincode moet een 4-cijferige string zijn.")

    def open_deur(self, pincode):
        if self.pincode is None:
            raise ValueError("Er is geen pincode ingesteld.")
        if self.pogingen >= 3:
            self.log("Te veel mislukte pogingen. Deurslot is vergrendeld.")
            return False
        if pincode == self.pincode:
            self.geopend = True
            self.pogingen = 0
            self.log("Deur geopend met juiste pincode.")
            return True
        else:
            self.pogingen += 1
            self.log(f"Foute pincode. Poging {self.pogingen}/3.")
            if self.pogingen >= 3:
                self.log("Deurslot is vergrendeld na 3 mislukte pogingen.")
            return False
