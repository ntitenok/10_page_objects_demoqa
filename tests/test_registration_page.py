from pages.registration_page import StudentRegistrationPage
from pages.registration_page import Gender
from pages.registration_page import Hobbies
from data.users import User


def test_student_registration_form():
    registration_page = StudentRegistrationPage()
    nikolay = User(first_name='Nikolai')

    registration_page.open_registration_form()
    registration_page.__

    registration_page.fill_first_name('Nikolai')
    registration_page.__fill_last_name('Titenok')
    registration_page.__fill_email('ntitenok@gmail.com')
    registration_page.__select_gender(Gender.male.value)
    registration_page.__fill_mobile_number('1234567890')
    registration_page.__fill_date_of_birth('May', '1989', '22')
    registration_page.__select_subjects('Computer Science', 'Maths', 'Chemistry')
    registration_page.__select_hobbies(Hobbies.sports.value, Hobbies.reading.value, Hobbies.music.value)
    registration_page.load_file('resources\\myfile.txt')
    registration_page.select_current_address("Bombey's street")
    registration_page.select_state_and_city('Haryana', 'Panipat')
    registration_page.submit_registration_form()
    registration_page.assert_registration_form('Nikolai Titenok', 'ntitenok@gmail.com', 'Male', '1234567890',
                                               '22 May,1989',
                                               'Computer Science, Maths, Chemistry', 'Sports, Reading, Music',
                                               'myfile.txt', "Bombey's street",
                                               'Haryana Panipat')
