

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ClaimPage(BasePage):

    SUBMIT_CLAIM_TAB = (By.XPATH, "//a[text()='Submit Claim']")
    EVENT_DROPDOWN = (By.XPATH, "(//div[contains(@class,'oxd-select-text')])[1]")
    CURRENCY_DROPDOWN = (By.XPATH, "(//div[contains(@class,'oxd-select-text')])[2]")
    DROPDOWN_OPTION = (By.CSS_SELECTOR, ".oxd-select-option")
    REMARKS_TEXTAREA = (By.CSS_SELECTOR, "textarea")
    CREATE_BUTTON = (By.XPATH, "//button[normalize-space()='Create']")
    SUCCESS_TOAST = (By.CSS_SELECTOR, ".oxd-toast-content--success")
    CLAIM_STATUS_HEADER = (By.CSS_SELECTOR, ".oxd-topbar-header-breadcrumb h6")

    def click_submit_claim_tab(self):
        self.click(self.SUBMIT_CLAIM_TAB)

    def initiate_claim(self, event_name: str, currency: str, remarks: str):
        """Fill and submit a new claim request."""
        self.select_dropdown_option(self.EVENT_DROPDOWN, event_name, self.DROPDOWN_OPTION)
        self.select_dropdown_option(self.CURRENCY_DROPDOWN, currency, self.DROPDOWN_OPTION)
        if self.is_visible(self.REMARKS_TEXTAREA, timeout=3):
            self.type_text(self.REMARKS_TEXTAREA, remarks)
        self.click(self.CREATE_BUTTON)

    def is_claim_submitted_successfully(self) -> bool:
        """Return True if the claim was created and the status page loaded."""
        return self.is_visible(self.CLAIM_STATUS_HEADER, timeout=10)
