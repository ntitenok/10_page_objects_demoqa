import datetime
import time

from pages.registration_page import StudentRegistrationPage
from data.users import Gender, Hobbies, User


def test_student_registration_form():
    registration_page = StudentRegistrationPage()
    nikolai = User(first_name='Nikolai', last_name='Titenok', email='ntitenok@gmail.com', gender=Gender.Male,
                   mobile_number='1234567890', birth_date=datetime.date(1989, 5, 22), subjects='Computer Science',
                   hobbies=Hobbies.Music, file_name='myfile.txt', current_address="Bombey's street",
                   state='Uttar Pradesh', city='Agra')
    registration_page.open_registration_form()
    registration_page.register_student(nikolai)
    registration_page.assert_registration_form(nikolai)
