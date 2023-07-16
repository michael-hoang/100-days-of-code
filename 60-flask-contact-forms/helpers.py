import smtplib


def send_gmail(user_email: str, user_pw: str, message: str):
    """Send Gmail message with the provided login and message."""
    with smtplib.SMTP(host="smtp.gmail.com") as connection:
        connection.ehlo()
        connection.starttls()
        connection.ehlo
        connection.login(user=user_email, password=user_pw)
        connection.sendmail(from_addr=user_email, to_addrs=user_email, msg=message)
