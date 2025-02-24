def check_wachtwoord(wachtwoord):
    if len(wachtwoord)< 8:
        return False
    if wachtwoord.isalpha():
        return False
    if wachtwoord.isdigit():
        return False
    upper = any(c.isupper() for c in wachtwoord)
    lower = any(c.islower() for c in wachtwoord)
    if not upper or not lower:
        return False
    return True

def main():
    wachtwoord = input("Geef een wachtwoord: ")
    if check_wachtwoord(wachtwoord):
        print("Wachtwoord is OK")
    else:
        print("Wachtwoord is niet OK")


if __name__ == '__main__':
    main()
