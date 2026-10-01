from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from conftest import driver
from utils.data_loader import load_excel_data
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
from page.login_page import LoginPage
from page.home_page import HomePage

@pytest.mark.parametrize("testDataBNIL", load_excel_data("testData_login"))
def test_logout(driver, base_url, testDataBNIL):
    log = LoginPage(driver)
    home = HomePage(driver)

    #inisialisasi data
    username = testDataBNIL.get("username", "")
    password = testDataBNIL.get("password", "")  
    expected = testDataBNIL.get("expected", "")

    #link
    driver.get(base_url)

    #POM login
    log.login(username, password)

    time.sleep(10)

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h3[text()='Insurance Submission System BNI Life Insurance']"))
        )
        actual = "berhasil masuk dashboard"
    except:
        actual = "gagal masuk dashboard"
    
    assert expected.lower() in actual.lower(), f"Expected '{expected}', but got '{actual}'" 

    home.logout()
    time.sleep(5)

    try: 
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//img[@src='/Insubsyt2/Images/password.png']"))
        )
        actual = "berhasil logout"
    except:
        actual = "gagal logout"