import json

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

login_url = "https://signinssl.gmarket.co.kr/LogIn/LogIn?URL=http://myg.gmarket.co.kr/ContractList/ContractList"


def handler(event, context):
    driver = init_driver()
    driver.get(login_url)

    driver.close()
    driver.quit()

    body = {
        "message": "Headless Chrome Initialized, Page title: {driver.title}",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


def init_driver():
    options = webdriver.ChromeOptions()
    options.binary_location = '/opt/headless-chromium'
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome('/opt/chromedriver', chrome_options=options)
    return driver
