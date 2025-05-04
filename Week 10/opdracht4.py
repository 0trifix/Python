class Transactie:
    balans = 0
    def __init__(self, bedrag: float) -> None:
        self.bedrag = bedrag
        Transactie.balans += bedrag

def main():
    Transactie(100)
    Transactie(-50)
    Transactie(200)
    print("Huidige balans:", Transactie.balans)

if __name__ == "__main__":
    main()
