import pytest
from selenium import webdriver

def test_open_vwologinpage():
    #LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome() # Post Request new session request
    driver.get("https://app.vwo.com") #Get Request with URL Parameters
    print(driver.title)
    driver.maximize_window()
    #print(driver.page_source)
    print(driver.session_id)