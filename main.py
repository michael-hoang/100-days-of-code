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

URL = 'https://www.linkedin.com/'
WEBDRIVER_PATH = r'C:\Users\Mike\OneDrive\Desktop\edgedriver_win64\msedgedriver.exe'
EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('PASSWORD')


def sign_in():
    """Automatically send environment variables to sign in LinkedIn."""
    email_input = driver.find_element(By.CSS_SELECTOR, '#session_key')
    password_input = driver.find_element(By.CSS_SELECTOR, '#session_password')
    sign_in_btn = driver.find_element(
        By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')

    email_input.send_keys(EMAIL)
    password_input.send_keys(PASSWORD)
    sign_in_btn.click()


def navigate_to_job_page():
    """Navigate to LinkedIn job page from the home page."""
    jobs_btn = driver.find_element(By.LINK_TEXT, 'Jobs')
    jobs_btn.click()


def search_job(job_name: str):
    """Search for jobs on LinkedIn based on job_name."""
    search_input = driver.find_element(
        By.CSS_SELECTOR, 'input.jobs-search-box__text-input'
    )
    search_input.send_keys(job_name)
    time.sleep(1)
    search_input.send_keys(Keys.ENTER)


def check_for_entry_level_jobs(job_element) -> bool:
    """Return True if Entry Level is in the job description."""
    job_link = job_element.find_element(By.CSS_SELECTOR, 'a')
    job_link.click()
    time.sleep(1)
    job_level_ele = driver.find_element(
        By.CSS_SELECTOR, '.jobs-unified-top-card__job-insight span'
    )
    job_level = job_level_ele.text.lower()
    if 'entry' in job_level:
        return True


def save_job():
    """Click on 'Save' if the job is not yet saved."""
    save_btn = driver.find_element(
        By.CSS_SELECTOR, 'button.jobs-save-button span')
    if save_btn.text == 'Save':
        save_btn.click()


def scroll_down_job_listing():
    """Scroll down job listing panel."""
    driver.execute_script(
        f'document.querySelector(".jobs-search-results-list").scrollTo(0, {scroll_range});'
    )


def save_all_entry_jobs_on_page():
    """
    Loop through each job listings on the page and save entry level jobs to
    favorites.
    """
    job_listings = driver.find_elements(
        By.CSS_SELECTOR, 'ul.scaffold-layout__list-container li.ember-view'
    )
    scroll_range = 110
    for job_element in job_listings:
        if check_for_entry_level_jobs(job_element):
            save_job()
        scroll_down_job_listing()
        scroll_range += 110
        time.sleep(2)


service = Service(WEBDRIVER_PATH)
edge_options = Options()
edge_options.add_experimental_option('detach', True)
driver = webdriver.Edge(service=service, options=edge_options)
driver.get(URL)
time.sleep(2)  # Allow page to load

try:
    sign_in()
except:
    sign_in_authwall = driver.find_element(By.LINK_TEXT, 'Sign in')
    sign_in_authwall.click()
    time.sleep(2)
    sign_in()

navigate_to_job_page()
time.sleep(2)
search_job('python developer')
time.sleep(2)

save_all_entry_jobs_on_page()
