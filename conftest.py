import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# driver
driver = webdriver.Chrome()


# declaring the url
@pytest.fixture
def test_nav():
    driver.get('https://blazedemo.com/')


# user data for Register
user_data = {
    "name": "John Doe",
    "company": "ABC Corp",
    "email": "john.doe@example.com",
    "password": "password123",
    "password-confirm": "password123"

}
# function for registering multiple columns
def register_user(user_data):
    # Iterate over keys in user_data and fill in the corresponding fields
    for field_name, field_value in user_data.items():
        driver.find_element(By.ID, field_name).send_keys(field_value)

