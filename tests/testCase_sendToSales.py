from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from conftest import driver
from page.referral_page import referralPage
from utils.data_loader import load_excel_data, load_excel_data_merge
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
from page.login_page import LoginPage
from page.home_page import HomePage
from page.referral_page import referralPage
from page.SPAJ_page import SPAJPage
from page.upload_page import uploadPage
from selenium.webdriver.common.action_chains import ActionChains

@pytest.mark.parametrize("testDataBNIL", load_excel_data_merge("testData_login", "testData_sales"))
def test_sendToSales(driver, base_url, testDataBNIL):
    log = LoginPage(driver)
    home = HomePage(driver)
    referral = referralPage(driver)
    SPAJ = SPAJPage(driver)
    upload = uploadPage(driver)
    wait = WebDriverWait(driver, 50)

    #inisialisasi
    pemegangPolis = testDataBNIL.get("pemegangPolis", "")
    CIF = testDataBNIL.get("CIF", "")
    statusPegawai = testDataBNIL.get("statusPegawai", "")
    kodeCabang = testDataBNIL.get("kodeCabang", "")
    divisi = testDataBNIL.get("divisi", "")
    nama = testDataBNIL.get("nama", "")
    NPPpegawai = testDataBNIL.get("NPPpegawai", "")
    NPPpemimpin = testDataBNIL.get("NPPpemimpin", "")
    notes = testDataBNIL.get("notes", "")
    username = testDataBNIL.get("username", "")
    password = testDataBNIL.get("password", "")

    # Link
    driver.get(base_url)

    print(CIF, statusPegawai, kodeCabang, divisi, nama, NPPpegawai, NPPpemimpin)

    # POM login
    log.login(username, password)
    time.sleep(3)

    #POM dataSPAJ
    home.dataSPAJ()

    #POM searchSPAJ
    SPAJ.search(pemegangPolis)
    time.sleep(5)

    # POM page referral
    referral.hrefRefferal(pemegangPolis)

    #POM update refferal
    referral.updateRefferal(CIF, statusPegawai, kodeCabang, divisi, nama, NPPpegawai, NPPpemimpin)

    #verify referral pdf
    try:
        main_window = driver.current_window_handle
        WebDriverWait(driver, 200).until(
            lambda d: len(d.window_handles) > 1
        )

        new_window = driver.window_handles[-1]
        driver.switch_to.window(new_window)

        WebDriverWait(driver, 10).until(
            lambda d: d.current_url.endswith(".pdf") or d.current_url.startswith("file:///")
        )

        print("pdf referral terlihat")
    except:
        print("pdf referral tidak terlihat")

    time.sleep(3)

    driver.close()
    driver.switch_to.window(main_window)
    time.sleep(3)

    driver.find_element(By.XPATH, "//li[@class='has-dropdown not-click']/a[text()='SPAJ']")
    print("spaj terlihat...")
    time.sleep(5)
    SPAJmenu = WebDriverWait(driver, 50).until(
        EC.visibility_of_element_located((By.XPATH, "//li[@class='has-dropdown not-click']/a[text()='SPAJ']"))
    ).click()
    #actions = ActionChains(driver)
    #actions.move_to_element(SPAJmenu).perform()
    print("Hover berhasil")

    time.sleep(2)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/Insubsyt2/Transactions/SPAJ']"))
    ).click()

    #POM search SPAJ
    SPAJ.search(pemegangPolis)
    time.sleep(5)
    print("berhasil serach pemegang polis...")

    #POM href upload
    referral.hrefUpload(pemegangPolis)

    #POM upload files
    upload.upload_files()

    driver.find_element(By.XPATH, "//li[@class='has-dropdown not-click']/a[text()='SPAJ']")
    print("spaj terlihat...")
    time.sleep(5)
    WebDriverWait(driver, 50).until(
        EC.visibility_of_element_located((By.XPATH, "//li[@class='has-dropdown not-click']/a[text()='SPAJ']"))
    ).click()
    #actions = ActionChains(driver)
    #actions.move_to_element(SPAJmenu).perform()
    print("Hover berhasil")
    time.sleep(2)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/Insubsyt2/Transactions/SPAJ']"))
    ).click()

    SPAJ.search(pemegangPolis)
    time.sleep(5)

    referral.hrefSendToSales(pemegangPolis)

    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='expand button']"))
    ).click()
    print("Berhasil mengirim ke Sales Leader")

    wait.until(EC.element_to_be_clickable((By.XPATH, "//textarea[@id='notes']"))).send_keys(notes)
    time.sleep(3)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='beforesend']"))).click()
    time.sleep(5)

    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='status-msg' and contains(normalize-space(), 'Berhasil dikirim')]")))
    time.sleep(3)
    print("flow berhasil...")
