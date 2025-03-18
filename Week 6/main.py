import sys
import json
import re

def terminal():
    command = input("> ")
    serversFile = "servers.json"
    try:
        with open(serversFile, "r") as file:
            if file.read() == "":
                with open(serversFile, "w") as file:
                    json.dump([], file)
    except FileNotFoundError:
        with open(serversFile, "w") as file:
            json.dump([], file)
        
    while command != "exit":
        if command == "add":
            add(serversFile)
        elif command == "remove":
            remove(serversFile)
        elif command == "list":
            list(serversFile)
        elif command == "help":
            help()
        else:
            print("Invalid command")
        command = input("> ")

def add(serverFile):
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
    with open(serverFile, "r") as file:
        servers = json.load(file)
    for server in servers:
        print(f"{server['name']} - {server['ip']}")
    
def help():
    print("add - Add a server")
    print("remove - Remove a server")
    print("list - List all servers")
    print("exit - Exit the program")

def html():
    pass

def checkIP(ip):
    return re.match(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", ip) is not None

def main():
    terminal()

if __name__ == "__main__":
    main()
