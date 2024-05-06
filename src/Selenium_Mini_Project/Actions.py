from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_01_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/single_text_input.html")
    actions = ActionChains(driver)
    actions.send_keys("Selenium")
    actions.perform()
    time.sleep(3)