from pages.base_page import BasePage
import requests


class LoginPage(BasePage):
    def __init__(self):
        BasePage.__init__(self)
        self.driver.get(self.config.base_url)

    def set_email(self):
        element = self.driver.find_element_by_xpath("//div[@class='line']//input[@placeholder='Email']")
        element.click()
        element.clear()
        element.send_keys(self.config.email)

    def set_password(self):
        element = self.driver.find_element_by_xpath("//div[@class='line']//input[@placeholder='Password']")
        element.click()
        element.clear()
        element.send_keys(self.config.password)

    def sign_in_button(self):
        element = self.driver.find_element_by_xpath("//div[@class='line']//button[text()='Log in']")
        element.click()

    def open_campaigns_page(self):
        element = self.driver.find_element_by_xpath("//div[@class='nav main']//a[contains(@href,'campaigns')]"
                                                    "//div[@class='content']")
        element.click()

    def verify_login(self):
        r = requests.get(self.config.base_url)
        assert r.status_code == 200, f'User login failed with: {r.status_code}'
