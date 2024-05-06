from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
def test_MiniProject4():
    global price
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/")
    driver.maximize_window()


    search_field = driver.find_element(By.XPATH,"//input[@id='gh-ac']")
    search_field.send_keys("16 gb")

    driver.implicitly_wait(10)

    submitbtn = driver.find_element(By.XPATH, "//input[@id='gh-btn']")
    submitbtn.click()


    price_list = driver.find_elements(By.XPATH,"//span[@class='s-item__price']")
    for price in range(len(price_list)):
        #print(price.text)
        value = price_list[price].text.replace('$', '')
        #print(value)
        print(type(value))

        value1 = int(value)
        print(value1)
        #
        # if int(min(value)) <= 10:
        #     print("Low Price")
        #     print(int(min(value)))
        # else:
        #     print("High Price")

        # if int(value) <= 10:
        #     print("Cheapest RAM Found")
        #     print(value)
        # else:
        #     print("Cheapest RAM not Found")