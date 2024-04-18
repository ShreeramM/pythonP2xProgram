

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_make_Appointment():
        driver = webdriver.Chrome()
        driver.get("https://katalon-demo-cura.herokuapp.com/") #launch URl
        driver.maximize_window()

        makeappt = driver.find_element(By.ID,value="btn-make-appointment")
        makeappt.click() #Make Appointment button click

        time.sleep(3)

        titlechange = driver.title
        print(titlechange)
        assert titlechange == "CURA Healthcare Service"

        time.sleep(5)

        username = driver.find_element(By.ID, value="txt-username")
        username.send_keys("John Doe")  # Enter Username

        password = driver.find_element(By.ID, value="txt-password")
        password.send_keys("ThisIsNotAPassword")  # Enter Password

        loginbtn = driver.find_element(By.ID, value="btn-login")
        loginbtn.click() #Click on Login button

        titlechange = driver.title
        print(titlechange)
        assert titlechange == "CURA Healthcare Service"

        ApptText = driver.find_element(By.CLASS_NAME,value="col-sm-12")
        print(ApptText.text) #Print ApptText value
        assert ApptText.text == 'Make Appointment' #Assert Make Appointment text