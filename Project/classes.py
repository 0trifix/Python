class Apparaat:
    def __init__(self, naam, merk) -> None:
        self.naam = naam
        self.merk = merk
        self.type = type
        self.status = True
        self.kamer = None
    def __str__(self) -> str:
        return f"{self.naam} ({self.merk}) - {self.type} - {'Aan' if self.status else 'Uit'}"

class Lamp(Apparaat):
    def __init__(self, naam, merk) -> None:
        super().__init__(naam, merk)
        self.helderheid = 0
        self.type = "lamp"
    def zet_helderheid(self, helderheid):
        if 0 <= helderheid <= 100:
            self.helderheid = helderheid
            if helderheid == 0:
                self.status = False
            else:
                self.status = True
        else:
            raise ValueError("Helderheid moet tussen 0 en 100 liggen.")
    def __str__(self) -> str:
        return f"{super().__str__()} - Helderheid: {self.helderheid}"
    
class Thermostaat(Apparaat):
    def __init__(self, naam, merk, temperatuur) -> None:
        super().__init__(naam, merk)
        self.temperatuur = temperatuur
        self.type = "thermostaat"

class Deurslot(Apparaat):
    def __init__(self, naam, merk) -> None:
        super().__init__(naam, merk)
        self.geopend = False
        self.type = "deurslot"
        self.pincode = None
        self.status = False
        self.pogingen = 0
    def pin_toevoegen(self, pincode):
        if isinstance(pincode, str) and len(pincode) == 4 and pincode.isdigit():
            self.pincode = pincode
        else:
            raise ValueError("Pincode moet een 4-cijferige string zijn.")
    def open_deur(self, pincode):
        if self.pincode is None:
            raise ValueError("Er is geen pincode ingesteld.")
        if self.pogingen >= 3:
            print("Te veel mislukte pogingen. Deurslot is vergrendeld.")
            return False
        if pincode == self.pincode:
            self.geopend = True
            self.pogingen = 0
            print(f"{self.naam} is geopend.")
            return True
        else:
            self.pogingen += 1
            print(f"Foute pincode. Poging {self.pogingen}/3.")
            if self.pogingen >= 3:
                print("Deurslot is vergrendeld na 3 mislukte pogingen.")
            return False
      
class Bewegingssensor(Apparaat):
    def __init__(self, naam, merk) -> None:
        super().__init__(naam, merk)
        self.beweging = False
        self.type = "bewegingssensor"

class Rookmelder(Apparaat):
    def __init__(self, naam, merk) -> None:
        super().__init__(naam, merk)
        self.rook_detectie = False
        self.type = "rookmelder"

class Gordijn(Apparaat):
    def __init__(self, naam, merk) -> None:
        super().__init__(naam, merk)
        self.open = False
        self.type = "gordijn"
    def __str__(self) -> str:
        return f"{super().__str__()} - {'Open' if self.open else 'Gesloten'}"

class Kamer:
    def __init__(self, naam) -> None:
        self.naam = naam
        self.apparaten = []
        self.bewoners = []
        self.deurslot = None
    def voeg_apparaat_toe(self, apparaat):
        self.apparaten.append(apparaat)
        apparaat.kamer = self
    def voeg_bewoner_toe(self, bewoner): #Bewoner toevoegen aan kamers
        self.bewoners.append(bewoner)
        bewoner.kamer = self
    def verplaats_bewoner(self, bewoner): # Bewoner verplaatsen naar een andere kamer
        if bewoner.kamer is not None:
            bewoner.kamer.bewoners.remove(bewoner)
        bewoner.kamer = self
        self.bewoners.append(bewoner)
    def __str__(self) -> str:
        apparaten_str = "\n".join([" + " + str(apparaat) for apparaat in self.apparaten])
        return f"{self.naam}\n________\nApparaten:\n{apparaten_str}\n________\n"

class Woning:
    def __init__(self, naam) -> None:
        self.naam = naam
        self.kamers = []
    def voeg_kamer_toe(self, kamer):
        self.kamers.append(kamer)
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
    def __init__(self, naam) -> None:
        self.naam = naam
        self.apparaten = []
        self.regels = []
    def voeg_apparaat_toe(self, apparaat):
        self.apparaten.append(apparaat)
    def beweging_gedetecteerd(self, sensor):
        self.voer_opdracht_uit("lamp", sensor)
    def tijd_trigger(self):
        self.voer_opdracht_uit("gordijn")
    def voer_opdracht_uit(self, apparaatType, sensor=None):
        if sensor != None:
            sensor_kamer = sensor.kamer
        for apparaat in self.apparaten:
            if apparaatType == "lamp" and apparaat.type == "lamp" and apparaat.kamer == sensor_kamer:
                apparaat.zet_helderheid(100)
                print(f"{apparaat.naam} is aangezet door {sensor.naam}.")
            if apparaatType == "gordijn" and apparaat.type == "gordijn":
                if apparaat.open == False:
                    apparaat.open = True
                    print(f"{apparaat.naam} is geopend.")
                else:
                    apparaat.open = False
                    print(f"{apparaat.naam} is gesloten.")

class Logger:
    def __init__(self, naam) -> None:
        self.naam = naam
        self.logs = []
    def log(self, bericht):
        self.logs.append(bericht)

# class HTML_Generator:
#     def __init__(self, naam) -> None:
#         self.naam = naam
#     def genereer_html(self, inhoud):
#         with open(f"{self.naam}.html", "w") as f:
