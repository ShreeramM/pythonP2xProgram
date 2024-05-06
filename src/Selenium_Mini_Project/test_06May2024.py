from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
import selenium.webdriver.support.relative_locator 
import time


def test_MiniProject6():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    driver.maximize_window()

    driver.find_element(loca)
