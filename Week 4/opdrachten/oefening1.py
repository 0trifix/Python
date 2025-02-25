def print_lijst(lijst):
    for i in range(len(lijst)):
        print(lijst[i])

def main():
    getal = int(input("Geef een getal: "))
    lijst = []
    while getal != 0:
        lijst.append(getal)
        getal = int(input("Geef een getal: "))
    lijst.sort()
    print_lijst(lijst)

if __name__ == '__main__':
    main()
