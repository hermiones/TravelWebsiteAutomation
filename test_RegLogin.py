import pytest
from selenium import webdriver
import confest
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

@pytest.fixture()
def test_nav():
    driver.get("https://blazedemo.com/")

def test_1(test_nav):
    driver.find_element(By.XPATH, "//a[contains(text(),'home')]")
