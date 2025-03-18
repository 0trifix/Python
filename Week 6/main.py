import sys
import json
import os
from management import add, remove, list, help

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
            print("Invalid command, type 'help")
        command = input("> ")

def check():
    serversFile = "servers.json"
    with open(serversFile, "r") as file:
        servers = json.load(file)
    for server in servers:
        if ping(server["ip"]):
            print(f"{server['name']}-{server['ip']}: UP")
        else:
            print(f"{server['name']}-{server['ip']}: DOWN")

def ping(ip):
    response = os.system("ping -c 1 " + ip)
    if response == 0:
        return True
    else:
        return False

def html():
    pass

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py [terminal|check]")
        return
    elif sys.argv[1] == "terminal":
        terminal()
    elif sys.argv[1] == "check":
        check()
    else:
        print("Invalid option")
        print("Usage: python main.py [terminal|check]")
        return


if __name__ == "__main__":
    main()
