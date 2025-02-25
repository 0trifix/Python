def dobbelstenen():
    import random
    dobbelstenen_waardes = {"2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "11": 0, "12": 0}
    for i in range(1000):
        dobbelsteen1 = random.randint(1, 6)
        dobbelsteen2 = random.randint(1, 6)
        dobbelstenen_waardes[str(dobbelsteen1 + dobbelsteen2)] += 1
    return dobbelstenen_waardes

def tabel(dobbelstenen_waardes):
    print("Waarde\tGesimuleerd Percentage\tVerwacht Percentage")
    for waarde, frequentie in dobbelstenen_waardes.items():
        percentage = round(frequentie / 1000 * 100, 2)
        verwachte_percentage = [2.78, 5.56, 8.33, 11.11, 13.89, 16.67, 13.89, 11.11, 8.33, 5.56, 2.78]
        print(f"{waarde}\t{percentage}%\t\t\t{verwachte_percentage[int(waarde) - 2]}%")

def main():
    dobbelstenen_waardes = dobbelstenen()
    tabel(dobbelstenen_waardes)

if __name__ == '__main__':
    main()
