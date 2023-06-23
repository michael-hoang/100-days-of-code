import os
import requests
import time

from bs4 import BeautifulSoup
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options


class ZillowHouseScraper:
    """
    Scraper for Zillow house listings that exports data to Google sheet via Google form.
    """

    def __init__(self, webdriver_path: str, zillow_url: str):
        google_form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSdIBMqzYh4TDWwAUin8oxXYGL4xZQz7Jnc7cmFg_cX0gnV32w/viewform?usp=sf_link'
        self.driver = self.create_webdriver()
        self.parser = self.create_parser()

        # bs = BeautifulSoup(html, 'html.parser')
        # attributes = {'data-test': 'property-card'}
        # tags = bs.find_all(attrs=attributes)
        # count = 0
        # for tag in tags:
        #     count +=1
        # print(count)

    def create_parser(self) -> BeautifulSoup:
        """Return BeautifulSoup object from zillow_url."""
        try:
            html = self._get_full_dynamic_html()
            return BeautifulSoup(html, 'html.parser')
        except Exception as e:
            print(f'Unable to create parser from zillow_url.\n{e}')

    def _get_full_dynamic_html(self) -> str:
        self.driver.get(zillow_url)
        self.driver.execute_script(
            'window.scrollTo(0, document.body.scrollHeight);'
        )
        time.sleep(5)
        return self.driver.page_source

    def create_webdriver(self) -> webdriver.Edge:
        """Return Webdriver object from webdriver_path."""
        service = Service(webdriver_path)
        options = Options()
        options.add_experimental_option('detach', True)
        return webdriver.Edge(service=service, options=options)


if __name__ == '__main__':
    webdriver_path = r'C:\Users\Mike\OneDrive\Desktop\edgedriver_win64\msedgedriver.exe'
    zillow_url = 'https://www.zillow.com/orange-county-ca/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A34.1212772497386%2C%22east%22%3A-116.96606875585937%2C%22south%22%3A33.15862901775036%2C%22west%22%3A-118.57281924414062%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A1286%2C%22regionType%22%3A4%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A850000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22mp%22%3A%7B%22max%22%3A4273%7D%2C%22sort%22%3A%7B%22value%22%3A%22days%22%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D'
    zhs = ZillowHouseScraper(webdriver_path, zillow_url)
