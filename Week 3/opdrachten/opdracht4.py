def mediaan_drie_getallen(a,b,c):
    lijst = [a,b,c]
    lijst.sort()
    return lijst[1]

def main():
    a = int(input("Geef het eerste getal: "))
    b = int(input("Geef het tweede getal: "))
    c = int(input("Geef het derde getal: "))
    print(f"De mediaan is {mediaan_drie_getallen(a,b,c)}")

if __name__ == "__main__":
    main()
