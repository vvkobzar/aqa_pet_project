from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.PAGE_URL)

    def element_is_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def elements_is_not_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element).perform()

    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element).perform()

    def get_list_windows_handles(self):
        return self.driver.window_handles

    def get_current_window_handle(self):
        return self.driver.current_window_handle

    def get_url_page(self):
        return self.driver.current_url

    def switch_to_new_windows(self, page):
        self.driver.switch_to.window(page)

    def alert_is_present(self, timeout=6):
        return wait(self.driver, timeout).until(EC.alert_is_present())
