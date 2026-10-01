from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from conftest import driver
from utils.data_loader import load_excel_data, load_excel_data_merge
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
from page.login_page import LoginPage
from page.home_page import HomePage
from page.ilustrasi_page import IlustrasiPage
from page.SPAJ_page import SPAJPage
from page.upload_page import uploadPage
from page.referral_page import referralPage

@pytest.mark.parametrize("testDataBNIL", load_excel_data_merge("testData_login", "testData_buatSPAJ", "testData_PMPL", "testData_sales"))
def test_addSPAJ(driver, base_url, testDataBNIL):
    log = LoginPage(driver)
    ilustrasi = IlustrasiPage(driver)
    SPAJ = SPAJPage(driver)
    home = HomePage(driver)
    upload = uploadPage(driver)
    referral = referralPage(driver)
    wait = WebDriverWait(driver, 10)

    #inisialisasi
    kotaSPAJ = testDataBNIL.get("kotaSPAJ", "")
    tempatLahir = testDataBNIL.get("tempat lahir", "")
    jenisIdentitas = testDataBNIL.get("jenis identitas", "")
    nomorIdentitas = testDataBNIL.get("nomor identitas", "")
    ibu = testDataBNIL.get("ibu", "")
    agama = testDataBNIL.get("agama", "")
    nasabahPriority = testDataBNIL.get("nasabah priority", "")
    pekerjaan = testDataBNIL.get("pekerjaan", "")
    bidangUsaha = testDataBNIL.get("bidang usaha", "")
    perusahaan = testDataBNIL.get("perusahaan", "")
    jabatan = testDataBNIL.get("jabatan", "")
    tugas = testDataBNIL.get("tugas", "")
    lokasiKerja = testDataBNIL.get("lokasi kerja", "")
    statusTempatTinggal = testDataBNIL.get("status tempat tinggal", "")
    tipeAlamat = testDataBNIL.get("tipeAlamat", "")
    komplek = testDataBNIL.get("komplek", "")
    blok = testDataBNIL.get("blok", "")
    RT = testDataBNIL.get("RT", "")
    RW = testDataBNIL.get("RW", "")
    provinsi = testDataBNIL.get("provinsi", "")
    kota = testDataBNIL.get("kota", "")
    kecamatan = testDataBNIL.get("kecamatan", "")
    kelurahan = testDataBNIL.get("kelurahan", "")
    kodePos = testDataBNIL.get("kode pos", "")
    NPWP = testDataBNIL.get("NPWP", "")
    tinggiBadan = testDataBNIL.get("tinggi badan", "")
    beratBadan = testDataBNIL.get("berat badan", "")
    relationAgent = testDataBNIL.get("hub pemasar", "")
    timeAgent = testDataBNIL.get("berapa lama kenal", "")
    kondisiCPP1 = testDataBNIL.get("kondisiCPP1", "")
    pengirimanPolis = testDataBNIL.get("pengiriman polis", "")
    tujuanPengajuan = testDataBNIL.get("tujuan Pengajuan", "")
    calonPembayarPremi = testDataBNIL.get("calonPembayarPremi", "")
    penghasilanKotor = testDataBNIL.get("penghasilan kotor", "")
    sumberDana = testDataBNIL.get("sumber dana", "")
    caraPembayaranPremi1 = testDataBNIL.get("cara pembayaran premi 1", "")
    caraPembayaranPremi2 = testDataBNIL.get("cara pembayaran premi 2", "")
    norek1 = testDataBNIL.get("norek1", "")
    tipeKartuKredit = testDataBNIL.get("tipe kartu kredit", "")
    cabangBank = testDataBNIL.get("cabang bank", "")
    norek2 = testDataBNIL.get("norek2", "")
    namaPemilikRek = testDataBNIL.get("nama pemilik rek", "")
    penghasilanLain = testDataBNIL.get("penghasilanLain")
    hubPemilikRek = testDataBNIL.get("hub pemilik rek", "")
    namaDepan = testDataBNIL.get("nama depan", "")
    namaBelakang = testDataBNIL.get("nama belakang", "")
    kelamin = testDataBNIL.get("kelamin", "")
    ttl = testDataBNIL.get("ttl", "")
    hubTertanggung = testDataBNIL.get("hub tertanggung", "")
    identitas = testDataBNIL.get("identitas", "")
    noIdentitas = testDataBNIL.get("no identitas", "")
    presentaseManfaat = testDataBNIL.get("presentase manfaat", "")
    username = testDataBNIL.get("username", "")
    password = testDataBNIL.get("password", "")
    namaPolis = testDataBNIL.get("namaPolis", "")

    pemegangPolis = testDataBNIL.get("pemegangPolis", "")
    CIF = testDataBNIL.get("CIF", "")
    statusPegawai = testDataBNIL.get("statusPegawai", "")
    kodeCabang = testDataBNIL.get("kodeCabang", "")
    divisi = testDataBNIL.get("divisi", "")
    nama = testDataBNIL.get("nama", "")
    NPPpegawai = testDataBNIL.get("NPPpegawai", "")
    NPPpemimpin = testDataBNIL.get("NPPpemimpin", "")
    notes = testDataBNIL.get("notes", "")
    

     # Link
    driver.get(base_url)
    
    # POM login
    print("DEBUG: Melakukan login...")
    log.login(username, password)
    time.sleep(10)
    
    # POM page ilustrasi
    print("DEBUG: Navigasi ke halaman ilustrasi...")
    home.dataIlustrasi()
    time.sleep(3)
  
    #POM search ilustrasi calon pemegang polis
    print("DEBUG:SEARCH CALON PEMEGANG POLIS...")
    ilustrasi.search(namaPolis)

    time.sleep(5)
    details_buttons = driver.find_elements(By.XPATH, "//a[contains(text(),'Details')]")
    details_buttons[0].click()   # klik row ke-1
    time.sleep(5)

    driver.find_element(By.XPATH, "//a[normalize-space()='Daftar Ilustrasi']").click()

    radios = driver.find_elements(By.XPATH, "//input[@type='radio' and @name='action']")
    radios[0].click()

    el = wait.until(EC.element_to_be_clickable((By.ID, "b-apply")))
    driver.execute_script("arguments[0].click();", el)

    time.sleep(5)

    ttdKota = wait.until(EC.element_to_be_clickable((By.ID, "SignOfPlace")))
    ttdKota.send_keys(kotaSPAJ)
   
    wait.until(EC.element_to_be_clickable((By.ID, "btnSubmit"))).click()

    SPAJ.formCPP(tempatLahir, jenisIdentitas, nomorIdentitas, ibu, agama, nasabahPriority, pekerjaan, bidangUsaha, perusahaan, jabatan, tugas, lokasiKerja, statusTempatTinggal, tipeAlamat, komplek, blok, RT, RW, provinsi, kota, kecamatan, kelurahan, kodePos, NPWP, tinggiBadan, beratBadan, relationAgent, timeAgent, kondisiCPP1, pengirimanPolis)

    print("DEBUG data =", calonPembayarPremi, sumberDana, caraPembayaranPremi1, caraPembayaranPremi2, namaPemilikRek)

    SPAJ.formPP(tujuanPengajuan, calonPembayarPremi, penghasilanKotor, sumberDana, caraPembayaranPremi1, caraPembayaranPremi2, norek1, cabangBank, norek2, penghasilanLain)

    SPAJ.formPMPL(namaDepan, namaBelakang, kelamin, ttl, hubTertanggung, identitas, noIdentitas, presentaseManfaat)

    SPAJ.formSKDebet(namaPemilikRek, hubPemilikRek)

    #POM page data SPAJ
    home.dataSPAJ()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "(//td[@style='text-align: left; vertical-align: middle;']/a[text()='Print SPAJ'])[1]"))).click()

    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@id='beforeprint']"))
        ).click()

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

        print("header SPAJ terlihat")
    except:
        print("header SPAJ tidak terlihat")

    time.sleep(5)

    driver.close()
    driver.switch_to.window(main_window)
    time.sleep(3)

    driver.find_element(By.XPATH, "//li[@class='has-dropdown not-click']/a[text()='SPAJ']")
    print("spaj terlihat...")
    time.sleep(5)
    SPAJmenu = WebDriverWait(driver, 50).until(
        EC.visibility_of_element_located((By.XPATH, "//li[@class='has-dropdown not-click']/a[text()='SPAJ']"))
    ).click()
    print("Hover berhasil")

    time.sleep(2)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/Insubsyt2/Transactions/SPAJ']"))
    ).click()

    #POM search SPAJ
    SPAJ.search(pemegangPolis)
    time.sleep(5)
    print("berhasil serach pemegang polis...")

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