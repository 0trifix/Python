import sys

def terminal():
    command = input("> ")
    servers = []
    while command != "exit":
        if command == "add":
            add()
        elif command == "remove":
            remove()
        elif command == "list":
            list()
        else:
            print("Invalid command")
        command = input("> ")

def add():


def remove():

def list():

def main():
    terminal()

if __name__ == "__main__":
    main()
