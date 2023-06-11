##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import pandas as pd
import datetime as dt
import random
import os
from os.path import isfile, join
import smtplib

LETTER_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'letter_templates'))

sender = 'yourEmail@email.com'
my_password = 'yourPassword'

letters = [file for file in os.listdir(LETTER_PATH) if isfile(join(LETTER_PATH, file))]

current_date = dt.datetime.now()
current_month = current_date.month
current_day = current_date.day

df = pd.read_csv(filepath_or_buffer='birthdays.csv')
people = [row[1] for row in df.iterrows()]
bday_ppl = [person for person in people if person['month'] == current_month and person['day'] == current_day]

for person in bday_ppl:
    name = person['name']
    receiver = person['email']
    random_letter = random.choice(letters)
    abs_path = f"{LETTER_PATH}\{random_letter}"
    with open(file=abs_path, mode='r') as f:
        template = f.read()
        message = template.replace('[NAME]', name)

    with smtplib.SMTP(host='smtp.gmail.com') as connection:
        connection.ehlo()
        connection.starttls()
        connection.ehlo()
        connection.login(user=sender, password=my_password)
        connection.sendmail(from_addr=sender,
                            to_addrs=receiver,
                            msg=f"Subject: Happy Birthday!\n\n{message}")
