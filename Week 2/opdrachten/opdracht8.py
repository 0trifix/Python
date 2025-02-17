def scrhikkeljaar(jaar):
    if jaar % 4 == 0:
        if jaar % 100 == 0:
            if jaar % 400 == 0:
                print(f"Het jaar {jaar} is een schrikkeljaar")
                return True
            else:
                print(f"Het jaar {jaar} is geen schrikkeljaar")
                return False
        else:
            print(f"Het jaar {jaar} is een schrikkeljaar")
            return True
    else:
        print(f"Het jaar {jaar} is geen schrikkeljaar")
        return False

scrhikkeljaar(int(input("Geef een jaar: ")))
