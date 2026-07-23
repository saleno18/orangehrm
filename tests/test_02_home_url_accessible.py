

from pages.login_page import LoginPage


def test_home_url_loads_without_error(driver):
    login_page = LoginPage(driver).load()
    assert login_page.is_page_loaded(), "Home page should load without error."
    assert "orangehrmlive" in driver.current_url, (
        f"Unexpected URL after navigation: {driver.current_url}"
    )
