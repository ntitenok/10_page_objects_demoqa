from enum import StrEnum

from selene import browser, have, be
from selene import by
import os
from data.users import User





class StudentRegistrationPage:

    def __init__(self):
        self.first_name = browser.element('#firstName').should(be.blank)


    def register_student(self, user: User):

        self.__fill_first_name(user.first_name)
        self.__fill_last_name(user.last_name)
        self.__fill_email(user.email)
        self.__select_gender(user.gender)
        self.__fill_mobile_number(user.mobile_number)
        self.__fill_date_of_birth(user.birth_date)
        self.__select_subjects(user.subjects)
        self.__select_hobbies(user.hobbies)
        self.__select_hobbies()



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


    def open_registration_form(self):
        browser.open('/automation-practice-form')

    def __fill_first_name(self, value):
        self.first_name.type(value)

    def __fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)

    def __fill_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)

    def __select_gender(self, value):
        browser.element(value).click()

    def __fill_mobile_number(self, value):
        browser.element('#userNumber').should(be.blank).type(value)

    def __fill_date_of_birth(self, birth_date):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element('.react-datepicker__month-select').click().element(by.text(birth_date.month)).click()
        browser.element('.react-datepicker__year-select').click()
        browser.element('.react-datepicker__year-select').click().element(by.text(birth_date.year)).click()
        browser.element(f'.react-datepicker__day--0{birth_date.day}').click()

    def __select_subjects(self, *values):
        for value in values:
            browser.element('#subjectsInput').type(value).press_enter()

    def __select_hobbies(self, *values):
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
