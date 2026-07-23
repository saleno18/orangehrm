

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DashboardPage(BasePage):

    MENU_ITEM_LINK = (By.CSS_SELECTOR, ".oxd-main-menu-item")
    USER_DROPDOWN = (By.CSS_SELECTOR, ".oxd-userdropdown-tab")
    LOGOUT_LINK = (By.XPATH, "//a[text()='Logout']")
    DASHBOARD_HEADER = (By.CSS_SELECTOR, ".oxd-topbar-header-breadcrumb h6")

    EXPECTED_MENU_ITEMS = [
        "Admin", "PIM", "Leave", "Time", "Recruitment",
        "My Info", "Performance", "Dashboard",
    ]

    def is_loaded(self) -> bool:
        """Confirm the dashboard/home page loaded successfully after login."""
        return self.is_visible(self.DASHBOARD_HEADER, timeout=15)

    def get_menu_item_locator(self, name: str):
        return (By.XPATH, f"//span[@class='oxd-main-menu-item--name' and text()='{name}']")

    def is_menu_item_visible_and_clickable(self, name: str) -> bool:
        """Check that a given main-menu item (e.g. 'Admin', 'PIM') is visible and clickable."""
        locator = self.get_menu_item_locator(name)
        return self.is_visible(locator, timeout=10) and self.is_clickable(locator, timeout=10)

    def click_menu_item(self, name: str):
        """Click a main-menu item by its visible text."""
        self.click(self.get_menu_item_locator(name))

    def logout(self):
        """Open the user dropdown and click Logout."""
        self.click(self.USER_DROPDOWN)
        self.click(self.LOGOUT_LINK)
