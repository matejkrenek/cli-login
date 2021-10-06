import sys

class CLI:
    def __init__(self, prepand, *args, **kwargs):
        self.prepand = prepand
        self.commands = []

    def command(self, name, description = "---", *args, **kwargs):
        def wrapper(func):

            func.command = {
                "name": name.strip().replace(" ", "-"),
                "shortcut": "",
                "description": description,
                "function": func
            }

            self.commands.append(func.command)

            print("idk:", func)

            return func
        return wrapper

    def option(self, *args, **kwargs):
        def wrapper(func):

            print(func)

            return func
        return wrapper
    
    def run(self):
        cmd = input(f"{self.prepand} ")

        for command in self.commands:
            if command["name"] == cmd:
                command["function"]()
                self.run()
                return

        sys.exit(1)