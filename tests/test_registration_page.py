import datetime
import time

from demoqa_tests.application import app

from demoqa_tests.model.pages.registration_page import StudentRegistrationPage
from demoqa_tests.data.users import User, Gender, Hobbies


class TestDemoqa:

    nikolai = User(first_name='Nikolai', last_name='Titenok', email='ntitenok@gmail.com', gender=Gender.Male,
                   mobile_number='1234567890', birth_date=datetime.date(1989, 5, 22), subjects='Computer Science',
                   hobbies=Hobbies.Music, file_name='myfile.txt', current_address="Bombey's street",
                   state='Uttar Pradesh', city='Agra')

    def test_student_registration(self):
        app.student_registration.open_form()
        app.student_registration.fill_student_form(self.nikolai)
        app.student_registration.assert_student_form(self.nikolai)


    def test_text_box(self):
        app.student_registration.open_form()
        app.left_panel.open_text_box()
        app.text_box.fill_user_form(self.nikolai)
        app.text_box.assert_user_form(self.nikolai)
