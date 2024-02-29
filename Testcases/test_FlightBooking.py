from selenium.webdriver.support.select import Select

from conftest import Path_Screenshot
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
    driver.find_element(By.ID,"address").send_keys("INDIA")
    driver.find_element(By.ID,"city").send_keys("ABC")

    driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/form[1]/div[11]/div[1]/input[1]").click()
#Taking screenshot of the final booking
def test_FB5():
    driver.save_screenshot(Path_Screenshot+"ticket.png")


