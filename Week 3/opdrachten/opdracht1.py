def hypothenusa(a, b):
    return (a**2 + b**2)**0.5

def main():
    a = int(input("Geef de lengte van de eerste rechthoekszijde: "))
    b = int(input("Geef de lengte van de tweede rechthoekszijde: "))
    print(f"De lengte van de schuine zijde is {hypothenusa(a, b)}")

if __name__ == "__main__":
    main()
