from selene.support.shared import browser

from demoqa_tests.model.components import Panel
from demoqa_tests.model.pages.profile_page import ProfilePage
from demoqa_tests.model.pages.registration_page import StudentRegistrationPage


class Application:
    def __init__(self):
        self.simple_registration = StudentRegistrationPage()
        self.profile = ProfilePage()
        self.panel = Panel()

app = Application()