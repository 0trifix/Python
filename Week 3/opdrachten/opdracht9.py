def is_priemgetal(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def volgend_priemgetal(n):
    while True:
        n += 1
        if is_priemgetal(n):
            return n
def main():
    n = int(input("Geef een getal: "))
    print(f"Het volgende priemgetal is {volgend_priemgetal(n)}")

if __name__ == "__main__":
    main()
