import pytest
from selenium import webdriver
driver = webdriver.Chrome()

@pytest.fixture
def test_nav():
    driver.get('https://blazedemo.com/')
