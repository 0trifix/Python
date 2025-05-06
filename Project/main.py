from classes import *

# Huis aanmaken
huis = Woning("Mijn Huis")

# Kamers aanmaken
kamers = [Kamer("Keuken"), Kamer("Woonkamer"), Kamer("Slaapkamer"), Kamer("Badkamer"), Kamer("Gang"), Kamer("Bureau")]
for kamer in kamers:
    huis.voeg_kamer_toe(kamer)
# Apparaten aanmaken en toevoegen aan kamers
for kamer in huis.kamers:
    apparaten = [
        Lamp("Lamp", "Philips"),
        Thermostaat("Thermostaat", "Nest", 22),
        Deurslot("Deurslot", "Yale"),
        Bewegingssensor("Bewegingssensor", "Ring"),
        Rookmelder("Rookmelder", "Nest"),
        Gordijn("Gordijn", "IKEA")
    ]
    for apparaat in apparaten:
        kamer.voeg_apparaat_toe(apparaat)

huis.kamers[0].apparaten[0].zet_helderheid(50)  # Zet de helderheid van de lamp in de keuken op 50%

# Huis weergeven
print(huis)
