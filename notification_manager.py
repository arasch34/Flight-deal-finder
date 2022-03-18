# This class is responsible for sending notifications with the deal flight details.
from twilio.rest import Client
import os

TWILIO_SID = "AC7a83e6e7597d979c5cdeccad642232ba"
TWILIO_AUTH_TOKEN = "42561089ffad410aaa22beb90a3e98e6"
TWILIO_VIRTUAL_NUMBER = "+16106326185"
TWILIO_VERIFIED_NUMBER = os.environ["VERIFIED_NUMBER"]


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )


