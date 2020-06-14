# This service emails whatever it gets back from the selector service
from selector_service import SelectorService
import smtplib
from email.message import EmailMessage

select = SelectorService()

select.read_json_data()
selected_entries = select.select_random_entries()

msg = EmailMessage()
msg['Subject'] = 'Your Highlights and Notes for today'
msg['From'] = "ankifunkey@gmail.com"
msg['To'] = "ankifunkey@gmail.com"


def get_content_of_the_email():
    content = ''
    for item_index in range(len(selected_entries)):
        item = "DATE-ADDED: " + selected_entries[item_index]['date_added']
        content = content + item + "\n"
        item = "HIGHLIGHT: " + selected_entries[item_index]['highlight']
        content = content + item + "\n"
        item = "TITLE: " + selected_entries[item_index]['title']
        content = content + item + "\n"
        item = "CHAPTER: " + selected_entries[item_index]['chapter']
        content = content + item + "\n"
        item = "SOURCE: " + selected_entries[item_index]['source']
        content = content + item + "\n"
        item = "PAGE-NUMBER: " + selected_entries[item_index]['page_number']
        content = content + item + "\n" + "------------" + "\n"
    return content


content = get_content_of_the_email()
msg.set_content(content)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

    smtp.login("ankifunkey@gmail.com", 'ONSConatE')

    smtp.send_message(msg)





