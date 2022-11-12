# Helper Methods in python to use for PBillAutomate.py
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from decouple import config

# Water Bill Helpers

# Eletric Bill Helpers

# Internet Bill Helpers

# Common Helpers


def exists_by_id(driver, id, seconds):
    while (__check_exists_by_id(driver, id) == False):
        time.sleep(seconds)


def exists_by_xpath(driver, path, seconds):
    while (__check_exists_by_xpath(driver, path) == False):
        time.sleep(seconds)


# Private Methods
def __check_exists_by_id(driver, id):
    try:
        driver.find_element(By.ID, id)
    except NoSuchElementException:
        return False
    return True


def __check_exists_by_xpath(driver, xpath):
    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True
