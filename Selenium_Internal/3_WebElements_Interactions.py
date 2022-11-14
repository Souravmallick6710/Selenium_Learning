""""
This script is used to show operations on radio-button, check-box etc..
Also, it covers how to come out of frame using default_content() method.
"""

from selenium import webdriver
import time
# To use chromeDriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


# Open the browser
driver.get("https://jqueryui.com/")

# Maximize browser window
driver.maximize_window()

# Synchronize time of 5 sec for each web operation
driver.implicitly_wait(3)

# Find element by text and click
driver.find_element(by=By.LINK_TEXT, value='Checkboxradio').click()
# Adding sleep for demo purpose only, do not use once ready for deployment
time.sleep(2)

# # Switch to iframe
driver.switch_to.frame(driver.find_element(by=By.CLASS_NAME, value="demo-frame"))
driver.find_element(by=By.XPATH, value="//*[@for ='radio-3']").click()
time.sleep(2)
driver.find_element(by=By.XPATH, value="//*[@for='checkbox-2']").click()
time.sleep(2)
driver.find_element(by=By.XPATH, value="//*[@for='checkbox-3']").click()
time.sleep(2)
driver.find_element(by=By.XPATH, value="//*[@for='checkbox-4']").click()
time.sleep(2)
driver.find_element(by=By.XPATH, value="//*[@for ='radio-2']").click()
time.sleep(3)
driver.switch_to.default_content()

# Find element by text and click
driver.find_element(by=By.LINK_TEXT, value='Selectmenu').click()
# Adding sleep for demo purpose only, do not use once ready for deployment
time.sleep(5)

# Switch to iframe
driver.switch_to.frame(driver.find_element(by=By.CLASS_NAME, value="demo-frame"))
# Select Menu
driver.find_element(by=By.ID, value="speed-button").click()

time.sleep(3)

driver.close()



