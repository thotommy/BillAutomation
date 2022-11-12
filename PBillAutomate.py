from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from datetime import date
import undetected_chromedriver.v2 as uc
from helper import *
from decouple import config


def check_accountExists_And_Requires_Payment(driver):
    acct = driver.find_element(By.XPATH,
                               "/html/body/div[2]/div[2]/div[3]/div/div[2]/div/div/table/tbody/tr/td[1]").text
    price = driver.find_element(By.XPATH,
                                "/html/body/div[2]/div[2]/div[3]/div/div[2]/div/div/table/tbody/tr/td[4]").text
    if (acct == config('SHORT_VERS_ADDR') and price != "0.00"):
        today = date.today()
        print(
            f'Water Bill has came on {today} The price of the water bill is ${price}')
        return True
    else:
        print(f'Account {acct} does not require payment price is ${price}')
        return False


if __name__ == '__main__':

    print("Starting Chrome up")
    options = webdriver.ChromeOptions()
    options.add_argument("--auto-open-devtools-for-tabs")
    driver = uc.Chrome(options=options)
    driver.maximize_window()

    # Water Bill Automation ======================================================
    print("Starting the Water Bill Payment")
    driver.get(config('WATER_BILL_SITE'))

    exists_by_id(driver, "inputAddress", 2.4)

    driver.find_element(By.ID, "inputAddress").send_keys(
        config('SHORT_VERS_ADDR'))
    driver.find_element(By.ID, "inputAccountNumber").send_keys(
        config('WATER_BILL_ACCT_NUM') + Keys.ENTER)

    exists_by_id(driver, "tblQuickPay", 2.4)

    # if (check_accountExists_And_Requires_Payment(driver) == False):  # Need to change this to false
    #     driver.quit()
    #     quit()

    # driver.find_element(
    #     By.XPATH, "/html/body/div[2]/div[2]/div[3]/div/div[2]/div/div/table/tbody/tr/td[5]/a").click()

    # exists_by_id(driver, "txtCardNumber", 2.4)

    # driver.find_element(By.ID, "txtCardNumber").send_keys(config('CARD_NUMBER'))
    # driver.find_element(By.ID, "txtNameOnCard").send_keys(config('PERSON_NAME'))
    # driver.find_element(By.ID, "txtCvvCid").send_keys(config('CARD_CID'))
    # driver.find_element(By.ID, "txtExpires").send_keys(config('CARD_EXP_DATE'))
    # driver.find_element(By.ID, "txtAddress").send_keys(config('SHORT_VERS_ADDR'))
    # driver.find_element(By.ID, "txtCity").send_keys(config('ADDR_CITY'))
    # driver.find_element(By.ID, "txtStateProvince").send_keys(config('ADDR_STATE'))
    # driver.find_element(By.ID, "txtZipPostal").send_keys(config('ADDR_ZIP'))
    # driver.find_element(By.ID, "emlEmail").send_keys(config('USER_NAME'))
    # Water Bill Automation ======================================================

    # Electric Bill Automation ===================================================
    print('Starting Power Bill payment')
    driver.get(config('POWER_BILL_SITE'))
    exists_by_id(driver, "username", 2.4)

    driver.find_element(By.ID, "username").send_keys(config('POWER_USER_NAME'))
    driver.find_element(By.ID, "password").send_keys(config('POWER_PWD'))
    driver.find_element(
        By.XPATH, "/html/body/main/div[2]/section[1]/div/div[2]/div[2]/div/div/form/div[4]/button").click()

    exists_by_xpath(
        driver, "/html/body/div[3]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[2]/p[1]", 2.4)

    billPrice = driver.find_element(
        By.XPATH, "/html/body/div[3]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[2]/p[1]").text

    if (billPrice == "$0.00"):
        print('No Power Bill to pay')
    else:
        print('Eletric bill is ' + billPrice)

    # Electric Bill Automation ===================================================

    # Internet Bill Automation ===================================================
    print('Starting Internet Bill payment')

    driver.get(config('INTERNET_BILL_SITE'))
    exists_by_xpath(
        driver, "/html/body/div[1]/div/attwc-globalnav-header/att-wcgn-header-bootstrap/div/att-wcgn-header-core/div/header/div/nav/div[1]/div[3]/attwc-globalnav-profile/div/a/span", 2.4)

    time.sleep(5.4)
    driver.find_element(
        By.XPATH, "/html/body/div[1]/div/attwc-globalnav-header/att-wcgn-header-bootstrap/div/att-wcgn-header-core/div/header/div/nav/div[1]/div[3]/attwc-globalnav-profile/div/a/span").click()
    time.sleep(2.4)
    driver.find_element(
        By.XPATH, "/html/body/div[1]/div/attwc-globalnav-header/att-wcgn-header-bootstrap/div/att-wcgn-header-core/div/header/div/nav/div[1]/div[3]/attwc-globalnav-profile/div/div/div/div/div[2]/ul/li[8]/a").click()

    # https://www.blog.datahut.co/post/web-scraping-how-to-bypass-anti-scraping-tools-on-websites

    exists_by_id(driver, "userID", 2.4)

    driver.find_element(By.ID, "userID").send_keys(config('INT_USER_NAME'))
    driver.find_element(By.ID, "password").send_keys(config('INT_PWD'))
    time.sleep(4.0)
    driver.find_element(
        By.XPATH, "/html/body/div[1]/div/div/div/app-manual-login/form/div[6]/div/button[1]").click()

    driver.get(config('INTERNET_BILL_OVERVIEW'))
    print('checking for internet price')
    exists_by_xpath(
        driver, "/html/body/div[1]/div/div[2]/div[2]/div/div[7]/div/div[1]/p[1]/span[2]", 2.4)
    print('Found price for internet')
    internetPrice = driver.find_element(
        By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[7]/div/div[1]/p[1]/span[2]").text
    print('Internet price: ' + internetPrice)
    time.sleep(10.0)
    if (internetPrice == "0.00"):
        print('No Internet Bill to pay')
        driver.close()
        driver.quit()
        quit()
    # Internet Bill Automation ===================================================
    driver.close()
    driver.quit()
