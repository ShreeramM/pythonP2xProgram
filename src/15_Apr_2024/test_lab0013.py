
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_quite_browser():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    emailaddress = driver.find_element(By.NAME,value="username")
    emailaddress.send_keys("admin")

    password = driver.find_element(By.NAME, value="password")
    password.send_keys("admin")

    submit = driver.find_element(By.ID, value="js-login-btn")
    submit.click()

    msg = driver.find_element(By.ID, value="js-notification-box-msg")
    text = msg.text
    print(text)
    assert text == "Your email, password, IP address or location did not match"
    time.sleep(5)
    # id > name > classname > tagName > LinkText - Partialtext > Css selector > xpath
    #find the element where button with anchor tag is present
    # click on button

