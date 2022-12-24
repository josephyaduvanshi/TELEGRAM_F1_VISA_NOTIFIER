import requests
from src.Constants.constants import Constants


class TelegramHelper:
    @staticmethod
    def send_message(message):
        """
        It sends a message to a telegram chat.
        
        param message: The message you want to send
        """
        txt = "ϟ-------<b>Visa Dates Update</b>-------ϟ\n\n" + f"<b>{message}</b>" + "\n\n<b>ϟ--------------END" \
                                                                                     "--------------ϟ</b> "
        response = requests.post(Constants.TELEGRAM_URL,
                                 json={"chat_id": f"{Constants.TELEGRAM_CHAT_ID}", "text": f"{txt}",
                                       "parse_mode": "HTML"})
        if response.status_code == 200:
            print("Message sent successfully(PUBLIC)")
        if response.status_code == 200:
            print("Message sent successfully(PUBLIC)")
        if response.status_code != 200:
            raise Exception("Telegram API Error")

    @staticmethod
    def send_message_private(message):
        """
        It sends a message to a private group.
        
        param message: The message you want to send
        """
        txt = "ϟ-------<b>Visa Dates Update</b>-------ϟ\n\n" + f"<b>{message}</b>" + "\n\n<b>ϟ--------------END" \
                                                                                     "--------------ϟ</b> "
        response = requests.post(Constants.TELEGRAM_URL_PRIVATE,
                                 json={"chat_id": "-1001446768426", "text": f"{txt}",
                                       "parse_mode": "HTML"})
        if response.status_code == 200:
            print("Message sent successfully(PUBLIC)")
        if response.status_code != 200:
            raise Exception("Telegram API Error")

# if __name__ == '__main__':
#     TelegramHelper.send_message_private("Test")
