from lib.cli import CLI
import sys

cli = CLI(
    prepand = "-->"
)

@cli.command("--help", "testing command")
@cli.option("-f", "--filter", choices={"pepa", "vojta"})
def help(self, *args, **kwargs):
    print("\n")

    for command in self.commands:
        print(f"{command['name']} \t\t\t {command['description']}")

    print("\n")

@cli.command("--exit", "exit command")
def exit(self, *args, **kwargs):
    sys.exit(1)

if __name__ == "__main__":
    cli.run()