import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def setUp():
    global Name,driver
    Name = input("enter name")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    driver.close()

def test_form(setUp):
    driver.get("https://iprimedtraining.herokuapp.com/")
    driver.find_element_by_name("name").send_keys(Name)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[2]/td[2]/input[2]").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[3]/td[2]/select/option[1]").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[4]/td[2]/div/input").click()
    time.sleep(1)
    driver.find_element_by_name("subbtn").click()
    time.sleep(1)

