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


    def login(self):

        print(self.server)
        print(self.sender)

    # def storage(self):
    #     smtp_server = "smtp.gmail.com"
    #     port = 587  # For starttls
    #     sender_email = "matejkrenek.spam@gmail.com"
    #     receiver_email = "jindra.machka@gmail.com"
    #     password = getpass.getpass("password: ")
    #     message = input("Message: ")

    #     context = ssl.create_default_context()

    #     try:
    #         server = smtplib.SMTP(smtp_server,port)
    #         server.ehlo()
    #         server.starttls(context=context)
    #         server.ehlo()
    #         server.login(sender_email, password)
    #         server.sendmail(sender_email, receiver_email, message)
    #     except Exception as e:
    #         print(e)
    #     finally:
    #         server.quit()
    #     print("You are login")

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
