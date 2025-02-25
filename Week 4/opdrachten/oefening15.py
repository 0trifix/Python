def scrabble_score(word):
    score = 0
    letter_values = {"A": 1, "B": 3, "C": 5, "D": 2, "E": 1, "F": 4, "G": 3, "H": 4, "I": 1, "J": 4, "K": 3, "L": 3, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 2, "S": 2, "T": 2, "U": 4, "V": 4, "W": 5, "X": 8, "Y": 8, "Z": 4}
    for letter in word:
        score += letter_values[letter]
    return score

def main():
    word = "BOK"
    print(scrabble_score(word))

if __name__ == '__main__':
    main()
