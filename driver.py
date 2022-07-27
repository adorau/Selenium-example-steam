from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from singleton import Singleton
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, JavascriptException
from selenium.common.exceptions import StaleElementReferenceException


class Driver(metaclass=Singleton):
    def __init__(self):
        self.driver = None

        self.init_driver()

    def init_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options,
                                       service=ChromeService(ChromeDriverManager().install()))

    def open_page(self, page):
        return self.driver.get(page)

    def quit(self):
        self.driver.quit()

    def find_element_by(self, path, by=By.XPATH):
        element = WebDriverWait(self.driver,
                                10,
                                ignored_exceptions=(StaleElementReferenceException,
                                                    NoSuchElementException,
                                                    JavascriptException)) \
            .until(EC.visibility_of_element_located((by, path)))

        return element
