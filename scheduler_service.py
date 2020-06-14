# Scheduler code for sending emails on a schedule
import schedule
import time
from mail_service import MailerService



def job():
    # Send email with 3 messages here
    composed_email = MailerService()
    composed_email.run_mailer()

schedule.every().day.at("8:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

