from lib.cli import CLI
from lib.emailer import Emailer
from lib.inputs import Input
from lib.template import Template
from settings import ATTACHMENTS_DIR, TEMPLATES_DIR
import sys

# create cli instance
cli = CLI(
    prepand = "-->"
)
Field = Input()

# help command
@cli.command("help", "shows this help legend")
def help(self, *args, **kwargs):
    print("\n")

    for command in self.commands:
        print(f"{command['name']} - {command['description']}")

    print("\n")

# exit command
@cli.command("exit", "exits CLI")
def exit(self, *args, **kwargs):
    agreement = input("Are you sure you want to leave (Y/N): ")

    if agreement.lower() == "n":
        return
    else: 
        sys.exit(1)

@cli.command("send email", "send simple email from cli")
def send_email(self, *args, **kwargs):
    recivers = Field.EmailList("email příjemců (oddělené čárkou): ", True)
    subject = Field.Text("předmět: ", True)
    body = Field.Text("obsah: ", False)
    html = Field.Path("html šablona: ", False, TEMPLATES_DIR)
    attachments = Field.PathList("přílohy (oddělené čárkou): ", False, ATTACHMENTS_DIR)
    
    Email = Emailer()
    Email.to(recivers).subject(subject).body(body).html(html).attach(attachments).send()  
    
if __name__ == "__main__":
    cli.run()