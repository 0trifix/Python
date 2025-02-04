rente = 0.012
bedrag = float(input("Hoeveel heb je op je rekening? \n"))

jaar_1 = bedrag + bedrag*rente
jaar_2 = bedrag + (bedrag*rente*2)
jaar_3 = bedrag + (bedrag*rente*3)

print(f"Na 1 jaar: €{jaar_1}.")
print(f"Na 2 jaar: €{jaar_2}.")
print(f"Na 3 jaar: €{jaar_3}.")