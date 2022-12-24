import os

from dotenv import load_dotenv

# It's loading the environment variables from the `.env` file.
load_dotenv()


# It's a class that contains all the constants that are used in the project
# > The Constants class is a container for all the constants used in the program
class Constants:
    main_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_BOT_TOKEN_PRIVATE = os.getenv("TELEGRAM_BOT_TOKEN_PRIVATE")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
    TELEGRAM_URL = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    TELEGRAM_URL_PRIVATE = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN_PRIVATE}/sendMessage'
    TELEGRAM_APP_ID = os.getenv("TELEGRAM_APP_ID")
    TELEGRAM_API_HASH = os.getenv("TELEGRAM_API_HASH")
    MAILGUN_PUBLIC_API_KEY = os.getenv("MAILGUN_PUBLIC_API_KEY")
    MAILGUN_AUTH_API_KEY = os.getenv("MAILGUN_AUTH_API_KEY")
    MAILGUN_DOMAIN = os.getenv("MAILGUN_DOMAIN")
    MAILGUN_PRIVATE_API_KEY = os.getenv("MAILGUN_PRIVATE_API_KEY")
    MAILJET_PUBLIC_API_KEY = os.getenv("MAILJET_PUBLIC_API_KEY")
    MAILJET_SECRET_API_KEY = os.getenv("MAILJET_SECRET_API_KEY")
    FROM_EMAIL = os.getenv("FROM_EMAIL")
    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
    PERSONAL_NUMBER = os.getenv("PERSONAL_NUMBER")
    PERSONAL_EMAIL = os.getenv("PERSONAL_EMAIL")
    TWILIO_MESSAGE_SERVICE_SID = os.getenv("TWILIO_MESSAGE_SERVICE_SID")
