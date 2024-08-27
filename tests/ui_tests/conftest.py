import platform
import os
import pytest
import allure
from selenium import webdriver


# --- Configuring Pytest ---
def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption(
        "--page_load_strategy", action="store", default="normal", help="Set page load strategy: normal, eager, or none"
    )


# --- Fixture for WebDriver ---
@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("browser")
    headless = request.config.getoption("headless")
    page_load_strategy = request.config.getoption("page_load_strategy")

    with allure.step(
            f"Setting up {browser_name} browser with headless={headless}, page_load_strategy={page_load_strategy}"
    ):
        driver = setup_browser(browser_name, headless, page_load_strategy)

    yield driver
    with allure.step("Quitting the browser"):
        driver.quit()


# --- Hook for capturing screenshot on failure ---
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_exception_interact(node, call, report):
    driver = node.funcargs.get('driver')
    if driver and report.failed:
        with allure.step("Taking screenshot on failure"):
            screenshot = driver.get_screenshot_as_png()
            allure.attach(screenshot, name="Failure Screenshot", attachment_type=allure.attachment_type.PNG)
    yield


# --- Hook for creating environment.properties ---
@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    create_environment_properties(session.config)


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
    with allure.step("Starting Chrome browser for the test"):
        options = webdriver.ChromeOptions()
        options.page_load_strategy = page_load_strategy
        options.add_argument(f"--user-agent={get_user_agent()}")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("prefs", {"download.default_directory": get_download_directory()})

        if headless:
            with allure.step("Applying headless options for Chrome"):
                apply_headless_options(options)

        return webdriver.Chrome(options=options)


# --- Options for Firefox ---
def setup_firefox(headless, page_load_strategy):
    with allure.step("Starting Firefox browser for the test"):
        options = webdriver.FirefoxOptions()
        options.page_load_strategy = page_load_strategy
        set_firefox_preferences(options)

        if headless:
            with allure.step("Applying headless options for Firefox"):
                apply_headless_options(options)

        return webdriver.Firefox(options=options)


# --- General support functions ---
def get_user_agent():
    return (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    )


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


# --- Function to create environment.properties ---
def create_environment_properties(config):
    browser_name = config.getoption("browser")
    headless = config.getoption("headless")
    page_load_strategy = config.getoption("page_load_strategy")

    environment_data = {
        "OS": platform.system(),
        "OS.Version": platform.version(),
        "Python.Version": platform.python_version(),
        "Browser": browser_name,
        "Headless": str(headless),
        "Page.Load.Strategy": page_load_strategy,
        "Docker": str(is_running_in_docker()),
    }

    properties_file = os.path.join(os.getcwd(), "allure-results/environment.properties")
    os.makedirs(os.path.dirname(properties_file), exist_ok=True)

    with open(properties_file, 'w') as f:
        for key, value in environment_data.items():
            f.write(f"{key}={value}\n")


# --- Utility function to detect Docker environment ---
def is_running_in_docker():
    """Detect if the tests are running inside a Docker container."""
    path = '/proc/self/cgroup'
    return (
            os.path.exists('/.dockerenv') or
            (os.path.isfile(path) and any('docker' in line for line in open(path)))
    )
