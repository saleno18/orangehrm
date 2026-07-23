

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
)

from config import config
from utils.logger import get_logger

logger = get_logger(__name__)


class BasePage:
    """Common functionality shared by every page object."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, config.DEFAULT_TIMEOUT)

    def open(self, url):
        """Navigate to a URL."""
        logger.info("Navigating to %s", url)
        self.driver.get(url)

    def find(self, locator):
        """Wait for and return a single element."""
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException as exc:
            raise NoSuchElementException(f"Element not found for locator: {locator}") from exc

    def find_all(self, locator):
        """Wait for and return a list of elements."""
        try:
            return self.wait.until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            logger.warning("No elements found for locator: %s", locator)
            return []

    def click(self, locator):
        """Wait until an element is clickable, then click it safely."""
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except ElementClickInterceptedException:
            element = self.find(locator)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)
        except (TimeoutException, StaleElementReferenceException) as exc:
            raise NoSuchElementException(f"Element not clickable for locator: {locator}") from exc

    def type_text(self, locator, text):
        """Clear a field and type the given text."""
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Return the visible text of an element."""
        return self.find(locator).text

    def is_visible(self, locator, timeout=None):
        """Return True if the element becomes visible within the timeout, else False."""
        try:
            wait = WebDriverWait(self.driver, timeout or config.DEFAULT_TIMEOUT)
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def is_clickable(self, locator, timeout=None):
        """Return True if the element becomes clickable within the timeout, else False."""
        try:
            wait = WebDriverWait(self.driver, timeout or config.DEFAULT_TIMEOUT)
            wait.until(EC.element_to_be_clickable(locator))
            return True
        except TimeoutException:
            return False

    def select_dropdown_option(self, dropdown_locator, option_text: str, option_locator):
        """
        Handle OrangeHRM's custom (non-native <select>) dropdown widgets:
        click to open, then click the matching option by visible text.
        """
        self.click(dropdown_locator)
        options = self.find_all(option_locator)
        for option in options:
            if option.text.strip() == option_text:
                option.click()
                return
        raise NoSuchElementException(f"Dropdown option '{option_text}' not found.")
