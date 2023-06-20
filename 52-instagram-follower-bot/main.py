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

    def login(self, url, username, password):
        """Log in to Instagram."""
        self.driver.get(url)
        time.sleep(4)
        username_input = self.driver.find_element(By.NAME, 'username')
        username_input.send_keys(username)
        password_input = self.driver.find_element(By.NAME, 'password')
        password_input.send_keys(password)
        login_btn = self.driver.find_element(
            By.XPATH, '//*[@id="loginForm"]/div/div[3]/button'
        )
        login_btn.click()

    def check_turn_on_notifications(self):
        """Clear the Turn on Notifications window, if present."""
        try:
            not_now_btn = self.driver.find_element(
                By.XPATH, '//button[text()="Not Now"]'
            )
            print(not_now_btn)
        except NoSuchElementException:
            return
        else:
            not_now_btn.click()

    def find_followers(self):
        """Look for followers from another account."""
        search_btn = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_Em"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a')
        search_btn.click()

    def follow(self):
        """Follow the person's Instagram account."""


if __name__ == '__main__':
    # Load environment variables from .env file
    load_dotenv()

    # Get environment variables
    USERNAME = os.getenv('LOGIN_USERNAME')
    PASSWORD = os.getenv('PASSWORD')

    WEBDRIVER_PATH = r'C:\Users\Mike\OneDrive\Desktop\edgedriver_win64\msedgedriver.exe'
    URL = 'https://www.instagram.com/'
    SIMILAR_ACCOUNT = 'blackpinkofficial'

    bot = InstaFollower(
        driver_path=WEBDRIVER_PATH
    )
    bot.login(URL, USERNAME, PASSWORD)
    time.sleep(3)
    bot.check_turn_on_notifications()
