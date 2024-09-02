import streamlit as st
import os, time

@st.experimental_singleton
def installff():
  os.system('sbase install geckodriver')
  os.system('ln -s /home/appuser/venv/lib/python3.7/site-packages/seleniumbase/drivers/geckodriver /home/appuser/venv/bin/geckodriver')

_ = installff()
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
opts = FirefoxOptions()
opts.add_argument("--headless")
browser = webdriver.Firefox(options=opts)

browser.get('https://www.amazon.com')


time.sleep(7)
screenshot1_file = "test2.png"
browser.save_screenshot(screenshot1_file)
time.sleep(7)
st.image(screenshot1_file)
