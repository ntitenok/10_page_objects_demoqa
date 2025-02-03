from astra_tests.utils.selenium_commands import SeleniumCommands


class LoginPage():

    USER_INPUT = '#user'
    PASSWORD_INPUT = '#password'
    SUBMIT = 'button[type="submit"]'


    def __init__(self, driver):
        self.driver = driver
        self._s = SeleniumCommands(driver)



    def enter_disk(self, user: str, password: str):
        self._s.type(self.USER_INPUT, user)
        self._s.type(self.PASSWORD_INPUT, password)
        self._s.click(self.SUBMIT)

