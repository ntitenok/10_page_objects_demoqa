import datetime
from demoqa_tests.application import app

from demoqa_tests.model.pages.registration_page import StudentRegistrationPage
from demoqa_tests.data import Gender, Hobbies, User


def test_student_registration_form():
    nikolai = User(first_name='Nikolai', last_name='Titenok', email='ntitenok@gmail.com', gender=Gender.Male,
                   mobile_number='1234567890', birth_date=datetime.date(1989, 5, 22), subjects='Computer Science',
                   hobbies=Hobbies.Music, file_name='myfile.txt', current_address="Bombey's street",
                   state='Uttar Pradesh', city='Agra')
    app.simple_registration.open_form()
    app.simple_registration.register_student(nikolai)
    app.simple_registration.assert_form(nikolai)
