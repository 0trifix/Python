from classes import *

# Huis aanmaken
huis = Woning("Mijn Huis")

# Kamers aanmaken
huis.voeg_kamer_toe(Kamer("Keuken"))
huis.voeg_kamer_toe(Kamer("Woonkamer"))
huis.voeg_kamer_toe(Kamer("Slaapkamer"))
huis.voeg_kamer_toe(Kamer("Badkamer"))
huis.voeg_kamer_toe(Kamer("Gang"))
huis.voeg_kamer_toe(Kamer("Bureau"))

# Standaard apparaten voor elk kamer
standaard_apparaten = [Lamp("Lamp", "Philips"), Deurslot("Deurslot", "Yale"), Bewegingssensor("Bewegingssensor", "Nest"), Rookmelder("Rookmelder", "Nest"), Gordijn("Gordijn", "IKEA")]

# Apparaten toevoegen aan de Kamers
for kamer in huis.kamers:
    for apparaat in standaard_apparaten:
        kamer.voeg_apparaat_toe(apparaat)

# Huis weergeven
print(huis)
