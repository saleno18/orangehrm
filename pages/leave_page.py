

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LeavePage(BasePage):

    ASSIGN_LEAVE_TAB = (By.XPATH, "//a[text()='Assign Leave']")
    EMPLOYEE_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Type for hints...']")
    EMPLOYEE_SUGGESTION = (By.CSS_SELECTOR, ".oxd-autocomplete-option")
    LEAVE_TYPE_DROPDOWN = (By.XPATH, "(//div[contains(@class,'oxd-select-text')])[1]")
    DROPDOWN_OPTION = (By.CSS_SELECTOR, ".oxd-select-option")
    ASSIGN_BUTTON = (By.XPATH, "//button[normalize-space()='Assign']")
    SUCCESS_TOAST = (By.CSS_SELECTOR, ".oxd-toast-content--success")

    def click_assign_leave_tab(self):
        self.click(self.ASSIGN_LEAVE_TAB)

    def assign_leave(self, employee_name: str, leave_type: str):
        """Fill and submit the Assign Leave form."""
        self.type_text(self.EMPLOYEE_NAME_INPUT, employee_name)
        suggestions = self.find_all(self.EMPLOYEE_SUGGESTION)
        if suggestions:
            suggestions[0].click()

        self.select_dropdown_option(self.LEAVE_TYPE_DROPDOWN, leave_type, self.DROPDOWN_OPTION)
        self.click(self.ASSIGN_BUTTON)

    def is_leave_assigned_successfully(self) -> bool:
        return self.is_visible(self.SUCCESS_TOAST, timeout=10)
