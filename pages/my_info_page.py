

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MyInfoPage(BasePage):

    SUBMENU_ITEM = (By.CSS_SELECTOR, ".orangehrm-tabs a")
    PAGE_HEADER = (By.CSS_SELECTOR, ".oxd-topbar-header-breadcrumb h6")

    EXPECTED_SUBMENU_ITEMS = [
        "Personal Details",
        "Contact Details",
        "Emergency Contacts",
        "Dependents",
        "Immigration",
        "Job",
        "Salary",
        "Report-to",
        "Qualifications",
        "Memberships",
    ]

    def get_visible_submenu_items(self):
        """Return the visible text of every sub-menu tab under My Info."""
        items = self.find_all(self.SUBMENU_ITEM)
        return [item.text.strip() for item in items if item.text.strip()]

    def is_submenu_item_clickable(self, name: str) -> bool:
        locator = (By.XPATH, f"//a[contains(@class,'oxd-topbar-body-nav-tab-item') and text()='{name}']")
        return self.is_clickable(locator, timeout=5)

    def click_submenu_item(self, name: str):
        locator = (By.XPATH, f"//a[contains(@class,'oxd-topbar-body-nav-tab-item') and text()='{name}']")
        self.click(locator)

    def get_current_section_header(self) -> str:
        return self.get_text(self.PAGE_HEADER)
