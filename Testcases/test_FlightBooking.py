from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from conftest import *
#book a flight from Boston to Paris
def test_FB1(test_nav):
    driver.maximize_window()
    dropdown1 = Select(driver.find_element(By.XPATH,"/html[1]/body[1]/div[3]/form[1]/select[1]"))
    dropdown1.select_by_visible_text("Boston")
    dropdown2 = Select(driver.find_element(By.XPATH,"/html[1]/body[1]/div[3]/form[1]/select[2]"))
    dropdown2.select_by_visible_text("London")
    driver.find_element(By.XPATH,"/html[1]/body[1]/div[3]/form[1]/div[1]/input[1]").click()
    try:
        if "Flights from Boston to London" in driver.page_source:
            print("The text 'Flights from Boston to London' is present in the page source.")
        else:
            print("The text 'Flights from Boston to London' is not present in the page source.")

    except:
        print("An error occurred:")






