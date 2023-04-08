import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options


class ExtendExpiryBot:
    def __init__(self, driver_path):
        """
        A class for automating expiry renewal on Pythonanywhere using Selenium.
        (Only for Edge browsers)

        Attributes:
            service (selenium.webdriver.service): Responsible for starting and 
                stoping web browser driver.
            options (seleniuim.webdriver.options): Determine various properties
                of the web browser driver.
            driver (selenium.webdriver): The web browser driver to use.
            website_url (str): The URL of the website to interact with
                (https://www.pythonanywhere.com/).

        Methods:
            __init__(self, driver, website_url):
                Constructs the ExtendExpiryBot object.
        """
        self.service = Service(driver_path)
        self.options = Options()
        self.options.add_experimental_option('detach', True)
        self.driver = webdriver.Edge(
            service=self.service, options=self.options
        )
        self.website_url = 'https://www.pythonanywhere.com/'

    def open_website(self):
        """Opens the website_url in the web browser."""
        self.driver.get(self.website_url)

    def go_to_login_page(self):
        """Navigate to the login page."""
        login = self.driver.find_element(By.LINK_TEXT, 'Log in')
        login.click()

    def sign_in(self, username: str, password: str):
        """Sign the user into the website."""
        username_input = self.driver.find_element(By.NAME, 'auth-username')
        username_input.send_keys(username)
        password_input = self.driver.find_element(By.NAME, 'auth-password')
        password_input.send_keys(password)
        login_btn = self.driver.find_element(By.ID, 'id_next')
        login_btn.click()


if __name__ == '__main__':
    # Load environment variables from .env file
    load_dotenv()

    # Get environment variables
    USER = os.environ.get('USER')
    PASSWORD = os.environ.get('PASSWORD')

    webdriver_path = r'C:\Users\Mike\OneDrive\Desktop\edgedriver_win64\msedgedriver.exe'
    exp_renewal_bot = ExtendExpiryBot(webdriver_path)
    exp_renewal_bot.open_website()
    time.sleep(2)
    exp_renewal_bot.go_to_login_page()
    time.sleep(2)
    exp_renewal_bot.sign_in(USER, PASSWORD)
