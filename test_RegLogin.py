import pytest
from selenium.webdriver.common.by import By
import conftest
from conftest import driver



def test_1(test_nav):
    driver.find_element(By.XPATH, "//a[contains(text(),'home')]").click()
