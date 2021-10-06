from lib.cli import CLI
from lib.emailer import Emailer
import sys, smtplib, ssl, getpass
from settings import EMAILER

# create cli instance
cli = CLI(
    prepand = "-->"
)

# help command
@cli.command("--help", "testing command")
def help(self, *args, **kwargs):
    print("\n")

    for command in self.commands:
        print(f"{command['name']} \t\t\t {command['description']}")

    print("\n")

# exit command
@cli.command("--exit", "exit command")
def exit(self, *args, **kwargs):
    agreement = input("Are you sure you want to leave (Y/N): ")

    if agreement.lower() == "n":
        return
    else: 
        sys.exit(1)

@cli.command("login", "login to google")
def login(self, *args, **kwargs):
    email = input("Email: ")
    password = getpass.getpass("Password: ")
    
    user = cli.authorize(email, password)
    sender = Emailer(user, EMAILER["SERVER"])

if __name__ == "__main__":
    # run cli
    cli.run()