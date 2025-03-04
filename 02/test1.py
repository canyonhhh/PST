import unittest
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

        # Step 1: Click on the "Widgets" tab
        wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Widgets']/ancestor::div[contains(@class, 'top-card')]"))).click()

        # Step 2: Click on the "Progress bar" menu item
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Progress Bar']/ancestor::li"))).click()

        # Step 3: Click on the "Start" button
        wait.until(EC.element_to_be_clickable((By.ID, 'startStopButton'))).click()

        # Step 4: Wait for the progress bar to reach 100%
        wait.until(EC.text_to_be_present_in_element((By.ID, 'progressBar'), '100%'))

        # Step 5: Verify that the progress bar has reached 100%
        progress_bar = driver.find_element(By.ID, 'progressBar')
        self.assertEqual(progress_bar.text, '100%')

        # Step 6: Click on the "Reset" button
        wait.until(EC.element_to_be_clickable((By.ID, 'resetButton'))).click()

        # Step 7: Verify that the progress bar has been reset
        self.assertEqual(progress_bar.text, '0%')


if __name__ == "__main__":
    test_suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    BetterPyUnitTestRunner().run(test_suite)
