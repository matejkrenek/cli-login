import smtplib, ssl
import helpers.crypto as crypto
from settings import STATUS

class Emailer():
    
    def __init__(self, user, server, *args, **kwargs):
        self.sender = {
            "email": user["email"],
            "password": user["password"]
        }

        self.server = server

    def send(self, sender, recivers, subject = "", body = "", template = None, attachments = None):
        context = ssl.create_default_context()
        host = self.server["host"]
        port = self.server["port"]

        print(sender, recivers, body)
        
        try: 
            self.server = smtplib.SMTP(host, port)
            self.server.starttls(context=context)
            self.server.login(self.sender["email"], self.sender["password"])
            self.server.sendmail(self.sender["email"], recivers, body)    

            print(STATUS.success + "Email byl uspěšně odeslán" + "\033[0m")

        except Exception as e:
            print(STATUS.error + "Něco se pokazilo" + "\033[0m")
            print(e)