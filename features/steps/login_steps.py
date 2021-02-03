from behave import *
from pages.login_page import LoginPage


@step("Open Leanplum URL and login")
def open_page(context):
    login = LoginPage()
    login.set_email()
    login.set_password()
    login.sign_in_button()
    login.verify_login()
