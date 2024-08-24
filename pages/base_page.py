import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        with allure.step(f"Open page with URL: {self.PAGE_URL}"):
            self.driver.get(self.PAGE_URL)

    @allure.step("Wait for element to be visible")
    def element_is_visible(self, locator, timeout=5):
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Wait for all elements to be visible")
    def elements_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    @allure.step("Wait for element to be present")
    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step("Wait for all elements to be present")
    def elements_are_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    @allure.step("Wait for element to be not visible")
    def elements_is_not_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step("Wait for element to be clickable")
    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step("Scrolling to element")
    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Double-click on element")
    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element).perform()

    @allure.step("Right-click on element")
    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element).perform()

    @allure.step("Drag and drop element by offset")
    def action_drag_and_drop_by_offset(self, element, x_coords, y_coords):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_coords, y_coords)
        action.perform()

    @allure.step("Drag and drop to element")
    def action_drag_and_drop_to_element(self, what, where):
        action = ActionChains(self.driver)
        action.drag_and_drop(what, where)
        action.perform()

    @allure.step("Move to element")
    def action_move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    @allure.step("Select option by value: '{value}'")
    def select_by_value(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_value(str(value))

    @allure.step("Select option by visible text: '{text}'")
    def select_by_text(self, element, text):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(text)

    @allure.step("Get all selected options")
    def get_all_selected_options(self, element):
        select = Select(self.element_is_present(element))
        return select.all_selected_options

    @allure.step("Get list of window handles")
    def get_list_windows_handles(self):
        return self.driver.window_handles

    @allure.step("Get current window handle")
    def get_current_window_handle(self):
        return self.driver.current_window_handle

    @allure.step("Get current URL of the page")
    def get_url_page(self):
        return self.driver.current_url

    @allure.step("Switch to new window")
    def switch_to_new_windows(self, page):
        self.driver.switch_to.window(page)

    @allure.step("Check if alert is present")
    def alert_is_present(self, timeout=6):
        return wait(self.driver, timeout).until(EC.alert_is_present())

    @allure.step("Switch to iframe")
    def switch_to_frame(self, iframe):
        self.driver.switch_to.frame(iframe)
