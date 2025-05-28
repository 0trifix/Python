from classes import *

smarthub = SmartHub("Centrale Hub")

huis = Woning("Mijn Huis")
kamer_namen = ["Keuken", "Woonkamer", "Slaapkamer", "Badkamer", "Gang", "Bureau"]
kamers = []
for naam in kamer_namen:
    kamer = Kamer(naam)
    huis.voeg_kamer_toe(kamer)
    kamers.append(kamer)

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
    kamer.sensor = sensor
    kamer.lamp = lamp

def simuleer_beweging(bewoner, kamers):
    interval = 3
    index = 0
    for tijd in range(24):
        print(f"\n {tijd}:00")
        if tijd == 6 or tijd == 21:
            smarthub.tijd_trigger()
        if tijd >= 6 and tijd <= 21:
            if tijd % interval == 0 and index < len(kamers):
                print(f"{bewoner.naam} beweegt naar {kamers[index].naam}.")
                kamers[index].verplaats_bewoner(bewoner)
                if kamers[index].lamp:
                    kamers[index].lamp.zet_helderheid(100)
                index += 1                                   
        for kamer in kamers:
            if len(kamer.bewoners) == 0:
                for apparaat in kamer.apparaten:
                    if apparaat.type == "lamp":
                        apparaat.zet_helderheid(0)


def main():
    bewoner = Bewoner("Jan")
    kamers[2].voeg_bewoner_toe(bewoner)

    volgorde = [kamers[0], kamers[1], kamers[5], kamers[3], kamers[4], kamers[2]]
    simuleer_beweging(bewoner, volgorde)

    print("\nEindstatus woning:\n")
    print(huis)

if __name__ == "__main__":
    main()
