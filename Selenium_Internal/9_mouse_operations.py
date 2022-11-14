""""
This script show how to perform mouse operations like drag & drop, cursor movements and double click etc.
"""

from selenium import webdriver
import time
# To use chromeDriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Open the browser
driver.get("https://jqueryui.com/")

# Maximize browser window
driver.maximize_window()

# Synchronize time of 5 sec for each web operation
driver.implicitly_wait(3)

# Find element by text and click
driver.find_element(by=By.LINK_TEXT, value="Droppable").click()

# Adding sleep for demo purpose only, do not use once ready for deployment
time.sleep(3)

# Switch to iframe
driver.switch_to.frame(driver.find_element(by=By.CLASS_NAME, value="demo-frame"))

draggable = driver.find_element(by=By.ID, value="draggable")
droppable = driver.find_element(by=By.ID, value="droppable")

ActionChains(driver).drag_and_drop(draggable, droppable).perform()

driver.switch_to.default_content()
driver.find_element(by=By.LINK_TEXT, value='Checkboxradio').click()
driver.switch_to.frame(driver.find_element(by=By.CLASS_NAME, value="demo-frame"))

# clickable = driver.find_element(by=By.XPATH, value="//*[@for='checkbox-2']")

#   ActionChains(driver).click(clickable).perform()

# Note that the first argument X specifies to move right when positive,\
# while the second argument Y specifies to move down when positive.
ActionChains(driver).move_by_offset(13, 15).perform()
time.sleep(3)
ActionChains(driver).move_by_offset(40, -40).perform()

time.sleep(3)
#driver.close()

# Open the browser
driver.get("https://omayo.blogspot.com/")

# Maximize browser window
driver.maximize_window()

# Synchronize time of 5 sec for each web operation
driver.implicitly_wait(3)

double_click = driver.find_element(by=By.XPATH, value="//*[@id='HTML46']/div[1]/button")
ActionChains(driver).double_click(double_click).perform()

time.sleep(2)
alert = Alert(driver)
print(alert.text)
alert.accept()

time.sleep(2)
#right_click = driver.find_element(by=By.XPATH, value="//*[@for='checkbox-2']")

# Right click
#ActionChains(driver).context_click(right_click).perform()

driver.close()