from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Chrome Options
chrome_options = webdriver.ChromeOptions()
chrome_service = Service('C:/Users/ASUS/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe')

# Initialize WebDriver with Chrome Options and Service
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Test Case: Admin Login
def test_admin_login():
    driver.get("https://opensource-demo.orangehrmlive.com/")
    
    try:
        # Wait until the username field is present
        username = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "txtUsername"))
        )
        password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "txtPassword"))
        )
        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "btnLogin"))
        )
        
        username.send_keys("Admin")
        password.send_keys("admin123")
        login_button.click()
        
        time.sleep(2)  # Wait for page to load
        
        # Verification
        assert "Dashboard" in driver.title
        print("Admin login successful.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the browser
        driver.quit()

# Execute test case
test_admin_login()
