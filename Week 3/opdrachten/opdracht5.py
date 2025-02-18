def check_string_lengte(string, beschikbare_lengte):
    if len(string) < beschikbare_lengte:
        nieuwe_string = ((beschikbare_lengte-len(string))//2)*" "+string
        return nieuwe_string
    else:
        return string

def main():
    string = input("Geef een string: ")
    beschikbare_lengte = int(input("Geef de beschikbare lengte: "))
    print(check_string_lengte(string, beschikbare_lengte))

if __name__ == "__main__":
    main()      
