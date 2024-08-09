import os
import pytest
from selenium import webdriver


# --- Configuring Pytest ---
def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--page_load_strategy", action="store", default="normal", help="Set page load strategy: normal, eager, or none")


# --- Fixture for WebDriver ---
@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("browser")
    headless = request.config.getoption("headless")
    page_load_strategy = request.config.getoption("page_load_strategy")

    driver = setup_browser(browser_name, headless, page_load_strategy)

    yield driver
    driver.quit()


# --- Browser Setup ---
def setup_browser(browser_name, headless, page_load_strategy):
    if browser_name == 'chrome':
        return setup_chrome(headless, page_load_strategy)
    elif browser_name == 'firefox':
        return setup_firefox(headless, page_load_strategy)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")


# --- Options for Chrome ---
def setup_chrome(headless, page_load_strategy):
    print("\nstart chrome browser for test..")
    options = webdriver.ChromeOptions()
    options.page_load_strategy = page_load_strategy
    options.add_argument(f"--user-agent={get_user_agent()}")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("prefs", {"download.default_directory": get_download_directory()})

    if headless:
        apply_headless_options(options)

    return webdriver.Chrome(options=options)


# --- Options for Firefox ---
def setup_firefox(headless, page_load_strategy):
    print("\nstart firefox browser for test..")
    options = webdriver.FirefoxOptions()
    options.page_load_strategy = page_load_strategy
    set_firefox_preferences(options)

    if headless:
        apply_headless_options(options)

    return webdriver.Firefox(options=options)


# --- General support functions ---
def get_user_agent():
    return ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36")


def get_download_directory():
    return os.path.join(os.getcwd(), "downloads")


def apply_headless_options(options):
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")


def set_firefox_preferences(options):
    download_dir = get_download_directory()
    options.set_preference("browser.download.folderList", 2)
    options.set_preference("browser.download.manager.showWhenStarting", False)
    options.set_preference("browser.download.dir", download_dir)
    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "image/jpeg")
