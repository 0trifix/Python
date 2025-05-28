class Apparaat:
    def __init__(self, naam, merk, logger=None) -> None:
        self.naam = naam
        self.merk = merk
        self.type = type
        self.status = True
        self.kamer = None
        self.logger = logger

    def set_logger(self, logger):
        self.logger = logger

    def log(self, bericht):
        if self.logger:
            self.logger.log(f"{self.naam}: {bericht}")
        elif self.kamer and hasattr(self.kamer, "logger") and self.kamer.logger:
            self.kamer.logger.log(f"{self.naam}: {bericht}")

    def __str__(self) -> str:
        return f"{self.naam} ({self.merk}) - {self.type} - {'Aan' if self.status else 'Uit'}"

