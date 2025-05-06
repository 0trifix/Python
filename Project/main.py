from classes import *

# Huis aanmaken
huis = Woning("Mijn Huis")

# Kamers aanmaken
kamers = [Kamer("Keuken"), Kamer("Woonkamer"), Kamer("Slaapkamer"), Kamer("Badkamer"), Kamer("Gang"), Kamer("Bureau")]
for kamer in kamers:
    huis.voeg_kamer_toe(kamer)
# Standaard apparaten voor elk kamer
standaard_apparaten = [Lamp("Lamp", "Philips"), Deurslot("Deurslot", "Yale"), Bewegingssensor("Bewegingssensor", "Nest"), Rookmelder("Rookmelder", "Nest"), Gordijn("Gordijn", "IKEA")]

# Apparaten toevoegen aan de Kamers
for kamer in huis.kamers:
    for apparaat in standaard_apparaten:
        kamer.voeg_apparaat_toe(apparaat)

# Huis weergeven
print(huis)
