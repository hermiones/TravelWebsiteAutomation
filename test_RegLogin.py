from selenium.webdriver.common.by import By
from conftest import driver


#Validating the title of the webpage
def test_1(test_nav):
    assert driver.title == "BlazeDemo"

#Navigating to the homepage
def test_2():
    driver.find_element(By.XPATH, "//a[contains(text(),'home')]").click()

#Navigating to the Registration page
def test_3():
    driver.find_element(By.XPATH,"//a[normalize-space()='Register']").click()

