from selenium import webdriver
import  time

def test_open_vwologinpage():
    driver = webdriver.Chrome() # Post Request new session request
    driver.get("https://app.vwo.com") #Get Request with URL Parameters
    time.sleep(5)
