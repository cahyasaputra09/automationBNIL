from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.XPATH, "//input[@id='UserName']")
        self.password_input = (By.XPATH, "//input[@id='Password']")
        self.login_button = (By.XPATH, "//button[@id='signIn']")

    def login(self, username, password):
        try:

            
            
            close_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@class='close-reveal-modal']"))
            )
            close_button.click()
        except:
            pass  

        username_field = self.driver.find_element(*self.username_input)
        username_field.clear()
        username_field.send_keys(username)

        password_field = self.driver.find_element(*self.password_input) 
        password_field.clear()
        password_field.send_keys(password) 
        
        time.sleep(2)

        signin = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((self.login_button))
        )

        self.driver.execute_script("arguments[0].click();", signin)
        

        print("username:", username_field.get_attribute("value"))
        print("Password:", password_field.get_attribute("value"))
        print("Clickable:", signin.is_enabled(), signin.is_displayed())
        print("Location:", signin.location)
        print("URL setelah login:", driver.current_url)
        print("Title setelah login:", driver.title)
        driver.save_screenshot("after_login.png")
        self.driver.execute_script("""arguments[0].addEventListener('click', () => console.log('Button clicked!'));""", signin)