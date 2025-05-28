import os

class Logger:
    def __init__(self):
        import datetime
        if not os.path.exists("logs"):
            os.makedirs("logs")
        self.log_file = f"logs/{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_log.txt"
        self.logs = []

    def log(self, bericht):
        import datetime
        tijd = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        regel = f"{tijd} - {bericht}"
        self.logs.append(regel)
        with open(self.log_file, "a") as f:
            f.write(regel + "\n")

    def get_logs(self):
        return "\n".join(self.logs)

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
    
class Thermostaat(Apparaat):
    def __init__(self, naam, merk, temperatuur, logger=None) -> None:
        super().__init__(naam, merk, logger)
        self.temperatuur = temperatuur
        self.type = "thermostaat"

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

class Bewegingssensor(Apparaat):
    def __init__(self, naam, merk, logger=None) -> None:
        super().__init__(naam, merk, logger)
        self.beweging = False
        self.type = "bewegingssensor"

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

class Gordijn(Apparaat):
    def __init__(self, naam, merk, logger=None) -> None:
        super().__init__(naam, merk, logger)
        self.open = False
        self.type = "gordijn"

    def __str__(self) -> str:
        return f"{super().__str__()} - {'Open' if self.open else 'Gesloten'}"

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

class Bewoner:
    def __init__(self, naam) -> None:
        self.naam = naam
        self.kamer = None

    def __str__(self) -> str:
        return f"Bewoner: {self.naam} - Kamer: {self.kamer.naam if self.kamer else 'Geen kamer toegewezen'}"

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

class HTML_Generator:
    def __init__(self) -> None:
        import os
        self.naam = "_sites/index.html"
        if not os.path.exists("_sites"):
            os.makedirs("_sites")
    def genereer_html(self, inhoud):
        import webbrowser, os
        with open(f"{self.naam}", "w") as f:
            f.write("<html>\n<head>\n<title>Smart Home Log</title>\n</head>\n<body>\n")
            f.write("<h1>Smart Home Simulatie</h1>\n")
            f.write("<pre>\n")
            f.write(inhoud)
            f.write("</pre>\n")
            f.write("</body>\n</html>")
        webbrowser.open(f"file://{os.path.realpath(self.naam)}", new=0)
