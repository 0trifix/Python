from classes import *

# SmartHub aanmaken
smarthub = SmartHub("Centrale Hub")

# Huis en kamers aanmaken
huis = Woning("Mijn Huis")
kamer_namen = ["Keuken", "Woonkamer", "Slaapkamer", "Badkamer", "Gang", "Bureau"]
kamers = []
for naam in kamer_namen:
    kamer = Kamer(naam)
    huis.voeg_kamer_toe(kamer)
    kamers.append(kamer)

# Apparaten per kamer aanmaken en koppelen aan SmartHub
for kamer in kamers:
    lamp = Lamp(f"Lamp {kamer.naam}", "Philips")
    thermostaat = Thermostaat(f"Thermostaat {kamer.naam}", "Nest", 21)
    deurslot = Deurslot(f"Deurslot {kamer.naam}", "Yale")
    rookmelder = Rookmelder(f"Rookmelder {kamer.naam}", "Nest")
    gordijn = Gordijn(f"Gordijn {kamer.naam}", "IKEA")
    sensor = Bewegingssensor(f"Bewegingssensor {kamer.naam}", "Ring")
    for apparaat in [lamp, thermostaat, deurslot, rookmelder, gordijn, sensor]:
        kamer.voeg_apparaat_toe(apparaat)
        smarthub.voeg_apparaat_toe(apparaat)

# Simulatiefunctie: bewoner loopt door kamers, triggert sensoren
def simuleer_beweging(bewoner, volgorde_kamers):
    for tijd in range(24):  # Simuleer 24 uur
        for kamer in volgorde_kamers:
            print(f"\nTijd: {tijd}:00")
            print(f"\n{bewoner.naam} loopt naar {kamer.naam}.")
            kamer.verplaats_bewoner(bewoner)
            # Bewegingssensor 'detecteert' beweging
            print(f"{kamer.sensor.naam} detecteert beweging in {kamer.naam}.")
            smarthub.beweging_gedetecteerd(kamer.sensor)
            if tijd == 6 or tijd == 21:
                smarthub.tijd_trigger()
            # Toon lampstatus van ALLE lampen in deze kamer
            for apparaat in kamer.apparaten:
                if apparaat.type == "lamp":
                    print(f"Lampstatus {apparaat.naam}: {'Aan' if apparaat.status else 'Uit'}\n")
                if apparaat.type == "gordijn" and tijd == 6:
                    print(apparaat)

def main():
# Bewoner aanmaken en startkamer toewijzen
    bewoner = Bewoner("BOK")
    kamers[0].voeg_bewoner_toe(bewoner)

# Simuleer een rondje door het Huis
#AANPASSEN MET RANDOM!!!
    volgorde = [kamers[0], kamers[1], kamers[4], kamers[2], kamers[3], kamers[5]]
    simuleer_beweging(bewoner, volgorde)

# Eindstatus van het huis weergeven
    print("\nEindstatus woning:\n")
    print(huis)

if __name__ == "__main__":
    main()
