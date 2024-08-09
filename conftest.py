import os
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--page_load_strategy", action="store", default="normal",
                     help="Set page load strategy: normal, eager, or none")


@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("browser")
    headless = request.config.getoption("headless")
    page_load_strategy = request.config.getoption("page_load_strategy")

    if browser_name == 'chrome':
        print("\nstart chrome browser for test..")
        options = webdriver.ChromeOptions()
        user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36")
        options.add_argument(f"--user-agent={user_agent}")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.page_load_strategy = page_load_strategy
        preferences = {"download.default_directory": os.path.join(os.getcwd(), "downloads")}
        options.add_experimental_option("prefs", preferences)
        if headless:
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)

    elif browser_name == 'firefox':
        print("\nstart firefox browser for test..")
        options = webdriver.FirefoxOptions()
        options.page_load_strategy = page_load_strategy
        download_dir = os.path.join(os.getcwd(), "downloads")
        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.download.manager.showWhenStarting", False)
        options.set_preference("browser.download.dir", download_dir)
        options.set_preference("browser.helperApps.neverAsk.saveToDisk", "image/jpeg")
        if headless:
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")
        driver = webdriver.Firefox(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    yield driver
    driver.quit()
