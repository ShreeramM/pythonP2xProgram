import time

from selenium import webdriver

def test_open_chrome():
    driver = webdriver.Chrome()
    time.sleep(40)