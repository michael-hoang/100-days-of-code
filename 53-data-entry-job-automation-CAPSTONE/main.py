import os
import time

from bs4 import BeautifulSoup
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from typing import List


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
        options.add_experimental_option('detach', True)
        self.driver = webdriver.Edge(service=service, options=options)

    def get_html(self, url: str) -> str:
        """
        Return the html code of a url. Works for both dynamic and static webpages.
        """
        try:
            self.driver.get(url)
        except AttributeError:
            print(
                'Need to instantiate Webdriver object using the set_driver method.'
            )
        else:
            self.driver.execute_script(
                'window.scrollTo(0, document.body.scrollHeight);'
            )
            # allow dynamic elements to load after scrolling to bottom
            time.sleep(5)
            return self.driver.page_source


class ZillowParser:
    """
    A parser that extracts house listings from a Zillow webpage.
    """
    def __init__(self):
        self.parser = None

    def set_parser(self, html: str):
        """Set a BeautifulSoup object from an HTML code."""
        self.parser = BeautifulSoup(html, 'html.parser')


class ZillowHouseScraper:
    """
    Scraper for Zillow house listings that exports data to Google sheet via Google form.
    """

    def __init__(self, webdriver_path: str, zillow_url: str):
        google_form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSdIBMqzYh4TDWwAUin8oxXYGL4xZQz7Jnc7cmFg_cX0gnV32w/viewform?usp=sf_link'
        self.driver = self.create_webdriver()
        self.parser = self.create_parser()
        self.house_listings = self.get_house_listings()
        self.links = []
        self.prices = []
        self.addresses = []

    def get_house_listings(self):
        """
        Parse for house listings in the form of article tags.
        Return value is a list subclass 'bs4.element.ResultSet'.
        """
        attributes = {'data-test': 'property-card'}
        return self.parser.find_all(attrs=attributes)


if __name__ == '__main__':
    webdriver_path = r'C:\Users\Mike\OneDrive\Desktop\edgedriver_win64\msedgedriver.exe'
    google_form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSdIBMqzYh4TDWwAUin8oxXYGL4xZQz7Jnc7cmFg_cX0gnV32w/viewform?usp=sf_link'
    zillow_url = 'https://www.zillow.com/orange-county-ca/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A34.1212772497386%2C%22east%22%3A-116.96606875585937%2C%22south%22%3A33.15862901775036%2C%22west%22%3A-118.57281924414062%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A1286%2C%22regionType%22%3A4%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A850000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22mp%22%3A%7B%22max%22%3A4273%7D%2C%22sort%22%3A%7B%22value%22%3A%22days%22%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D'
    # zhs = ZillowHouseScraper(webdriver_path, zillow_url)
    bot = EdgeBrowserBot()
    html = bot.get_html(zillow_url)
    parser = ZillowParser()
    parser.set_parser(html)
