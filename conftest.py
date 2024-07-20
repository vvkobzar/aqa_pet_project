import os

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


preferences = {
    "download.default_directory": os.path.join(os.getcwd(), "downloads")
}
options = Options()
options.add_experimental_option("prefs", preferences)
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")
service = Service(ChromeDriverManager().install())


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
