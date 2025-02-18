def verzendkosten(aantal_artikkelen):
    prijs = 0
    if aantal_artikkelen == 1:
        prijs = 8.5
    else:
        prijs = 8.5 + (aantal_artikkelen - 1) * 3
    return prijs

def main():
    aantal_artikkelen = int(input("Geef het aantal artikelen: "))
    print(f"De verzendkosten zijn {verzendkosten(aantal_artikkelen)} euro")

if __name__ == "__main__":
    main()
