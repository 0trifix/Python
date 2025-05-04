class Envelop:
    def __init__(self, gewicht: float, is_verstuurd: bool = False) -> None:
        self.gewicht = gewicht
        self.is_verstuurd = is_verstuurd
    def portokosten_nodig(self) -> float:
        self.portokosten = self.gewicht * 10
        return self.portokosten
    def verstuur(self) -> None:
        self.is_verstuurd = True
    def frankeer(self, portokosten) -> None:
        if self.portokosten_nodig() <= portokosten:
            self.verstuur()

envelop = Envelop(0.5)
envelop.frankeer(5)
print(envelop.is_verstuurd)  # Output: True

class GroteEnvelop(Envelop):
    def __init__(self, gewicht: float, is_verstuurd: bool = False) -> None:
        super().__init__(gewicht, is_verstuurd)
    def portokosten_nodig(self) -> float:
        self.portokosten = self.gewicht * 15
        return self.portokosten
