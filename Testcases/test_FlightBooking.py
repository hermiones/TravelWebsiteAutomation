from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

from conftest import *
#book a flight from Boston to rome
def test_FB1(test_nav):
    #Selecting the
    dropdown = Select(driver.find_element(By.XPATH,"/html[1]/body[1]/div[3]/form[1]/select[1]"))
    dropdown.select_by_visible_text("Boston")

