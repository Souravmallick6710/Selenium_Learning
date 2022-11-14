""""
This script is used to show select menu options like select by index, value and text.
"""
from selenium import webdriver
import time
# To use chromeDriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


# Open the browser
driver.get("https://omayo.blogspot.com/")

# Maximize browser window
driver.maximize_window()

# Synchronize time of 5 sec for each web operation
driver.implicitly_wait(3)


speedMenu = Select(driver.find_element(by=By.ID, value="drop1"))

time.sleep(2)
speedMenu.select_by_index(1)
time.sleep(2)
speedMenu.select_by_visible_text("doc 3")
time.sleep(2)
speedMenu.select_by_value("mno")
time.sleep(2)
# speedMenu.deselect_all()

time.sleep(3)

driver.close()



