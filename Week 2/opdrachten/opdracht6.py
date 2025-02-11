def seizoen(maand,dag):
    winter = ["december", "januari", "februari", "maart"]
    lente = ["maart", "april", "mei", "juni"]
    zomer = ["juni", "juli",  "augustus", "september"]
    herfst = ["september", "oktober", "november", "december"]

    if maand in winter:
        if maand == winter[0] and dag < 21:
            print("Op de gegeven dag is het herfst.")
        elif maand == winter[-1] and dag > 19:
            print("Op de gegeven dag is het lente.")
        else:
            print("Op de gegeven dag is het winter.")

    elif maand in lente:
        if maand == lente[0] and dag < 20:
            print("Op de gegeven dag is het winter.")
        elif maand == lente[-1] and dag > 20:
            print("Op de gegeven dag is het zomer.")
        else:
            print("Op de gegeven dag is het lente.")

    elif maand in zomer:
        if maand == zomer[0] and dag < 21:
            print("Op de gegeven dag is het lente.")
        elif maand == zomer[-1] and dag > 21:
            print("Op de gegeven dag is het herfst.")
        else:
            print("Op de gegeven dag is het zomer.")

    elif maand in herfst:
        if maand == herfst[0] and dag < 22:
            print("Op de gegeven dag is het zomer.")
        elif maand == herfst[-1] and dag > 20:
            print("Op de gegeven dag is het winter.")
        else:
            print("Op de gegeven dag is het herfst.")

seizoen("maart", 19)
