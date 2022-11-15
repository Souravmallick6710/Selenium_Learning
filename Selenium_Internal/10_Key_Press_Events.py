""""
This script is used to learn about keyboard operations
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


# use FireFox browser
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

try:
        browser.get("https://en.wikipedia.org")
        print(browser.title)
        data = browser.find_element(by=By.ID, value="searchInput")
        data.send_keys("Python3")

        # Using Keys module to control keyboard operations
        data.send_keys(Keys.ENTER)
        time.sleep(3)
        print(browser.title)
finally:
        browser.close()
