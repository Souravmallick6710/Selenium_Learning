""""
This script will show how to use explicitly waits to find obj and control them
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://omayo.blogspot.com/")
try:
    element = WebDriverWait(driver, 12).until(
        EC.presence_of_element_located((By.ID, "delayedText"))
    )
    print(type(element))

    obj_status = WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, "delayedText"), 'This text is displayed after 10 seconds of wait.')
    )

    print(obj_status)
finally:
    driver.close()