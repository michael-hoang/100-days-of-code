import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options


load_dotenv()

URL = 'https://www.pythonanywhere.com/'
WEBDRIVER_PATH = r'C:\Users\Mike\OneDrive\Desktop\edgedriver_win64\msedgedriver.exe'
USER = os.environ.get('USER')
PASSWORD = os.environ.get('PASSWORD')

service = Service(WEBDRIVER_PATH)
edge_options = Options()
edge_options.add_experimental_option('detach', True)
driver = webdriver.Edge(service=service, options=edge_options)
driver.get(URL)
time.sleep(2)