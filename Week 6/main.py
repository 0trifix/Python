import sys
import json
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
            print("Invalid command")
        command = input("> ")

def check():

def html():
    pass

def main():
    if sys.argv[1] == "terminal":
        terminal()
    elif sys.argv[1] == "check":

if __name__ == "__main__":
    main()
