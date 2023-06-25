import os
import time

from bs4 import BeautifulSoup
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class EdgeBrowserBot:
    """
    A bot that controls Edge browser. It is capable of extracting fully dynamic
    HTML code, filling out Google forms, and exporting data to Google Sheets.
    """

    def __init__(self):
        self.driver = None

    def set_driver(self, driver_path: str):
        """Instantiate a Webdriver object from the driver_path."""
        service = Service(driver_path)
        options = Options()
        # Prevent bot detection on Chromium-based browsers
        options.add_argument("--disable-blink-features=AutomationControlled")
        # Keep browser open
        options.add_experimental_option("detach", True)
        try:
            self.driver = webdriver.Edge(service=service, options=options)
        except TypeError:
            print(
                "ERROR set_driver: Unable to set driver with the provided driver_path."
            )

    def get_html(self, url: str) -> str:
        """
        Return the html code of a url. Works for both dynamic and static webpages.
        """
        try:
            self.driver.get(url)
        except AttributeError:
            print(
                "ERROR get_html: Need to instantiate Webdriver object using the set_driver method."
            )
        else:
            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )
            # allow dynamic elements to load after scrolling to bottom
            time.sleep(5)
            return self.driver.page_source

    def fill_google_form(self, url: str, link: str, price: str, address: str):
        """Fill and submit the Google form from the provided url."""
        try:
            self.driver.get(url)
        except AttributeError:
            print(
                "ERROR get_html: Need to instantiate Webdriver object using the set_driver method."
            )
        else:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@type='text']"))
            )
            inputs = self.driver.find_elements(By.XPATH, "//input[@type='text']")
            inputs[0].send_keys(address)
            inputs[1].send_keys(price)
            inputs[2].send_keys(link)
            self.driver.find_element(By.XPATH, "//div[@role='button']").click()

    def create_google_sheet(
        self,
        google_forms_url: str,
        email: str,
        password: str,
        two_step_verification=False,
    ):
        """Create a Google sheet from the filled forms."""
        self._log_in_google_forms(email, password)
        if two_step_verification:
            self._wait_for_2_step_verification()
        self.driver.get(google_forms_url)
        # Wait for Edit form button to appear and then click it
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@data-tooltip='Edit this form']")
            )
        )
        self.driver.find_element(
            By.XPATH, "//div[@data-tooltip='Edit this form']"
        ).click()
        # Wait for Responses tab to appear and then click it
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()='Responses']"))
        )
        self.driver.find_element(By.XPATH, "//div[text()='Responses']").click()
        # Wait for Link to Sheets button to appear and then click it
        WebDriverWait(
            self.driver, 10, ignored_exceptions=StaleElementReferenceException
        ).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Link to Sheets']"))
        )
        self.driver.find_element(By.XPATH, "//span[text()='Link to Sheets']").click()
        # Wait for Create button to appear and then click it
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//div[@aria-label='Select destination for responses']/div[3]/div[2]",
                )
            )
        )
        self.driver.find_element(
            By.XPATH,
            "//div[@aria-label='Select destination for responses']/div[3]/div[2]",
        ).click()

    def _log_in_google_forms(self, email, password):
        """Log in to Google Forms."""
        try:
            self.driver.get("https://docs.google.com/forms/u/0/?tgif=d")
        except AttributeError:
            print(
                "ERROR get_html: Need to instantiate Webdriver object using the set_driver method."
            )
        else:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@type='email']"))
            )
            self.driver.find_element(By.XPATH, "//input[@type='email']").send_keys(
                email
            )
            self.driver.find_element(By.XPATH, "//span[text()='Next']").click()

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@type='password']"))
            )
            self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys(
                password
            )
            self.driver.find_element(By.XPATH, "//span[text()='Next']").click()

    def _wait_for_2_step_verification(self):
        """Wait 60 seconds to resolve 2-step verification."""
        print("Waiting for 2-step verification...(60s)")
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='docs-homescreen-grid-item']")
            )
        )
        print("2-step verification completed.")


class ZillowParser:
    """
    A parser that extracts house listings from a Zillow webpage.
    """

    def __init__(self):
        self.parser = None

    def set_parser(self, html: str):
        """Set a BeautifulSoup object from the HTML code."""
        try:
            self.parser = BeautifulSoup(html, "html.parser")
        except TypeError:
            print(
                "ERROR set_parser: Invalid HTML. Unable to instantiate the parser object."
            )

    def get_listings(self) -> list[dict]:
        """
        Return a list of houses in the form of a dictionary containing the links,
        prices, and addresses.
        """
        listings = []
        try:
            article_tags = self.parser.find_all(attrs={"data-test": "property-card"})
            for tag in article_tags:
                anchor_tag = tag.find("a")
                link = anchor_tag.get("href")
                price = str(tag.find(attrs={"data-test": "property-card-price"}).string)
                address = str(anchor_tag.string)
                house = {"link": link, "price": price, "address": address}
                listings.append(house)
            return listings
        except AttributeError as e:
            print(
                f"ERROR get_listings: Check if parser object was instantiated using set_parser. Error message: {e}"
            )


if __name__ == "__main__":
    driver_path = r"C:\Users\Mike\OneDrive\Desktop\edgedriver_win64\msedgedriver.exe"
    google_forms_url = "https://docs.google.com/forms/d/e/1FAIpQLSf8_2FsnYdanFUJWL00YY3YLhA1GGcTnU7k5k02d-UE5X2jvw/viewform?usp=sf_link"
    zillow_url = "https://www.zillow.com/las-vegas-nv/?searchQueryState=%7B%22mapBounds%22%3A%7B%22north%22%3A36.536232%2C%22east%22%3A-114.972982%2C%22south%22%3A35.896203%2C%22west%22%3A-115.648624%7D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A600000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22mp%22%3A%7B%22max%22%3A3019%7D%2C%22sort%22%3A%7B%22value%22%3A%22days%22%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A18959%2C%22regionType%22%3A6%7D%5D%2C%22pagination%22%3A%7B%7D%7D"

    load_dotenv()
    email = os.getenv("email")
    password = os.getenv("password")

    bot = EdgeBrowserBot()
    bot.set_driver(driver_path)
    html = bot.get_html(zillow_url)

    parser = ZillowParser()
    parser.set_parser(html)
    listings = parser.get_listings()

    for house in listings:
        bot.fill_google_form(
            google_forms_url, house["link"], house["price"], house["address"]
        )

    bot.create_google_sheet(
        google_forms_url, email, password, two_step_verification=True
    )
