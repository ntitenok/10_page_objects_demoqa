import datetime
from demoqa_tests.application import app
from demoqa_tests.data import users

def test_student_registration():
    app.student_registration.open_form()
    app.student_registration.fill_student_form(users.nikolai)
    app.student_registration.assert_student_form(users.nikolai)


    # def test_text_box(self):
    #     app.left_panel.open_text_box()
    #     app.text_box.fill_user_form(self.nikolai)
    #     app.text_box.assert_user_form(self.nikolai)
