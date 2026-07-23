

from pages.login_page import LoginPage


def test_forgot_password_shows_confirmation(driver):
    login_page = LoginPage(driver).load()
    login_page.click_forgot_password()

    login_page.submit_password_reset_request(username="Admin")

    confirmation = login_page.get_reset_confirmation_text()
    assert confirmation, "A confirmation message should appear after requesting a password reset."
    assert "reset password link sent" in confirmation.lower() or "sent" in confirmation.lower(), (
        f"Unexpected confirmation text: '{confirmation}'"
    )
