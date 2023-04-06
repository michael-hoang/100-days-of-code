from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time

UPGRADE_EVERY_SECONDS = 5


def upgrade():
    """Click and purchase the most expensive upgrade available from Store."""
    avail_upgrades = driver.find_elements(
        By.CSS_SELECTOR, '.product.unlocked.enabled')
    most_expensive_upgrade_avail = avail_upgrades[-1]
    most_expensive_upgrade_avail.click()


url = 'https://orteil.dashnet.org/cookieclicker/'
webdriver_path = r'C:\Users\Mike\OneDrive\Desktop\edgedriver_win64\msedgedriver.exe'

service = Service(webdriver_path)
edge_options = Options()
edge_options.add_experimental_option('detach', True)
driver = webdriver.Edge(service=service, options=edge_options)
driver.get(url)

action = ActionChains(driver)
time.sleep(10.0)  # Give the game 10 seconds to load before executing program.
cookie_btn = driver.find_element(By.CSS_SELECTOR, '#bigCookie')
p0_div = driver.find_element(By.CSS_SELECTOR, '#product0')  # Cursor
p1_div = driver.find_element(By.CSS_SELECTOR, '#product1')  # Grandma
p2_div = driver.find_element(By.CSS_SELECTOR, '#product2')  # Farm
grandma_div = driver.find_element(By.CSS_SELECTOR, '#product3')  # Mine

start_time = time.time()
track_time = start_time
while True:
    cookie_btn.click()
    current_time = time.time()
    cursor_price = int(driver.find_element(
        By.CSS_SELECTOR, '#productPrice0').text)
    if current_time - track_time >= UPGRADE_EVERY_SECONDS:
        action.move_to_element(cursor_div).click().perform()
        track_time = current_time
