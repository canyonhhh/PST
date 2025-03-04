import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from utils.user_creator import create_user

class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.email, cls.password = create_user()

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://demowebshop.tricentis.com/")
        self.wait = WebDriverWait(self.driver, 5)

    def tearDown(self):
        self.driver.quit()
