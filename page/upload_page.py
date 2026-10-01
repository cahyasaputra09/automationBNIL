from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver
import time
from selenium.webdriver.common.action_chains import ActionChains

class uploadPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

        self.hrefDokumenLainnya = (By.XPATH, "//a[text()='Dokumen Lainnya']")

        self.SPAJTrigger = (By.XPATH, "//input[@id='fileloadlist[0]' and not(@hidden)]")
        self.ilustrasiTrigger = (By.XPATH, "//input[@id='fileloadlist[1]' and not(@hidden)]")
        self.KTPTrigger = (By.XPATH, "//input[@id='fileloadlist[3]' and not(@hidden)]")
        self.formReferralTrigger = (By.XPATH, "//input[@id='fileloadlist[12]' and not(@hidden)]")

        self.copyBukuTabunganTrigger = (By.XPATH, "//input[@id='fileloadlisting[3]' and not(@hidden)]")
        self.suratKuasaDebitTrigger = (By.XPATH, "//input[@id='fileloadlisting[6]' and not(@hidden)]")
        self.formPernyataanPengajuanTrigger = (By.XPATH, "//input[@id='fileloadlisting[24]' and not(@hidden)]")
        self.formPernyataanNasabah = (By.XPATH, "//input[@id='fileloadlisting[28]' and not(@hidden)]")

        self.KTPCheck = (By.XPATH, "//input[@id='no' and @name='isLiveCam[3]']/following-sibling::label/preceding-sibling::span[@class='custom radio']")

        self.uploadUtama = (By.XPATH, "(//button[@class='button right small'])[1]")
        self.uploadLainnya = (By.XPATH, "(//button[@class='button right small'])[2]")

    def upload_files(self):
        self.wait.until(EC.element_to_be_clickable(self.SPAJTrigger)).send_keys(r"C:\Users\zoyadzaka\Downloads\REFERRAL-9210355558.pdf")
        print("DEBUG: file berhasil di upload...")

        self.wait.until(EC.element_to_be_clickable(self.ilustrasiTrigger)).send_keys(r"C:\Users\zoyadzaka\Downloads\REFERRAL-9210355558.pdf")
        print("DEBUG: file ilustrasi berhasil di upload...")

        self.wait.until(EC.element_to_be_clickable(self.KTPCheck)).click()
        print("DEBUG: KTP check berhasil di centang...")
        self.wait.until(EC.element_to_be_clickable(self.KTPTrigger)).send_keys(r"C:\Users\zoyadzaka\Downloads\REFERRAL-9210355558.pdf")
        print("DEBUG: file KTP berhasil di upload...")

        self.wait.until(EC.element_to_be_clickable(self.formReferralTrigger)).send_keys(r"C:\Users\zoyadzaka\Downloads\REFERRAL-9210355558.pdf")
        print("DEBUG: file form referral berhasil di upload...")

        self.wait.until(EC.element_to_be_clickable(self.uploadUtama)).click()
        print("DEBUG: file utama berhasil di upload...")

        time.sleep(2)

        self.wait.until(EC.element_to_be_clickable(self.hrefDokumenLainnya)).click()
        print("DEBUG: Dokumen Lainnya berhasil di klik...")

        time.sleep(3)

        self.wait.until(EC.element_to_be_clickable(self.copyBukuTabunganTrigger)).send_keys(r"C:\Users\zoyadzaka\Downloads\REFERRAL-9210355558.pdf")
        print("DEBUG: file copy buku tabungan berhasil di upload...")

        self.wait.until(EC.element_to_be_clickable(self.suratKuasaDebitTrigger)).send_keys(r"C:\Users\zoyadzaka\Downloads\REFERRAL-9210355558.pdf")
        print("DEBUG: file surat kuasa debit berhasil di upload...")

        self.wait.until(EC.element_to_be_clickable(self.formPernyataanPengajuanTrigger)).send_keys(r"C:\Users\zoyadzaka\Downloads\REFERRAL-9210355558.pdf")
        print("DEBUG: file form pernyataan pengajuan berhasil di upload...")

        self.wait.until(EC.element_to_be_clickable(self.formPernyataanNasabah)).send_keys(r"C:\Users\zoyadzaka\Downloads\REFERRAL-9210355558.pdf")
        print("DEBUG: file form pernyataan nasabah berhasil di upload...")

        self.wait.until(EC.element_to_be_clickable(self.uploadLainnya)).click()
        print("DEBUG: file lainnya berhasil di upload...")

        time.sleep(5)
