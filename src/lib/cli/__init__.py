import helpers.crypto as crypto
import sys

class CLI:
    def __init__(self, prepand, *args, **kwargs):
        self.prepand = prepand
        self.commands = []
        self.user = {}

    def command(self, name, description = "---", *args, **kwargs):
        def wrapper(func):

            func.command = {
                "name": name.strip().replace(" ", "-"),
                "shortcut": "",
                "description": description,
                "function": func
            }

            self.commands.append(func.command)

            return func

        return wrapper

    def option(self, *args, **kwargs):
        def wrapper(func):

            print(func)

            return func
        return wrapper

    def authorize(self, email, password):
        self.user = {
            "email": email,
            "password": crypto.encode(password)
        }

        return self.user
        
    
    def notFound(self, cmd):
        commonCommand = ""

        for command in self.commands:
            if cmd in command["name"]:
                commonCommand+=command["name"] + " "

        print(f"'{cmd}' does not exist, do you mean: {commonCommand}?")
        self.run()

    def run(self):
        cmd = input(f"{self.prepand} ")

        for command in self.commands:
            if command["name"] == cmd:
                command["function"](self)
                self.run()
                return

        self.notFound(cmd)  