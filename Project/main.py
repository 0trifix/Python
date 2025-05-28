from classes import *
import random, time

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
        if apparaat.type == "deurslot" and kamer.naam == "Gang":
            deurslot.status = True
            pincode = str(random.randint(1000, 9999))  # Genereer een willekeurige 4-cijferige pincode
            deurslot.pin_toevoegen(pincode)
            print(f"Pincode voor {deurslot.naam} is ingesteld op {pincode}")
            kamer.deurslot = deurslot

def simuleer_beweging(bewoner, kamers):
    interval = 2
    index = 0
    for tijd in range(24):
        print(f"\n {tijd}:00")
        if tijd == 6:
            smarthub.tijd_trigger()
            print(f"{bewoner.naam} is wakker geworden.")
        if tijd >= 6 and tijd <= 21:
            if tijd % interval == 0 and index < len(kamers):
                if kamers[index].naam == "Gang":
                    lijst_pincode = [random.randint(1000, 9999), random.randint(1000, 9999), kamers[index].deurslot.pincode]
                    for pincode in lijst_pincode:
                        if kamers[index].deurslot.open_deur(pincode):
                            break
                else:
                    print(f"{bewoner.naam} beweegt naar {kamers[index].naam}.")
                    kamers[index].verplaats_bewoner(bewoner)
                for apparaat in kamers[index].apparaten:
                    if apparaat.type == "lamp":
                        apparaat.zet_helderheid(100)
                index += 1                                   
        if tijd == 21:
            smarthub.tijd_trigger()
            print(f"{bewoner.naam} gaat slapen.")
        if tijd == 3:
            for apparaat in kamers[0].apparaten:
                if apparaat.type == "rookmelder":
                    apparaat.detecteer_rook()
                    apparaat.reset()
        for kamer in kamers:
            # Lichten uit zetten als er geen bewoners zijn of het tijd is om te slapen
            if len(kamer.bewoners) == 0:
                for apparaat in kamer.apparaten:
                    if apparaat.type == "lamp":
                        apparaat.zet_helderheid(0)
            if tijd == 21:
                for apparaat in kamer.apparaten:
                    if apparaat.type == "lamp":
                        apparaat.zet_helderheid(0)
        # if tijd < 6 or tijd > 21:
        #     time.sleep(0.5)
        # else:
        #     time.sleep(2)

def main():
    bewoner = Bewoner("Jan")
    kamers[2].voeg_bewoner_toe(bewoner)

    volgorde = [kamers[0], kamers[1], kamers[5], kamers[3], kamers[4], kamers[4], kamers[2]]
    simuleer_beweging(bewoner, volgorde)

    HTML = HTML_Generator()
    HTML.genereer_html(str(huis))

if __name__ == "__main__":
    main()
