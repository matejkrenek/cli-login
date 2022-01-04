from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import smtplib
import os
import sys

from lib.template import Template
from settings import EMAILER, STATUS, ATTACHMENTS_DIR

class Emailer():
    recivers = []
    attachments = []
    subject = "no subject"
    body = "no body"
    
    def __init__(self, user = EMAILER["MIDDLEMAN"], server = EMAILER["SERVER"], *args, **kwargs):
        self.sender = {
            "email": user["email"],
            "password": user["password"]
        }

        self.server = server

    def to(self, emails):
        self.recivers = emails

        return self

    def html(self, html, context = None):
        self.html = html
        self.context = context

        return self

    def subject(self, subject):
        self.subject = subject

        return self

    def body(self, body):
        self.body = body

        return self

    def attach(self, attach = []):
        if len(attach[0]) > 0:
            self.attachments = attach

        return self

    def connect(self):
        host = self.server["host"]
        port = self.server["port"]
        
        try: 
            self.server = smtplib.SMTP_SSL(host, port)
            self.server.login(self.sender["email"], self.sender["password"])
        except smtplib.SMTPRecipientsRefused:
            sys.stdout.write('\r' + STATUS.error + f"Připojování k SMTP serveru selhalo" + "\033[0m")
        except Exception as e:
            sys.stdout.write('\r' + STATUS.error + f"Něco se pokazilo" + "\033[0m")

    def connectSendClose(self, msg):
        sys.stdout.write('\r' + STATUS.info + f"Připojování k SMTP serveru..." + "\033[0m")

        try: 
            self.server = smtplib.SMTP_SSL(self.server["host"], self.server["port"])
            self.server.login(self.sender["email"], self.sender["password"])
        except smtplib.SMTPRecipientsRefused:
            sys.stdout.write('\r' + STATUS.error + f"Připojování k SMTP serveru selhalo" + "\033[0m\n")
            return
        except smtplib.SMTPAuthenticationError:
            sys.stdout.write('\r' + STATUS.error + f"Nesprávé údaje                    " + "\033[0m\n")
            return
        except Exception as e:
            sys.stdout.write('\r' + STATUS.error + f"Něco se pokazilo                  " + "\033[0m\n")
            print(e)
            return

        sys.stdout.write('\r' + STATUS.info + f"Posílání...                  " + "\033[0m")
        self.server.sendmail(self.sender['email'], self.recivers, msg.as_string())
        sys.stdout.write('\r' + STATUS.success + f"Posláno                      " + "\033[0m\n")
        self.server.close()

    def send(self):
        msg = MIMEMultipart()
        msg['From'] = self.sender['email']
        msg['To'] = ', '.join(self.recivers)
        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.body, 'text'))

        if len(self.html) > 0:
            if not self.context:
                self.context = {
                    "sender": self.sender['email'],
                    "subject": self.subject,
                    "body": self.body,
                    "recivers": ', '.join(self.recivers),
                }
                msg.attach(MIMEText(Template(self.html, self.context).render(), 'html'))


        if len(self.attachments) > 0:
            for file in self.attachments:

                try:
                    with open(os.path.join(ATTACHMENTS_DIR, file), "rb") as f:
                        attach = MIMEApplication(f.read())

                        attach.add_header('Content-Disposition','attachment',filename=str(file))
                        msg.attach(attach)
                except FileNotFoundError:
                    print(STATUS.error + f"příloha {file} neexistuje v {ATTACHMENTS_DIR}" + "\033[0m")
                    return
                except:
                    print(STATUS.error + f"Něco se pokazilo" + "\033[0m")
                    return

        self.connectSendClose(msg)
