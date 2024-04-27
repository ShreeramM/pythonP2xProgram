#Selenium Mini Project 2
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest



def test_IDrive_Login():
    driver = webdriver.Chrome()
    driver.get("https://www.idrive360.com/enterprise/login") #Launch URL
    driver.maximize_window()

    username = driver.find_element(By.XPATH,value="//input[@id='username']")
    username.send_keys("augtest_040823@idrive.com")

    password = driver.find_element(By.XPATH, value="//input[@id='password']")
    password.send_keys("123456")

    submitbtn = driver.find_element(By.ID,value="frm-btn")
    submitbtn.click()

    time.sleep(25)

    currenturl = driver.current_url
    print(currenturl)
    assert currenturl == "https://www.idrive360.com/enterprise/account?upgradenow=true"

    texttitle = driver.find_element(By.XPATH, value="//h5[@class='id-card-title']")
    print(texttitle.text)
    assert texttitle.text == "Your free trial has expired"