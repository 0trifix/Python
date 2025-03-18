import sys, os, json, datetime
from management import add, remove, list, help

def terminal(serversFile):
    command = input("> ")
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

def check(serversFile):
    with open(serversFile, "r") as file:
        servers = json.load(file)
    for server in servers:
        if ping(server["ip"], server["name"]):
            print(f"{server['name']}-{server['ip']}: UP")
        else:
            print(f"{server['name']}-{server['ip']}: DOWN")

def ping(ip, name):
    response = os.system(f"ping -c 1 {ip} > logs/{name}{datetime.datetime.now().strftime('_%H_%M_%d_%m_%Y.log')}")
    if response == 0:
        return True
    else:
        return False

def init():
    try:
        os.mkdir("logs")
    except FileExistsError:
        pass


def html():
    

def main():
    serversFile = "servers.json"
    if len(sys.argv) < 2:
        print("Usage: python main.py [terminal|check]")
        return
    elif sys.argv[1] == "terminal":
        init()
        terminal(serversFile)
    elif sys.argv[1] == "check":
        init()
        check(serversFile)
    else:
        print("Invalid option")
        print("Usage: python main.py [terminal|check]")
        return


if __name__ == "__main__":
    main()
