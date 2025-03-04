import unittest
import tempfile
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from utils.user_creator import create_user
from selenium.webdriver.chrome.options import Options

class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.email, cls.password = create_user()

    def setUp(self):
        temp_user_data_dir = tempfile.mkdtemp()
        
        chrome_options = Options()
        chrome_options.add_argument(f"--user-data-dir={temp_user_data_dir}")
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://demowebshop.tricentis.com/")
        self.wait = WebDriverWait(self.driver, 5)

    def tearDown(self):
        self.driver.quit()
