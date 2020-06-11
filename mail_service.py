# This service emails whatever it gets back from the selector service
from selector_service import SelectorService
import smtplib
from email.message import EmailMessage

select = SelectorService(
    bucket='testing-correct-aws-account',
    key='sample_dataset.json')

select.read_json_data()
selected_entries = select.select_random_entries()
print(selected_entries)

msg = EmailMessage()
msg['Subject'] = 'Your Highlights and Notes for today'
msg['From'] = "ankifunkey@gmail.com"
msg['To'] = "ankifunkey@gmail.com"


msg.set_content(
    "Highlight: {} \n"
    "----------------- \n"
    "Date added: {} \n"
    "----------------- \n"
    "Book: {} \n"
    "----------------- \n"
    "Chapter: {} \n"
    "----------------- \n"
    "Page Number: {}".format(selected_entries['highlight'],
                             selected_entries['date_added'],
                             selected_entries['book'],
                             selected_entries['chapter'],
                             selected_entries['page_number'])
    )

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

    smtp.login("receiever-email", 'password')

    smtp.send_message(msg)





