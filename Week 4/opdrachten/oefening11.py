def aantal_unieke_karakters(woord):
    unieke_karakters = {}
    for karakter in woord:
        if karakter not in unieke_karakters:
            unieke_karakters[karakter] = 1
        else:
            unieke_karakters[karakter] += 1
    return len(unieke_karakters)

def main():
    woord = input("Geef een woord: ")
    print(aantal_unieke_karakters(woord))

if __name__ == '__main__':
    main()
