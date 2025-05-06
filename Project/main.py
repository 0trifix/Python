from classes import *

# Huis aanmaken
huis = Woning("Mijn Huis")

# Kamers aanmaken
kamer1 = Kamer("Keuken")
kamer2 = Kamer("Woonkamer")
kamer3 = Kamer("Slaapkamer")
kamer4 = Kamer("Badkamer")
kamer5 = Kamer("Gang")
kamer6 = Kamer("Garage")

# Kamers toevoegen aan het huis
huis.voeg_kamer_toe(kamer1)
huis.voeg_kamer_toe(kamer2)
huis.voeg_kamer_toe(kamer3)
huis.voeg_kamer_toe(kamer4)
huis.voeg_kamer_toe(kamer5)
huis.voeg_kamer_toe(kamer6)

# Standaard apparaten voor elk kamer
standaard_apparaten = [Lamp("Lamp", "Philips"), Deurslot("Deurslot", "Yale"), Bewegingssensor("Bewegingssensor", "Nest"), Rookmelder("Rookmelder", "Nest"), Gordijn("Gordijn", "IKEA")]

# Apparaten toevoegen aan de Kamers
for kamer in huis.kamers:
    for apparaat in standaard_apparaten:
        kamer.voeg_apparaat_toe(apparaat)

# Huis weergeven
print(huis)
