import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from BetterPyUnitFormat import BetterPyUnitTestRunner

BASE_URL='https://demowebshop.tricentis.com'
RECIPIENT_NAME='Vardas Vardas'
SENDER_NAME='Vardas Vardas'
GIFT_QTY=5000
JEWELRY_QTY=26

class TestWebShop(unittest.TestCase):
    def setUp(self):
        """Initialize the Selenium WebDriver before each test."""
        self.driver = webdriver.Chrome()
        self.driver.get(BASE_URL)
        self.driver.execute_script("document.body.style.zoom='90%'")

    def tearDown(self):
        """Close the browser after each test."""
        self.driver.quit()

    def test_shop_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        # Step 2: Click on 'Gift Cards'
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Gift Cards"))).click()

        # Step 3: Select the first product with a price > 99
        products = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-item")))
        for product in products:
            price_element = product.find_element(By.CSS_SELECTOR, ".price")
            price = float(price_element.text.replace("$", ""))
            if price > 99:
                product.find_element(By.CSS_SELECTOR, ".product-title a").click()
                break

        # Step 4: Fill in recipient and sender names
        wait.until(EC.visibility_of_element_located((By.ID, "giftcard_4_RecipientName"))).send_keys(RECIPIENT_NAME)
        wait.until(EC.visibility_of_element_located((By.ID, "giftcard_4_SenderName"))).send_keys(SENDER_NAME)

        # Step 5: Enter '5000' in 'Qty'
        qty_field = wait.until(EC.element_to_be_clickable((By.ID, "addtocart_4_EnteredQuantity")))
        qty_field.clear()
        qty_field.send_keys(str(GIFT_QTY))

        # Step 6 & 7: Add to cart and wish list
        wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-button-4"))).click()
        wait.until(EC.visibility_of_element_located((By.ID, "bar-notification")))
        wait.until(EC.element_to_be_clickable((By.ID, "add-to-wishlist-button-4"))).click()
        wait.until(EC.visibility_of_element_located((By.ID, "bar-notification")))

        # Step 8 & 9: Navigate to Jewelry > Create Your Own Jewelry
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Jewelry"))).click()
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Create Your Own Jewelry"))).click()

        # Step 10: Select options
        wait.until(EC.element_to_be_clickable((By.ID, "product_attribute_71_9_15"))).send_keys("Silver (1 mm)")
        wait.until(EC.element_to_be_clickable((By.ID, "product_attribute_71_10_16"))).send_keys("80")
        wait.until(EC.element_to_be_clickable((By.ID, "product_attribute_71_11_17_50"))).click()

        # Step 11: Enter '26' in 'Qty'
        qty_field = wait.until(EC.element_to_be_clickable((By.ID, "addtocart_71_EnteredQuantity")))
        qty_field.clear()
        qty_field.send_keys(str(JEWELRY_QTY))

        # Step 12 & 13: Add to cart and wish list
        wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-button-71"))).click()
        wait.until(EC.visibility_of_element_located((By.ID, "bar-notification")))
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".add-to-wishlist-button"))).click()
        wait.until(EC.visibility_of_element_located((By.ID, "bar-notification")))

        # Step 14: Go to wishlist
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Wishlist"))).click()

        # Step 15: Check 'Add to cart' for both items
        checkboxes = wait.until(EC.presence_of_all_elements_located((By.NAME, "addtocart")))
        for checkbox in checkboxes:
            checkbox.click()

        # Step 16: Click 'Add to cart'
        wait.until(EC.element_to_be_clickable((By.NAME, "addtocartbutton"))).click()

        # Step 17: Verify sub-total price
        sub_total_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart-total-right span")))
        self.assertEqual(sub_total_element.text, "1002600.00")

if __name__ == "__main__":
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestWebShop)
    BetterPyUnitTestRunner().run(test_suite)

