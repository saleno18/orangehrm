

from pages.admin_page import AdminPage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from config.config import NEW_USER


def test_create_user_and_login_with_new_credentials(logged_in_dashboard, driver):
    logged_in_dashboard.click_menu_item("Admin")

    admin_page = AdminPage(driver)
    admin_page.click_add_user()
    admin_page.add_new_user(
        user_role=NEW_USER["user_role"],
        employee_name=NEW_USER["employee_name"],
        status=NEW_USER["status"],
        username=NEW_USER["username"],
        password=NEW_USER["password"],
        confirm_password=NEW_USER["confirm_password"],
    )

    assert admin_page.is_user_created_successfully(), "New user should be created successfully."

    # Log out of the admin session
    logged_in_dashboard.logout()

    # Attempt login with the newly created user
    login_page = LoginPage(driver)
    login_page.login(NEW_USER["username"], NEW_USER["password"])

    dashboard = DashboardPage(driver)
    assert dashboard.is_loaded(), (
        f"Newly created user '{NEW_USER['username']}' should be able to log in."
    )
