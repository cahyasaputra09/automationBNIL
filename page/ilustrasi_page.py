from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementNotInteractableException, TimeoutException
import time
from selenium.webdriver.support.select import Select


class IlustrasiPage  :
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
        # Locators
        self.name_field = (By.ID, "FirstName")
        self.lastName_field = (By.ID, "LastName")
        self.date_field = (By.ID, "BirthDate")
        self.no_hp = (By.ID, "MobilePhoneNumber")
        self.email_field=(By.ID, "EmailAddress")
        self.note_field=(By.ID, "Note")

        # Custom dropdown locators
        self.gender_dropdown_trigger = (By.XPATH, "//a[@class='current' and contains(text(), 'Pilih Jenis Kelamin')]")
        self.gender_dropdown_options = (By.XPATH, "//div[contains(@class, 'row collapse')]//ul//li")
        
        self.status_dropdown_trigger=(By.XPATH, "//a[@class='current' and contains(text(), 'Pilih Status Perkawinan')]")

        self.simpan_button = (By.XPATH, "//button[@class='small' and @type='submit']")

        self.buat_ilustrasi = (By.XPATH, "//div[@class='large-12 columns text-right']/a[@class='medium button']")
        self.radio_tertanggung_yes = (By.XPATH, "//input[@type='radio' and @value='0']")
        self.select_produk = (By.XPATH,"//select[@id='productName']")

        self.ilustrasi_submit = (By.XPATH, "//button[@class='button small success' and @type='submit']")

        self.formDataProduk_submit = (By.XPATH, "//button[@id='saveButton' and @class='expand small button right']")
        self.radio_premi = (By.XPATH, "//span[@class='custom radio']")

        self.bayar_select = (By.XPATH, "//a[@class='current' and contains(normalize-space(.), 'Pilih Cara Bayar')]")
        

        self.masa_select = (By.XPATH, "//a[@class='current' and contains(normalize-space(.), 'Pilih Masa Bayar')]")
        self.masa_option = lambda masa_bayar: (
            By.XPATH, f"//a[@class='current' and contains(normalize-space(.), 'Pilih Masa Bayar')]/following-sibling::ul/li[normalize-space(text())='{masa_bayar}']"
        )

        self.premiDasar_field = (By.XPATH, "//div[@class='large-3 columns']/input[@id='premidasar']")
        
        self.simpan_premi = (By.XPATH, "//div[@class='large-3 columns']/button[@id='saveButton']")

        self.save_pdf = (By.XPATH, "//div[@class='large-4 columns']/button[@id='b-download']")

    def _scroll_to_element(self, element):
        """Scroll to element to make it visible"""
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        time.sleep(1)

    def _safe_input_text(self, locator, text, element_name):
        """Safely input text with multiple methods"""
        try:
            print(f"DEBUG: Mencari {element_name}...")
            element = self.wait.until(EC.element_to_be_clickable(locator))
            self._scroll_to_element(element)
            
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

    def _handle_custom_dropdown(self, gender_text):
        """Handle custom dropdown for gender selection"""
        try:
            print(f"DEBUG: Mencari custom dropdown untuk gender...")
            
            # 1. Click dropdown trigger to open it
            trigger_element = self.wait.until(EC.element_to_be_clickable(self.gender_dropdown_trigger))
            self._scroll_to_element(trigger_element)
            trigger_element.click()
            time.sleep(2)  # Wait for dropdown to open
            
            print("DEBUG: Dropdown trigger diklik, mencari options...")
            
            # 2. Wait for options to be visible and get all options
            options = self.wait.until(EC.presence_of_all_elements_located(self.gender_dropdown_options))
            
            print(f"DEBUG: Ditemukan {len(options)} options:")
            for i, option in enumerate(options):
                option_text = option.text.strip()
                print(f"  [{i}] '{option_text}'")
            
            # 3. Find and click the matching option
            gender_lower = gender_text.lower()
            
            for option in options:
                option_text = option.text.strip().lower()
                print(f"DEBUG: Checking option: '{option_text}' vs '{gender_lower}'")
                
                if (("laki" in gender_lower and "laki" in option_text) or 
                    ("perempuan" in gender_lower and "perempuan" in option_text) or
                    ("male" in gender_lower and "male" in option_text) or
                    ("female" in gender_lower and "female" in option_text)):
                    
                    print(f"DEBUG: Match found! Clicking option: '{option.text}'")
                    
                    # Try multiple ways to click the option
                    try:
                        option.click()
                        print("DEBUG: Option clicked successfully (direct click)")
                        return True
                    except:
                        try:
                            self.driver.execute_script("arguments[0].click();", option)
                            print("DEBUG: Option clicked successfully (JS click)")
                            return True
                        except:
                            try:
                                actions = ActionChains(self.driver)
                                actions.move_to_element(option).click().perform()
                                print("DEBUG: Option clicked successfully (ActionChains)")
                                return True
                            except Exception as e:
                                print(f"DEBUG: Failed to click option: {e}")
                                continue
            
            print(f"WARNING: Tidak ditemukan option yang cocok untuk '{gender_text}'")
            return False
            
        except TimeoutException:
            print("ERROR: Timeout waiting for dropdown elements")
            return False
        except Exception as e:
            print(f"ERROR: Error handling custom dropdown: {e}")
            return False

    def _close_calendar_popup(self):
        """Close calendar popup if it appears"""
        try:
            # Try clicking outside the calendar
            body = self.driver.find_element(By.TAG_NAME, "body")
            actions = ActionChains(self.driver)
            actions.move_to_element(body).click().perform()
            time.sleep(1)
            print("DEBUG: Calendar popup closed")
        except:
            pass

    def form_addData(self, nama_depan, ttl, kelamin, expected_message, noTLP, nama_belakang, status, email, note):
        try:
            print("DEBUG: ===== MULAI MENGISI FORM =====")
        
            # 1. Input Nama Depan
            if not self._safe_input_text(self.name_field, nama_depan, "Nama Depan"):
                raise Exception("Gagal input nama depan")
        
            #nama belakang
            if not self._safe_input_text(self.lastName_field, nama_belakang, "Nama Belakang"):
                raise Exception("Gagal input nama belakang")

            # 2. Input Tanggal Lahir
            if not self._safe_input_text(self.date_field, ttl, "Tanggal Lahir"):
                raise Exception("Gagal input tanggal lahir")
        
            # ✅ Trigger semua event agar usia tahun & bulan dihitung
            try:
                date_element = self.driver.find_element(*self.date_field)
                self.driver.execute_script("""
                    const el = arguments[0];
                    el.dispatchEvent(new Event('input', { bubbles: true }));
                    el.dispatchEvent(new Event('change', { bubbles: true }));
                    el.dispatchEvent(new Event('blur', { bubbles: true }));
                """, date_element)
                print("DEBUG: Event input, change & blur untuk TTL berhasil dipicu")
                time.sleep(1)  # beri waktu kalkulasi
            except Exception as e:
                print(f"WARNING: Gagal trigger event TTL: {e}")
        
            self._close_calendar_popup()
        
            # 3. Pilih Jenis Kelamin
            if not self._handle_custom_dropdown(kelamin):
                raise Exception("Gagal memilih jenis kelamin")
            
            # input no telephone
            if not self._safe_input_text(self.no_hp, noTLP, "Nomor Telephone"):
                raise Exception("gagal input no hp")

            # select status
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.status_dropdown_trigger)
            ).click()

            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, f"//li[text()='{status}']"))
            )
            print("opsi status located")

            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, f"//li[text()='{status}']"))
            ).click()
            print("opsi status berhasil dipilih")

            #input email
            if not self._safe_input_text(self.email_field, email, "Alamat Email"):
                raise Exception("gagal input email")
            
            #input note
            if not self._safe_input_text(self.note_field, note, "Note"):
                raise Exception("gagal input note")

            # 4. Klik tombol simpan
            print("DEBUG: Mencari tombol simpan...")
            simpan_element = self.wait.until(EC.element_to_be_clickable(self.simpan_button))
            self._scroll_to_element(simpan_element)
            time.sleep(1)
            simpan_element.click()
            print("DEBUG: Tombol simpan berhasil diklik")
        
            # 5. Assert pesan sukses
            print("DEBUG: Menunggu pesan sukses...")
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Data Calon Pemegang Polis Berhasil Disimpan')]"))
                )
                actual_message = "Data Calon Pemegang Polis Berhasil Disimpan"
            except:
                actual_message = "tidak tersimpan"

            assert actual_message == expected_message, f"Expected: '{expected_message}', Actual: '{actual_message}'"
            
            print("DEBUG: Pesan sesuai, assert PASS ✅")
        
            print("DEBUG: ===== FORM BERHASIL DISUBMIT =====")
    
        except Exception as e:
            print(f"ERROR in form_addData: {str(e)}")
            self.driver.save_screenshot("error_form_addData.png")
            raise e

    def ilustrasi_page(self, cara_bayar, masa_bayar, premi_dasar,): 

        # 1. Klik tombol Buat Ilustrasi dengan timeout lebih panjang
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.buat_ilustrasi)
        ).click()
        print("Tombol Buat Ilustrasi berhasil diklik")

            # 2. Verifikasi halaman dengan timeout lebih panjang
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//h5[contains(text(), 'Buat Ilustrasi')]"))
        )
        print("Berhasil masuk ke halaman Buat Ilustrasi Baru")

            # Alternatif jika radio button tidak bisa diklik langsung
            # Tunggu modal muncul
        label_yes = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='large-6 columns']/input[@id='yes']"))
        )
        label_yes.click()

            # 4. Pilih produk dari dropdown dengan beberapa strategi
        product_dropdown = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "productName"))
        )
        
            # Scroll ke element jika perlu
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", product_dropdown)
        time.sleep(1)  # Beri waktu untuk render
        
            # Coba beberapa metode seleksi
  # Metode 1: Select by visible text
        Select(product_dropdown).select_by_visible_text("BNI LIFE STEADY PROTECTION+")
        print("Produk dipilih menggunakan teks visible")
        
        #submit ilustrasi
        submit_ilustrasi = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.ilustrasi_submit)
        )
        submit_ilustrasi.click()
        time.sleep(3)

        #form data Produk
        #scroll ke form data produk
        submit_form = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.formDataProduk_submit)
        )

        self.driver.execute_script("arguments[0].scrollIntoView();", submit_form)
        time.sleep(2)
        print("berhasil scroll")

        #isi form data produk
        #radio premi
        radioPremi = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.radio_premi)
        )
        radioPremi.click()
        print("berhasil click premi radio")

        #select cara bayar
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.bayar_select)
        ).click()

        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, f"//ul/li[@class='' and text()='{cara_bayar}']"))
        )
        print("opsi tahunan located")

        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, f"//ul/li[@class='' and text()='{cara_bayar}']"))
        ).click()
        print("opsi tahunan ter pilih")

        #select masa bayar
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.masa_select)
        ).click()

        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.masa_option(masa_bayar))
        ).click()
        print("masa bayar sudah dipilih")

        #input premi dasar
        premiDasar_input = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.premiDasar_field)
        )
        premiDasar_input.clear()
        premiDasar_input.send_keys(premi_dasar)

        #save premi
        save = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.simpan_premi)
        )
        save.click()    

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(By.XPATH, "//div[@class='large-12 columns']/h4[text()='Pilihan Ilustrasi']")
            )
            print("berhasil simpan")
        except:
            print("gagal simpan")

        download_pdf = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.save_pdf)
        )
        download_pdf.click()
        time.sleep(5)

    def search(self, namaPolis):
        searchBox = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='Name' and @type='text']"))
        )
        searchBox.clear()
        searchBox.send_keys(namaPolis)

        searchButton = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='postfix small-2 columns end' and @type='submit']"))
        )
        searchButton.click()
 