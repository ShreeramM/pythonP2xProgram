
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
import time
def test_MiniProject6():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

    driver.implicitly_wait(5)

    username = driver.find_element(By.XPATH,"//input[@name='username']")
    username.send_keys("Admin")

    password = driver.find_element(By.XPATH, "//input[@name='password']")
    password.send_keys("admin123")

    submitbtn = driver.find_element(By.XPATH, "//button[@type='submit']")
    submitbtn.click()

    adminbtn = driver.find_element(By.XPATH, "//span[text()='Admin']")
    adminbtn.click()

    driver.implicitly_wait(10)

    addbtn = driver.find_element(By.XPATH, "//button[text()=' Add ']")
    addbtn.click()
    #
    user_role = driver.find_elements(By.XPATH,"//*[@class='oxd-select-text--after']")
    user_role[0].click()
    list = driver.find_element(By.XPATH,"//div[@role='listbox']/div[3]")
    print(list.text)
    list.click()
    #
    status = driver.find_elements(By.XPATH, "//*[@class='oxd-select-text--after']/i[1]")
    status[1].click()
    list = driver.find_element(By.XPATH, "//div[@role='listbox']/div[3]")
    print(list.text)
    list.click()
    driver.implicitly_wait(5)
    #
    employee_name = driver.find_element(By.XPATH,"//div[@class='oxd-autocomplete-wrapper']/div/input")
    employee_name.send_keys("manda")
    