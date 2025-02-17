def palindroom(woord):
    reversed_woord = woord[::-1]
    if woord == reversed_woord:
        return True
    else:
        return False

print(palindroom("lepel"))
# https://www.w3schools.com/python/python_howto_reverse_string.asp
