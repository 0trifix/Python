class Bolletje:
    def __init__(self, smaak: str) -> None:
        self.smaak = smaak
class Hoorntje:
    def __init__(self) -> None:
        self.bolletjes = []
        self.maximale_bolletjes = 3
    def bolletjes_toevoegen(self, *nieuwe_bolletjes) -> None:
        for bolletje in nieuwe_bolletjes:
            if len(self.bolletjes) >= self.maximale_bolletjes:
                print("Het hoorntje is vol!")
                break
            else:
                self.bolletjes.append(bolletje)

    def __str__(self) -> str:
        return str.join(", ", [bolletje.smaak for bolletje in self.bolletjes])

class Reuzehoorntje(Hoorntje):
    def __init__(self) -> None:
        super().__init__()
        self.maximale_bolletjes = 5

    def bolletjes_toevoegen(self, *nieuwe_bolletjes) -> None:
        for bolletje in nieuwe_bolletjes:
            if len(self.bolletjes) >= self.maximale_bolletjes:
                print("Het reuzehoorntje is vol!")
                break
            else:
                self.bolletjes.append(bolletje)

def main():
    bolletje1 = Bolletje("vanille")
    bolletje2 = Bolletje("aardbei")
    bolletje3 = Bolletje("banaan")
    bolletje4 = Bolletje("chocolade")

    hoorntje = Hoorntje()
    hoorntje.bolletjes_toevoegen(bolletje1, bolletje2, bolletje3, bolletje4)

    reuzehoorntje = Reuzehoorntje()
    reuzehoorntje.bolletjes_toevoegen(bolletje1, bolletje2, bolletje3, bolletje4)

    print(f"Het hoorntje bevat de smaken: {hoorntje}")
    print(f"Het reuzehoorntje bevat de smaken: {reuzehoorntje}")

if __name__ == "__main__":
    main()
