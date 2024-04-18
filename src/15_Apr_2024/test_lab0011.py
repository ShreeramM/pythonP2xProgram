import time

from selenium import webdriver

def test_quite_browser():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    driver.back()
    driver.get("https://app.vwo.com")
    driver.forward()
    driver.back()
    driver.refresh()
    time.sleep(5)