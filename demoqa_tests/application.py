from demoqa_tests.model.components.left_panel import Panel
from demoqa_tests.model.pages.text_box_page import TextBoxPage
from demoqa_tests.model.pages.registration_page import StudentRegistrationPage


class Application:
    def __init__(self):
        self.student_registration = StudentRegistrationPage()
        self.text_box = TextBoxPage()
        self.left_panel = Panel()


app = Application()
