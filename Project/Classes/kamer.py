class Kamer:
    def __init__(self, naam, logger=None) -> None:
        self.naam = naam
        self.apparaten = []
        self.bewoners = []
        self.deurslot = None
        self.logger = logger

    def set_logger(self, logger):
        self.logger = logger
        for apparaat in self.apparaten:
            apparaat.set_logger(logger)

    def voeg_apparaat_toe(self, apparaat):
        self.apparaten.append(apparaat)
        apparaat.kamer = self
        apparaat.set_logger(self.logger)

    def voeg_bewoner_toe(self, bewoner):
        self.bewoners.append(bewoner)
        bewoner.kamer = self
        if self.logger:
            self.logger.log(f"{bewoner.naam} is toegevoegd aan {self.naam}.")

    def verplaats_bewoner(self, bewoner):
        if bewoner.kamer is not None:
            bewoner.kamer.bewoners.remove(bewoner)
            if self.logger:
                self.logger.log(f"{bewoner.naam} verlaat {bewoner.kamer.naam}.")
        bewoner.kamer = self
        self.bewoners.append(bewoner)
        if self.logger:
            self.logger.log(f"{bewoner.naam} is nu in {self.naam}.")

    def __str__(self) -> str:
        apparaten_str = "\n".join([" + " + str(apparaat) for apparaat in self.apparaten])
        return f"{self.naam}\n________\nApparaten:\n{apparaten_str}\n________\n"
