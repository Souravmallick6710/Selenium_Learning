""""
This script is used to show how different web objects are identified using X-path as a locator.
Also, it will cover some basic info fetching using get_attribute() method.
"""

from selenium import webdriver
import time
# To use chromeDriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


# Open the browser
driver.get("https://omayo.blogspot.com/")

# Maximize browser window
driver.maximize_window()

# Synchronize time of 5 sec for each web operation
driver.implicitly_wait(3)

# Find element by text and click
time.sleep(3)
tb1 = driver.find_element(by=By.XPATH, value="//*[@id='HTML11']/div[1]/textarea")

# using get_attribute method to fetch information about the object
if tb1.is_enabled():
    print("Text inside the box - %s " % tb1.get_attribute('value'))
    print("Name - %s " % tb1.get_attribute('name'))
    print("Text - %s " % tb1.get_attribute('text'))

driver.find_element(by=By.XPATH, value="//*[@id='HTML31']/div[1]/form/input[1]").send_keys("userName")
driver.find_element(by=By.XPATH, value="//*[@id='HTML31']/div[1]/form/input[2]").send_keys("Password")

time.sleep(2)
driver.find_element(by=By.XPATH, value="//*[@id='HTML31']/div[1]/form/button").click()



# Close the driver
driver.close()
