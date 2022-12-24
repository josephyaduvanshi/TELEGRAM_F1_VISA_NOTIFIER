from telethon import TelegramClient, events

from src.Constants.constants import Constants
from src.helpers.csv_helper import CSVHelper
from src.helpers.mailgunhelper import MailgunHelper
from src.helpers.mailjet_helper import send_email_message
from src.helpers.telegram_helper import TelegramHelper
from src.helpers.twilio_sms_helper import send_sms, send_sms_me

# Creating a client to connect to the telegram server.
api_id = int(Constants.TELEGRAM_APP_ID)
api_hash = Constants.TELEGRAM_API_HASH
client = TelegramClient('visanotifier', api_id, api_hash)
print(client)

# A list of months that the bot will look for in the chat.
"""USVN GROUP CHAT ID"""
chat_ids = [-1001567966058]

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

"""It listens for new messages in the chat_ids list, and if the message contains a month in the months
    list, it sends a message to the Telegram group, sends an SMS to me, sends an email to me, sends an
    SMS to the numbers in the CSV file, and sends an email to the emails in the CSV file

    param event: The event that triggered the handler function"""


@client.on(events.NewMessage(chats=chat_ids))
async def newMessageListener(event):
    newMessage = event.message.message
    print(newMessage)
    for month in months:
        if month.lower() in newMessage.lower():
            TelegramHelper.send_message(f"Date available: {newMessage}")
    if newMessage.__str__().lower().__contains__("dec") or newMessage.__str__().lower().__contains__(
            "jan") or newMessage.__str__().lower().__contains__("nov"):
        send_sms_me(f"Date available: {newMessage}")
        MailgunHelper.send_simple_message(newMessage)
        TelegramHelper.send_message_private(newMessage)
        important_numbers = CSVHelper.read_csv_email_number()[1]
        important_emails = CSVHelper.read_csv_email_number()[0]
        for number in important_numbers:
            send_sms(newMessage, number)
        for email in important_emails:
            send_email_message(message=newMessage, email=email)
        print("Date available: " + newMessage)


# A context manager that ensures that the client is disconnected when the program is done.
with client:
    client.run_until_disconnected()
