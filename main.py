import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options


class TwitterComplaintBot:
    """
    A class representing a Twitter bot that complains to the user's ISP on
    Twitter if the user's current internet speed doesn't match at least the
    internet speed guaranteed by the ISP.
    """

    def __init__(
            self,
            promised_down,
            promised_up,
            driver_path,
            twitter_login_url,
            twitter_email,
            twitter_password
    ):
        """Initialize browser driver."""

        self.service = Service(driver_path)
        self.options = Options()
        self.driver = webdriver.Edge(
            service=self.service, options=self.options
        )


if __name__ == '__main__':
    # Load environment variables from .env file
    load_dotenv()

    # Get environment variables
    TWITTER_EMAIL = os.getenv('EMAIL')
    TWITTER_PASSWORD = os.getenv('PASSWORD')

    WEBDRIVER_PATH = r'C:\Users\Mike\OneDrive\Desktop\edgedriver_win64\msedgedriver.exe'
    TWITTER_LOGIN_URL = 'https://twitter.com/login'

    tcp = TwitterComplaintBot
