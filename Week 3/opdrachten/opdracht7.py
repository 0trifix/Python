def is_intiger(string):
    new_string = string.strip()
    is_int = False
    if new_string[0] == "-" or new_string[0] == "+":
        new_string = new_string[1:]
    for i in new_string:
        if i.isdigit():
            is_int = True
        else:
            is_int = False
            break
    return is_int

def main():
    string = input("Geef een string: ")
    if is_intiger(string):
        print("De string is een integer")
    else:
        print("De string is geen integer")

if __name__ == "__main__":
    main()

