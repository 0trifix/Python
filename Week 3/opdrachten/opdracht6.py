# def hoofdletter_verbetering(tekst):
#     for i in range(0, len(tekst)):
#         if i == 0:
#             tekst[i] = tekst[i].upper()
#         if tekst[i] == "." or tekst[i] == "!" or tekst[i] == "?":
#             tekst[i + 1] = tekst[i + 1].upper()
#     return tekst

def hoofdletter_verbetering(tekst):
    tekst = tekst.strip()  # Verwijder overbodige spaties aan begin/einde
    nieuwe_tekst = []
    hoofdletter_volgende = True  # Eerste letter moet hoofdletter zijn
    
    for i, char in enumerate(tekst):
        if hoofdletter_volgende and char.isalpha():
            nieuwe_tekst.append(char.upper())
            hoofdletter_volgende = False
        else:
            nieuwe_tekst.append(char)

        if char in ".!?":  # Na een leesteken een hoofdletter laten volgen
            hoofdletter_volgende = True
    
    return "".join(nieuwe_tekst)

def main():
    tekst = input("Geef een tekst: ")
    print(hoofdletter_verbetering(tekst))

if __name__ == "__main__":
    main()
