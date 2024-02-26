from enum import StrEnum

from selene import browser, have, be
from selene import by
import os


class Gender(StrEnum):
    male = '[for="gender-radio-1"]'
    female = '[for="gender-radio-2"]'
    other = '[for="gender-radio-3"]'


class Hobbies(StrEnum):
    sports = '[for="hobbies-checkbox-1"]'
    reading = '[for="hobbies-checkbox-2"]'
    music = '[for="hobbies-checkbox-3"]'


class StudentRegistrationPage:

    def open_registration_form(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)

    def fill_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)

    def selected_gender(self, value):
        browser.element(value).click()

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
            browser.element(value).click()

    def load_file(self, path):
        browser.element('#uploadPicture').send_keys(os.path.abspath(path))

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
