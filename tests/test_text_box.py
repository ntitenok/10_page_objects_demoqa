from demoqa_tests.application import app
from tests.test_registration_page import users

def test_text_box():
    app.left_panel.open_text_box()
    app.text_box.fill_user_form(users.nikolai)
    app.text_box.assert_user_form(users.nikolai)
