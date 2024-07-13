import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(ChromeDriverManager().install())


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()
