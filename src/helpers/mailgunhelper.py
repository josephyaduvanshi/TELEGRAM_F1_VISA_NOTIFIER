import requests
from src.Constants.constants import Constants


class MailgunHelper:
    @staticmethod
    def send_simple_message(message):
        """
        It sends an email to the email address specified in the Constants.py file
        
        param message: The message you want to send
        """
        res = requests.post(
            "https://api.mailgun.net/v3/{}/messages".format(Constants.MAILGUN_DOMAIN),
            auth=("api", "{}".format(Constants.MAILGUN_AUTH_API_KEY)),
            data={"from": f"VISA NOTIFIER <visanotifier@{Constants.MAILGUN_DOMAIN}>",
                  "to": "{}".format(Constants.PERSONAL_EMAIL),
                  "subject": f"VISA DATE ALERT!! {message}!!",
                  "text": f"The available visa date is {message}"})
        print(res.text)
