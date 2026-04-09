import datetime
import requests
import os

def build_message():
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

    start_monat = datetime.date(2026, 1, 1)  # Start der Rotation
    heute = datetime.date.today()

    # Monate seit Start berechnen
    monate = (heute.year - start_monat.year) * 12 + (heute.month - start_monat.month)

    rotation = monate % len(personen)

    verteilung = {}

    for i, dienst in enumerate(dienste):
        person = personen[(i + rotation) % len(personen)]
        verteilung[dienst] = person

    text = "Dienstplan diesen Monat:\n\n"

    for dienst, person in verteilung.items():
        text += f"{dienst} - {person}\n"

    return text




def send_telegram(message,TOKEN,CHAT_ID):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    
    data = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(url, data=data)

if __name__ == "__main__":
    TOKEN = os.environ["TOKEN"]
    CHAT_ID = os.environ["CHAT_ID"]
    message = build_message()
    send_telegram(message, TOKEN, CHAT_ID)
