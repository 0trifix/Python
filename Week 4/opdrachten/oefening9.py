def omgekeerd_zoeken(dictionary, value):
    for key in dictionary:
        if dictionary[key] == value:
            return key
    return None

def main():
    dictionary = {"a": 1, "b": 2, "c": 3}
    value = 2
    print(omgekeerd_zoeken(dictionary, value))

if __name__ == '__main__':
    main()
