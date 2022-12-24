# TELEGRAM F1 VISA NOTIFIER

## Telegram Channel

The script runs 24/7 on the Ubuntu server. You will never miss a date again.
You can also host yourself on your own server by following the instructions and setting the configurations.

**The channel is available at https://t.me/f1visadates**

Feel free to join and share with your friends.

<img width="595" alt="Screenshot 2022-12-24 at 5 55 38 PM" src="https://i.imgur.com/FC4hnho.png">

## Email Subscription

You can set the script to send an email when the desired date becomes accessible. Additionally, you can host yourself on
your own server by following the instructions and configuring the settings.

<img width="595" alt="Screenshot 2022-12-24 at 5 55 38 PM" src="https://i.imgur.com/dz61Xr9.png">

## Phone / Text Subscription

You can set the script to send a text message when the desired date becomes accessible. The script supports Twilio as of
now.

<img width="595" alt="Screenshot 2022-12-24 at 5 55 38 PM" src="https://i.imgur.com/MXx4sXG.jpg">

## Private Telegram Bot / Channel

You can set the script to send a message to your private telegram channel when the desired date becomes accessible.

<img width="595" alt="Screenshot 2022-12-24 at 5 55 38 PM" src="https://i.imgur.com/hqvfy3N.png">

## Introduction / Instructions

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
6. Create a .env file and add all the variables from the Constants file.

## Usage

    python main.py

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License

[APACHE 2.0](https://www.apache.org/licenses/LICENSE-2.0)

## Disclaimer

This is for educational purposes only. I am not responsible for any misuse of this script.

## Contact

If you have any questions, please contact me at [josefyaduvanshi@gmail.com](mailto:)
