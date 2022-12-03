from mailjet_rest import Client
from constants import Constants

api_key = '{}'.format(Constants.MAILJET_PUBLIC_API_KEY)
api_secret = '{}'.format(Constants.MAILJET_SECRET_API_KEY)
mailjet = Client(auth=(api_key, api_secret), version='v3.1')


def send_email_message(message: str, email: str):
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
    result = mailjet.send.create(data=data)
    return result.json()
