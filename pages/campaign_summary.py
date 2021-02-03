from time import sleep

from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage


class CampaignSummary(BasePage):
    def __init__(self):
        BasePage.__init__(self)

    def open_campaigns_list(self, campaign_name: str):
        element = self.driver.find_element_by_xpath("//div[@class='campaigns-entry-details']//"
                                                    f"div[text()='{campaign_name}']")
        element.click()

    def verify_name_of_campaign(self, expected_campaign_name: str):
        actual_name = self.driver.find_element_by_xpath("//div[@class='campaign-name-box']//span").text
        assert actual_name == expected_campaign_name, f'Expected campaign name is:{expected_campaign_name} ' \
                                                      f'but Actual is: {actual_name}'
