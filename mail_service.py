# This service emails whatever it gets back from the selector service
from selector_service import SelectorService
import smtplib
from email.message import EmailMessage


class MailerService:
    def __init__(self):
        self.sample_entries = SelectorService().select_random_entries()
        self.msg = EmailMessage()
        self.content = None

    def define_email_parameters(self):
        self.msg['Subject'] = 'Your Highlights and Notes for today'
        self.msg['From'] = "ankifunkey@gmail.com"
        self.msg['To'] = ["ankifunkey@gmail.com", "shikha.bansal228@gmail.com"]

    def email_content(self):
        content = ''
        for item_index in range(len(self.sample_entries)):
            item = "DATE-ADDED: " + self.sample_entries[item_index]['date_added']
            content = content + item + "\n"
            item = "HIGHLIGHT: " + self.sample_entries[item_index]['highlight']
            content = content + item + "\n"
            item = "TITLE: " + self.sample_entries[item_index]['title']
            content = content + item + "\n"
            item = "CHAPTER: " + self.sample_entries[item_index]['chapter']
            content = content + item + "\n"
            item = "SOURCE: " + self.sample_entries[item_index]['source']
            content = content + item + "\n"
            item = "PAGE-NUMBER: " + self.sample_entries[item_index]['page_number']
            content = content + item + "\n" + "------------" + "\n"
        self.content = content
        return self.content

    def send_email(self):
        self.msg.set_content(self.content)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login("ankifunkey@gmail.com", 'ONSConatE')
            smtp.send_message(self.msg)
        return True

    def run_mailer(self):
        self.define_email_parameters()
        self.email_content()
        self.send_email()


def run_job():
    composed_email = MailerService()
    composed_email.run_mailer()


run_job()




