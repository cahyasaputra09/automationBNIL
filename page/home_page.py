from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver
import time
from selenium.webdriver.common.action_chains import ActionChains

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.account_menu = (By.XPATH, "//li[@class='has-dropdown not-click']/a[text()='Logged as BAS-25377']")
        self.logout_button = (By.XPATH, "//a[@href='/Insubsyt/Account/LogOff']")
        self.ilustrasi_menu = (By.XPATH, "//li[@class='has-dropdown not-click']/a[text()='Ilustrasi']")
        self.dataIlustrasi_page = (By.XPATH, "//a[@href='/Insubsyt/Transactions/BancassuranceIllustration']")
        self.dataSPAJ_menu = (By.XPATH, "//li[@class='has-dropdown not-click']/a[text()='SPAJ']")
        self.dataSPAJ_page = (By.XPATH, "//a[@href='/Insubsyt/Transactions/SPAJ']")
        self.rencanaUang_page = (By.XPATH, "//a[@href='/Insubsyt/Transactions/FinancialCalculator']")
    def logout(self):       
        accountMenu = self.driver.find_element(*self.account_menu)
        actions = ActionChains(self.driver)
        actions.move_to_element(accountMenu).perform() 

        time.sleep(2)

        logoutAccount = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.logout_button) 
        ) 
        logoutAccount.click()
        
    def dataIlustrasi(self):
        time.sleep(2)
        ilustrasiMenu = self.driver.find_element(*self.ilustrasi_menu)
        actions = ActionChains(self.driver)
        actions.move_to_element(ilustrasiMenu).perform()

        time.sleep(2)

        ilustrasiPage = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.dataIlustrasi_page)
        )
        ilustrasiPage.click()
        
    def dataSPAJ(self):
        time.sleep(2)
        SPAJmenu = self.driver.find_element(*self.dataSPAJ_menu)
        actions = ActionChains(self.driver)
        actions.move_to_element(SPAJmenu).perform()

        time.sleep(2)

        SPAJPage = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.dataSPAJ_page)
        )
        SPAJPage.click()

    def rencanaUang(self):
        time.sleep(2)
        ilustrasiMenu = self.driver.find_element(*self.ilustrasi_menu)
        actions = ActionChains(self.driver)
        actions.move_to_element(ilustrasiMenu).perform()

        time.sleep(2)

        rencanaUangPage = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.rencanaUang_page)
        )
        rencanaUangPage.click()