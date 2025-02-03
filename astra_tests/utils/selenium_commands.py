from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from astra_tests.utils.selector import locator
from selenium.webdriver.common.keys import Keys


class Base:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)


class Navigation(Base):

    def open(self, url: str):
        self.driver.get(url)
        return self


class SeleniumCommands(Base):

    def element_is_visible(self, selector):
        return self.wait.until(
            ec.visibility_of_element_located(locator(selector))
        )

    def element_is_clickable(self, selector):
        return self.wait.until(
            ec.element_to_be_clickable(locator(selector))
        )

    def click(self, selector):
        self.element_is_clickable(selector).click()
        return self

    def type(self, selector, text: str):
        element = self.element_is_visible(selector)
        element.send_keys(text)
        return self

    def check_text(self, selector, expected_text):
        element = self.element_is_visible(selector)
        assert element.text == expected_text
