# wifi login script for NTU
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Load environment variables from .env file
load_dotenv()


def get_login_url():
    USERNAME = os.getenv('NTU_USERNAME') # customize your username
    PASSWORD = os.getenv('NTU_PASSWORD') # customize your password

    """Get the actual login URL by attempting to access a website"""
    options = webdriver.ChromeOptions()
    options.add_argument('--headless') # run in headless mode to facilitate login
    driver = webdriver.Chrome(options=options)
    
    try:
        # Try to access Google, which should redirect to the wifi login page
        print("Getting login URL...")
        driver.get("http://www.google.com")
        connect = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "primary-button"))
        )
        connect.click()        
        time.sleep(3)
        # Get the URL we were redirected to
        login_tab = driver.window_handles[-1]
        driver.switch_to.window(login_tab)

        username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
        username_field.send_keys(USERNAME)
        
        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys(PASSWORD)
        
        login_button = driver.find_element(By.XPATH, "//input[@type='submit']")
        login_button.click()
        
    except Exception as e:
        print(f"Error getting login URL: {str(e)}")
        return None

    finally:
        driver.quit()

if __name__ == "__main__":  
    get_login_url()