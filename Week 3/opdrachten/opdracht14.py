def dagen_in_maand(maand,jaar):
    dagen30 = [4,6,9,11]
    dagen31 = [1,3,5,7,8,10,12]
    if maand in dagen30:
        return 30
    elif maand in dagen31:
        return 31
    else:
        if jaar % 4 == 0:
            return 29
        else:
            return 28

def main():
    maand = int(input("Geef de maand: "))
    jaar = int(input("Geef het jaar: "))
    print(f"De maand {maand} in het jaar {jaar} heeft {dagen_in_maand(maand,jaar)} dagen")

if __name__ == '__main__':
    main()
