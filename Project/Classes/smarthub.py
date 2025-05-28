class SmartHub:
    def __init__(self, naam, logger=None) -> None:
        self.naam = naam
        self.apparaten = []
        self.logger = logger
    def set_logger(self, logger):
        self.logger = logger

    def voeg_apparaat_toe(self, apparaat):
        self.apparaten.append(apparaat)
        apparaat.set_logger(self.logger)
    def beweging_gedetecteerd(self, sensor):
        self.voer_opdracht_uit("lamp", sensor)
        if self.logger:
            self.logger.log(f"SmartHub: beweging gedetecteerd door {sensor.naam} in {sensor.kamer.naam}.")
    def tijd_trigger(self):
        self.voer_opdracht_uit("gordijn")
        if self.logger:
            self.logger.log(f"SmartHub: tijd-trigger uitgevoerd, gordijnen geactiveerd.")
    def voer_opdracht_uit(self, apparaatType, sensor=None):
        if sensor is not None:
            sensor_kamer = sensor.kamer
        for apparaat in self.apparaten:
            if apparaatType == "lamp" and apparaat.type == "lamp" and apparaat.kamer == sensor_kamer:
                apparaat.zet_helderheid(100)
            if apparaatType == "gordijn" and apparaat.type == "gordijn":
                apparaat.open = not apparaat.open
                if self.logger:
                    self.logger.log(f"{apparaat.naam} is {'geopend' if apparaat.open else 'gesloten'} door tijd-trigger.")
