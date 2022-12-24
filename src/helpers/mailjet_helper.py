# Importing the Client class from the mailjet_rest module and the Constants class from the constants.py file.
# module.
from mailjet_rest import Client
from constants import Constants

# Creating a mailjet client object.
api_key = '{}'.format(Constants.MAILJET_PUBLIC_API_KEY)
api_secret = '{}'.format(Constants.MAILJET_SECRET_API_KEY)
mailjet = Client(auth=(api_key, api_secret), version='v3.1')


def send_email_message(message: str, email: str):
    """
    It sends an email message to the specified email address
    
    param message: The message you want to send
    type message: str
    param email: The email address to send the message to
    type email: str
    """
    # Creating a dictionary with the message to be sent.
    data = {
        'Messages': [
            {
                "From": {
                    "Email": "{}".format(Constants.FROM_EMAIL),
                    "Name": "VISA NOTIFIER"
                },
                "To": [
                    {
                        "Email": email,
                        "Name": "VISA NOTIFIER"
                    },
                ],
                "Cc": [
                    {
                        "Email": "copilot@mailjet.com",
                        "Name": "VISA NOTIFIER"
                    }
                ],
                "Bcc": [
                    {
                        "Email": "air-traffic-control@mailjet.com",
                        "Name": "VISA NOTIFIER"
                    }
                ],
                "Subject": "VISA DATE ALERT!!",
                "TextPart": f"The available visa date is {message}",
            }
        ]
    }
    # Sending the email.
    result = mailjet.send.create(data=data)
    return result.json()
