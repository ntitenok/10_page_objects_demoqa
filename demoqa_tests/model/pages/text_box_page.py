import time

from selene import browser, have, be
from demoqa_tests.data.users import User

class TextBoxPage:
    def fill_user_form(self, user: User):
        browser.element('#userName').should(be.blank).type(f'{user.first_name} {user.last_name}')
        browser.element('#userEmail').should(be.blank).type(user.email)
        browser.element('#currentAddress').should(be.blank).type(user.current_address)
        browser.element('#permanentAddress').should(be.blank).type(f'{user.state} {user.city}')
        browser.element('#submit').click()

    def assert_user_form(self, user: User):

        browser.element('#output #name').should(have.exact_text(f'Name:{user.first_name} {user.last_name}'))
        browser.element('#output #email').should(have.exact_text(f'Email:{user.email}'))
        browser.element('#output #currentAddress').should(have.exact_text(f"Current Address :{user.current_address}"))
        browser.element('#output #permanentAddress').should(have.exact_text(f'Permananet Address :{user.state} {user.city}'))


        # browser.element('#output').all('p').even.should(
        #     have.texts(
        #         f'Name:{user.first_name} {user.last_name}', f'Email:{user.email}',
        #         f'Current Address :{user.current_address}', f'Permananet Address :{user.state} {user.city}'))
