from classes import *
# In dit bestand test ik alle delen van mijn code
def test():
    kamer1 = Kamer("Keuken")
    huis = Woning("Mijn Huis")
    huis.voeg_kamer_toe(kamer1)
    print(huis)

if __name__ == "__main__":
    test()
