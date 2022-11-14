import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
driver = webdriver.Remote(
    command_executor='http://10.8.137.143:4444',
    options=chrome_options
)
# Open the browser
driver.get("https://jqueryui.com/")

# Maximize browser window
driver.maximize_window()
# Find element by text and click
driver.find_element(by=By.LINK_TEXT, value="Autocomplete").click()

# Switch to iframe
driver.switch_to.frame(driver.find_element(by=By.CLASS_NAME, value="demo-frame"))

# Find element and enter text
driver.find_element(by=By.CLASS_NAME, value="ui-autocomplete-input").send_keys('MitelCloud')

# Adding sleep for demo purpose only, do not use once ready for deployment
time.sleep(5)

driver.close()

