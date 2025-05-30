from Classes import *
import random, time

def main():
    logger = Logger()

    smarthub = SmartHub("Centrale Hub", logger=logger)

    huis = Woning("Mijn Huis", logger=logger)
    kamer_namen = [
        "Keuken", "Woonkamer", "Slaapkamer Jan", "Slaapkamer Sophie", "Badkamer", "Gang", "Bureau"
    ]
    kamers = []
    for naam in kamer_namen:
        kamer = Kamer(naam, logger=logger)
        huis.voeg_kamer_toe(kamer)
        kamers.append(kamer)

    for kamer in kamers:
        lamp = Lamp(f"Lamp {kamer.naam}", "Philips", logger=logger)
        thermostaat = Thermostaat(f"Thermostaat {kamer.naam}", "Nest", 21, logger=logger)
        deurslot = Deurslot(f"Deurslot {kamer.naam}", "Yale", logger=logger)
        rookmelder = Rookmelder(f"Rookmelder {kamer.naam}", "Nest", logger=logger)
        gordijn = Gordijn(f"Gordijn {kamer.naam}", "IKEA", logger=logger)
        sensor = Bewegingssensor(f"Bewegingssensor {kamer.naam}", "Ring", logger=logger)
        for apparaat in [lamp, thermostaat, deurslot, rookmelder, gordijn, sensor]:
            kamer.voeg_apparaat_toe(apparaat)
            smarthub.voeg_apparaat_toe(apparaat)
            if apparaat.type == "deurslot" and kamer.naam == "Gang":
                deurslot.status = True
                pincode = str(random.randint(1000, 9999))
                deurslot.pin_toevoegen(pincode)
                kamer.deurslot = deurslot
            kamer.sensor = sensor

    jan = Bewoner("Jan")
    sophie = Bewoner("Sophie")
    kamers[2].voeg_bewoner_toe(jan)
    kamers[3].voeg_bewoner_toe(sophie)
    bewoners = [jan, sophie]

    volgordes = [
        [kamers[0], kamers[1], kamers[5], kamers[4], kamers[2]],  # Jan
        [kamers[0], kamers[1], kamers[3], kamers[5], kamers[4]]   # Sophie
    ]
    indices = [0, 0]

    html_generator = HTML_Generator()

    for tijd in range(24):
        logger.log(f"\n------ {tijd}:00 ------")
        print(f"\n {tijd}:00")
        if tijd == 6:
            smarthub.tijd_trigger()
            for bewoner in bewoners:
                logger.log(f"{bewoner.naam} wordt wakker.")
        if tijd >= 6 and tijd <= 21:
            for i, bewoner in enumerate(bewoners):
                if tijd % 2 == 0 and indices[i] < len(volgordes[i]):
                    kamer = volgordes[i][indices[i]]
                    if kamer.naam == "Gang" and kamer.deurslot:
                        lijst_pincode = [
                            str(random.randint(1000, 9999)),
                            str(random.randint(1000, 9999)),
                            kamer.deurslot.pincode
                        ]
                        for pincode in lijst_pincode:
                            if kamer.deurslot.open_deur(pincode):
                                logger.log(f"{bewoner.naam} heeft het deurslot geopend in {kamer.naam}")
                                break
                            else:
                                logger.log(f"{bewoner.naam} heeft een foute poging gedaan voor deurslot in {kamer.naam}")
                    else:
                        logger.log(f"{bewoner.naam} beweegt naar {kamer.naam}")
                        kamer.verplaats_bewoner(bewoner)
                        smarthub.beweging_gedetecteerd(kamer.sensor)
                    indices[i] += 1
        if tijd == 21:
            smarthub.tijd_trigger()
            for bewoner in bewoners:
                logger.log(f"{bewoner.naam} gaat slapen.")
        if tijd == 3:
            for apparaat in kamers[0].apparaten:
                if apparaat.type == "rookmelder":
                    apparaat.detecteer_rook()
                    apparaat.reset()
        for kamer in kamers:
            if len(kamer.bewoners) == 0:
                for apparaat in kamer.apparaten:
                    if apparaat.type == "lamp":
                        apparaat.zet_helderheid(0)
            if tijd == 21:
                for apparaat in kamer.apparaten:
                    if apparaat.type == "lamp":
                        apparaat.zet_helderheid(0)
        html_generator.genereer_html(
            str(huis) + "\n\nLOGS:\n" + logger.get_logs()
        )
        # if tijd < 6 or tijd > 21:
        #     time.sleep(1)
        # else:
        #     time.sleep(3)

if __name__ == "__main__":
    main()
