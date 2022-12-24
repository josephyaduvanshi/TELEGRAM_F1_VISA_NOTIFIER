from twilio.rest import Client
from constants import Constants

# Creating a client object which is used to send messages.
account_sid = Constants.TWILIO_ACCOUNT_SID
auth_token = Constants.TWILIO_AUTH_TOKEN
client = Client(account_sid, auth_token)


def send_sms_me(message: str):
    """
    It sends a message to my personal number
    
    param message: The message you want to send
    type message: str
    return: The message object is being returned.
    """
    message = client.messages.create(
        messaging_service_sid=Constants.TWILIO_MESSAGE_SERVICE_SID,
        body='DATE AVAILABLE{}'.format(message),
        to='+977{}'.format(Constants.PERSONAL_NUMBER)
    )
    return message


def send_sms(message: str, number: str):
    """
    It takes a message and a number as arguments and sends an SMS to the number with the message
    
    param message: The message you want to send
    type message: str
    param number: The phone number you want to send the message to
    type number: str
    return: The message object is being returned.
    """
    message = client.messages.create(
        messaging_service_sid=Constants.TWILIO_MESSAGE_SERVICE_SID,
        body='DATE AVAILABLE{}'.format(message),
        to='+977{}'.format(number)
    )
    return message
