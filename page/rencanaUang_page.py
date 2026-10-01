from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementNotInteractableException, TimeoutException
import time
from selenium.webdriver.support.select import Select

class RencanaUangPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.fullName_field = (By.ID, "FullName")
        self.pengeluaran_field = (By.ID, "SumSpend")
        self.danaSedia_field = (By.ID, "SumInvest")
        self.anak_field = (By.ID, "SumChild")
        self.usia_field = (By.ID, "dob-year")

        self.status_trigger = (By.XPATH, "//a[@class='current' and contains(text(), 'Pilih Status Perkawinan')]")
        self.tujuan_trigger = (By.XPATH, "//a[@class='current' and contains(text(), 'Pilih Tujuan')]")
        self.submit_button = (By.XPATH, "//button[@type='submit' and contains(text(), 'Simpan Data')]")

    def form_rencanaUang(self, fullName, usiaOrTTL, pengeluaran, status, usia, danaSedia, anak, tujuan):
        self.wait.until(EC.element_to_be_clickable(self.fullName_field)).send_keys(fullName)
        print("DEBUG: FULL NAME BERHASIL...")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[@class='large-9 columns']/label[@for='{usiaOrTTL}']"))).click()
        print("DEBUG: RADIO USIA BERHASIL...")

        self.wait.until(EC.element_to_be_clickable(self.usia_field)).clear()
        self.wait.until(EC.element_to_be_clickable(self.usia_field)).send_keys(usia)
        print("DEBUG: USIA BERHASIL...")

        self.wait.until(EC.element_to_be_clickable(self.pengeluaran_field)).clear()
        self.wait.until(EC.element_to_be_clickable(self.pengeluaran_field)).send_keys(pengeluaran)
        print("DEBUG: PENGELUARAN BERHASIL...")

        self.wait.until(EC.element_to_be_clickable(self.danaSedia_field)).clear()
        self.wait.until(EC.element_to_be_clickable(self.danaSedia_field)).send_keys(danaSedia)
        print("DEBUG: DANA SEDIA BERHASIL...")

        self.wait.until(EC.element_to_be_clickable(self.status_trigger)).click()
        print("DEBUG: STATUS BERHASIL KLIK...")
        self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//ul/li[@class='' and contains(text(), '{status}')]")))
        print("DEBUG: STATUS TERLIHAT...")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//ul/li[@class='' and contains(text(), '{status}')]"))).click()
        print("DEBUG: STATUS SUDAH TERPILIH...")

        self.wait.until(EC.element_to_be_clickable(self.anak_field)).clear()
        self.wait.until(EC.element_to_be_clickable(self.anak_field)).send_keys(anak)
        print("DEBUG: ANAK BERHASIL...")

        self.wait.until(EC.element_to_be_clickable(self.tujuan_trigger)).click()
        print("DEBUG: TUJUAN BERHASIL KLIK...")
        self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//ul/li[@class='' and contains(text(), '{tujuan}')]")))
        print("DEBUG: TUJUAN TERLIHAT...")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//ul/li[@class='' and contains(text(), '{tujuan}')]"))).click()
        print("DEBUG: TUJUAN SUDAH TERPILIH...")

        self.wait.until(EC.element_to_be_clickable(self.submit_button)).click()