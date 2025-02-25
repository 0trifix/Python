def vraag_woorden():
    woorden = []
    while True:
        woord = input("Geef een woord: ")
        if woord == "":
            break
        woorden.append(woord)
    return woorden

def verwijder_kopies(woorden):
    unieke_woorden = []
    for woord in woorden:
        if woord not in unieke_woorden:
            unieke_woorden.append(woord)
    return unieke_woorden

def print_lijst(lijst):
    for i in range(len(lijst)):
        print(lijst[i])

def main():
    woorden = vraag_woorden()
    unieke_woorden = verwijder_kopies(woorden)
    print_lijst(unieke_woorden)

if __name__ == '__main__':
    main()
