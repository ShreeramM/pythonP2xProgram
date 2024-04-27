from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.by import By
def test_MiniProject3():
    driver = webdriver.Chrome()
    driver.get("https://cdpn.io/AbdullahSajjad/fullpage/LYGVRgK?anon=true&view=fullpage")
    driver.maximize_window()

    time.sleep(5)
    driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='result']"))

    email = driver.find_element(By.XPATH,"//input[@id='email']")
    email.send_keys("test@gmail.com")

    password = driver.find_element(By.XPATH, "//input[@id='password']")
    password.send_keys("123456")

    confirm_password = driver.find_element(By.XPATH, "//input[@id='password2']")
    confirm_password.send_keys("123456")

    submitbtn = driver.find_element(By.XPATH, "//button[text()='Submit']")
    submitbtn.click()

    time.sleep(5)

    msgtitle = driver.find_element(By.XPATH, "//div/small")
    print(msgtitle.text)
    assert msgtitle.text == "Username must be at least 3 characters"