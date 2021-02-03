from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from behave.runner import Context
from pom.config import Config


class BasePage(object):
    def __init__(self):
        pass

    driver = webdriver.Chrome()
    config = Config()
    driver.maximize_window()
    driver.implicitly_wait(5)
    wait = WebDriverWait(driver, 40)
