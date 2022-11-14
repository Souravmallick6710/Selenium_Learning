""""
This script will cover about how different browser drivers like chrome, firefox and edge \
can be initiated and launched.
Also, this will cover how object inside the frame can be controlled.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# To use chromeDriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


# use FireFox browser
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager
# driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


# For edge browser
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))


# Open the browser
driver.get("https://jqueryui.com/")

# Maximize browser window
driver.maximize_window()

# Synchronize time of 5 sec for each web operation
driver.implicitly_wait(3)

# Find element by text and click
driver.find_element(by=By.LINK_TEXT, value="Autocomplete").click()

# Adding sleep for demo purpose only, do not use once ready for deployment
time.sleep(3)

# Switch to iframe
driver.switch_to.frame(driver.find_element(by=By.CLASS_NAME, value="demo-frame"))

# Find element and enter text
driver.find_element(by=By.CLASS_NAME, value="ui-autocomplete-input").send_keys('MitelCloud')

# Adding sleep for demo purpose only, do not use once ready for deployment
time.sleep(3)

# Close the driver
driver.close()
