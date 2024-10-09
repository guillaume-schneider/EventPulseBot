import requests
from bs4 import BeautifulSoup

url = r"https://www.eventbrite.fr/checkout-external?eid=1002383194117&parent=https%3A%2F%2Fwww.eventbrite.fr%2Fe%2Fbillets-scientic-game-jam-2024-1002383194117%3Faff%3Doddtdtcreator&modal=1&aff=oddtdtcreator"


def check_ticket_availability():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    ticket_status = soup.find('div', {'class': 'ChoiceCard_root__fshrp ChoiceCard_disabled__fshrp TicketDisplayCardContentFullSize-module__card___2860Y eds-l-pad-bot-4 eds-l-mar-top-4 eds-l-pad-top-4 undefined'})

    if ticket_status:
        elements = ticket_status.find_all("span", class_="eds-stepper-total-quantity eds-stepper-quantity-initial-pos")

        for element in elements:
            quantity = element.text
    else:
        print("Élément indiquant la disponibilité des tickets non trouvé.")

    return quantity > 0
