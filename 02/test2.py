import unittest
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from BetterPyUnitFormat import BetterPyUnitTestRunner

BASE_URL='https://web.archive.org/web/20240112153757/https://demoqa.com/'

class Test(unittest.TestCase):
    def setUp(self):
        """Initialize the Selenium WebDriver before each test."""
        self.driver = webdriver.Chrome()
        self.driver.get(BASE_URL)
        self.driver.execute_script("document.body.style.zoom='90%'")

    def tearDown(self):
        """Close the browser after each test."""
        self.driver.quit()
    
    def test(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        # Step 1: Click on the "Elements" tab
        wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Elements']/ancestor::div[contains(@class, 'top-card')]"))).click()

        # Step 2: Click on the "Web Tables" menu item
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Web Tables']/ancestor::li"))).click()

        while not EC.element_to_be_clickable((By.CSS_SELECTOR, ".-next .-btn"))(driver):
            # Step 3: Click on the "Add" button
            wait.until(EC.element_to_be_clickable((By.ID, "addNewRecordButton"))).click()

            # Step 4: Fill in the "First Name", "Last Name", "Email", "Age", "Salary" and "Department" fields
            wait.until(EC.element_to_be_clickable((By.ID, "firstName"))).send_keys("Name")
            wait.until(EC.element_to_be_clickable((By.ID, "lastName"))).send_keys("Name")
            wait.until(EC.element_to_be_clickable((By.ID, "userEmail"))).send_keys("email@email.email")
            wait.until(EC.element_to_be_clickable((By.ID, "age"))).send_keys("30")
            wait.until(EC.element_to_be_clickable((By.ID, "salary"))).send_keys("10000")
            wait.until(EC.element_to_be_clickable((By.ID, "department"))).send_keys("IT")

            # Step 5: Click on the "Submit" button
            wait.until(EC.element_to_be_clickable((By.ID, "submit"))).click()

        # Step 6: Click on the "Next" button
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".-next .-btn"))).click()

        # Step 7: Delete the record on the second page
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@id, 'delete-record-')]"))).click()

        # Step 8: Verify page total is 1
        total_pages_element = driver.find_element(By.CLASS_NAME, "-totalPages").text.strip()
        self.assertEqual(total_pages_element, "1")

        # Step 9: Verify page number is 1
        page_jump_element = driver.find_element(By.CSS_SELECTOR, ".-pageJump input").get_attribute("value")
        self.assertEqual(page_jump_element, "1", "Page number is not 1")

if __name__ == "__main__":
    test_suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    BetterPyUnitTestRunner().run(test_suite)
