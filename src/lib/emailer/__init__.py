import smtplib, ssl
import helpers.crypto as crypto

class Emailer():
    
    def __init__(self, user, server, *args, **kwargs):
        self.sender = {
            "email": user["email"],
            "password": user["password"]
        }

        self.server = server

        self.initSMTP()
        
    def initSMTP(self):
        context = ssl.create_default_context()
        host = self.server["host"]
        port = self.server["port"]

        try: 
            self.server = smtplib.SMTP(host, port)
            self.server.starttls(context=context)
            self.server.login(self.sender["email"], crypto.decode(self.sender["password"]))
            print(self.server)
        except Exception as e:
            print(e)
