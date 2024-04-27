import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Selenium Mini Project #1
def test_make_Appointment():
        driver = webdriver.Chrome()
        driver.get("https://katalon-demo-cura.herokuapp.com/") #launch URl
        driver.maximize_window()

        makeappt = driver.find_element(By.ID,value="btn-make-appointment")
        makeappt.click() #Make Appointment button click

        time.sleep(3)

        currenturl = driver.current_url
        print(currenturl)
        assert currenturl == "https://katalon-demo-cura.herokuapp.com/profile.php#login","Failed Msg - Not matching"
        allure.attach(driver.get_screenshot_as_png(), name="current screenshot", attachment_type='image/png"')
        time.sleep(5)

        username = driver.find_element(By.NAME, value="username")
        username.send_keys("John Doe")  # Enter Username

        password = driver.find_element(By.ID, value="txt-password")
        password.send_keys("ThisIsNotAPassword")  # Enter Password

        loginbtn = driver.find_element(By.ID, value="btn-login")
        loginbtn.click() #Click on Login button

        currenturl = driver.current_url
        print(currenturl)
        assert currenturl == "https://katalon-demo-cura.herokuapp.com/#appointment","Failed Msg #2 - Not matching"

        ApptText = driver.find_element(By.CLASS_NAME,value="col-sm-12")
        print(ApptText.text) #Print ApptText value
        assert ApptText.text == 'Make Appointment' #Assert Make Appointment text