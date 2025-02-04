aantal_grote = float(input("Geef de aantal grote flessen: "))
aantal_kleine = float(input("Geef de aantal kleine flessen: "))

prijs_groot = 0.25
prijs_klein = 0.12

print(f"Je krijgt €{round((prijs_groot*aantal_grote + prijs_klein * aantal_kleine),2)} terug.")