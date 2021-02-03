from behave import *
from pages.dashboard_page import DashboardPage

dashboard = DashboardPage()


@then("Open campaign page")
def open_campaign_page(context):
    dashboard.open_campaigns_page()


@step("Click button Create Campaign to start creating new campaign")
def create_new_campaign(context):
    dashboard.click_button_create_campaign()


@step("Verify that the page is opened '{expected}'")
def create_new_campaign(context, expected):
    dashboard.verify_open_page(expected)


@step("Change the title of the campaign name")
def change_text(context):
    dashboard.change_text()


@step("Choose your goal")
def choose_goal(context):
    dashboard.set_goal()


@step("Click on '{tab_name}' to set your actions")
@step("Click on '{tab_name}' to set your delivery method")
@step("Click on '{tab_name}' to set your target")
def choose_tab_item(context, tab_name):
    dashboard.press_on_tab(tab_name)


@step("Set your '{option}'")
def set_scheduled(context, option):
    dashboard.set_scheduled(option)


@step("Choose your notifications Push")
def push_notifications(context):
    dashboard.set_push_notifications()


@step("Review and click on button '{button_name}'")
def button_review_start_campaign(context, button_name):
    dashboard.click_button_to_start_campaign(button_name)


@step("Click on button '{button_name}' from modal")
def button_start_campaign(context, button_name):
    dashboard.click_start_modal_button(button_name)


@step("Click on button '{button_name}' to finish")
def button_end_campaign(context, button_name):
    dashboard.click_end_button(button_name)


@step("Click on button '{button_name}' to close window")
def button_end_campaign_window(context, button_name):
    dashboard.click_end_modal_button(button_name)


@step("State of the created campaign is '{expected_state}'")
def verify_state_campaign(context, expected_state):
    dashboard.verify_state(expected_state)


@step("Close browser")
def close_browser(context):
    dashboard.close_browser()
