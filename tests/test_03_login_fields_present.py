

from pages.login_page import LoginPage


def test_login_fields_visible_and_enabled(driver):
    login_page = LoginPage(driver).load()

    assert login_page.is_username_field_visible_and_enabled(), (
        "Username field must be visible and enabled for input."
    )
    assert login_page.is_password_field_visible_and_enabled(), (
        "Password field must be visible and enabled for input."
    )
