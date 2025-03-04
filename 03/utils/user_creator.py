from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string

def generate_random_email():
    return ''.join(random.choices(string.ascii_lowercase, k=8)) + "@testmail.com"

def create_user():
    driver = webdriver.Chrome()
    try:
        driver.get("https://demowebshop.tricentis.com/")
        wait = WebDriverWait(driver, 10)

        register_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "ico-register")))
        register_button.click()

        email = generate_random_email()
        password = "Test@12345"

        wait.until(EC.element_to_be_clickable((By.ID, "gender-male"))).click()
        driver.find_element(By.ID, "FirstName").send_keys("Test")
        driver.find_element(By.ID, "LastName").send_keys("User")
        driver.find_element(By.ID, "Email").send_keys(email)
        driver.find_element(By.ID, "Password").send_keys(password)
        driver.find_element(By.ID, "ConfirmPassword").send_keys(password)
        driver.find_element(By.ID, "register-button").click()

        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "register-continue-button"))).click()
    finally:
        driver.quit()

    return email, password

if __name__ == "__main__":
    create_user()
