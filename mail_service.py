# This service emails whatever it gets back from the selector service
from parse_content import ContentParser
import smtplib
from email.message import EmailMessage


class MailerService:
    def __init__(self):
        self.msg = EmailMessage()
        self.content = ContentParser().parse_selected_entries()

    def define_email_parameters(self):
        self.msg['Subject'] = 'Your Highlights and Notes for today'
        self.msg['From'] = "ankifunkey@gmail.com"
        self.msg['To'] = ["example@gmail.com"]

    def send_email(self):
        self.msg.set_content(self.content)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login("example@gmail.com", 'password')
            smtp.send_message(self.msg)
        return True

    def run_mailer(self):
        self.define_email_parameters()
        self.send_email()


def run_job():
    composed_email = MailerService()
    composed_email.run_mailer()


run_job()




