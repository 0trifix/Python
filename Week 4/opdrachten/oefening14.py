def bingo_kaart():
    import random
    kaart = {"B": [], "I": [], "N": [], "G": [], "O": []}
    for letter in kaart:
        kaart[letter] = random.sample(range(1, 16), 5)
    return kaart

def print_kaart(kaart):
    print("B\tI\tN\tG\tO")
    for i in range(5):
        for letter in kaart:
            print(kaart[letter][i], end="\t")
        print()

def main():
    kaart = bingo_kaart()
    print_kaart(kaart)

if __name__ == '__main__':
    main()
