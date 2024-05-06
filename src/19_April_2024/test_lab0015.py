
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_make_Appointment():
        driver = webdriver.Chrome()
        driver.get("https://katalon-demo-cura.herokuapp.com/") #launch URl
        driver.maximize_window()
        #Link Text
        # make_appt_btn = driver.find_element(By.LINK_TEXT,value='Make Appointment') #exact or full match
        # make_appt_btn.click()

        # #Partial Link Text
        # make_appt_btn = driver.find_element(By.PARTIAL_LINK_TEXT,value='Make') #exact or full match
        # make_appt_btn.click()
        #Tag Name
        list_of_a_tags = driver.find_elements(By.TAG_NAME, value='a')  # exact or full match
        make_appt_btn = list_of_a_tags[5]
        make_appt_btn.click()
        time.sleep(20)
        driver.quit()