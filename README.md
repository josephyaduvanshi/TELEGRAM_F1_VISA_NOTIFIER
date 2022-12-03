# TELEGRAM_F1_VISA_NOTIFIER
A simple python script to notify you directly to your email and phone when the F1 visa appointment slots are available.
You can set the date range and the script will notify you when the slots are available for the dates in the range.
I hope this helps you to get your visa appointment as soon as possible. Good luck!

I have used multiple packages for this project.

#### The packages are:
1. Telethon
2. Twilio
3. Mailgun
4. Mailjet

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required packages.

```bash
pip install -r requirements.txt
```

## REQUIREMENTS
1. Create a telegram account and join the group.
2. Create a telegram app and get the api_id and api_hash.
3. Create a twilio account and get the account_sid and auth_token.
4. Create a mailgun account and get the api_key and domain.
5. Create a mailjet account and get the api_key and api_secret.
6. Create a .env file and add the following variables.
    1. TELEGRAM_API_ID
    2. TELEGRAM_API_HASH
    3. TELEGRAM_PHONE_NUMBER
    4. TWILIO_ACCOUNT_SID
    5. TWILIO_AUTH_TOKEN
    6. TWILIO_PHONE_NUMBER
    7. MAILGUN_API_KEY
    8. MAILGUN_DOMAIN
    9. MAILJET_API_KEY
    10. MAILJET_API_SECRET


## Usage
    
    ```python
    python main.py
    ```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License
[APACHE 2.0](https://www.apache.org/licenses/LICENSE-2.0)

## Disclaimer
This is for educational purposes only. I am not responsible for any misuse of this script.

## Contact
If you have any questions, please contact me at [josefyaduvanshi@gmail.com](mailto:)
