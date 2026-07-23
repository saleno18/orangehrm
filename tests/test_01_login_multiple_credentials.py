

import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from data.test_data import load_login_data
from utils.logger import get_logger

logger = get_logger(__name__)

login_dataset = load_login_data("data/login_data.csv")


@pytest.mark.parametrize(
    "record", login_dataset, ids=[row["test_id"] for row in login_dataset]
)
def test_login_with_data_driven_credentials(driver, record):
    logger.info(
        "Running %s (tester: %s) with username='%s'",
        record["test_id"], record["tester"], record["username"],
    )

    login_page = LoginPage(driver).load()
    login_page.login(record["username"], record["password"])

    if record["expected"] == "valid":
        dashboard = DashboardPage(driver)
        assert dashboard.is_loaded(), (
            f"[{record['test_id']}] Expected successful login for "
            f"'{record['username']}', but dashboard did not load."
        )
        # Perform logout after each successful login, per project spec
        dashboard.logout()
        assert login_page.is_page_loaded(), (
            f"[{record['test_id']}] Expected redirect to login page after logout."
        )
    else:
        error = login_page.get_error_message() or (
            "required field error" if login_page.has_required_field_errors() else ""
        )
        assert error, (
            f"[{record['test_id']}] Expected invalid credentials to be rejected "
            f"with an error message, but none was shown."
        )
