from time import sleep
from selenium.common.exceptions import NoSuchElementException

from pages.base_page import BasePage
from pom.utils import wait_loop


class DashboardPage(BasePage):
    def __init__(self):
        BasePage.__init__(self)

    def open_campaigns_page(self):
        element = self.driver.find_element_by_xpath("//div[@class='nav main']//a[contains(@href,'campaigns')]"
                                                    "//div[@class='content']")
        element.click()

    def click_button_create_campaign(self):
        button = self.driver.find_element_by_xpath("//div[@class='header-wrapper']"
                                                   "//button[@class='lp-button color-primary normal enabled']")
        element = wait_loop(condition=lambda: button, timeout_seconds=10)
        if not element:
            raise NoSuchElementException("Missing element")
        button.click()
        sleep(4)

    def verify_open_page(self, expected: str):
        element = wait_loop(condition=lambda: self.driver.find_element_by_xpath("//div[@class='placeholder-pane-text']")
                            , timeout_seconds=10)
        if not element:
            raise NoSuchElementException("Missing element")
        actual = element.text
        assert actual == expected

    def change_text(self):
        element = self.driver.find_element_by_xpath("//div[@class='campaign-name-box']//div[@class='name']")
        element.click()
        element = self.driver.find_element_by_css_selector("input.lp-wrapped-text-input-field")
        element.click()
        element.clear()
        element.send_keys("New Campaign Test")
        button = self.driver.find_element_by_xpath("//button[@type='button']//span[text()='Save']")
        button.click()

    def set_goal(self):
        element = self.driver.find_element_by_xpath("//div[@class='options']//p[text()='Onboard']")
        element = wait_loop(condition=lambda: element, timeout_seconds=10)
        if not element:
            raise NoSuchElementException("Missing element")
        element.click()

    def press_on_tab(self, tab_name: str):
        element = self.driver.find_element_by_xpath("//div[@class='tab']//span[text()='" + tab_name + "']").click()
        return element

    def set_scheduled(self, option: str):
        element = self.driver.find_element_by_xpath("//div[@class='options']//p[text()='" + option + "']")
        sleep(2)
        element.click()
        element = self.driver.find_element_by_xpath("//div[@class='date-time']//i[@class='lp-icon']")
        element = wait_loop(condition=lambda: element, timeout_seconds=10)
        if not element:
            raise NoSuchElementException("No")
        element.click()
        sleep(3)
        element = self.driver.find_element_by_xpath("//div[@class='lp-calendar-week']//div[@class='lp-day']"
                                                    "//span[text()='8']")

        element.click()

    def set_push_notifications(self):
        element = self.driver.find_element_by_xpath("//div[@class='composer-actions-kind-item']"
                                                    "//span[text()='Push Notification']")
        sleep(2)
        element.click()
        element = self.driver.find_element_by_xpath("//div[@class='text-field-view']//input")
        element.click()
        element.clear()
        element.send_keys("test")

    def click_button_to_start_campaign(self, button_name: str):
        element = self.driver.find_element_by_xpath("//button[@type='button']//span[text()='" + button_name + "']")
        sleep(2)
        element.click()

    def click_start_modal_button(self, button_name: str):
        element = self.driver.find_element_by_xpath("//button[@type='button']//span[text()='" + button_name + "']")

        element.click()

    def click_end_button(self, button_name: str):
        element = self.driver.find_element_by_xpath("//button[@type='button']//span[text()='" + button_name + "']")
        sleep(2)
        element.click()

    def click_end_modal_button(self, button_name: str):
        element = self.driver.find_element_by_xpath("//div[@class='footer']//span[text()='" + button_name + "']")
        element.click()

    def verify_state(self, expected_state: str):
        sleep(2)
        actual = self.driver.find_element_by_xpath("//div[@class='navigation-bar-controls']//span").text
        assert actual == expected_state, f'Actual state is: {actual} but expected is: {expected_state}'

    def close_browser(self):
        self.driver.quit()
