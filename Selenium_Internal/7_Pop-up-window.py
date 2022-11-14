""""
This script show how to handle pop-up windows & multi-tab windows
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
driver.implicitly_wait(5)

# Find element by text and click
time.sleep(3)
timerObj = driver.find_element(by=By.LINK_TEXT, value="Open a popup window")
if timerObj.is_enabled() and timerObj.is_displayed():
    timerObj.click()

time.sleep(3)
# switch to pop-up window
popup_window = driver.window_handles[1]
driver.switch_to.window(popup_window)
time.sleep(5)

print(driver.find_element(by=By.ID, value="para1").text)
print(driver.find_element(by=By.ID, value="para2").text)

driver.maximize_window()
# driver.fullscreen_window()
time.sleep(2)
driver.close()
time.sleep(2)

# Switch back to main window
main_window = driver.window_handles[0]
driver.switch_to.window(main_window)
time.sleep(2)

driver.find_element(by=By.LINK_TEXT, value="SeleniumTutorial").click()
new_tab = driver.window_handles[1]
driver.switch_to.window(new_tab)
time.sleep(3)

driver.find_element(by=By.LINK_TEXT, value="What is Selenium?").click()
time.sleep(3)
# Close the driver
driver.close()
