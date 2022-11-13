# Helper Methods in python to use for PBillAutomate.py
# Credit to # https://www.blog.datahut.co/post/web-scraping-how-to-bypass-anti-scraping-tools-on-websites
# twilio imports
import os
import time
from datetime import date

from decouple import config
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from twilio.rest import Client

__water_bill = ''
__electric_bill = ''
__internet_bill = ''

# Water Bill Helpers


def check_accountExists_And_Requires_Payment(driver):
    acct = driver.find_element(By.XPATH,
                               "/html/body/div[2]/div[2]/div[3]/div/div[2]/div/div/table/tbody/tr/td[1]").text
    __water_bill = driver.find_element(By.XPATH,
                                       "/html/body/div[2]/div[2]/div[3]/div/div[2]/div/div/table/tbody/tr/td[4]").text
    if (acct == config('SHORT_VERS_ADDR') and __water_bill != "0.00"):
        today = date.today()
        print(
            f'On {today}, water bill price is ${__water_bill}')
        return True
    else:
        print(f'No water bill. Price is ${__water_bill}')
        return False
    # if (check_accountExists_And_Requires_Payment(driver) == False):  # Need to change this to false
    #     driver.quit()
    #     quit()


def check_water_bill_prices(driver):
    print("Checking the water bill...")
    driver.get(config('WATER_BILL_SITE'))

    exists_by_id(driver, "inputAddress", 2.4)

    driver.find_element(By.ID, "inputAddress").send_keys(
        config('SHORT_VERS_ADDR'))
    driver.find_element(By.ID, "inputAccountNumber").send_keys(
        config('WATER_BILL_ACCT_NUM') + Keys.ENTER)

    exists_by_id(driver, "tblQuickPay", 2.4)

    check_accountExists_And_Requires_Payment(driver)


def pay_water_bill(driver):
    print("Paying the Water Bill...")
    driver.find_element(
        By.XPATH, "/html/body/div[2]/div[2]/div[3]/div/div[2]/div/div/table/tbody/tr/td[5]/a").click()

    exists_by_id(driver, "txtCardNumber", 2.4)

    driver.find_element(By.ID, "txtCardNumber").send_keys(
        config('CARD_NUMBER'))
    driver.find_element(By.ID, "txtNameOnCard").send_keys(
        config('PERSON_NAME'))
    driver.find_element(By.ID, "txtCvvCid").send_keys(config('CARD_CID'))
    driver.find_element(By.ID, "txtExpires").send_keys(
        config('CARD_EXP_DATE'))
    driver.find_element(By.ID, "txtAddress").send_keys(
        config('SHORT_VERS_ADDR'))
    driver.find_element(By.ID, "txtCity").send_keys(config('ADDR_CITY'))
    driver.find_element(By.ID, "txtStateProvince").send_keys(
        config('ADDR_STATE'))
    driver.find_element(By.ID, "txtZipPostal").send_keys(
        config('ADDR_ZIP'))
    driver.find_element(By.ID, "emlEmail").send_keys(config('USER_NAME'))

# Eletric Bill Helpers


def check_electric_bill_prices(driver):
    print('Checking the electric bill...')
    driver.get(config('POWER_BILL_SITE'))
    exists_by_id(driver, "username", 2.4)

    driver.find_element(By.ID, "username").send_keys(
        config('POWER_USER_NAME'))
    driver.find_element(By.ID, "password").send_keys(config('POWER_PWD'))
    driver.find_element(
        By.XPATH, "/html/body/main/div[2]/section[1]/div/div[2]/div[2]/div/div/form/div[4]/button").click()

    exists_by_xpath(
        driver, "/html/body/div[3]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[2]/p[1]", 2.4)

    __electric_bill = driver.find_element(
        By.XPATH, "/html/body/div[3]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[2]/p[1]").text

    if (__electric_bill != "$0.00"):
        today = date.today()
        print(f'On {today}, electric bill price is {__electric_bill}')
    else:
        print(f'No power bill. Price is {__electric_bill}')

# Internet Bill Helpers


def check_internet_bill_prices(driver):
    print('Checking the internet bill...')
    driver.get(config('INTERNET_BILL_SITE'))
    exists_by_xpath(
        driver, "/html/body/div[1]/div/attwc-globalnav-header/att-wcgn-header-bootstrap/div/att-wcgn-header-core/div/header/div/nav/div[1]/div[3]/attwc-globalnav-profile/div/a/span", 2.4)

    time.sleep(5.4)
    driver.find_element(
        By.XPATH, "/html/body/div[1]/div/attwc-globalnav-header/att-wcgn-header-bootstrap/div/att-wcgn-header-core/div/header/div/nav/div[1]/div[3]/attwc-globalnav-profile/div/a/span").click()
    time.sleep(2.4)
    driver.find_element(
        By.XPATH, "/html/body/div[1]/div/attwc-globalnav-header/att-wcgn-header-bootstrap/div/att-wcgn-header-core/div/header/div/nav/div[1]/div[3]/attwc-globalnav-profile/div/div/div/div/div[2]/ul/li[8]/a").click()

    exists_by_id(driver, "userID", 2.4)

    driver.find_element(By.ID, "userID").send_keys(config('INT_USER_NAME'))
    driver.find_element(By.ID, "password").send_keys(config('INT_PWD'))
    time.sleep(4.0)
    driver.find_element(
        By.XPATH, "/html/body/div[1]/div/div/div/app-manual-login/form/div[6]/div/button[1]").click()

    driver.get(config('INTERNET_BILL_OVERVIEW'))
    exists_by_xpath(
        driver, "/html/body/div[1]/div/div[2]/div[2]/div/div[7]/div/div[1]/p[1]/span[2]", 2.4)
    __internet_bill = driver.find_element(
        By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[7]/div/div[1]/p[1]/span[2]").text

    time.sleep(10.0)
    if (__internet_bill != "0.00"):
        today = date.today()
        print(f'On {today}, internet bill price is ${__internet_bill}')
    else:
        print(f'No internet bill. Price is ${__internet_bill}')
        # driver.close()
        # driver.quit()
        # quit()

# Twilio calls


def send_message():
    msg = f"Water Bill: {__water_bill}, Electric Bill: {__electric_bill}, Internet Bill: {__internet_bill}"
    client = Client(config('TWILIO_ACCT_SID'), config('TWILIO_AUTH_TOKEN'))
    client.messages.create(
        to=config('USER_NUMBER'),
        from_=config('TWILIO_PHONE_NUMBER'),
        body=msg)
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
