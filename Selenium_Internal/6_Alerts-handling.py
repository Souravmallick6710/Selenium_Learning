""""
This script will show how to handle alerts
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
time.sleep(5)
driver.find_element(by=By.XPATH, value='//*[@id="timerButton"]').click()
time.sleep(2)
alert_v1 = driver.switch_to.alert
print(alert_v1.text)
alert_v1.accept()

# Close the driver
driver.close()
