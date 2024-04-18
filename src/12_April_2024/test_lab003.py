from selenium import webdriver

#Selenium 4 no need to install browser

def test_open_vwologinpage():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")