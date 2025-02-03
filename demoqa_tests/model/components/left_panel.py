from selene import browser, have
from demoqa_tests.model.pages.text_box_page import TextBoxPage


class Panel:
    def open(self, category, menu):
        browser.open('/')
        browser.element('.category-cards').all('.card-body').element_by(have.exact_text(category)).click()
        browser.element('.menu-list').all('.text').element_by(have.exact_text(menu)).click()


    def open_text_box(self):
        self.open('Elements', 'Text Box')
        return TextBoxPage()
