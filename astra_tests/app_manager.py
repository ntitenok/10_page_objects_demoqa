from astra_tests.pages.login_page import LoginPage
from astra_tests.utils.selenium_commands import Navigation
from astra_tests.pages.cloud_page import CloudPage


class ApplicationManager():
    def __init__(self, driver):
        self.driver = driver
        self.navigation = Navigation(driver)
        self.login = LoginPage(driver)
        self.cloud = CloudPage(driver)


