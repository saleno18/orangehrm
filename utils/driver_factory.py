"""
Driver Factory
---------------
Creates and configures a Selenium WebDriver instance for the requested
browser, enabling cross-browser execution as required by the project scope.
Encapsulating this logic follows the Factory design pattern and keeps
browser-specific setup out of the test / page layers.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from config import config
from utils.logger import get_logger

logger = get_logger(__name__)


class DriverFactory:
    """Creates WebDriver instances for the browsers supported by the suite."""

    @staticmethod
    def get_driver(browser: str = None, headless: bool = None):
        """
        Build and return a configured WebDriver instance.

        Args:
            browser: 'chrome' | 'firefox' | 'edge' (defaults to config.DEFAULT_BROWSER).
            headless: Whether to run headless (defaults to config.HEADLESS).

        Returns:
            selenium.webdriver.Remote: A ready-to-use WebDriver instance.

        Raises:
            ValueError: If an unsupported browser name is supplied.
            RuntimeError: If driver initialization fails for any reason.
        """
        browser = (browser or config.DEFAULT_BROWSER).lower()
        headless = config.HEADLESS if headless is None else headless

        if browser not in config.SUPPORTED_BROWSERS:
            raise ValueError(
                f"Unsupported browser '{browser}'. Supported: {config.SUPPORTED_BROWSERS}"
            )

        try:
            logger.info("Initializing '%s' WebDriver (headless=%s)", browser, headless)

            if browser == "chrome":
                options = ChromeOptions()
                if headless:
                    options.add_argument("--headless=new")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--window-size=1920,1080")
                service = ChromeService(ChromeDriverManager().install())
                driver = webdriver.Chrome(service=service, options=options)

            elif browser == "firefox":
                options = FirefoxOptions()
                if headless:
                    options.add_argument("-headless")
                options.add_argument("--width=1920")
                options.add_argument("--height=1080")
                service = FirefoxService(GeckoDriverManager().install())
                driver = webdriver.Firefox(service=service, options=options)

            elif browser == "edge":
                options = EdgeOptions()
                if headless:
                    options.add_argument("--headless=new")
                options.add_argument("--window-size=1920,1080")
                service = EdgeService(EdgeChromiumDriverManager().install())
                driver = webdriver.Edge(service=service, options=options)

            driver.set_page_load_timeout(config.PAGE_LOAD_TIMEOUT)
            driver.implicitly_wait(0)  # rely on explicit waits instead
            return driver

        except Exception as exc:
            logger.error("Failed to initialize WebDriver for '%s': %s", browser, exc)
            raise RuntimeError(f"Failed to initialize WebDriver for '{browser}': {exc}") from exc
