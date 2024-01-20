from selenium.webdriver.common.by import By

# Ensure you have your fixture for the driver and user_data available
from conftest import driver, user_data

# Successful login
def test_log1(test_nav):
    # Navigating to the homepage
    driver.find_element(By.XPATH, "//a[contains(text(),'home')]").click()

    # Executing the test
    driver.find_element(By.ID, "email").send_keys(user_data["email"])
    driver.find_element(By.ID, "password").send_keys(user_data["password"])
    driver.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[3]/div[1]/div[1]/label[1]/input[1]").click()
    driver.find_element(By.XPATH,"//button[contains(text(),'Login')]").click()
    assert "You are logged in!" in driver.page_source
    driver.delete_all_cookies()

# Unsuccessful login
def test_log2(test_nav):
    # Navigating to the homepage
    driver.find_element(By.XPATH, "//a[contains(text(),'home')]").click()

    # Executing the test with incorrect credentials
    driver.find_element(By.ID, "email").send_keys("incorrect@example.com")
    driver.find_element(By.ID, "password").send_keys("incorrect_password")
    driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()


