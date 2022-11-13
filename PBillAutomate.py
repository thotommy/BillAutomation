from selenium import webdriver
import undetected_chromedriver.v2 as uc
from helper import *

if __name__ == '__main__':

    print("Starting Chrome up")
    options = webdriver.ChromeOptions()
    options.add_argument("--auto-open-devtools-for-tabs")
    driver = uc.Chrome(options=options)
    driver.maximize_window()

    # Water Bill Automation ======================================================
    check_water_bill_prices(driver)

    # Electric Bill Automation ===================================================
    check_electric_bill_prices(driver)

    # Internet Bill Automation ===================================================
    check_internet_bill_prices(driver)

    send_message()

    # Exit program
    driver.close()
    driver.quit()
