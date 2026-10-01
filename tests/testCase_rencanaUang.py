from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from conftest import driver
from page.SPAJ_page import SPAJPage
from utils.data_loader import load_excel_data_merge
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
from page.login_page import LoginPage
from page.home_page import HomePage
from page.rencanaUang_page import RencanaUangPage

@pytest.mark.parametrize("testDataBNIL", load_excel_data_merge("testData_login", "testData_rencanaUang"))
def test_rencanaUang(driver, base_url, testDataBNIL):
    log = LoginPage(driver)
    home = HomePage(driver)
    rencana = RencanaUangPage(driver)

    #inisialisasi test data
    username = testDataBNIL.get("username", "")
    password = testDataBNIL.get("password", "")
    nama_lengkap = testDataBNIL.get("nama_lengkap", "")
    usiaOrTTL = testDataBNIL.get("usiaOrTTL", "")
    pengeluaran = testDataBNIL.get("pengeluaran", "")
    usia = testDataBNIL.get("usia", "")
    status = testDataBNIL.get("status", "")
    danaSedia = testDataBNIL.get("danaSedia", "")
    anak = testDataBNIL.get("anak", "")
    tujuan = testDataBNIL.get("tujuan", "")

    driver.get(base_url)

    #POM Login
    print("DEBUG: Melakukan login...")
    log.login(username, password)
    time.sleep(3)

    #POM page Rencana Uang
    print("DEBUG: Mengakses halaman Rencana Uang...")
    home.rencanaUang()
    time.sleep(3)

    #POM perencanaan uang
    rencana.form_rencanaUang(nama_lengkap, usiaOrTTL, pengeluaran, status, usia, danaSedia, anak, tujuan)
    time.sleep(5)