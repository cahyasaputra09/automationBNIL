import select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementNotInteractableException, TimeoutException
import time
from selenium.webdriver.support.select import Select


class SPAJPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.status_trigger = (By.XPATH, "//a[@class='current' and contains(text(), '--Pilih Jenis Status--')]")
        
        self.kategori_trigger = (By.XPATH, "//a[@class='current' and contains(text(), '--Cari Berdasarkan--')]")

        self.tgl_awal = (By.ID, "query1")
        self.tgl_akhir = (By.ID, "query2")

        self.searchBar = (By.ID, "query")
        self.searchButton = (By.XPATH, "//button[@type='submit']")

        self.search_button = (By.XPATH, "//button[@class='postfix small-2 columns end' and @type='submit']")

        # Form CPP
        self.IDVerifikasiButton = (By.ID, "verificationButton1")
        self.phoneVerifikasiButton = (By.ID, "verificationButton2")

        self.tempatLahir = (By.ID, "tempatlahir")
        self.identitasTrigger = (By.XPATH, "//a[@class='current' and contains(text(), 'Pilih Jenis Identitas')]")
        self.nomorIdentitas = (By.ID, "nomoridentitas")
        self.ibu = (By.ID, "namaibu")
        self.agamaTrigger = (By.XPATH, "//a[@class='current' and contains(text(), 'Pilih Agama')]")
        self.nasabahPriorityTrigger = (By.XPATH, "//a[@class='current' and contains(text(), 'Pilih Nasabah Priority BNI')]")
        self.searchPekerjaan = (By.XPATH, "//input[@type='text' and @placeholder='Cari Nama Jenis Pekerjaan']")
        self.bidangUsahaTrigger = (By.XPATH, "//a[@class='current' and contains(text(), 'Pilih Bidang Usaha')]")
        self.namaPerusahaan = (By.ID, "namaperusahaan")
        self.jabatan = (By. ID, "jabatancpp")
        self.rincianTugasTrigger = (By.XPATH, "//a[@class='current' and contains(text(), 'ADMINISTRASI')]")
        self.lokasiKerjaTrigger = (By.XPATH, "//a[@class='current' and contains(text(), 'Pilih Lokasi Tempat Kerja')]")
        self.statusTempatTinggalTrigger = (By.XPATH, "//a[@class='current' and contains(text(), 'Pilih Status Tempat Tinggal')]")
        self.tipeAlamatTrigger = (By.XPATH, "//a[@class='current' and contains(text(), 'Pilih Tipe Alamat')]")
        self.komplek = (By.ID, "alamat")
        self.blok = (By.ID, "blok")
        self.RT = (By.ID, "rt")
        self.RW = (By.ID, "rw")
        self.provinsiTrigger = (By.XPATH, "//a[@class='current' and contains(text(), 'Pilih Provinsi')]")
        self.kotaTrigger = (By.XPATH, "//a[@class='current' and contains(text(), 'Choose Regency')]")
        self.kecamatanTrigger = (By.XPATH, "//a[@class='current' and contains(text(), 'Choose Sub District')]")
        self.kelurahanTrigger = (By.XPATH, "//a[@class='current' and contains(text(), 'Choose Villages')]")
        self.kodePosTrigger = (By.XPATH, "//a[@class='current' and contains(text(), 'Choose ZipCode')]")
        self.NPWP = (By.ID, "npwp")
        self.tinggiBadan = (By.ID, "height")
        self.beratBadan = (By.ID, "weight")
        self.relationAgent = (By.ID, "relationagent")
        self.timeAgent = (By.ID, "timeagent")
        self.kondisiCPPTrigger1 = (By.XPATH, "(//a[@class='current' and contains(text(), 'Pilih Kondisi CPP')])[1]")
        self.kondisiCPPTrigger2 = (By.XPATH, "(//a[@class='current' and contains(text(), 'Pilih Kondisi CPP')])[2]")
        self.kondisiCPPTrigger3 = (By.XPATH, "(//a[@class='current' and contains(text(), 'Pilih Kondisi CPP')])[3]")
        self.kondisiCPPTrigger4 = (By.XPATH, "(//a[@class='current' and contains(text(), 'Pilih Kondisi CPP')])[4]")
        self.pengirimanPolisTrigger = (By.XPATH, "//a[@class='current' and contains(text(), 'Pilih Cara Pengiriman Polis')]")

        #form PP
        self.calonPembayarPremiTrigger = (By.XPATH, "//a[@class='current' and contains(text(), 'Pilih Calon Pembayar Premi')]")
        self.penghasilanKotorTrigger = (By.XPATH, "//a[@class='current' and contains(text(), 'Pilih Penghasilan Kotor Pertahun')]")
        self.penghasilLainInput = (By.XPATH, "//div[@class='large-2 columns']/input[@name='penghasilanlain']")
        self.penghasilLainTrigger = (By.XPATH, "//a[@class='current' and contains(text(), 'Pilih Penghasilan Lain')]")
        self.sumberDanaTrigger = (By.XPATH, "(//a[contains(@class, 'current') and contains(normalize-space(.), 'Pilih Sumber Dana Pembayaran Premi')])[2]")
        self.caraBayarPremi1Trigger = (By.XPATH, "//a[@class='current' and text()='Pilih Cara Bayar Premi Pertama']")
        self.caraBayarPremi2Trigger = (By.XPATH, "//a[@class='current' and text()='Pilih Cara Bayar Premi Lanjutan']")
        self.norekPremi2Field = (By.XPATH, "//input[@id='nomorrekening']")
        self.namaRekening = (By.ID, "namaRekening")
        self.norek2 = (By.ID, "norek")
        self.cabangBank = (By.XPATH, "//input[@id='cabangbank']")
        self.rekeningSamaCheckbox = (By.XPATH, "//label[strong[contains(., 'Silahkan Klik, Jika Nama Data Rekening')]]/preceding::span[@class='custom checkbox'][1]")
        self.PPSubmit = (By.XPATH, "//button[@id='approval-button4']")

        #form Pertg
        self.submitPertg = (By.XPATH, "//button[@id='approval-button5']")

        #form PMPL
        self.addPMPLButton = (By.XPATH, "//input[@value='Tambah Penerima Manfaat']")
        self.namaLengkap = (By.XPATH, "//input[@name='namalengkappm']")
        self.namaBelakang = (By.XPATH, "//input[@name='namabelakangpm']")
        self.genderTrigger = (By.XPATH, "//select[@class='ben-gender']")
        self.birthday = (By.XPATH, "//input[@name='birthdaypm']")
        self.relationTrigger = (By.XPATH, "//select[@name='relation']")
        self.identityTrigger = (By.XPATH, "//select[@name='identity']")
        self.nomorIdentity = (By.XPATH, "//input[@name='identitynopm']")
        self.presentase = (By.XPATH, "//input[@name='prosentasepm']")
        self.submitPMPL = (By.XPATH, "//button[text()='Simpan Data Penerima Manfaat']")

        #form PKes
        self.submitPKes = (By.XPATH, "//button[@id='approval-button7']")   
        self.submitPKes2 = (By.XPATH, "//button[@id='approval-button8']")
        self.submitPKes3 = (By.XPATH, "//button[@id='approval-button9']")

        #form SKDebet
        self.pemilikRekeningField = (By.XPATH, "//input[@id='pemilikrekening' and @type='text']")
        self.hubunganCTTrigger = (By.XPATH, "(//a[@class='current' and text()='Pilih Hubungan CPP dengan CT'])[2]")
        self.submitSKDebet = (By.XPATH, "//button[@id='approval-button10']")

        #form FWNA
        self.submitFWNA = (By.XPATH, "//button[@id='approval-button11']")


    def _safe_input_text(self, locator, text, element_name):
        """Safely input text with multiple methods"""
        try:
            print(f"DEBUG: Mencari {element_name}...")
            element = self.wait.until(EC.element_to_be_clickable(locator))
            
            # Method 1: Clear and send_keys
            try:
                element.clear()
                element.send_keys(text)
                print(f"DEBUG: {element_name} '{text}' berhasil diinput (Method 1)")
                return True
            except:
                pass
            
            # Method 2: JavaScript
            try:
                self.driver.execute_script("arguments[0].value = '';", element)
                self.driver.execute_script("arguments[0].value = arguments[1];", element, text)
                self.driver.execute_script("arguments[0].dispatchEvent(new Event('input'));", element)
                self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", element)
                print(f"DEBUG: {element_name} '{text}' berhasil diinput (Method 2 - JS)")
                return True
            except:
                pass
                
            # Method 3: Click first then type
            try:
                element.click()
                time.sleep(0.5)
                element.clear()
                time.sleep(0.5)
                for char in text:
                    element.send_keys(char)
                    time.sleep(0.1)
                print(f"DEBUG: {element_name} '{text}' berhasil diinput (Method 3 - Char by char)")
                return True
            except:
                pass
                
            print(f"WARNING: Gagal input {element_name}")
            return False
            
        except Exception as e:
            print(f"ERROR: Tidak bisa menemukan {element_name}: {e}")
            return False
        
    def filterDataSPAJ(self, status, tglAwal, tglAkhir, kategori):
        self.wait.until(EC.element_to_be_clickable(self.status_trigger)).click()
        print("tombol status berhasil klik")

        self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//ul/li[@class='' and contains(text(), '{status}')]")))
        print("pilihan status terlihat")

        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//ul/li[@class='' and contains(text(), '{status}')]"))).click()
        print("pilihan status berhasil diklik")

        if not self._safe_input_text(self.tgl_awal, tglAwal, "Tanggal Awal"):
            raise Exception("gagal pilih tanggal awal")

        if not self._safe_input_text(self.tgl_akhir, tglAkhir, "Tanggal Akhir"):
            raise Exception("gagal pilih tanggal akhir")

        self.wait.until(EC.element_to_be_clickable(self.kategori_trigger)).click()
        print("tombol kategori berhasil diklik")

        self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//ul/li[@class='' and contains(text(), '{kategori}')]")))
        print("pilihan kategori terlihat")

        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//ul/li[@class='' and contains(text(), '{kategori}')]"))).click()
        print("pilihan kategori berhasil diklik")

        self.driver.find_element(*self.search_button).click()
        return True
    

    def formCPP(self, tempatLahir, identitas, nomorIdentitas, ibu, agama, nasabahPriority, pekerjaan, bidangUsaha, 
                namaPerusahaan, jabatan, rincianTugas, lokasiKerja, statusTempatTinggal, tipeAlamat, komplek, blok, 
                rt, rw, provinsi, kota, kecamatan, kelurahan, kodePos, NPWP, tinggiBadan, beratBadan, relationAgent, 
                timeAgent, kondisiCPP1, pengirimanPolis):
        time.sleep(3)
        tempat_lahir_field = self.wait.until(
            EC.visibility_of_element_located(self.tempatLahir)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", tempat_lahir_field)
        tempat_lahir_field.clear()
        tempat_lahir_field.send_keys(tempatLahir)

        self.wait.until(EC.element_to_be_clickable(self.identitasTrigger)).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//ul/li[contains(text(), '{identitas}')]")))
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//ul/li[contains(text(), '{identitas}')]"))).click()

        self.wait.until(EC.element_to_be_clickable(self.nomorIdentitas)).send_keys(nomorIdentitas)
        self.wait.until(EC.element_to_be_clickable(self.IDVerifikasiButton)).click()

        time.sleep(10)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='small-1 columns text-center']/span[@class='custom checkbox']"))).click()

        self.wait.until(EC.element_to_be_clickable(self.ibu)).send_keys(ibu)

        self.wait.until(EC.element_to_be_clickable(self.agamaTrigger)).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//ul/li[contains(text(), '{agama}')]")))
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//ul/li[contains(text(), '{agama}')]"))).click()

        self.wait.until(EC.element_to_be_clickable(self.nasabahPriorityTrigger)).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//ul/li[contains(text(), '{nasabahPriority}')]")))
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//ul/li[contains(text(), '{nasabahPriority}')]"))).click()

        self.wait.until(EC.element_to_be_clickable((By.ID, "occupation-label1"))).click()
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(self.searchPekerjaan)).send_keys(pekerjaan)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']/i[@class='icon-search']"))).click()
        time.sleep(5)
        choose_btn = self.driver.find_element(
            By.XPATH,f"//td[normalize-space()='{pekerjaan}']/preceding-sibling::td/a"
        )
        choose_btn.click()
        time.sleep(2)

        self.wait.until(EC.element_to_be_clickable(self.bidangUsahaTrigger)).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//ul/li[contains(text(), '{bidangUsaha}')]")))
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//ul/li[contains(text(), '{bidangUsaha}')]"))).click()

        self.wait.until(EC.element_to_be_clickable(self.namaPerusahaan)).send_keys(namaPerusahaan)

        jabatan_field = self.wait.until(EC.element_to_be_clickable(self.jabatan))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", jabatan_field)
        jabatan_field.clear()
        jabatan_field.send_keys(jabatan)

        self.wait.until(EC.element_to_be_clickable(self.rincianTugasTrigger)).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//ul/li[contains(text(), '{rincianTugas}')]")))
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//ul/li[contains(text(), '{rincianTugas}')]"))).click()

        self.wait.until(EC.element_to_be_clickable(self.lokasiKerjaTrigger)).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//ul/li[contains(text(), '{lokasiKerja}')]")))
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//ul/li[contains(text(), '{lokasiKerja}')]"))).click()

        self.wait.until(EC.element_to_be_clickable(self.statusTempatTinggalTrigger)).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//ul/li[contains(text(), '{statusTempatTinggal}')]")))
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//ul/li[contains(text(), '{statusTempatTinggal}')]"))).click()

        checkbox = self.driver.find_element(By.XPATH, "//input[@id='alamatsama']/following-sibling::span[@class='custom checkbox']")
        checkbox.click()

        try:
            # Tunggu dan scroll ke dropdown
            dropdown_trigger = self.wait.until(EC.element_to_be_clickable(self.tipeAlamatTrigger))
        
            actions = ActionChains(self.driver)
            actions.move_to_element(dropdown_trigger).click().perform()
            print("DEBUG: Dropdown diklik dengan ActionChains...")
        
            # Tunggu dropdown menu
            time.sleep(1)
        
            # Cari dan klik opsi
            option_xpath = f"//ul/li[normalize-space(text())='{tipeAlamat}']"
            option_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
        
            actions.move_to_element(option_element).click().perform()
            print(f"DEBUG: Berhasil memilih '{tipeAlamat}' dengan ActionChains")
        
        except Exception as e:
            print(f"ERROR: ActionChains gagal - {str(e)}")
            raise

        self.wait.until(EC.element_to_be_clickable(self.komplek)).send_keys(komplek)

        self.wait.until(EC.element_to_be_clickable(self.blok)).send_keys(blok)

        self.wait.until(EC.element_to_be_clickable(self.RT)).send_keys(rt)
        self.wait.until(EC.element_to_be_clickable(self.RW)).send_keys(rw)

        self.wait.until(EC.element_to_be_clickable(self.provinsiTrigger)).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//ul/li[contains(text(), '{provinsi}')]")))
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//ul/li[contains(text(), '{provinsi}')]"))).click()

        self.wait.until(EC.element_to_be_clickable(self.kotaTrigger)).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//ul/li[contains(text(), '{kota}')]")))
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//ul/li[contains(text(), '{kota}')]"))).click()

        self.wait.until(EC.element_to_be_clickable(self.kecamatanTrigger)).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//ul/li[contains(text(), '{kecamatan}')]")))
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//ul/li[contains(text(), '{kecamatan}')]"))).click()



        # scroll ke elemen biar kelihatan
        self.wait.until(EC.element_to_be_clickable(self.kelurahanTrigger)).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//ul/li[contains(text(), '{kelurahan}')]")))
        print("DEBUG: BERHASIL LIAT OPSI LURAH...")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//ul/li[contains(text(), '{kelurahan}')]"))).click()
        print("DEBUG: BERHASIL PILIH OPSI KELURAHAN...")

        self.wait.until(EC.element_to_be_clickable(self.kodePosTrigger)).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//ul/li[contains(text(), '{kodePos}')]")))
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//ul/li[contains(text(), '{kodePos}')]"))).click()

        # scroll ke phoneVerifikasiButton
        self.wait.until(EC.visibility_of_element_located(self.phoneVerifikasiButton))
        print("DEBUG: BERHASIL LIAT TOMBOL VERIFIKASI...")
        self.wait.until(EC.element_to_be_clickable(self.phoneVerifikasiButton))
        print("DEBUG: TOMBOL VERIFIKASI DAPAT DI CLICK...")
        self.wait.until(EC.element_to_be_clickable(self.phoneVerifikasiButton)).click()
        print("DEBUG: BERHASIL KLIK TOMBOL VERIFIKASI...")




        #phone_button = self.wait.until(EC.visibility_of_element_located(self.phoneVerifikasiButton))
        #self.driver.execute_script("arguments[0].scrollIntoView(true);", phone_button)
        #self.wait.until(EC.element_to_be_clickable(self.phoneVerifikasiButton)).click()
        time.sleep(4)
        # scroll ke NPWP
        npwp_input = self.wait.until(EC.visibility_of_element_located(self.NPWP))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", npwp_input)
        npwp_input.send_keys(NPWP)

        self.wait.until(EC.element_to_be_clickable(self.tinggiBadan)).clear()
        self.wait.until(EC.element_to_be_clickable(self.tinggiBadan)).send_keys(tinggiBadan)

        self.wait.until(EC.element_to_be_clickable(self.beratBadan)).clear()
        self.wait.until(EC.element_to_be_clickable(self.beratBadan)).send_keys(beratBadan)


        self.wait.until(EC.element_to_be_clickable(self.relationAgent)).send_keys(relationAgent)

        self.wait.until(EC.element_to_be_clickable(self.timeAgent)).send_keys(timeAgent)

        time.sleep(5)

        print("DEBUG: LANJUT KONDISI CPP...")
        elems = self.driver.find_elements(By.XPATH, "//a[contains(text(), 'Pilih Kondisi CPP')]")
        print("DEBUG: ketemu berapa elemen CPP?", len(elems))

        cpp1 = self.wait.until(EC.element_to_be_clickable(self.kondisiCPPTrigger1))
        cpp1.click()
        print("DEBUG: BERHASIL BUKA OPSI...")
        self.wait.until(EC.visibility_of_element_located((By.XPATH, f"(//a[@class='current' and contains(text(),'Pilih Kondisi CPP')])[1]/following-sibling::ul/li[normalize-space()='{kondisiCPP1}']")))
        print("DEBUG: BERHASIL LIAT OPSI CPP 1...")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"(//a[@class='current' and contains(text(),'Pilih Kondisi CPP')])[1]/following-sibling::ul/li[normalize-space()='{kondisiCPP1}']"))).click()
        print("DEBUG: BERHASIL PILIH OPSI CPP 1...")

        cpp2 = self.wait.until(EC.element_to_be_clickable(self.kondisiCPPTrigger1))
        cpp2.click()
        print("DEBUG: BERHASIL BUKA OPSI...")
        self.wait.until(EC.visibility_of_element_located((By.XPATH, f"(//a[@class='current' and contains(text(),'Pilih Kondisi CPP')])[1]/following-sibling::ul/li[normalize-space()='{kondisiCPP1}']")))
        print("DEBUG: BERHASIL LIAT OPSI CPP 2...")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"(//a[@class='current' and contains(text(),'Pilih Kondisi CPP')])[1]/following-sibling::ul/li[normalize-space()='{kondisiCPP1}']"))).click()
        print("DEBUG: BERHASIL PILIH OPSI CPP 2...")

        cpp3 = self.wait.until(EC.element_to_be_clickable(self.kondisiCPPTrigger1))
        cpp3.click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, f"(//a[@class='current' and contains(text(),'Pilih Kondisi CPP')])[1]/following-sibling::ul/li[normalize-space()='{kondisiCPP1}']")))
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"(//a[@class='current' and contains(text(),'Pilih Kondisi CPP')])[1]/following-sibling::ul/li[normalize-space()='{kondisiCPP1}']"))).click()

        cpp4 = self.wait.until(EC.element_to_be_clickable(self.kondisiCPPTrigger1))
        cpp4.click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, f"(//a[@class='current' and contains(text(),'Pilih Kondisi CPP')])[1]/following-sibling::ul/li[normalize-space()='{kondisiCPP1}']")))
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"(//a[@class='current' and contains(text(),'Pilih Kondisi CPP')])[1]/following-sibling::ul/li[normalize-space()='{kondisiCPP1}']"))).click()

        self.wait.until(EC.element_to_be_clickable(self.pengirimanPolisTrigger)).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//ul/li[contains(text(), '{pengirimanPolis}')]")))
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//ul/li[contains(text(), '{pengirimanPolis}')]"))).click()

        self.wait.until(EC.element_to_be_clickable((By.ID, "approval-button2"))).click()


    def formPP(self, tujuanPengajuan, calonPembayarPremi, penghasilanKotor, sumberDana, caraPembayaranPremi1, caraPembayaranPremi2, norek1, cabangBank, norek2, penghasilanLain):
            self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//label[contains(., '{tujuanPengajuan}')]//span[@class='custom checkbox']")))
            print("DEBUG: DANA PENSIUN checkbox is visible...")
            checkbox = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//label[contains(., '{tujuanPengajuan}')]//span[@class='custom checkbox']")))
            self.driver.execute_script("arguments[0].click();", checkbox)
            time.sleep(2)
            self.wait.until(EC.element_to_be_clickable(self.calonPembayarPremiTrigger)).click()
            self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//ul/li[contains(text(), '{calonPembayarPremi}')]")))
            print("DEBUG: BERHASIL LIAT OPSI...")
            self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//ul/li[contains(normalize-space(.), '{calonPembayarPremi}')]"))).click()
            print("DEBUG: BERHASIL KLIK OPSI...")

            self.wait.until(EC.element_to_be_clickable(self.penghasilanKotorTrigger)).click()
            self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//ul/li[contains(text(), '{penghasilanKotor}')]")))
            self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//ul/li[contains(text(), '{penghasilanKotor}')]"))).click()
            self.wait.until(EC.visibility_of_element_located(self.penghasilLainInput))
            print("DEBUG: PENGHASIL LAIN INPUT TERLIHAT...")
            self.wait.until(EC.element_to_be_clickable(self.penghasilLainInput)).send_keys("jualan")
            print("DEBUG: BERHASIL INPUT PENGHASIL LAIN...")
            self.wait.until(EC.visibility_of_element_located(self.penghasilLainTrigger))
            print("DEBUG: PENGHASIL LAIN TRIGGER TERLIHAT...")
            self.wait.until(EC.element_to_be_clickable(self.penghasilLainTrigger)).click()
            time.sleep(1)

            option = self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, f"//a[contains(normalize-space(text()), 'Pilih Penghasilan Lainnya')]/following-sibling::ul/li[normalize-space(text())='{penghasilanLain}']")
            ))
            actions = ActionChains(self.driver)
            actions.move_to_element(option).pause(0.5).click().perform()
            print("DEBUG: BERHASIL SELECT DROPDOWN PENGHASIL LAIN...")

            dropdown_toggle = self.wait.until(EC.visibility_of_element_located((self.sumberDanaTrigger)))

            dropdown_toggle.click()
            print("DEBUG: BERHASIL KLIK DROPDOWN SUMBER DANA...")

            self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//ul/li[text()='{sumberDana}']"))).click()

            self.wait.until(EC.element_to_be_clickable(self.caraBayarPremi1Trigger)).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//ul/li[text()='{caraPembayaranPremi1}']"))).click()

            self.wait.until(EC.element_to_be_clickable(self.caraBayarPremi2Trigger)).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//ul/li[text()='{caraPembayaranPremi2}']"))).click()
            self.wait.until(EC.element_to_be_clickable(self.norekPremi2Field)).send_keys(norek1)

            self.wait.until(EC.element_to_be_clickable(self.rekeningSamaCheckbox)).click()

            self.wait.until(EC.element_to_be_clickable(self.norek2))
            self.wait.until(EC.element_to_be_clickable(self.norek2)).send_keys(norek2)

            self.wait.until(EC.element_to_be_clickable(self.cabangBank))
            print("DEBUG: Cabang Bank input field is visible...")
            self.wait.until(EC.element_to_be_clickable(self.cabangBank)).send_keys(cabangBank)

            self.wait.until(EC.element_to_be_clickable(self.PPSubmit)).click()

            time.sleep(2)

            submit = self.wait.until(EC.element_to_be_clickable(self.submitPertg))
            self.driver.execute_script("arguments[0].click();", submit)

    def formPMPL(self, namaLengkap, namaBelakang, gender, birthday, relation, identity, nomorIdentity, presentase):

        addButton = self.wait.until(EC.element_to_be_clickable(self.addPMPLButton))
        self.driver.execute_script("arguments[0].click();", addButton)
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(self.namaLengkap)).send_keys(namaLengkap)
        self.wait.until(EC.element_to_be_clickable(self.namaBelakang)).send_keys(namaBelakang)
        self.wait.until(EC.element_to_be_clickable(self.genderTrigger)).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//select[@class='ben-gender']/option[text()='{gender}']"))).click()
        if not self._safe_input_text(self.birthday, birthday, "birthdaypm"):
            raise Exception("Gagal input tanggal lahir")
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(self.relationTrigger)).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//select[@class='ben-relation']/option[text()='{relation}']"))).click()
        self.wait.until(EC.element_to_be_clickable(self.identityTrigger)).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//select[@class='ben-identity']/option[text()='{identity}']"))).click()
        self.wait.until(EC.element_to_be_clickable(self.nomorIdentity)).clear()
        self.wait.until(EC.element_to_be_clickable(self.nomorIdentity)).send_keys(nomorIdentity)
        self.wait.until(EC.element_to_be_clickable(self.presentase)).send_keys(presentase)
        self.wait.until(EC.element_to_be_clickable(self.submitPMPL)).click()
        time.sleep(2)

        submitPkes = self.wait.until(EC.element_to_be_clickable(self.submitPKes))
        self.driver.execute_script("arguments[0].scrollIntoView(true); arguments[0].click();", submitPkes)

        time.sleep(10)

        submitPkes2 = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.submitPKes2))
        self.driver.execute_script("arguments[0].scrollIntoView(true); arguments[0].click();", submitPkes2)
        print("DEBUG: SUBMITPKES2 is clicked")

        time.sleep(10)

        submitPkes3 = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.submitPKes3))
        self.driver.execute_script("arguments[0].scrollIntoView(true); arguments[0].click();", submitPkes3)
        print("DEBUG: SUBMITPKES3 is clicked")

        time.sleep(4)

        


    def formSKDebet(self, namaPemilikRek, hubPemilikRek):
        time.sleep(4)
        namarek = self.wait.until(EC.element_to_be_clickable(self.pemilikRekeningField))
        self.driver.execute_script("arguments[0].value = arguments[1];", namarek, namaPemilikRek)
        print("DEBUG: pemilikRekeningField is filled with", namaPemilikRek)
        time.sleep(10)

        try:
            # Tunggu element terlihat
            self.wait.until(EC.visibility_of_element_located(self.hubunganCTTrigger))
            print("DEBUG: hubCTTrigger is visible")

            # Scroll ke element
            trigger_element = self.driver.find_element(*self.hubunganCTTrigger)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", trigger_element)
            time.sleep(1)

            # Coba klik dengan berbagai method
            try:
                # Method 1: Regular click
                WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable(self.hubunganCTTrigger)).click()
                print("DEBUG: hubCTTrigger clicked with regular click")
            except:
                try:
                    # Method 2: JavaScript click
                    WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable(self.hubunganCTTrigger))
                    self.driver.execute_script("arguments[0].click();", trigger_element)
                    print("DEBUG: hubCTTrigger clicked with JS")
                except:
                    # Method 3: ActionChains
                    actions = ActionChains(self.driver)
                    actions.move_to_element(trigger_element).click().perform()
                    print("DEBUG: hubCTTrigger clicked with ActionChains")

            time.sleep(2)

            # Tunggu dan klik opsi
            self.wait.until(EC.visibility_of_element_located((By.XPATH, f"(//a[@class='current' and text()='Pilih Hubungan CPP dengan CT'])[2]/following-sibling::ul/li[normalize-space(.)='{hubPemilikRek}']")))
            print("DEBUG: hubCTOpsi is visible")

            hubunganCTOpsi = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"(//a[@class='current' and text()='Pilih Hubungan CPP dengan CT'])[2]/following-sibling::ul/li[normalize-space(.)='{hubPemilikRek}']")))
            self.driver.execute_script("arguments[0].click();", hubunganCTOpsi)
            print("DEBUG: hubCTOpsi is clicked", hubPemilikRek)

        except TimeoutException:
            print("DEBUG: hubCTTrigger is not visible")
            return

        submitSKDebet = self.wait.until(EC.element_to_be_clickable(self.submitSKDebet))
        self.driver.execute_script("arguments[0].click();", submitSKDebet)
        print("DEBUG: submitSKDebet is clicked")

        time.sleep(5)

        self.wait.until(EC.element_to_be_clickable(self.submitFWNA)).click()
        print("DEBUG: submitFWNA is clicked....")
        time.sleep(3)

    def search(self, pemegangPolis):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='current' and text()='--Cari Berdasarkan--']"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//ul/li[@class='' and text()='Nama Pemegang Polis']"))).click()
        self.wait.until(EC.element_to_be_clickable(self.searchBar)).send_keys(pemegangPolis)
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable(self.searchButton)).click()
        time.sleep(3)
        

