import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options


url = 'https://www.linkedin.com/'
webdriver_path = r'C:\Users\Mike\OneDrive\Desktop\edgedriver_win64\msedgedriver.exe'

service = Service(webdriver_path)
edge_options = Options()
edge_options.add_experimental_option('detach', True)
driver = webdriver.Edge(service=service, options=edge_options)
driver.get(url)

# Load environment variables
load_dotenv()
email = os.environ.get('EMAIL')
password = os.environ.get('PASSWORD')

# Log in
email_input = driver.find_element(By.CSS_SELECTOR, '#session_key')
password_input = driver.find_element(By.CSS_SELECTOR, '#session_password')
sign_in_btn = driver.find_element(
    By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')

email_input.send_keys(email)
password_input.send_keys(password)
sign_in_btn.click()

# Search jobs
jobs_btn = driver.find_element(By.LINK_TEXT, 'Jobs')
jobs_btn.click()
time.sleep(3)  # Allow page to load all elements
search_input = driver.find_element(
    By.CSS_SELECTOR, 'input.jobs-search-box__text-input')
search_input.send_keys('python developer')
time.sleep(1)
search_input.send_keys(Keys.ENTER)
