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

# Bewoners aanmaken
bewoners = [
    Bewoner("Alice", 30),
    Bewoner("Bob", 35),
    Bewoner("Charlie", 25)
]
# Bewoners toevoegen aan Kamers
for bewoner in bewoners:
    huis.kamers[0].voeg_bewoner_toe(bewoner)  # Voeg elke bewoner toe aan de Keuken
    
print(huis.kamers[0].bewoners)  # Print de bewoners in de keuken
# Bewoners verplaatsen
for bewoner in bewoners:
    huis.kamers[1].verplaats_bewoner(bewoner)  # Verplaats elke bewoner naar de woonkamer

print(huis.kamers[1].bewoners)  # Print de bewoners in de woonkamer
