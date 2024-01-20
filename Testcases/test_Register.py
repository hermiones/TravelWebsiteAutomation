

from selenium.webdriver.common.by import By
from conftest import driver, register_user
from conftest import user_data


# Validating the title of the webpage
def test_reg1(test_nav):
    assert driver.title == "BlazeDemo"

# Navigating to the homepage
def test_reg2():
    driver.find_element(By.XPATH, "//a[contains(text(),'home')]").click()

# Navigating to the Registration page and registering as a user with valid credentials
def test_reg3():
    driver.find_element(By.XPATH,"//a[normalize-space()='Register']").click()
    register_user(user_data)
    driver.find_element(By.XPATH, "//button[contains(text(),'Register')]").click()

