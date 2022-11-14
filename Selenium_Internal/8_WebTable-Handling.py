""""
This script shows how to control web tables and fetch data from specific cell using row & col number
"""

import sys
import re
from cgitb import text
from selenium import webdriver
import time
# To use chromeDriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

sys.path.append("../log")
# from log import log


def get_table_cell_data(locator, row, col):
    """Returns cell data of a table using row & col number.
    your xpath for table should be something like : //form[2]/table/tbody

    """
    try:
        table = locator
        if table:
            row_list = table.find_elements(by=By.TAG_NAME, value='tr')
            # row_list = table.find_elements_by_tag_name('tr')
            # check row count
            if len(row_list) < row:
                raise AssertionError("Expected row no is not present in table")

            # get coloumn list
            expected_row = row_list[row]
            # col_list = expected_row.find_elements(by=By.TAG_NAME, value='th')
            col_list = expected_row.find_elements(by=By.TAG_NAME, value='td')

            # check col count
            if len(col_list) < col:
                raise AssertionError("Expected col no is not present in table")

            return col_list[col].text
    except:
        raise AssertionError("Error in get_table_cell_data - Check table xpath" \
                             "or row count or col count")


if __name__ == '__main__':
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # Open the browser
    driver.get("https://omayo.blogspot.com/")

    # Maximize browser window
    driver.maximize_window()

    # Synchronize time of 5 sec for each web operation
    driver.implicitly_wait(3)

    # Identify table using Xpath or ID
    # webTable = driver.find_element(by=By.XPATH, value='//*[@id="table1"]/thead')
    webTable = driver.find_element(by=By.XPATH, value='//*[@id="table1"]/tbody')

    # Get cell data from the table
    print("cell data - %s " % get_table_cell_data(webTable, 1, 0))

    driver.close()
