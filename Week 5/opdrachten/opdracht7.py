def vraag_getallen():
    getallen = []
    while True:
        getal = input("Voer een getal in: ")
        if getal == "":
            break
        if not getal.isnumeric():
            print("Dit is geen getal.")
            continue
        getallen.append(int(getal))
    return getallen

def main():
    getallen = vraag_getallen()
    print(f"De som van de getallen is: {sum(getallen)}")

if __name__ == "__main__":
    main()
