def is_zin_anagram(zin1, zin2):
    woorden1 = zin1.split()
    woorden2 = zin2.split()
    letters = {}
    ignore = ['.', ',', '!', '?', ' ', ':', ';']
    for woord in woorden1:
        for letter in woord:
            if letter in ignore:
                continue
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    for woord in woorden2:
        for letter in woord:
            if letter in ignore:
                continue
            if letter in letters:
                letters[letter] -= 1
            else:
                return False

