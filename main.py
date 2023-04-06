from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time


url = 'https://www.linkedin.com/'
webdriver_path = r'C:\Users\Mike\OneDrive\Desktop\edgedriver_win64\msedgedriver.exe'

service = Service(webdriver_path)
edge_options = Options()
edge_options.add_experimental_option('detach', True)
driver = webdriver.Edge(service=service, options=edge_options)
driver.get(url)


# Log in
email_input = driver.find_element(By.CSS_SELECTOR, '#session_key')
password_input = driver.find_element(By.CSS_SELECTOR, '#session_password')
sign_in_btn = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')

# email_input.send_keys('myemail')
# password_input.send_keys('mypassword')
# sign_in_btn.click()
