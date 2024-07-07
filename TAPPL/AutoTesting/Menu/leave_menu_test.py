import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def leave_menu_test():
    logging.info("Starting Leave Menu Test")

    try:
        # Initialize WebDriver with ChromeDriverManager
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        logging.info("Opening URL")
        driver.get("https://opensource-demo.orangehrmlive.com/")
        
        # Wait until the username field is present
        logging.info("Waiting for username field")
        username = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]'))
        )
        
        logging.info("Entering credentials and logging in")
        username.send_keys("Admin")
        password.send_keys("admin123")
        login_button.click()
        
        logging.info("Waiting for dashboard to load")
        time.sleep(2)  # Wait for page to load

        logging.info("Verifying dashboard load")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'span.oxd-topbar-header-breadcrumb'))
        )
        
        logging.info("Navigating to Leave menu")
        leave_menu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//a[@href="/web/index.php/leave/viewLeaveModule"]'))
        )
        leave_menu.click()
        
        logging.info("Waiting for Leave menu page to load")
        time.sleep(2)  # Wait for page to load
        
        # Verification
        logging.info("Verifying Leave menu")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//a[@href="/web/index.php/leave/assignLeave"]'))
        )
        logging.info("Leave menu test successful.")
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    
    finally:
        logging.info("Closing browser")
        driver.quit()

# Execute test case
leave_menu_test()
