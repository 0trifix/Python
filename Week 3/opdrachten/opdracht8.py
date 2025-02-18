def is_priemgetal(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main():
    n = int(input("Geef een getal: "))
    if is_priemgetal(n):
        print("Het getal is een priemgetal")
    else:
        print("Het getal is geen priemgetal")
        
if __name__ == "__main__":
   main() 
