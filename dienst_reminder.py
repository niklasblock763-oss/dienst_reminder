import datetime
import requests
import os

def build_message(date):
    dienste = [
        "Küche & Altglas",
        "Bad",
        "Müll",
        "Staubsaugen",
        "Waschen & Treppenhaus"
    ]

    personen = [
        "Rick",
        "Lea",
        "Niklas",
        "Moritz",
        "Paddy"
    ]


    start_monat = datetime.date(2026, 4, 1)

    monate = (date.year - start_monat.year) * 12 + (date.month - start_monat.month)
    rotation = monate % len(personen) # 0

    verteilung = {}

    for i, dienst in enumerate(dienste): 
        person = personen[(i - rotation) % len(personen)] 
        verteilung[dienst] = person

    if date.day == 1:
        text = "Neuer Monatsdienstplan:\n\n"
    else:
        text = "Freitags‑Reminder:\n\n"

    for dienst, person in verteilung.items():
        text += f"{dienst} - {person}\n"

    return text


def send_telegram(message, TOKEN, CHAT_ID):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(url, data=data)


if __name__ == "__main__":
    TOKEN = os.environ["TOKEN"]
    CHAT_ID = os.environ["CHAT_ID"]

    today = datetime.date.today()

    if today.day == 1 or today.weekday() == 4:
        message = build_message(today)
        send_telegram(message, TOKEN, CHAT_ID)
