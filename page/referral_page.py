from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver
import time
from selenium.webdriver.common.action_chains import ActionChains

class referralPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)
        self.refferHref = (By.XPATH, "//tr[td[normalize-space()='UCOK BABA'] and td[normalize-space()='PROPOSAL PRINTING']]//a[contains(normalize-space(),'Referral Form')]")
        self.uploadHref = (By.XPATH, "//tr[td[normalize-space()='UCOK BABA'] and td[normalize-space()='PROPOSAL PRINTING']]//a[contains(normalize-space(),'Upload')]")
        self.sendToSales = (By.XPATH, "//tr[td[normalize-space()='UCOK BABA'] and td[normalize-space()='PROPOSAL PRINTING']]//a[contains(normalize-space(),'Send To Sales Leader')]")

        self.CIFInput = (By.ID, "cifnasabah")
        self.statusPegawaiTrigger = (By.XPATH, "//span[@id='select2-statuspegawai-container']")
        self.NPPpegawaiTrigger = (By.XPATH,"//input[@id='referral-labelLG']")
        self.kodeCabangTrigger = (By.XPATH, "//span[@id='select2-kodecabangpenutup-container']")
        self.divisiTrigger = (By.XPATH, "//span[@id='select2-divisiref-container']")
        self.namaInput = (By.XPATH, "//input[@id='namapetugasoutlet']")
        self.NPPInput = (By.XPATH, "//input[@id='npppetugasoutlet']")

        self.updateButton = (By.XPATH, "//button[@class='small button right']")
        self.cetakButton = (By.XPATH, "//button[@id='approval-button' and @class='small button expand right']")
    def hrefRefferal(self, pemegangPolis):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//tr[td[normalize-space()='{pemegangPolis}'] and td[normalize-space()='PROPOSAL PRINTING']]//a[contains(normalize-space(),'Referral Form')]"))).click()

    def hrefUpload(self, pemegangPolis):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//tr[td[normalize-space()='{pemegangPolis}'] and td[normalize-space()='PROPOSAL PRINTING']]//a[contains(normalize-space(),'Upload')]"))).click()

    def hrefSendToSales(self, pemegangPolis):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//tr[td[normalize-space()='{pemegangPolis}'] and td[normalize-space()='PROPOSAL PRINTING']]//a[contains(normalize-space(),'Send To Sales Leader')]"))).click()

    def updateRefferal(self, CIF, statusPegawai, kodeCabang, divisi, nama, NPPpegawai, NPPpemimpin):
        #self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='lg' and @type='checkbox']"))).click()
        checkbox_input = self.driver.find_element(By.XPATH, "//input[@id='lg' and @type='checkbox']")
        is_checked = checkbox_input.get_attribute("checked")

        # kalau belum dicheck (atribut checked None), baru klik span-nya
        if is_checked is None:
            checkbox_span = self.driver.find_element(By.XPATH, "//input[@id='lg']/following-sibling::span")
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='lg' and @type='checkbox']"))).click()
            print("Checkbox diklik karena belum dicheck.")
        else:
            print("Checkbox sudah dicheck, tidak perlu klik.")


        self.wait.until(EC.element_to_be_clickable(self.CIFInput)).clear()
        self.wait.until(EC.element_to_be_clickable(self.CIFInput)).send_keys(CIF)
        print("DEBUG: BERHASIL MEMILIH CIF...")

        self.wait.until(EC.element_to_be_clickable(self.statusPegawaiTrigger)).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//li[@role='option' and text()='{statusPegawai}']")))
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//li[@role='option' and text()='{statusPegawai}']"))).click()
        print("DEBUG: BERHASIL MEMILIH STATUS PEGAWAI...")

        self.wait.until(EC.element_to_be_clickable(self.NPPpegawaiTrigger)).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//tr[td/b[normalize-space()='{NPPpegawai}']]//a[normalize-space()='CHOOSE']")))
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//tr[td/b[normalize-space()='{NPPpegawai}']]//a[normalize-space()='CHOOSE']"))).click()
        print("DEBUG: BERHASIL MEMILIH NPP PEGAWAI...")

        time.sleep(3)
        self.wait.until(EC.element_to_be_clickable(self.kodeCabangTrigger)).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//li[@role='option' and text()='{kodeCabang}']")))
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//li[@role='option' and text()='{kodeCabang}']"))).click()
        print("DEBUG: BERHASIL MEMILIH KODE CABANG...")

        self.wait.until(EC.element_to_be_clickable(self.divisiTrigger)).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//li[@role='option' and text()='{divisi}']")))
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//li[@role='option' and text()='{divisi}']"))).click()
        print("DEBUG: BERHASIL MEMILIH DIVISI...")

        self.wait.until(EC.element_to_be_clickable(self.namaInput)).clear()
        self.wait.until(EC.element_to_be_clickable(self.namaInput)).send_keys(nama)
        print("DEBUG: BERHASIL MEMILIH NAMA...")

        self.wait.until(EC.element_to_be_clickable(self.NPPInput)).clear()
        self.wait.until(EC.element_to_be_clickable(self.NPPInput)).send_keys(NPPpemimpin)
        print("DEBUG: BERHASIL MEMILIH NPP PEMIMPIN...")

        self.wait.until(EC.element_to_be_clickable(self.updateButton)).click()
        print("DEBUG: BERHASIL MENGUPDATE REFERAL...")

        self.wait.until(EC.presence_of_element_located(self.cetakButton))
        self.wait.until(EC.element_to_be_clickable(self.cetakButton)).click()
        print("DEBUG: BERHASIL MENCETAK REFERAL...")

        time.sleep(3)