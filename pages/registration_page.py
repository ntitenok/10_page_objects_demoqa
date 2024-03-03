from enum import Enum
from selene import browser, by, have, be
from pages.resource import path


class Gender(Enum):
    male = 1
    female = 2
    other = 3

class Hobbies(Enum):
    sports = 1
    reading = 2
    music = 3


class StudentRegistrationPage:

    def open_registration_form(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)

    def fill_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)

    def select_gender(self, value):
        browser.element(f'[for="gender-radio-{value}"]').click()

    def fill_mobile_number(self, value):
        browser.element('#userNumber').should(be.blank).type(value)

    def fill_date_of_birth(self, month, year, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element('.react-datepicker__month-select').click().element(by.text(month)).click()
        browser.element('.react-datepicker__year-select').click()
        browser.element('.react-datepicker__year-select').click().element(by.text(year)).click()
        browser.element(f'.react-datepicker__day--0{day}').click()

    def select_subjects(self, *values):
        for value in values:
            browser.element('#subjectsInput').type(value).press_enter()

    def select_hobbies(self, *values):
        for value in values:
            browser.element(f'[for="hobbies-checkbox-{value}"]').click()

    def load_file(self, value):
        browser.element('#uploadPicture').set_value(path(value))
    def select_current_address(self, value):
        browser.element('#currentAddress').should(be.blank).type(value)

    def select_state_and_city(self, value_state, value_city):

        browser.element('#state').click().element(by.text(value_state)).click()
        browser.element('#city').click().element(by.text(value_city)).click()

    def submit_registration_form(self):
        browser.element('#submit').click()

    def assert_registration_form(self, full_name, email, gender, mobile_number, birth_date, subjects, hobbies,
                                 file_name, current_address, state_and_city):
        browser.element('.table').all('td:nth-child(2)').should(
            have.texts(full_name, email, gender, mobile_number, birth_date, subjects, hobbies, file_name,
                       current_address, state_and_city))
