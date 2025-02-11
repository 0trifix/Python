def honden_naar_mensenjaren(leeftijdMensenJaren):
    leeftijdHondenJaren = 0
    if leeftijdMensenJaren == 0:
        print("Input mag niet nul zijn.")
        return
    elif leeftijdMensenJaren <= 2:
        leeftijdHondenJaren += 10.5 * leeftijdMensenJaren
    else:
        leeftijdHondenJaren += (leeftijdMensenJaren - 2) * 4 + 21
    return leeftijdHondenJaren

print(honden_naar_mensenjaren(int(input("Geef een leeftijd in mensenjaren. "))))
