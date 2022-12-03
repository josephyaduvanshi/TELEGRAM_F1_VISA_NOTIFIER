import requests
from constants import Constants


class MailgunHelper:
    @staticmethod
    def send_simple_message(message):
        res = requests.post(
            "https://api.mailgun.net/v3/{}/messages".format(Constants.MAILGUN_DOMAIN),
            auth=("api", "{}".format(Constants.MAILGUN_AUTH_API_KEY)),
            data={"from": f"VISA NOTIFIER <visanotifier@{Constants.MAILGUN_DOMAIN}>",
                  "to": "{}".format(Constants.PERSONAL_EMAIL),
                  "subject": f"VISA DATE ALERT!! {message}!!",
                  "text": f"The available visa date is {message}"})
        print(res.text)
