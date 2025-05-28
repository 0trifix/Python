import os

class Logger:
    def __init__(self):
        import datetime
        if not os.path.exists("logs"):
            os.makedirs("logs")
        self.log_file = f"logs/{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_log.txt"
        self.logs = []

    def log(self, bericht):
        import datetime
        tijd = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        regel = f"{tijd} - {bericht}"
        self.logs.append(regel)
        with open(self.log_file, "a") as f:
            f.write(regel + "\n")

    def get_logs(self):
        return "\n".join(self.logs)
