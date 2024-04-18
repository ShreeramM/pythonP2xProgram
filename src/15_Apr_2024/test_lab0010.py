import time

from selenium import webdriver

def test_quite_browser():
    driver = webdriver.Chrome()
    driver.get("https://bing.com/chat")
    time.sleep(25) #telling to python interpreter to wait for 25 seconds not to the webdriver
    driver.get("https:google.com")
    time.sleep(20)