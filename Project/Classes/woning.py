class Woning:
    def __init__(self, naam, logger=None) -> None:
        self.naam = naam
        self.kamers = []
        self.logger = logger

    def voeg_kamer_toe(self, kamer):
        self.kamers.append(kamer)
        kamer.set_logger(self.logger)

    def __str__(self) -> str:
        kamers_str = "\n".join([str(kamer) for kamer in self.kamers])
        return f"Woning: {self.naam}\nKamers:\n{kamers_str}"
