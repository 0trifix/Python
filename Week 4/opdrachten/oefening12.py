def is_anagram(word1, word2):
    letters = {}
    for letter in word1:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    for letter in word2:
        if letter in letters:
            letters[letter] -= 1
        else:
            return False
    for letter in letters:
        if letters[letter] != 0:
            return False
    return True

def main():
    print(is_anagram("listen", "silent"))
    print(is_anagram("hello", "world"))

if __name__ == '__main__':
    main()
