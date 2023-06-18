import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class InstaFollower:
    """
    Instagram bot that follows other people's followers.
    """

    def __init__(self, driver_path):
        """Initialize browser driver."""
        self.service = Service(driver_path)
        self.options = Options()
        self.options.add_experimental_option('detach', True)
        self.driver = webdriver.Edge(
            service=self.service, options=self.options
        )

    def login(self, url):
        """Log in to Instagram."""
        self.driver.get(url)

    def find_followers(self):
        """Look for followers from another account."""

    def follow(self):
        """Follow the person's Instagram account."""


if __name__ == '__main__':
    # Load environment variables from .env file
    load_dotenv()

    # Get environment variables
    USERNAME = os.getenv('USERNAME')
    PASSWORD = os.getenv('PASSWORD')

    WEBDRIVER_PATH = r'C:\Users\Mike\OneDrive\Desktop\edgedriver_win64\msedgedriver.exe'
    URL = 'https://www.instagram.com/'
    SIMILAR_ACCOUNT = 'blackpinkofficial'

    bot = InstaFollower(
        driver_path=WEBDRIVER_PATH
    )
    bot.login(URL)
