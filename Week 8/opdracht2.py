class Bolletje:
    def __init__(self, smaak: str) -> None:
        self.smaak = smaak
class Hoorntje:
    def __init__(self) -> None:
        self.bolletjes = []
    def bolletjes_toevoegen(self, *nieuwe_bolletjes) -> None:
        for bolletje in nieuwe_bolletjes:
            self.bolletjes.append(bolletje)
    def __str__(self) -> str:
        return str.join(", ", [bolletje.smaak for bolletje in self.bolletjes])


def main():
    bolletje1 = Bolletje("vanille")
    bolletje2 = Bolletje("aardbei")
    bolletje3 = Bolletje("banaan")

    hoorntje = Hoorntje()
    hoorntje.bolletjes_toevoegen(bolletje1, bolletje2, bolletje3)

    print(f"Het hoorntje bevat de smaken: {hoorntje}")

if __name__ == "__main__":
    main()
