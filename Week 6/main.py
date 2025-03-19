import sys, os, json, datetime, customtkinter
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
    try:
        with open(serversFile, "r") as file:
            servers = json.load(file)
    except FileNotFoundError:
        print("No servers listed!")
        return
    server_statuses = []
    for server in servers:
        status = "UP" if ping(server["ip"], server["name"]) else "DOWN"
        server_statuses.append({"name": server["name"], "ip": server["ip"], "status": status})
        print(f"{server['name']}-{server['ip']}: {status}")
    # generate_html(server_statuses)
    return server_statuses

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

def gui(serversFile):
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    app = customtkinter.CTk()
    app.geometry("800x600")
    app.title("Server Monitor")
    
    status_label = customtkinter.CTkLabel(app, text="Server status zal hier worden weergegeven")
    status_label.pack(pady=20)

    def update_status():
        server_statuses = check(serversFile)
        status_text = "\n".join([f"{server['name']} - {server['ip']}: {server['status']}" for server in server_statuses])
        status_label.configure(text=status_text if status_text else "Geen servers gevonden")

    button = customtkinter.CTkButton(app, text="Ping Servers", command=update_status)
    button.pack(padx=20, pady=20)

    app.mainloop()

# def generate_html(server_statuses):
#     html_content = """
#     <html>
#         <head>
#             <title>Server Status</title>
#         </head>
#         <body>
#             <h1>Server Status</h1>
#             <p>Generated at: {generated_at}</p>
#             <table>
#                 <tr>
#                     <th>Name</th>
#                     <th>IP</th>
#                     <th>Status</th>
#                 </tr>
#                 {rows}
#             </table>
#         </body>
#     </html>
#     """
#     rows = ""
#     for server in server_statuses:
#         row = f"<tr><td>{server['name']}</td><td>{server['ip']}</td><td>{server['status']}</td></tr>"
#         rows += row
#
#     html_content = html_content.format(generated_at=datetime.datetime.now().strftime("%H:%M %d/%m/%Y"), rows=rows)
#
#     with open("index.html", "w") as file:
#         file.write(html_content)

def main():
    serversFile = "servers.json"
    if len(sys.argv) < 2:
        print("Usage: python main.py [terminal|check|gui]")
        return
    elif sys.argv[1] == "terminal":
        init()
        terminal(serversFile)
    elif sys.argv[1] == "check":
        init()
        check(serversFile)
    elif sys.argv[1] == "gui":
        gui(serversFile)
    else:
        print("Invalid option")
        print("Usage: python main.py [terminal|check]")
        return

if __name__ == "__main__":
    main()
