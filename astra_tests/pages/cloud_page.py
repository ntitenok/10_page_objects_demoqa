from astra_tests.utils.selenium_commands import SeleniumCommands


class CloudPage():
    SELECT_FILE_CHECKBOX = '[data-file="{}"] label'
    SUBMIT = 'button[type="submit"]'
    ACTIONS_DROPDOWN = '.actions-selected'
    DELETE_ACTION = '.item-delete'
    DIALOG_TITTLE = '.oc-dialog-title:nth-of-type(1)'

    def __init__(self, driver):
        self.driver = driver
        self._s = SeleniumCommands(driver)

    def delete_file(self, file_name):
        self._s.click(self.SELECT_FILE_CHECKBOX.format(file_name)).click(self.ACTIONS_DROPDOWN).click(
            self.DELETE_ACTION)

    def check_delete_box(self, text):
        self._s.check_text(self.DIALOG_TITTLE, text)
