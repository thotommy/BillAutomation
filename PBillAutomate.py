from selenium import webdriver
import undetected_chromedriver.v2 as uc
from helper import *

if __name__ == '__main__':

    print("Starting Chrome up")
    options = webdriver.ChromeOptions()
    options.add_argument("--auto-open-devtools-for-tabs")
    driver = uc.Chrome(options=options)
    driver.maximize_window()

    h = Helper()

    # Water Bill Automation ======================================================
    h.check_water_bill_prices(driver)
    h.pay_water_bill(driver)

    # Electric Bill Automation ===================================================
    # h.check_electric_bill_prices(driver)

    # Internet Bill Automation ===================================================
    # h.check_internet_bill_prices(driver)

    # h.send_message()

    # Exit program
    driver.close()
    driver.quit()
    quit()
