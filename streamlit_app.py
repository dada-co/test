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
        options=chrome_options,
    )


user_data_dir = "./chrome_user_data"  # Replace with the desired path to save user data
# Ensure the directory exists
# Setup Chrome options to use the custom user data directory
chrome_options = Options()
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")  # Specify the user data directory
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")

driver = get_driver()
driver.get("https://www.amazon.com")

time.sleep(7)
screenshot1_file = "test2.png"
driver.save_screenshot(screenshot1_file)
time.sleep(7)
st.image(screenshot1_file)
