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


class InternetSpeedTwitterBot:
    """
    A class representing a Twitter bot that complains to the user's ISP on
    Twitter if the user's current internet speed doesn't match at least the
    internet speed guaranteed by the ISP.
    """

    def __init__(self, driver_path, promised_down, promised_up):
        """Initialize browser driver."""
        self.service = Service(driver_path)
        self.options = Options()
        self.options.add_experimental_option('detach', True)
        self.driver = webdriver.Edge(
            service=self.service, options=self.options
        )
        self.down = promised_down
        self.up = promised_up

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

        return True

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

    def skip_turn_on_notifications(self):
        """Select 'Skip for now' if prompted to turn on notifications."""
        try:
            skip_btn = self.driver.find_element(
                By.XPATH, '//*[ text() = "Skip for now"]'
            )
            skip_btn.click()
        except NoSuchElementException:
            return

    def get_internet_speed(self):
        """
        Run internet speed test and return a tuple containing the download and upload speeds.
        """
        self.visit_website('https://www.speedtest.net/')
        go_btn = self.driver.find_element(
            By.CSS_SELECTOR, 'span.start-text'
        )
        time.sleep(2)
        go_btn.click()

        WebDriverWait(self.driver, 120).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'div.audience-survey')
            )
        )

        dl_speed = self.driver.find_element(
            By.CSS_SELECTOR, 'span.download-speed'
        ).text
        ul_speed = self.driver.find_element(
            By.CSS_SELECTOR, 'span.upload-speed'
        ).text

        return float(dl_speed), float(ul_speed)

    def tweet_at_provider(self, dl_speed, ul_speed):
        header_ele = self.driver.find_element(By.CSS_SELECTOR, 'header')
        tweet_btn = header_ele.find_element(
            By.XPATH, '//*[ text() = "Tweet"]'
        )
        tweet_btn.click()
        time.sleep(2)
        tweet = f'Hey Internet Provider, why is my internet speed {dl_speed}down/{ul_speed}up when I pay for {self.down}down/{self.up}up? (Day 51 of 100 Days of Code)'
        focused_element = self.driver.switch_to.active_element
        focused_element.send_keys(tweet)
        tweet_btn = header_ele.find_element(
            By.XPATH, '//*[ text() = "Tweet"]'
        )
        tweet_btn.click()


if __name__ == '__main__':
    # Load environment variables from .env file
    load_dotenv()

    # Get environment variables
    TWITTER_EMAIL = os.getenv('EMAIL')
    TWITTER_PASSWORD = os.getenv('PASSWORD')
    TWITTER_USERNAME = os.getenv('TWITTER_USERNAME')

    WEBDRIVER_PATH = r'C:\Users\Mike\OneDrive\Desktop\edgedriver_win64\msedgedriver.exe'
    TWITTER_LOGIN_URL = 'https://twitter.com/login'
    PROMISED_DOWN = 100  # Mbps download
    PROMISED_UP = 25  # Mbps upload

    tbot = InternetSpeedTwitterBot(
        driver_path=WEBDRIVER_PATH,
        promised_down=PROMISED_DOWN,
        promised_up=PROMISED_UP
    )
    dl_speed, ul_speed = tbot.get_internet_speed()
    if dl_speed < PROMISED_DOWN or ul_speed < PROMISED_UP:
        tbot.visit_website(TWITTER_LOGIN_URL)
        time.sleep(2)
        tbot.log_in_website(TWITTER_EMAIL, TWITTER_PASSWORD, TWITTER_USERNAME)
        time.sleep(2)
        tbot.skip_turn_on_notifications
        time.sleep(2)
        tbot.tweet_at_provider(dl_speed, ul_speed)
