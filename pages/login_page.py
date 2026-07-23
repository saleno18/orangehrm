

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config import config


class LoginPage(BasePage):

    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_ALERT = (By.CSS_SELECTOR, ".oxd-alert-content-text")
    REQUIRED_FIELD_ERROR = (By.CSS_SELECTOR, ".oxd-input-group__message")
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, ".orangehrm-login-forgot-header")
    ORANGEHRM_LOGO = (By.CSS_SELECTOR, ".orangehrm-login-branding img")

    # Forgot-password page
    RESET_USERNAME_INPUT = (By.NAME, "username")
    RESET_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    RESET_CONFIRMATION_TITLE = (By.CSS_SELECTOR, ".orangehrm-forgot-password-title")

    def load(self):
        """Navigate to the login page."""
        self.open(config.LOGIN_URL)
        return self

    def is_page_loaded(self) -> bool:
        """Confirm the login page (and site) has loaded without error."""
        return self.is_visible(self.LOGIN_BUTTON, timeout=10)

    def is_username_field_visible_and_enabled(self) -> bool:
        field = self.find(self.USERNAME_INPUT)
        return field.is_displayed() and field.is_enabled()

    def is_password_field_visible_and_enabled(self) -> bool:
        field = self.find(self.PASSWORD_INPUT)
        return field.is_displayed() and field.is_enabled()

    def login(self, username: str, password: str):
        """Perform a login attempt with the supplied credentials."""
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        """Return the invalid-credentials banner text, if present."""
        if self.is_visible(self.ERROR_ALERT, timeout=5):
            return self.get_text(self.ERROR_ALERT)
        return ""

    def has_required_field_errors(self) -> bool:
        """Return True if 'Required' validation messages are shown (e.g. blank username)."""
        return len(self.find_all(self.REQUIRED_FIELD_ERROR)) > 0

    def click_forgot_password(self):
        """Click the 'Forgot your password?' link."""
        self.click(self.FORGOT_PASSWORD_LINK)

    def submit_password_reset_request(self, username: str):
        """On the forgot-password page, submit a reset request for the given username."""
        self.type_text(self.RESET_USERNAME_INPUT, username)
        self.click(self.RESET_BUTTON)

    def get_reset_confirmation_text(self) -> str:
        """Return the confirmation heading shown after submitting a reset request."""
        if self.is_visible(self.RESET_CONFIRMATION_TITLE, timeout=10):
            return self.get_text(self.RESET_CONFIRMATION_TITLE)
        return ""
