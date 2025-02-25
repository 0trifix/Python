def kommas_in_lijst(lijst):
    for i in range(len(lijst)):
        print(lijst[i], end="")
        if i != len(lijst) - 2:
            print(", ", end="")
        else:
            print(" en", end=" ")
    print()

def main():
    lijst = ["rozen", "viooltjes", "madeliefjes"]
    kommas_in_lijst(lijst)

if __name__ == '__main__':
    main()
