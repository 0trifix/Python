def vereenvoudig(teller,noemer):
    ggd = 1
    for i in range(1,min(teller,noemer)+1):
        if teller % i == 0 and noemer % i == 0:
            ggd = i
    return teller//ggd, noemer//ggd

def main():
    teller = int(input("Geef de teller: "))
    noemer = int(input("Geef de noemer: "))
    teller,noemer = vereenvoudig(teller,noemer)
    print(f"Vereenvoudigd: {teller}/{noemer}")

if __name__ == '__main__':
    main()
