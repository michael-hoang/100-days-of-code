import os
import time

from bs4 import BeautifulSoup
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options



if __name__ == '__main__':
    google_form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSdIBMqzYh4TDWwAUin8oxXYGL4xZQz7Jnc7cmFg_cX0gnV32w/viewform?usp=sf_link'