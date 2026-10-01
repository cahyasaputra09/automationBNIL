from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from conftest import driver
from utils.data_loader import load_excel_data_merge
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
from page.login_page import LoginPage
from page.home_page import HomePage
from page.SPAJ_page import SPAJPage

@pytest.mark.parametrize("testDataBNIL", load_excel_data_merge("testData_login", "testData_dataSPAJ"))
def test_filterSPAJ(driver, base_url, testDataBNIL):
    log = LoginPage(driver)
    home = HomePage(driver)
    spaj = SPAJPage(driver)

    #inisialisasi test data excel
    username = testDataBNIL.get("username", "")
    password = testDataBNIL.get("password", "")
    expected = testDataBNIL.get("expected", "")
    statusData = testDataBNIL.get("data status", "")
    tgl_awal = testDataBNIL.get("tanggal awal", "")
    tgl_akhir = testDataBNIL.get("tanggal akhir", "")
    kategoriData = testDataBNIL.get("kategori data", "")

    driver.get(base_url)

    #POM Login
    print("DEBUG: Melakukan login...")
    log.login(username, password)
    time.sleep(3)

    #POM page SPAJ
    print("DEBUG: Mengakses halaman SPAJ...")
    home.dataSPAJ()
    time.sleep(3)

    #verify halaman SPAJ
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Data SPAJ')]"))
    )
    print("DEBUG: BERHASIL MASUK PAGE DATA SPAJ...")

    # Lakukan filter data SPAJ
    print("DEBUG: Melakukan filter data SPAJ...")
    spaj.filterDataSPAJ(statusData, tgl_awal, tgl_akhir, kategoriData)
    print("DEBUG: Filter data SPAJ berhasil dilakukan.")

    time.sleep(5)