from twilio.rest import Client
from constants import Constants

account_sid = Constants.TWILIO_ACCOUNT_SID
auth_token = Constants.TWILIO_AUTH_TOKEN
client = Client(account_sid, auth_token)


def send_sms_me(message: str):
    message = client.messages.create(
        messaging_service_sid=Constants.TWILIO_MESSAGE_SERVICE_SID,
        body='DATE AVAILABLE{}'.format(message),
        to='+977{}'.format(Constants.PERSONAL_NUMBER)
    )
    return message


def send_sms(message: str, number: str):
    message = client.messages.create(
        messaging_service_sid=Constants.TWILIO_MESSAGE_SERVICE_SID,
        body='DATE AVAILABLE{}'.format(message),
        to='+977{}'.format(number)
    )
    return message
