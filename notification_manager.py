import requests
import smtplib


BOT_TOKEN = 'yourTelegramBotToken'  # Telegram
BOT_CHAT_ID = 'yourBotChatID'  # Telegram
MY_EMAIL = 'yourEmail@gmail.com'
MY_PASSWORD = 'yourPassword'  # Gmail


class NotificationManager:
    """This class is responsible for sending notifications with the deal flight details."""

    def telegram_bot_sendtext(self, bot_message):
        """Sends Telegram message"""
        api_endpoint = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
        params = {
            'chat_id': BOT_CHAT_ID,
            'parse_mode': 'Markdown',
            'text': bot_message,
        }
        response = requests.get(url=api_endpoint, params=params)

        # return response.json()

    def send_email(self, email_address, email_message):
        """Sends email message."""
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=email_address,
                                msg=email_message)


if __name__ == '__main__':
    nm = NotificationManager()
    nm.telegram_bot_sendtext(bot_message='test')
