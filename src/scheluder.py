import time
from notification import send_email_notification
from scrapper import check_ticket_availability

while True:
    if check_ticket_availability():
        send_email_notification()
        break
    time.sleep(150)  # 3 minutes schelude
