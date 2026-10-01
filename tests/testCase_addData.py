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
from page.ilustrasi_page import IlustrasiPage

@pytest.mark.parametrize("testDataBNIL", load_excel_data("testData_addData"))
def test_addData(driver, base_url, testDataBNIL):
    print(f"DEBUG: Starting test with data: {testDataBNIL}")
    
    log = LoginPage(driver)
    home = HomePage(driver)
    ilustrasi = IlustrasiPage(driver)
    
    # Inisialisasi data
    username = testDataBNIL.get("username", "")
    password = testDataBNIL.get("password", "")
    expected = testDataBNIL.get("expected", "")
    namaDepan = testDataBNIL.get("nama_depan", "")
    birth = testDataBNIL.get("tgl_lahir", "")
    kelamin = testDataBNIL.get("kelamin", "")
    status = testDataBNIL.get("status", "")
    caraBayar = testDataBNIL.get("cara bayar", "")
    masaBayar = testDataBNIL.get("masa bayar", "")
    premiDasar = testDataBNIL.get("premi dasar", "")
    noTLP = testDataBNIL.get("no tlp", "")
    nama_belakang = testDataBNIL.get("nama_belakang", "")
    email = testDataBNIL.get("email", "")
    note = testDataBNIL.get("note", "")



    
    print(f"DEBUG: Data yang akan digunakan:")
    print(f"  - username: {username}")
    print(f"  - Nama: {namaDepan}")
    print(f"  - Tanggal lahir: {birth}")
    print(f"  - Kelamin: {kelamin}")
    print(f"  - Expected: {expected}")
    
    # Link
    driver.get(base_url)
    
    # POM login
    print("DEBUG: Melakukan login...")
    log.login(username, password)
    time.sleep(10)
    
    # POM page ilustrasi
    print("DEBUG: Navigasi ke halaman ilustrasi...")
    home.dataIlustrasi()
    
    # Navigate to form
    print("DEBUG: Klik tombol untuk menambah data...")
    add_button = driver.find_element(By.XPATH, "//a[@class='medium button' and @href='/Insubsyt2/Transactions/BancassuranceIllustration/Main']")
    driver.execute_script("arguments[0].scrollIntoView();", add_button)
    time.sleep(1)
    add_button.click()
    time.sleep(3)  # Wait for page load
    
    
    # POM form add data
    print("DEBUG: Mengisi form data...")
    ilustrasi.form_addData(namaDepan, birth, kelamin, expected, noTLP, nama_belakang, status, email, note)

    ilustrasi.ilustrasi_page(caraBayar, masaBayar, premiDasar)

    time.sleep(10)
    
