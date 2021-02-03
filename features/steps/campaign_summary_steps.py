from behave import *
from pages.campaign_summary import CampaignSummary
from pages.dashboard_page import DashboardPage


summary_list = CampaignSummary()
dashboard = DashboardPage()


@given("Open created campaign '{campaign_name}'")
def open_campaign_page(context, campaign_name):
    dashboard.open_campaigns_page()
    summary_list.open_campaigns_list(campaign_name)


@step("Verify the name of the campaign '{expected_campaign_name}'")
def open_campaign_page(context, expected_campaign_name):
    summary_list.verify_name_of_campaign(expected_campaign_name)
