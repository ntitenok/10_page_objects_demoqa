from selene import browser, be, have, by
from demoqa_tests import resource
from demoqa_tests.data.users import User


class StudentRegistrationPage:

    def fill_student_form(self, user: User):

        self.__fill_first_name(user.first_name)
        self.__fill_last_name(user.last_name)
        self.__fill_email(user.email)
        self.__select_gender(f'[for="gender-radio-{user.gender.value}"]')
        self.__fill_mobile_number(user.mobile_number)
        self.__fill_date_of_birth(user.birth_date)
        self.__select_subjects(user.subjects)
        self.__select_hobbies(f'[for="hobbies-checkbox-{user.hobbies.value}"]')
        self.__load_file(user.file)
        self.__select_current_address(user.current_address)
        self.__select_state_and_city(user.state, user.city)
        self.__submit_registration_form()

    def assert_student_form(self, user: User):
        browser.element('.table').all('td').even.should(
            have.texts(
                f'{user.first_name} {user.last_name}', user.email, user.gender.Male.name,
                user.mobile_number,
                user.birth_date.strftime('%d %B,%Y'), user.subjects, user.hobbies.Music.name,
                user.file_name,
                user.current_address, f'{user.state} {user.city}'))

    def open_form(self):
        browser.open('/automation-practice-form')

    def __fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)

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
        browser.element('.react-datepicker__month-select').click().element(by.text(birth_date.strftime('%B'))).click()
        browser.element('.react-datepicker__year-select').click()
        browser.element('.react-datepicker__year-select').click().element(by.text(birth_date.strftime('%Y'))).click()
        browser.element(f'.react-datepicker__day--0{birth_date.day}').click()

    def __select_subjects(self, *values):
        for value in values:
            browser.element('#subjectsInput').type(value).press_enter()

    def __select_hobbies(self, *values):
        for value in values:
            browser.element(value).click()

    def __load_file(self, value):
        browser.element('#uploadPicture').set_value(resource.path(value))

    def __select_current_address(self, value):
        browser.element('#currentAddress').should(be.blank).type(value)

    def __select_state_and_city(self, value_state, value_city):

        browser.element('#state').click().element(by.text(value_state)).click()
        browser.element('#city').click().element(by.text(value_city)).click()

    def __submit_registration_form(self):
        browser.element('#submit').click()
