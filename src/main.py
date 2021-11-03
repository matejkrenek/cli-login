from lib.cli import CLI
from lib.emailer import Emailer
from lib.inputs import Input
import sys, smtplib, ssl, getpass
from settings import EMAILER

# create cli instance
cli = CLI(
    prepand = "-->"
)
emailer = Emailer(EMAILER["MIDDLEMAN"], EMAILER["SERVER"])
inputField = Input()

# help command
@cli.command("--help", "shows this help legend")
def help(self, *args, **kwargs):
    print("\n")

    for command in self.commands:
        print(f"{command['name']} \t\t\t {command['description']}")

    print("\n")

# exit command
@cli.command("--exit", "exists CLI")
def exit(self, *args, **kwargs):
    agreement = input("Are you sure you want to leave (Y/N): ")

    if agreement.lower() == "n":
        return
    else: 
        sys.exit(1)

@cli.command("send_email", "send simple email from cli")
def send_email(self, *args, **kwargs):
    recivers = inputField.EmailList("prijemci(oddelene čárkou): ", True)
    subject = inputField.Text("predmet: ", True)
    body = inputField.Text("obsah: ", False)
    template = inputField.Path("cesta html sablony: ", False)
    attachments = inputField.PathList("prilohy: ", False)

    print(recivers, subject, body, template, attachments)
        

if __name__ == "__main__":
    # run cli
    cli.run()