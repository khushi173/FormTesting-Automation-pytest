import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def setUp():
    global Name,Address,Pincode,Mobile,EmailId,Password,ConfirmPassword,driver
    Name = input("enter the name==> ")
    Address = input("enter address==> ")
    Pincode = input("enter pincode==> ")
    Mobile = input("enter mobile number==>  ")
    EmailId = input("enter email id==> ")
    Password = input("enter password==> ")
    ConfirmPassword = input("enter password again==> ")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(10)
    driver.close()
def test_userdetails(setUp):
    driver.get("https://iprimedtraining.herokuapp.com/userdata.php")
    driver.find_element_by_name("name").send_keys(Name)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[2]/td[2]/input[2]").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[3]/td[2]/select/option[1]").click()
    time.sleep(1)
    driver.find_element_by_name("Address").send_keys(Address)
    time.sleep(1)
    driver.find_element_by_name("Pincode").send_keys(Pincode)
    time.sleep(1)
    driver.find_element_by_name("Mobile").send_keys(Mobile)
    time.sleep(1)
    driver.find_element_by_name("Email").send_keys(EmailId)
    time.sleep(1)
    driver.find_element_by_name("pass").send_keys(Password)
    time.sleep(1)
    driver.find_element_by_name("cnfpass").send_keys(ConfirmPassword)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[10]/td[2]/div/input").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[11]/td[2]/button").click()
    time.sleep(1)
