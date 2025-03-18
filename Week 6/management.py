def add(serverFile):
    import json
    name = input("Name: ")
    ip = input("IP: ")
    if not checkIP(ip):
        print("Invalid IP")
        return
    server = {
        "name": name,
        "ip": ip
    }
    with open(serverFile, "r") as file:
        servers = json.load(file)
    servers.append(server)
    with open(serverFile, "w") as file:
        json.dump(servers, file)
    

def remove(serverFile):
    import json
    name = input("Name: ")
    with open(serverFile, "r") as file:
        servers = json.load(file)
    for server in servers:
        if server["name"] == name:
            servers.remove(server)
            break
    with open(serverFile, "w") as file:
        json.dump(servers, file)

def list(serverFile):
    import json
    with open(serverFile, "r") as file:
        servers = json.load(file)
    for server in servers:
        print(f"{server['name']} - {server['ip']}")
    
def help():
    print("add - Add a server")
    print("remove - Remove a server")
    print("list - List all servers")
    print("exit - Exit the program")

def checkIP(ip):
    n = len(ip)

    if n < 7:
        return False

    # Using split to separate all the strings from '.'
    # and create a list like for example -
    substrings = ip.split(".")
    count = 0

    for substr in substrings:
        count += 1

        # If the substring size is greater than 1 and 
        # the first character is '0', return false
        if len(substr) > 1 and substr[0] == '0':
            return False

        # For substrings like a.b.c.d, checking if
        # any character is non-numeric
        if not substr.isdigit():
            return False

        # Check if the number is greater than 255
        if int(substr) > 255:
            return False

    # If the count of substrings is not 4, return false
    if count != 4:
        return False

    return True

