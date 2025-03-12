def vraag_getallen():
    getallen = []
    while True:
        getal = input("Voer een getal in: ")
        if getal == "":
            break
        elif not getal.isnumeric():
            print("Dit is geen getal.")
            continue
        else:
            if "." in getal:
                getallen.append(float(getal))
            else:
                getallen.append(int(getal))
    return getallen

def main():
    getallen = vraag_getallen()
    print(f"De som van de getallen is: {sum(getallen)}")

if __name__ == "__main__":
    main()
