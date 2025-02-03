import pytest
from selene import browser
import allure
import datetime

@pytest.fixture(scope='function', autouse=True)
def open_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://demoqa.com'

    yield
    attach = browser.driver.get_screenshot_as_png()
    allure.attach(attach, name=f"Screenshot {datetime.date.today()}", attachment_type=allure.attachment_type.PNG)

    browser.quit()
