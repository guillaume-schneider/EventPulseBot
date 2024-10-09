import smtplib
from email.mime.text import MIMEText


def send_email_notification(email_receiver: str):
    msg = MIMEText('Un ticket est disponible sur Eventbrite.')
    msg['Subject'] = 'Ticket disponible'
    msg['From'] = 'eventpulsebot@gmail.com'
    msg['To'] = email_receiver

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('eventpulsebot@gmail.com', 'npih wiie fizf egmw')
        server.send_message(msg)
