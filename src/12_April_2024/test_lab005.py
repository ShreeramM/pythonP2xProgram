import pytest
from selenium import webdriver
import logging
import  time

@pytest.mark.normal
def test_open_vwologinpage():
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome() # Post Request new session request
    driver.get("https://app.vwo.com") #Get Request with URL Parameters
    print(driver.title)
    driver.maximize_window()
    print(logging)
    assert driver.title == 'Login - VWO'