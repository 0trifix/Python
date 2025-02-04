rente = 0.012
bedrag = float(input("Hoeveel heb je op je rekening? \n"))

jaar_1 = round(bedrag + bedrag*rente,2)
jaar_2 = round(bedrag + (bedrag*rente*2),2)
jaar_3 = round(bedrag + (bedrag*rente*3),2)

print(f"Na 1 jaar: €{jaar_1}.")
print(f"Na 2 jaar: €{jaar_2}.")
print(f"Na 3 jaar: €{jaar_3}.")