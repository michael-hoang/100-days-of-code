from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time

UPGRADE_EVERY_SECONDS = 5

url = 'https://orteil.dashnet.org/cookieclicker/'
webdriver_path = r'C:\Users\Mike\OneDrive\Desktop\edgedriver_win64\msedgedriver.exe'

service = Service(webdriver_path)
edge_options = Options()
edge_options.add_experimental_option('detach', True)
driver = webdriver.Edge(service=service, options=edge_options)
driver.get(url)

time.sleep(10.0) # Give the game 10 seconds to load before executing program.
cookie_btn = driver.find_element(By.CSS_SELECTOR, '#bigCookie')
cursor_div = driver.find_element(By.CSS_SELECTOR, '#product0')

start_time = time.time()
while True:
    cookie_btn.click()
    current_time = time.time()
    if start_time - current_time == UPGRADE_EVERY_SECONDS:
        
        start_time = current_time