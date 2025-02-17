def roulette():
    from random import randint
    getal = randint(0, 37)
    rood = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    zwart = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    if getal == 37:
        print("Balletje is beland op 00")
    else:
        print(f"Balletje is beland op {getal}")
    if getal == 0:
        print("Betaal 0")
    elif getal == 37:
        print("Betaal 00")
    else:
        print(f"Betaal {getal}")
        if getal in rood:
            print("Betaal rood")
        elif getal in zwart:
            print("Betaal zwart")
        if getal % 2 == 0:
            print("Betaal even")
        else:
            print("Betaal oneven")
        if getal <= 18:
            print("Betaal 1 t.e.m. 18")
        else:
            print("Betaal 19 t.e.m. 36")
    return getal

roulette()
