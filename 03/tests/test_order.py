from .base_test import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest

class OrderTest(BaseTest):

    def login(self):
        email, password = self.email, self.password

        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "ico-login"))).click()
        self.wait.until(EC.presence_of_element_located((By.ID, "Email"))).send_keys(email)
        self.wait.until(EC.presence_of_element_located((By.ID, "Password"))).send_keys(password)
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".login-button"))).click()

    def add_products_to_cart(self, file_path):
        """Reads product names from a file and adds them to the cart."""
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Digital downloads"))).click()

        with open(file_path, "r") as f:
            products = [line.strip() for line in f.readlines() if line.strip()]

        for product_name in products:
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-grid")))

            product_cards = self.driver.find_elements(By.CLASS_NAME, "item-box")

            for card in product_cards:
                title_element = card.find_element(By.CLASS_NAME, "product-title")
                title_text = title_element.text.strip()

                if title_text == product_name:
                    add_to_cart_button = card.find_element(By.CLASS_NAME, "product-box-add-to-cart-button")
                    self.wait.until(EC.element_to_be_clickable(add_to_cart_button)).click()

                    self.wait.until(EC.visibility_of_element_located((By.ID, "bar-notification")))

                    break

    def checkout(self):
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Shopping cart"))).click()
        self.wait.until(EC.element_to_be_clickable((By.ID, "termsofservice"))).click()
        self.wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

        try:
            self.wait.until(EC.presence_of_element_located((By.ID, "billing-address-select")))
        except:
            self.wait.until(EC.element_to_be_clickable((By.ID, "BillingNewAddress_CountryId"))).click()
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "option[value='156']"))).click()

            self.wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_City"))).send_keys("Vilnius")
            self.wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_Address1"))).send_keys("1234")
            self.wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_ZipPostalCode"))).send_keys("00100")
            self.wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_PhoneNumber"))).send_keys("+71212345678")

        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".new-address-next-step-button"))).click()

        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".payment-method-next-step-button"))).click()

        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".payment-info-next-step-button"))).click()

        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".confirm-order-next-step-button"))).click()

        # assert that the order was placed
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".details")))
        order_number_element = self.driver.find_element(By.XPATH, "//li[contains(text(), 'Order number:')]")
        order_number = order_number_element.text.split(":")[1].strip()
        self.assertTrue(order_number.isdigit())

    def test_order_placement_data1(self):
        """Test that executes login, adding products from 'data1.txt', and checkout."""
        self.login()
        self.add_products_to_cart("data/data1.txt")
        self.checkout()

    def test_order_placement_data2(self):
        """Test that executes login, adding products from 'data2.txt', and checkout."""
        self.login()
        self.add_products_to_cart("data/data2.txt")
        self.checkout()

if __name__ == "__main__":
    unittest.main()
