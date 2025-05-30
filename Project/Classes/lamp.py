from .apparaat import Apparaat

class Lamp(Apparaat):
    def __init__(self, naam, merk, logger=None) -> None:
        super().__init__(naam, merk, logger)
        self.helderheid = 0
        self.type = "lamp"

    def zet_helderheid(self, helderheid):
        if 0 <= helderheid <= 100:
            self.helderheid = helderheid
            if helderheid == 0:
                self.status = False
            else:
                self.status = True
            self.log(f"Helderheid ingesteld op {self.helderheid}. Status: {'Aan' if self.status else 'Uit'}")
        else:
            raise ValueError("Helderheid moet tussen 0 en 100 liggen.")

    def __str__(self) -> str:
        return f"{super().__str__()} - Helderheid: {self.helderheid}"
