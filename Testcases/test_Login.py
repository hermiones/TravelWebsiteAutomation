from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Ensure you have your fixture for the driver and user_data available
from conftest import *


# Successful login
def test_log1(test_nav):
    # Navigating to the homepage
    driver.find_element(By.XPATH, "//a[contains(text(),'home')]").click()

    # Executing the test
    driver.find_element(By.ID, "email").send_keys(user_data["email"])
    driver.find_element(By.ID, "password").send_keys(user_data["password"])
    driver.find_element(By.XPATH,
                        "//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[3]/div[1]/div[1]/label[1]/input[1]").click()
    driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
    #assert "You are logged in!" in driver.page_source
    driver.delete_all_cookies()


# Unsuccessful login
def test_log2(test_nav):
    # Navigating to the homepage
    driver.find_element(By.XPATH, "//a[contains(text(),'home')]").click()

    # Executing the test with incorrect credentials
    driver.find_element(By.ID, "email").send_keys("incorrect@example.com")
    driver.find_element(By.ID, "password").send_keys("incorrect_passwyyord")
    driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
    assert "You are logged in!" not in driver.page_source


# Blank email and password is provided
def test_log3(test_nav):
    # Navigating to the homepage
    driver.find_element(By.XPATH, "//a[contains(text(),'home')]").click()

    # Executing the test with incorrect credentials
    driver.find_element(By.ID, "email").send_keys("")
    driver.find_element(By.ID, "password").send_keys("")
    driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()

    # Wait for the alert to appear
    #alert = WebDriverWait(driver, 10).until(EC.alert_is_present())

    # Get the text of the alert

    #alert_text = alert.text

    # Assert the alert text
    #assert "Please fill in" not in alert_text, "Expected alert message not found"

# Test forgot password
def test_log4(test_nav):
    # Navigating to the homepage
    driver.find_element(By.XPATH, "//a[contains(text(),'home')]").click()

    # Clicking on the "Forgot Your Password" link
    driver.find_element(By.PARTIAL_LINK_TEXT, "Forgot Your Passwor").click()
    assert "Reset Password" in driver.page_source
