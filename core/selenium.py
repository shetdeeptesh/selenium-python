from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


from core import browser_actions
from logger import logger as Logger


_driver: webdriver = None
_logger = None


def setup(browser="chrome"):
    global _logger
    _logger = Logger.get_logger()
    _logger.info(f"Setting up {browser} browser")

    global _driver
    if browser.lower() == "chrome":
        _driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser.lower() == "firefox":
        _driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser.lower() == "edge":
        _driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        _logger.error(f"Invalid browser option: {browser}")
        raise ValueError("Invalid browser option")

    browser_actions.set_driver(_driver)
    return _driver


def teardown():
    if _driver:
        _logger.info(f"closing down browser")
        _driver.quit()
