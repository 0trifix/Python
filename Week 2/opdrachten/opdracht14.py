def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted += char
    return encrypted
# https://www.w3schools.com/python/ref_func_ord.asp
# https://www.w3schools.com/python/ref_func_chr.asp
