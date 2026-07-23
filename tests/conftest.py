

import os
import pytest
from datetime import datetime

from utils.driver_factory import DriverFactory
from utils.logger import get_logger
from pages.login_page import LoginPage
from config import config

logger = get_logger(__name__)


def pytest_addoption(parser):
    """Register the --browser CLI option for cross-browser test runs."""
    parser.addoption(
        "--browser",
        action="store",
        default=config.DEFAULT_BROWSER,
        help="Browser to run tests against: chrome | firefox | edge",
    )


@pytest.fixture(scope="function")
def driver(request):
    """
    Provide a fresh WebDriver instance per test (browser selectable via
    --browser) and guarantee it is closed afterwards, even on failure.
    """
    browser = request.config.getoption("--browser")
    drv = DriverFactory.get_driver(browser=browser)
    logger.info("=== Starting test: %s [%s] ===", request.node.name, browser)
    yield drv
    try:
        drv.quit()
    except Exception as exc:
        logger.warning("Driver failed to quit cleanly: %s", exc)
    logger.info("=== Finished test: %s ===", request.node.name)


@pytest.fixture(scope="function")
def logged_in_dashboard(driver):
    """Log in with the default admin credentials and return the DashboardPage."""
    from pages.dashboard_page import DashboardPage

    login_page = LoginPage(driver).load()
    login_page.login("Admin", "admin123")
    dashboard = DashboardPage(driver)
    assert dashboard.is_loaded(), "Dashboard failed to load after login"
    return dashboard


@pytest.fixture
def screenshot_dir():
    """Ensure a directory exists for screenshots captured during test runs."""
    path = os.path.join("reports", "screenshots")
    os.makedirs(path, exist_ok=True)
    return path


def take_screenshot(driver, screenshot_dir, name: str):
    """Capture and save a timestamped screenshot; returns the file path."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = os.path.join(screenshot_dir, f"{name}_{timestamp}.png")
    driver.save_screenshot(filepath)
    return filepath


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Log the pass/fail result of every test case, per project requirements."""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call":
        status = "PASSED" if report.passed else "FAILED" if report.failed else "SKIPPED"
        logger.info("Test result: %s -> %s", item.name, status)
