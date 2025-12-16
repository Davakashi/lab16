"""
Self-Healing Automation - Selenium тест жишээ

Энэ скрипт нь HTML file-г нээж, login button-г олох эртэй хэрэглэнэ.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

class SelfHealingLoginTest:
    """Self-healing locator strategy-ээр test нь хэрэглэх класс"""
    
    def __init__(self, html_file_path):
        self.driver = webdriver.Chrome()
        self.file_path = html_file_path
        self.wait = WebDriverWait(self.driver, 10)
    
    def open_page(self):
        """HTML page нээх"""
        # Windows: file:/// + path
        file_url = f"file:///{self.file_path.replace(os.sep, '/')}"
        print(f"Opening: {file_url}")
        self.driver.get(file_url)
        time.sleep(1)
    
    def find_login_button_basic(self):
        """Үндсэн ID selector"""
        try:
            button = self.driver.find_element(By.ID, "loginBtn")
            print("✓ Found button using ID: loginBtn")
            return button
        except Exception as e:
            print(f"✗ Error with basic ID selector: {e}")
            return None
    
    def find_login_button_robust(self):
        """Self-healing strategy: олон locators туршилдаж сонгох"""
        locators = [
            (By.ID, "loginBtn"),
            (By.ID, "signinButton"),
            (By.CSS_SELECTOR, "button[type='submit']"),
            (By.XPATH, "//button[contains(text(), 'Нэвтрэх')]"),
            (By.XPATH, "//button"),
            (By.CLASS_NAME, "submit-button")
        ]
        
        print("\nTrying multiple locators (Self-Healing)...")
        for strategy, selector in locators:
            try:
                element = self.driver.find_element(strategy, selector)
                print(f"✓ Found using: {strategy.name} = '{selector}'")
                return element, strategy, selector
            except Exception as e:
                print(f"  - {strategy.name} '{selector}' - not found")
        
        print("✗ No button found with any locator strategy")
        return None, None, None
    
    def test_basic_selector(self):
        """Үндсэн selector туршилдах"""
        print("\n" + "="*50)
        print("TEST 1: Basic ID Selector")
        print("="*50)
        
        self.open_page()
        button = self.find_login_button_basic()
        
        if button:
            print("✓ TEST PASSED - Button found and can click")
            time.sleep(1)
        else:
            print("✗ TEST FAILED - Button not found")
    
    def test_robust_selector(self):
        """Self-healing robust selector туршилдах"""
        print("\n" + "="*50)
        print("TEST 2: Self-Healing Robust Selector")
        print("="*50)
        
        self.open_page()
        button, strategy, selector = self.find_login_button_robust()
        
        if button:
            print(f"✓ TEST PASSED - Button found with fallback locator")
            print(f"  Strategy: {strategy.name}")
            print(f"  Selector: {selector}")
            time.sleep(1)
        else:
            print("✗ TEST FAILED - Button not found with any locator")
    
    def test_fill_form(self):
        """Form бөглөж login туршилдах"""
        print("\n" + "="*50)
        print("TEST 3: Form Filling Test")
        print("="*50)
        
        self.open_page()
        
        try:
            # Email оруулах
            email_field = self.driver.find_element(By.ID, "emailField")
            email_field.send_keys("test@example.com")
            print("✓ Email entered")
            
            # Password оруулах
            password_field = self.driver.find_element(By.ID, "passwordField")
            password_field.send_keys("password123")
            print("✓ Password entered")
            
            # Login button дарах (robust)
            button, _, _ = self.find_login_button_robust()
            if button:
                button.click()
                print("✓ Login button clicked")
                time.sleep(1)
                
                # Success message байгаа эсэхийг шалгах
                message = self.driver.find_element(By.ID, "message")
                if "Амжилттай" in message.text:
                    print(f"✓ TEST PASSED - {message.text}")
                else:
                    print(f"✗ TEST FAILED - {message.text}")
            else:
                print("✗ Could not find login button")
        
        except Exception as e:
            print(f"✗ TEST FAILED - {e}")
    
    def close(self):
        """Browser хаах"""
        self.driver.quit()

def main():
    """Main test runner"""
    # HTML file path-г дүүргэнэ
    html_path = r"C:\Users\Admin\Desktop\school\F.CSA313\15\Work3_SelfHealingAutomation\login_demo.html"
    
    # HTML file байгаа эсэхийг шалгах
    if not os.path.exists(html_path):
        print(f"ERROR: HTML file not found at {html_path}")
        return
    
    # Test хэрэглэх
    test = SelfHealingLoginTest(html_path)
    
    try:
        # Test 1: Үндсэн selector
        test.test_basic_selector()
        test.close()
        time.sleep(1)
        
        # Test 2: Robust selector
        test = SelfHealingLoginTest(html_path)
        test.test_robust_selector()
        test.close()
        time.sleep(1)
        
        # Test 3: Form filling
        test = SelfHealingLoginTest(html_path)
        test.test_fill_form()
        test.close()
        
    finally:
        test.close()

if __name__ == "__main__":
    main()
