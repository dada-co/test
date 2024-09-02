import time

import streamlit as st

"""
## Web scraping on Streamlit Cloud with Selenium

[![Source](https://img.shields.io/badge/View-Source-<COLOR>.svg)](https://github.com/snehankekre/streamlit-selenium-chrome/)

This is a minimal, reproducible example of how to scrape the web with Selenium and Chrome on Streamlit's Community Cloud.

Fork this repo, and edit `/streamlit_app.py` to customize this app to your heart's desire. :heart:
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

@st.cache_resource
def get_driver():
    return webdriver.Chrome(
        service=Service(
            ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
        ),
        options=options,
    )

options = Options()
options.add_argument("--disable-gpu")
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# Simulate San Francisco timezone by setting environment variables
chrome_options.add_argument("TZ=America/Los_Angeles")

driver = get_driver()
driver.get("https://www.amazon.com")

time.sleep(7)
screenshot1_file = "test.png"
driver.save_screenshot(screenshot1_file)
time.sleep(7)
st.image(screenshot1_file)
