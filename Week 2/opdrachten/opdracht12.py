def gemiddelde():
    getallen = []
    while True:
        getal = input("Geef een getal: ")
        if getal == "0":
            break
        getallen.append(int(getal))

    if len(getallen) == 0 and getal == "0":
        print("Er zijn geen getallen ingegeven.")
        return 0
    return sum(getallen) / len(getallen)

print(gemiddelde())
