def loterij():
    import random
    loterij = []
    while len(loterij) < 6:
        randomgetal = random.randint(1, 49)
        if randomgetal not in loterij:
            loterij.append(randomgetal)
        loterij.sort()
    return loterij

def main():
    print(loterij())

if __name__ == '__main__':
    main()
