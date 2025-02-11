
def klinkerOfNiet(input):
    klinkers = ["a", "o" ,"e", "i", "u"]
    if len(input) >1:
        print("Kan uitkomst niet berekenen; string te lang. (Max 1 teken)")
        return
    elif input in klinkers:
        print("Je hebt een klinker gegeven.")
        return
    elif input == "y":
        print("De letter 'y' word soms gezien als een klinker en soms niet.")
        return
    else:
        print("Dit is een medeklinker.")
        return
klinkerOfNiet(input("Geef een letter. "))
