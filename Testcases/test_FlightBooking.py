from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from conftest import *




#select a flight from Boston to Paris
def test_FB1(test_nav):
    driver.maximize_window()
    dropdown1 = Select(driver.find_element(By.XPATH,"/html[1]/body[1]/div[3]/form[1]/select[1]"))
    dropdown1.select_by_visible_text("Boston")
    dropdown2 = Select(driver.find_element(By.XPATH,"/html[1]/body[1]/div[3]/form[1]/select[2]"))
    dropdown2.select_by_visible_text("London")
    driver.find_element(By.XPATH,"/html[1]/body[1]/div[3]/form[1]/div[1]/input[1]").click()

#Validate that the search results are coming for boston to paris
def test_FB2():
    assert "Flights from Boston to London" in driver.page_source

#validate that the user is in the purchase page
def test_FB3():
    driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/table[1]/tbody[1]/tr[3]/td[1]/input[1]").click()
    assert "BlazeDemo Purchase" in driver.title

def test_FB4():
    driver.find_element(By.ID,"inputName").send_keys(user_data["name"])
#will skip the part where will be adding user details and card details for now
    driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/form[1]/div[11]/div[1]/input[1]").click()
