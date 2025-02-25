def lees_getallen():
    lijst = []
    while True:
        getal = input("Geef een getal: ")
        if getal == "":
            break
        else:
            lijst.append(int(getal))
    return lijst

def filter_getallen(lijst):
    negatieven = []
    nullen = []
    positieven = []
    for getal in lijst:
        if getal < 0:
            negatieven.append(getal)
        elif getal == 0:
            nullen.append(getal)
        else:
            positieven.append(getal)
    return negatieven, nullen, positieven

def print_lijst(lijst):
    for i in range(len(lijst)):
        print(lijst[i])
def main():
    lijst = lees_getallen()
    print_lijst(filter_getallen(lijst)[0])
    print_lijst(filter_getallen(lijst)[1])
    print_lijst(filter_getallen(lijst)[2])

if __name__ == '__main__':
    main()
