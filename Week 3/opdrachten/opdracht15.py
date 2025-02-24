def magische_datum(dag, maand, jaar):
    if dag * maand == jaar % 100:
        return True
    else:
        return False

def main():
    dag = int(input("Geef de dag: "))
    maand = int(input("Geef de maand: "))
    jaar = int(input("Geef het jaar: "))
    if magische_datum(dag, maand, jaar):
        print("Magische datum")
    else:
        print("Geen magische datum")

if __name__ == '__main__':
    main()
