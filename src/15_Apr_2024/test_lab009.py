import time

from selenium import webdriver

def test_quite_browser():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    driver.quit() #Close will close all the tabs
    time.sleep(20)