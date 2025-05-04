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


class GroteEnvelop(Envelop):
    def __init__(self, gewicht: float, is_verstuurd: bool = False) -> None:
        super().__init__(gewicht, is_verstuurd)
    def portokosten_nodig(self) -> float:
        self.portokosten = self.gewicht * 15
        return self.portokosten

def main():
    e1 = Envelop(0.5)
    print("Portokosten envelop:", e1.portokosten_nodig())
    e1.frankeer(10)
    print("Is envelop verstuurd?", e1.is_verstuurd)

    ge1 = GroteEnvelop(0.5)
    print("Portokosten grote envelop:", ge1.portokosten_nodig())
    ge1.frankeer(10)
    print("Is grote envelop verstuurd?", ge1.is_verstuurd)

if __name__ == "__main__":
    main()
