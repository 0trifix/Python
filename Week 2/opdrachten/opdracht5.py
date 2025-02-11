def lengteMaand(naamMaand):
    maand30 = ["april", "juni", "september", "november"]
    maand31 = ["januari", "maart", "mei", "juli", "augustus", "oktober", "december"]
    if naamMaand in maand30:
        print(f"De maand {naamMaand} telt 30 dagen.")
        return
    elif naamMaand in maand31:
        print(f"De maand {naamMaand} telt 31 dagen.")
        return
    elif naamMaand == "februari":
        print(f"De maand {naamMaand} telt 28 of 29 dagen.")
        return

lengteMaand(input("Geef een maand (zonder hoofdletter).\n"))
