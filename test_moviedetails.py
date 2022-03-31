import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def setUp():
    global MovieName,YearOfRelease,DirectorName,Distributor,Producer,driver
    MovieName =input("enter movie name==> ")
    YearOfRelease =input("enter year of release==> ")
    DirectorName =input("enter Director Name==> ")
    Distributor =input("enter Distributor==> ")
    Producer =input("Producer==> ")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(10)
    driver.close()

def test_moviedetails(setUp):
    driver.get("https://iprimedtraining.herokuapp.com/movie.php")
    driver.find_element_by_name("mname").send_keys(MovieName)
    time.sleep(1)
    driver.find_element_by_name("myear").send_keys(YearOfRelease)
    time.sleep(1)
    driver.find_element_by_name("mdirector").send_keys(DirectorName)
    time.sleep(1)
    driver.find_element_by_name("mdist").send_keys(Distributor)
    time.sleep(1)
    driver.find_element_by_name("mproducer").send_keys(Producer)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[6]/td[2]/select/option[3]").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[7]/td[2]/button").click()
    time.sleep(1)

