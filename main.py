#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

import requests
import datetime
import smtplib
# import tkinter as tk
import time

MY_LAT = 33.659485 # Your latitude
MY_LONG = -117.998802 # Your longitude
MY_EMAIL = 'yourEmail@gmail.com'
MY_PASSWORD = 'yourPassword'

#Your position is within +5 or -5 degrees of the ISS position.
def is_ISS_above():
    """
    Returns boolean value indicating if ISS is above your current position within +-5 degrees.
    """
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    global iss_latitude
    global iss_longitude
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # if (iss_latitude > MY_LAT - 5) and (iss_latitude < MY_LAT + 5) and \
    #     (iss_longitude > MY_LONG - 5) and (iss_longitude < MY_LONG + 5):
    #     return True

    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5):
        return True

def is_dark():
    """
    Returns boolean value indicating if it is currently dark outside.
    """
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    # sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    # sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # Calculate hour time difference between UTC and current time zone.
    delta_hour_t = datetime.datetime.utcnow().hour - datetime.datetime.now().hour
    sunrise = datetime.datetime.strptime(data["results"]["sunrise"], "%Y-%m-%dT%H:%M:%S%z")
    sunset = datetime.datetime.strptime(data["results"]["sunset"], "%Y-%m-%dT%H:%M:%S%z")
    sunrise -= datetime.timedelta(hours=delta_hour_t)
    sunset -= datetime.timedelta(hours=delta_hour_t)

    sunrise_hour = sunrise.hour # Hour attribute is within range(24).
    sunset_hour = sunset.hour
    current_hour = datetime.datetime.now().hour

    if (current_hour >= sunset_hour) or (current_hour <= sunrise_hour):
        return True

def ISS_Overhead_Notifier():
    """
    Main ISS Overhead Notifier App.
    """
    if is_dark() and is_ISS_above():
        message = f'Subject: [NOTIFICATION] ISS is close by!\n\nThis is a notification\
 from your ISS Overhead Notifier app informing you that the International\
 Space Station is right above you.\nYour coordinate: {MY_LAT, MY_LONG}\n\
ISS coordinate: {iss_latitude, iss_longitude}'

        with smtplib.SMTP(host='smtp.gmail.com') as connection:
            connection.ehlo()
            connection.starttls()
            connection.ehlo()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=message)

#     countdown_timer()

# def countdown_timer():
#     root.after(60_000, ISS_Overhead_Notifier)


# root = tk.Tk()
# root.withdraw()
# ISS_Overhead_Notifier()

# root.mainloop()

while True:
    time.sleep(60)
    ISS_Overhead_Notifier()
