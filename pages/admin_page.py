
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AdminPage(BasePage):

    ADD_BUTTON = (By.XPATH, "//button[normalize-space()='Add']")
    USER_ROLE_DROPDOWN = (By.XPATH, "(//div[contains(@class,'oxd-select-text')])[1]")
    DROPDOWN_OPTION = (By.CSS_SELECTOR, ".oxd-select-option")
    EMPLOYEE_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Type for hints...']")
    EMPLOYEE_SUGGESTION = (By.CSS_SELECTOR, ".oxd-autocomplete-option")
    STATUS_DROPDOWN = (By.XPATH, "(//div[contains(@class,'oxd-select-text')])[2]")
    USERNAME_INPUT = (By.XPATH, "(//div[contains(@class,'user-password-row')]/preceding-sibling::div//input)[1]")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']")
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")
    SUCCESS_TOAST = (By.CSS_SELECTOR, ".oxd-toast-content--success")

    SEARCH_USERNAME_INPUT = (By.XPATH, "(//label[text()='Username']/following::input)[1]")
    SEARCH_BUTTON = (By.XPATH, "//button[normalize-space()='Search']")
    RESULT_TABLE_ROWS = (By.CSS_SELECTOR, ".oxd-table-card")
    NO_RECORDS_FOUND = (By.CSS_SELECTOR, ".oxd-text--span")

    def click_add_user(self):
        self.click(self.ADD_BUTTON)

    def add_new_user(self, user_role: str, employee_name: str, status: str,
                      username: str, password: str, confirm_password: str):
        """Fill and submit the 'Add User' form under Admin > User Management."""
        self.select_dropdown_option(self.USER_ROLE_DROPDOWN, user_role, self.DROPDOWN_OPTION)

        self.type_text(self.EMPLOYEE_NAME_INPUT, employee_name)
        suggestions = self.find_all(self.EMPLOYEE_SUGGESTION)
        if suggestions:
            suggestions[0].click()

        self.select_dropdown_option(self.STATUS_DROPDOWN, status, self.DROPDOWN_OPTION)

        self.type_text(self.USERNAME_INPUT, username)

        password_fields = self.find_all(self.PASSWORD_INPUT)
        password_fields[0].clear()
        password_fields[0].send_keys(password)
        password_fields[1].clear()
        password_fields[1].send_keys(confirm_password)

        self.click(self.SAVE_BUTTON)

    def is_user_created_successfully(self) -> bool:
        """Return True if the success toast is displayed after saving."""
        return self.is_visible(self.SUCCESS_TOAST, timeout=10)

    def search_user_by_username(self, username: str):
        """Search the User Management list for a given username."""
        self.type_text(self.SEARCH_USERNAME_INPUT, username)
        self.click(self.SEARCH_BUTTON)

    def is_user_present_in_results(self, username: str) -> bool:
        """Return True if the given username appears in the search results table."""
        rows = self.find_all(self.RESULT_TABLE_ROWS)
        for row in rows:
            if username in row.text:
                return True
        return False
