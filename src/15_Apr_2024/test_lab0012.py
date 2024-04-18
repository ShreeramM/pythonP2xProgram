import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_quite_browser():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    element = driver.find_element(By.ID,value="btn-make-appointment")
    element.click()
    # id > name > classname > tagName > LinkText - Partialtext > Css selector > xpath
    #find the element where button with anchor tag is present
    # click on button

