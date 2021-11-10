import unittest
from selenium import webdriver
import page


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("http://www.python.org")

    # run after test case is finished
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
