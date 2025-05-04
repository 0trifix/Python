class Persoon:
    populatie = 0
    def __init__(self):
        Persoon.populatie += 1
    def __del__(self):
        Persoon.populatie -= 1

def main():
    p1 = Persoon()
    p2 = Persoon()
    print("Aantal personen:", Persoon.populatie)
    del p1
    print("Aantal personen:", Persoon.populatie)
    del p2
    print("Aantal personen:", Persoon.populatie)

if __name__ == "__main__":
    main()
