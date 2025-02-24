def wachtwoord_generator():
    import random
    lengte = random.randint(7,10)
    wachtwoord = ""
    for i in range(lengte):
        wachtwoord += chr(random.randint(33,126))
    return wachtwoord

if __name__ == "__main__":
    print(wachtwoord_generator())

