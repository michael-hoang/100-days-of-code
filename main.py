import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options


class InternetSpeedTwitterBot:
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
            twitter_username,
            twitter_email,
            twitter_password
    ):
        """Initialize browser driver."""

        self.service = Service(driver_path)
        self.options = Options()
        self.options.add_experimental_option('detach', True)
        self.driver = webdriver.Edge(
            service=self.service, options=self.options
        )
        self.promised_down = promised_down
        self.promised_up = promised_up

        self.visit_website(twitter_login_url)
        time.sleep(3)
        self.log_in_website(twitter_email, twitter_password, twitter_username)

    def visit_website(self, url):
        """Visit the website URL using Selenium webdriver."""
        self.driver.get(url)

    def _check_for_unusual_login_activity(self, login_username, login_password) -> bool:
        """
        Resolve any unusual login activity. Return True if unusual login was detected.
        """
        try:
            verification = self.driver.find_element(
                By.XPATH, '//*[ text() = "Phone or username"]'
            )
            if verification:
                phone_username_input = self.driver.find_element(
                    By.CSS_SELECTOR, 'input'
                )
                phone_username_input.send_keys(login_username)
                next_btn = self.driver.find_element(
                    By.XPATH, '//*[ text() = "Next" ]'
                )
                next_btn.click()
                time.sleep(2)
                password_input = self.driver.find_element(
                    By.CSS_SELECTOR, 'input[name="password"]'
                )
                password_input.send_keys(login_password)
                login_btn = self.driver.find_element(
                    By.XPATH, '//*[ text() = "Log in" ]'
                )
                login_btn.click()
        except NoSuchElementException:
            return False

    def log_in_website(self, login_handle, login_password, login_username):
        """Log in to the website."""
        login_handle_input = self.driver.find_element(By.CSS_SELECTOR, 'input')
        login_handle_input.send_keys(login_handle)
        next_btn = self.driver.find_element(By.XPATH, '//*[ text() = "Next" ]')
        next_btn.click()
        time.sleep(2)
        if not self._check_for_unusual_login_activity(login_username, login_password):
            password_input = self.driver.find_element(
                By.CSS_SELECTOR, 'input[name="password"]'
            )
            password_input.send_keys(login_password)
            login_btn = self.driver.find_element(
                By.XPATH, '//*[ text() = "Log in" ]'
            )
            login_btn.click()


if __name__ == '__main__':
    # Load environment variables from .env file
    load_dotenv()

    # Get environment variables
    TWITTER_EMAIL = os.getenv('EMAIL')
    TWITTER_PASSWORD = os.getenv('PASSWORD')
    TWITTER_USERNAME = os.getenv('TWITTER_USERNAME')

    WEBDRIVER_PATH = r'C:\Users\Mike\OneDrive\Desktop\edgedriver_win64\msedgedriver.exe'
    TWITTER_LOGIN_URL = 'https://twitter.com/login'
    PROMISED_DOWN = 150  # Mbps download
    PROMISED_UP = 10  # Mbps upload

    tcp = InternetSpeedTwitterBot(
        promised_down=PROMISED_DOWN,
        promised_up=PROMISED_UP,
        driver_path=WEBDRIVER_PATH,
        twitter_login_url=TWITTER_LOGIN_URL,
        twitter_username=TWITTER_USERNAME,
        twitter_email=TWITTER_EMAIL,
        twitter_password=TWITTER_PASSWORD
    )
