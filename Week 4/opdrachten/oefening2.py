def grootste_kleinste_getallen(lijst, n):
    if n*2 > len(lijst):
        print("De lijst is te kort.")
        return None
    else:
        lijst.sort()
        return lijst[:n] + lijst[-n:]

def main():
    lijst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = 3
    print(grootste_kleinste_getallen(lijst, n))

if __name__ == '__main__':
    main()
