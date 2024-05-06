from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_make_Appointment():
        driver = webdriver.Chrome()
        driver.get("https://katalon-demo-cura.herokuapp.com/") #launch URl
        driver.maximize_window()

        makeappt = driver.find_element(By.ID,value="btn-make-appointment")
        makeappt.click() #Make Appointment button click

        # < input
        # type = "email"
        # class ="text-input W(100%)" name="username" id="login-username" data-qa="hocewoqisi" >