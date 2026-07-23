

from pages.admin_page import AdminPage
from config.config import NEW_USER


def test_new_user_present_in_user_management_list(logged_in_dashboard, driver):
    logged_in_dashboard.click_menu_item("Admin")

    admin_page = AdminPage(driver)
    admin_page.search_user_by_username(NEW_USER["username"])

    assert admin_page.is_user_present_in_results(NEW_USER["username"]), (
        f"User '{NEW_USER['username']}' should appear in the Admin > "
        f"User Management search results."
    )
