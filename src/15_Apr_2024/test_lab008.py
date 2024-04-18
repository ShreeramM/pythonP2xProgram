import time

from selenium import webdriver

def test_quite_browser():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    driver.close() #Close will close the current window or tab session id will be invalid and not close other tabs
    time.sleep(20)