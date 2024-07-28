import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ServiceChrome
from selenium.webdriver.firefox.service import Service as ServiceFireFox
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FireFoxOptions


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption("--headless", action="store_true", help="Run headless")


@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("browser_name")
    headless = request.config.getoption("--headless")

    if browser_name == 'chrome':
        print("\nstart chrome browser for test..")
        options = ChromeOptions()
        preferences = {"download.default_directory": os.path.join(os.getcwd(), "downloads")}
        options.add_experimental_option("prefs", preferences)
        if headless:
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")
        service = ServiceChrome(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

    if browser_name == 'firefox':
        print("\nstart firefox browser for test..")
        options = FireFoxOptions()
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
        service = ServiceFireFox(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)

    yield driver
    driver.quit()
