class Bolletje:
    def __init__(self, smaak: str) -> None:
        self.smaak = smaak

def maak_bolletjes():
    bol1 = Bolletje("vanille")
    bol2 = Bolletje("aardbei")
    bol3 = Bolletje("bannan")

    bolletjes = [bol1, bol2, bol3]

    for bolletje in bolletjes:
        print(f"Bolletje met smaak: {bolletje.smaak}")

def main():
    maak_bolletjes()

if __name__ == "__main__":
    main()
