from telethon import TelegramClient, events
from mailgunhelper import MailgunHelper
from telegram_helper import TelegramHelper
from twilio_sms_helper import send_sms, send_sms_me
from csv_helper import CSVHelper
from mailjet_helper import send_email_message
from constants import Constants

api_id = int(Constants.TELEGRAM_APP_ID)
api_hash = Constants.TELEGRAM_API_HASH
client = TelegramClient('visanotifier', api_id, api_hash)
print(client)

"""USVN GROUP CHAT ID"""
chat_ids = [-1001567966058]

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


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


with client:
    client.run_until_disconnected()
