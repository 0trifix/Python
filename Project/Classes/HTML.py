import os, webbrowser

class HTML_Generator:
    def __init__(self) -> None:
        self.naam = "_sites/index.html"
        if not os.path.exists("_sites"):
            os.makedirs("_sites")
    def genereer_html(self, inhoud):
        with open(f"{self.naam}", "w") as f:
            f.write("<html>\n<head>\n<title>Smart Home Log</title>\n</head>\n<body>\n")
            f.write("<h1>Smart Home Simulatie</h1>\n")
            f.write("<pre>\n")
            f.write(inhoud)
            f.write("</pre>\n")
            f.write("</body>\n</html>")
        webbrowser.open(f"file://{os.path.realpath(self.naam)}", new=0)
