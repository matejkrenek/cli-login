import helpers.crypto as crypto
import sys

class CLI:
    def __init__(self, prepand, *args, **kwargs):
        self.prepand = prepand
        self.commands = []

    def command(self, name, description = "---", *args, **kwargs):
        def wrapper(func):

            print("command")

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
        print(f"'{cmd}' does not exist")
        self.run()

    def run(self):
        cmd = input(f"{self.prepand} ")

        for command in self.commands:
            if command["name"] == cmd:
                command["function"](self)
                self.run()
                return

        self.notFound(cmd)  