import time
from notification import send_email_notification
from scrapper import check_ticket_availability


def schelude(emails):
    while True:
        if check_ticket_availability():
            for email in emails:
                send_email_notification(email)
            break
        time.sleep(150)  # 3 minutes schelude
